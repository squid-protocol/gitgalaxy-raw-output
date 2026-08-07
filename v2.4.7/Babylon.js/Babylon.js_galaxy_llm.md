# ARCHITECTURAL_BRIEF: Babylon.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/Babylon.js` |
| **Timestamp** | `2026-08-07T04:09:45.369833+00:00` |
| **Scan Duration** | `42.43s` |
| **Git Branch** | `master` |
| **Git Commit** | `8a9572aaf79143d490a55a164c489632a9a1196e` |
| **Git Remote** | `https://github.com/BabylonJS/Babylon.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3638 malicious artifacts.

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
| Total Artifacts | 6919 |
| Analyzed Artifacts (Scanned) | 4586 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2333 |
| Total LOC | 493751 |
| Volatility Index | 0.01 |
| % Scanned of codebase = | 66.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6236 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1569 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.447 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 160 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 3516 | 445706 | 76.7% |
| XML | 420 | 93 | 9.2% |
| JSON | 167 | 2933 | 3.6% |
| CSS | 144 | 19972 | 3.1% |
| MARKDOWN | 103 | 0 | 2.2% |
| JAVASCRIPT | 98 | 22995 | 2.1% |
| PLAINTEXT | 87 | 1 | 1.9% |
| HTML | 27 | 1885 | 0.6% |
| GLSL | 12 | 154 | 0.3% |
| BINARY_THREAT | 11 | 11 | 0.2% |
| BATCH | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.362`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 2579 | 56.2% |
| file_cluster_8 | 1213 | 26.5% |
| file_cluster_2 | 216 | 4.7% |
| file_cluster_4 | 162 | 3.5% |
| file_cluster_16 | 46 | 1.0% |
| file_cluster_17 | 29 | 0.6% |
| file_cluster_0 | 27 | 0.6% |
| Unknown | 12 | 0.3% |
| file_cluster_11 | 6 | 0.1% |
| file_cluster_7 | 6 | 0.1% |
| file_cluster_12 | 2 | 0.0% |
| file_cluster_15 | 2 | 0.0% |
| file_cluster_9 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 189 | 4.1% |
| Static: Minified & Vendor Opaque Mass | 96 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2333*

**Composition by Extension & Reason:**
- `.png`: 916x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.fx`: 721x Unsupported Format (.fx)
- `.ts`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 2x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.md`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 38x Excluded (Machine-Generated Source Code Signature: 72 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 10166 LOC)
- `.jpg`: 86x Excluded (Explicitly Denied Extension: '.jpg'), 1x Excluded (Explicitly Denied Extension: '.JPG')
- `.json`: 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 25562 LOC), 1x Excluded (Massive Static Asset Blob: 3872 LOC)
- `.js`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 9 exceeds 500 chars), 5x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.ktx`: 38x Excluded (Binary Format Detected)
- `.dds`: 31x Excluded (Binary Format Detected)
- `no_extension`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.wasm`: 24x Excluded (Binary Format Detected)
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gltf`: 13x Excluded (Explicitly Denied Extension: '.gltf')
- `.env`: 9x Excluded (Binary Format Detected), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.babylon`: 8x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Monolithic Amalgamation: 892574 LOC exceeds safe regex boundaries)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 26.7 | 14.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 48.6 | 59.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.4 | 2.3 | 0.0 |
| API Exposure | 0.0 | 20.0 | 6.3 | 6.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 48.2 | 22.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 79.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.9 | 0.1 | 0.1 | 0.1 |
| Volatility Exposure | 0.0 | 98.5 | 17.5 | 22.4 | 22.4 |
| Documentation Exposure | 0.0 | 100.0 | 44.5 | 31.9 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/tools/playground/public/index.js` (Hits: 84)
- `packages/tools/playground/src/tools/monaco/monacoManager.ts` (Hits: 53)
- `packages/dev/core/src/Meshes/mesh.ts` (Hits: 50)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **scene.ts** (`packages/dev/core/src/scene.ts`) — 653 inbound connections
2. **observable.ts** (`packages/dev/core/src/Misc/observable.ts`) — 576 inbound connections
3. **typeStore.ts** (`packages/dev/core/src/Misc/typeStore.ts`) — 532 inbound connections
4. **index.ts** (`packages/dev/serializers/src/3MF/core/index.ts`) — 271 inbound connections
5. **abstractMesh.ts** (`packages/dev/core/src/Meshes/abstractMesh.ts`) — 259 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **blockTools.ts** (`packages/tools/nodeEditor/src/blockTools.ts`) — 117 outbound dependencies
2. **propertyGridTabComponent.tsx** (`packages/dev/inspector/src/components/actionTabs/tabs/propertyGridTabComponent.tsx`) — 116 outbound dependencies
3. **index.ts** (`packages/dev/core/src/PostProcesses/index.ts`) — 102 outbound dependencies
4. **index.ts** (`packages/dev/inspector-v2/src/index.ts`) — 97 outbound dependencies
5. **index.ts** (`packages/dev/core/src/Misc/index.ts`) — 89 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `a` (@ `packages/tools/babylonServer/public/gltf_validator.js`) -> Impact: **1895.8** | LOC: 1924
- `dartProgram` (@ `packages/tools/babylonServer/public/gltf_validator.js`) -> Impact: **1782.7** | LOC: 1844
- `createTexture` (@ `packages/dev/core/src/Engines/webgpuEngine.ts`) -> Impact: **973.1** | LOC: 1154
- `LoadAssetContainer` (@ `packages/dev/core/src/Loading/Plugins/babylonFileLoader.ts`) -> Impact: **699.5** | LOC: 798
- `continuationCallback` (@ `packages/dev/core/src/Engines/webgpuEngine.ts`) -> Impact: **648.1** | LOC: 1115
- `initAsync` (@ `packages/dev/core/src/Engines/webgpuEngine.ts`) -> Impact: **620.5** | LOC: 1187
- `_draw` (@ `packages/dev/core/src/Meshes/mesh.ts`) -> Impact: **600.0** | LOC: 1119
  * *Intent:* /** * Returns the registered LOD mesh distant from the parameter `camera` position if any, else returns the current mesh. * @see https://doc.babylonjs...
- `dispose` (@ `packages/dev/core/src/scene.ts`) -> Impact: **573.8** | LOC: 1577
  * *Intent:* /**
- `_linkPrePassRenderer` (@ `packages/dev/core/src/Rendering/geometryBufferRenderer.ts`) -> Impact: **566.9** | LOC: 1017
  * *Intent:* /** * Constant used to retrieve the velocity texture index in the G-Buffer textures array
- `BASIS` (@ `packages/tools/babylonServer/public/basis_encoder.js`) -> Impact: **540.6** | LOC: 1424

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 19 | 5184.01 | 7.45% | 0.0% |
| `packages/tools/playground/public/scenes/Elf` | 4 | 2000.0 | 0.0% | 0.0% |
| `packages/dev/core/src/Meshes` | 31 | 1993.97 | 36.53% | 29.16% |
| `packages/dev/core/src/Materials` | 46 | 1737.03 | 32.04% | 27.04% |
| `packages/dev/core/src/Misc` | 83 | 1568.21 | 31.88% | 30.94% |
| `packages/dev/core/src/Engines` | 25 | 1507.37 | 24.76% | 18.52% |
| `packages/dev/gui/src/2D/controls` | 26 | 1358.51 | 42.59% | 63.99% |
| `packages/dev/core/src/Rendering` | 27 | 1226.94 | 38.98% | 45.55% |
| `packages/dev/sharedUiComponents/src/imgs` | 139 | 1110.04 | 3.67% | 0.0% |
| `packages/dev/core/src/Particles` | 22 | 1076.96 | 34.29% | 36.88% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/public/@babylonjs/core/watcher.cjs` -> **100.0%** Exposure
- `packages/public/rollupUtils.mjs` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/gltf_validator.js` -> **100.0%** Exposure
- `packages/tools/flowGraphEditor/public/index.js` -> **100.0%** Exposure
- `packages/tools/guiEditor/public/index.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/tools/babylonServer/public/basis_encoder.js` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/gltf_validator.js` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/recast.js` -> **100.0%** Exposure
- `packages/tools/babylonServer/public/uiControls/babylon.uiControls.max.js` -> **100.0%** Exposure
- `packages/tools/vsm/public/index.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/tools/babylonServer/public/gltf_validator.js` -> **24** Orphaned Functions | **952** Duplicates
- `packages/dev/core/src/Maths/math.vector.ts` -> **0** Orphaned Functions | **325** Duplicates
- `packages/dev/core/src/FlowGraph/Blocks/Data/Math/flowGraphMathBlocks.ts` -> **0** Orphaned Functions | **115** Duplicates
- `packages/tools/babylonServer/public/recast.js` -> **0** Orphaned Functions | **95** Duplicates
- `packages/dev/loaders/src/glTF/2.0/Extensions/objectModelMapping.ts` -> **0** Orphaned Functions | **91** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/dev/core/src/Animations/runtimeAnimation.ts`** -> AI Confidence: **99.48%**
2. **`packages/dev/core/src/Loading/Plugins/babylonFileLoader.ts`** -> AI Confidence: **99.48%**
3. **`packages/dev/core/src/Meshes/Builders/boxBuilder.ts`** -> AI Confidence: **99.48%**
4. **`packages/dev/core/src/Meshes/Builders/cylinderBuilder.ts`** -> AI Confidence: **99.48%**
5. **`packages/dev/core/src/Meshes/Builders/ribbonBuilder.ts`** -> AI Confidence: **99.48%**
6. **`packages/dev/core/src/Meshes/Builders/tiledBoxBuilder.ts`** -> AI Confidence: **99.48%**
7. **`packages/dev/core/src/Meshes/mesh.vertexData.ts`** -> AI Confidence: **99.48%**
8. **`packages/dev/gui/src/2D/controls/inputTextArea.ts`** -> AI Confidence: **99.48%**
9. **`packages/dev/core/src/Animations/animatable.core.ts`** -> AI Confidence: **99.39%**
10. **`packages/dev/core/src/Bones/skeleton.functions.ts`** -> AI Confidence: **99.39%**
11. **`packages/dev/core/src/DeviceInput/webDeviceInputSystem.ts`** -> AI Confidence: **99.39%**
12. **`packages/dev/core/src/Engines/Extensions/engine.multiRender.ts`** -> AI Confidence: **99.39%**
13. **`packages/dev/core/src/Engines/WebGL/webGLRenderTargetWrapper.ts`** -> AI Confidence: **99.39%**
14. **`packages/dev/core/src/Engines/WebGPU/Extensions/engine.multiRender.ts`** -> AI Confidence: **99.39%**
15. **`packages/dev/core/src/Engines/WebGPU/webgpuShaderProcessorsGLSL.ts`** -> AI Confidence: **99.39%**
16. **`packages/dev/core/src/Engines/WebGPU/webgpuShaderProcessorsWGSL.ts`** -> AI Confidence: **99.39%**
17. **`packages/dev/core/src/Engines/WebGPU/webgpuTextureManager.ts`** -> AI Confidence: **99.39%**
18. **`packages/dev/core/src/Engines/renderTargetWrapper.ts`** -> AI Confidence: **99.39%**
19. **`packages/dev/core/src/Engines/thinEngine.ts`** -> AI Confidence: **99.39%**
20. **`packages/dev/core/src/Lights/Shadows/shadowGenerator.ts`** -> AI Confidence: **99.39%**
21. **`packages/dev/core/src/Lights/lightingVolume.ts`** -> AI Confidence: **99.39%**
22. **`packages/dev/core/src/Materials/Node/Blocks/PBR/pbrMetallicRoughnessBlock.ts`** -> AI Confidence: **99.39%**
23. **`packages/dev/core/src/Materials/Node/Blocks/PBR/subSurfaceBlock.ts`** -> AI Confidence: **99.39%**
24. **`packages/dev/core/src/Materials/PBR/pbrBaseMaterial.ts`** -> AI Confidence: **99.39%**
25. **`packages/dev/core/src/Materials/Textures/Packer/packer.ts`** -> AI Confidence: **99.39%**
26. **`packages/dev/core/src/Materials/materialHelper.functions.ts`** -> AI Confidence: **99.39%**
27. **`packages/dev/core/src/Materials/shaderMaterial.ts`** -> AI Confidence: **99.39%**
28. **`packages/dev/core/src/Materials/standardMaterial.ts`** -> AI Confidence: **99.39%**
29. **`packages/dev/core/src/Meshes/Builders/greasedLineBuilder.ts`** -> AI Confidence: **99.39%**
30. **`packages/dev/core/src/Meshes/Builders/groundBuilder.ts`** -> AI Confidence: **99.39%**
31. **`packages/dev/core/src/Meshes/Builders/polygonBuilder.ts`** -> AI Confidence: **99.39%**
32. **`packages/dev/core/src/Meshes/Builders/polyhedronBuilder.ts`** -> AI Confidence: **99.39%**
33. **`packages/dev/core/src/Meshes/GreasedLine/greasedLineRibbonMesh.ts`** -> AI Confidence: **99.39%**
34. **`packages/dev/core/src/Meshes/geometry.ts`** -> AI Confidence: **99.39%**
35. **`packages/dev/core/src/Meshes/mesh.ts`** -> AI Confidence: **99.39%**
36. **`packages/dev/core/src/Meshes/trailMesh.ts`** -> AI Confidence: **99.39%**
37. **`packages/dev/core/src/Misc/dds.ts`** -> AI Confidence: **99.39%**
38. **`packages/dev/core/src/Misc/decorators.serialization.ts`** -> AI Confidence: **99.39%**
39. **`packages/dev/core/src/Particles/particleSystem.ts`** -> AI Confidence: **99.39%**
40. **`packages/dev/core/src/Particles/pointsCloudSystem.ts`** -> AI Confidence: **99.39%**
41. **`packages/dev/core/src/Rendering/geometryBufferRenderer.ts`** -> AI Confidence: **99.39%**
42. **`packages/dev/core/src/Rendering/objectRenderer.ts`** -> AI Confidence: **99.39%**
43. **`packages/dev/core/src/XR/features/WebXRControllerPhysics.ts`** -> AI Confidence: **99.39%**
44. **`packages/dev/inspector/src/components/actionTabs/tabs/propertyGrids/animations/curveEditor/graph/keyPoint.tsx`** -> AI Confidence: **99.39%**
45. **`packages/tools/flowGraphEditor/src/graphSystem/smartGroup.ts`** -> AI Confidence: **99.39%**
46. **`packages/dev/core/src/Bones/skeleton.ts`** -> AI Confidence: **99.35%**
47. **`packages/dev/core/src/Engines/Extensions/engine.renderTarget.ts`** -> AI Confidence: **99.35%**
48. **`packages/dev/core/src/Materials/Node/nodeMaterialBuildState.ts`** -> AI Confidence: **99.35%**
49. **`packages/dev/core/src/Materials/effectRenderer.ts`** -> AI Confidence: **99.35%**
50. **`packages/dev/core/src/Animations/animatorAvatar.ts`** -> AI Confidence: **99.34%**
51. **`packages/dev/core/src/Bones/boneIKController.ts`** -> AI Confidence: **99.34%**
52. **`packages/dev/core/src/Bones/boneLookController.ts`** -> AI Confidence: **99.34%**
53. **`packages/dev/core/src/Cameras/targetCamera.ts`** -> AI Confidence: **99.34%**
54. **`packages/dev/core/src/Engines/WebGPU/webgpuCacheBindGroups.ts`** -> AI Confidence: **99.34%**
55. **`packages/dev/core/src/Engines/WebGPU/webgpuTextureHelper.ts`** -> AI Confidence: **99.34%**
56. **`packages/dev/core/src/Materials/clipPlaneMaterialHelper.ts`** -> AI Confidence: **99.34%**
57. **`packages/dev/core/src/Meshes/Builders/shapeBuilder.ts`** -> AI Confidence: **99.34%**
58. **`packages/dev/core/src/Meshes/Builders/tiledPlaneBuilder.ts`** -> AI Confidence: **99.34%**
59. **`packages/dev/core/src/Meshes/thinInstanceMesh.ts`** -> AI Confidence: **99.34%**
60. **`packages/dev/lottiePlayer/src/parsing/spritePacker.ts`** -> AI Confidence: **99.34%**
61. **`packages/tools/babylonServer/src/loaders/index-dev.ts`** -> AI Confidence: **99.34%**
62. **`packages/tools/nodeParticleEditor/src/graphSystem/display/inputDisplayManager.ts`** -> AI Confidence: **99.34%**
63. **`packages/tools/babylonServer/public/gltf_validator.js`** -> AI Confidence: **99.31%**
64. **`packages/dev/addons/src/atmosphere/atmospherePBRMaterialPlugin.ts`** -> AI Confidence: **99.31%**
65. **`packages/dev/addons/src/htmlMesh/htmlMesh.ts`** -> AI Confidence: **99.31%**
66. **`packages/dev/addons/src/htmlMesh/htmlMeshRenderer.ts`** -> AI Confidence: **99.31%**
67. **`packages/dev/addons/src/navigation/generator/generator.single-thread.ts`** -> AI Confidence: **99.31%**
68. **`packages/dev/addons/src/navigation/plugin/RecastJSCrowd.ts`** -> AI Confidence: **99.31%**
69. **`packages/dev/addons/src/navigation/plugin/RecastNavigationJSPlugin.ts`** -> AI Confidence: **99.31%**
70. **`packages/dev/buildTools/src/buildShaders.ts`** -> AI Confidence: **99.31%**
71. **`packages/dev/buildTools/src/generateDeclaration.ts`** -> AI Confidence: **99.31%**
72. **`packages/dev/buildTools/src/webpackTools.ts`** -> AI Confidence: **99.31%**
73. **`packages/dev/core/src/Actions/actionManager.ts`** -> AI Confidence: **99.31%**
74. **`packages/dev/core/src/Actions/interpolateValueAction.ts`** -> AI Confidence: **99.31%**
75. **`packages/dev/core/src/Animations/animatable.ts`** -> AI Confidence: **99.31%**
76. **`packages/dev/core/src/Animations/animation.ts`** -> AI Confidence: **99.31%**
77. **`packages/dev/core/src/Animations/animationGroup.ts`** -> AI Confidence: **99.31%**
78. **`packages/dev/core/src/Audio/audioSceneComponent.ts`** -> AI Confidence: **99.31%**
79. **`packages/dev/core/src/Audio/sound.ts`** -> AI Confidence: **99.31%**
80. **`packages/dev/core/src/AudioV2/abstractAudio/subNodes/spatialAudioSubNode.ts`** -> AI Confidence: **99.31%**
81. **`packages/dev/core/src/AudioV2/webAudio/subNodes/webAudioBusAndSoundSubGraph.ts`** -> AI Confidence: **99.31%**
82. **`packages/dev/core/src/AudioV2/webAudio/webAudioStaticSound.ts`** -> AI Confidence: **99.31%**
83. **`packages/dev/core/src/AudioV2/webAudio/webAudioStreamingSound.ts`** -> AI Confidence: **99.31%**
84. **`packages/dev/core/src/Behaviors/Meshes/attachToBoxBehavior.ts`** -> AI Confidence: **99.31%**
85. **`packages/dev/core/src/Behaviors/Meshes/baseSixDofDragBehavior.ts`** -> AI Confidence: **99.31%**
86. **`packages/dev/core/src/Behaviors/Meshes/followBehavior.ts`** -> AI Confidence: **99.31%**
87. **`packages/dev/core/src/Behaviors/Meshes/handConstraintBehavior.ts`** -> AI Confidence: **99.31%**
88. **`packages/dev/core/src/Bones/bone.ts`** -> AI Confidence: **99.31%**
89. **`packages/dev/core/src/Buffers/buffer.ts`** -> AI Confidence: **99.31%**
90. **`packages/dev/core/src/Cameras/Inputs/BaseCameraPointersInput.ts`** -> AI Confidence: **99.31%**
91. **`packages/dev/core/src/Cameras/Inputs/arcRotateCameraKeyboardMoveInput.ts`** -> AI Confidence: **99.31%**
92. **`packages/dev/core/src/Cameras/Inputs/arcRotateCameraPointersInput.ts`** -> AI Confidence: **99.31%**
93. **`packages/dev/core/src/Cameras/Inputs/flyCameraKeyboardInput.ts`** -> AI Confidence: **99.31%**
94. **`packages/dev/core/src/Cameras/Inputs/followCameraKeyboardMoveInput.ts`** -> AI Confidence: **99.31%**
95. **`packages/dev/core/src/Cameras/Inputs/followCameraPointersInput.ts`** -> AI Confidence: **99.31%**
96. **`packages/dev/core/src/Cameras/Inputs/freeCameraDeviceOrientationInput.ts`** -> AI Confidence: **99.31%**
97. **`packages/dev/core/src/Cameras/Inputs/freeCameraGamepadInput.ts`** -> AI Confidence: **99.31%**
98. **`packages/dev/core/src/Cameras/Inputs/freeCameraKeyboardMoveInput.ts`** -> AI Confidence: **99.31%**
99. **`packages/dev/core/src/Cameras/Inputs/freeCameraMouseInput.ts`** -> AI Confidence: **99.31%**
100. **`packages/dev/core/src/Cameras/Inputs/freeCameraMouseWheelInput.ts`** -> AI Confidence: **99.31%**
101. **`packages/dev/core/src/Cameras/Inputs/freeCameraTouchInput.ts`** -> AI Confidence: **99.31%**
102. **`packages/dev/core/src/Cameras/Inputs/geospatialCameraKeyboardInput.ts`** -> AI Confidence: **99.31%**
103. **`packages/dev/core/src/Cameras/VR/vrExperienceHelper.ts`** -> AI Confidence: **99.31%**
104. **`packages/dev/core/src/Cameras/arcRotateCamera.ts`** -> AI Confidence: **99.31%**
105. **`packages/dev/core/src/Cameras/camera.ts`** -> AI Confidence: **99.31%**
106. **`packages/dev/core/src/Cameras/followCamera.ts`** -> AI Confidence: **99.31%**
107. **`packages/dev/core/src/Cameras/freeCamera.ts`** -> AI Confidence: **99.31%**
108. **`packages/dev/core/src/Cameras/geospatialCameraMovement.ts`** -> AI Confidence: **99.31%**
109. **`packages/dev/core/src/Collisions/gpuPicker.ts`** -> AI Confidence: **99.31%**
110. **`packages/dev/core/src/Collisions/pickingInfo.ts`** -> AI Confidence: **99.31%**
111. **`packages/dev/core/src/Compute/computeEffect.ts`** -> AI Confidence: **99.31%**
112. **`packages/dev/core/src/Compute/computeShader.ts`** -> AI Confidence: **99.31%**
113. **`packages/dev/core/src/Culling/Helper/computeShaderBoundingHelper.ts`** -> AI Confidence: **99.31%**
114. **`packages/dev/core/src/Culling/Helper/transformFeedbackBoundingHelper.ts`** -> AI Confidence: **99.31%**
115. **`packages/dev/core/src/Culling/ray.core.ts`** -> AI Confidence: **99.31%**
116. **`packages/dev/core/src/Engines/AbstractEngine/abstractEngine.cubeTexture.ts`** -> AI Confidence: **99.31%**
117. **`packages/dev/core/src/Engines/Extensions/engine.cubeTexture.ts`** -> AI Confidence: **99.31%**
118. **`packages/dev/core/src/Engines/Extensions/engine.multiview.ts`** -> AI Confidence: **99.31%**
119. **`packages/dev/core/src/Engines/Extensions/engine.query.ts`** -> AI Confidence: **99.31%**
120. **`packages/dev/core/src/Engines/Extensions/engine.rawTexture.ts`** -> AI Confidence: **99.31%**
121. **`packages/dev/core/src/Engines/Native/Extensions/nativeEngine.cubeTexture.ts`** -> AI Confidence: **99.31%**
122. **`packages/dev/core/src/Engines/Native/nativePipelineContext.ts`** -> AI Confidence: **99.31%**
123. **`packages/dev/core/src/Engines/Processors/shaderProcessor.ts`** -> AI Confidence: **99.31%**
124. **`packages/dev/core/src/Engines/WebGPU/Extensions/engine.computeShader.ts`** -> AI Confidence: **99.31%**
125. **`packages/dev/core/src/Engines/WebGPU/Extensions/engine.cubeTexture.ts`** -> AI Confidence: **99.31%**
126. **`packages/dev/core/src/Engines/WebGPU/Extensions/engine.rawTexture.ts`** -> AI Confidence: **99.31%**
127. **`packages/dev/core/src/Engines/WebGPU/Extensions/engine.renderTarget.ts`** -> AI Confidence: **99.31%**
128. **`packages/dev/core/src/Engines/WebGPU/webgpuBufferManager.ts`** -> AI Confidence: **99.31%**
129. **`packages/dev/core/src/Engines/WebGPU/webgpuClearQuad.ts`** -> AI Confidence: **99.31%**
130. **`packages/dev/core/src/Engines/WebGPU/webgpuComputeContext.ts`** -> AI Confidence: **99.31%**
131. **`packages/dev/core/src/Engines/WebGPU/webgpuDrawContext.ts`** -> AI Confidence: **99.31%**
132. **`packages/dev/core/src/Engines/WebGPU/webgpuMaterialContext.ts`** -> AI Confidence: **99.31%**
133. **`packages/dev/core/src/Engines/WebGPU/webgpuPipelineContext.ts`** -> AI Confidence: **99.31%**
134. **`packages/dev/core/src/Engines/WebGPU/webgpuTimestampQuery.ts`** -> AI Confidence: **99.31%**
135. **`packages/dev/core/src/Engines/abstractEngine.functions.ts`** -> AI Confidence: **99.31%**
136. **`packages/dev/core/src/Engines/abstractEngine.ts`** -> AI Confidence: **99.31%**
137. **`packages/dev/core/src/Engines/thinWebGPUEngine.ts`** -> AI Confidence: **99.31%**
138. **`packages/dev/core/src/Engines/webgpuEngine.ts`** -> AI Confidence: **99.31%**
139. **`packages/dev/core/src/FlowGraph/Blocks/Data/Math/flowGraphMatrixMathBlocks.ts`** -> AI Confidence: **99.31%**
140. **`packages/dev/core/src/FlowGraph/Blocks/Data/flowGraphDebugBlock.ts`** -> AI Confidence: **99.31%**
141. **`packages/dev/core/src/FlowGraph/Blocks/Execution/Animation/flowGraphInterpolationBlock.ts`** -> AI Confidence: **99.31%**
142. **`packages/dev/core/src/FlowGraph/Blocks/Execution/Animation/flowGraphPlayAnimationBlock.ts`** -> AI Confidence: **99.31%**
143. **`packages/dev/core/src/FlowGraph/Blocks/Execution/Animation/flowGraphStopAnimationBlock.ts`** -> AI Confidence: **99.31%**
144. **`packages/dev/core/src/FlowGraph/Blocks/Execution/flowGraphSetVariableBlock.ts`** -> AI Confidence: **99.31%**
145. **`packages/dev/core/src/FlowGraph/flowGraph.ts`** -> AI Confidence: **99.31%**
146. **`packages/dev/core/src/FlowGraph/flowGraphValidator.ts`** -> AI Confidence: **99.31%**
147. **`packages/dev/core/src/FlowGraph/serialization.ts`** -> AI Confidence: **99.31%**
148. **`packages/dev/core/src/FrameGraph/Node/Blocks/inputBlock.ts`** -> AI Confidence: **99.31%**
149. **`packages/dev/core/src/FrameGraph/Node/nodeRenderGraph.ts`** -> AI Confidence: **99.31%**
150. **`packages/dev/core/src/FrameGraph/Node/nodeRenderGraphBlock.ts`** -> AI Confidence: **99.31%**
151. **`packages/dev/core/src/FrameGraph/Tasks/Layers/baseLayerTask.ts`** -> AI Confidence: **99.31%**
152. **`packages/dev/core/src/FrameGraph/Tasks/PostProcesses/depthOfFieldTask.ts`** -> AI Confidence: **99.31%**
153. **`packages/dev/core/src/FrameGraph/Tasks/PostProcesses/ssrRenderingPipelineTask.ts`** -> AI Confidence: **99.31%**
154. **`packages/dev/core/src/FrameGraph/Tasks/Rendering/csmShadowGeneratorTask.ts`** -> AI Confidence: **99.31%**
155. **`packages/dev/core/src/FrameGraph/Tasks/Rendering/objectRendererTask.ts`** -> AI Confidence: **99.31%**
156. **`packages/dev/core/src/FrameGraph/frameGraphTextureManager.ts`** -> AI Confidence: **99.31%**
157. **`packages/dev/core/src/Gamepads/gamepadManager.ts`** -> AI Confidence: **99.31%**
158. **`packages/dev/core/src/Gizmos/boundingBoxGizmo.ts`** -> AI Confidence: **99.31%**
159. **`packages/dev/core/src/Gizmos/gizmo.ts`** -> AI Confidence: **99.31%**
160. **`packages/dev/core/src/Gizmos/gizmoManager.ts`** -> AI Confidence: **99.31%**
161. **`packages/dev/core/src/Gizmos/planeRotationGizmo.ts`** -> AI Confidence: **99.31%**
162. **`packages/dev/core/src/Gizmos/rotationGizmo.ts`** -> AI Confidence: **99.31%**
163. **`packages/dev/core/src/Helpers/environmentHelper.ts`** -> AI Confidence: **99.31%**
164. **`packages/dev/core/src/Helpers/sceneHelpers.ts`** -> AI Confidence: **99.31%**
165. **`packages/dev/core/src/Helpers/textureDome.ts`** -> AI Confidence: **99.31%**
166. **`packages/dev/core/src/Inputs/scene.inputManager.ts`** -> AI Confidence: **99.31%**
167. **`packages/dev/core/src/Layers/effectLayerSceneComponent.ts`** -> AI Confidence: **99.31%**
168. **`packages/dev/core/src/Layers/layer.ts`** -> AI Confidence: **99.31%**
169. **`packages/dev/core/src/Layers/thinEffectLayer.ts`** -> AI Confidence: **99.31%**
170. **`packages/dev/core/src/Layers/thinHighlightLayer.ts`** -> AI Confidence: **99.31%**
171. **`packages/dev/core/src/Layers/thinSelectionOutlineLayer.ts`** -> AI Confidence: **99.31%**
172. **`packages/dev/core/src/LensFlares/lensFlareSystem.ts`** -> AI Confidence: **99.31%**
173. **`packages/dev/core/src/Lights/Shadows/cascadedShadowGenerator.ts`** -> AI Confidence: **99.31%**
174. **`packages/dev/core/src/Lights/Shadows/shadowGeneratorSceneComponent.ts`** -> AI Confidence: **99.31%**
175. **`packages/dev/core/src/Lights/directionalLight.ts`** -> AI Confidence: **99.31%**
176. **`packages/dev/core/src/Lights/light.ts`** -> AI Confidence: **99.31%**
177. **`packages/dev/core/src/Lights/spotLight.ts`** -> AI Confidence: **99.31%**
178. **`packages/dev/core/src/Materials/Background/backgroundMaterial.ts`** -> AI Confidence: **99.31%**
179. **`packages/dev/core/src/Materials/GaussianSplatting/gaussianSplattingGpuPickingMaterialPlugin.ts`** -> AI Confidence: **99.31%**
180. **`packages/dev/core/src/Materials/GreasedLine/greasedLinePluginMaterial.ts`** -> AI Confidence: **99.31%**
181. **`packages/dev/core/src/Materials/GreasedLine/greasedLineSimpleMaterial.ts`** -> AI Confidence: **99.31%**
182. **`packages/dev/core/src/Materials/Node/Blocks/Dual/lightBlock.ts`** -> AI Confidence: **99.31%**
183. **`packages/dev/core/src/Materials/Node/Blocks/Dual/reflectionTextureBaseBlock.ts`** -> AI Confidence: **99.31%**
184. **`packages/dev/core/src/Materials/Node/Blocks/Dual/textureBlock.ts`** -> AI Confidence: **99.31%**
185. **`packages/dev/core/src/Materials/Node/Blocks/Fragment/fragmentOutputBlock.ts`** -> AI Confidence: **99.31%**
186. **`packages/dev/core/src/Materials/Node/Blocks/Fragment/perturbNormalBlock.ts`** -> AI Confidence: **99.31%**
187. **`packages/dev/core/src/Materials/Node/Blocks/Fragment/prePassOutputBlock.ts`** -> AI Confidence: **99.31%**
188. **`packages/dev/core/src/Materials/Node/Blocks/Input/inputBlock.ts`** -> AI Confidence: **99.31%**
189. **`packages/dev/core/src/Materials/Node/Blocks/PBR/clearCoatBlock.ts`** -> AI Confidence: **99.31%**
190. **`packages/dev/core/src/Materials/Node/Blocks/PBR/reflectionBlock.ts`** -> AI Confidence: **99.31%**
191. **`packages/dev/core/src/Materials/Node/Blocks/PBR/sheenBlock.ts`** -> AI Confidence: **99.31%**
192. **`packages/dev/core/src/Materials/Node/Blocks/Vertex/instancesBlock.ts`** -> AI Confidence: **99.31%**
193. **`packages/dev/core/src/Materials/Node/Blocks/Vertex/morphTargetsBlock.ts`** -> AI Confidence: **99.31%**
194. **`packages/dev/core/src/Materials/Node/Blocks/colorConverterBlock.ts`** -> AI Confidence: **99.31%**
195. **`packages/dev/core/src/Materials/Node/Blocks/conditionalBlock.ts`** -> AI Confidence: **99.31%**
196. **`packages/dev/core/src/Materials/Node/Blocks/curveBlock.ts`** -> AI Confidence: **99.31%**
197. **`packages/dev/core/src/Materials/Node/Blocks/meshAttributeExistsBlock.ts`** -> AI Confidence: **99.31%**
198. **`packages/dev/core/src/Materials/Node/Blocks/transformBlock.ts`** -> AI Confidence: **99.31%**
199. **`packages/dev/core/src/Materials/Node/Blocks/triPlanarBlock.ts`** -> AI Confidence: **99.31%**
200. **`packages/dev/core/src/Materials/Node/Blocks/trigonometryBlock.ts`** -> AI Confidence: **99.31%**
201. **`packages/dev/core/src/Materials/Node/Blocks/vectorMergerBlock.ts`** -> AI Confidence: **99.31%**
202. **`packages/dev/core/src/Materials/Node/nodeMaterial.ts`** -> AI Confidence: **99.31%**
203. **`packages/dev/core/src/Materials/Node/nodeMaterialBlock.ts`** -> AI Confidence: **99.31%**
204. **`packages/dev/core/src/Materials/PBR/openpbrMaterial.ts`** -> AI Confidence: **99.31%**
205. **`packages/dev/core/src/Materials/PBR/pbrClearCoatConfiguration.ts`** -> AI Confidence: **99.31%**
206. **`packages/dev/core/src/Materials/PBR/pbrIridescenceConfiguration.ts`** -> AI Confidence: **99.31%**
207. **`packages/dev/core/src/Materials/PBR/pbrSheenConfiguration.ts`** -> AI Confidence: **99.31%**
208. **`packages/dev/core/src/Materials/Textures/Procedurals/customProceduralTexture.ts`** -> AI Confidence: **99.31%**
209. **`packages/dev/core/src/Materials/Textures/Procedurals/proceduralTexture.ts`** -> AI Confidence: **99.31%**
210. **`packages/dev/core/src/Materials/Textures/colorGradingTexture.ts`** -> AI Confidence: **99.31%**
211. **`packages/dev/core/src/Materials/Textures/cubeTexture.ts`** -> AI Confidence: **99.31%**
212. **`packages/dev/core/src/Materials/Textures/dynamicTexture.ts`** -> AI Confidence: **99.31%**
213. **`packages/dev/core/src/Materials/Textures/envCubeTexture.ts`** -> AI Confidence: **99.31%**
214. **`packages/dev/core/src/Materials/Textures/htmlElementTexture.ts`** -> AI Confidence: **99.31%**
215. **`packages/dev/core/src/Materials/Textures/internalTexture.ts`** -> AI Confidence: **99.31%**
216. **`packages/dev/core/src/Materials/Textures/multiRenderTarget.ts`** -> AI Confidence: **99.31%**
217. **`packages/dev/core/src/Materials/Textures/texture.ts`** -> AI Confidence: **99.31%**
218. **`packages/dev/core/src/Materials/Textures/textureMerger.ts`** -> AI Confidence: **99.31%**
219. **`packages/dev/core/src/Materials/Textures/videoTexture.ts`** -> AI Confidence: **99.31%**
220. **`packages/dev/core/src/Materials/effect.functions.ts`** -> AI Confidence: **99.31%**
221. **`packages/dev/core/src/Materials/effect.webgl.functions.ts`** -> AI Confidence: **99.31%**
222. **`packages/dev/core/src/Materials/material.ts`** -> AI Confidence: **99.31%**
223. **`packages/dev/core/src/Materials/materialPluginManager.ts`** -> AI Confidence: **99.31%**
224. **`packages/dev/core/src/Materials/meshDebugPluginMaterial.ts`** -> AI Confidence: **99.31%**
225. **`packages/dev/core/src/Materials/multiMaterial.ts`** -> AI Confidence: **99.31%**
226. **`packages/dev/core/src/Materials/pushMaterial.ts`** -> AI Confidence: **99.31%**
227. **`packages/dev/core/src/Materials/shadowDepthWrapper.ts`** -> AI Confidence: **99.31%**
228. **`packages/dev/core/src/Materials/uniformBuffer.ts`** -> AI Confidence: **99.31%**
229. **`packages/dev/core/src/Meshes/Builders/geodesicBuilder.ts`** -> AI Confidence: **99.31%**
230. **`packages/dev/core/src/Meshes/Builders/goldbergBuilder.ts`** -> AI Confidence: **99.31%**
231. **`packages/dev/core/src/Meshes/Builders/linesBuilder.ts`** -> AI Confidence: **99.31%**
232. **`packages/dev/core/src/Meshes/Builders/planeBuilder.ts`** -> AI Confidence: **99.31%**
233. **`packages/dev/core/src/Meshes/Builders/textBuilder.ts`** -> AI Confidence: **99.31%**
234. **`packages/dev/core/src/Meshes/GaussianSplatting/gaussianSplattingMesh.ts`** -> AI Confidence: **99.31%**
235. **`packages/dev/core/src/Meshes/GaussianSplatting/gaussianSplattingMeshBase.ts`** -> AI Confidence: **99.31%**
236. **`packages/dev/core/src/Meshes/GreasedLine/greasedLineMesh.ts`** -> AI Confidence: **99.31%**
237. **`packages/dev/core/src/Meshes/Node/Blocks/Set/setPositionsBlock.ts`** -> AI Confidence: **99.31%**
238. **`packages/dev/core/src/Meshes/Node/Blocks/booleanGeometryBlock.ts`** -> AI Confidence: **99.31%**
239. **`packages/dev/core/src/Meshes/Node/Blocks/conditionBlock.ts`** -> AI Confidence: **99.31%**
240. **`packages/dev/core/src/Meshes/Node/Blocks/extrudeGeometryBlock.ts`** -> AI Confidence: **99.31%**
241. **`packages/dev/core/src/Meshes/Node/Blocks/geometryCurveBlock.ts`** -> AI Confidence: **99.31%**
242. **`packages/dev/core/src/Meshes/Node/Blocks/geometryEaseBlock.ts`** -> AI Confidence: **99.31%**
243. **`packages/dev/core/src/Meshes/Node/Blocks/geometryInputBlock.ts`** -> AI Confidence: **99.31%**
244. **`packages/dev/core/src/Meshes/Node/Blocks/geometryOptimizeBlock.ts`** -> AI Confidence: **99.31%**
245. **`packages/dev/core/src/Meshes/Node/Blocks/geometryTrigonometryBlock.ts`** -> AI Confidence: **99.31%**
246. **`packages/dev/core/src/Meshes/Node/Blocks/randomBlock.ts`** -> AI Confidence: **99.31%**
247. **`packages/dev/core/src/Meshes/Node/nodeGeometry.ts`** -> AI Confidence: **99.31%**
248. **`packages/dev/core/src/Meshes/Node/nodeGeometryBlock.ts`** -> AI Confidence: **99.31%**
249. **`packages/dev/core/src/Meshes/Node/nodeGeometryBuildState.ts`** -> AI Confidence: **99.31%**
250. **`packages/dev/core/src/Meshes/abstractMesh.ts`** -> AI Confidence: **99.31%**
251. **`packages/dev/core/src/Meshes/csg.ts`** -> AI Confidence: **99.31%**
252. **`packages/dev/core/src/Meshes/csg2.ts`** -> AI Confidence: **99.31%**
253. **`packages/dev/core/src/Meshes/goldbergMesh.ts`** -> AI Confidence: **99.31%**
254. **`packages/dev/core/src/Meshes/instancedMesh.ts`** -> AI Confidence: **99.31%**
255. **`packages/dev/core/src/Meshes/linesMesh.ts`** -> AI Confidence: **99.31%**
256. **`packages/dev/core/src/Meshes/meshSimplification.ts`** -> AI Confidence: **99.31%**
257. **`packages/dev/core/src/Meshes/polygonMesh.ts`** -> AI Confidence: **99.31%**
258. **`packages/dev/core/src/Meshes/subMesh.ts`** -> AI Confidence: **99.31%**
259. **`packages/dev/core/src/Meshes/transformNode.ts`** -> AI Confidence: **99.31%**
260. **`packages/dev/core/src/Misc/HighDynamicRange/cubemapToSphericalPolynomial.ts`** -> AI Confidence: **99.31%**
261. **`packages/dev/core/src/Misc/PerformanceViewer/performanceViewerCollector.ts`** -> AI Confidence: **99.31%**
262. **`packages/dev/core/src/Misc/basis.ts`** -> AI Confidence: **99.31%**
263. **`packages/dev/core/src/Misc/environmentTextureTools.ts`** -> AI Confidence: **99.31%**
264. **`packages/dev/core/src/Misc/fileTools.ts`** -> AI Confidence: **99.31%**
265. **`packages/dev/core/src/Misc/greasedLineTools.ts`** -> AI Confidence: **99.31%**
266. **`packages/dev/core/src/Misc/khronosTextureContainer2.ts`** -> AI Confidence: **99.31%**
267. **`packages/dev/core/src/Misc/screenshotTools.ts`** -> AI Confidence: **99.31%**
268. **`packages/dev/core/src/Misc/snapshotRenderingHelper.ts`** -> AI Confidence: **99.31%**
269. **`packages/dev/core/src/Misc/textureTools.ts`** -> AI Confidence: **99.31%**
270. **`packages/dev/core/src/Misc/thinMinMaxReducer.ts`** -> AI Confidence: **99.31%**
271. **`packages/dev/core/src/Morph/morphTarget.ts`** -> AI Confidence: **99.31%**
272. **`packages/dev/core/src/Morph/morphTargetManager.ts`** -> AI Confidence: **99.31%**
273. **`packages/dev/core/src/Navigation/Plugins/recastJSPlugin.ts`** -> AI Confidence: **99.31%**
274. **`packages/dev/core/src/Offline/database.ts`** -> AI Confidence: **99.31%**
275. **`packages/dev/core/src/Particles/Node/Blocks/Conditions/particleConditionBlock.ts`** -> AI Confidence: **99.31%**
276. **`packages/dev/core/src/Particles/Node/Blocks/particleInputBlock.ts`** -> AI Confidence: **99.31%**
277. **`packages/dev/core/src/Particles/Node/Blocks/particleRandomBlock.ts`** -> AI Confidence: **99.31%**
278. **`packages/dev/core/src/Particles/Node/Blocks/particleTrigonometryBlock.ts`** -> AI Confidence: **99.31%**
279. **`packages/dev/core/src/Particles/Node/nodeParticleBlock.ts`** -> AI Confidence: **99.31%**
280. **`packages/dev/core/src/Particles/Node/nodeParticleSystemSet.helper.ts`** -> AI Confidence: **99.31%**
281. **`packages/dev/core/src/Particles/Node/nodeParticleSystemSet.ts`** -> AI Confidence: **99.31%**
282. **`packages/dev/core/src/Particles/gpuParticleSystem.ts`** -> AI Confidence: **99.31%**
283. **`packages/dev/core/src/Particles/particle.ts`** -> AI Confidence: **99.31%**
284. **`packages/dev/core/src/Particles/particleSystemSet.ts`** -> AI Confidence: **99.31%**
285. **`packages/dev/core/src/Particles/solidParticleSystem.ts`** -> AI Confidence: **99.31%**
286. **`packages/dev/core/src/Particles/thinParticleSystem.ts`** -> AI Confidence: **99.31%**
287. **`packages/dev/core/src/Particles/webgl2ParticleSystem.ts`** -> AI Confidence: **99.31%**
288. **`packages/dev/core/src/Physics/physicsHelper.ts`** -> AI Confidence: **99.31%**
289. **`packages/dev/core/src/Physics/v1/Plugins/ammoJSPlugin.ts`** -> AI Confidence: **99.31%**
290. **`packages/dev/core/src/Physics/v1/Plugins/cannonJSPlugin.ts`** -> AI Confidence: **99.31%**
291. **`packages/dev/core/src/Physics/v1/Plugins/oimoJSPlugin.ts`** -> AI Confidence: **99.31%**
292. **`packages/dev/core/src/Physics/v1/physicsImpostor.ts`** -> AI Confidence: **99.31%**
293. **`packages/dev/core/src/Physics/v2/IPhysicsEnginePlugin.ts`** -> AI Confidence: **99.31%**
294. **`packages/dev/core/src/Physics/v2/Plugins/havokPlugin.ts`** -> AI Confidence: **99.31%**
295. **`packages/dev/core/src/Physics/v2/characterController.ts`** -> AI Confidence: **99.31%**
296. **`packages/dev/core/src/Physics/v2/physicsAggregate.ts`** -> AI Confidence: **99.31%**
297. **`packages/dev/core/src/Physics/v2/physicsBody.ts`** -> AI Confidence: **99.31%**
298. **`packages/dev/core/src/Physics/v2/ragdoll.ts`** -> AI Confidence: **99.31%**
299. **`packages/dev/core/src/PostProcesses/RenderPipeline/Pipelines/defaultRenderingPipeline.ts`** -> AI Confidence: **99.31%**
300. **`packages/dev/core/src/PostProcesses/RenderPipeline/Pipelines/ssrRenderingPipeline.ts`** -> AI Confidence: **99.31%**
301. **`packages/dev/core/src/PostProcesses/RenderPipeline/postProcessRenderPipeline.ts`** -> AI Confidence: **99.31%**
302. **`packages/dev/core/src/PostProcesses/postProcess.ts`** -> AI Confidence: **99.31%**
303. **`packages/dev/core/src/PostProcesses/postProcessManager.ts`** -> AI Confidence: **99.31%**
304. **`packages/dev/core/src/PostProcesses/thinBlurPostProcess.ts`** -> AI Confidence: **99.31%**
305. **`packages/dev/core/src/PostProcesses/thinPassPostProcess.ts`** -> AI Confidence: **99.31%**
306. **`packages/dev/core/src/PostProcesses/thinSSAO2PostProcess.ts`** -> AI Confidence: **99.31%**
307. **`packages/dev/core/src/PostProcesses/thinSSRPostProcess.ts`** -> AI Confidence: **99.31%**
308. **`packages/dev/core/src/PostProcesses/thinTAAPostProcess.ts`** -> AI Confidence: **99.31%**
309. **`packages/dev/core/src/PostProcesses/volumetricLightScatteringPostProcess.ts`** -> AI Confidence: **99.31%**
310. **`packages/dev/core/src/Probes/reflectionProbe.ts`** -> AI Confidence: **99.31%**
311. **`packages/dev/core/src/Rendering/GlobalIllumination/giRSMManager.ts`** -> AI Confidence: **99.31%**
312. **`packages/dev/core/src/Rendering/IBLShadows/iblShadowsRenderPipeline.ts`** -> AI Confidence: **99.31%**
313. **`packages/dev/core/src/Rendering/IBLShadows/iblShadowsVoxelRenderer.ts`** -> AI Confidence: **99.31%**
314. **`packages/dev/core/src/Rendering/boundingBoxRenderer.ts`** -> AI Confidence: **99.31%**
315. **`packages/dev/core/src/Rendering/depthRenderer.ts`** -> AI Confidence: **99.31%**
316. **`packages/dev/core/src/Rendering/depthRendererSceneComponent.ts`** -> AI Confidence: **99.31%**
317. **`packages/dev/core/src/Rendering/edgesRenderer.ts`** -> AI Confidence: **99.31%**
318. **`packages/dev/core/src/Rendering/fluidRenderer/fluidRenderingObjectCustomParticles.ts`** -> AI Confidence: **99.31%**
319. **`packages/dev/core/src/Rendering/outlineRenderer.ts`** -> AI Confidence: **99.31%**
320. **`packages/dev/core/src/Rendering/prePassRenderer.ts`** -> AI Confidence: **99.31%**
321. **`packages/dev/core/src/Rendering/renderingGroup.ts`** -> AI Confidence: **99.31%**
322. **`packages/dev/core/src/Rendering/renderingManager.ts`** -> AI Confidence: **99.31%**
323. **`packages/dev/core/src/Rendering/utilityLayerRenderer.ts`** -> AI Confidence: **99.31%**
324. **`packages/dev/core/src/Sprites/spriteManager.ts`** -> AI Confidence: **99.31%**
325. **`packages/dev/core/src/Sprites/spriteMap.ts`** -> AI Confidence: **99.31%**
326. **`packages/dev/core/src/Sprites/spriteRenderer.ts`** -> AI Confidence: **99.31%**
327. **`packages/dev/core/src/Sprites/spriteSceneComponent.ts`** -> AI Confidence: **99.31%**
328. **`packages/dev/core/src/XR/features/Layers/WebXRCompositionLayer.ts`** -> AI Confidence: **99.31%**
329. **`packages/dev/core/src/XR/features/WebXRAnchorSystem.ts`** -> AI Confidence: **99.31%**
330. **`packages/dev/core/src/XR/features/WebXRControllerMovement.ts`** -> AI Confidence: **99.31%**
331. **`packages/dev/core/src/XR/features/WebXRDepthSensing.ts`** -> AI Confidence: **99.31%**
332. **`packages/dev/core/src/XR/features/WebXRHandTracking.ts`** -> AI Confidence: **99.31%**
333. **`packages/dev/core/src/XR/features/WebXRHitTest.ts`** -> AI Confidence: **99.31%**
334. **`packages/dev/core/src/XR/features/WebXRLightEstimation.ts`** -> AI Confidence: **99.31%**
335. **`packages/dev/core/src/XR/features/WebXRMeshDetector.ts`** -> AI Confidence: **99.31%**
336. **`packages/dev/core/src/XR/motionController/webXRMicrosoftMixedRealityController.ts`** -> AI Confidence: **99.31%**
337. **`packages/dev/core/src/XR/motionController/webXRProfiledMotionController.ts`** -> AI Confidence: **99.31%**
338. **`packages/dev/core/src/XR/webXRCamera.ts`** -> AI Confidence: **99.31%**
339. **`packages/dev/core/src/XR/webXRDefaultExperience.ts`** -> AI Confidence: **99.31%**
340. **`packages/dev/core/src/XR/webXRInputSource.ts`** -> AI Confidence: **99.31%**
341. **`packages/dev/core/src/XR/webXRManagedOutputCanvas.ts`** -> AI Confidence: **99.31%**
342. **`packages/dev/core/src/assetContainer.ts`** -> AI Confidence: **99.31%**
343. **`packages/dev/core/src/node.ts`** -> AI Confidence: **99.31%**
344. **`packages/dev/core/src/scene.ts`** -> AI Confidence: **99.31%**
345. **`packages/dev/gui/src/2D/advancedDynamicTexture.ts`** -> AI Confidence: **99.31%**
346. **`packages/dev/gui/src/2D/controls/colorpicker.ts`** -> AI Confidence: **99.31%**
347. **`packages/dev/gui/src/2D/controls/container.ts`** -> AI Confidence: **99.31%**
348. **`packages/dev/gui/src/2D/controls/grid.ts`** -> AI Confidence: **99.31%**
349. **`packages/dev/gui/src/2D/controls/image.ts`** -> AI Confidence: **99.31%**
350. **`packages/dev/gui/src/2D/controls/inputText.ts`** -> AI Confidence: **99.31%**
351. **`packages/dev/gui/src/2D/controls/multiLine.ts`** -> AI Confidence: **99.31%**
352. **`packages/dev/gui/src/2D/controls/scrollViewers/scrollViewer.ts`** -> AI Confidence: **99.31%**
353. **`packages/dev/gui/src/2D/controls/sliders/baseSlider.ts`** -> AI Confidence: **99.31%**
354. **`packages/dev/gui/src/2D/controls/sliders/imageBasedSlider.ts`** -> AI Confidence: **99.31%**
355. **`packages/dev/gui/src/2D/controls/sliders/imageScrollBar.ts`** -> AI Confidence: **99.31%**
356. **`packages/dev/gui/src/2D/controls/sliders/slider.ts`** -> AI Confidence: **99.31%**
357. **`packages/dev/gui/src/2D/controls/stackPanel.ts`** -> AI Confidence: **99.31%**
358. **`packages/dev/gui/src/2D/controls/textBlock.ts`** -> AI Confidence: **99.31%**
359. **`packages/dev/gui/src/2D/controls/toggleButton.ts`** -> AI Confidence: **99.31%**
360. **`packages/dev/gui/src/2D/controls/virtualKeyboard.ts`** -> AI Confidence: **99.31%**
361. **`packages/dev/gui/src/3D/controls/MRTK3/touchHolographicButton.ts`** -> AI Confidence: **99.31%**
362. **`packages/dev/gui/src/3D/controls/touchButton3D.ts`** -> AI Confidence: **99.31%**
363. **`packages/dev/gui/src/3D/gizmos/slateGizmo.ts`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `54` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10685` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/dev/inspector/src/components/globalState.ts` (TYPESCRIPT) -> Cumulative Risk: **784.54**
- **Archetype:** `file_cluster_13` (Distance: 11.981 IQR)
- **Magnitude:** 22.37 | **LOC:** 234 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `prepareGLTFPlugin` (Impact: 19.8), `enableLightGizmo` (Impact: 19.1), `enableCameraGizmo` (Impact: 19.1)

### 2. `packages/dev/sharedUiComponents/src/nodeGraphSystem/frameNodePort.ts` (TYPESCRIPT) -> Cumulative Risk: **782.78**
- **Archetype:** `file_cluster_13` (Distance: 11.2 IQR)
- **Magnitude:** 10.83 | **LOC:** 100 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Tech Debt (97.1366%)
- **Heaviest Functions:** `constructor` (Impact: 15.4), `CreateFrameNodePortElement` (Impact: 13.4), `super` (Impact: 11.9)

### 3. `packages/dev/core/src/Engines/WebGPU/webgpuTimestampQuery.ts` (TYPESCRIPT) -> Cumulative Risk: **781.63**
- **Archetype:** `file_cluster_4` (Distance: 14.26 IQR)
- **Magnitude:** 23.68 | **LOC:** 149 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `enable` (Impact: 14.4), `endPass` (Impact: 11.0), `endFrame` (Impact: 8.7)

### 4. `packages/dev/core/src/AudioV2/webAudio/webAudioEngine.ts` (TYPESCRIPT) -> Cumulative Risk: **775.71**
- **Archetype:** `file_cluster_4` (Distance: 15.453 IQR)
- **Magnitude:** 76.64 | **LOC:** 530 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `dispose` (Impact: 15.2), `_initAsync` (Impact: 14.2), `_onAudioContextStateChange` (Impact: 13.1)

### 5. `packages/dev/core/src/Misc/thinMinMaxReducer.ts` (TYPESCRIPT) -> Cumulative Risk: **771.47**
- **Archetype:** `file_cluster_13` (Distance: 12.674 IQR)
- **Magnitude:** 22.77 | **LOC:** 207 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.8937%)
- **Heaviest Functions:** `_recreatePostProcesses` (Impact: 17.6), `readMinMax` (Impact: 11.3), `bind` (Impact: 10.3)

### 6. `packages/dev/core/src/FrameGraph/frameGraphTask.ts` (TYPESCRIPT) -> Cumulative Risk: **770.31**
- **Archetype:** `file_cluster_13` (Distance: 14.58 IQR)
- **Magnitude:** 33.01 | **LOC:** 285 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.4718%)
- **Heaviest Functions:** `_checkTask` (Impact: 55.5), `_execute` (Impact: 14.7), `_initializePasses` (Impact: 12.9)

### 7. `packages/dev/core/src/FrameGraph/Tasks/PostProcesses/volumetricLightingTask.ts` (TYPESCRIPT) -> Cumulative Risk: **769.4**
- **Archetype:** `file_cluster_13` (Distance: 14.007 IQR)
- **Magnitude:** 35.75 | **LOC:** 313 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9967%), Safety Score (99.6697%)
- **Heaviest Functions:** `record` (Impact: 25.8), `name` (Impact: 13.0), `constructor` (Impact: 10.2)

### 8. `packages/dev/core/src/Materials/material.ts` (TYPESCRIPT) -> Cumulative Risk: **767.37**
- **Archetype:** `file_cluster_13` (Distance: 15.01 IQR)
- **Magnitude:** 195.27 | **LOC:** 2144 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9783%)
- **Heaviest Functions:** `forceCompilation` (Impact: 45.2), `_disposeMeshResources` (Impact: 40.8), `_markAllSubMeshesAsDirty` (Impact: 39.5)

### 9. `packages/dev/core/src/Rendering/fluidRenderer/fluidRenderingObject.ts` (TYPESCRIPT) -> Cumulative Risk: **763.26**
- **Archetype:** `file_cluster_13` (Distance: 14.362 IQR)
- **Magnitude:** 36.16 | **LOC:** 274 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_createEffects` (Impact: 14.9), `renderThicknessTexture` (Impact: 10.2), `renderDepthTexture` (Impact: 9.9)

### 10. `packages/dev/core/src/Rendering/fluidRenderer/fluidRenderingTextures.ts` (TYPESCRIPT) -> Cumulative Risk: **761.71**
- **Archetype:** `file_cluster_4` (Distance: 13.13 IQR)
- **Magnitude:** 58.23 | **LOC:** 484 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9936%), Safety Score (98.5127%)
- **Heaviest Functions:** `_createBlurPostProcesses` (Impact: 72.7), `constructor` (Impact: 26.1), `dispose` (Impact: 13.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dev/core/src/Physics/v2/IPhysicsEnginePlugin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.37 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.336 IQR)
- **Top Global Matches:** file_cluster_13: 13.37, file_cluster_8: 13.477, file_cluster_2: 13.582
- **Magnitude:** 560.26 | **LOC:** 499 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.6108%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 61`, `args: 85`, `func_start: 85`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 16`, `concurrency: 6`, `import: 12`
* *Defense:* `safety: 52`, `doc: 75`, `sync_locks: 1`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` math.vector, observable, physicsBody, physicsShape, physicsRaycastResult, transformNode, mesh, groundMesh...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dev/core/src/Engines/thinEngine.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.6 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.647 IQR)
- **Top Global Matches:** file_cluster_13: 15.6, file_cluster_11: 15.682, file_cluster_0: 15.78
- **Magnitude:** 514.12 | **LOC:** 4665 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (53.1718%), Tech Debt (13.8632%)
**Top Internal Functions/Classes:**
  * `_getRGBABufferInternalSizedFormat` (Impact: 205.1)
  * `_initGLContext` (Impact: 182.3)
  * `enableEffect` (Impact: 150.0)
  * `constructor` (Impact: 134.9)
    * *Intent:* /** * Make the canvas XR Compatible for XR sessions */
  * `bindFramebuffer` (Impact: 111.6)
    * *Intent:* // Overcome a bug when using a texture to store morph targets on Mali-G72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 838`, `structural_boundaries: 334`, `args: 154`, `func_start: 151`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 2837`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 171`, `concurrency: 31`, `import: 40`
* *Defense:* `safety: 111`, `doc: 298`, `immutability_locks: 148`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.957
  * `Choke Point (Betweenness):` 0.000772 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` abstractEngine, IDrawContext, textureCreationOptions, performanceMonitor, ICanvas, abstractEngine.functions, renderTargetTexture, webGLHardwareTexture...
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `packages/tools/playground/public/scenes/Alien/Alien.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/BoomBox/BoomBox.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Box/Box.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Box/Box_extras.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/BrainStem/BrainStem0.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Buggy/glTF-Draco/0.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Buggy/glTF/Buggy0.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Elf/Elf.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Elf/Elf_allAnimations.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Elf/Elf_die.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/playground/public/scenes/Elf/Elf_run.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dev/core/src/Engines/webgpuEngine.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.971 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.554 IQR)
- **Top Global Matches:** file_cluster_13: 15.971, file_cluster_11: 16.178, file_cluster_4: 16.205
- **Magnitude:** 495.67 | **LOC:** 4190 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (54.3216%), Tech Debt (93.214%)
**Top Internal Functions/Classes:**
  * `createTexture` (Impact: 973.1)
  * `continuationCallback` (Impact: 648.1)
  * `initAsync` (Impact: 620.5)
  * `_startRenderTargetRenderPass` (Impact: 212.0)
  * `bindFramebuffer` (Impact: 175.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 443`, `structural_boundaries: 222`, `args: 121`, `func_start: 106`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 1204`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 18`
* *Architecture:* `api: 128`, `concurrency: 83`, `import: 66`
* *Defense:* `safety: 115`, `doc: 238`, `immutability_locks: 116`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.004134 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 65):` engine.renderTarget, engine.renderTargetTexture, baseTexture, iShaderProcessor, math.like, math, shaderLanguage, alphaCullingState...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Meshes/mesh.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.938 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.952 IQR)
- **Top Global Matches:** file_cluster_0: 14.938, file_cluster_13: 15.141, file_cluster_11: 15.186
- **Magnitude:** 490.5 | **LOC:** 5919 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (52.8098%), Tech Debt (38.0226%)
**Top Internal Functions/Classes:**
  * `_draw` (Impact: 600.0)
    * *Intent:* /** * Returns the registered LOD mesh distant from the parameter `camera` position if any, else retu...
  * `Parse` (Impact: 253.1)
  * `_MergeMeshesCoroutine` (Impact: 124.8)
  * `increaseVertices` (Impact: 115.4)
  * `_copySource` (Impact: 97.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 965`, `structural_boundaries: 291`, `args: 169`, `func_start: 155`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 1826`, `dead_code: 3`, `planned_debt: 4`, `duplicate_logic: 18`
* *Architecture:* `io: 50`, `api: 267`, `concurrency: 80`, `import: 43`
* *Defense:* `safety: 165`, `doc: 565`, `immutability_locks: 273`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.615
  * `Choke Point (Betweenness):` 0.003433 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` capsuleBuilder, tags, physicsImpostor, camera, sceneComponent, tools, transformNode, math.color...
  * `Imported By (In-Degree: 247):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Maths/math.vector.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.521 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.413 IQR)
- **Top Global Matches:** file_cluster_16: 14.521, file_cluster_2: 14.57, file_cluster_13: 14.766
- **Magnitude:** 456.36 | **LOC:** 8881 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.9542%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `ProjectOnTriangleToRef` (Impact: 297.6)
  * `NormalizeToRef` (Impact: 224.1)
    * *Intent:* /** * Normalize the current Vector with the given input length. * Please note that this is an in pla...
  * `decompose` (Impact: 65.0)
    * *Intent:* /** * Negate this vector in place * @returns this */
  * `equals` (Impact: 45.6)
    * *Intent:* /** * Adds the given coordinates to the current Vector4 * @param x defines the x coordinate of the o...
  * `PerspectiveFovRHToRef` (Impact: 36.5)
    * *Intent:* /** * Updates the current quaternion with the given float coordinates * Example Playground https://p...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 692`, `args: 523`, `func_start: 523`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1436`, `duplicate_logic: 325`
* *Architecture:* `api: 630`, `import: 13`
* *Defense:* `safety: 10`, `doc: 1792`, `immutability_locks: 475`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` typeStore, tensor, math.scalar.functions, math.plane, thinMath.matrix.functions, math.viewport, math.like, arrayTools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tools/viewer/src/viewer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.966 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.695 IQR)
- **Top Global Matches:** file_cluster_4: 15.966, file_cluster_13: 15.987, file_cluster_11: 16.142
- **Magnitude:** 401.99 | **LOC:** 3280 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (49.872%), Tech Debt (99.906%)
**Top Internal Functions/Classes:**
  * `_shouldRender` (Impact: 481.9)
  * `_loadModel` (Impact: 474.4)
    * *Intent:* /**
  * `_updateShadowMap` (Impact: 245.0)
  * `reject` (Impact: 119.2)
    * *Intent:* // Detect SPZ files and set the appropriate plugin extension and options.
  * `_reframeCameraFromBounds` (Impact: 84.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 292`, `args: 193`, `func_start: 146`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1304`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 40`
* *Architecture:* `api: 95`, `concurrency: 303`, `import: 59`
* *Defense:* `safety: 193`, `doc: 146`, `immutability_locks: 197`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` constants, hdrCubeTexture, math.vector, pointerEvents, hemisphericLight, discBuilder, engine.multiRender, sceneLoader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dev/core/src/Materials/PBR/pbrBaseMaterial.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.996 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.438 IQR)
- **Top Global Matches:** file_cluster_13: 14.996, file_cluster_11: 15.247, file_cluster_8: 15.353
- **Magnitude:** 366.6 | **LOC:** 2535 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (52.7079%), Tech Debt (92.9522%)
**Top Internal Functions/Classes:**
  * `bindForSubMesh` (Impact: 231.6)
  * `_prepareDefines` (Impact: 221.9)
  * `isReadyForSubMesh` (Impact: 174.3)
  * `BindVertexPullingUniforms` (Impact: 158.0)
  * `PrepareDefinesForOIT` (Impact: 151.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 152`, `args: 92`, `func_start: 88`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1657`, `dead_code: 1`, `duplicate_logic: 32`
* *Architecture:* `api: 296`, `concurrency: 30`, `import: 44`
* *Defense:* `safety: 34`, `doc: 147`, `immutability_locks: 60`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.51
  * `Choke Point (Betweenness):` 0.001014 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` shaderLanguage, baseTexture.polynomial, abstractMesh, mesh, vertexPullingHelper.functions, subMesh, scene, baseTexture...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Particles/thinParticleSystem.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.609 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.019 IQR)
- **Top Global Matches:** file_cluster_13: 15.609, file_cluster_4: 15.832, file_cluster_11: 15.834
- **Magnitude:** 355.04 | **LOC:** 2435 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (52.2419%), Tech Debt (96.3906%)
**Top Internal Functions/Classes:**
  * `_render` (Impact: 85.1)
    * *Intent:* /** * Fill the uniforms, attributes and samplers arrays according to the current settings of the par...
  * `animate` (Impact: 66.7)
  * `constructor` (Impact: 64.5)
    * *Intent:* /** * Observable that will be called just before the particles are drawn
  * `_appendParticleVertex` (Impact: 62.1)
  * `start` (Impact: 52.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 174`, `args: 166`, `func_start: 151`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 2181`, `duplicate_logic: 37`
* *Architecture:* `api: 162`, `concurrency: 64`, `import: 34`
* *Defense:* `safety: 43`, `doc: 228`, `immutability_locks: 61`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.862
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` particles.fragment, materialHelper.functions, math.color, clipPlaneMaterialHelper, scene, executionQueue, constants, rawTexture...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Lights/Shadows/shadowGenerator.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.003 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.182 IQR)
- **Top Global Matches:** file_cluster_13: 15.003, file_cluster_11: 15.256, file_cluster_4: 15.266
- **Magnitude:** 307.88 | **LOC:** 2326 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (53.4028%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `dispose` (Impact: 488.8)
    * *Intent:* /** * Determine whether the shadow generator is ready or not (mainly all effects and related post pr...
  * `isReady` (Impact: 138.8)
  * `_renderSubMeshForShadowMap` (Impact: 89.3)
  * `Parse` (Impact: 82.9)
  * `_initializeShadowMap` (Impact: 72.9)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 157`, `args: 120`, `func_start: 109`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1412`, `planned_debt: 1`, `duplicate_logic: 50`
* *Architecture:* `api: 89`, `concurrency: 51`, `import: 38`
* *Defense:* `safety: 39`, `doc: 145`, `immutability_locks: 108`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.431
  * `Choke Point (Betweenness):` 0.000242 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` devTools, depthBoxBlur.fragment, abstractMesh, mesh, subMesh, scene, baseTexture, effectFallbacks...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/scene.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.525 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.14 IQR)
- **Top Global Matches:** file_cluster_13: 15.525, file_cluster_11: 15.854, file_cluster_4: 15.894
- **Magnitude:** 297.65 | **LOC:** 6733 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (49.1093%), Tech Debt (47.3112%)
**Top Internal Functions/Classes:**
  * `dispose` (Impact: 573.8)
    * *Intent:* /**
  * `isReady` (Impact: 147.0)
    * *Intent:* /** * All of the transform nodes added to this scene * In the context of a Scene, it is not supposed...
  * `_checkIntersections` (Impact: 121.8)
  * `_renderForCamera` (Impact: 105.8)
    * *Intent:* // Return the non-offset position
  * `_evaluateActiveMeshes` (Impact: 92.6)
    * *Intent:* /** * This Observable will be triggered after rendering each renderingGroup of each rendered camera.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 324`, `args: 150`, `func_start: 125`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1118`, `dead_code: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 177`, `concurrency: 73`, `import: 83`
* *Defense:* `safety: 53`, `doc: 291`, `immutability_locks: 77`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.939
  * `Choke Point (Betweenness):` 0.027586 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 68):` ray.core, frameGraph, stringDictionary, collider, performanceViewerCollector, texture, tools, transformNode...
  * `Imported By (In-Degree: 653):` (Excluded from Brief to save tokens)

### `packages/dev/core/src/Materials/standardMaterial.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.557 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.583 IQR)
- **Top Global Matches:** file_cluster_13: 14.557, file_cluster_0: 14.627, file_cluster_11: 14.799
- **Magnitude:** 288.33 | **LOC:** 2017 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (52.3586%), Tech Debt (99.2045%)
**Top Internal Functions/Classes:**
  * `isReadyForSubMesh` (Impact: 299.6)
  * `bindForSubMesh` (Impact: 220.2)
  * `BindVertexPullingUniforms` (Impact: 142.8)
  * `PrepareDefinesForAttributes` (Impact: 130.2)
  * `PrepareDefinesForOIT` (Impact: 115.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 136`, `args: 90`, `func_start: 86`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1220`, `duplicate_logic: 40`
* *Architecture:* `api: 239`, `concurrency: 20`, `import: 40`
* *Defense:* `safety: 16`, `doc: 112`, `immutability_locks: 33`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.806
  * `Choke Point (Betweenness):` 0.000651 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` pushMaterial, materialDefines, math.color, renderTargetTexture, effectFallbacks, scene, baseTexture, mesh...
  * `Imported By (In-Degree: 71):` (Excluded from Brief to save tokens)

### `packages/dev/proceduralTextures/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.995 IQR)
- **Top Global Matches:** file_cluster_8: 11.995, file_cluster_11: 12.383, file_cluster_17: 12.417
- **Magnitude:** 284.4 | **LOC:** 436 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.7024%), Tech Debt (98.9013%)
**Top Internal Functions/Classes:**
  * `addPToptions` (Impact: 36.7)
  * `addPToptions` (Impact: 32.8)
  * `resetPTOptions` (Impact: 27.2)
  * `addFloatSubOption` (Impact: 7.9)
  * `addFloatSubOption` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 60`, `args: 19`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 137`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 2`
* *Defense:* `safety: 11`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BabylonLoader.js, addNormalMapPT.js, addWoodPT.js, addCloudPT.js, index.js, addRoadPT.js, dat.gui.min.js, addGrassPT.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dev/core/src/Rendering/geometryBufferRenderer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.58 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.256 IQR)
- **Top Global Matches:** file_cluster_13: 14.58, file_cluster_0: 14.727, file_cluster_4: 14.73
- **Magnitude:** 268.6 | **LOC:** 1400 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (59.5467%), Tech Debt (65.5805%)
**Top Internal Functions/Classes:**
  * `_linkPrePassRenderer` (Impact: 566.9)
    * *Intent:* /** * Constant used to retrieve the velocity texture index in the G-Buffer textures array
  * `AddClipPlaneUniforms` (Impact: 417.1)
  * `_createRenderTargets` (Impact: 247.3)
  * `renderSubMesh` (Impact: 229.8)
  * `isReady` (Impact: 178.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 81`, `args: 40`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 791`, `dead_code: 11`, `duplicate_logic: 12`
* *Architecture:* `io: 2`, `api: 36`, `concurrency: 30`, `import: 26`
* *Defense:* `safety: 21`, `doc: 42`, `immutability_locks: 62`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 0.000231 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` geometry.fragment, materialHelper.functions, math.color, clipPlaneMaterialHelper, scene, subMesh, texture, geometry.vertex...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/dev/core/src/Materials/PBR/pbrBaseSimpleMaterial.ts` (TYPESCRIPT) | Magnitude: 5.02 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, decorators: 27, api: 19, doc: 19
- `packages/tools/testsMemoryLeaks/test/unit/testFramework.ts` (TYPESCRIPT) | Magnitude: 2.6 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 12, branch: 9, safety_bypasses: 8
- `scripts/updateVersion.js` (JAVASCRIPT) | Magnitude: 110.96 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 127, immutability_locks: 40, branch: 35, io: 26
- `packages/dev/gui/src/3D/materials/mrdl/mrdlSliderThumbMaterial.ts` (TYPESCRIPT) | Magnitude: 51.43 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 449, state_mutation: 250, api: 97, doc: 79
- `packages/dev/gui/src/3D/materials/mrdl/mrdlSliderBarMaterial.ts` (TYPESCRIPT) | Magnitude: 51.84 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 450, state_mutation: 254, api: 97, doc: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/dev/core/src/Cameras/cameraInputsManager.ts` (TYPESCRIPT) | Magnitude: 24.35 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 149, state_mutation: 128, doc: 42, structural_boundaries: 36
- `packages/dev/inspector-v2/src/instrumentation/propertyInstrumentation.ts` (TYPESCRIPT) | Magnitude: 15.1 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 36, branch: 33, structural_boundaries: 30
- `packages/tools/babylonServer/public/uiControls/babylon.uiControls.max.js` (JAVASCRIPT) | Magnitude: 1.67 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 254, branch: 237, indent_spaces: 234, structural_boundaries: 176
- `packages/dev/core/src/XR/native/nativeXRFrame.ts` (TYPESCRIPT) | Magnitude: 10.76 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, state_mutation: 41, api: 21, structural_boundaries: 18
- `packages/tools/babylonServer/public/recast.js` (JAVASCRIPT) | Magnitude: 3.61 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1722, state_mutation: 1416, structural_boundaries: 860, branch: 490

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/dev/core/src/Materials/uniformBufferEffectCommonAccessor.ts` (TYPESCRIPT) | Magnitude: 9.01 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 55, reflection_metaprogramming: 40, structural_boundaries: 33
- `packages/dev/smartFilters/src/utils/buildTools/buildToolsLogger.ts` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.249 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, safety: 5, doc: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/dev/sharedUiComponents/src/nodeGraphSystem/graphCanvas.tsx` (TYPESCRIPT) | Magnitude: 137.91 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 663, state_mutation: 565, branch: 154, structural_boundaries: 121
- `packages/tools/devHost/src/lottie/main.ts` (TYPESCRIPT) | Magnitude: 4.77 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 36, concurrency: 17, immutability_locks: 17, structural_boundaries: 13
- `packages/tools/smartFiltersEditorControl/src/graphSystem/properties/genericNodePropertyComponent.tsx` (TYPESCRIPT) | Magnitude: 19.77 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 181, state_mutation: 81, branch: 41, structural_boundaries: 41
- `packages/dev/core/src/FrameGraph/frameGraphRenderTarget.ts` (TYPESCRIPT) | Magnitude: 16.33 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 86, indent_spaces: 74, branch: 28, structural_boundaries: 14
- `packages/dev/sharedUiComponents/src/tabs/propertyGrids/gui/scrollViewerPropertyGridComponent.tsx` (TYPESCRIPT) | Magnitude: 2.71 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 64, ui_framework: 26, structural_boundaries: 18, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/dev/core/src/Misc/PerformanceViewer/performanceViewerCollectionStrategies.ts` (TYPESCRIPT) | Magnitude: 27.52 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 369, structural_boundaries: 151, args: 112, closures: 84
- `packages/dev/core/src/Offline/IOfflineProvider.ts` (TYPESCRIPT) | Magnitude: 11.05 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, safety: 8, structural_boundaries: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/dev/core/src/Misc/lazy.ts` (TYPESCRIPT) | Magnitude: 2.67 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 16, indent_spaces: 12, structural_boundaries: 5, api: 4
- `packages/dev/inspector-v2/src/instrumentation/functionInstrumentation.ts` (TYPESCRIPT) | Magnitude: 9.61 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 30, branch: 24, structural_boundaries: 22
- `packages/dev/core/src/Maths/math.plane.ts` (TYPESCRIPT) | Magnitude: 14.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 102, state_mutation: 72, doc: 58, api: 25
- `packages/dev/inspector-v2/src/components/properties/boundProperty.tsx` (TYPESCRIPT) | Magnitude: 2.47 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 42, generics: 26, branch: 20
- `packages/dev/core/src/Misc/timer.ts` (TYPESCRIPT) | Magnitude: 22.97 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, state_mutation: 123, branch: 36, doc: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/dev/inspector-v2/src/components/performanceViewer/performanceSidebar.tsx` (TYPESCRIPT) | Magnitude: 12.23 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 40, ui_framework: 29, branch: 28
- `packages/dev/inspector/src/components/actionTabs/tabsComponent.tsx` (TYPESCRIPT) | Magnitude: 3.07 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, ui_framework: 13, state_mutation: 11
- `packages/dev/inspector/src/components/actionTabs/tabs/propertyGrids/animations/curveEditor/graph/graphComponent.tsx` (TYPESCRIPT) | Magnitude: 130.74 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1013, state_mutation: 781, branch: 204, structural_boundaries: 126
- `packages/dev/inspector-v2/src/modularity/serviceContainer.ts` (TYPESCRIPT) | Magnitude: 27.27 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 121, concurrency: 44, branch: 34
- `packages/tools/flowGraphEditor/src/sceneContext.ts` (TYPESCRIPT) | Magnitude: 26.45 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, state_mutation: 126, structural_boundaries: 63, args: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/dev/inspector-v2/src/extensions/quickCreate/spriteManagers.tsx` (TYPESCRIPT) | Magnitude: 0.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 20, ui_framework: 12, args: 7
- `packages/dev/sharedUiComponents/src/components/reactGraphSystem/GraphContainer.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, ui_framework: 4, doc: 3, api: 2
- `packages/dev/sharedUiComponents/src/lines/colorPickerComponent.tsx` (TYPESCRIPT) | Magnitude: 13.71 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 76, ui_framework: 26, structural_boundaries: 22
- `packages/dev/inspector/src/components/actionTabs/tabs/propertyGrids/postProcesses/ssaoRenderingPipelinePropertyGridComponent.tsx` (TYPESCRIPT) | Magnitude: 2.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, ui_framework: 24, structural_boundaries: 19, state_mutation: 15
- `packages/dev/inspector-v2/src/components/properties/particles/sizeProperties.tsx` (TYPESCRIPT) | Magnitude: 3.99 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 100, sec_high_risk_execution: 39, structural_boundaries: 26, ui_framework: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/tools/tests/test/playwright/interaction.test.ts` (TYPESCRIPT) | Magnitude: 9.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, concurrency: 78, structural_boundaries: 77, args: 17
- `packages/dev/core/src/PostProcesses/thinPassPostProcess.ts` (TYPESCRIPT) | Magnitude: 11.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 34, branch: 19, concurrency: 18
- `packages/dev/inspector-v2/src/misc/observableCollection.ts` (TYPESCRIPT) | Magnitude: 3.55 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 13, structural_boundaries: 10, concurrency: 7
- `packages/tools/smartFiltersEditorControl/src/helpers/observableProperty.ts` (TYPESCRIPT) | Magnitude: 5.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 17, concurrency: 14, structural_boundaries: 10
- `packages/dev/core/src/FrameGraph/Node/nodeRenderGraphBuildState.ts` (TYPESCRIPT) | Magnitude: 3.01 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 9, doc: 7, concurrency: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/dev/core/src/Animations/animationEvent.ts` (TYPESCRIPT) | Magnitude: 1.7 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 9, api: 8, structural_boundaries: 4
- `packages/dev/core/src/Maths/math.polar.ts` (TYPESCRIPT) | Magnitude: 32.11 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 307, doc: 215, state_mutation: 105, api: 73
- `packages/dev/core/src/FlowGraph/CustomTypes/flowGraphInteger.ts` (TYPESCRIPT) | Magnitude: 4.64 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, doc: 25, api: 17, structural_boundaries: 12
- `packages/dev/core/src/Maths/math.scalar.functions.ts` (TYPESCRIPT) | Magnitude: 16.36 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 113, indent_spaces: 95, structural_boundaries: 54, api: 43
- `packages/dev/core/src/Maths/math.size.ts` (TYPESCRIPT) | Magnitude: 10.03 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, doc: 51, api: 32, state_mutation: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/dev/core/src/Misc/screenshotTools.ts` (TYPESCRIPT) | Magnitude: 46.19 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 463, doc: 110, branch: 107, structural_boundaries: 90
- `packages/dev/sharedUiComponents/src/nodeGraphSystem/interfaces/nodeContainer.ts` (TYPESCRIPT) | Magnitude: 1.83 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, import: 2, indent_spaces: 2, args: 1
- `packages/dev/core/src/Engines/WebGPU/Extensions/engine.debugging.ts` (TYPESCRIPT) | Magnitude: 26.11 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 199, indent_spaces: 70, branch: 39, safety: 30
- `packages/dev/core/src/Meshes/Builders/capsuleBuilder.ts` (TYPESCRIPT) | Magnitude: 8.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 177, state_mutation: 71, immutability_locks: 62, branch: 35
- `packages/dev/serializers/src/glTF/glTFFileExporter.ts` (TYPESCRIPT) | Magnitude: 1.61 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, indent_spaces: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/tools/babylonServer/src/loaders/index-dev.ts` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 26, branch: 16, safety_bypasses: 10, dead_code: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/dev/core/src/Engines/abstractEngine.ts` -> Churn: **98.5%** | Cog Load: 54.0098% | Debt: 90.6639%
- `packages/dev/core/src/Misc/tools.ts` -> Churn: **93.51%** | Cog Load: 40.804% | Debt: 99.9996%
- `packages/dev/core/src/Engines/webgpuEngine.ts` -> Churn: **77.58%** | Cog Load: 54.3216% | Debt: 93.214%
- `packages/tools/viewer/src/viewer.ts` -> Churn: **77.58%** | Cog Load: 49.872% | Debt: 99.906%
- `packages/tools/playground/src/tools/monaco/monacoManager.ts` -> Churn: **74.49%** | Cog Load: 89.9563% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/dev/core/src/Meshes/GaussianSplatting/gaussianSplattingMeshBase.ts` -> **Jesse Foltz** (100.0% isolated ownership) | Magnitude: 222.01
- `packages/dev/core/src/Materials/material.ts` -> **Ryan Tremblay** (100.0% isolated ownership) | Magnitude: 195.27
- `packages/dev/core/src/Cameras/arcRotateCamera.ts` -> **Ryan Tremblay** (100.0% isolated ownership) | Magnitude: 183.9
- `packages/dev/inspector/src/components/actionTabs/tabs/propertyGrids/animations/curveEditor/graph/keyPoint.tsx` -> **Ryan Tremblay** (100.0% isolated ownership) | Magnitude: 156.18
- `packages/dev/core/src/FlowGraph/Blocks/Data/Math/flowGraphMathBlocks.ts` -> **Ryan Tremblay** (100.0% isolated ownership) | Magnitude: 154.11

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/dev/core/src/scene.ts` -> **Severity: 2.759** (Bridge: 0.0276 * Flux: 100.0%)
- `packages/dev/core/src/Materials/Node/nodeMaterial.ts` -> **Severity: 0.861** (Bridge: 0.0086 * Flux: 100.0%)
- `packages/dev/core/src/Engines/abstractEngine.ts` -> **Severity: 0.688** (Bridge: 0.0069 * Flux: 100.0%)
- `packages/dev/core/src/Audio/sound.ts` -> **Severity: 0.601** (Bridge: 0.006 * Flux: 100.0%)
- `packages/dev/core/src/PostProcesses/postProcess.ts` -> **Severity: 0.484** (Bridge: 0.0048 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/dev/core/src/Misc/observable.ts` -> **Severity: 1364.854** (Blast Radius: 24.747 * Doc Risk: 55.1523%)
- `packages/dev/core/src/Misc/typeStore.ts` -> **Severity: 1277.875** (Blast Radius: 13.948 * Doc Risk: 91.6171%)
- `packages/dev/core/src/Meshes/abstractMesh.ts` -> **Severity: 931.381** (Blast Radius: 9.899 * Doc Risk: 94.0884%)
- `packages/dev/core/src/Misc/logger.ts` -> **Severity: 908.426** (Blast Radius: 11.231 * Doc Risk: 80.8856%)
- `packages/dev/core/src/Materials/Textures/internalTexture.ts` -> **Severity: 662.6** (Blast Radius: 6.626 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
