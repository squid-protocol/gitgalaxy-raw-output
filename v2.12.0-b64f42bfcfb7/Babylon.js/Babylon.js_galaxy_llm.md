# ARCHITECTURAL_BRIEF: Babylon.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/BabylonJS/Babylon.js.git` |
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
- **Scope:** 4605 analyzed artifact(s), 578209 LOC.
- **Load-bearing artifact:** `packages/dev/core/src/types.ts` -- 595 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/tools/nodeEditor/src/blockTools.ts` -- pulls in 117 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 6919 |
| Analyzed Artifacts (Scanned) | 4605 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2314 |
| Total LOC | 578209 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 66.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6848 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1172 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.9233 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 296 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 3428 | 514160 | 74.4% |
| XML | 413 | 92 | 9.0% |
| JSON | 212 | 3743 | 4.6% |
| MARKDOWN | 170 | 0 | 3.7% |
| JAVASCRIPT | 136 | 39644 | 3.0% |
| CSS | 136 | 18625 | 3.0% |
| PLAINTEXT | 78 | 1 | 1.7% |
| HTML | 30 | 1906 | 0.7% |
| YAML | 2 | 38 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 4592 |
| utf-8 | bom | 12 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 28%, Large Core Modules (3) 20%, Declarative / Non-Code 11%, State Mutators Files 9%, Callbacks & Closures Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4254 | 92.4% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 247 | 5.4% |
| Static: Minified & Vendor Opaque Mass | 103 | 2.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2314*

**Composition by Extension & Reason:**
- `.png`: 916x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.fx`: 721x Unsupported Format (.fx)
- `.ts`: 201x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 2x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.jpg`: 86x Excluded (Explicitly Denied Extension: '.jpg'), 1x Excluded (Explicitly Denied Extension: '.JPG')
- `.json`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 25562 LOC), 1x Excluded (Massive Static Asset Blob: 3872 LOC)
- `.ktx`: 38x Excluded (Binary Format Detected)
- `.dds`: 31x Excluded (Binary Format Detected)
- `.tsx`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.wasm`: 23x Excluded (Binary Format Detected), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 10166 LOC)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 1 exceeds 500 chars), 3x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.scss`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gltf`: 13x Excluded (Explicitly Denied Extension: '.gltf')
- `.glsl`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 19.5 | 7.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.8 | 37.7 | 51.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 32.7 | 33.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.5 | 23.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.9 | 0.1 | 0.1 | 0.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 98.5 | 17.7 | 22.4 | 22.4 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.8 | 3.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4396 | 1394 | 2 | `packages/dev/core/src/FlowGraph/Blocks/Data/Math/flowGraphMathBlocks.ts` |
| cleanup | 2511 | 747 | 2 | `packages/tools/viewer/src/viewer.ts` |
| guards | 28487 | 2147 | 13 | `packages/tools/babylonServer/public/ammo.wasm.js` |
| danger | 11546 | 1726 | 6 | `packages/tools/babylonServer/public/gltf_validator.js` |
| concurrency | 10539 | 1017 | 4 | `packages/tools/flowGraphEditor/test/playwright/flowGraphEditor.test.ts` |
| connectivity | 41032 | 3397 | 21 | `packages/dev/core/src/Maths/math.vector.ts` |
| io | 2081 | 376 | 0 | `packages/tools/playground/src/tools/monaco/monacoManager.ts` |
| crypto | 2 | 2 | 0 | `packages/tools/babylonServer/public/basis_encoder.js` |
| ipc | 119 | 36 | 0 | `packages/dev/core/src/Meshes/Compression/dracoCompressionWorker.ts` |
| time | 471 | 173 | 0 | `packages/tools/babylonServer/public/gltf_validator.js` |
| serialization | 472 | 145 | 0 | `packages/dev/serializers/test/integration/glTFSerializer.test.ts` |
| regex | 1196 | 260 | 0 | `packages/dev/buildTools/src/generateDeclaration.ts` |
| events | 3558 | 560 | 1 | `packages/dev/core/src/Materials/shaderMaterial.ts` |
| tests | 5968 | 136 | 0 | `packages/dev/core/test/unit/Math/babylon.math.vector.test.ts` |
| docs | 37725 | 2517 | 20 | `packages/tools/babylonServer/public/cannon.js` |
| debt | 1191 | 290 | 0 | `packages/tools/babylonServer/public/gltf_validator.js` |
| mutation | 166697 | 3101 | 85 | `packages/tools/babylonServer/public/gltf_validator.js` |
| dead_code | 2573 | 255 | 0 | `packages/tools/babylonServer/public/ammo.wasm.js` |
| credential | 31 | 12 | 0 | `packages/tools/playground/public/index.js` |
| threat | 31 | 21 | 0 | `scripts/generateChangelog.js` |
| ml_ai | 4326 | 618 | 2 | `packages/dev/loaders/test/unit/Interactivity/interactivity.math nodes.test.ts` |
| ui | 21686 | 1105 | 13 | `packages/dev/inspector/src/components/actionTabs/tabs/propertyGrids/materials/pbrMaterialPropertyGridComponent.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/tools/playground/src/tools/monaco/monacoManager.ts` (Hits: 53)
- `packages/tools/playground/src/components/editor/monacoComponent.tsx` (Hits: 49)
- `packages/dev/buildTools/src/generateDeclaration.ts` (Hits: 46)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.ts** (`packages/dev/core/src/types.ts`) — 595 inbound connections
2. **math.vector.ts** (`packages/dev/core/src/Maths/math.vector.ts`) — 499 inbound connections
3. **typeStore.ts** (`packages/dev/core/src/Misc/typeStore.ts`) — 420 inbound connections
4. **scene.ts** (`packages/dev/core/src/scene.ts`) — 402 inbound connections
5. **index.ts** (`packages/dev/serializers/src/3MF/core/index.ts`) — 274 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **blockTools.ts** (`packages/tools/nodeEditor/src/blockTools.ts`) — 117 outbound dependencies
2. **propertyGridTabComponent.tsx** (`packages/dev/inspector/src/components/actionTabs/tabs/propertyGridTabComponent.tsx`) — 116 outbound dependencies
3. **index.ts** (`packages/dev/core/src/PostProcesses/index.ts`) — 102 outbound dependencies
4. **index.ts** (`packages/dev/inspector-v2/src/index.ts`) — 97 outbound dependencies
5. **index.ts** (`packages/dev/core/src/Misc/index.ts`) — 89 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `dartProgram` **(Defensive Guards)** (@ `packages/tools/babylonServer/public/gltf_validator.js`) -> Impact: **4709.8** | LOC: 10996
- `attachControl` **(Many-Argument Workhorses)** (@ `packages/dev/core/src/Inputs/scene.inputManager.ts`) -> Impact: **434.3** | LOC: 546
  * *Intent:* /** * Attach events to the canvas (To handle actionManagers triggers and raise onPointerMove, onPointerDown and onPointerUp */
- `_mergeCoroutine` **(Many-Argument Workhorses)** (@ `packages/dev/core/src/Meshes/mesh.vertexData.ts`) -> Impact: **429.1** | LOC: 436
  * *Intent:* /** */
- `GetBlockFromString` **(Many-Argument Workhorses)** (@ `packages/tools/nodeEditor/src/blockTools.ts`) -> Impact: **410.4** | LOC: 609
- `CreateDecal` **(Many-Argument Workhorses)** (@ `packages/dev/core/src/Meshes/Builders/decalBuilder.ts`) -> Impact: **370.2** | LOC: 484
  * *Intent:* * * The parameter `normal` (Vector3, default `Vector3.Up`) sets the normal of the mesh where the decal is applied onto in World coordinates * * The pa...
- `ShowPickerDialogAsync` **(Many-Argument Workhorses)** (@ `packages/dev/gui/src/2D/controls/colorpicker.ts`) -> Impact: **353.5** | LOC: 1042
  * *Intent:* * This function expands the color picker by creating a color picker dialog with manual * color value input and the ability to save colors into an arra...
- `_createTextureBase` **(Many-Argument Workhorses)** (@ `packages/dev/core/src/Engines/abstractEngine.ts`) -> Impact: **296.4** | LOC: 239
- `UploadDDSLevels` **(Many-Argument Workhorses)** (@ `packages/dev/core/src/Misc/dds.ts`) -> Impact: **289.4** | LOC: 286
  * *Intent:* /** * Uploads DDS Levels to a Babylon Texture */
- `isReadyForSubMesh` **(Many-Argument Workhorses)** (@ `packages/dev/core/src/Materials/standardMaterial.ts`) -> Impact: **287.6** | LOC: 593
  * *Intent:* /** * Get if the submesh is ready to be used and all its information available. * Child classes can use it to update shaders */
- `CreateV2Runner` **(Many-Argument Workhorses)** (@ `packages/tools/playground/src/tools/monaco/run/runner.ts`) -> Impact: **273.7** | LOC: 594
  * *Intent:* /** */

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/dev/core/src/Meshes` | 31 | 17985.2 | 34.72% | 0.26% |
| `packages/dev/core/src/Misc` | 83 | 14794.52 | 35.95% | 1.91% |
| `packages/dev/core/src/Engines` | 25 | 14048.62 | 20.72% | 6.1% |
| `packages/dev/core/src/Materials` | 46 | 11989.06 | 30.53% | 0.93% |
| `packages/dev/gui/src/2D/controls` | 26 | 11010.56 | 43.87% | 3.13% |
| `packages/dev/core/src/Particles` | 22 | 9649.28 | 32.96% | 3.68% |
| `packages/dev/core/src/Meshes/Builders` | 26 | 7564.28 | 52.23% | 0.43% |
| `packages/dev/core/src/Rendering` | 27 | 7515.58 | 32.1% | 2.7% |
| `packages/dev/core/src/Engines/WebGPU` | 31 | 7349.1 | 48.47% | 4.34% |
| `packages/dev/core/src/Maths` | 24 | 6963.76 | 17.84% | 7.9% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/tools/babylonServer/public/ammo.wasm.js` -> **100.0%** Exposure
- `packages/dev/core/src/Actions/directAudioActions.ts` -> **100.0%** Exposure
- `packages/dev/core/src/Engines/ICanvas.ts` -> **100.0%** Exposure
- `packages/dev/core/src/LibDeclarations/webgl2.d.ts` -> **100.0%** Exposure
- `packages/dev/core/src/LibDeclarations/webgpu.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/tools/babylonServer/public/ammo.wasm.js` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/audiov2-test.js` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/cannon.js` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/gltf_validator.js` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/recast.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/tools/babylonServer/public/ammo.wasm.js` -> **1593** Orphaned Functions | **0** Duplicates
- `packages/tools/babylonServer/public/gltf_validator.js` -> **42** Orphaned Functions | **108** Duplicates
- `packages/dev/core/src/LibDeclarations/webgpu.d.ts` -> **50** Orphaned Functions | **54** Duplicates
- `packages/dev/loaders/src/glTF/2.0/Extensions/objectModelMapping.ts` -> **0** Orphaned Functions | **51** Duplicates
- `packages/dev/core/src/LibDeclarations/webxr.d.ts` -> **38** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `51` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10924` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.089
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dev/core/src/Meshes/mesh.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.88)
- **Top Global Matches:** file_cluster_4: 6.88, file_cluster_6: 9.959, file_cluster_12: 12.92
- **Magnitude:** 4767.56 | **LOC:** 5919 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **157** in-repo importer(s); it depends on **43**; blast radius 2.706; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 4.5213% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parse` **(Many-Argument Workhorses)** (Impact: 249.1)
    * *Intent:* /** * Returns a new Mesh object parsed from the source provided. */
  * `render` **(Many-Argument Workhorses)** (Impact: 162.3)
    * *Intent:* /** * Triggers the draw call for the mesh. Usually, you don't need to call this method by your own b...
  * `_updateInstancedBuffers` **(Many-Argument Workhorses)** (Impact: 148.9)
    * *Intent:* /** * This method will also draw the instances if fillMode and effect are passed */
  * `_MergeMeshesCoroutine` **(Many-Argument Workhorses)** (Impact: 124.8)
  * `_copySource` **(Many-Argument Workhorses)** (Impact: 92.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 527 instances
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 1702
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1111`, `structural_boundaries: 411`, `args: 209`, `func_start: 195`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 648`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 284`, `concurrency: 20`, `import: 43`
* *Defense:* `safety: 36`, `doc: 282`, `immutability_locks: 20`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.706
  * `Choke Point (Betweenness):` 0.003432 | `Ripple Effect (Closeness):` 0.139483
  * `Imports (Out-Degree: 41):` animatable.interface, skeleton, buffer, camera, boundingSphere, constants, sceneLoaderFlags, drawWrapper...
  * `Imported By (In-Degree: 157):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Engines/thinEngine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.282)
- **Top Global Matches:** file_cluster_4: 6.282, file_cluster_12: 10.744, file_cluster_6: 11.821
- **Magnitude:** 3889.82 | **LOC:** 4665 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **40**; blast radius 0.507; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (78.6%), Guard Balance (formerly Safety Score) (69.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.0%)
- **Documentation Coverage:** 14.5658% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getRGBABufferInternalSizedFormat` **(Many-Argument Workhorses)** (Impact: 205.1)
    * *Intent:* /** */
  * `_createInternalTexture` **(Many-Argument Workhorses)** (Impact: 142.2)
    * *Intent:* /** * Creates an internal texture without binding it to a framebuffer */
  * `constructor` **(Many-Argument Workhorses)** (Impact: 112.6)
    * *Intent:* /** * Creates a new engine */
  * `_initGLContext` **(I/O & Config Routines)** (Impact: 111.0)
  * `bindFramebuffer` **(Many-Argument Workhorses)** (Impact: 108.8)
    * *Intent:* /** * Binds the frame buffer to the specified texture. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 400 instances
* *State Mutation (weighted view):* 1285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 943`, `structural_boundaries: 545`, `args: 189`, `func_start: 184`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 485`, `dead_code: 7`, `fragile_debt: 1`
* *Architecture:* `api: 174`, `concurrency: 6`, `import: 40`
* *Defense:* `safety: 38`, `doc: 179`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.507
  * `Choke Point (Betweenness):` 0.00122 | `Ripple Effect (Closeness):` 0.099694
  * `Imports (Out-Degree: 38):` buffer, dataBuffer, hardwareTextureWrapper, internalTexture, renderTargetTexture, textureCreationOptions, thinTexture, videoTexture...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Maths/math.vector.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.466)
- **Top Global Matches:** file_cluster_0: 8.466, file_cluster_15: 10.488, file_cluster_11: 11.038
- **Magnitude:** 3875.7 | **LOC:** 8881 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **499** in-repo importer(s); it depends on **13**; blast radius 15.401; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 6.2128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decompose` **(Many-Argument Workhorses)** (Impact: 65.0)
    * *Intent:* /** * Decomposes the current Matrix into a translation, rotation and scaling components * Example Pl...
  * `ProjectOnTriangleToRef` **(Many-Argument Workhorses)** (Impact: 41.4)
    * *Intent:* /** * Projects "vector" on the triangle determined by its extremities "p0", "p1" and "p2", stores th...
  * `PerspectiveFovRHToRef` **(Many-Argument Workhorses)** (Impact: 36.5)
    * *Intent:* /** * Stores a right-handed perspective projection into a given matrix * Example Playground - https:...
  * `PerspectiveFovLHToRef` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* /** * Stores a left-handed perspective projection into a given matrix * Example Playground - https:/...
  * `equals` **(Compute Cores)** (Impact: 32.8)
    * *Intent:* /** * Check equality between this matrix and a second one */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 229 instances
* *State Mutation (weighted view):* 1309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 828`, `args: 594`, `func_start: 594`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 851`, `dead_code: 2`, `duplicate_logic: 44`
* *Architecture:* `api: 622`, `import: 13`
* *Defense:* `safety: 6`, `doc: 590`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.401
  * `Choke Point (Betweenness):` 0.006711 | `Ripple Effect (Closeness):` 0.186019
  * `Imports (Out-Degree: 13):` engineStore, performanceConfigurator, transformNode, arrayTools, typeStore, types, thinMath.matrix.functions, math.constants...
  * `Imported By (In-Degree: 499):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/scene.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.752)
- **Top Global Matches:** file_cluster_0: 8.752, file_cluster_12: 9.431, file_cluster_4: 9.622
- **Magnitude:** 3831.24 | **LOC:** 6733 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **402** in-repo importer(s); it depends on **83**; blast radius 8.595; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (65.7%), Guard Balance (formerly Safety Score) (63.9%)
- **Documentation Coverage:** 5.5389% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_renderForCamera` **(Many-Argument Workhorses)** (Impact: 123.3)
    * *Intent:* /** */
  * `isReady` **(Compute Cores)** (Impact: 90.4)
    * *Intent:* /** * This function will check if the scene can be rendered (textures are loaded, shaders are compil...
  * `render` **(Many-Argument Workhorses)** (Impact: 86.4)
    * *Intent:* /** * Render the scene */
  * `_renderWithFrameGraph` **(Many-Argument Workhorses)** (Impact: 80.3)
  * `freezeActiveMeshes` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* /** * Use this function to stop evaluating active meshes. The current list will be keep alive betwee...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 330 instances
* *Concurrency (weighted view):* 120
* *State Mutation (weighted view):* 1145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 812`, `structural_boundaries: 751`, `args: 408`, `func_start: 348`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 485`
* *Architecture:* `api: 541`, `concurrency: 90`, `import: 83`
* *Defense:* `safety: 31`, `doc: 550`, `immutability_locks: 8`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.595
  * `Choke Point (Betweenness):` 0.031359 | `Ripple Effect (Closeness):` 0.166202
  * `Imports (Out-Degree: 83):` abstractActionManager, action, actionEvent, animatable.core, animatable.interface, animation, animationGroup, animationPropertiesOverride...
  * `Imported By (In-Degree: 402):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Engines/webgpuEngine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.403)
- **Top Global Matches:** file_cluster_4: 8.403, file_cluster_12: 9.919, file_cluster_5: 10.717
- **Magnitude:** 3210.26 | **LOC:** 4190 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **83**; blast radius 0.42; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.6%), Connectivity (formerly Api Exposure) (68.4%)
- **Documentation Coverage:** 13.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_startRenderTargetRenderPass` **(Many-Argument Workhorses)** (Impact: 207.1)
    * *Intent:* //------------------------------------------------------------------------------ // Render Pass //--...
  * `_draw` **(Many-Argument Workhorses)** (Impact: 117.0)
  * `createEffect` **(Many-Argument Workhorses)** (Impact: 96.2)
    * *Intent:* * Create a new effect (used to store vertex/fragment shaders) */
  * `_createInternalTexture` **(Many-Argument Workhorses)** (Impact: 78.1)
    * *Intent:* /** * Creates an internal texture without binding it to a framebuffer */
  * `createTexture` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 282 instances
* *Concurrency (weighted view):* 75
* *State Mutation (weighted view):* 957
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 733`, `structural_boundaries: 405`, `args: 204`, `func_start: 179`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 393`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 170`, `concurrency: 30`, `import: 66`
* *Defense:* `safety: 108`, `doc: 206`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.000595 | `Ripple Effect (Closeness):` 0.005842
  * `Imports (Out-Degree: 76):` audioEngine, buffer, buffer.align, dataBuffer, storageBuffer, computeEffect, baseTexture, externalTexture...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `packages/dev/loaders/src/glTF/2.0/glTFLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.82)
- **Top Global Matches:** file_cluster_4: 6.82, file_cluster_12: 10.024, file_cluster_16: 10.298
- **Magnitude:** 2523.5 | **LOC:** 3155 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **48**; blast radius 1.217; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.4%)
- **Documentation Coverage:** 38.0117% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_loadAsync` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `loadNodeAsync` **(Many-Argument Workhorses)** (Impact: 56.2)
    * *Intent:* /** * Loads a glTF node. */
  * `_loadAnimationChannelAsync` **(Many-Argument Workhorses)** (Impact: 54.8)
    * *Intent:* /** * Loads a glTF animation channel. */
  * `_loadMeshPrimitiveAsync` **(Many-Argument Workhorses)** (Impact: 44.3)
    * *Intent:* /** */
  * `_loadAccessorAsync` **(Many-Argument Workhorses)** (Impact: 42.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 235 instances
* *Concurrency (weighted view):* 349
* *State Mutation (weighted view):* 788
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 612`, `args: 235`, `func_start: 119`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 318`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 15`, `api: 64`, `concurrency: 134`, `import: 50`
* *Defense:* `safety: 29`, `doc: 77`, `immutability_locks: 7`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.217
  * `Choke Point (Betweenness):` 0.001187 | `Ripple Effect (Closeness):` 0.009836
  * `Imports (Out-Degree: 13):` glTFFileLoader, objectModelMapping, glTFLoaderAnimation, glTFLoaderExtension, glTFLoaderExtensionRegistry, glTFLoaderInterfaces, materialLoadingAdapter, openpbrMaterialLoadingAdapter...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Meshes/mesh.vertexData.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.623)
- **Top Global Matches:** file_cluster_6: 9.623, file_cluster_8: 11.901, file_cluster_4: 16.475
- **Magnitude:** 2165.26 | **LOC:** 2429 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **61** in-repo importer(s); it depends on **13**; blast radius 1.065; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (86.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%)
- **Documentation Coverage:** 10.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mergeCoroutine` **(Many-Argument Workhorses)** (Impact: 429.1)
    * *Intent:* /** */
  * `ComputeNormals` **(Many-Argument Workhorses)** (Impact: 119.6)
    * *Intent:* * * facetNormals : optional array of facet normals (vector3) * * facetPositions : optional array of ...
  * `_applyToCoroutine` **(Many-Argument Workhorses)** (Impact: 86.2)
    * *Intent:* /** */
  * `_ComputeSides` **(Many-Argument Workhorses)** (Impact: 51.6)
    * *Intent:* /** */
  * `_ExtractFrom` **(Many-Argument Workhorses)** (Impact: 50.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 785
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 559`, `structural_boundaries: 116`, `args: 83`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 303`, `dead_code: 2`
* *Architecture:* `api: 68`, `import: 13`
* *Defense:* `safety: 7`, `doc: 94`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.065
  * `Choke Point (Betweenness):` 0.000517 | `Ripple Effect (Closeness):` 0.115153
  * `Imports (Out-Degree: 13):` buffer, math.color, math.vector, geometry, mesh, coroutine, decorators, devTools...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `packages/dev/loaders/src/glTF/1.0/glTFLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.149)
- **Top Global Matches:** file_cluster_4: 7.149, file_cluster_6: 8.504, file_cluster_12: 13.674
- **Magnitude:** 1928.74 | **LOC:** 2355 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **34**; blast radius 0.155; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.4%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 55.3398% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoadMaterialAsync` **(Many-Argument Workhorses)** (Impact: 148.0)
    * *Intent:* // eslint-disable-next-line no-restricted-syntax
  * `ImportNode` **(Many-Argument Workhorses)** (Impact: 132.0)
    * *Intent:* /** * Imports a node */
  * `ImportMesh` **(Many-Argument Workhorses)** (Impact: 106.5)
    * *Intent:* /** * Imports a mesh and its geometries */
  * `OnBindShaderMaterial` **(Many-Argument Workhorses)** (Impact: 76.1)
    * *Intent:* /** * onBind shaderrs callback to set uniforms and matrices */
  * `ImportSkeleton` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* /** * Imports a skeleton */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 221 instances
* *State Mutation (weighted view):* 682
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 409`, `args: 117`, `func_start: 69`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 240`
* *Architecture:* `io: 1`, `api: 40`, `concurrency: 10`, `import: 34`
* *Defense:* `safety: 1`, `doc: 43`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.000651
  * `Imports (Out-Degree: 8):` glTFFileLoader, glTFLoaderInterfaces, glTFLoaderUtils, animation, bone, skeleton, buffer, bufferUtils...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Engines/abstractEngine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.82)
- **Top Global Matches:** file_cluster_12: 8.82, file_cluster_5: 9.345, file_cluster_0: 10.668
- **Magnitude:** 1898.16 | **LOC:** 2848 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 90.0%
- **Blast Radius:** changing it is visible to **139** in-repo importer(s); it depends on **52**; blast radius 4.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (98.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 5.8659% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_createTextureBase` **(Many-Argument Workhorses)** (Impact: 296.4)
  * `constructor` **(Defensive Guards)** (Impact: 54.2)
    * *Intent:* /** * Creates a new engine */
  * `createTexture` **(Many-Argument Workhorses)** (Impact: 48.9)
    * *Intent:* */
  * `createEffect` **(Many-Argument Workhorses)** (Impact: 38.8)
    * *Intent:* * Create a new effect (used to store vertex/fragment shaders) */
  * `resize` **(Defensive Guards)** (Impact: 29.7)
    * *Intent:* /** * Resize the view according to the canvas' size */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 109 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 368`, `args: 214`, `func_start: 189`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 141`
* *Architecture:* `api: 257`, `concurrency: 35`, `import: 52`
* *Defense:* `safety: 26`, `doc: 299`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.573
  * `Choke Point (Betweenness):` 0.008509 | `Ripple Effect (Closeness):` 0.153068
  * `Imports (Out-Degree: 49):` IAudioEngine, IAudioEngineOptions, dataBuffer, storageBuffer, loadingScreen, internalTextureLoader, hardwareTextureWrapper, internalTexture...
  * `Imported By (In-Degree: 139):` (Excluded from Brief to save tokens)

### `packages/dev/gui/src/2D/controls/control.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.289)
- **Top Global Matches:** file_cluster_12: 7.289, file_cluster_15: 7.432, file_cluster_16: 8.011
- **Magnitude:** 1894.06 | **LOC:** 2895 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **26**; blast radius 1.642; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 20.6897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_processObservables` **(Many-Argument Workhorses)** (Impact: 62.8)
    * *Intent:* /** */
  * `_computeAlignment` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* /** */
  * `_onPointerUp` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* /** */
  * `_parseFromContent` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* /** */
  * `_onPointerPick` **(Many-Argument Workhorses)** (Impact: 27.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 180 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 311`, `args: 218`, `func_start: 212`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 226`
* *Architecture:* `api: 244`, `concurrency: 19`, `import: 26`
* *Defense:* `safety: 15`, `doc: 211`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.642
  * `Choke Point (Betweenness):` 0.000944 | `Ripple Effect (Closeness):` 0.009737
  * `Imports (Out-Degree: 11):` advancedDynamicTexture, math2D, measure, style, valueAndUnit, container, focusableControl, BaseGradient...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Materials/PBR/pbrBaseMaterial.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.541)
- **Top Global Matches:** file_cluster_6: 7.541, file_cluster_8: 10.641, file_cluster_4: 14.926
- **Magnitude:** 1852.8 | **LOC:** 2535 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **45**; blast radius 0.263; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 8.6207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bindForSubMesh` **(Many-Argument Workhorses)** (Impact: 229.6)
    * *Intent:* /** * Binds the submesh data. */
  * `_prepareDefines` **(Many-Argument Workhorses)** (Impact: 219.4)
  * `isReadyForSubMesh` **(Many-Argument Workhorses)** (Impact: 172.3)
    * *Intent:* /** * Specifies that the submesh is ready to be used. */
  * `_prepareEffect` **(Many-Argument Workhorses)** (Impact: 122.5)
  * `getAnimatables` **(Compute Cores)** (Impact: 47.0)
    * *Intent:* /** * Returns the animatable textures. * If material have animatable metallic texture, then reflecti...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 167 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 538
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 163`, `args: 35`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 204`
* *Architecture:* `api: 289`, `concurrency: 5`, `import: 44`
* *Defense:* `safety: 23`, `doc: 118`, `immutability_locks: 15`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.000795 | `Ripple Effect (Closeness):` 0.062863
  * `Imports (Out-Degree: 41):` animatable.interface, buffer, constants, baseTexture, baseTexture.polynomial, renderTargetTexture, effect, imageProcessingConfiguration...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Engines/thinNativeEngine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.919)
- **Top Global Matches:** file_cluster_12: 7.919, file_cluster_5: 9.236, file_cluster_4: 9.783
- **Magnitude:** 1851.32 | **LOC:** 2613 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **41**; blast radius 0.297; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.2%), Guard Balance (formerly Safety Score) (61.9%)
- **Documentation Coverage:** 56.2682% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createTexture` **(Many-Argument Workhorses)** (Impact: 216.1)
    * *Intent:* */
  * `_readTexturePixels` **(Many-Argument Workhorses)** (Impact: 71.6)
  * `_createInternalTexture` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `_setTexture` **(Many-Argument Workhorses)** (Impact: 45.4)
    * *Intent:* // TODO: Refactor to share more logic with base Engine implementation. /** */
  * `_initializeNativeEngine` **(Compute Cores)** (Impact: 32.7)
    * *Intent:* ////////////////////////////////////////////////////////////////////// /** * Keeps as a separate fun...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 103 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 425
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 342`, `args: 187`, `func_start: 175`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 219`, `dead_code: 1`, `planned_debt: 12`, `fragile_debt: 1`
* *Architecture:* `api: 157`, `concurrency: 19`, `import: 40`
* *Defense:* `safety: 37`, `doc: 78`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.297
  * `Choke Point (Betweenness):` 0.000151 | `Ripple Effect (Closeness):` 0.002906
  * `Imports (Out-Degree: 41):` buffer, buffer.align, buffer.nonFloatVertexBuffers, dataBuffer, timeToken, baseTexture, hardwareTextureWrapper, internalTexture...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Meshes/abstractMesh.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.05)
- **Top Global Matches:** file_cluster_12: 8.05, file_cluster_0: 8.115, file_cluster_15: 8.116
- **Magnitude:** 1809.32 | **LOC:** 2829 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **164** in-repo importer(s); it depends on **42**; blast radius 3.158; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.2%)
- **Documentation Coverage:** 5.3672% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `intersects` **(Many-Argument Workhorses)** (Impact: 106.4)
    * *Intent:* /** * Checks if the passed Ray intersects with the mesh. A mesh triangle can be picked both from its...
  * `dispose` **(Many-Argument Workhorses)** (Impact: 66.0)
    * *Intent:* /** * Releases resources associated with this abstract mesh. */
  * `_getData` **(Many-Argument Workhorses)** (Impact: 59.4)
  * `getClosestFacetAtLocalCoordinates` **(Many-Argument Workhorses)** (Impact: 37.2)
    * *Intent:* /** * Returns the closest mesh facet index at (x,y,z) local coordinates, null if not found */
  * `updateFacetData` **(I/O & Config Routines)** (Impact: 34.6)
    * *Intent:* /** * Updates the mesh facetData arrays and the internal partitioning when the mesh is morphed or up...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 172 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 570
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 336`, `structural_boundaries: 300`, `args: 192`, `func_start: 183`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 226`
* *Architecture:* `api: 275`, `concurrency: 8`, `import: 42`
* *Defense:* `safety: 7`, `doc: 228`, `immutability_locks: 4`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.158
  * `Choke Point (Betweenness):` 0.004543 | `Ripple Effect (Closeness):` 0.143971
  * `Imports (Out-Degree: 42):` abstractActionManager, bakedVertexAnimationManager, skeleton, buffer, camera, collider, intersectionInfo, meshCollisionData...
  * `Imported By (In-Degree: 164):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Meshes/GaussianSplatting/gaussianSplattingMeshBase.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.228)
- **Top Global Matches:** file_cluster_4: 6.228, file_cluster_12: 10.404, file_cluster_6: 11.421
- **Magnitude:** 1738.4 | **LOC:** 2398 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 0.138; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Concurrency Surface (formerly Concurrency) (62.2%)
- **Documentation Coverage:** 23.4783% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_ValueNameToEnum` **(Compute Cores)** (Impact: 136.2)
  * `_GetSplat` **(Many-Argument Workhorses)** (Impact: 104.8)
  * `_updateData` **(Many-Argument Workhorses)** (Impact: 83.3)
  * `_postToWorker` **(Compute Cores)** (Impact: 50.6)
  * `_GetCompressedChunks` **(Many-Argument Workhorses)** (Impact: 49.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 189 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 323`, `args: 87`, `func_start: 76`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 284`
* *Architecture:* `api: 48`, `concurrency: 25`, `import: 22`
* *Defense:* `safety: 27`, `doc: 74`, `immutability_locks: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.003004
  * `Imports (Out-Degree: 5):` abstractMesh, mesh, mesh.vertexData, subMesh, camera, nativeInterfaces, constants, engineStore...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Particles/thinParticleSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.816)
- **Top Global Matches:** file_cluster_4: 5.816, file_cluster_12: 9.175, file_cluster_15: 9.743
- **Magnitude:** 1730.68 | **LOC:** 2435 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **35**; blast radius 0.235; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (71.2%), Guard Balance (formerly Safety Score) (70.7%)
- **Documentation Coverage:** 8.2418% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_appendParticleVertex` **(Many-Argument Workhorses)** (Impact: 62.1)
    * *Intent:* /** */
  * `constructor` **(Many-Argument Workhorses)** (Impact: 61.7)
    * *Intent:* /** * Instantiates a particle system. * Particles are often small sprites used to simulate hard-to-r...
  * `_render` **(Defensive Guards)** (Impact: 58.8)
  * `animate` **(Compute Cores)** (Impact: 43.6)
    * *Intent:* /** * Animates the particle system for the current frame by emitting new particles and or animating ...
  * `fillDefines` **(Many-Argument Workhorses)** (Impact: 40.5)
    * *Intent:* /** * Fill the defines array according to the current settings of the particle system */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 225 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 743
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 203`, `args: 117`, `func_start: 100`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 293`
* *Architecture:* `api: 120`, `concurrency: 14`, `import: 34`
* *Defense:* `safety: 22`, `doc: 119`, `immutability_locks: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.235
  * `Choke Point (Betweenness):` 0.000337 | `Ripple Effect (Closeness):` 0.060883
  * `Imports (Out-Degree: 30):` animatable.interface, buffer, dataBuffer, engine.alpha, abstractEngine, constants, engineStore, thinEngine...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Particles/solidParticleSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.056)
- **Top Global Matches:** file_cluster_4: 7.056, file_cluster_12: 11.12, file_cluster_6: 11.163
- **Magnitude:** 1715.66 | **LOC:** 2184 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.1%)
- **Documentation Coverage:** 3.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setParticles` **(Many-Argument Workhorses)** (Impact: 223.3)
    * *Intent:* /** * Sets all the particles : this method actually really updates the mesh according to the particl...
  * `_meshBuilder` **(Many-Argument Workhorses)** (Impact: 122.2)
    * *Intent:* */
  * `constructor` **(Many-Argument Workhorses)** (Impact: 78.5)
    * *Intent:* */
  * `digest` **(Many-Argument Workhorses)** (Impact: 62.2)
    * *Intent:* * Thus the particles generated from `digest()` have their property `position` set yet. * {delta} (op...
  * `_insertNewParticle` **(Many-Argument Workhorses)** (Impact: 41.5)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *State Mutation (weighted view):* 790
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 107`, `args: 70`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 322`, `planned_debt: 1`
* *Architecture:* `api: 66`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 7`, `doc: 79`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.001242 | `Ripple Effect (Closeness):` 0.086289
  * `Imports (Out-Degree: 21):` buffer, targetCamera, pickingInfo, boundingInfo, engineStore, pbrMaterial, material, multiMaterial...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Materials/PBR/openpbrMaterial.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.257)
- **Top Global Matches:** file_cluster_4: 7.257, file_cluster_6: 10.873, file_cluster_12: 12.227
- **Magnitude:** 1672.48 | **LOC:** 3075 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **44**; blast radius 0.104; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.5%), Guard Balance (formerly Safety Score) (63.1%)
- **Documentation Coverage:** 13.1313% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_prepareDefines` **(Many-Argument Workhorses)** (Impact: 166.3)
  * `_prepareEffect` **(Many-Argument Workhorses)** (Impact: 129.0)
  * `isReadyForSubMesh` **(Many-Argument Workhorses)** (Impact: 118.0)
    * *Intent:* /** * Specifies that the submesh is ready to be used. */
  * `bindForSubMesh` **(Many-Argument Workhorses)** (Impact: 109.9)
    * *Intent:* /** * Binds the submesh data. */
  * `constructor` **(Many-Argument Workhorses)** (Impact: 59.7)
    * *Intent:* /** * Instantiates a new OpenPBRMaterial instance. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 143 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 171`, `args: 63`, `func_start: 53`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 211`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 348`, `concurrency: 5`, `import: 44`
* *Defense:* `safety: 10`, `doc: 260`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.071273
  * `Imports (Out-Degree: 37):` animatable.interface, buffer, constants, engine, baseTexture, effect, material, uniformBuffer...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Physics/v2/Plugins/havokPlugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.258)
- **Top Global Matches:** file_cluster_4: 7.258, file_cluster_12: 7.694, file_cluster_15: 9.904
- **Magnitude:** 1663.9 | **LOC:** 3046 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 0.181; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.6%), Connectivity (formerly Api Exposure) (52.9%)
- **Documentation Coverage:** 11.6379% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initConstraint` **(Many-Argument Workhorses)** (Impact: 113.9)
    * *Intent:* // constraint /** * Initializes a physics constraint with the given parameters. * * * This function ...
  * `initShape` **(Many-Argument Workhorses)** (Impact: 77.3)
    * *Intent:* /** * Initializes a physics shape with the given type and parameters. * * This code is useful for in...
  * `raycast` **(Many-Argument Workhorses)** (Impact: 54.5)
    * *Intent:* /** * Performs a raycast from a given start point to a given end point and stores the result in a gi...
  * `setPhysicsBodyTransformation` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* /** * Sets the transformation of the given physics body to the given transform node. * Sets the tran...
  * `executeStep` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* /** * Executes a single step of the physics engine. * * * This method is useful for simulating the p...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 94 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 455`, `structural_boundaries: 318`, `args: 147`, `func_start: 133`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 156`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `api: 121`, `concurrency: 11`, `import: 23`
* *Defense:* `safety: 73`, `doc: 131`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.181
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.000488
  * `Imports (Out-Degree: 23):` buffer, boundingBox, floatingOriginMatrixOverrides, math.vector, instancedMesh, mesh, transformNode, arrayTools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Particles/gpuParticleSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.432)
- **Top Global Matches:** file_cluster_4: 7.432, file_cluster_12: 9.47, file_cluster_5: 10.487
- **Magnitude:** 1651.72 | **LOC:** 2310 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **39**; blast radius 0.135; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.5%), Concurrency Surface (formerly Concurrency) (58.4%)
- **Documentation Coverage:** 11.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 69.5)
    * *Intent:* /** * Renders the particle system in its current state */
  * `_initialize` **(I/O & Config Routines)** (Impact: 55.0)
  * `_render` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* /** * Instantiates a GPU particle system. * Particles are often small sprites used to simulate hard-...
  * `fillDefines` **(Many-Argument Workhorses)** (Impact: 40.8)
    * *Intent:* /** * Fill the defines array according to the current settings of the particle system */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 229 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 774
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 181`, `args: 101`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 316`
* *Architecture:* `api: 100`, `concurrency: 9`, `import: 36`
* *Defense:* `safety: 15`, `doc: 97`, `immutability_locks: 2`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.000301 | `Ripple Effect (Closeness):` 0.049141
  * `Imports (Out-Degree: 37):` animatable.interface, buffer, dataBuffer, engine.transformFeedback, abstractEngine, constants, engine, engineStore...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Materials/materialHelper.functions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.829)
- **Top Global Matches:** file_cluster_6: 6.829, file_cluster_4: 12.659, file_cluster_8: 13.775
- **Magnitude:** 1638.36 | **LOC:** 1570 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **25**; blast radius 0.324; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 1.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PrepareDefinesForIBL` **(Many-Argument Workhorses)** (Impact: 88.4)
    * *Intent:* /** * Prepare defines relating to IBL logic. */
  * `PrepareDefinesAndAttributesForMorphTargets` **(Many-Argument Workhorses)** (Impact: 76.6)
    * *Intent:* /** * Prepares the list of attributes and defines required for morph targets. */
  * `BindIBLParameters` **(Many-Argument Workhorses)** (Impact: 72.2)
    * *Intent:* * Update parameters for IBL */
  * `PrepareDefinesForLight` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* * Prepares the defines related to the light information passed in parameter */
  * `PrepareAttributesForMorphTargets` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* /** * Prepares the list of attributes required for morph targets according to the effect defines. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 703
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 146`, `args: 38`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 301`
* *Architecture:* `api: 38`, `import: 25`
* *Defense:* `safety: 4`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.324
  * `Choke Point (Betweenness):` 0.000311 | `Ripple Effect (Closeness):` 0.103808
  * `Imports (Out-Degree: 23):` abstractEngine, constants, engineStore, light, lightConstants, abstractMesh, mesh, logger...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Lights/Shadows/shadowGenerator.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.307)
- **Top Global Matches:** file_cluster_4: 6.307, file_cluster_12: 9.608, file_cluster_16: 10.905
- **Magnitude:** 1630.2 | **LOC:** 2326 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **38**; blast radius 0.282; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.7%), Connectivity (formerly Api Exposure) (55.7%)
- **Documentation Coverage:** 9.0395% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isReady` **(Many-Argument Workhorses)** (Impact: 134.8)
    * *Intent:* /** * Determine whether the shadow generator is ready or not (mainly all effects and related post pr...
  * `_renderSubMeshForShadowMap` **(Many-Argument Workhorses)** (Impact: 87.5)
  * `Parse` **(Many-Argument Workhorses)** (Impact: 82.9)
    * *Intent:* /** * Parses a serialized ShadowGenerator and returns a new ShadowGenerator. */
  * `_initializeShadowMap` **(I/O & Config Routines)** (Impact: 42.1)
  * `prepareDefines` **(Compute Cores)** (Impact: 38.3)
    * *Intent:* /** * Prepare all the defines in a material relying on a shadow map at the specified light index. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 191 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 380`, `structural_boundaries: 204`, `args: 114`, `func_start: 102`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 238`, `planned_debt: 1`
* *Architecture:* `api: 103`, `concurrency: 16`, `import: 38`
* *Defense:* `safety: 14`, `doc: 115`, `immutability_locks: 11`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.282
  * `Choke Point (Betweenness):` 0.000383 | `Ripple Effect (Closeness):` 0.098917
  * `Imports (Out-Degree: 29):` buffer, camera, constants, light, shadowLight, baseTexture, renderTargetTexture, texture...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Materials/Node/nodeMaterial.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.311)
- **Top Global Matches:** file_cluster_4: 7.311, file_cluster_12: 7.46, file_cluster_15: 9.144
- **Magnitude:** 1594.82 | **LOC:** 2676 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **71**; blast radius 0.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (87.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.8%)
- **Documentation Coverage:** 9.9338% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseSerializedObject` **(Many-Argument Workhorses)** (Impact: 67.8)
    * *Intent:* /** * Clear the current graph and load a new one from a serialization object */
  * `isReadyForSubMesh` **(Many-Argument Workhorses)** (Impact: 57.9)
    * *Intent:* /** * Get if the submesh is ready to be used and all its information available. * Child classes can ...
  * `ParseFromSnippetAsync` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* /** * Creates a node material from a snippet saved by the node material editor */
  * `_createEffectForParticles` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `_processDefines` **(Many-Argument Workhorses)** (Impact: 38.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 139 instances
* *Concurrency (weighted view):* 52
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 273`, `args: 114`, `func_start: 84`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 217`
* *Architecture:* `io: 1`, `api: 128`, `concurrency: 22`, `import: 71`
* *Defense:* `safety: 17`, `doc: 139`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.018066 | `Ripple Effect (Closeness):` 0.105091
  * `Imports (Out-Degree: 71):` buffer, camera, abstractEngine, constants, engineStore, baseTexture, materialDefines, math.color...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `packages/dev/gui/src/2D/controls/colorpicker.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.754)
- **Top Global Matches:** file_cluster_4: 7.754, file_cluster_12: 10.305, file_cluster_16: 12.293
- **Magnitude:** 1543.8 | **LOC:** 1520 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.092; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%)
- **Documentation Coverage:** 71.831% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ShowPickerDialogAsync` **(Many-Argument Workhorses)** (Impact: 353.5)
    * *Intent:* * This function expands the color picker by creating a color picker dialog with manual * color value...
  * `updateFloat` **(Compute Cores)** (Impact: 38.2)
    * *Intent:* // When the user enters a float for R, G, or B we check to make sure it is a valid number and replac...
  * `updateSwatches` **(Many-Argument Workhorses)** (Impact: 35.9)
    * *Intent:* /** * When Save Color button is pressed this function will first create a swatch drawer if one is no...
  * `updateInt` **(Compute Cores)** (Impact: 29.5)
    * *Intent:* // When the user enters an integer for R, G, or B we check to make sure it is a valid number and rep...
  * `_createColorWheelCanvas` **(Many-Argument Workhorses)** (Impact: 27.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 183 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 115`, `args: 93`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 412`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `concurrency: 6`, `import: 16`
* *Defense:* `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000347
  * `Imports (Out-Degree: 9):` advancedDynamicTexture, textBlock, measure, button, control, grid, inputText, rectangle...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Loading/sceneLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.865)
- **Top Global Matches:** file_cluster_12: 8.865, file_cluster_5: 8.915, file_cluster_4: 10.777
- **Magnitude:** 1530.24 | **LOC:** 1983 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **24**; blast radius 0.384; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (83.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.0%)
- **Documentation Coverage:** 29.5652% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadDataAsync` **(Many-Argument Workhorses)** (Impact: 189.1)
  * `importAnimationsImplAsync` **(Many-Argument Workhorses)** (Impact: 72.5)
    * *Intent:* // This is the core implementation of import animations
  * `ImportAnimations` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* * Import animations from a file into a scene */
  * `appendSceneImplAsync` **(Many-Argument Workhorses)** (Impact: 52.8)
    * *Intent:* // This is the core implementation of append scene
  * `loadAssetContainerImplAsync` **(Many-Argument Workhorses)** (Impact: 52.5)
    * *Intent:* // This is the core implementation of load asset container
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 150
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 401`, `args: 123`, `func_start: 81`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 51`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 57`, `concurrency: 90`, `import: 24`
* *Defense:* `safety: 63`, `doc: 124`, `immutability_locks: 29`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.384
  * `Choke Point (Betweenness):` 0.001015 | `Ripple Effect (Closeness):` 0.056438
  * `Imports (Out-Degree: 23):` animationGroup, skeleton, abstractEngine, constants, engineStore, light, abstractMesh, geometry...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/dev/core/src/Audio/analyser.ts` (TYPESCRIPT) | Magnitude: 118.46 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 29, structural_boundaries: 21, branch: 20
- `packages/dev/core/src/AudioV2/webAudio/webAudioStaticSound.ts` (TYPESCRIPT) | Magnitude: 486.62 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 384, branch: 108, structural_boundaries: 105, args: 45
- `packages/dev/core/src/AudioV2/abstractAudio/components/spatialAudioAttacherComponent.ts` (TYPESCRIPT) | Magnitude: 41.94 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 19, branch: 10, doc: 8
- `packages/tools/playground/src/components/editor/searchPanelComponent.tsx` (TYPESCRIPT) | Magnitude: 0.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 288, core_var_decl: 97, structural_boundaries: 67, ui_framework: 61
- `packages/dev/core/src/Misc/pressureObserverWrapper.ts` (TYPESCRIPT) | Magnitude: 43.24 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 10, safety: 8, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/tools/testsMemoryLeaks/test/unit/runner.test.ts` (TYPESCRIPT) | Magnitude: 0.05 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 28, concurrency: 17, test: 15
- `packages/dev/core/src/Particles/Node/Blocks/particleMathBlock.ts` (TYPESCRIPT) | Magnitude: 214.96 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 254, structural_boundaries: 110, branch: 58, state_mutation: 42
- `packages/dev/addons/src/navigation/common/tile-cache.ts` (TYPESCRIPT) | Magnitude: 24.8 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 12, state_mutation: 4, core_var_decl: 4
- `packages/tools/flowGraphEditor/src/graphSystem/registerToPropertyLedger.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 16, indent_spaces: 16, structural_boundaries: 14, import: 12
- `packages/dev/inspector/src/components/actionTabs/tabs/propertyGrids/animations/curveEditor/controls/controlButtonComponent.tsx` (TYPESCRIPT) | Magnitude: 8.96 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 14, ui_framework: 11, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/dev/core/src/Culling/Helper/boundingInfoHelper.ts` (TYPESCRIPT) | Magnitude: 57.28 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 34, concurrency: 15, branch: 7
- `packages/dev/core/src/Rendering/IBLShadows/iblShadowsSpatialBlurPass.ts` (TYPESCRIPT) | Magnitude: 108.88 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 40, branch: 22, args: 18
- `packages/dev/core/src/Instrumentation/sceneInstrumentation.ts` (TYPESCRIPT) | Magnitude: 350.2 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 426, state_mutation: 82, structural_boundaries: 67, branch: 54
- `packages/dev/core/src/Materials/Node/Blocks/Fragment/ambientOcclusionBlock.ts` (TYPESCRIPT) | Magnitude: 98.94 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 197, core_var_decl: 52, structural_boundaries: 44, design_snake_case: 40
- `packages/tools/vsm/src/actions/BaseBehavior.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, args: 5, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/dev/gui/src/3D/materials/mrdl/mrdlSliderBarMaterial.ts` (TYPESCRIPT) | Magnitude: 211.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 450, core_var_decl: 90, api: 89, doc: 78
- `packages/dev/core/src/Actions/abstractActionManager.ts` (TYPESCRIPT) | Magnitude: 53.24 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 21, api: 19, doc: 19
- `packages/dev/core/src/FrameGraph/Node/Blocks/PostProcesses/blurPostProcessBlock.ts` (TYPESCRIPT) | Magnitude: 34.36 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 18, api: 11, args: 10
- `packages/dev/gui/src/3D/materials/mrdl/mrdlSliderThumbMaterial.ts` (TYPESCRIPT) | Magnitude: 211.54 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 449, core_var_decl: 90, api: 89, doc: 78
- `packages/tools/nodeRenderGraphEditor/src/sharedComponents/draggableLineWithButtonComponent.tsx` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 32, ui_framework: 13, structural_boundaries: 11, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/dev/loaders/src/glTF/2.0/Extensions/KHR_mesh_quantization.ts` (TYPESCRIPT) | Magnitude: 10.08 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, doc: 8, api: 6
- `packages/dev/core/src/Materials/PBR/pbrBRDFConfiguration.ts` (TYPESCRIPT) | Magnitude: 60.48 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 80, core_var_decl: 37, api: 25, doc: 24
- `packages/public/umd/babylonjs/scripts/postinstall.js` (JAVASCRIPT) | Magnitude: 11.04 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: debug_prints: 2, decorators: 1
- `packages/public/umd/babylonjs-ktx2decoder/webpack.config.js` (JAVASCRIPT) | Magnitude: 8.52 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, io: 3, import: 3, core_var_decl: 3
- `packages/dev/core/src/Cameras/RigModes/stereoscopicAnaglyphRigMode.ts` (TYPESCRIPT) | Magnitude: 4.74 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, state_mutation: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/tools/playground/src/custom.d.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 11, api: 6, safety_bypasses: 4
- `packages/dev/core/test/unit/DeviceInput/babylon.deviceInput.test.ts` (TYPESCRIPT) | Magnitude: 19.3 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 50, core_var_decl: 48, test: 47
- `packages/dev/inspector/src/tools.ts` (TYPESCRIPT) | Magnitude: 60.92 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 54, branch: 23, structural_boundaries: 14, safety_bypasses: 10
- `packages/dev/core/test/unit/Cameras/babylon.arcRotateCameraInputs.test.ts` (TYPESCRIPT) | Magnitude: 52.46 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 189, structural_boundaries: 44, safety_bypasses: 41, core_var_decl: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/dev/core/src/Meshes/GaussianSplatting/gaussianSplattingPartProxyMesh.ts` (TYPESCRIPT) | Magnitude: 49.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 25, doc: 14, api: 13
- `packages/dev/core/src/Particles/Queue/executionQueue.ts` (TYPESCRIPT) | Magnitude: 62.12 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 14, state_mutation: 14, doc: 8
- `packages/dev/core/src/Rendering/subSurfaceConfiguration.ts` (TYPESCRIPT) | Magnitude: 66.22 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 26, doc: 20, api: 19
- `packages/tools/guiEditor/src/diagram/gizmoScalePoint.tsx` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 114, core_var_decl: 46, structural_boundaries: 40, design_camel_case: 24
- `packages/dev/core/src/FrameGraph/Passes/renderPass.ts` (TYPESCRIPT) | Magnitude: 97.62 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 99, branch: 22, structural_boundaries: 22, doc: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/dev/gui/src/3D/controls/slider3D.ts` (TYPESCRIPT) | Magnitude: 232.36 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 206, structural_boundaries: 49, state_mutation: 47, branch: 31
- `packages/dev/sharedUiComponents/src/nodeGraphSystem/graphSearch.tsx` (TYPESCRIPT) | Magnitude: 152.28 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 186, branch: 51, structural_boundaries: 33, ui_framework: 27
- `packages/tools/guiEditor/src/keyboardManager.ts` (TYPESCRIPT) | Magnitude: 0.06 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 57, args: 11, func_start: 11, structural_boundaries: 10
- `packages/dev/core/src/Cameras/Stereoscopic/stereoscopicScreenUniversalCamera.ts` (TYPESCRIPT) | Magnitude: 71.08 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 17, state_mutation: 16, args: 10
- `packages/dev/core/src/Materials/Node/Blocks/biPlanarBlock.ts` (TYPESCRIPT) | Magnitude: 39.62 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 77, core_var_decl: 19, structural_boundaries: 18, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/dev/core/src/PostProcesses/RenderPipeline/Pipelines/index.ts` (TYPESCRIPT) | Magnitude: 32.38 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 19, api: 17, import: 17
- `packages/dev/core/src/Materials/Textures/Loaders/EXR/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/dev/loaders/src/legacy/legacy.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8, doc: 1
- `packages/dev/serializers/src/3MF/core/model/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/dev/core/src/Rendering/screenSpaceReflections2Configuration.ts` (TYPESCRIPT) | Magnitude: 11.2 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, api: 5, doc: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/tools/nodeEditor/webpack.config.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, branch: 4, core_var_decl: 4, structural_boundaries: 3
- `packages/tools/nodeGeometryEditor/src/graphSystem/registerToDisplayLedger.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: state_mutation: 17, indent_spaces: 17, structural_boundaries: 11, import: 9
- `packages/dev/core/src/Materials/drawWrapper.functions.ts` (TYPESCRIPT) | Magnitude: 2.7 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, listeners: 4, import: 2, args: 1
- `packages/tools/babylonServer/webpack.config.js` (JAVASCRIPT) | Magnitude: 0.03 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 271, io: 26, dependency_injection: 26, core_var_decl: 13
- `packages/dev/core/src/Meshes/Node/Interfaces/nodeGeometryInstancingContext.ts` (TYPESCRIPT) | Magnitude: 3.16 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, doc: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/dev/sharedUiComponents/src/nodeGraphSystem/graphFrame.ts` (TYPESCRIPT) | Magnitude: 1441.14 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1372, state_mutation: 320, branch: 291, structural_boundaries: 173
- `packages/dev/core/src/Lights/lightingVolume.ts` (TYPESCRIPT) | Magnitude: 533.14 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 506, branch: 138, state_mutation: 123, core_var_decl: 75
- `packages/dev/core/src/Lights/directionalLight.ts` (TYPESCRIPT) | Magnitude: 187.16 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 43, branch: 35, core_var_decl: 27
- `packages/tools/guiEditor/src/workbenchEditor.tsx` (TYPESCRIPT) | Magnitude: 0.16 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 265, structural_boundaries: 79, ui_framework: 67, core_var_decl: 53
- `packages/dev/core/src/Materials/Node/nodeMaterialBlockConnectionPoint.ts` (TYPESCRIPT) | Magnitude: 355.36 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 431, structural_boundaries: 132, branch: 104, doc: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/dev/core/src/Actions/directAudioActions.ts` (TYPESCRIPT) | Magnitude: 33.8 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 18, doc: 10, args: 8
- `packages/dev/sharedUiComponents/src/components/reactGraphSystem/GraphLinesContainer.tsx` (TYPESCRIPT) | Magnitude: 9.52 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, branch: 5, args: 4
- `packages/dev/core/src/Engines/Extensions/engine.cubeTexture.ts` (TYPESCRIPT) | Magnitude: 249.66 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 189, branch: 48, structural_boundaries: 48, core_var_decl: 19
- `packages/tools/nodeGeometryEditor/src/components/propertyTab/propertyTabComponent.tsx` (TYPESCRIPT) | Magnitude: 0.12 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 347, ui_framework: 114, core_var_decl: 95, structural_boundaries: 77
- `packages/dev/sharedUiComponents/src/lines/draggableLineWithButtonComponent.tsx` (TYPESCRIPT) | Magnitude: 9.88 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 32, ui_framework: 22, structural_boundaries: 14, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/dev/serializers/src/glTF/2.0/glTFAnimation.ts` (TYPESCRIPT) | Magnitude: 920.3 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 816, branch: 188, core_var_decl: 138, state_mutation: 106
- `packages/dev/serializers/src/glTF/2.0/Extensions/KHR_materials_fuzz.ts` (TYPESCRIPT) | Magnitude: 206.96 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 153, branch: 43, structural_boundaries: 34, state_mutation: 32
- `packages/dev/core/src/XR/features/WebXRHandTracking.ts` (TYPESCRIPT) | Magnitude: 645.3 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 668, branch: 188, core_var_decl: 114, state_mutation: 101
- `packages/dev/core/src/Misc/khronosTextureContainer2Worker.ts` (TYPESCRIPT) | Magnitude: 219.56 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 142, branch: 44, structural_boundaries: 26, state_mutation: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/tools/flowGraphEditor/src/sharedComponents/checkBoxLineComponent.tsx` (TYPESCRIPT) | Magnitude: 0.08 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 83, ui_framework: 37, branch: 24, structural_boundaries: 22
- `packages/tools/nodeRenderGraphEditor/src/sharedComponents/checkBoxLineComponent.tsx` (TYPESCRIPT) | Magnitude: 0.08 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 83, ui_framework: 37, branch: 24, structural_boundaries: 22
- `packages/tools/babylonServer/public/test.html` (HTML) | Magnitude: 0.01 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, core_var_decl: 24, design_snake_case: 21, func_start: 18
- `packages/tools/guiEditor/src/scss/header.scss` (CSS) | Magnitude: 0.79 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 35, class_start: 4, ui_framework: 3, safety_bypasses: 1
- `packages/dev/core/src/Actions/directActions.ts` (TYPESCRIPT) | Magnitude: 245.06 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 245, structural_boundaries: 70, doc: 58, safety_bypasses: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/dev/core/src/assetContainer.ts` (TYPESCRIPT) | Magnitude: 1111.88 | Delta: **0.208** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 952, branch: 340, structural_boundaries: 165, state_mutation: 123

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/dev/core/src/Engines/WebGPU/Extensions/engine.readTexture.ts` (TYPESCRIPT) | Magnitude: 79.06 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 42, branch: 15, structural_boundaries: 12, core_var_decl: 7
- `packages/dev/inspector/src/components/actionTabs/tabs/propertyGrids/meshes/physics/physicsBodyGridComponent.tsx` (TYPESCRIPT) | Magnitude: 45.1 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 40, branch: 22, core_var_decl: 22
- `packages/dev/core/src/Engines/thinWebGPUEngine.ts` (TYPESCRIPT) | Magnitude: 99.2 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 37, branch: 31, api: 24
- `packages/dev/inspector-v2/src/components/curveEditor/bottomBar.tsx` (TYPESCRIPT) | Magnitude: 38.8 | Delta: **0.171** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 211, core_var_decl: 57, structural_boundaries: 52, design_camel_case: 40

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/dev/core/src/Engines/webgpuEngine.ts` -> Churn: **77.58%** | Cog Load: 51.9845% | Debt: 7.7165%
- `packages/tools/playground/src/tools/monaco/monacoManager.ts` -> Churn: **74.49%** | Cog Load: 89.2217% | Debt: 0.0%
- `packages/dev/core/src/Meshes/mesh.ts` -> Churn: **71.08%** | Cog Load: 52.661% | Debt: 7.9706%
- `packages/dev/inspector-v2/src/services/panes/scene/nodeExplorerService.tsx` -> Churn: **67.27%** | Cog Load: 56.5152% | Debt: 25.6695%
- `packages/dev/core/src/Meshes/GaussianSplatting/gaussianSplattingMesh.ts` -> Churn: **62.95%** | Cog Load: 53.5318% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/dev/core/src/Engines/abstractEngine.ts` -> **Babylon.js Platform** (90.0% isolated ownership) | Magnitude: 1898.16
- `packages/dev/gui/src/2D/controls/control.ts` -> **Ryan Tremblay** (100.0% isolated ownership) | Magnitude: 1894.06
- `packages/dev/core/src/Meshes/GaussianSplatting/gaussianSplattingMeshBase.ts` -> **Jesse Foltz** (100.0% isolated ownership) | Magnitude: 1738.4
- `packages/dev/core/src/Inputs/scene.inputManager.ts` -> **Ryan Tremblay** (100.0% isolated ownership) | Magnitude: 1451.86
- `packages/dev/core/src/Animations/animation.ts` -> **Ryan Tremblay** (100.0% isolated ownership) | Magnitude: 1323.58

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/dev/core/src/scene.ts` -> **Severity: 3.136** (Bridge: 0.0314 * Flux: 99.9966%)
- `packages/dev/core/src/Materials/Node/nodeMaterial.ts` -> **Severity: 1.806** (Bridge: 0.0181 * Flux: 99.9869%)
- `packages/tools/nodeEditor/src/nodeEditor.ts` -> **Severity: 1.301** (Bridge: 0.013 * Flux: 99.9643%)
- `packages/dev/core/src/PostProcesses/postProcess.ts` -> **Severity: 1.23** (Bridge: 0.0123 * Flux: 100.0%)
- `packages/dev/core/src/Engines/abstractEngine.ts` -> **Severity: 0.851** (Bridge: 0.0085 * Flux: 99.965%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/dev/core/src/types.ts` -> **Severity: 13.533** (Embedded: 0.2106 * Error Risk: 64.2466%)
- `packages/dev/core/src/Misc/observable.ts` -> **Severity: 12.965** (Embedded: 0.1735 * Error Risk: 74.7047%)
- `packages/dev/core/src/Maths/math.vector.ts` -> **Severity: 11.84** (Embedded: 0.186 * Error Risk: 63.6474%)
- `packages/dev/core/src/Misc/decorators.ts` -> **Severity: 11.361** (Embedded: 0.142 * Error Risk: 80.0%)
- `packages/dev/core/src/Misc/decorators.serialization.ts` -> **Severity: 10.924** (Embedded: 0.1401 * Error Risk: 77.9984%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/dev/inspector/src/components/globalState.ts` -> **Severity: 365.4** (Blast Radius: 3.654 * Doc Risk: 100.0%)
- `packages/tools/tests/test/audioV2/utils/audioV2.utils.ts` -> **Severity: 240.16** (Blast Radius: 2.625 * Doc Risk: 91.4894%)
- `packages/dev/serializers/src/3MF/core/xml/xml.serializer.format.ts` -> **Severity: 227.622** (Blast Radius: 20.486 * Doc Risk: 11.1111%)
- `packages/tools/babylonServer/public/audiov2-test.js` -> **Severity: 214.725** (Blast Radius: 2.454 * Doc Risk: 87.5%)
- `packages/dev/serializers/src/3MF/core/xml/xml.interfaces.ts` -> **Severity: 209.259** (Blast Radius: 22.321 * Doc Risk: 9.375%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 1766 literal sites + 51 sites through wrappers = 1817

- `throwBindingError` (function, panics_and_aborts, primitive): 27 call sites in 1 files -- `packages/tools/babylonServer/public/basis_encoder.js`
- `Node` (function, panics_and_aborts, primitive): 16 call sites in 2 files -- `packages/tools/babylonServer/public/ammo.wasm.js`
- `throwInternalError` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `packages/tools/babylonServer/public/basis_encoder.js`
- `reject` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/tools/babylonServer/public/uiControls/babylon.uiControls.max.js`
- `dc` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/tools/babylonServer/public/gltf_validator.js`
- `pw` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/tools/babylonServer/public/gltf_validator.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 73937 call pairs -- scoped 36.9%, unique 0.0%, ambiguous 36.8%, external 26.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 61597 | 42.0% | 0.0% | 38.6% | 19.4% |
| javascript | 12249 | 11.5% | 0.0% | 27.9% | 60.6% |
| html | 91 | 2.2% | 0.0% | 0.0% | 97.8% |

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
