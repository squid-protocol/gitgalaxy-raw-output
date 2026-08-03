# ARCHITECTURAL_BRIEF: three.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/three.js` |
| **Timestamp** | `2026-08-03T20:07:21.679815+00:00` |
| **Scan Duration** | `13.26s` |
| **Git Branch** | `dev` |
| **Git Commit** | `f04b082d40e8104ea3003c13fdf9dd6db8f88971` |
| **Git Remote** | `https://github.com/mrdoob/three.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1521 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 5861 |
| Analyzed Artifacts (Scanned) | 2712 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3149 |
| Total LOC | 398136 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 46.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.72 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0714 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8571 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 1504 | 189865 | 55.5% |
| HTML | 1008 | 203188 | 37.2% |
| XML | 75 | 19 | 2.8% |
| PLAINTEXT | 36 | 6 | 1.3% |
| JSON | 27 | 2207 | 1.0% |
| MARKDOWN | 25 | 0 | 0.9% |
| CSS | 20 | 2834 | 0.7% |
| BINARY_THREAT | 17 | 17 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.862`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1805 | 66.6% |
| file_cluster_13 | 573 | 21.1% |
| file_cluster_0 | 123 | 4.5% |
| file_cluster_4 | 32 | 1.2% |
| file_cluster_9 | 27 | 1.0% |
| Unknown | 23 | 0.8% |
| file_cluster_17 | 14 | 0.5% |
| file_cluster_7 | 13 | 0.5% |
| file_cluster_11 | 12 | 0.4% |
| file_cluster_12 | 2 | 0.1% |
| file_cluster_15 | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 55 | 2.0% |
| Static: Minified & Vendor Opaque Mass | 31 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3149*

**Composition by Extension & Reason:**
- `.jpg`: 821x Excluded (Explicitly Denied Extension: '.jpg'), 7x Excluded (Explicitly Denied Extension: '.JPG')
- `.html`: 788x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 30 exceeds 500 chars), 3x Excluded (Saturation: Line 44 exceeds 500 chars)
- `.md`: 778x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 204x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.js`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Excluded (Saturation: Line 1 exceeds 500 chars), 3x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.glb`: 42x Excluded (Unsupported Extension: '.glb'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mtlx`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Unsupported Extension: '.mtlx')
- `.ktx2`: 19x Excluded (Unsupported Extension: '.ktx2')
- `.pdb`: 18x Excluded (Unsupported Extension: '.pdb')
- `.hdr`: 18x Excluded (Unsupported Extension: '.hdr')
- `.gltf`: 16x Excluded (Explicitly Denied Extension: '.gltf')
- `.mpd`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wrl`: 15x Excluded (Unsupported Extension: '.wrl')
- `.tmpl`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md2`: 14x Excluded (Unsupported Extension: '.md2')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.5 | 8.4 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 17.5 | 8.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.9 | 4.4 | 4.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.8 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `editor/js/libs/tern-threejs/threejs.js` (Hits: 201)
- `manual/ko/fundamentals.html` (Hits: 191)
- `manual/en/game.html` (Hits: 165)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **infer.js** (`editor/js/libs/ternjs/infer.js`) — 3 inbound connections
2. **signal.js** (`editor/js/libs/ternjs/signal.js`) — 2 inbound connections
3. **threejs-responsive.js** (`manual/examples/threejs-responsive.js`) — 2 inbound connections
4. **ogc-parser.js** (`manual/resources/tools/geo-picking/ogc-parser.js`) — 2 inbound connections
5. **manifest.json** (`editor/manifest.json`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Addons.js** (`examples/jsm/Addons.js`) — 257 outbound dependencies
2. **Three.Core.js** (`src/Three.Core.js`) — 161 outbound dependencies
3. **Nodes.js** (`src/nodes/Nodes.js`) — 139 outbound dependencies
4. **TSL.js** (`src/nodes/TSL.js`) — 136 outbound dependencies
5. **ShaderChunk.js** (`src/renderers/shaders/ShaderChunk.js`) — 124 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addChangeToHistory` (@ `editor/js/libs/codemirror/codemirror.js`) -> Impact: **7563.0** | LOC: 1310
  * *Intent:* // Computes display.scroller.scrollLeft + display.gutters.offsetWidth, // but using getBoundingClientRect to get a sub-pixel-accurate // result.
- `dispatchKey` (@ `editor/js/libs/codemirror/codemirror.js`) -> Impact: **4477.5** | LOC: 644
- `mod` (@ `editor/js/libs/codemirror/mode/javascript.js`) -> Impact: **3150.8** | LOC: 947
- `setupWorker` (@ `examples/jsm/libs/lottie_canvas.module.js`) -> Impact: **2147.9** | LOC: 1613
- `stretchSpansOverChange` (@ `editor/js/libs/codemirror/codemirror.js`) -> Impact: **2009.3** | LOC: 782
- `mod` (@ `editor/js/libs/ternjs/doc_comment.js`) -> Impact: **1614.2** | LOC: 391
- `parse` (@ `examples/jsm/loaders/EXRLoader.js`) -> Impact: **1610.7** | LOC: 2213
  * *Intent:* /** * Constructs a new EXR loader. * * @param {LoadingManager} [manager] - The loading manager.
- `_getVariantPaths` (@ `examples/jsm/loaders/usd/USDComposer.js`) -> Impact: **1586.1** | LOC: 1882
- `parse` (@ `examples/jsm/loaders/VRMLLoader.js`) -> Impact: **1556.2** | LOC: 2598
- `tinf_inflate_uncompressed_block` (@ `examples/jsm/libs/opentype.module.js`) -> Impact: **1261.2** | LOC: 1582

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `main` (@ `manual/examples/game-conga-line-w-notes.html`) -> **O(2^N) [Recursive]**
- `pick` (@ `editor/js/libs/codemirror/addon/show-hint.js`) -> **O(2^N) [Recursive]**
- `addChangeToHistory` (@ `editor/js/libs/codemirror/codemirror.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // Computes display.scroller.scrollLeft + display.gutters.offsetWidth, // but using getBoundingClientRect to get a sub-pixel-accurate // result.
- `dispatchKey` (@ `editor/js/libs/codemirror/codemirror.js`) -> **O(2^N) [Recursive]**
- `parseAssignmentExpression` (@ `editor/js/libs/esprima.js`) -> **O(2^N) [Recursive]**
- `reinterpretExpressionAsPattern` (@ `editor/js/libs/esprima.js`) -> **O(2^N) [Recursive]**
- `checkPatternParam` (@ `editor/js/libs/esprima.js`) -> **O(2^N) [Recursive]**
- `addType` (@ `editor/js/libs/ternjs/def.js`) -> **O(2^N) [Recursive]**
- `_setupProperties` (@ `examples/jsm/libs/tween.module.js`) -> **O(2^N) [Recursive]**
- `constructor` (@ `examples/jsm/libs/ecsy.module.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Remove an event listener * @param {String} eventName Name of the event to remove * @param {Function} listener Callback for the specified event

### Highest Data Gravity (Database Complexity)
- `setupWorker` (@ `examples/jsm/libs/lottie_canvas.module.js`) -> DB Complexity: **678**
- `addChangeToHistory` (@ `editor/js/libs/codemirror/codemirror.js`) -> DB Complexity: **434**
  * *Intent:* // Computes display.scroller.scrollLeft + display.gutters.offsetWidth, // but using getBoundingClientRect to get a sub-pixel-accurate // result.
- `tinf_inflate_uncompressed_block` (@ `examples/jsm/libs/opentype.module.js`) -> DB Complexity: **391**
- `constructor` (@ `src/materials/Material.js`) -> DB Complexity: **340**
  * *Intent:* /** * Abstract base class for materials. * * Materials define the appearance of renderable 3D objects.
- `constructor` (@ `examples/jsm/controls/ArcballControls.js`) -> DB Complexity: **308**
  * *Intent:* /** * Fires when an interaction has finished. * * @event ArcballControls#end * @type {Object} */
- `parse` (@ `examples/jsm/loaders/SVGLoader.js`) -> DB Complexity: **290**
- `setXRRenderTargetTextures` (@ `src/renderers/webgl-fallback/WebGLBackend.js`) -> DB Complexity: **254**
  * *Intent:* /** * The target framebuffer when rendering with * the WebXR device API. * * @private * @type {?WebGLFramebuffer} * @default null */
- `_getVariantPaths` (@ `examples/jsm/loaders/usd/USDComposer.js`) -> DB Complexity: **219**
- `constructor` (@ `src/renderers/common/XRManager.js`) -> DB Complexity: **217**
  * *Intent:* /** * The XR manager is built on top of the WebXR Device API to * manage XR sessions with `WebGPURenderer`. *
- `compileAsync` (@ `src/renderers/common/Renderer.js`) -> DB Complexity: **179**
  * *Intent:* /** * When `autoClear` is set to `true`, this property defines whether the renderer * should clear the color buffer. * * @type {boolean} * @default tr...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `manual/examples/resources/data/gpw` | 7 | 30001.0 | 0.0% | 0.0% |
| `examples` | 570 | 26385.46 | 10.76% | 0.0% |
| `examples/jsm/loaders` | 48 | 24230.66 | 36.73% | 0.0% |
| `editor/js/libs/codemirror` | 2 | 20280.97 | 52.03% | 18.31% |
| `examples/jsm/libs` | 11 | 19180.62 | 64.67% | 0.0% |
| `editor/js/libs` | 4 | 18467.28 | 81.91% | 56.01% |
| `manual/examples` | 176 | 10054.92 | 14.24% | 0.0% |
| `editor/js/libs/ternjs` | 6 | 9092.9 | 90.33% | 30.02% |
| `examples/jsm/controls` | 9 | 7217.32 | 39.87% | 0.0% |
| `src/renderers/common` | 57 | 5971.3 | 26.18% | 12.5% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `editor/js/libs/ternjs/infer.js` -> **100.0%** Exposure
- `editor/js/libs/ui.js` -> **100.0%** Exposure
- `manual/resources/threejs-cameras.js` -> **100.0%** Exposure
- `src/materials/nodes/PointsNodeMaterial.js` -> **100.0%** Exposure
- `src/nodes/accessors/ReferenceBaseNode.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `editor/js/Command.js` -> **100.0%** Exposure
- `editor/js/Editor.js` -> **100.0%** Exposure
- `editor/js/GLTFImportDialog.js` -> **100.0%** Exposure
- `editor/js/History.js` -> **100.0%** Exposure
- `editor/js/Selector.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `editor/js/libs/ternjs/infer.js` -> **0** Orphaned Functions | **121** Duplicates
- `examples/jsm/loaders/GLTFLoader.js` -> **0** Orphaned Functions | **55** Duplicates
- `manual/resources/threejs-primitives.js` -> **0** Orphaned Functions | **49** Duplicates
- `editor/js/libs/ui.js` -> **0** Orphaned Functions | **48** Duplicates
- `examples/jsm/libs/lottie_canvas.module.js` -> **0** Orphaned Functions | **48** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`editor/js/Sidebar.Object.js`** -> AI Confidence: **99.48%**
2. **`examples/jsm/postprocessing/GTAOPass.js`** -> AI Confidence: **99.48%**
3. **`src/loaders/MaterialLoader.js`** -> AI Confidence: **99.48%**
4. **`src/renderers/webgl/WebGLPrograms.js`** -> AI Confidence: **99.48%**
5. **`src/renderers/webgpu/utils/WebGPUTextureUtils.js`** -> AI Confidence: **99.48%**
6. **`src/renderers/WebGLRenderer.js`** -> AI Confidence: **99.39%**
7. **`src/renderers/webgl-fallback/WebGLBackend.js`** -> AI Confidence: **99.39%**
8. **`src/renderers/webgl/WebGLProgram.js`** -> AI Confidence: **99.39%**
9. **`src/renderers/webgl/WebGLShadowMap.js`** -> AI Confidence: **99.39%**
10. **`src/renderers/webgpu/WebGPUBackend.js`** -> AI Confidence: **99.39%**
11. **`src/textures/Texture.js`** -> AI Confidence: **99.39%**
12. **`src/materials/Material.js`** -> AI Confidence: **99.34%**
13. **`examples/jsm/misc/Volume.js`** -> AI Confidence: **99.32%**
14. **`src/renderers/webgl-fallback/utils/WebGLState.js`** -> AI Confidence: **99.32%**
15. **`editor/js/Editor.js`** -> AI Confidence: **99.31%**
16. **`editor/js/Loader.js`** -> AI Confidence: **99.31%**
17. **`editor/js/Sidebar.Material.MapProperty.js`** -> AI Confidence: **99.31%**
18. **`editor/js/Sidebar.Material.js`** -> AI Confidence: **99.31%**
19. **`editor/js/libs/ui.three.js`** -> AI Confidence: **99.31%**
20. **`examples/jsm/tsl/lighting/DynamicLightsNode.js`** -> AI Confidence: **99.31%**
21. **`src/animation/AnimationClip.js`** -> AI Confidence: **99.31%**
22. **`src/animation/AnimationMixer.js`** -> AI Confidence: **99.31%**
23. **`src/animation/KeyframeTrack.js`** -> AI Confidence: **99.31%**
24. **`src/core/BufferGeometry.js`** -> AI Confidence: **99.31%**
25. **`src/extras/PMREMGenerator.js`** -> AI Confidence: **99.31%**
26. **`src/geometries/ExtrudeGeometry.js`** -> AI Confidence: **99.31%**
27. **`src/loaders/BufferGeometryLoader.js`** -> AI Confidence: **99.31%**
28. **`src/loaders/ObjectLoader.js`** -> AI Confidence: **99.31%**
29. **`src/materials/nodes/MeshPhysicalNodeMaterial.js`** -> AI Confidence: **99.31%**
30. **`src/materials/nodes/NodeMaterials.js`** -> AI Confidence: **99.31%**
31. **`src/nodes/Nodes.js`** -> AI Confidence: **99.31%**
32. **`src/nodes/accessors/Camera.js`** -> AI Confidence: **99.31%**
33. **`src/nodes/accessors/InstanceNode.js`** -> AI Confidence: **99.31%**
34. **`src/nodes/accessors/MaterialNode.js`** -> AI Confidence: **99.31%**
35. **`src/nodes/accessors/MorphNode.js`** -> AI Confidence: **99.31%**
36. **`src/nodes/accessors/TextureNode.js`** -> AI Confidence: **99.31%**
37. **`src/nodes/core/NodeBuilder.js`** -> AI Confidence: **99.31%**
38. **`src/nodes/core/NodeUtils.js`** -> AI Confidence: **99.31%**
39. **`src/nodes/functions/BasicLightingModel.js`** -> AI Confidence: **99.31%**
40. **`src/nodes/geometry/RangeNode.js`** -> AI Confidence: **99.31%**
41. **`src/nodes/lighting/AnalyticLightNode.js`** -> AI Confidence: **99.31%**
42. **`src/nodes/pmrem/PMREMNode.js`** -> AI Confidence: **99.31%**
43. **`src/nodes/utils/CubeMapNode.js`** -> AI Confidence: **99.31%**
44. **`src/objects/BatchedMesh.js`** -> AI Confidence: **99.31%**
45. **`src/objects/Line.js`** -> AI Confidence: **99.31%**
46. **`src/objects/Mesh.js`** -> AI Confidence: **99.31%**
47. **`src/objects/SkinnedMesh.js`** -> AI Confidence: **99.31%**
48. **`src/renderers/common/Renderer.js`** -> AI Confidence: **99.31%**
49. **`src/renderers/common/XRManager.js`** -> AI Confidence: **99.31%**
50. **`src/renderers/common/extras/PMREMGenerator.js`** -> AI Confidence: **99.31%**
51. **`src/renderers/common/nodes/NodeManager.js`** -> AI Confidence: **99.31%**
52. **`src/renderers/webgl-fallback/nodes/GLSLNodeBuilder.js`** -> AI Confidence: **99.31%**
53. **`src/renderers/webgl/WebGLBackground.js`** -> AI Confidence: **99.31%**
54. **`src/renderers/webgpu/nodes/WGSLNodeBuilder.js`** -> AI Confidence: **99.31%**
55. **`src/renderers/webxr/WebXRManager.js`** -> AI Confidence: **99.31%**
56. **`test/unit/src/core/BufferGeometry.tests.js`** -> AI Confidence: **99.31%**
57. **`editor/js/libs/codemirror/addon/dialog.js`** -> AI Confidence: **99.29%**
58. **`editor/js/libs/tern-threejs/threejs.js`** -> AI Confidence: **99.29%**
59. **`examples/jsm/controls/FirstPersonControls.js`** -> AI Confidence: **99.29%**
60. **`examples/jsm/controls/FlyControls.js`** -> AI Confidence: **99.29%**
61. **`examples/jsm/controls/OrbitControls.js`** -> AI Confidence: **99.29%**
62. **`examples/jsm/controls/TrackballControls.js`** -> AI Confidence: **99.29%**
63. **`examples/jsm/controls/TransformControls.js`** -> AI Confidence: **99.29%**
64. **`examples/jsm/csm/CSMShader.js`** -> AI Confidence: **99.29%**
65. **`examples/jsm/effects/AsciiEffect.js`** -> AI Confidence: **99.29%**
66. **`examples/jsm/interactive/SelectionBox.js`** -> AI Confidence: **99.29%**
67. **`examples/jsm/loaders/lwo/IFFParser.js`** -> AI Confidence: **99.29%**
68. **`examples/jsm/loaders/lwo/LWO2Parser.js`** -> AI Confidence: **99.29%**
69. **`examples/jsm/loaders/lwo/LWO3Parser.js`** -> AI Confidence: **99.29%**
70. **`examples/jsm/loaders/usd/USDAParser.js`** -> AI Confidence: **99.29%**
71. **`examples/jsm/shaders/DigitalGlitch.js`** -> AI Confidence: **99.29%**
72. **`examples/jsm/shaders/FocusShader.js`** -> AI Confidence: **99.29%**
73. **`examples/jsm/shaders/MirrorShader.js`** -> AI Confidence: **99.29%**
74. **`examples/jsm/shaders/SMAAShader.js`** -> AI Confidence: **99.29%**
75. **`examples/jsm/shaders/ToonShader.js`** -> AI Confidence: **99.29%**
76. **`examples/jsm/transpiler/Linker.js`** -> AI Confidence: **99.29%**
77. **`src/nodes/core/NodeFrame.js`** -> AI Confidence: **99.29%**
78. **`src/renderers/shaders/ShaderChunk/alphatest_fragment.glsl.js`** -> AI Confidence: **99.29%**
79. **`src/renderers/shaders/ShaderChunk/aomap_fragment.glsl.js`** -> AI Confidence: **99.29%**
80. **`src/renderers/shaders/ShaderChunk/clipping_planes_fragment.glsl.js`** -> AI Confidence: **99.29%**
81. **`src/renderers/shaders/ShaderChunk/color_pars_vertex.glsl.js`** -> AI Confidence: **99.29%**
82. **`src/renderers/shaders/ShaderChunk/color_vertex.glsl.js`** -> AI Confidence: **99.29%**
83. **`src/renderers/shaders/ShaderChunk/cube_uv_reflection_fragment.glsl.js`** -> AI Confidence: **99.29%**
84. **`src/renderers/shaders/ShaderChunk/envmap_fragment.glsl.js`** -> AI Confidence: **99.29%**
85. **`src/renderers/shaders/ShaderChunk/envmap_pars_fragment.glsl.js`** -> AI Confidence: **99.29%**
86. **`src/renderers/shaders/ShaderChunk/envmap_pars_vertex.glsl.js`** -> AI Confidence: **99.29%**
87. **`src/renderers/shaders/ShaderChunk/envmap_vertex.glsl.js`** -> AI Confidence: **99.29%**
88. **`src/renderers/shaders/ShaderChunk/lights_fragment_begin.glsl.js`** -> AI Confidence: **99.29%**
89. **`src/renderers/shaders/ShaderChunk/lights_fragment_end.glsl.js`** -> AI Confidence: **99.29%**
90. **`src/renderers/shaders/ShaderChunk/lights_fragment_maps.glsl.js`** -> AI Confidence: **99.29%**
91. **`src/renderers/shaders/ShaderChunk/lights_physical_fragment.glsl.js`** -> AI Confidence: **99.29%**
92. **`src/renderers/shaders/ShaderChunk/map_particle_fragment.glsl.js`** -> AI Confidence: **99.29%**
93. **`src/renderers/shaders/ShaderChunk/map_particle_pars_fragment.glsl.js`** -> AI Confidence: **99.29%**
94. **`src/renderers/shaders/ShaderChunk/morphcolor_vertex.glsl.js`** -> AI Confidence: **99.29%**
95. **`src/renderers/shaders/ShaderChunk/normal_fragment_begin.glsl.js`** -> AI Confidence: **99.29%**
96. **`src/renderers/shaders/ShaderChunk/shadowmap_pars_fragment.glsl.js`** -> AI Confidence: **99.29%**
97. **`src/renderers/shaders/ShaderChunk/shadowmap_pars_vertex.glsl.js`** -> AI Confidence: **99.29%**
98. **`src/renderers/shaders/ShaderChunk/shadowmap_vertex.glsl.js`** -> AI Confidence: **99.29%**
99. **`src/renderers/shaders/ShaderChunk/shadowmask_pars_fragment.glsl.js`** -> AI Confidence: **99.29%**
100. **`src/renderers/shaders/ShaderChunk/worldpos_vertex.glsl.js`** -> AI Confidence: **99.29%**
101. **`src/renderers/shaders/ShaderLib/meshnormal.glsl.js`** -> AI Confidence: **99.29%**
102. **`src/renderers/webgl-fallback/utils/WebGLTextureUtils.js`** -> AI Confidence: **99.29%**
103. **`src/renderers/webgl/WebGLInfo.js`** -> AI Confidence: **99.29%**
104. **`src/renderers/webgl/WebGLMaterials.js`** -> AI Confidence: **99.29%**
105. **`src/renderers/webgpu/utils/WebGPUPipelineUtils.js`** -> AI Confidence: **99.29%**
106. **`test/unit/src/core/RenderTarget.tests.js`** -> AI Confidence: **99.29%**
107. **`test/unit/utils/console-wrapper.js`** -> AI Confidence: **99.29%**
108. **`editor/js/Viewport.js`** -> AI Confidence: **99.24%**
109. **`src/Three.WebGPU.Nodes.js`** -> AI Confidence: **99.24%**
110. **`src/Three.WebGPU.js`** -> AI Confidence: **99.24%**
111. **`src/nodes/display/ScreenNode.js`** -> AI Confidence: **99.24%**
112. **`src/nodes/display/ViewportTextureNode.js`** -> AI Confidence: **99.24%**
113. **`src/nodes/tsl/TSLCore.js`** -> AI Confidence: **99.24%**
114. **`src/objects/Sprite.js`** -> AI Confidence: **99.24%**
115. **`test/unit/src/core/Object3D.tests.js`** -> AI Confidence: **99.24%**
116. **`examples/jsm/postprocessing/SSRPass.js`** -> AI Confidence: **99.23%**
117. **`src/nodes/display/NormalMapNode.js`** -> AI Confidence: **99.23%**
118. **`src/nodes/gpgpu/ComputeNode.js`** -> AI Confidence: **99.23%**
119. **`src/objects/InstancedMesh.js`** -> AI Confidence: **99.23%**
120. **`src/objects/Points.js`** -> AI Confidence: **99.23%**
121. **`src/renderers/common/Background.js`** -> AI Confidence: **99.23%**
122. **`utils/llms/build.js`** -> AI Confidence: **99.23%**
123. **`examples/jsm/postprocessing/SAOPass.js`** -> AI Confidence: **99.22%**
124. **`examples/jsm/postprocessing/SSAOPass.js`** -> AI Confidence: **99.22%**
125. **`editor/js/Sidebar.Geometry.ExtrudeGeometry.js`** -> AI Confidence: **99.2%**
126. **`examples/jsm/inspector/ui/Profiler.js`** -> AI Confidence: **99.2%**
127. **`examples/jsm/loaders/VRMLLoader.js`** -> AI Confidence: **99.2%**
128. **`examples/jsm/misc/ProgressiveLightMap.js`** -> AI Confidence: **99.2%**
129. **`examples/jsm/transpiler/WGSLEncoder.js`** -> AI Confidence: **99.2%**
130. **`src/cameras/CubeCamera.js`** -> AI Confidence: **99.2%**
131. **`src/helpers/ArrowHelper.js`** -> AI Confidence: **99.18%**
132. **`src/materials/nodes/Line2NodeMaterial.js`** -> AI Confidence: **99.18%**
133. **`src/materials/nodes/MeshStandardNodeMaterial.js`** -> AI Confidence: **99.18%**
134. **`src/nodes/accessors/BatchNode.js`** -> AI Confidence: **99.18%**
135. **`src/nodes/accessors/ClippingNode.js`** -> AI Confidence: **99.18%**
136. **`src/nodes/accessors/SkinningNode.js`** -> AI Confidence: **99.18%**
137. **`src/nodes/display/PassNode.js`** -> AI Confidence: **99.18%**
138. **`src/nodes/functions/BSDF/BRDF_GGX.js`** -> AI Confidence: **99.18%**
139. **`src/nodes/functions/VolumetricLightingModel.js`** -> AI Confidence: **99.18%**
140. **`src/nodes/lighting/EnvironmentNode.js`** -> AI Confidence: **99.18%**
141. **`src/nodes/lighting/SpotLightNode.js`** -> AI Confidence: **99.18%**
142. **`src/nodes/utils/RTTNode.js`** -> AI Confidence: **99.18%**
143. **`src/renderers/webgl/WebGLOutput.js`** -> AI Confidence: **99.18%**
144. **`test/unit/src/core/Raycaster.tests.js`** -> AI Confidence: **99.18%**
145. **`test/unit/src/math/Matrix4.tests.js`** -> AI Confidence: **99.18%**
146. **`editor/js/Animation.js`** -> AI Confidence: **99.17%**
147. **`editor/js/History.js`** -> AI Confidence: **99.17%**
148. **`editor/js/Menubar.View.js`** -> AI Confidence: **99.17%**
149. **`editor/js/Viewport.Info.js`** -> AI Confidence: **99.17%**
150. **`editor/js/libs/ternjs/comment.js`** -> AI Confidence: **99.17%**
151. **`examples/jsm/controls/DragControls.js`** -> AI Confidence: **99.17%**
152. **`examples/jsm/effects/OutlineEffect.js`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `test/unit/src/math/Matrix3.tests.js` -> **100.0%** Exposure
- `test/unit/src/math/Matrix4.tests.js` -> **100.0%** Exposure
- `test/unit/src/constants.tests.js` -> **0.0002%** Exposure
- `test/unit/src/math/Vector3.tests.js` -> **0.0001%** Exposure
- `test/unit/src/math/Vector4.tests.js` -> **0.0001%** Exposure
### Exploit Generation Surface
- `manual/examples/game-conga-line-w-notes.html` -> **100.0%** Exposure
- `manual/examples/game-conga-line.html` -> **100.0%** Exposure
- `manual/examples/game-player-input.html` -> **100.0%** Exposure
- `editor/js/libs/codemirror/addon/show-hint.js` -> **100.0%** Exposure
- `editor/js/libs/codemirror/addon/tern.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `examples/webgl_buffergeometry_selective_draw.html` -> **100.0%** Exposure
- `examples/webgl_geometry_extrude_shapes.html` -> **100.0%** Exposure
- `examples/webgl_interactive_lines.html` -> **100.0%** Exposure
- `examples/webgl_modifier_edgesplit.html` -> **100.0%** Exposure
- `examples/webgl_modifier_simplifier.html` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `examples/webgl_geometry_text_shapes.html` -> **100.0%** Exposure
- `examples/webgl_loader_3dtiles.html` -> **100.0%** Exposure
- `examples/webgl_loader_svg.html` -> **100.0%** Exposure
- `examples/webgl_postprocessing_dof.html` -> **100.0%** Exposure
- `manual/examples/cleanup-loaded-files.html` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `90` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1522` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `editor/js/libs/ternjs/infer.js` (JAVASCRIPT) -> Cumulative Risk: **853.74**
- **Archetype:** `file_cluster_11` (Distance: 14.592 IQR)
- **Magnitude:** 3827.74 | **LOC:** 1636 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `similarType` (Impact: 163.5), `maybeInstantiate` (Impact: 135.7), `canonicalType` (Impact: 76.9)

### 2. `editor/js/libs/ternjs/def.js` (JAVASCRIPT) -> Cumulative Risk: **844.49**
- **Archetype:** `file_cluster_11` (Distance: 14.16 IQR)
- **Magnitude:** 1585.64 | **LOC:** 589 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Safety Score (98.6697%)
- **Heaviest Functions:** `passTwo` (Impact: 145.8), `parsePath` (Impact: 120.2), `passOne` (Impact: 103.2)

### 3. `editor/js/libs/codemirror/addon/show-hint.js` (JAVASCRIPT) -> Cumulative Risk: **815.16**
- **Archetype:** `file_cluster_4` (Distance: 14.41 IQR)
- **Magnitude:** 1518.42 | **LOC:** 530 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Widget` (Impact: 582.8), `pick` (Impact: 73.5), `buildKeyMap` (Impact: 35.9)

### 4. `editor/js/libs/codemirror/codemirror.js` (JAVASCRIPT) -> Cumulative Risk: **812.89**
- **Archetype:** `file_cluster_11` (Distance: 14.445 IQR)
- **Magnitude:** 20280.36 | **LOC:** 9850 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `addChangeToHistory` (Impact: 7563.0), `dispatchKey` (Impact: 4477.5), `stretchSpansOverChange` (Impact: 2009.3)

### 5. `editor/js/libs/esprima.js` (JAVASCRIPT) -> Cumulative Risk: **808.21**
- **Archetype:** `file_cluster_11` (Distance: 15.78 IQR)
- **Magnitude:** 16897.8 | **LOC:** 6401 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `parseStatement` (Impact: 373.9), `scanPunctuator` (Impact: 349.6), `parseForStatement` (Impact: 310.4)

### 6. `editor/js/libs/codemirror/mode/javascript.js` (JAVASCRIPT) -> Cumulative Risk: **807.76**
- **Archetype:** `file_cluster_8` (Distance: 12.07 IQR)
- **Magnitude:** 3439.64 | **LOC:** 960 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9815%)
- **Heaviest Functions:** `mod` (Impact: 3150.8)

### 7. `editor/js/libs/ternjs/tern.js` (JAVASCRIPT) -> Cumulative Risk: **802.95**
- **Archetype:** `file_cluster_11` (Distance: 13.843 IQR)
- **Magnitude:** 1601.88 | **LOC:** 994 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `findCompletions` (Impact: 350.1), `findRefsToVariable` (Impact: 139.3), `invalidDoc` (Impact: 84.2)

### 8. `editor/js/libs/codemirror/addon/tern.js` (JAVASCRIPT) -> Cumulative Risk: **784.72**
- **Archetype:** `file_cluster_4` (Distance: 13.532 IQR)
- **Magnitude:** 1681.62 | **LOC:** 751 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `mod` (Impact: 1158.5)

### 9. `src/renderers/common/Renderer.js` (JAVASCRIPT) -> Cumulative Risk: **706.54**
- **Archetype:** `file_cluster_13` (Distance: 15.612 IQR)
- **Magnitude:** 1478.2 | **LOC:** 3681 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 44.1%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Churn (100.0%)
- **Heaviest Functions:** `compileAsync` (Impact: 910.5)

### 10. `utils/packLDrawModel.mjs` (JAVASCRIPT) -> Cumulative Risk: **688.56**
- **Archetype:** `file_cluster_8` (Distance: 12.466 IQR)
- **Magnitude:** 227.28 | **LOC:** 307 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (97.3786%)
- **Heaviest Functions:** `parseObject` (Impact: 166.6), `parseObject` (Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `editor/js/libs/codemirror/codemirror.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.445 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.09 IQR)
- **Top Global Matches:** file_cluster_11: 14.445, file_cluster_8: 14.461, file_cluster_15: 14.644
- **Magnitude:** 20280.36 | **LOC:** 9850 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 434
- **Risk Profile:** Cognitive Load (98.9082%), Tech Debt (18.2132%)
**Top Internal Functions/Classes:**
  * `addChangeToHistory` (Impact: 7563.0 | O(2^N) | DB: 434)
    * *Intent:* // Computes display.scroller.scrollLeft + display.gutters.offsetWidth, // but using getBoundingClien...
  * `dispatchKey` (Impact: 4477.5 | O(2^N) | DB: 114)
  * `stretchSpansOverChange` (Impact: 2009.3 | O(N^6) | DB: 143)
  * `drawSelectionRange` (Impact: 228.6 | O(N^3) | DB: 27)
    * *Intent:* // Render the DOM representation of the text of a line. Also builds // up a 'line map', which points...
  * `updateHeightsInViewport` (Impact: 177.1 | O(2^N) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1940`, `structural_boundaries: 1215`, `args: 459`, `func_start: 585`
* *Risk/State:* `safety_bypasses: 423`, `state_mutation: 3289`, `dead_code: 3`, `fragile_debt: 6`, `duplicate_logic: 7`
* *Architecture:* `api: 25`, `concurrency: 48`
* *Defense:* `safety: 52`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/esprima.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.78 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.813 IQR)
- **Top Global Matches:** file_cluster_11: 15.78, file_cluster_8: 15.948, file_cluster_17: 16.061
- **Magnitude:** 16897.8 | **LOC:** 6401 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 116
- **Risk Profile:** Cognitive Load (79.8346%), Tech Debt (10.8685%)
**Top Internal Functions/Classes:**
  * `parseStatement` (Impact: 373.9 | O(N^6) | DB: 29)
  * `scanPunctuator` (Impact: 349.6 | O(N^6) | DB: 32)
  * `parseForStatement` (Impact: 310.4 | O(N^6) | DB: 116)
  * `scanTemplate` (Impact: 297.1 | O(N^6) | DB: 53)
  * `parsePrimaryExpression` (Impact: 283.7 | O(N^6) | DB: 70)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1486`, `structural_boundaries: 964`, `args: 247`, `func_start: 214`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 7`, `state_mutation: 7620`, `dead_code: 9`, `duplicate_logic: 8`
* *Architecture:* `api: 50`, `concurrency: 12`
* *Defense:* `safety: 456`, `doc: 59`, `test: 93`, `immutability_locks: 8`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/libs/lottie_canvas.module.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.43 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.316 IQR)
- **Top Global Matches:** file_cluster_11: 15.43, file_cluster_8: 15.56, file_cluster_17: 15.678
- **Magnitude:** 12295.98 | **LOC:** 14850 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 678
- **Risk Profile:** Cognitive Load (95.4114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setupWorker` (Impact: 2147.9 | O(N^6) | DB: 678)
  * `searchShapes` (Impact: 261.2 | O(2^N) | DB: 28)
  * `seedRandom` (Impact: 144.5 | O(N^4) | DB: 13)
  * `addFonts` (Impact: 123.0 | O(N^3) | DB: 50)
  * `extendPrototype` (Impact: 120.1 | O(2^N) | DB: 90)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1411`, `structural_boundaries: 1238`, `args: 448`, `func_start: 485`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 6381`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 48`
* *Architecture:* `io: 59`, `api: 47`, `concurrency: 44`
* *Defense:* `safety: 431`, `doc: 13`, `sync_locks: 7`, `immutability_locks: 43`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` howler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014bt_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014bt_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014ft_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014ft_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014mt_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014mt_2010_dens_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/ternjs/infer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.592 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.373 IQR)
- **Top Global Matches:** file_cluster_11: 14.592, file_cluster_15: 14.802, file_cluster_8: 14.83
- **Magnitude:** 3827.74 | **LOC:** 1636 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (92.3441%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `similarType` (Impact: 163.5 | O(2^N) | DB: 5)
  * `maybeInstantiate` (Impact: 135.7 | O(2^N) | DB: 10)
  * `canonicalType` (Impact: 76.9 | O(N^2) | DB: 8)
  * `maybeTagAsGeneric` (Impact: 56.5 | O(N^2) | DB: 16)
  * `addType` (Impact: 52.8 | O(2^N) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 580`, `structural_boundaries: 505`, `args: 233`, `func_start: 247`
* *Risk/State:* `safety_bypasses: 121`, `state_mutation: 1483`, `fragile_debt: 1`, `duplicate_logic: 121`
* *Architecture:* `io: 2`, `api: 63`, `import: 5`
* *Defense:* `safety: 54`, `test: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.992
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` acorn, signal, walk, acorn_loose, def
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `editor/js/libs/codemirror/mode/javascript.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.07 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.334 IQR)
- **Top Global Matches:** file_cluster_8: 12.07, file_cluster_4: 12.323, file_cluster_11: 12.473
- **Magnitude:** 3439.64 | **LOC:** 960 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 84
- **Risk Profile:** Cognitive Load (91.4668%), Tech Debt (10.8358%)
**Top Internal Functions/Classes:**
  * `mod` (Impact: 3150.8 | O(N^6) | DB: 84)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 632`, `structural_boundaries: 387`, `args: 110`, `func_start: 112`
* *Risk/State:* `safety_bypasses: 332`, `high_risk_execution: 1`, `state_mutation: 244`, `fragile_debt: 2`
* *Architecture:* `api: 4`, `concurrency: 23`, `import: 1`
* *Defense:* `safety: 14`, `test: 34`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` codemirror
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/libs/opentype.module.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.721 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.352 IQR)
- **Top Global Matches:** file_cluster_8: 13.721, file_cluster_11: 13.802, file_cluster_13: 13.972
- **Magnitude:** 2759.56 | **LOC:** 14507 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 391
- **Risk Profile:** Cognitive Load (64.4447%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tinf_inflate_uncompressed_block` (Impact: 1261.2 | O(N^6) | DB: 391)
  * `makeGlobalSubrIndex` (Impact: 170.0 | O(N^5) | DB: 6)
  * `tinf_decode_trees` (Impact: 51.0 | O(N^2) | DB: 5)
  * `makeDict` (Impact: 25.8 | O(N^4) | DB: 4)
  * `tinf_inflate_block_data` (Impact: 19.6 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 417`, `args: 119`, `func_start: 118`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1086`, `dead_code: 3`, `fragile_debt: 3`
* *Architecture:* `io: 8`, `api: 14`, `concurrency: 2`
* *Defense:* `safety: 75`, `doc: 70`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` glyf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/EXRLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.581 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.291 IQR)
- **Top Global Matches:** file_cluster_8: 12.581, file_cluster_7: 12.954, file_cluster_13: 12.985
- **Magnitude:** 2737.98 | **LOC:** 3434 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 137
- **Risk Profile:** Cognitive Load (73.2587%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 1610.7 | O(2^N) | DB: 137)
    * *Intent:* /** * Constructs a new EXR loader. * * @param {LoadingManager} [manager] - The loading manager.
  * `setupDecoder` (Impact: 285.4 | O(N^1) | DB: 9)
  * `parseDeepScanline` (Impact: 80.9 | O(N^2) | DB: 13)
  * `parseMultiPartScanline` (Impact: 21.9 | O(N^1) | DB: 4)
  * `parseScanline` (Impact: 21.6 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 242`, `args: 80`, `func_start: 133`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 542`, `dead_code: 3`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 52`, `doc: 21`, `immutability_locks: 426`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three, fflate.module.js, EXRLoader.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/GLTFLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.325 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.38 IQR)
- **Top Global Matches:** file_cluster_4: 14.325, file_cluster_8: 14.645, file_cluster_11: 14.704
- **Magnitude:** 2470.2 | **LOC:** 4861 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 27.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (50.0524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadNode` (Impact: 158.5 | O(N^1) | DB: 30)
  * `parse` (Impact: 149.2 | O(2^N) | DB: 28)
  * `createNodeMesh` (Impact: 103.0 | O(2^N) | DB: 11)
  * `loadMaterial` (Impact: 67.7 | O(N^1) | DB: 13)
  * `load` (Impact: 44.0 | O(2^N) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 422`, `structural_boundaries: 236`, `args: 161`, `func_start: 121`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 842`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 55`
* *Architecture:* `io: 12`, `api: 15`, `concurrency: 300`, `import: 3`
* *Defense:* `safety: 186`, `doc: 108`, `immutability_locks: 322`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SkeletonUtils.js, BufferGeometryUtils.js, three, GLTFLoader.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/VRMLLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.42 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.339 IQR)
- **Top Global Matches:** file_cluster_8: 13.42, file_cluster_11: 13.472, file_cluster_0: 13.553
- **Magnitude:** 2218.42 | **LOC:** 3647 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 153
- **Risk Profile:** Cognitive Load (78.6325%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 1556.2 | O(N^2) | DB: 153)
  * `paintFaces` (Impact: 41.0 | O(N^1) | DB: 7)
    * *Intent:* // since face definitions can have more than three vertices, it's necessary to // perform a simple t...
  * `load` (Impact: 28.6 | O(2^N) | DB: 15)
    * *Intent:* /** * A loader for the VRML format. * * ```js * const loader = new VRMLLoader(); * const object = aw...
  * `computeNormalAttribute` (Impact: 15.2 | O(N^1) | DB: 9)
  * `weightedNormal` (Impact: 11.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 584`, `structural_boundaries: 176`, `args: 96`, `func_start: 74`, `class_start: 5`
* *Risk/State:* `state_mutation: 490`, `dead_code: 22`, `duplicate_logic: 4`
* *Architecture:* `io: 7`, `api: 1`, `import: 2`
* *Defense:* `safety: 66`, `doc: 18`, `immutability_locks: 322`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three, chevrotain.module.min.js, VRMLLoader.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/controls/OrbitControls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.19 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.424 IQR)
- **Top Global Matches:** file_cluster_0: 15.19, file_cluster_13: 15.293, file_cluster_8: 15.297
- **Magnitude:** 2134.08 | **LOC:** 1964 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 137
- **Risk Profile:** Cognitive Load (46.3531%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 121.9 | O(N^1) | DB: 137)
  * `_handleKeyDown` (Impact: 75.5 | O(N^1) | DB: 34)
  * `onMouseDown` (Impact: 74.1 | O(N^1) | DB: 22)
  * `onTouchStart` (Impact: 62.3 | O(N^1) | DB: 23)
  * `onTouchMove` (Impact: 40.7 | O(N^1) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 58`, `args: 66`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1371`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 52`, `doc: 98`, `immutability_locks: 59`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three, OrbitControls.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/usd/USDComposer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.075 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.691 IQR)
- **Top Global Matches:** file_cluster_8: 14.075, file_cluster_11: 14.337, file_cluster_13: 14.354
- **Magnitude:** 2120.5 | **LOC:** 4595 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 48.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 219
- **Risk Profile:** Cognitive Load (69.7777%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_getVariantPaths` (Impact: 1586.1 | O(2^N) | DB: 219)
  * `constructor` (Impact: 2.8 | O(N^1) | DB: 3)
    * *Intent:* /** * USDComposer handles scene composition from parsed USD data. * This includes reference resoluti...
  * `compose` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 377`, `structural_boundaries: 126`, `args: 48`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 506`
* *Architecture:* `io: 20`, `api: 2`, `import: 1`
* *Defense:* `safety: 130`, `doc: 16`, `immutability_locks: 265`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/SVGLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.481 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.319 IQR)
- **Top Global Matches:** file_cluster_8: 12.481, file_cluster_17: 12.777, file_cluster_7: 12.819
- **Magnitude:** 1984.12 | **LOC:** 3268 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 290
- **Risk Profile:** Cognitive Load (49.4241%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 1142.1 | O(N^2) | DB: 290)
  * `pointsToStrokeWithBuffers` (Impact: 238.2 | O(N^2) | DB: 12)
  * `createShapes` (Impact: 105.3 | O(N^1) | DB: 45)
    * *Intent:* // Calculate eigenvectors
  * `addCapGeometry` (Impact: 51.9 | O(N^1))
  * `load` (Impact: 24.0 | O(2^N) | DB: 3)
    * *Intent:* * Scalable Vector Graphics is an XML-based vector image format for two-dimensional graphics * with s...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 151`, `args: 66`, `func_start: 219`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 277`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 85`, `api: 5`, `import: 1`
* *Defense:* `safety: 117`, `doc: 42`, `immutability_locks: 221`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SVGLoader.js, three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderers/webgl-fallback/WebGLBackend.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.927 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.705 IQR)
- **Top Global Matches:** file_cluster_13: 14.927, file_cluster_0: 14.943, file_cluster_8: 14.967
- **Magnitude:** 1877.08 | **LOC:** 2779 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 42.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 254
- **Risk Profile:** Cognitive Load (48.2159%), Tech Debt (8.4644%)
**Top Internal Functions/Classes:**
  * `setXRRenderTargetTextures` (Impact: 1003.2 | O(N^2) | DB: 254)
    * *Intent:* /** * The target framebuffer when rendering with * the WebXR device API. * * @private * @type {?WebG...
  * `init` (Impact: 36.2 | O(2^N) | DB: 27)
  * `makeXRCompatible` (Impact: 7.5 | O(2^N) | DB: 2)
    * *Intent:* /** * A unique collection of bindings. * * @private * @type {WeakSet<Array<BindGroup>>}
  * `getArrayBufferAsync` (Impact: 4.7 | O(2^N) | DB: 1)
    * *Intent:* /** * A reference to the current render context. * * @private * @type {RenderContext} * @default nul...
  * `setXRTarget` (Impact: 2.2 | O(N^1) | DB: 1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 110`, `args: 68`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `state_mutation: 745`, `planned_debt: 2`
* *Architecture:* `api: 5`, `concurrency: 43`, `import: 14`
* *Defense:* `safety: 81`, `doc: 228`, `immutability_locks: 241`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WebGLUtils.js, WebGLTextureUtils.js, WebGLBufferRenderer.js, RenderContext.js, constants.js, utils.js, GLSLNodeBuilder.js, WebGLExtensions.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/ternjs/doc_comment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.773 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.18 IQR)
- **Top Global Matches:** file_cluster_8: 12.773, file_cluster_13: 12.896, file_cluster_11: 12.927
- **Magnitude:** 1793.4 | **LOC:** 402 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 91
- **Risk Profile:** Cognitive Load (87.299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mod` (Impact: 1614.2 | O(N^6) | DB: 91)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 94`, `args: 30`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 172`
* *Architecture:* `io: 11`, `import: 5`
* *Defense:* `safety: 12`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` infer, acorn, tern, walk, comment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/libs/tween.module.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.676 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.524 IQR)
- **Top Global Matches:** file_cluster_11: 13.676, file_cluster_8: 13.756, file_cluster_15: 13.875
- **Magnitude:** 1764.72 | **LOC:** 877 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (82.7662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_setupProperties` (Impact: 745.2 | O(2^N) | DB: 50)
  * `update` (Impact: 94.8 | O(2^N) | DB: 9)
  * `CatmullRom` (Impact: 79.0 | O(2^N) | DB: 4)
  * `start` (Impact: 59.1 | O(N^5) | DB: 34)
  * `Out` (Impact: 31.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 170`, `args: 72`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 360`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 37`, `orphaned_logic: 6`
* *Architecture:* `io: 4`, `api: 2`
* *Defense:* `safety: 46`, `doc: 10`, `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderers/webgpu/nodes/WGSLNodeBuilder.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.137 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.7 IQR)
- **Top Global Matches:** file_cluster_0: 15.137, file_cluster_13: 15.173, file_cluster_8: 15.312
- **Magnitude:** 1759.8 | **LOC:** 2511 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 53.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 148
- **Risk Profile:** Cognitive Load (46.8449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generateTextureDimension` (Impact: 1213.5 | O(2^N) | DB: 148)
  * `generateWrapFunction` (Impact: 33.4 | O(N^1) | DB: 5)
  * `generateTextureSampleLevel` (Impact: 25.7 | O(N^1) | DB: 4)
    * *Intent:* /** * A flag that indicates that early returns are allowed. * * @type {boolean}
  * `_generateTextureSample` (Impact: 20.2 | O(N^1) | DB: 2)
  * `constructor` (Impact: 2.9 | O(N^1) | DB: 6)
    * *Intent:* /** * A node builder targeting WGSL. * * This module generates WGSL shader code from node materials ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 163`, `args: 50`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 444`
* *Architecture:* `io: 2`, `api: 2`, `import: 14`
* *Defense:* `safety: 89`, `doc: 205`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeUniformsGroup.js, WebGPUConstants.js, VarNode.js, WebGPUTextureUtils.js, ExpressionNode.js, utils.js, NodeSampler.js, NodeSampledTexture.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/codemirror/addon/tern.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.532 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.573 IQR)
- **Top Global Matches:** file_cluster_4: 13.532, file_cluster_8: 13.62, file_cluster_11: 13.749
- **Magnitude:** 1681.62 | **LOC:** 751 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 162
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mod` (Impact: 1158.5 | O(N^6) | DB: 162)
    * *Intent:* // queries. // * responseFilter: A function(doc, query, request, error, data) that // will be applie...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 163`, `args: 83`, `func_start: 91`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 462`
* *Architecture:* `concurrency: 49`, `import: 1`
* *Defense:* `safety: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` codemirror
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/exporters/GLTFExporter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.874 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.945 IQR)
- **Top Global Matches:** file_cluster_4: 13.874, file_cluster_8: 14.068, file_cluster_11: 14.247
- **Magnitude:** 1675.24 | **LOC:** 3739 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (49.496%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createNormalizedNormalAttribute` (Impact: 243.9 | O(N^2) | DB: 24)
  * `processNodeAsync` (Impact: 80.6 | O(2^N) | DB: 8)
  * `writeNode` (Impact: 43.7 | O(N^1) | DB: 7)
  * `processAnimation` (Impact: 31.2 | O(N^1) | DB: 15)
  * `insertKeyframe` (Impact: 30.1 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 156`, `args: 86`, `func_start: 69`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 588`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 34`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 174`, `import: 1`
* *Defense:* `safety: 100`, `doc: 115`, `immutability_locks: 188`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three, GLTFExporter.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/FBXLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.688 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.812 IQR)
- **Top Global Matches:** file_cluster_17: 13.688, file_cluster_8: 13.831, file_cluster_11: 13.859
- **Magnitude:** 1617.52 | **LOC:** 4463 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 101
- **Risk Profile:** Cognitive Load (68.4938%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bindSkeleton` (Impact: 271.2 | O(N^2) | DB: 101)
  * `parseAnimStacks` (Impact: 221.1 | O(N^1) | DB: 69)
  * `parseMaterial` (Impact: 88.7 | O(N^1) | DB: 1)
  * `createLight` (Impact: 60.1 | O(N^1) | DB: 8)
  * `createCamera` (Impact: 44.5 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 133`, `args: 91`, `func_start: 66`, `class_start: 5`
* *Risk/State:* `state_mutation: 561`, `dead_code: 9`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 9`, `api: 1`, `import: 3`
* *Defense:* `safety: 132`, `doc: 12`, `immutability_locks: 245`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NURBSCurve.js, three, fflate.module.js, FBXLoader.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/jsm/materials/WoodNodeMaterial.js` (JAVASCRIPT) | Magnitude: 80.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 271, immutability_locks: 80, structural_boundaries: 77, state_mutation: 44
- `manual/en/backgrounds.html` (HTML) | Magnitude: 24.7 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 85, indent_spaces: 65, io: 62, structural_boundaries: 54
- `src/objects/InstancedMesh.js` (JAVASCRIPT) | Magnitude: 288.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 170, indent_tabs: 140, doc: 43, structural_boundaries: 30
- `examples/jsm/postprocessing/SSAARenderPass.js` (JAVASCRIPT) | Magnitude: 213.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 142, state_mutation: 108, doc: 30, branch: 20
- `manual/en/tips.html` (HTML) | Magnitude: 44.9 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 119, indent_spaces: 99, structural_boundaries: 86, io: 62

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `editor/js/libs/ternjs/tern.js` (JAVASCRIPT) | Magnitude: 1601.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 616, state_mutation: 442, branch: 319, structural_boundaries: 190
- `editor/js/libs/codemirror/codemirror.js` (JAVASCRIPT) | Magnitude: 20280.36 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4057, state_mutation: 3289, branch: 1940, structural_boundaries: 1215
- `examples/jsm/loaders/lwo/IFFParser.js` (JAVASCRIPT) | Magnitude: 1009.82 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 526, indent_tabs: 347, branch: 136, immutability_locks: 23
- `examples/jsm/misc/VolumeSlice.js` (JAVASCRIPT) | Magnitude: 158.92 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 112, indent_tabs: 101, doc: 33, immutability_locks: 12
- `test/unit/utils/console-wrapper.js` (JAVASCRIPT) | Magnitude: 50.12 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 30, indent_tabs: 13, debug_prints: 8, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/animation/tracks/BooleanKeyframeTrack.js` (JAVASCRIPT) | Magnitude: 15.16 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 5, sec_state_mutation: 5, reflection_metaprogramming: 4
- `src/animation/tracks/StringKeyframeTrack.js` (JAVASCRIPT) | Magnitude: 15.16 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 5, sec_state_mutation: 5, reflection_metaprogramming: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/jsm/physics/RapierPhysics.js` (JAVASCRIPT) | Magnitude: 180.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 188, branch: 53, immutability_locks: 52, state_mutation: 38
- `editor/js/commands/SetMaterialValueCommand.js` (JAVASCRIPT) | Magnitude: 80.5 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 52, indent_tabs: 46, structural_boundaries: 8, func_start: 7
- `src/cameras/OrthographicCamera.js` (JAVASCRIPT) | Magnitude: 167.88 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 131, indent_tabs: 76, doc: 18, structural_boundaries: 10
- `src/renderers/common/nodes/NodeManager.js` (JAVASCRIPT) | Magnitude: 434.92 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 252, state_mutation: 199, doc: 72, branch: 65
- `examples/jsm/controls/FlyControls.js` (JAVASCRIPT) | Magnitude: 575.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 325, indent_tabs: 176, branch: 91, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/loaders/Cache.js` (JAVASCRIPT) | Magnitude: 42.7 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 25, doc: 17, state_mutation: 14, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/jsm/libs/motion-controllers.module.js` (JAVASCRIPT) | Magnitude: 425.64 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 229, state_mutation: 223, branch: 63, structural_boundaries: 24
- `examples/webgl_loader_gltf.html` (HTML) | Magnitude: 62.1 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 140, immutability_locks: 22, structural_boundaries: 21, args: 16
- `src/nodes/core/StackTrace.js` (JAVASCRIPT) | Magnitude: 72.44 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 21, branch: 17, structural_boundaries: 16
- `manual/resources/tools/geo-picking/ogc-parser.js` (JAVASCRIPT) | Magnitude: 0.09 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 155, state_mutation: 41, immutability_locks: 33, func_start: 25
- `src/extras/lib/earcut.js` (JAVASCRIPT) | Magnitude: 1038.74 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 278, branch: 149, state_mutation: 111, structural_boundaries: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/webgpu_reversed_depth_buffer.html` (HTML) | Magnitude: 82.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 176, structural_boundaries: 24, state_mutation: 22, immutability_locks: 22
- `editor/js/GLTFImportDialog.js` (JAVASCRIPT) | Magnitude: 57.5 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 61, state_mutation: 33, immutability_locks: 10, structural_boundaries: 8
- `editor/js/libs/app.js` (JAVASCRIPT) | Magnitude: 190.56 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 160, state_mutation: 69, func_start: 28, branch: 25
- `src/renderers/common/extras/PMREMGenerator.js` (JAVASCRIPT) | Magnitude: 702.04 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 512, state_mutation: 344, immutability_locks: 121, branch: 76
- `examples/webgpu_loader_gltf.html` (HTML) | Magnitude: 108.7 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 160, structural_boundaries: 25, immutability_locks: 23, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/renderers/common/nodes/NodeBuilderState.js` (JAVASCRIPT) | Magnitude: 40.36 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 36, indent_tabs: 29, state_mutation: 23, planned_debt: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/nodes/core/NodeCode.js` (JAVASCRIPT) | Magnitude: 7.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, indent_tabs: 6, state_mutation: 3, structural_boundaries: 2
- `src/core/GLBufferAttribute.js` (JAVASCRIPT) | Magnitude: 42.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 42, indent_tabs: 31, state_mutation: 17, api: 7
- `src/math/Vector3.js` (JAVASCRIPT) | Magnitude: 184.14 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 145, doc: 100, state_mutation: 88, structural_boundaries: 31
- `src/renderers/common/InspectorBase.js` (JAVASCRIPT) | Magnitude: 49.3 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 39, indent_tabs: 26, func_start: 16, args: 15
- `src/nodes/core/NodeAttribute.js` (JAVASCRIPT) | Magnitude: 8.98 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 13, indent_tabs: 6, state_mutation: 4, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/geometries/BoxGeometry.js` (JAVASCRIPT) | Magnitude: 76.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 83, state_mutation: 41, immutability_locks: 19, structural_boundaries: 18
- `examples/webgl_loader_gltf_animation_pointer.html` (HTML) | Magnitude: 10.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 91, structural_boundaries: 16, memory_alloc: 14, immutability_locks: 13
- `editor/js/commands/SetGeometryValueCommand.js` (JAVASCRIPT) | Magnitude: 58.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 37, indent_tabs: 36, structural_boundaries: 8, func_start: 6
- `src/nodes/core/LightingModel.js` (JAVASCRIPT) | Magnitude: 18.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 15, indent_tabs: 9, args: 6, func_start: 6
- `src/renderers/webgl/WebGLOutput.js` (JAVASCRIPT) | Magnitude: 68.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 122, state_mutation: 30, structural_boundaries: 20, encapsulation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `examples/jsm/loaders/TDSLoader.js` (JAVASCRIPT) | Magnitude: 724.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 428, indent_tabs: 406, dead_code: 178, branch: 108
- `test/unit/src/extras/core/Interpolations.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3
- `test/unit/src/renderers/webgl/WebGLAttributes.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3
- `test/unit/src/renderers/webgl/WebGLBackground.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3
- `test/unit/src/renderers/webgl/WebGLBufferRenderer.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `examples/jsm/loaders/usd/USDComposer.js` -> Churn: **93.72%** | Cog Load: 69.7777% | Debt: 0.0%
- `src/loaders/ObjectLoader.js` -> Churn: **64.76%** | Cog Load: 69.6855% | Debt: 0.0%
- `src/materials/nodes/NodeMaterial.js` -> Churn: **64.76%** | Cog Load: 47.5662% | Debt: 99.968%
- `examples/jsm/inspector/ui/Profiler.js` -> Churn: **62.47%** | Cog Load: 76.0282% | Debt: 0.0%
- `src/renderers/common/nodes/NodeManager.js` -> Churn: **62.31%** | Cog Load: 51.7156% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `examples/jsm/loaders/VRMLLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 2218.42
- `examples/jsm/loaders/VTKLoader.js` -> **mrdoob** (100.0% isolated ownership) | Magnitude: 1102.32
- `examples/jsm/inspector/ui/Profiler.js` -> **sunag** (88.9% isolated ownership) | Magnitude: 993.36
- `examples/jsm/loaders/3DMLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 930.16
- `src/renderers/webgl-fallback/utils/WebGLTextureUtils.js` -> **Michael Herzog** (83.3% isolated ownership) | Magnitude: 916.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `editor/js/libs/ternjs/infer.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `editor/js/libs/ternjs/signal.js` -> **Severity: 89.177** (Blast Radius: 0.946 * Doc Risk: 94.2676%)
- `editor/js/libs/ternjs/infer.js` -> **Severity: 71.17** (Blast Radius: 0.992 * Doc Risk: 71.7437%)
- `editor/js/libs/ternjs/def.js` -> **Severity: 70.128** (Blast Radius: 0.79 * Doc Risk: 88.7699%)
- `editor/js/libs/ternjs/comment.js` -> **Severity: 41.791** (Blast Radius: 0.523 * Doc Risk: 79.906%)
- `editor/js/Menubar.js` -> **Severity: 36.7** (Blast Radius: 0.367 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
