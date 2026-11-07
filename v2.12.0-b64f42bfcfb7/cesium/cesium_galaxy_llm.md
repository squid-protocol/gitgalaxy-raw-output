# ARCHITECTURAL_BRIEF: cesium
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/CesiumGS/cesium.git` |
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
- **Scope:** 3979 analyzed artifact(s), 686587 LOC.
- **Load-bearing artifact:** `packages/engine/Source/Core/defined.js` -- 690 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/engine/Source/DataSources/CzmlDataSource.js` -- pulls in 93 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/engine/Specs/DataSources/KmlDataSourceSpec.js` at magnitude 59712.57 (structural weight, not risk).
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
| Total Artifacts | 8126 |
| Analyzed Artifacts (Scanned) | 3979 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4147 |
| Total LOC | 686587 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 49.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4902 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2307 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2495 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 116 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 2157 | 587715 | 54.2% |
| HTML | 586 | 55128 | 14.7% |
| JSON | 390 | 22338 | 9.8% |
| GLSL | 316 | 10147 | 7.9% |
| YAML | 302 | 2465 | 7.6% |
| MARKDOWN | 73 | 0 | 1.8% |
| CSS | 59 | 4333 | 1.5% |
| TYPESCRIPT | 45 | 4297 | 1.1% |
| XML | 27 | 0 | 0.7% |
| PLAINTEXT | 19 | 1 | 0.5% |
| PYTHON | 3 | 135 | 0.1% |
| SHELL | 1 | 19 | 0.0% |
| CSV | 1 | 9 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3967 |
| utf-8 | bom | 11 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 21%, Callbacks & Closures Files 14%, Large Core Modules (2) 7%, Large Core Modules (3) 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3856 | 96.9% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 91 | 2.3% |
| Static: Minified & Vendor Opaque Mass | 31 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4147*

**Composition by Extension & Reason:**
- `.js`: 1330x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 7207 commas in 959 LOC)
- `.jpg`: 655x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 569x Excluded (Explicitly Denied Extension: '.png')
- `.css`: 232x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 221x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 71 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 7210 commas in 996 LOC)
- `.b3dm`: 193x Excluded (Unsupported Extension: '.b3dm')
- `.gltf`: 123x Excluded (Explicitly Denied Extension: '.gltf')
- `.gif`: 117x Excluded (Explicitly Denied Extension: '.gif')
- `.bin`: 95x Excluded (Unsupported Extension: '.bin')
- `.geom`: 81x Excluded (Binary Format Detected)
- `.glb`: 78x Excluded (Unsupported Extension: '.glb')
- `.pnts`: 56x Excluded (Unsupported Extension: '.pnts')
- `.vctr`: 50x Excluded (Unsupported Extension: '.vctr')
- `.ttf`: 40x Excluded (Explicitly Denied Extension: '.ttf')
- `no_extension`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.5 | 2.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.5 | 32.1 | 45.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 97.3 | 10.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 28.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 690 | 118 | 0 | `packages/engine/Specs/Scene/MetadataTablePropertySpec.js` |
| cleanup | 1369 | 412 | 1 | `packages/engine/Source/Scene/Scene.js` |
| guards | 13141 | 1504 | 9 | `packages/engine/Source/Scene/Expression.js` |
| danger | 7219 | 1166 | 4 | `packages/engine/Specs/Renderer/AutomaticUniformSpec.js` |
| concurrency | 9275 | 841 | 3 | `packages/engine/Specs/Scene/Model/ModelSpec.js` |
| connectivity | 7725 | 1776 | 7 | `packages/engine/Source/Scene/GlobeSurfaceTileProvider.js` |
| io | 2060 | 410 | 1 | `packages/engine/Specs/Renderer/AutomaticUniformSpec.js` |
| crypto | 1 | 1 | 0 | `packages/sandcastle/scripts/buildGallery.js` |
| ipc | 330 | 18 | 0 | `packages/engine/Specs/DataSources/EntityClusterSpec.js` |
| time | 284 | 98 | 0 | `packages/engine/Specs/Core/JulianDateSpec.js` |
| serialization | 163 | 67 | 0 | `packages/engine/Specs/Core/ITwinPlatformSpec.js` |
| regex | 417 | 102 | 0 | `packages/engine/Source/DataSources/KmlDataSource.js` |
| events | 3244 | 701 | 4 | `packages/engine/Specs/Core/Intersections2DSpec.js` |
| tests | 60042 | 738 | 33 | `packages/engine/Specs/DataSources/CzmlDataSourceSpec.js` |
| docs | 12110 | 1657 | 9 | `packages/engine/Source/Scene/ModelComponents.js` |
| debt | 1501 | 562 | 1 | `Specs/getWebGLStub.js` |
| mutation | 179275 | 3007 | 120 | `packages/engine/Specs/Scene/ExpressionSpec.js` |
| dead_code | 376 | 185 | 0 | `packages/engine/Source/DataSources/CompositeEntityCollection.js` |
| credential | 37 | 19 | 0 | `packages/sandcastle/gallery/panorama/main.js` |
| threat | 22 | 17 | 0 | `packages/engine/Specs/Scene/Cesium3DTilesetSpec.js` |
| ml_ai | 736 | 152 | 0 | `packages/engine/Source/Scene/ScreenSpaceCameraController.js` |
| ui | 1505 | 252 | 0 | `packages/engine/Specs/DataSources/KmlDataSourceSpec.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/engine/Specs/Renderer/AutomaticUniformSpec.js` (Hits: 170)
- `packages/engine/Specs/Renderer/BuiltinFunctionsSpec.js` (Hits: 66)
- `packages/engine/Specs/Renderer/UniformSpec.js` (Hits: 66)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **defined.js** (`packages/engine/Source/Core/defined.js`) — 690 inbound connections
2. **Cartesian3.js** (`packages/engine/Source/Core/Cartesian3.js`) — 375 inbound connections
3. **DeveloperError.js** (`packages/engine/Source/Core/DeveloperError.js`) — 360 inbound connections
4. **Check.js** (`packages/engine/Source/Core/Check.js`) — 324 inbound connections
5. **Sandcastle-header.js** (`Apps/Sandcastle/Sandcastle-header.js`) — 285 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CzmlDataSource.js** (`packages/engine/Source/DataSources/CzmlDataSource.js`) — 93 outbound dependencies
2. **Scene.js** (`packages/engine/Source/Scene/Scene.js`) — 83 outbound dependencies
3. **KmlDataSource.js** (`packages/engine/Source/DataSources/KmlDataSource.js`) — 69 outbound dependencies
4. **Cesium3DTileset.js** (`packages/engine/Source/Scene/Cesium3DTileset.js`) — 65 outbound dependencies
5. **GlobeSurfaceTileProvider.js** (`packages/engine/Source/Scene/GlobeSurfaceTileProvider.js`) — 53 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createPickingSpecs` **(Many-Argument Workhorses)** (@ `packages/engine/Specs/Scene/PickingSpec.js`) -> Impact: **278.0** | LOC: 2619
- `addDrawCommandsForTile` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/GlobeSurfaceTileProvider.js`) -> Impact: **247.2** | LOC: 783
- `createQuadEdgeGeometry` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/Model/EdgeVisibilityPipelineStage.js`) -> Impact: **243.6** | LOC: 460
  * *Intent:* */
- `getShaderExpression` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/Expression.js`) -> Impact: **237.1** | LOC: 262
- `intersectPlaneTestCornersEdgesFaces` **(Many-Argument Workhorses)** (@ `packages/engine/Specs/Core/OrientedBoundingBoxSpec.js`) -> Impact: **210.7** | LOC: 472
- `update` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/BillboardCollection.js`) -> Impact: **189.6** | LOC: 539
  * *Intent:* /** * get the draw commands needed to render this primitive. * <p> * Do not call this function directly. This is documented just to * list the excepti...
- `update` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/VoxelEllipsoidShape.js`) -> Impact: **185.7** | LOC: 480
  * *Intent:* /** * Update the shape's state. */
- `handleZoom` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/ScreenSpaceCameraController.js`) -> Impact: **182.6** | LOC: 425
- `createShaders` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/PointCloud.js`) -> Impact: **171.8** | LOC: 397
- `pickModel` **(Many-Argument Workhorses)** (@ `packages/engine/Source/Scene/Model/pickModel.js`) -> Impact: **166.0** | LOC: 322
  * *Intent:* /** * Find an intersection between a ray and the model surface that was rendered. The ray must be given in world coordinates. * * */

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/engine/Source/Scene` | 376 | 84764.2 | 37.46% | 7.03% |
| `packages/engine/Specs/DataSources` | 92 | 67075.01 | 4.28% | 0.0% |
| `packages/engine/Source/Core` | 291 | 54615.3 | 32.58% | 4.08% |
| `packages/engine/Specs/Scene` | 251 | 25996.3 | 7.74% | 0.0% |
| `packages/engine/Source/DataSources` | 108 | 24654.94 | 45.73% | 1.49% |
| `Apps/Sandcastle/gallery` | 215 | 14378.96 | 31.45% | 0.08% |
| `packages/engine/Source/Scene/Model` | 87 | 12875.04 | 28.18% | 0.13% |
| `packages/engine/Specs/Core` | 211 | 10882.5 | 3.68% | 0.0% |
| `packages/engine/Source/Renderer` | 46 | 8815.2 | 38.89% | 1.29% |
| `__monolith__` | 22 | 6265.46 | 11.72% | 1.76% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/dev.yml` -> **100.0%** Exposure
- `.github/workflows/prod.yml` -> **100.0%** Exposure
- `packages/engine/Source/Scene/Cesium3DTileContent.js` -> **100.0%** Exposure
- `packages/engine/Source/Scene/Empty3DTileContent.js` -> **100.0%** Exposure
- `packages/engine/Source/Scene/Tileset3DTileContent.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Apps/Sandcastle/Sandcastle-header.js` -> **100.0%** Exposure
- `Apps/TimelineDemo/TimelineDemo.js` -> **100.0%** Exposure
- `Tools/jsdoc/cesium_template/publish.js` -> **100.0%** Exposure
- `Tools/jsdoc/cesium_template/static/javascript/html5.js` -> **100.0%** Exposure
- `packages/engine/Source/Core/ArcGISTiledElevationTerrainProvider.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/engine/Source/Scene/Cesium3DTileContent.js` -> **8** Orphaned Functions | **16** Duplicates
- `packages/engine/Specs/Core/RequestSchedulerSpec.js` -> **0** Orphaned Functions | **22** Duplicates
- `packages/engine/Specs/Scene/Cesium3DTileStyleSpec.js` -> **1** Orphaned Functions | **21** Duplicates
- `packages/engine/Specs/Scene/I3SDataProviderSpec.js` -> **1** Orphaned Functions | **17** Duplicates
- `packages/engine/Specs/Scene/GeometryRenderingSpec.js` -> **0** Orphaned Functions | **14** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `Apps/Sandcastle/gallery/Drape Imagery on 3D Tiles.html` -> **99.9997%** Exposure
- `packages/sandcastle/gallery/itwin-gaussian-splats/main.js` -> **99.9985%** Exposure
- `packages/engine/Source/Core/Ion.js` -> **99.9973%** Exposure
- `packages/sandcastle/gallery/drape-imagery-on-3d-tiles/main.js` -> **99.97%** Exposure
- `Apps/Sandcastle/gallery/iTwin Feature Service.html` -> **99.8324%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `67` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `985` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/engine/Specs/DataSources/KmlDataSourceSpec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.114)
- **Top Global Matches:** file_cluster_10: 6.114, file_cluster_2: 7.427, file_cluster_12: 7.584
- **Magnitude:** 59712.57 | **LOC:** 5865 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (91.3%), Guard Balance (formerly Safety Score) (43.0%), Complexity Load (formerly Cognitive Load) (5.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 287
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 245`, `args: 456`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 9`, `state_mutation: 34`
* *Architecture:* `concurrency: 222`, `import: 3`
* *Defense:* `safety: 6`, `test: 1021`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` createCamera.js, pollToPromise.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/engine/Source/DataSources/KmlDataSource.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.05)
- **Top Global Matches:** file_cluster_6: 7.05, file_cluster_4: 7.804, file_cluster_15: 15.239
- **Magnitude:** 3291.78 | **LOC:** 4250 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **69**; blast radius 0.168; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (67.5%), Guard Balance (formerly Safety Score) (63.9%), Concurrency Surface (formerly Concurrency) (50.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processScreenOverlay` **(Many-Argument Workhorses)** (Impact: 101.4)
  * `processNetworkLink` **(Many-Argument Workhorses)** (Impact: 93.0)
  * `applyStyle` **(Many-Argument Workhorses)** (Impact: 76.2)
  * `processDescription` **(Many-Argument Workhorses)** (Impact: 72.8)
  * `processStyles` **(Many-Argument Workhorses)** (Impact: 72.2)
    * *Intent:* //Processes all shared and external styles and stores //their id into the provided styleCollection. ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 425 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 1409
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 599`, `structural_boundaries: 347`, `args: 131`, `func_start: 112`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 559`, `dead_code: 1`
* *Architecture:* `api: 4`, `concurrency: 28`, `import: 69`
* *Defense:* `safety: 208`, `doc: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.168
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000251
  * `Imports (Out-Degree: 66):` ArcType.js, AssociativeArray.js, BoundingRectangle.js, Cartesian2.js, Cartesian3.js, Cartographic.js, ClockRange.js, ClockStep.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/Scene.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.612)
- **Top Global Matches:** file_cluster_4: 6.612, file_cluster_15: 9.908, file_cluster_10: 10.417
- **Magnitude:** 2720.22 | **LOC:** 5293 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **83**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.9%), Complexity Load (formerly Cognitive Load) (46.5%), Connectivity (formerly Api Exposure) (40.4%)
- **Documentation Coverage:** 19.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeCommands` **(Many-Argument Workhorses)** (Impact: 112.9)
    * *Intent:* /** * Execute the draw commands for all the render passes. * * */
  * `updateAndClearFramebuffers` **(Many-Argument Workhorses)** (Impact: 95.8)
  * `executeCommand` **(Many-Argument Workhorses)** (Impact: 71.1)
    * *Intent:* /** * Execute a single draw command, or one of its derived commands if appropriate for the current r...
  * `updateEnvironment` **(I/O & Config Routines)** (Impact: 44.5)
    * *Intent:* /** */
  * `Scene` **(I/O & Config Routines)** (Impact: 39.8)
    * *Intent:* * * * // Create scene without anisotropic texture filtering * const scene = new Cesium.Scene({ * can...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 379 instances
* *State Mutation (weighted view):* 1326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 292`, `args: 170`, `func_start: 163`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 568`, `duplicate_logic: 4`
* *Architecture:* `api: 20`, `concurrency: 2`, `import: 83`
* *Defense:* `safety: 102`, `doc: 160`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.000251
  * `Imports (Out-Degree: 83):` BoundingRectangle.js, BoundingSphere.js, BoxGeometry.js, Cartesian3.js, Cartographic.js, Check.js, Color.js, ColorGeometryInstanceAttribute.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/engine/Source/DataSources/CzmlDataSource.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.838)
- **Top Global Matches:** file_cluster_4: 6.838, file_cluster_15: 8.407, file_cluster_16: 9.642
- **Magnitude:** 2329.96 | **LOC:** 5152 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **93**; blast radius 0.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (55.8%), Complexity Load (formerly Cognitive Load) (36.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.9%)
- **Documentation Coverage:** 80.198% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processProperty` **(Many-Argument Workhorses)** (Impact: 130.5)
  * `processPositionProperty` **(Many-Argument Workhorses)** (Impact: 128.4)
  * `processMaterialProperty` **(Many-Argument Workhorses)** (Impact: 116.1)
  * `unwrapInterval` **(Defensive Guards)** (Impact: 105.6)
  * `getPropertyType` **(Compute Cores)** (Impact: 96.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 241 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 777
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 356`, `args: 107`, `func_start: 101`
* *Risk/State:* `state_mutation: 295`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 93`
* *Defense:* `safety: 118`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 92):` ArcType.js, BoundingRectangle.js, Cartesian2.js, Cartesian3.js, Cartographic.js, ClockRange.js, ClockStep.js, Color.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/engine/Source/Core/GeometryPipeline.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.447)
- **Top Global Matches:** file_cluster_6: 5.447, file_cluster_4: 10.455, file_cluster_8: 14.649
- **Magnitude:** 2204.76 | **LOC:** 3292 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **24**; blast radius 0.275; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (60.8%), Connectivity (formerly Api Exposure) (53.2%)
- **Documentation Coverage:** 53.2258% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `computeTriangleAttributes` **(Many-Argument Workhorses)** (Impact: 89.8)
  * `splitLongitudePolyline` **(I/O & Config Routines)** (Impact: 53.2)
  * `compressVertices` **(Compute Cores)** (Impact: 49.9)
    * *Intent:* /** * Compresses and packs geometry normal attribute values to save memory. * * * geometry = Cesium....
  * `splitTriangle` **(Many-Argument Workhorses)** (Impact: 49.1)
  * `splitLongitudeTriangles` **(Compute Cores)** (Impact: 43.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 368 instances
* *State Mutation (weighted view):* 1238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 219`, `args: 49`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 502`
* *Architecture:* `api: 15`, `import: 24`
* *Defense:* `safety: 40`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.275
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.010129
  * `Imports (Out-Degree: 24):` AttributeCompression.js, BoundingSphere.js, Cartesian2.js, Cartesian3.js, Cartesian4.js, Cartographic.js, ComponentDatatype.js, DeveloperError.js...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/Camera.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.709)
- **Top Global Matches:** file_cluster_4: 7.709, file_cluster_15: 8.158, file_cluster_10: 9.106
- **Magnitude:** 2030.98 | **LOC:** 3990 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **30**; blast radius 0.176; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.3%), Connectivity (formerly Api Exposure) (58.2%), Complexity Load (formerly Cognitive Load) (47.9%)
- **Documentation Coverage:** 28.2609% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateMembers` **(Compute Cores)** (Impact: 60.3)
  * `rectangleCameraPosition3D` **(Many-Argument Workhorses)** (Impact: 41.0)
  * `_updateCameraChanged` **(I/O & Config Routines)** (Impact: 33.0)
  * `setView` **(Defensive Guards)** (Impact: 29.5)
    * *Intent:* * // 4. View rectangle with a top-down view * viewer.camera.setView({ * destination : Cesium.Rectang...
  * `flyTo` **(Defensive Guards)** (Impact: 29.4)
    * *Intent:* * up : new Cesium.Cartesian3(-0.47934589305293746, -0.8553216253114552, 0.1966022179118339) * } * })...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 298 instances
* *State Mutation (weighted view):* 1043
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 186`, `args: 105`, `func_start: 105`
* *Risk/State:* `state_mutation: 447`
* *Architecture:* `api: 34`, `import: 30`
* *Defense:* `safety: 124`, `doc: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.001293
  * `Imports (Out-Degree: 30):` BoundingSphere.js, Cartesian2.js, Cartesian3.js, Cartesian4.js, Cartographic.js, DeveloperError.js, EasingFunction.js, Ellipsoid.js...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/GltfLoader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.892)
- **Top Global Matches:** file_cluster_15: 6.892, file_cluster_4: 7.302, file_cluster_16: 8.609
- **Magnitude:** 1996.12 | **LOC:** 3182 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 35.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **36**; blast radius 0.203; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.5%), Guard Balance (formerly Safety Score) (64.5%), Complexity Load (formerly Cognitive Load) (59.0%)
- **Documentation Coverage:** 77.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadPrimitive` **(Many-Argument Workhorses)** (Impact: 68.6)
    * *Intent:* /** * Load resources associated with a mesh primitive for a glTF node */
  * `loadVertexAttribute` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `loadMaterial` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* /** * Load textures and parse factors and flags for a glTF material * */
  * `loadAttribute` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `loadInstancedAttribute` **(Many-Argument Workhorses)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 233 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 861
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 232`, `args: 114`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 395`
* *Architecture:* `api: 5`, `concurrency: 13`, `import: 36`
* *Defense:* `safety: 76`, `doc: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.002097
  * `Imports (Out-Degree: 36):` ArticulationStageType.js, Cartesian2.js, Cartesian3.js, Cartesian4.js, Check.js, ComponentDatatype.js, Credit.js, FeatureDetection.js...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/Expression.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.8)
- **Top Global Matches:** file_cluster_4: 7.8, file_cluster_6: 9.172, file_cluster_15: 14.208
- **Magnitude:** 1984.12 | **LOC:** 2234 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.216; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.2%), Guard Balance (formerly Safety Score) (42.7%), Connectivity (formerly Api Exposure) (26.7%)
- **Documentation Coverage:** 88.7755% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getShaderExpression` **(Many-Argument Workhorses)** (Impact: 237.1)
  * `setEvaluateFunction` **(Defensive Guards)** (Impact: 133.7)
  * `parseCall` **(Defensive Guards)** (Impact: 109.0)
  * `getEvaluateTernaryComponentwise` **(Defensive Guards)** (Impact: 54.0)
  * `createRuntimeAst` **(Defensive Guards)** (Impact: 49.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 191 instances
* *State Mutation (weighted view):* 617
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 674`, `structural_boundaries: 328`, `args: 102`, `func_start: 95`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 235`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 453`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001379
  * `Imports (Out-Degree: 10):` Cartesian2.js, Cartesian3.js, Cartesian4.js, Check.js, Color.js, DeveloperError.js, Math.js, RuntimeError.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/GlobeSurfaceTileProvider.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.04)
- **Top Global Matches:** file_cluster_4: 8.04, file_cluster_10: 9.379, file_cluster_15: 9.422
- **Magnitude:** 1876.28 | **LOC:** 2911 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **53**; blast radius 0.158; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (64.9%), Connectivity (formerly Api Exposure) (60.0%)
- **Documentation Coverage:** 73.5632% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addDrawCommandsForTile` **(Many-Argument Workhorses)** (Impact: 247.2)
  * `updateTileBoundingRegion` **(Many-Argument Workhorses)** (Impact: 69.6)
  * `computeTileVisibility` **(Many-Argument Workhorses)** (Impact: 67.3)
    * *Intent:* /** * Determines the visibility of a given tile. The tile may be fully visible, partially visible, o...
  * `canRenderWithoutLosingDetail` **(Many-Argument Workhorses)** (Impact: 45.6)
    * *Intent:* /** * Determines if the given not-fully-loaded tile can be rendered without losing detail that * was...
  * `_onLayerAdded` **(Defensive Guards)** (Impact: 34.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 245 instances
* *State Mutation (weighted view):* 909
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 260`, `args: 113`, `func_start: 105`
* *Risk/State:* `state_mutation: 419`
* *Architecture:* `api: 66`, `import: 53`
* *Defense:* `safety: 104`, `doc: 30`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000335
  * `Imports (Out-Degree: 53):` BoundingSphere.js, BoxOutlineGeometry.js, Cartesian2.js, Cartesian3.js, Cartesian4.js, Cartographic.js, Color.js, ColorGeometryInstanceAttribute.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/ScreenSpaceCameraController.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.799)
- **Top Global Matches:** file_cluster_6: 5.799, file_cluster_4: 11.557, file_cluster_8: 13.65
- **Magnitude:** 1832.42 | **LOC:** 3112 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **26**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (50.9%), Connectivity (formerly Api Exposure) (19.6%)
- **Documentation Coverage:** 82.9268% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleZoom` **(Many-Argument Workhorses)** (Impact: 182.6)
  * `pan3D` **(Many-Argument Workhorses)** (Impact: 73.1)
  * `look3D` **(Many-Argument Workhorses)** (Impact: 66.5)
  * `rotateCVOnTerrain` **(Many-Argument Workhorses)** (Impact: 58.8)
  * `spin3D` **(Many-Argument Workhorses)** (Impact: 55.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 222 instances
* *State Mutation (weighted view):* 825
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 147`, `args: 39`, `func_start: 39`
* *Risk/State:* `state_mutation: 381`
* *Architecture:* `api: 3`, `import: 26`
* *Defense:* `safety: 31`, `doc: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000335
  * `Imports (Out-Degree: 26):` Cartesian2.js, Cartesian3.js, Cartesian4.js, Cartographic.js, DeveloperError.js, Ellipsoid.js, HeadingPitchRoll.js, IntersectionTests.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/Cesium3DTileset.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.452)
- **Top Global Matches:** file_cluster_15: 8.452, file_cluster_10: 8.522, file_cluster_4: 9.056
- **Magnitude:** 1799.38 | **LOC:** 3934 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **65**; blast radius 0.244; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (46.9%), Connectivity (formerly Api Exposure) (38.6%)
- **Documentation Coverage:** 5.042% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Cesium3DTileset` **(Many-Argument Workhorses)** (Impact: 126.9)
    * *Intent:* * scene.primitives.add(tileset); * * // Common settings for the dynamicScreenSpaceError optimization...
  * `updateTiles` **(Many-Argument Workhorses)** (Impact: 52.7)
    * *Intent:* /** */
  * `updateForPass` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* /** */
  * `loadTileset` **(Many-Argument Workhorses)** (Impact: 29.5)
    * *Intent:* /** * Loads the main tileset JSON file or a tileset JSON file referenced from a tile. * * or when th...
  * `addTileDebugLabel` **(Many-Argument Workhorses)** (Impact: 23.2)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 294 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 976
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 228`, `args: 120`, `func_start: 111`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 388`
* *Architecture:* `api: 9`, `concurrency: 9`, `import: 65`
* *Defense:* `safety: 102`, `doc: 142`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.001724
  * `Imports (Out-Degree: 65):` ApproximateTerrainHeights.js, BoundingSphere.js, Cartesian2.js, Cartesian3.js, Cartographic.js, Check.js, Color.js, Credit.js...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/engine/Specs/Scene/Cesium3DTilesetSpec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.975)
- **Top Global Matches:** file_cluster_10: 7.975, file_cluster_12: 8.011, file_cluster_15: 9.321
- **Magnitude:** 1793.14 | **LOC:** 7338 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.8%), Complexity Load (formerly Cognitive Load) (39.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findTileByUri` **(Compute Cores)** (Impact: 7.6)
  * `testColorBlendMode` **(I/O & Config Routines)** (Impact: 5.9)
  * `numberOfChildrenWithoutContent` **(Compute Cores)** (Impact: 4.8)
  * `checkPointAndFeatureCounts` **(Many-Argument Workhorses)** (Impact: 4.1)
  * `testBackFaceCulling` **(Callbacks & Closures)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 150 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 1159
* *State Mutation (weighted view):* 452
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 560`, `args: 647`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 364`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `concurrency: 409`, `import: 6`
* *Defense:* `safety: 11`, `test: 1314`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Cesium3DTilesTester.js, createScene.js, generateJsonBuffer.js, pollToPromise.js, Ellipsoid.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/engine/Source/Scene/Primitive.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.66)
- **Top Global Matches:** file_cluster_4: 6.66, file_cluster_6: 8.191, file_cluster_12: 13.655
- **Magnitude:** 1690.04 | **LOC:** 2505 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **40**; blast radius 0.313; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.6%), Complexity Load (formerly Cognitive Load) (62.2%), Connectivity (formerly Api Exposure) (36.4%)
- **Documentation Coverage:** 73.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Defensive Guards)** (Impact: 71.1)
    * *Intent:* /** * get the draw commands needed to render this primitive. * <p> * Do not call this function direc...
  * `updateAndQueueCommands` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `loadAsynchronous` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `createCommands` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `modifyForEncodedNormals` **(Many-Argument Workhorses)** (Impact: 36.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 252 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 920
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 184`, `args: 61`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 416`
* *Architecture:* `io: 11`, `api: 5`, `concurrency: 6`, `import: 40`
* *Defense:* `safety: 74`, `doc: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.313
  * `Choke Point (Betweenness):` 0.000155 | `Ripple Effect (Closeness):` 0.007349
  * `Imports (Out-Degree: 40):` BoundingSphere.js, Cartesian2.js, Cartesian3.js, Cartesian4.js, Cartographic.js, Color.js, ComponentDatatype.js, DeveloperError.js...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/Model/Model.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.393)
- **Top Global Matches:** file_cluster_10: 8.393, file_cluster_15: 8.59, file_cluster_16: 9.704
- **Magnitude:** 1568.2 | **LOC:** 3341 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **44**; blast radius 0.19; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.9%), Complexity Load (formerly Cognitive Load) (51.5%), Connectivity (formerly Api Exposure) (39.1%)
- **Documentation Coverage:** 25.7862% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Model` **(Defensive Guards)** (Impact: 85.4)
    * *Intent:* * * * */
  * `update` **(Compute Cores)** (Impact: 38.4)
    * *Intent:* /** * get the draw commands needed to render this primitive. * <p> * Do not call this function direc...
  * `fromGltfAsync` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* * } * }); * viewer.scene.primitives.add(model); * model.readyEvent.addEventListener(() => { * model....
  * `updateClamping` **(Defensive Guards)** (Impact: 20.1)
  * `destroy` **(I/O & Config Routines)** (Impact: 19.6)
    * *Intent:* * release of WebGL resources, instead of relying on the garbage collector to destroy this object. * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 243 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 176`, `args: 153`, `func_start: 149`
* *Risk/State:* `state_mutation: 305`
* *Architecture:* `api: 11`, `concurrency: 9`, `import: 44`
* *Defense:* `safety: 130`, `doc: 88`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.19
  * `Choke Point (Betweenness):` 0.000242 | `Ripple Effect (Closeness):` 0.001644
  * `Imports (Out-Degree: 44):` BoundingSphere.js, Cartesian3.js, Cartographic.js, Check.js, Color.js, Credit.js, DeveloperError.js, DistanceDisplayCondition.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/TerrainFillMesh.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.713)
- **Top Global Matches:** file_cluster_8: 7.713, file_cluster_6: 9.522, file_cluster_4: 17.797
- **Magnitude:** 1529.38 | **LOC:** 2223 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.156; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.3%), Complexity Load (formerly Cognitive Load) (56.8%), Connectivity (formerly Api Exposure) (20.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `propagateEdge` **(Many-Argument Workhorses)** (Impact: 128.6)
  * `visitRenderedTiles` **(Many-Argument Workhorses)** (Impact: 116.2)
  * `addEdgeMesh` **(Many-Argument Workhorses)** (Impact: 94.4)
  * `getCornerFromEdge` **(Many-Argument Workhorses)** (Impact: 87.8)
  * `createFillMesh` **(Many-Argument Workhorses)** (Impact: 72.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 205 instances
* *State Mutation (weighted view):* 686
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 155`, `args: 25`, `func_start: 24`
* *Risk/State:* `state_mutation: 276`
* *Architecture:* `api: 3`, `import: 20`
* *Defense:* `safety: 50`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.156
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000377
  * `Imports (Out-Degree: 20):` AttributeCompression.js, BoundingSphere.js, Cartesian2.js, Cartesian3.js, Cartesian4.js, Cartographic.js, DeveloperError.js, HeightmapTerrainData.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Core/Matrix4.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.944)
- **Top Global Matches:** file_cluster_4: 6.944, file_cluster_10: 9.444, file_cluster_15: 9.467
- **Magnitude:** 1449.46 | **LOC:** 3234 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **135** in-repo importer(s); it depends on **9**; blast radius 2.291; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (95.0%), Guard Balance (formerly Safety Score) (69.5%), Complexity Load (formerly Cognitive Load) (46.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Matrix4` **(Many-Argument Workhorses)** (Impact: 71.8)
    * *Intent:* */
  * `equalsEpsilon` **(Defensive Guards)** (Impact: 41.2)
    * *Intent:* * * // b = [10.0, 14.0, 18.0, 22.0] * // [11.0, 15.0, 19.0, 23.0] * // [12.0, 16.0, 20.0, 24.0] * //...
  * `equals` **(Defensive Guards)** (Impact: 34.4)
    * *Intent:* * * // b = [10.0, 14.0, 18.0, 22.0] * // [11.0, 15.0, 19.0, 23.0] * // [12.0, 16.0, 20.0, 24.0] * //...
  * `equalsArray` **(Defensive Guards)** (Impact: 33.0)
    * *Intent:* /** */
  * `computeViewportTransformation` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* * * // Create viewport transformation using an explicit viewport and depth range. * const m = Cesium...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 908
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 100`, `args: 63`, `func_start: 63`
* *Risk/State:* `state_mutation: 774`, `dead_code: 10`
* *Architecture:* `api: 47`, `import: 9`
* *Defense:* `safety: 68`, `doc: 83`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.291
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.056247
  * `Imports (Out-Degree: 9):` Cartesian3.js, Cartesian4.js, Check.js, DeveloperError.js, Frozen.js, Math.js, Matrix3.js, RuntimeError.js...
  * `Imported By (In-Degree: 135):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/PolylineCollection.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.232)
- **Top Global Matches:** file_cluster_6: 7.232, file_cluster_4: 8.384, file_cluster_15: 15.494
- **Magnitude:** 1389.74 | **LOC:** 1948 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **37**; blast radius 0.175; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.2%), Guard Balance (formerly Safety Score) (70.5%), Connectivity (formerly Api Exposure) (31.3%)
- **Documentation Coverage:** 70.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Many-Argument Workhorses)** (Impact: 114.2)
  * `writeUpdate` **(Many-Argument Workhorses)** (Impact: 80.9)
  * `createCommandLists` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `update` **(Compute Cores)** (Impact: 58.0)
    * *Intent:* /** * get the draw commands needed to render this primitive. * <p> * Do not call this function direc...
  * `createVertexArrays` **(Many-Argument Workhorses)** (Impact: 46.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 217 instances
* *State Mutation (weighted view):* 778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 151`, `args: 36`, `func_start: 36`
* *Risk/State:* `state_mutation: 344`
* *Architecture:* `io: 3`, `api: 5`, `import: 37`
* *Defense:* `safety: 56`, `doc: 13`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.0014
  * `Imports (Out-Degree: 34):` BoundingSphere.js, Cartesian2.js, Cartesian3.js, Cartesian4.js, Cartographic.js, Color.js, ComponentDatatype.js, DeveloperError.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/BillboardCollection.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.362)
- **Top Global Matches:** file_cluster_4: 7.362, file_cluster_15: 8.297, file_cluster_10: 9.059
- **Magnitude:** 1352.56 | **LOC:** 2151 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **38**; blast radius 0.188; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.4%), Guard Balance (formerly Safety Score) (70.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.1%)
- **Documentation Coverage:** 56.8966% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 189.6)
    * *Intent:* /** * get the draw commands needed to render this primitive. * <p> * Do not call this function direc...
  * `BillboardCollection` **(Compute Cores)** (Impact: 33.1)
    * *Intent:* * * // Create a billboard collection with two billboards * const billboards = scene.primitives.add(n...
  * `updateMode` **(Defensive Guards)** (Impact: 25.1)
  * `writeCompressedAttribute3` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `recomputeActualPositions` **(Many-Argument Workhorses)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 235 instances
* *State Mutation (weighted view):* 782
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 143`, `args: 52`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 312`
* *Architecture:* `io: 23`, `api: 9`, `import: 38`
* *Defense:* `safety: 68`, `doc: 22`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.188
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.002328
  * `Imports (Out-Degree: 36):` AttributeCompression.js, BoundingRectangle.js, BoundingSphere.js, Cartesian2.js, Cartesian3.js, Check.js, Color.js, ComponentDatatype.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Core/RectangleGeometry.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.491)
- **Top Global Matches:** file_cluster_6: 5.491, file_cluster_4: 11.047, file_cluster_8: 13.896
- **Magnitude:** 1328.86 | **LOC:** 1481 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 0.191; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (58.7%), Connectivity (formerly Api Exposure) (26.9%)
- **Documentation Coverage:** 45.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructExtrudedRectangle` **(Many-Argument Workhorses)** (Impact: 131.7)
  * `constructRectangle` **(Many-Argument Workhorses)** (Impact: 64.2)
  * `calculateAttributesWall` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `calculateAttributes` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `createGeometry` **(I/O & Config Routines)** (Impact: 21.3)
    * *Intent:* /** * Computes the geometric representation of a rectangle, including its vertices, indices, and a b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 285 instances
* *State Mutation (weighted view):* 921
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 111`, `args: 17`, `func_start: 17`
* *Risk/State:* `state_mutation: 351`
* *Architecture:* `api: 4`, `import: 26`
* *Defense:* `safety: 28`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.191
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000566
  * `Imports (Out-Degree: 26):` BoundingSphere.js, Cartesian2.js, Cartesian3.js, Cartographic.js, Check.js, ComponentDatatype.js, DeveloperError.js, Ellipsoid.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/engine/Source/Scene/Cesium3DTile.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.779)
- **Top Global Matches:** file_cluster_4: 7.779, file_cluster_15: 7.94, file_cluster_10: 8.766
- **Magnitude:** 1294.32 | **LOC:** 2476 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **45**; blast radius 0.165; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (76.6%), Guard Balance (formerly Safety Score) (64.5%), Complexity Load (formerly Cognitive Load) (40.0%)
- **Documentation Coverage:** 5.9701% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Cesium3DTile` **(Many-Argument Workhorses)** (Impact: 86.8)
    * *Intent:* /** * the content is loaded on-demand when needed based on the view. * <p> * </p> * */
  * `applyDebugSettings` **(Many-Argument Workhorses)** (Impact: 80.4)
    * *Intent:* /** */
  * `isPriorityDeferred` **(Many-Argument Workhorses)** (Impact: 31.0)
    * *Intent:* /** */
  * `createBoundingVolume` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* /** * Create a bounding volume from the tile's bounding volume header. * * * */
  * `processArrayBuffer` **(Many-Argument Workhorses)** (Impact: 28.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 163 instances
* *Concurrency (weighted view):* 60
* *State Mutation (weighted view):* 602
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 165`, `args: 62`, `func_start: 58`
* *Risk/State:* `state_mutation: 276`
* *Architecture:* `api: 10`, `concurrency: 10`, `import: 45`
* *Defense:* `safety: 69`, `doc: 79`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 9.7e-05 | `Ripple Effect (Closeness):` 0.00137
  * `Imports (Out-Degree: 45):` BoundingSphere.js, Cartesian3.js, Color.js, ColorGeometryInstanceAttribute.js, CullingVolume.js, Ellipsoid.js, Intersect.js, JulianDate.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/engine/Specs/Scene/Model/ModelSpec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.148)
- **Top Global Matches:** file_cluster_10: 8.148, file_cluster_12: 8.168, file_cluster_15: 9.844
- **Magnitude:** 1252.2 | **LOC:** 5109 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (77.8%), Guard Balance (formerly Safety Score) (46.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verifyDebugWireframe` **(Many-Argument Workhorses)** (Impact: 20.4)
  * `verifyRender` **(Defensive Guards)** (Impact: 19.6)
  * `setFeaturesWithOpacity` **(Many-Argument Workhorses)** (Impact: 6.9)
  * `zoomTo` **(Defensive Guards)** (Impact: 3.9)
  * `viewFog` **(State Mutators)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 63 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 747
* *State Mutation (weighted view):* 357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 337`, `args: 336`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 269`, `dead_code: 2`
* *Architecture:* `concurrency: 432`, `import: 4`
* *Defense:* `safety: 11`, `test: 845`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` createScene.js, pollToPromise.js, index.js, loadAndZoomToModelAsync.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/engine/Source/Workers/decodeI3S.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.129)
- **Top Global Matches:** file_cluster_4: 6.129, file_cluster_6: 8.807, file_cluster_15: 12.465
- **Magnitude:** 1206.26 | **LOC:** 1656 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%), Complexity Load (formerly Cognitive Load) (65.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateGltfBuffer` **(Many-Argument Workhorses)** (Impact: 114.7)
  * `decodeDracoAttribute` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `generateNormals` **(Many-Argument Workhorses)** (Impact: 46.1)
  * `generateIndexArray` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `decodeDracoEncodedGeometry` **(Defensive Guards)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 164 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 573
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 142`, `args: 52`, `func_start: 38`
* *Risk/State:* `state_mutation: 245`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 11`
* *Defense:* `safety: 35`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Cartesian3.js, Cartographic.js, Color.js, Ellipsoid.js, Math.js, Matrix3.js, WebMercatorProjection.js, defined.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/engine/Specs/Scene/BillboardCollectionSpec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.346)
- **Top Global Matches:** file_cluster_10: 6.346, file_cluster_12: 8.316, file_cluster_2: 9.317
- **Magnitude:** 1204.3 | **LOC:** 2801 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (45.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invokeCallback` **(Callbacks & Closures)** (Impact: 1.6)
  * `image` **(Callbacks & Closures)** (Impact: 1.1)
  * `image` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 115 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 728
* *State Mutation (weighted view):* 427
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 233`, `args: 291`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 405`, `duplicate_logic: 2`
* *Architecture:* `concurrency: 153`, `import: 3`
* *Defense:* `safety: 7`, `test: 574`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` createScene.js, pollToPromise.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/engine/Source/Core/CorridorGeometry.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.556)
- **Top Global Matches:** file_cluster_4: 7.556, file_cluster_6: 7.588, file_cluster_15: 14.455
- **Magnitude:** 1186.82 | **LOC:** 1412 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 0.203; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.1%), Complexity Load (formerly Cognitive Load) (55.3%), Connectivity (formerly Api Exposure) (30.1%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `combine` **(Many-Argument Workhorses)** (Impact: 91.6)
  * `extrudedAttributes` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `computePositionsExtruded` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `computeRectangle` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `CorridorGeometry` **(Defensive Guards)** (Impact: 16.1)
    * *Intent:* * * * * const corridor = new Cesium.CorridorGeometry({ * vertexFormat : Cesium.VertexFormat.POSITION...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 857
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 105`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 403`
* *Architecture:* `api: 5`, `import: 21`
* *Defense:* `safety: 22`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000566
  * `Imports (Out-Degree: 21):` BoundingSphere.js, Cartesian3.js, Cartographic.js, Check.js, ComponentDatatype.js, CornerType.js, CorridorGeometryLibrary.js, Ellipsoid.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/engine/Source/Scene/ClippingPlaneCollection.js` (JAVASCRIPT) | Magnitude: 387.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 341, state_mutation: 95, core_var_decl: 66, structural_boundaries: 62
- `packages/sandcastle/gallery/imodel-mesh-export-service/main.js` (JAVASCRIPT) | Magnitude: 98.84 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 175, state_mutation: 43, core_var_decl: 24, design_camel_case: 14
- `Apps/Sandcastle/gallery/Particle System Weather.html` (HTML) | Magnitude: 82.46 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 190, core_var_decl: 35, state_mutation: 26, design_snake_case: 20
- `Apps/Sandcastle/gallery/3D Tiles Adjust Height.html` (HTML) | Magnitude: 40.4 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 107, core_var_decl: 29, design_snake_case: 28, args: 14
- `packages/engine/Specs/Core/PolygonPipelineSpec.js` (JAVASCRIPT) | Magnitude: 26.3 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 561, test: 202, args: 52, closures: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/engine/Specs/Core/getStringFromTypedArraySpec.js` (JAVASCRIPT) | Magnitude: 5.02 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 78, test: 27, args: 19, closures: 18
- `Apps/Sandcastle/gallery/development/Custom Primitive.html` (HTML) | Magnitude: 131.34 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 264, core_var_decl: 75, design_snake_case: 48, state_mutation: 43
- `packages/engine/Specs/Core/CartographicSpec.js` (JAVASCRIPT) | Magnitude: 28.48 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 220, test: 88, core_var_decl: 46, design_snake_case: 40
- `packages/engine/Specs/Scene/LabelCollectionSpec.js` (JAVASCRIPT) | Magnitude: 748.22 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 2110, test: 551, state_mutation: 295, core_var_decl: 282
- `packages/engine/Specs/Scene/Model/pickModelSpec.js` (JAVASCRIPT) | Magnitude: 63.62 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 375, core_var_decl: 60, design_snake_case: 50, test: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/engine/Source/Core/Cartographic.js` (JAVASCRIPT) | Magnitude: 153.96 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 32, branch: 24, structural_boundaries: 23
- `packages/engine/Source/Scene/MetadataClassProperty.js` (JAVASCRIPT) | Magnitude: 666.56 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 711, branch: 171, structural_boundaries: 156, core_var_decl: 108
- `packages/engine/Source/Scene/BufferPrimitiveCollection.js` (JAVASCRIPT) | Magnitude: 233.64 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 245, state_mutation: 61, doc: 53, core_var_decl: 31
- `packages/engine/Source/Scene/GltfDracoLoader.js` (JAVASCRIPT) | Magnitude: 145.34 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 35, structural_boundaries: 31, core_var_decl: 25
- `packages/engine/Specs/Scene/Model/PickingPipelineStageSpec.js` (JAVASCRIPT) | Magnitude: 101.12 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 289, core_var_decl: 67, test: 52, design_camel_case: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/engine/Source/Scene/CullFace.js` (JAVASCRIPT) | Magnitude: 14.64 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 4, indent_spaces: 3, structural_boundaries: 2, branch: 1
- `packages/engine/Source/Core/Iso8601.js` (JAVASCRIPT) | Magnitude: 16.4 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, doc: 4, core_var_decl: 4, structural_boundaries: 3
- `packages/widgets/Source/widgets.css` (CSS) | Magnitude: 0.77 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Apps/Sandcastle/gallery/Resolution Scaling.html` (HTML) | Magnitude: 40.28 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 91, core_var_decl: 28, design_snake_case: 24, args: 15
- `packages/engine/Specs/DataSources/PolylineVolumeGraphicsSpec.js` (JAVASCRIPT) | Magnitude: 55.04 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 196, test: 68, state_mutation: 36, core_var_decl: 22
- `Apps/Sandcastle/gallery/development/Polyline Color.html` (HTML) | Magnitude: 52.78 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 81, core_var_decl: 21, design_snake_case: 21, state_mutation: 12
- `packages/engine/Specs/Scene/MetadataSchemaSpec.js` (JAVASCRIPT) | Magnitude: 17.46 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 120, test: 25, core_var_decl: 10, design_camel_case: 6
- `packages/widgets/Source/InspectorShared.js` (JAVASCRIPT) | Magnitude: 97.64 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 119, state_mutation: 26, core_var_decl: 20, globals: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/engine/Source/Scene/GlobeSurfaceTile.js` (JAVASCRIPT) | Magnitude: 680.12 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 674, state_mutation: 132, branch: 108, core_var_decl: 106
- `packages/engine/Source/Scene/GltfVertexBufferLoader.js` (JAVASCRIPT) | Magnitude: 382.96 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 427, state_mutation: 93, core_var_decl: 77, branch: 67
- `packages/engine/Source/Core/CorridorGeometry.js` (JAVASCRIPT) | Magnitude: 1186.82 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 1128, state_mutation: 403, core_var_decl: 294, design_snake_case: 141
- `packages/widgets/Source/Timeline/Timeline.js` (JAVASCRIPT) | Magnitude: 712.62 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 781, state_mutation: 205, core_var_decl: 127, branch: 118
- `packages/engine/Source/DataSources/PointVisualizer.js` (JAVASCRIPT) | Magnitude: 282.66 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 320, state_mutation: 72, core_var_decl: 54, branch: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/engine/Source/Core/PolygonGeometryLibrary.js` (JAVASCRIPT) | Magnitude: 1076.96 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 947, core_var_decl: 254, state_mutation: 242, structural_boundaries: 146

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/engine/Specs/Core/OrthographicFrustumSpec.js` (JAVASCRIPT) | Magnitude: 48.6 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 275, test: 74, args: 47, closures: 47
- `packages/engine/Specs/Core/SphericalSpec.js` (JAVASCRIPT) | Magnitude: 15.8 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 102, test: 46, core_var_decl: 20, design_snake_case: 18
- `packages/sandcastle/gallery/czml-polyline-volume/main.js` (JAVASCRIPT) | Magnitude: 17.44 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 65, core_var_decl: 3, safety_bypasses: 2, design_snake_case: 2
- `Apps/Sandcastle/gallery/Corridor.html` (HTML) | Magnitude: 25.04 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 79, core_var_decl: 19, design_snake_case: 16, structural_boundaries: 8
- `Apps/Sandcastle/gallery/development/Shared Context.html` (HTML) | Magnitude: 41.98 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 106, core_var_decl: 24, design_snake_case: 22, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/engine/Specs/DataSources/PolylineGeometryUpdaterSpec.js` (JAVASCRIPT) | Magnitude: 123.38 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 777, test: 170, core_var_decl: 140, design_snake_case: 115
- `packages/sandcastle/src/ViewerConsoleStack.tsx` (TYPESCRIPT) | Magnitude: 30.26 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 17, branch: 12, core_var_decl: 12
- `packages/sandcastle/gallery/clustering/main.js` (JAVASCRIPT) | Magnitude: 78.62 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 92, state_mutation: 24, core_var_decl: 23, branch: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/engine/Source/Scene/GaussianSplatPrimitive.js` -> Churn: **100.0%** | Cog Load: 50.9359% | Debt: 0.0%
- `packages/engine/Source/Scene/CubeMapPanorama.js` -> Churn: **88.24%** | Cog Load: 52.0347% | Debt: 0.0%
- `packages/engine/Source/Scene/GltfLoader.js` -> Churn: **78.48%** | Cog Load: 59.0168% | Debt: 0.0%
- `packages/sandcastle/src/Gallery/GalleryItemStore.ts` -> Churn: **75.32%** | Cog Load: 57.2779% | Debt: 0.0%
- `packages/engine/Source/Scene/Model/EdgeVisibilityPipelineStage.js` -> Churn: **74.5%** | Cog Load: 66.7377% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/engine/Source/DataSources/KmlDataSource.js` -> **MohammadShujaullah** (100.0% isolated ownership) | Magnitude: 3291.78
- `packages/engine/Source/Scene/ScreenSpaceCameraController.js` -> **Leafmire** (100.0% isolated ownership) | Magnitude: 1832.42
- `packages/engine/Specs/Scene/Cesium3DTilesetSpec.js` -> **Matt Schwartz** (100.0% isolated ownership) | Magnitude: 1793.14
- `packages/engine/Source/Core/RectangleGeometry.js` -> **MohammadShujaullah** (100.0% isolated ownership) | Magnitude: 1328.86
- `packages/engine/Specs/Scene/Model/ModelSpec.js` -> **MohammadShujaullah** (100.0% isolated ownership) | Magnitude: 1252.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/engine/Source/Core/Transforms.js` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 99.9617%)
- `packages/engine/Source/Core/Resource.js` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 99.998%)
- `packages/engine/Source/Scene/Cesium3DTileset.js` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 100.0%)
- `packages/engine/Source/Core/Rectangle.js` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 100.0%)
- `packages/engine/Source/Scene/Model/Model.js` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/engine/Source/Core/DeveloperError.js` -> **Severity: 8.414** (Embedded: 0.1405 * Error Risk: 59.8688%)
- `packages/engine/Source/Core/Math.js` -> **Severity: 6.783** (Embedded: 0.0972 * Error Risk: 69.7603%)
- `packages/engine/Source/Core/Cartesian3.js` -> **Severity: 6.665** (Embedded: 0.1033 * Error Risk: 64.5496%)
- `packages/engine/Source/Core/Check.js` -> **Severity: 6.023** (Embedded: 0.1289 * Error Risk: 46.7274%)
- `packages/engine/Source/Core/Frozen.js` -> **Severity: 4.883** (Embedded: 0.0907 * Error Risk: 53.8495%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Apps/Sandcastle/Sandcastle-header.js` -> **Severity: 1871.2** (Blast Radius: 18.712 * Doc Risk: 100.0%)
- `packages/engine/Source/Core/DeveloperError.js` -> **Severity: 1413.84** (Blast Radius: 35.346 * Doc Risk: 40.0%)
- `Specs/createScene.js` -> **Severity: 1403.0** (Blast Radius: 14.03 * Doc Risk: 100.0%)
- `Specs/pollToPromise.js` -> **Severity: 867.5** (Blast Radius: 8.675 * Doc Risk: 100.0%)
- `Specs/createCanvas.js` -> **Severity: 789.6** (Blast Radius: 7.896 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 748 literal sites + 2 sites through wrappers = 750
- **`panics_and_aborts`:** 1998 literal sites + 19 sites through wrappers = 2017

- `handleError` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `packages/engine/Source/Scene/GltfLoader.js`
- `handleError` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `packages/engine/Source/Scene/GltfVertexBufferLoader.js`
- `handleError` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/engine/Source/Scene/GltfIndexBufferLoader.js`
- `handleError` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/engine/Source/Scene/GltfJsonLoader.js`
- `handleError` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/engine/Source/Scene/GltfSpzLoader.js`
- `handleError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/engine/Source/Scene/GltfDracoLoader.js`
- `highlightLine` (function, debug_prints, primitive): 2 call sites in 1 files -- `packages/sandcastle/src/App.tsx`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 45307 call pairs -- scoped 45.4%, unique 0.0%, ambiguous 7.8%, external 46.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 38755 | 51.2% | 0.0% | 9.0% | 39.8% |
| html | 5999 | 10.3% | 0.1% | 0.0% | 89.6% |
| typescript | 517 | 18.2% | 0.0% | 9.9% | 72.0% |
| python | 31 | 29.0% | 0.0% | 0.0% | 71.0% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
