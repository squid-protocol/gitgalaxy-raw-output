# ARCHITECTURAL_BRIEF: three.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mrdoob/three.js.git` |
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
- **Scope:** 2770 analyzed artifact(s), 472165 LOC.
- **Load-bearing artifact:** `manual/resources/lang.css` -- 290 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `examples/jsm/Addons.js` -- pulls in 257 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `examples/jsm/libs/lottie_canvas.module.js` at magnitude 17618.3 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 2770 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3091 |
| Total LOC | 472165 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 47.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6977 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2946 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6805 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 90 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 1537 | 257367 | 55.5% |
| HTML | 1039 | 209167 | 37.5% |
| XML | 76 | 19 | 2.7% |
| PLAINTEXT | 36 | 6 | 1.3% |
| JSON | 28 | 2230 | 1.0% |
| MARKDOWN | 24 | 0 | 0.9% |
| CSS | 20 | 2841 | 0.7% |
| YAML | 10 | 535 | 0.4% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2752 |
| utf-8 | bom | 12 |
| unknown | unknown | 6 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Declarative / Non-Code 16%, Large Core Modules (3) 10%, Large Core Modules (2) 6%, Parameter Forwarders Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2673 | 96.5% |
| Unknown | 6 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 54 | 1.9% |
| Static: Minified & Vendor Opaque Mass | 37 | 1.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3091*

**Composition by Extension & Reason:**
- `.jpg`: 821x Excluded (Explicitly Denied Extension: '.jpg'), 7x Excluded (Explicitly Denied Extension: '.JPG')
- `.html`: 779x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 66 exceeds 500 chars), 1x Excluded (Saturation: Line 57 exceeds 500 chars)
- `.md`: 779x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 204x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.glb`: 45x Excluded (Unsupported Extension: '.glb')
- `.js`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 1 exceeds 500 chars), 2x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.mtlx`: 20x Excluded (Unsupported Extension: '.mtlx')
- `.ktx2`: 19x Excluded (Unsupported Extension: '.ktx2')
- `.pdb`: 18x Excluded (Unsupported Extension: '.pdb')
- `.hdr`: 18x Excluded (Unsupported Extension: '.hdr')
- `.bin`: 15x Excluded (Unsupported Extension: '.bin'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gltf`: 16x Excluded (Explicitly Denied Extension: '.gltf')
- `.mpd`: 16x Excluded (Unsupported Extension: '.mpd')
- `.wrl`: 15x Excluded (Unsupported Extension: '.wrl')
- `.tmpl`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 25.6 | 16.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 49.3 | 56.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.0 | 6.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.5 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.5 | 22.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 97.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 228 | 88 | 0 | `examples/jsm/controls/ArcballControls.js` |
| cleanup | 1059 | 351 | 1 | `src/renderers/common/Renderer.js` |
| guards | 18553 | 1658 | 10 | `examples/jsm/libs/ammo.wasm.js` |
| danger | 6625 | 946 | 4 | `editor/js/libs/codemirror/codemirror.js` |
| concurrency | 2266 | 519 | 2 | `examples/jsm/loaders/GLTFLoader.js` |
| connectivity | 14324 | 2536 | 8 | `examples/jsm/libs/ammo.wasm.js` |
| io | 18298 | 932 | 10 | `manual/ko/fundamentals.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 83 | 20 | 0 | `examples/jsm/libs/lottie_canvas.module.js` |
| time | 386 | 208 | 0 | `editor/js/libs/codemirror/codemirror.js` |
| serialization | 156 | 52 | 0 | `test/unit/src/math/Interpolant.tests.js` |
| regex | 822 | 153 | 0 | `editor/js/libs/esprima.js` |
| events | 5180 | 1226 | 5 | `editor/js/libs/tern-threejs/threejs.js` |
| tests | 4280 | 220 | 0 | `test/unit/src/math/Vector3.tests.js` |
| docs | 11480 | 1960 | 10 | `examples/jsm/libs/opentype.module.js` |
| debt | 1828 | 453 | 1 | `examples/jsm/libs/opentype.module.js` |
| mutation | 194640 | 2484 | 142 | `examples/jsm/libs/lottie_canvas.module.js` |
| dead_code | 904 | 219 | 0 | `examples/jsm/loaders/TDSLoader.js` |
| credential | 52 | 27 | 0 | `examples/jsm/libs/opentype.module.js` |
| threat | 560 | 308 | 1 | `manual/en/textures.html` |
| ml_ai | 1110 | 432 | 1 | `examples/webgl_multiple_elements_text.html` |
| ui | 3343 | 876 | 4 | `files/main.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `manual/ko/fundamentals.html` (Hits: 193)
- `manual/en/game.html` (Hits: 167)
- `manual/zh/game.html` (Hits: 167)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lang.css** (`manual/resources/lang.css`) — 290 inbound connections
2. **lesson.css** (`manual/resources/lesson.css`) — 290 inbound connections
3. **lesson.js** (`manual/resources/lesson.js`) — 290 inbound connections
4. **prettify.js** (`manual/resources/prettify.js`) — 290 inbound connections
5. **constants.js** (`src/constants.js`) — 152 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Addons.js** (`examples/jsm/Addons.js`) — 257 outbound dependencies
2. **Three.Core.js** (`src/Three.Core.js`) — 161 outbound dependencies
3. **Nodes.js** (`src/nodes/Nodes.js`) — 139 outbound dependencies
4. **TSL.js** (`src/nodes/TSL.js`) — 136 outbound dependencies
5. **ShaderChunk.js** (`src/renderers/shaders/ShaderChunk.js`) — 124 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `WebGLTextures` **(Many-Argument Workhorses)** (@ `src/renderers/webgl/WebGLTextures.js`) -> Impact: **1592.7** | LOC: 2438
- `constructor` **(Many-Argument Workhorses)** (@ `src/renderers/WebGLRenderer.js`) -> Impact: **891.9** | LOC: 3441
  * *Intent:* /** * Constructs a new WebGL renderer. * */
- `parse` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/VRMLLoader.js`) -> Impact: **765.0** | LOC: 3245
  * *Intent:* /** * Parses the given VRML data and returns the resulting scene. * */
- `parse` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/EXRLoader.js`) -> Impact: **741.5** | LOC: 3233
  * *Intent:* /** * Parses the given EXR texture data. * */
- `createVisitor` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/VRMLLoader.js`) -> Impact: **637.4** | LOC: 3075
- `parse` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/SVGLoader.js`) -> Impact: **511.2** | LOC: 1852
  * *Intent:* /** * Parses the given SVG data and returns the resulting data. * * SVG XML document. */
- `WebGLProgram` **(Many-Argument Workhorses)** (@ `src/renderers/webgl/WebGLProgram.js`) -> Impact: **453.4** | LOC: 615
- `WebGLPrograms` **(Many-Argument Workhorses)** (@ `src/renderers/webgl/WebGLPrograms.js`) -> Impact: **432.3** | LOC: 655
- `setProgram` **(Many-Argument Workhorses)** (@ `src/renderers/WebGLRenderer.js`) -> Impact: **374.1** | LOC: 428
- `parse` **(Many-Argument Workhorses)** (@ `examples/jsm/loaders/VTKLoader.js`) -> Impact: **319.8** | LOC: 1192
  * *Intent:* /** * Parses the given VTK data and returns the resulting geometry. * */

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `examples/jsm/libs` | 14 | 56549.64 | 71.17% | 0.0% |
| `examples` | 575 | 46452.17 | 41.53% | 0.0% |
| `examples/jsm/loaders` | 48 | 31732.34 | 52.91% | 0.0% |
| `manual/examples/resources/data/gpw` | 7 | 30001.0 | 0.0% | 0.0% |
| `manual/examples` | 177 | 14249.04 | 38.61% | 0.0% |
| `manual/en` | 59 | 13906.53 | 0.17% | 2.96% |
| `src/renderers/webgl` | 30 | 12417.36 | 64.28% | 2.05% |
| `editor/js/libs/codemirror` | 2 | 11319.47 | 46.04% | 5.04% |
| `manual/fr` | 54 | 9583.0 | 0.09% | 1.64% |
| `manual/zh` | 59 | 9217.74 | 0.17% | 2.52% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/renderers/common/nodes/NodeUniform.js` -> **100.0%** Exposure
- `editor/js/libs/ui.js` -> **99.8325%** Exposure
- `.github/workflows/ci.yml` -> **99.5664%** Exposure
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **98.5819%** Exposure
- `src/renderers/common/nodes/NodeBuilderState.js` -> **97.0688%** Exposure
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

### Credential Material (formerly Hardcoded Payload Artifacts)
- `examples/webgl_loader_3dtiles.html` -> **96.9895%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `48` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1264` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `examples/jsm/libs/lottie_canvas.module.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.572)
- **Top Global Matches:** file_cluster_4: 8.572, file_cluster_15: 12.165, file_cluster_12: 12.848
- **Magnitude:** 17618.3 | **LOC:** 14850 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.35; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (96.1%), Guard Balance (formerly Safety Score) (75.9%), Connectivity (formerly Api Exposure) (42.1%), Concurrency Surface (formerly Concurrency) (15.2%)
- **Documentation Coverage:** 98.8024% of unit weight undocumented
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
* *Structure:* `branch: 3176`, `structural_boundaries: 2639`, `args: 957`, `func_start: 867`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 3797`, `dead_code: 65`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 21`
* *Architecture:* `io: 12`, `api: 34`, `concurrency: 22`
* *Defense:* `safety: 875`, `doc: 13`, `sync_locks: 10`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.35
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000482
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/libs/ammo.wasm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 18.151)
- **Top Global Matches:** file_cluster_7: 18.151, file_cluster_12: 18.986, file_cluster_5: 19.089
- **Magnitude:** 13962.08 | **LOC:** 823 | **CtrlFlow:** 283.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 1.153; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Concurrency Surface (formerly Concurrency) (61.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreatePatchUV` **(Defensive Guards)** (Impact: 66.4)
  * `xB` **(Compute Cores)** (Impact: 60.1)
  * `CreatePatch` **(Defensive Guards)** (Impact: 60.1)
  * `CB` **(Defensive Guards)** (Impact: 56.6)
  * `addSingleResult` **(Defensive Guards)** (Impact: 42.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1583 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 5125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2306`, `structural_boundaries: 2589`, `args: 2735`, `func_start: 2701`
* *Risk/State:* `safety_bypasses: 98`, `state_mutation: 1959`, `planned_debt: 7`
* *Architecture:* `io: 10`, `api: 1512`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 2213`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002167
  * `Imports (Out-Degree: 0):` fs, path
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `editor/js/libs/codemirror/codemirror.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.523)
- **Top Global Matches:** file_cluster_7: 11.523, file_cluster_12: 11.728, file_cluster_5: 12.66
- **Magnitude:** 11318.96 | **LOC:** 9850 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.195; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.3%), Guard Balance (formerly Safety Score) (85.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchKey` **(Many-Argument Workhorses)** (Impact: 122.3)
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
* *Amplified Cascading Flux:* 1411 instances
* *Concurrency (weighted view):* 136
* *State Mutation (weighted view):* 4883
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2603`, `structural_boundaries: 2362`, `args: 968`, `func_start: 735`
* *Risk/State:* `safety_bypasses: 802`, `state_mutation: 2061`, `planned_debt: 1`, `fragile_debt: 16`
* *Architecture:* `api: 42`, `concurrency: 31`
* *Defense:* `safety: 115`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.195
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000361
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/libs/opentype.module.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.709)
- **Top Global Matches:** file_cluster_4: 9.709, file_cluster_15: 9.742, file_cluster_12: 10.681
- **Magnitude:** 10980.76 | **LOC:** 14507 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.35; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.0%), Connectivity (formerly Api Exposure) (58.8%), Complexity Load (formerly Cognitive Load) (58.5%), Concurrency Surface (formerly Concurrency) (12.4%)
- **Documentation Coverage:** 55.6164% of unit weight undocumented
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
* *Amplified Cascading Flux:* 1807 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 6054
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1741`, `structural_boundaries: 2599`, `args: 697`, `func_start: 635`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 2440`, `dead_code: 3`, `planned_debt: 27`, `fragile_debt: 5`
* *Architecture:* `io: 1`, `api: 140`, `concurrency: 1`
* *Defense:* `safety: 448`, `doc: 285`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.35
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000482
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/libs/utif.module.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 18.147)
- **Top Global Matches:** file_cluster_6: 18.147, file_cluster_4: 19.988, file_cluster_14: 20.378
- **Magnitude:** 7889.32 | **LOC:** 1665 | **CtrlFlow:** 88.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.35; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (100.0%), Complexity Load (formerly Cognitive Load) (98.3%), Connectivity (formerly Api Exposure) (24.7%), Dead Code Surface (formerly Dead Code) (13.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `a7` **(Defensive Guards)** (Impact: 262.3)
  * `ag` **(Defensive Guards)** (Impact: 249.9)
    * *Intent:* // Following lines add a JPEG decoder to UTIF.JpegDecoder
  * `av` **(Compute Cores)** (Impact: 220.6)
  * `_decompress` **(Many-Argument Workhorses)** (Impact: 207.2)
  * `_readIFD` **(Many-Argument Workhorses)** (Impact: 186.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1373 instances
* *State Mutation (weighted view):* 4318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1237`, `structural_boundaries: 847`, `args: 159`, `func_start: 150`
* *Risk/State:* `safety_bypasses: 407`, `state_mutation: 1572`, `dead_code: 40`
* *Architecture:* `io: 1`, `api: 4`
* *Defense:* `safety: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.35
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000482
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `editor/js/libs/esprima.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.336)
- **Top Global Matches:** file_cluster_4: 7.336, file_cluster_6: 11.407, file_cluster_10: 12.206
- **Magnitude:** 5867.38 | **LOC:** 6401 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.195; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.4%), Guard Balance (formerly Safety Score) (68.1%), Connectivity (formerly Api Exposure) (62.2%)
- **Documentation Coverage:** 98.1763% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseForStatement` **(I/O & Config Routines)** (Impact: 55.3)
    * *Intent:* // ECMA-262 13.7.4 The for Statement // ECMA-262 13.7.5 The for-in and for-of Statements
  * `isKeyword` **(Defensive Guards)** (Impact: 55.1)
    * *Intent:* ; // ECMA-262 11.6.2.1 Keywords
  * `scanPunctuator` **(Defensive Guards)** (Impact: 54.0)
    * *Intent:* ; // ECMA-262 11.7 Punctuators
  * `parseClassElement` **(Defensive Guards)** (Impact: 50.7)
    * *Intent:* // ECMA-262 14.5 Class Definitions
  * `parseObjectProperty` **(Defensive Guards)** (Impact: 45.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 897 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 3266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1396`, `structural_boundaries: 1305`, `args: 407`, `func_start: 298`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 8`, `state_mutation: 1472`, `dead_code: 6`
* *Architecture:* `api: 119`, `concurrency: 2`
* *Defense:* `safety: 499`, `doc: 65`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.195
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000361
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014bt_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014bt_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014ft_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014ft_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014mt_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014mt_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/acorn/acorn.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.073)
- **Top Global Matches:** file_cluster_4: 8.073, file_cluster_6: 11.168, file_cluster_12: 12.023
- **Magnitude:** 3616.26 | **LOC:** 3236 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.195; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseObj` **(Defensive Guards)** (Impact: 77.2)
    * *Intent:* // Parse an object literal or binding pattern.
  * `getTokenFromCode` **(Compute Cores)** (Impact: 71.2)
  * `parseStatement` **(Compute Cores)** (Impact: 65.6)
    * *Intent:* // Parse a single statement. // // If expecting a statement and finding a slash operator, parse a //...
  * `parseClass` **(Defensive Guards)** (Impact: 47.0)
    * *Intent:* // Parse a class declaration or literal (depending on the // `isStatement` parameter).
  * `checkLVal` **(Compute Cores)** (Impact: 43.9)
    * *Intent:* // Verify that a node is an lval — something that can be assigned // to.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 611 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 1923
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 850`, `structural_boundaries: 655`, `args: 186`, `func_start: 167`
* *Risk/State:* `safety_bypasses: 47`, `high_risk_execution: 2`, `state_mutation: 701`, `fragile_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `api: 53`, `concurrency: 1`, `import: 43`
* *Defense:* `safety: 251`, `test: 34`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.195
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000361
  * `Imports (Out-Degree: 0):` expression, identifier, location, lval, node, options, parseutil, state...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/renderers/webgl/WebGLTextures.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.098)
- **Top Global Matches:** file_cluster_8: 7.098, file_cluster_6: 11.797, file_cluster_4: 20.14
- **Magnitude:** 3378.84 | **LOC:** 2447 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WebGLTextures` **(Many-Argument Workhorses)** (Impact: 1592.7)
  * `uploadTexture` **(Many-Argument Workhorses)** (Impact: 220.0)
  * `getInternalFormat` **(Many-Argument Workhorses)** (Impact: 202.0)
  * `uploadCubeTexture` **(Many-Argument Workhorses)** (Impact: 117.8)
  * `setupRenderTarget` **(Compute Cores)** (Impact: 75.4)
    * *Intent:* // Set up GL resources for the render target
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 186 instances
* *State Mutation (weighted view):* 590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 519`, `structural_boundaries: 105`, `args: 45`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 218`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 212`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000542
  * `Imports (Out-Degree: 5):` constants.js, TextureUtils.js, ColorManagement.js, Vector2.js, utils.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/EXRLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.718)
- **Top Global Matches:** file_cluster_4: 6.718, file_cluster_6: 10.937, file_cluster_12: 11.604
- **Magnitude:** 3342.08 | **LOC:** 3434 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 0.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (88.7%), Guard Balance (formerly Safety Score) (81.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.2%), Connectivity (formerly Api Exposure) (31.2%)
- **Documentation Coverage:** 84.375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 741.5)
    * *Intent:* /** * Parses the given EXR texture data. * */
  * `setupDecoder` **(Many-Argument Workhorses)** (Impact: 235.2)
  * `parseValue` **(Many-Argument Workhorses)** (Impact: 89.3)
  * `lossyDctDecode` **(Many-Argument Workhorses)** (Impact: 63.6)
  * `uncompressB44` **(Compute Cores)** (Impact: 55.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 423 instances
* *State Mutation (weighted view):* 1445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 290`, `args: 80`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 599`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 52`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.445
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.003104
  * `Imports (Out-Degree: 2):` fflate.module.js, three
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/VRMLLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.998)
- **Top Global Matches:** file_cluster_4: 6.998, file_cluster_6: 7.302, file_cluster_15: 14.395
- **Magnitude:** 3197.74 | **LOC:** 3647 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.196; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (88.0%), Guard Balance (formerly Safety Score) (68.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.2%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 91.0714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 765.0)
    * *Intent:* /** * Parses the given VRML data and returns the resulting scene. * */
  * `createVisitor` **(Many-Argument Workhorses)** (Impact: 637.4)
  * `buildIndexedFaceSetNode` **(Compute Cores)** (Impact: 80.9)
  * `buildElevationGridNode` **(Compute Cores)** (Impact: 77.6)
  * `buildExtrusionNode` **(Compute Cores)** (Impact: 70.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 296 instances
* *State Mutation (weighted view):* 980
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 365`, `args: 100`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `state_mutation: 388`, `dead_code: 3`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 80`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.196
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000813
  * `Imports (Out-Degree: 2):` chevrotain.module.min.js, three
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/jsm/libs/fflate.module.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.337)
- **Top Global Matches:** file_cluster_4: 10.337, file_cluster_12: 10.448, file_cluster_7: 11.47
- **Magnitude:** 3186.56 | **LOC:** 2673 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); blast radius 1.602; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.0%), Connectivity (formerly Api Exposure) (73.8%), Complexity Load (formerly Cognitive Load) (67.9%), Concurrency Surface (formerly Concurrency) (59.2%)
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
* *Amplified Cascading Flux:* 447 instances
* *Concurrency (weighted view):* 65
* *State Mutation (weighted view):* 1428
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 580`, `structural_boundaries: 662`, `args: 238`, `func_start: 171`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 534`, `planned_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 48`, `concurrency: 15`
* *Defense:* `safety: 33`, `doc: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0057
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/renderers/WebGLRenderer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.909)
- **Top Global Matches:** file_cluster_4: 8.909, file_cluster_6: 8.989, file_cluster_15: 15.715
- **Magnitude:** 3180.26 | **LOC:** 3639 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 0.211; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%)
- **Documentation Coverage:** 29.3578% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 891.9)
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
* *Structure:* `branch: 508`, `structural_boundaries: 153`, `args: 83`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 378`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 31`, `concurrency: 5`, `import: 37`
* *Defense:* `safety: 204`, `doc: 78`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.000482
  * `Imports (Out-Degree: 37):` constants.js, Color.js, ColorManagement.js, Frustum.js, Matrix4.js, Vector3.js, Vector4.js, utils.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/usd/USDComposer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.008)
- **Top Global Matches:** file_cluster_8: 6.008, file_cluster_6: 13.115, file_cluster_4: 21.763
- **Magnitude:** 3102.36 | **LOC:** 4595 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 48.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (98.0%), Complexity Load (formerly Cognitive Load) (72.2%), Guard Balance (formerly Safety Score) (62.9%), Connectivity (formerly Api Exposure) (24.2%)
- **Documentation Coverage:** 61.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_buildGeometryWithSubsets` **(Many-Argument Workhorses)** (Impact: 184.6)
  * `applyTransform` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* /** * Apply USD transforms to a Three.js object. * Handles xformOpOrder with proper matrix compositi...
  * `_buildGeometry` **(Many-Argument Workhorses)** (Impact: 111.2)
  * `_buildHierarchy` **(Many-Argument Workhorses)** (Impact: 95.6)
    * *Intent:* /** * Build the scene hierarchy recursively. * Uses childrenByPath index for O(1) child lookup inste...
  * `_applyPreviewSurface` **(Many-Argument Workhorses)** (Impact: 75.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 387 instances
* *State Mutation (weighted view):* 1202
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 880`, `structural_boundaries: 282`, `args: 84`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `state_mutation: 428`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 257`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001083
  * `Imports (Out-Degree: 1):` three
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/SVGLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.544)
- **Top Global Matches:** file_cluster_6: 5.544, file_cluster_4: 11.494, file_cluster_8: 13.516
- **Magnitude:** 2945.78 | **LOC:** 3268 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.196; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (87.8%), Guard Balance (formerly Safety Score) (69.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.3%), Connectivity (formerly Api Exposure) (27.4%)
- **Documentation Coverage:** 73.5294% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 357`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 130`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.196
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000813
  * `Imports (Out-Degree: 1):` three
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/GLTFLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.36)
- **Top Global Matches:** file_cluster_4: 6.36, file_cluster_6: 10.214, file_cluster_15: 11.919
- **Magnitude:** 2903.46 | **LOC:** 4861 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 0.657; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (68.8%), Guard Balance (formerly Safety Score) (61.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.5%)
- **Documentation Coverage:** 53.5211% of unit weight undocumented
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
* *Structure:* `branch: 576`, `structural_boundaries: 344`, `args: 207`, `func_start: 129`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 429`, `planned_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `api: 7`, `concurrency: 95`, `import: 3`
* *Defense:* `safety: 247`, `doc: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.657
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003599
  * `Imports (Out-Degree: 4):` BufferGeometryUtils.js, SkeletonUtils.js, three
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/FBXLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.044)
- **Top Global Matches:** file_cluster_4: 6.044, file_cluster_6: 10.432, file_cluster_15: 11.687
- **Magnitude:** 2792.72 | **LOC:** 4463 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.196; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (71.9%), Guard Balance (formerly Safety Score) (67.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.3%), Connectivity (formerly Api Exposure) (14.9%)
- **Documentation Coverage:** 97.3684% of unit weight undocumented
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
* *Structure:* `branch: 601`, `structural_boundaries: 296`, `args: 163`, `func_start: 112`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 511`, `dead_code: 2`, `planned_debt: 5`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 216`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.196
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000813
  * `Imports (Out-Degree: 5):` NURBSCurve.js, fflate.module.js, three
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/jsm/exporters/GLTFExporter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.653)
- **Top Global Matches:** file_cluster_4: 6.653, file_cluster_6: 8.865, file_cluster_15: 13.374
- **Magnitude:** 2668.52 | **LOC:** 3739 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.215; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (71.3%), Complexity Load (formerly Cognitive Load) (68.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.8%)
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
  * `processMaterialAsync` **(Compute Cores)** (Impact: 45.3)
    * *Intent:* /** * Process material */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 372 instances
* *Concurrency (weighted view):* 318
* *State Mutation (weighted view):* 1208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 234`, `args: 109`, `func_start: 82`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 464`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 6`, `concurrency: 78`, `import: 1`
* *Defense:* `safety: 174`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.215
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000813
  * `Imports (Out-Degree: 2):` three
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `editor/js/libs/ternjs/infer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.224)
- **Top Global Matches:** file_cluster_7: 9.224, file_cluster_12: 9.65, file_cluster_5: 10.774
- **Magnitude:** 2080.64 | **LOC:** 1636 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.361; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (80.0%)
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
* *Structure:* `branch: 547`, `structural_boundaries: 515`, `args: 233`, `func_start: 195`
* *Risk/State:* `safety_bypasses: 121`, `state_mutation: 293`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 52`, `import: 5`
* *Defense:* `safety: 54`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001083
  * `Imports (Out-Degree: 2):` def, signal, acorn, acorn_loose, walk
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/collada/ColladaComposer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.64)
- **Top Global Matches:** file_cluster_4: 5.64, file_cluster_6: 9.06, file_cluster_15: 12.306
- **Magnitude:** 2040.92 | **LOC:** 3045 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.248; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (77.8%), Guard Balance (formerly Safety Score) (68.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.1%), Connectivity (formerly Api Exposure) (25.4%)
- **Documentation Coverage:** 98.1481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildMaterial` **(Compute Cores)** (Impact: 108.0)
  * `buildGeometryType` **(Many-Argument Workhorses)** (Impact: 94.0)
  * `buildGeometryData` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `setJointValue` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `buildObjects` **(Many-Argument Workhorses)** (Impact: 39.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 275 instances
* *State Mutation (weighted view):* 871
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 255`, `args: 84`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 321`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 99`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.248
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000903
  * `Imports (Out-Degree: 2):` ColladaParser.js, three
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `examples/webgl_loader_stl.html` (HTML) | Magnitude: 72.8 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 132, state_mutation: 53, core_var_decl: 29, design_snake_case: 25
- `examples/webgpu_compute_points.html` (HTML) | Magnitude: 44.56 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 111, core_var_decl: 42, design_snake_case: 25, state_mutation: 20
- `editor/js/libs/app.js` (JAVASCRIPT) | Magnitude: 207.66 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 160, state_mutation: 39, core_var_decl: 24, branch: 20
- `examples/webgpu_display_stereo.html` (HTML) | Magnitude: 103.2 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 162, state_mutation: 52, core_var_decl: 34, design_snake_case: 27
- `examples/jsm/libs/mikktspace.module.js` (JAVASCRIPT) | Magnitude: 81.62 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 39, core_var_decl: 34, design_snake_case: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/jsm/misc/Gyroscope.js` (JAVASCRIPT) | Magnitude: 25.8 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 24, core_var_decl: 8, branch: 6, structural_boundaries: 6
- `editor/js/commands/SetShadowValueCommand.js` (JAVASCRIPT) | Magnitude: 48.8 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 18, structural_boundaries: 8, api: 7
- `editor/js/commands/SetColorCommand.js` (JAVASCRIPT) | Magnitude: 46.8 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 16, structural_boundaries: 8, api: 7
- `.github/workflows/report-size.yml` (YAML) | Magnitude: 17.02 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 222, globals: 157, debug_prints: 61, core_var_decl: 53
- `src/materials/nodes/PointsNodeMaterial.js` (JAVASCRIPT) | Magnitude: 67.78 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 58, structural_boundaries: 25, core_var_decl: 16, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `manual/zh/transparency.html` (HTML) | Magnitude: 131.48 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 137, decorators: 123, core_var_decl: 113, design_snake_case: 112
- `examples/webxr_vr_handinput_pointerdrag.html` (HTML) | Magnitude: 227.42 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 394, state_mutation: 100, core_var_decl: 79, structural_boundaries: 57
- `manual/ru/responsive.html` (HTML) | Magnitude: 73.4 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: decorators: 99, structural_boundaries: 84, core_var_decl: 76, design_snake_case: 73
- `examples/jsm/shaders/BokehShader2.js` (JAVASCRIPT) | Magnitude: 79.36 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 261, core_var_decl: 84, design_snake_case: 68, state_mutation: 58
- `examples/webgl_postprocessing_pixel.html` (HTML) | Magnitude: 100.46 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 186, state_mutation: 60, core_var_decl: 58, design_camel_case: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/webgpu_lensflares.html` (HTML) | Magnitude: 50.48 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 116, state_mutation: 31, core_var_decl: 29, design_snake_case: 25
- `examples/webgl_materials_texture_filters.html` (HTML) | Magnitude: 70.42 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 158, state_mutation: 54, core_var_decl: 54, design_snake_case: 32
- `examples/webgpu_materials_basic.html` (HTML) | Magnitude: 62.14 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 114, core_var_decl: 36, state_mutation: 32, design_snake_case: 27
- `examples/webgpu_reflection_roughness.html` (HTML) | Magnitude: 48.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 111, state_mutation: 33, core_var_decl: 26, design_snake_case: 20
- `examples/webgpu_materials_toon.html` (HTML) | Magnitude: 68.18 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 126, core_var_decl: 38, state_mutation: 31, design_snake_case: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `examples/jsm/shaders/MirrorShader.js` (JAVASCRIPT) | Magnitude: 23.64 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 29, state_mutation: 7, safety_bypasses: 6, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `editor/js/commands/SetValueCommand.js` (JAVASCRIPT) | Magnitude: 49.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 18, structural_boundaries: 8, api: 7
- `editor/js/Sidebar.Geometry.ShapeGeometry.js` (JAVASCRIPT) | Magnitude: 23.22 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 35, core_var_decl: 9, design_snake_case: 7, structural_boundaries: 5
- `src/textures/CompressedArrayTexture.js` (JAVASCRIPT) | Magnitude: 17.76 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 13, doc: 8, structural_boundaries: 6, state_mutation: 6
- `src/materials/nodes/MeshSSSNodeMaterial.js` (JAVASCRIPT) | Magnitude: 37.44 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 42, structural_boundaries: 18, state_mutation: 15, doc: 14
- `manual/examples/load-gltf-rotate-cars-fixed.html` (HTML) | Magnitude: 74.6 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 117, core_var_decl: 47, design_snake_case: 35, state_mutation: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `examples/jsm/libs/demuxer_mp4.js` (JAVASCRIPT) | Magnitude: 34.2 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 70, encapsulation: 10, args: 9, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/renderers/webgpu/nodes/StandardNodeLibrary.js` (JAVASCRIPT) | Magnitude: 5.4 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 30, import: 26, dead_code: 4
- `src/Three.WebGPU.js` (JAVASCRIPT) | Magnitude: 49.72 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 36, api: 34, import: 34, branch: 28
- `src/renderers/webgpu/nodes/BasicNodeLibrary.js` (JAVASCRIPT) | Magnitude: 4.88 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 27, structural_boundaries: 17, import: 13, api: 2
- `src/Three.WebGPU.Nodes.js` (JAVASCRIPT) | Magnitude: 43.6 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 30, api: 28, import: 28, branch: 22
- `src/nodes/TSL.js` (JAVASCRIPT) | Magnitude: 153.72 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 136, api: 136, import: 136, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `manual/examples/billboard-labels-w-sprites-adjust-height.html` (HTML) | Magnitude: 67.46 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 111, core_var_decl: 48, design_snake_case: 31, state_mutation: 28
- `manual/examples/billboard-labels-w-sprites.html` (HTML) | Magnitude: 68.58 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 112, core_var_decl: 48, design_snake_case: 31, state_mutation: 29
- `examples/jsm/postprocessing/MaskPass.js` (JAVASCRIPT) | Magnitude: 46.34 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 51, state_mutation: 12, doc: 12, structural_boundaries: 9
- `manual/examples/load-gltf.html` (HTML) | Magnitude: 52.06 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 95, core_var_decl: 42, design_snake_case: 31, indent_spaces: 23
- `manual/examples/load-obj-auto-camera-xz.html` (HTML) | Magnitude: 52.06 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 95, core_var_decl: 41, design_snake_case: 30, indent_spaces: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/jsm/libs/opentype.module.js` (JAVASCRIPT) | Magnitude: 10980.76 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8494, structural_boundaries: 2599, state_mutation: 2440, core_var_decl: 2184
- `editor/js/Sidebar.Material.MapProperty.js` (JAVASCRIPT) | Magnitude: 184.72 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 126, branch: 30, safety: 28, state_mutation: 28
- `src/renderers/WebGLRenderer.js` (JAVASCRIPT) | Magnitude: 3180.26 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1587, branch: 508, core_var_decl: 391, state_mutation: 378
- `examples/physics_rapier_vehicle_controller.html` (HTML) | Magnitude: 197.98 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 238, state_mutation: 68, core_var_decl: 60, branch: 39
- `examples/jsm/inspector/RendererInspector.js` (JAVASCRIPT) | Magnitude: 306.56 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 224, state_mutation: 73, branch: 43, structural_boundaries: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/renderers/webgl/WebGLOutput.js` (JAVASCRIPT) | Magnitude: 212.78 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 164, core_var_decl: 42, state_mutation: 39, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/unit/src/math/Vector3.tests.js` (JAVASCRIPT) | Magnitude: 57.66 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 569, test: 242, core_var_decl: 129, design_snake_case: 129
- `manual/ko/responsive.html` (HTML) | Magnitude: 73.36 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: decorators: 107, core_var_decl: 81, structural_boundaries: 80, design_snake_case: 78
- `manual/fr/responsive.html` (HTML) | Magnitude: 80.14 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: decorators: 101, structural_boundaries: 80, core_var_decl: 75, design_snake_case: 72
- `test/unit/src/core/EventDispatcher.tests.js` (JAVASCRIPT) | Magnitude: 4.26 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 50, test: 15, safety: 13, structural_boundaries: 10
- `manual/zh/scenegraph.html` (HTML) | Magnitude: 106.26 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: decorators: 254, core_var_decl: 132, structural_boundaries: 116, design_snake_case: 114

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `examples/jsm/math/Octree.js` (JAVASCRIPT) | Magnitude: 413.34 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 344, core_var_decl: 113, design_snake_case: 99, state_mutation: 83

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/renderers/common/Renderer.js` -> Churn: **100.0%** | Cog Load: 51.4654% | Debt: 8.434%
- `examples/jsm/loaders/usd/USDComposer.js` -> Churn: **97.97%** | Cog Load: 72.2356% | Debt: 0.0%
- `src/renderers/WebGLRenderer.js` -> Churn: **94.64%** | Cog Load: 50.2415% | Debt: 7.8039%
- `src/renderers/webgpu/utils/WebGPUTextureUtils.js` -> Churn: **79.62%** | Cog Load: 63.404% | Debt: 8.8445%
- `editor/index.html` -> Churn: **64.6%** | Cog Load: 61.113% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `examples/jsm/loaders/VRMLLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 3197.74
- `examples/jsm/loaders/3DMLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 1473.62
- `examples/jsm/inspector/ui/Profiler.js` -> **sunag** (87.5% isolated ownership) | Magnitude: 1382.22
- `examples/jsm/loaders/VTKLoader.js` -> **mrdoob** (100.0% isolated ownership) | Magnitude: 1324.62
- `examples/jsm/loaders/3MFLoader.js` -> **mrdoob** (100.0% isolated ownership) | Magnitude: 1187.58

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/loaders/ObjectLoader.js` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 100.0%)
- `test/unit/utils/qunit-utils.js` -> **Severity: 0.043** (Bridge: 0.0004 * Flux: 100.0%)
- `src/nodes/tsl/TSLCore.js` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 100.0%)
- `src/materials/nodes/NodeMaterial.js` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 100.0%)
- `src/core/BufferGeometry.js` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/utils.js` -> **Severity: 7.935** (Embedded: 0.1375 * Error Risk: 57.7097%)
- `src/math/Matrix4.js` -> **Severity: 6.584** (Embedded: 0.08 * Error Risk: 82.2951%)
- `manual/resources/prettify.js` -> **Severity: 6.458** (Embedded: 0.1047 * Error Risk: 61.6666%)
- `src/math/Quaternion.js` -> **Severity: 6.375** (Embedded: 0.0782 * Error Risk: 81.4676%)
- `src/math/Vector3.js` -> **Severity: 6.249** (Embedded: 0.0991 * Error Risk: 63.0333%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/nodes/tsl/TSLBase.js` -> **Severity: 773.8** (Blast Radius: 7.738 * Doc Risk: 100.0%)
- `src/nodes/tsl/TSLCore.js` -> **Severity: 646.04** (Blast Radius: 6.849 * Doc Risk: 94.3262%)
- `editor/js/libs/ui.js` -> **Severity: 541.4** (Blast Radius: 5.414 * Doc Risk: 100.0%)
- `editor/js/Command.js` -> **Severity: 447.8** (Blast Radius: 6.717 * Doc Risk: 66.6667%)
- `manual/resources/prettify.js` -> **Severity: 401.0** (Blast Radius: 11.228 * Doc Risk: 35.7143%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 848 literal sites + 5 sites through wrappers = 853
- **`panics_and_aborts`:** 593 literal sites + 7 sites through wrappers = 600

- `throwSyntaxError` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `examples/jsm/loaders/SVGLoader.js`
- `fail` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `examples/jsm/libs/opentype.module.js`
- `printBuffer` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/jsm/loaders/lwo/IFFParser.js`
- `warn` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/jsm/tsl/lighting/data/DirectionalLightDataNode.js`
- `warn` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/jsm/tsl/lighting/data/HemisphereLightDataNode.js`
- `warn` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/jsm/tsl/lighting/data/PointLightDataNode.js`
- `warn` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/jsm/tsl/lighting/data/SpotLightDataNode.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 72565 call pairs -- scoped 19.5%, unique 0.0%, ambiguous 19.7%, external 60.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 42493 | 29.4% | 0.0% | 33.6% | 37.0% |
| html | 30072 | 5.6% | 0.1% | 0.2% | 94.2% |

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
