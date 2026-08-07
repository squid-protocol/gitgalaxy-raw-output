# ARCHITECTURAL_BRIEF: three.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/three.js` |
| **Timestamp** | `2026-08-07T04:28:07.348308+00:00` |
| **Scan Duration** | `13.49s` |
| **Git Branch** | `dev` |
| **Git Commit** | `f04b082d40e8104ea3003c13fdf9dd6db8f88971` |
| **Git Remote** | `https://github.com/mrdoob/three.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1521 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
> **Architectural Drift Z-Score:** `5.836`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1796 | 66.2% |
| file_cluster_13 | 579 | 21.3% |
| file_cluster_0 | 125 | 4.6% |
| file_cluster_4 | 30 | 1.1% |
| file_cluster_9 | 27 | 1.0% |
| Unknown | 23 | 0.8% |
| file_cluster_17 | 16 | 0.6% |
| file_cluster_7 | 15 | 0.6% |
| file_cluster_11 | 11 | 0.4% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 16.8 | 8.4 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 50.7 | 59.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.9 | 4.5 | 4.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.8 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 14.5 | 0.0 | 0.0 |
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

- `createVisitor` (@ `examples/jsm/loaders/VRMLLoader.js`) -> Impact: **1391.4** | LOC: 2649
- `addChangeToHistory` (@ `editor/js/libs/codemirror/codemirror.js`) -> Impact: **1136.6** | LOC: 1310
  * *Intent:* // Computes display.scroller.scrollLeft + display.gutters.offsetWidth, // but using getBoundingClientRect to get a sub-pixel-accurate // result.
- `parse` (@ `examples/jsm/loaders/VRMLLoader.js`) -> Impact: **1080.8** | LOC: 2598
- `mod` (@ `editor/js/libs/codemirror/mode/javascript.js`) -> Impact: **934.1** | LOC: 947
- `_getVariantPaths` (@ `examples/jsm/loaders/usd/USDComposer.js`) -> Impact: **840.1** | LOC: 1882
- `parse` (@ `examples/jsm/loaders/SVGLoader.js`) -> Impact: **792.1** | LOC: 1842
- `setXRRenderTargetTextures` (@ `src/renderers/webgl-fallback/WebGLBackend.js`) -> Impact: **704.2** | LOC: 2125
  * *Intent:* /** * The target framebuffer when rendering with * the WebXR device API. * * @private * @type {?WebGLFramebuffer} * @default null */
- `setupWorker` (@ `examples/jsm/libs/lottie_canvas.module.js`) -> Impact: **671.3** | LOC: 1613
- `workerStart` (@ `examples/jsm/libs/lottie_canvas.module.js`) -> Impact: **669.5** | LOC: 1613
- `dispatchKey` (@ `editor/js/libs/codemirror/codemirror.js`) -> Impact: **667.2** | LOC: 644

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `manual/examples/resources/data/gpw` | 7 | 30001.0 | 0.0% | 0.0% |
| `examples/jsm/loaders` | 48 | 29735.66 | 38.1% | 0.0% |
| `examples` | 570 | 26976.76 | 11.03% | 0.0% |
| `examples/jsm/libs` | 11 | 18495.92 | 64.64% | 0.0% |
| `manual/examples` | 176 | 13420.22 | 15.36% | 0.0% |
| `editor/js/libs` | 4 | 13380.48 | 86.81% | 77.7% |
| `editor/js/libs/codemirror` | 2 | 10612.77 | 51.96% | 59.2% |
| `src/renderers/webgl` | 27 | 7227.6 | 42.51% | 42.68% |
| `examples/jsm/controls` | 9 | 7215.82 | 42.6% | 0.0% |
| `editor/js/libs/ternjs` | 6 | 7061.7 | 91.78% | 66.3% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `editor/js/LoaderUtils.js` -> **100.0%** Exposure
- `editor/js/Storage.js` -> **100.0%** Exposure
- `editor/js/libs/ternjs/infer.js` -> **100.0%** Exposure
- `editor/js/libs/ui.js` -> **100.0%** Exposure
- `editor/js/libs/ui.three.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `editor/js/Command.js` -> **100.0%** Exposure
- `editor/js/Editor.js` -> **100.0%** Exposure
- `editor/js/GLTFImportDialog.js` -> **100.0%** Exposure
- `editor/js/History.js` -> **100.0%** Exposure
- `editor/js/Selector.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `editor/js/libs/codemirror/codemirror.js` -> **0** Orphaned Functions | **154** Duplicates
- `editor/js/libs/ternjs/infer.js` -> **0** Orphaned Functions | **139** Duplicates
- `examples/jsm/libs/lottie_canvas.module.js` -> **0** Orphaned Functions | **122** Duplicates
- `editor/js/libs/ui.js` -> **0** Orphaned Functions | **77** Duplicates
- `examples/jsm/loaders/SVGLoader.js` -> **0** Orphaned Functions | **67** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `90` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1522` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `editor/js/libs/app.js` (JAVASCRIPT) -> Cumulative Risk: **725.77**
- **Archetype:** `file_cluster_8` (Distance: 12.94 IQR)
- **Magnitude:** 249.16 | **LOC:** 291 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9511%), Cognitive Load (95.7471%)
- **Heaviest Functions:** `Player` (Impact: 59.2), `load` (Impact: 49.3), `animate` (Impact: 9.6)

### 2. `editor/js/libs/codemirror/addon/show-hint.js` (JAVASCRIPT) -> Cumulative Risk: **705.91**
- **Archetype:** `file_cluster_4` (Distance: 14.355 IQR)
- **Magnitude:** 1139.32 | **LOC:** 530 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9165%)
- **Heaviest Functions:** `Widget` (Impact: 156.7), `buildKeyMap` (Impact: 24.6), `resolveAutoHints` (Impact: 20.3)

### 3. `editor/js/libs/codemirror/addon/tern.js` (JAVASCRIPT) -> Cumulative Risk: **697.96**
- **Archetype:** `file_cluster_4` (Distance: 13.5 IQR)
- **Magnitude:** 1736.02 | **LOC:** 751 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9969%)
- **Heaviest Functions:** `mod` (Impact: 356.0), `parseFnType` (Impact: 242.1), `buildRequest` (Impact: 44.5)

### 4. `editor/js/Editor.js` (JAVASCRIPT) -> Cumulative Risk: **684.84**
- **Archetype:** `file_cluster_8` (Distance: 14.336 IQR)
- **Magnitude:** 683.76 | **LOC:** 820 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.4104%), Tech Debt (92.5658%)
- **Heaviest Functions:** `addHelper` (Impact: 37.2), `fromJSON` (Impact: 11.5), `addObject` (Impact: 11.4)

### 5. `src/renderers/common/Renderer.js` (JAVASCRIPT) -> Cumulative Risk: **665.08**
- **Archetype:** `file_cluster_13` (Distance: 15.561 IQR)
- **Magnitude:** 1404.5 | **LOC:** 3681 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 44.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Concurrency (99.987%)
- **Heaviest Functions:** `compileAsync` (Impact: 338.6), `setSize` (Impact: 164.8), `_renderScene` (Impact: 115.3)

### 6. `src/renderers/webgl-fallback/utils/WebGLTimestampQueryPool.js` (JAVASCRIPT) -> Cumulative Risk: **653.05**
- **Archetype:** `file_cluster_4` (Distance: 14.56 IQR)
- **Magnitude:** 429.6 | **LOC:** 397 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9911%), Safety Score (98.8932%)
- **Heaviest Functions:** `resolveQueriesAsync` (Impact: 25.2), `resolveQuery` (Impact: 24.2), `beginQuery` (Impact: 20.4)

### 7. `src/renderers/webgpu/utils/WebGPUTimestampQueryPool.js` (JAVASCRIPT) -> Cumulative Risk: **653.02**
- **Archetype:** `file_cluster_4` (Distance: 13.957 IQR)
- **Magnitude:** 359.82 | **LOC:** 311 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (96.6051%)
- **Heaviest Functions:** `dispose` (Impact: 27.5), `_resolveQueries` (Impact: 26.7), `resolveQueriesAsync` (Impact: 13.5)

### 8. `src/nodes/core/NodeBuilder.js` (JAVASCRIPT) -> Cumulative Risk: **648.16**
- **Archetype:** `file_cluster_13` (Distance: 15.593 IQR)
- **Magnitude:** 964.24 | **LOC:** 3300 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 65.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (90.9063%), Churn (89.39%)
- **Heaviest Functions:** `constructor` (Impact: 250.6), `getNodeUniform` (Impact: 46.5), `format` (Impact: 44.0)

### 9. `src/nodes/tsl/TSLCore.js` (JAVASCRIPT) -> Cumulative Risk: **644.67**
- **Archetype:** `file_cluster_13` (Distance: 13.345 IQR)
- **Magnitude:** 823.84 | **LOC:** 1251 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), State Flux (99.7662%), Documentation (93.6012%)
- **Heaviest Functions:** `ShaderNodeProxy` (Impact: 47.5), `call` (Impact: 39.4), `getProxyParameters` (Impact: 35.4)

### 10. `editor/js/libs/ternjs/tern.js` (JAVASCRIPT) -> Cumulative Risk: **644.21**
- **Archetype:** `file_cluster_17` (Distance: 13.829 IQR)
- **Magnitude:** 1244.88 | **LOC:** 994 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.2755%), Safety Score (98.1209%)
- **Heaviest Functions:** `findCompletions` (Impact: 178.1), `gather` (Impact: 75.3), `invalidDoc` (Impact: 42.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `examples/jsm/libs/lottie_canvas.module.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.41 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.553 IQR)
- **Top Global Matches:** file_cluster_11: 15.41, file_cluster_8: 15.553, file_cluster_17: 15.661
- **Magnitude:** 13224.88 | **LOC:** 14850 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.535%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setupWorker` (Impact: 671.3)
  * `workerStart` (Impact: 669.5)
  * `getDistancePerc` (Impact: 615.0)
  * `bezFunction` (Impact: 586.5)
  * `dataFunctionManager` (Impact: 203.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1411`, `structural_boundaries: 1238`, `args: 448`, `func_start: 485`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 6339`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 122`
* *Architecture:* `io: 59`, `api: 73`, `concurrency: 44`
* *Defense:* `safety: 431`, `doc: 13`, `sync_locks: 7`, `immutability_locks: 43`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` howler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/esprima.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.842 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.812 IQR)
- **Top Global Matches:** file_cluster_11: 15.842, file_cluster_8: 16.033, file_cluster_17: 16.129
- **Magnitude:** 11471.0 | **LOC:** 6401 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.3017%), Tech Debt (10.8685%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 522.7)
  * `parseStatement` (Impact: 109.8)
  * `scanPunctuator` (Impact: 102.8)
  * `parseForStatement` (Impact: 93.9)
  * `isKeyword` (Impact: 89.7)
    * *Intent:* ;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1486`, `structural_boundaries: 975`, `args: 247`, `func_start: 214`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 7`, `state_mutation: 7620`, `dead_code: 9`, `duplicate_logic: 8`
* *Architecture:* `api: 51`, `concurrency: 12`
* *Defense:* `safety: 456`, `doc: 59`, `test: 93`, `immutability_locks: 8`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/codemirror/codemirror.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.385 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.729 IQR)
- **Top Global Matches:** file_cluster_11: 14.385, file_cluster_8: 14.434, file_cluster_15: 14.592
- **Magnitude:** 10612.16 | **LOC:** 9850 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.7624%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `addChangeToHistory` (Impact: 1136.6)
    * *Intent:* // Computes display.scroller.scrollLeft + display.gutters.offsetWidth, // but using getBoundingClien...
  * `dispatchKey` (Impact: 667.2)
  * `stretchSpansOverChange` (Impact: 602.0)
  * `makeChangeFromHistory` (Impact: 339.9)
  * `setSelection` (Impact: 299.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1940`, `structural_boundaries: 1215`, `args: 459`, `func_start: 585`
* *Risk/State:* `safety_bypasses: 423`, `state_mutation: 3233`, `dead_code: 3`, `fragile_debt: 6`, `duplicate_logic: 154`
* *Architecture:* `api: 72`, `concurrency: 38`
* *Defense:* `safety: 52`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `manual/examples/resources/data/gpw/gpw_v4_basic_demographic_characteristics_rev10_a000_014bt_2010_cntm_1_deg.asc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `examples/jsm/loaders/VRMLLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.401 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.363 IQR)
- **Top Global Matches:** file_cluster_8: 13.401, file_cluster_11: 13.453, file_cluster_0: 13.532
- **Magnitude:** 4464.82 | **LOC:** 3647 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.479%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createVisitor` (Impact: 1391.4)
  * `parse` (Impact: 1080.8)
  * `processField` (Impact: 384.9)
  * `buildIndexedFaceSetNode` (Impact: 174.5)
  * `buildElevationGridNode` (Impact: 145.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 584`, `structural_boundaries: 176`, `args: 96`, `func_start: 74`, `class_start: 5`
* *Risk/State:* `state_mutation: 484`, `dead_code: 22`, `duplicate_logic: 10`
* *Architecture:* `io: 7`, `api: 1`, `import: 2`
* *Defense:* `safety: 66`, `doc: 18`, `immutability_locks: 322`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chevrotain.module.min.js, VRMLLoader.js, three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/ternjs/infer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.615 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.289 IQR)
- **Top Global Matches:** file_cluster_11: 14.615, file_cluster_15: 14.82, file_cluster_8: 14.866
- **Magnitude:** 3257.74 | **LOC:** 1636 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.3441%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `f` (Impact: 139.2)
  * `similarType` (Impact: 55.5)
  * `canonicalType` (Impact: 51.8)
  * `infer` (Impact: 42.3)
  * `maybeTagAsGeneric` (Impact: 38.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 580`, `structural_boundaries: 505`, `args: 233`, `func_start: 247`
* *Risk/State:* `safety_bypasses: 121`, `state_mutation: 1483`, `fragile_debt: 1`, `duplicate_logic: 139`
* *Architecture:* `io: 2`, `api: 63`, `import: 5`
* *Defense:* `safety: 54`, `test: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.992
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` signal, acorn_loose, walk, def, acorn
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/jsm/loaders/SVGLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.422 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.759 IQR)
- **Top Global Matches:** file_cluster_8: 12.422, file_cluster_17: 12.694, file_cluster_7: 12.759
- **Magnitude:** 2969.52 | **LOC:** 3268 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (48.0294%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 792.1)
  * `parsePathNode` (Impact: 266.2)
  * `pointsToStrokeWithBuffers` (Impact: 164.7)
  * `parseFloats` (Impact: 118.2)
  * `createShapes` (Impact: 105.3)
    * *Intent:* // Calculate eigenvectors
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 151`, `args: 66`, `func_start: 219`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 275`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 67`
* *Architecture:* `io: 85`, `api: 6`, `import: 1`
* *Defense:* `safety: 117`, `doc: 42`, `immutability_locks: 221`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SVGLoader.js, three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/libs/opentype.module.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.719 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.39 IQR)
- **Top Global Matches:** file_cluster_8: 13.719, file_cluster_11: 13.765, file_cluster_13: 13.936
- **Magnitude:** 2715.46 | **LOC:** 14507 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.277%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tinf_inflate_uncompressed_block` (Impact: 416.8)
  * `CHARSTRING` (Impact: 290.8)
    * *Intent:* /** * Draws cubic curve * @function * curveTo * @memberof opentype.Path.prototype * @param {number} ...
  * `makeGlobalSubrIndex` (Impact: 69.6)
  * `tinf_decode_trees` (Impact: 35.0)
  * `interpretDict` (Impact: 27.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 417`, `args: 119`, `func_start: 118`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1078`, `dead_code: 3`, `fragile_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `io: 8`, `api: 43`, `concurrency: 2`
* *Defense:* `safety: 75`, `doc: 70`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` glyf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/EXRLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.564 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.527 IQR)
- **Top Global Matches:** file_cluster_8: 12.564, file_cluster_7: 12.936, file_cluster_13: 12.957
- **Magnitude:** 2709.18 | **LOC:** 3434 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (73.3217%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 610.6)
    * *Intent:* /** * Constructs a new EXR loader. * * @param {LoadingManager} [manager] - The loading manager.
  * `setupDecoder` (Impact: 285.4)
  * `uncompressB44` (Impact: 92.6)
  * `uncompressDWA` (Impact: 89.8)
  * `parseValue` (Impact: 89.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 242`, `args: 80`, `func_start: 133`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 540`, `dead_code: 3`, `duplicate_logic: 41`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 52`, `doc: 21`, `immutability_locks: 426`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EXRLoader.js, three, fflate.module.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/usd/USDComposer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.069 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.711 IQR)
- **Top Global Matches:** file_cluster_8: 14.069, file_cluster_11: 14.294, file_cluster_13: 14.311
- **Magnitude:** 2655.8 | **LOC:** 4595 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 48.1%
- **Risk Profile:** Cognitive Load (84.0945%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_getVariantPaths` (Impact: 840.1)
  * `_buildGeometryWithSubsets` (Impact: 277.8)
  * `_getTextureFromOpenPBRConnection` (Impact: 253.1)
  * `_buildGeometry` (Impact: 111.2)
  * `_applyOpenPBRSurface` (Impact: 73.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 377`, `structural_boundaries: 126`, `args: 48`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 498`, `duplicate_logic: 10`
* *Architecture:* `io: 20`, `api: 15`, `import: 1`
* *Defense:* `safety: 130`, `doc: 16`, `immutability_locks: 265`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/loaders/GLTFLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.322 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.444 IQR)
- **Top Global Matches:** file_cluster_4: 14.322, file_cluster_8: 14.642, file_cluster_11: 14.695
- **Magnitude:** 2578.8 | **LOC:** 4861 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (50.0344%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadNode` (Impact: 158.5)
  * `parse` (Impact: 77.7)
  * `_createAnimationTracks` (Impact: 71.3)
    * *Intent:* /** * Specification: https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md#ac...
  * `loadMaterial` (Impact: 67.7)
  * `createNodeMesh` (Impact: 55.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 422`, `structural_boundaries: 236`, `args: 161`, `func_start: 121`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 842`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 66`
* *Architecture:* `io: 12`, `api: 19`, `concurrency: 290`, `import: 3`
* *Defense:* `safety: 186`, `doc: 108`, `immutability_locks: 322`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufferGeometryUtils.js, GLTFLoader.js, three, SkeletonUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderers/webgl-fallback/WebGLBackend.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.886 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.652 IQR)
- **Top Global Matches:** file_cluster_13: 14.886, file_cluster_0: 14.889, file_cluster_8: 14.96
- **Magnitude:** 2401.58 | **LOC:** 2779 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 42.1%
- **Risk Profile:** Cognitive Load (48.0568%), Tech Debt (15.1154%)
**Top Internal Functions/Classes:**
  * `setXRRenderTargetTextures` (Impact: 704.2)
    * *Intent:* /** * The target framebuffer when rendering with * the WebXR device API. * * @private * @type {?WebG...
  * `_setFramebuffer` (Impact: 145.8)
  * `draw` (Impact: 103.0)
  * `clear` (Impact: 68.0)
  * `_resolveRenderTarget` (Impact: 51.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 110`, `args: 68`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `state_mutation: 731`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 23`, `concurrency: 38`, `import: 14`
* *Defense:* `safety: 81`, `doc: 228`, `immutability_locks: 241`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WebGLTextureUtils.js, GLSLNodeBuilder.js, WebGLCapabilities.js, utils.js, RenderContext.js, Backend.js, WebGLAttributeUtils.js, WebGLUtils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/controls/OrbitControls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.19 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.424 IQR)
- **Top Global Matches:** file_cluster_0: 15.19, file_cluster_13: 15.293, file_cluster_8: 15.297
- **Magnitude:** 2132.08 | **LOC:** 1964 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (46.3531%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 121.9)
  * `_handleKeyDown` (Impact: 75.5)
  * `onMouseDown` (Impact: 74.1)
  * `onTouchStart` (Impact: 62.3)
  * `onTouchMove` (Impact: 40.7)
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

### `examples/jsm/loaders/FBXLoader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.676 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.825 IQR)
- **Top Global Matches:** file_cluster_17: 13.676, file_cluster_8: 13.828, file_cluster_11: 13.838
- **Magnitude:** 1990.32 | **LOC:** 4463 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (68.3002%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseAnimStacks` (Impact: 221.1)
  * `bindSkeleton` (Impact: 193.2)
  * `parseGeoNode` (Impact: 103.7)
  * `parseMaterial` (Impact: 88.7)
  * `createLight` (Impact: 60.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 133`, `args: 91`, `func_start: 66`, `class_start: 5`
* *Risk/State:* `state_mutation: 559`, `dead_code: 9`, `planned_debt: 4`, `duplicate_logic: 10`
* *Architecture:* `io: 9`, `api: 7`, `import: 3`
* *Defense:* `safety: 132`, `doc: 12`, `immutability_locks: 245`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FBXLoader.js, NURBSCurve.js, three, fflate.module.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/js/libs/codemirror/addon/tern.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.5 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.294 IQR)
- **Top Global Matches:** file_cluster_4: 13.5, file_cluster_8: 13.577, file_cluster_11: 13.651
- **Magnitude:** 1736.02 | **LOC:** 751 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9969%)
**Top Internal Functions/Classes:**
  * `mod` (Impact: 356.0)
    * *Intent:* // queries. // * responseFilter: A function(doc, query, request, error, data) that // will be applie...
  * `parseFnType` (Impact: 242.1)
  * `buildRequest` (Impact: 44.5)
  * `updateArgHints` (Impact: 36.7)
  * `makeTooltip` (Impact: 33.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 163`, `args: 83`, `func_start: 91`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 452`, `duplicate_logic: 31`
* *Architecture:* `api: 8`, `concurrency: 34`, `import: 1`
* *Defense:* `safety: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` codemirror
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/jsm/exporters/GLTFExporter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.869 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.965 IQR)
- **Top Global Matches:** file_cluster_4: 13.869, file_cluster_8: 14.069, file_cluster_11: 14.243
- **Magnitude:** 1655.64 | **LOC:** 3739 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (49.5006%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createNormalizedNormalAttribute` (Impact: 167.9)
  * `processAccessor` (Impact: 74.9)
  * `writeNode` (Impact: 43.7)
  * `processNodeAsync` (Impact: 42.6)
  * `processAnimation` (Impact: 31.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 156`, `args: 86`, `func_start: 69`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 588`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 38`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 174`, `import: 1`
* *Defense:* `safety: 100`, `doc: 115`, `immutability_locks: 188`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GLTFExporter.js, three
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderers/webgpu/utils/WebGPUTextureUtils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.487 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.372 IQR)
- **Top Global Matches:** file_cluster_8: 14.487, file_cluster_13: 14.585, file_cluster_7: 14.69
- **Magnitude:** 1535.14 | **LOC:** 1641 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 21.4%
- **Risk Profile:** Cognitive Load (49.0604%), Tech Debt (94.5379%)
**Top Internal Functions/Classes:**
  * `getFormat` (Impact: 384.7)
  * `error` (Impact: 136.4)
  * `_getBlockData` (Impact: 107.7)
    * *Intent:* // try/catch has been added to fix bad video frame data on certain devices, see #32391
  * `_getBytesPerTexel` (Impact: 97.0)
  * `_getTypedArrayType` (Impact: 96.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 463`, `structural_boundaries: 129`, `args: 27`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 214`, `planned_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `api: 8`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 221`, `doc: 108`, `immutability_locks: 76`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, WebGPUTexturePassUtils.js, WebGPUConstants.js, CubeTexture.js, ColorManagement.js, Texture.js, constants.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderers/webgpu/nodes/WGSLNodeBuilder.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.074 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.608 IQR)
- **Top Global Matches:** file_cluster_0: 15.074, file_cluster_13: 15.131, file_cluster_8: 15.322
- **Magnitude:** 1531.7 | **LOC:** 2511 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 53.6%
- **Risk Profile:** Cognitive Load (47.1173%), Tech Debt (13.9822%)
**Top Internal Functions/Classes:**
  * `generateTextureDimension` (Impact: 441.4)
  * `getUniforms` (Impact: 117.2)
    * *Intent:* /** * Returns `true` if the given builtin is defined in the given shader stage. * * @param {string} ...
  * `generateWrapFunction` (Impact: 33.4)
  * `getVaryings` (Impact: 33.0)
  * `getPropertyName` (Impact: 31.4)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 163`, `args: 50`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 442`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 24`, `import: 14`
* *Defense:* `safety: 89`, `doc: 205`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorageBuffer.js, utils.js, NodeSampledTexture.js, WebGPUConstants.js, NodeSampler.js, WebGPUTextureUtils.js, constants.js, VarNode.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/materials/Material.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 17.457 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.358 IQR)
- **Top Global Matches:** file_cluster_13: 17.457, file_cluster_11: 17.556, file_cluster_8: 17.696
- **Magnitude:** 1514.1 | **LOC:** 1018 | **CtrlFlow:** 89.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.2707%), Tech Debt (57.7495%)
**Top Internal Functions/Classes:**
  * `toJSON` (Impact: 315.9)
    * *Intent:* /** * Represents the RGB values of the constant blend color.
  * `constructor` (Impact: 265.5)
    * *Intent:* /** * Abstract base class for materials. * * Materials define the appearance of renderable 3D object...
  * `setValues` (Impact: 32.0)
  * `copy` (Impact: 10.1)
    * *Intent:* /** * This starts at `0` and counts how many times {@link Material#needsUpdate} is set to `true`. * ...
  * `extractFromCache` (Impact: 5.2)
    * *Intent:* /** * Whether it's possible to override the material with {@link Scene#overrideMaterial} or not. * *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 19`, `args: 11`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 849`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 85`, `doc: 100`, `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, Color.js, constants.js, MathUtils.js, EventDispatcher.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderers/common/Renderer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.561 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.239 IQR)
- **Top Global Matches:** file_cluster_13: 15.561, file_cluster_4: 15.583, file_cluster_0: 15.77
- **Magnitude:** 1404.5 | **LOC:** 3681 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 44.1%
- **Risk Profile:** Cognitive Load (52.1203%), Tech Debt (27.5965%)
**Top Internal Functions/Classes:**
  * `compileAsync` (Impact: 338.6)
    * *Intent:* /** * When `autoClear` is set to `true`, this property defines whether the renderer * should clear t...
  * `setSize` (Impact: 164.8)
  * `_renderScene` (Impact: 115.3)
    * *Intent:* // internals /** * The number of MSAA samples. * * @private
  * `_projectObject` (Impact: 99.3)
  * `_getFrameBufferTarget` (Impact: 23.9)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 86`, `args: 28`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 455`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `concurrency: 89`, `import: 37`
* *Defense:* `safety: 67`, `doc: 149`, `immutability_locks: 83`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ContextNode.js, ReadbackBuffer.js, NodeManager.js, utils.js, XRManager.js, Pipelines.js, constants.js, QuadMesh.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/jsm/materials/WoodNodeMaterial.js` (JAVASCRIPT) | Magnitude: 80.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 271, immutability_locks: 80, structural_boundaries: 77, state_mutation: 44
- `examples/jsm/physics/RapierPhysics.js` (JAVASCRIPT) | Magnitude: 273.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 188, branch: 53, immutability_locks: 52, state_mutation: 38
- `manual/en/backgrounds.html` (HTML) | Magnitude: 24.7 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 85, indent_spaces: 65, io: 62, structural_boundaries: 54
- `src/objects/InstancedMesh.js` (JAVASCRIPT) | Magnitude: 255.34 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 170, indent_tabs: 140, doc: 43, structural_boundaries: 30
- `manual/en/tips.html` (HTML) | Magnitude: 44.9 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 119, indent_spaces: 99, structural_boundaries: 86, io: 62

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/jsm/misc/VolumeSlice.js` (JAVASCRIPT) | Magnitude: 157.22 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 120, indent_tabs: 101, doc: 33, immutability_locks: 12
- `examples/jsm/loaders/lwo/IFFParser.js` (JAVASCRIPT) | Magnitude: 936.32 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 512, indent_tabs: 347, branch: 136, immutability_locks: 23
- `editor/js/libs/codemirror/codemirror.js` (JAVASCRIPT) | Magnitude: 10612.16 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4057, state_mutation: 3233, branch: 1940, structural_boundaries: 1215
- `test/unit/utils/console-wrapper.js` (JAVASCRIPT) | Magnitude: 50.12 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 30, indent_tabs: 13, debug_prints: 8, branch: 5
- `examples/jsm/libs/tween.module.js` (JAVASCRIPT) | Magnitude: 752.22 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 540, state_mutation: 360, structural_boundaries: 170, branch: 113

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/animation/tracks/BooleanKeyframeTrack.js` (JAVASCRIPT) | Magnitude: 15.16 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 5, sec_state_mutation: 5, reflection_metaprogramming: 4
- `src/animation/tracks/StringKeyframeTrack.js` (JAVASCRIPT) | Magnitude: 15.16 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 5, sec_state_mutation: 5, reflection_metaprogramming: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/unit/src/renderers/webgl/WebGLExtensions.tests.js` (JAVASCRIPT) | Magnitude: 28.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 35, test: 12, sec_high_risk_execution: 12, structural_boundaries: 11
- `editor/js/commands/SetMaterialValueCommand.js` (JAVASCRIPT) | Magnitude: 77.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 52, indent_tabs: 46, structural_boundaries: 8, func_start: 7
- `src/renderers/webgl-fallback/WebGLBackend.js` (JAVASCRIPT) | Magnitude: 2401.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 1161, state_mutation: 731, branch: 307, immutability_locks: 241
- `src/cameras/OrthographicCamera.js` (JAVASCRIPT) | Magnitude: 160.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 131, indent_tabs: 76, doc: 18, structural_boundaries: 10
- `examples/jsm/controls/FlyControls.js` (JAVASCRIPT) | Magnitude: 574.96 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 325, indent_tabs: 176, branch: 91, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/loaders/Cache.js` (JAVASCRIPT) | Magnitude: 42.7 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 25, doc: 17, state_mutation: 14, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/jsm/loaders/TDSLoader.js` (JAVASCRIPT) | Magnitude: 720.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 428, indent_tabs: 406, dead_code: 178, branch: 108
- `editor/js/libs/ternjs/tern.js` (JAVASCRIPT) | Magnitude: 1244.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 616, state_mutation: 442, branch: 319, structural_boundaries: 190
- `manual/resources/threejs-lesson-utils.js` (JAVASCRIPT) | Magnitude: 102.78 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 98, state_mutation: 36, structural_boundaries: 19, immutability_locks: 18
- `examples/jsm/libs/motion-controllers.module.js` (JAVASCRIPT) | Magnitude: 379.14 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 229, state_mutation: 223, branch: 63, structural_boundaries: 24
- `src/extras/lib/earcut.js` (JAVASCRIPT) | Magnitude: 764.24 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 278, branch: 149, state_mutation: 111, structural_boundaries: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/renderers/common/nodes/NodeManager.js` (JAVASCRIPT) | Magnitude: 543.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 252, state_mutation: 187, doc: 72, branch: 65
- `editor/js/GLTFImportDialog.js` (JAVASCRIPT) | Magnitude: 57.5 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 61, state_mutation: 33, immutability_locks: 10, structural_boundaries: 8
- `src/renderers/common/extras/PMREMGenerator.js` (JAVASCRIPT) | Magnitude: 694.14 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 512, state_mutation: 344, immutability_locks: 121, branch: 76
- `examples/webgpu_loader_gltf.html` (HTML) | Magnitude: 91.0 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 160, structural_boundaries: 25, immutability_locks: 23, args: 17
- `examples/webgpu_pmrem_scene.html` (HTML) | Magnitude: 27.98 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 94, memory_alloc: 28, structural_boundaries: 15, globals: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/renderers/common/nodes/NodeBuilderState.js` (JAVASCRIPT) | Magnitude: 40.36 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 36, indent_tabs: 29, state_mutation: 23, planned_debt: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `examples/jsm/math/OBB.js` (JAVASCRIPT) | Magnitude: 196.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 178, state_mutation: 85, doc: 53, structural_boundaries: 35
- `src/nodes/core/NodeCode.js` (JAVASCRIPT) | Magnitude: 7.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, indent_tabs: 6, state_mutation: 3, structural_boundaries: 2
- `src/core/GLBufferAttribute.js` (JAVASCRIPT) | Magnitude: 42.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 42, indent_tabs: 31, state_mutation: 17, api: 7
- `src/math/Vector3.js` (JAVASCRIPT) | Magnitude: 182.74 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 145, doc: 100, state_mutation: 88, structural_boundaries: 34
- `examples/jsm/controls/ArcballControls.js` (JAVASCRIPT) | Magnitude: 1265.14 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 700, indent_tabs: 475, branch: 102, doc: 98

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/geometries/BoxGeometry.js` (JAVASCRIPT) | Magnitude: 101.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 83, state_mutation: 41, immutability_locks: 19, structural_boundaries: 18
- `examples/webgl_loader_gltf_animation_pointer.html` (HTML) | Magnitude: 10.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 91, structural_boundaries: 16, memory_alloc: 14, immutability_locks: 13
- `examples/webgpu_reversed_depth_buffer.html` (HTML) | Magnitude: 72.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 176, structural_boundaries: 24, state_mutation: 22, immutability_locks: 22
- `editor/js/commands/SetGeometryValueCommand.js` (JAVASCRIPT) | Magnitude: 55.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 37, indent_tabs: 36, structural_boundaries: 8, func_start: 6
- `examples/jsm/loaders/LDrawLoader.js` (JAVASCRIPT) | Magnitude: 806.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 649, state_mutation: 262, branch: 158, structural_boundaries: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `test/unit/src/extras/core/Interpolations.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3
- `test/unit/src/renderers/webgl/WebGLAttributes.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3
- `test/unit/src/renderers/webgl/WebGLBackground.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3
- `test/unit/src/renderers/webgl/WebGLBufferRenderer.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3
- `test/unit/src/renderers/webgl/WebGLCapabilities.tests.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, args: 3, closures: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/renderers/common/Renderer.js` -> Churn: **100.0%** | Cog Load: 52.1203% | Debt: 27.5965%
- `examples/jsm/loaders/usd/USDComposer.js` -> Churn: **93.72%** | Cog Load: 84.0945% | Debt: 0.0%
- `src/nodes/core/NodeBuilder.js` -> Churn: **89.39%** | Cog Load: 47.8634% | Debt: 61.9335%
- `src/renderers/webgpu/utils/WebGPUTextureUtils.js` -> Churn: **76.17%** | Cog Load: 49.0604% | Debt: 94.5379%
- `src/loaders/ObjectLoader.js` -> Churn: **64.76%** | Cog Load: 69.6264% | Debt: 59.5638%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `examples/jsm/loaders/VRMLLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 4464.82
- `examples/jsm/loaders/VTKLoader.js` -> **mrdoob** (100.0% isolated ownership) | Magnitude: 1354.32
- `examples/jsm/inspector/ui/Profiler.js` -> **sunag** (88.9% isolated ownership) | Magnitude: 1116.26
- `src/renderers/webgl/WebGLUniforms.js` -> **mrdoob** (100.0% isolated ownership) | Magnitude: 941.3
- `examples/jsm/loaders/3DMLoader.js` -> **Michael Herzog** (100.0% isolated ownership) | Magnitude: 929.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `editor/js/libs/ternjs/infer.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `editor/js/libs/ternjs/signal.js` -> **Severity: 62.508** (Blast Radius: 0.946 * Doc Risk: 66.0756%)
- `editor/js/libs/ternjs/infer.js` -> **Severity: 50.484** (Blast Radius: 0.992 * Doc Risk: 50.8915%)
- `editor/js/Viewport.ViewHelper.js` -> **Severity: 36.7** (Blast Radius: 0.367 * Doc Risk: 100.0%)
- `editor/js/commands/Commands.js` -> **Severity: 36.7** (Blast Radius: 0.367 * Doc Risk: 100.0%)
- `src/Three.Core.js` -> **Severity: 36.7** (Blast Radius: 0.367 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
