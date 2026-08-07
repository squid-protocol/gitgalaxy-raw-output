# ARCHITECTURAL_BRIEF: pixijs
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/pixijs` |
| **Timestamp** | `2026-08-07T04:17:04.757926+00:00` |
| **Scan Duration** | `8.52s` |
| **Git Branch** | `dev` |
| **Git Commit** | `627a356cf297c027019195a7a27f1bf4b46c4767` |
| **Git Remote** | `https://github.com/pixijs/pixijs.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1444 malicious artifacts.

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
| Total Artifacts | 3149 |
| Analyzed Artifacts (Scanned) | 1530 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1619 |
| Total LOC | 104858 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 48.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5605 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2191 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5064 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 57 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1389 | 100308 | 90.8% |
| MARKDOWN | 53 | 0 | 3.5% |
| GLSL | 41 | 888 | 2.7% |
| JSON | 19 | 645 | 1.2% |
| JAVASCRIPT | 14 | 2327 | 0.9% |
| PLAINTEXT | 7 | 1 | 0.5% |
| XML | 4 | 1 | 0.3% |
| HTML | 2 | 21 | 0.1% |
| CSS | 1 | 667 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.498`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 895 | 58.5% |
| file_cluster_13 | 465 | 30.4% |
| file_cluster_4 | 49 | 3.2% |
| file_cluster_0 | 24 | 1.6% |
| file_cluster_16 | 24 | 1.6% |
| file_cluster_17 | 7 | 0.5% |
| file_cluster_11 | 2 | 0.1% |
| Unknown | 1 | 0.1% |
| file_cluster_2 | 1 | 0.1% |
| file_cluster_1 | 1 | 0.1% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 59 | 3.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1619*

**Composition by Extension & Reason:**
- `.png`: 1438x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 17x Excluded (Explicitly Denied Extension: '.jpg')
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wgsl`: 10x Unsupported Format (.wgsl), 5x Excluded (Unsupported Extension: '.wgsl')
- `.dds`: 13x Excluded (Binary Format Detected), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 32765 LOC exceeds safe regex boundaries), 1x Excluded (Static Asset Blob without Intent: 2084 LOC)
- `.ts`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Saturation: Line 88 exceeds 500 chars)
- `.fnt`: 10x Unsupported Format (.fnt), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ktx`: 9x Excluded (Binary Format Detected), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.webp`: 9x Excluded (Explicitly Denied Extension: '.webp')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 7x Excluded (Explicitly Denied Extension: '.ttf')
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.8 | 15.2 | 6.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 34.3 | 37.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 20.0 | 4.3 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 28.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 37.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.2 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 67.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 15.9 | 0.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/utils/__tests__/path.test.ts` (Hits: 401)
- `src/utils/path.ts` (Hits: 121)
- `src/scene/graphics/shared/__tests__/SVGParser.test.ts` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **scene.md** (`src/scene/__docs__/scene.md`) — 373 inbound connections
2. **assets.md** (`src/assets/__docs__/assets.md`) — 201 inbound connections
3. **Extensions.ts** (`src/extensions/Extensions.ts`) — 193 inbound connections
4. **rendering.md** (`src/rendering/__docs__/rendering.md`) — 105 inbound connections
5. **Container.ts** (`src/scene/container/Container.ts`) — 105 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/rendering/index.ts`) — 236 outbound dependencies
2. **index.ts** (`src/scene/index.ts`) — 192 outbound dependencies
3. **index.ts** (`src/filters/index.ts`) — 40 outbound dependencies
4. **index.ts** (`src/assets/index.ts`) — 37 outbound dependencies
5. **Container.ts** (`src/scene/container/Container.ts`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `isDataUrl` (@ `src/utils/path.ts`) -> Impact: **245.0** | LOC: 465
- `extend` (@ `src/color/Color.ts`) -> Impact: **166.1** | LOC: 521
- `wordWrapTaggedLines` (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **157.6** | LOC: 268
- `getBitmapTextLayout` (@ `src/scene/text-bitmap/utils/getBitmapTextLayout.ts`) -> Impact: **157.3** | LOC: 284
  * *Intent:* // / spaces: number
- `pruneFn` (@ `src/events/EventBoundary.ts`) -> Impact: **148.1** | LOC: 433
- `buildLine` (@ `src/scene/graphics/shared/buildCommands/buildLine.ts`) -> Impact: **143.7** | LOC: 385
- `execute` (@ `src/scene/graphics/canvas/CanvasGraphicsAdaptor.ts`) -> Impact: **138.6** | LOC: 244
- `getUncompressedTextureFormat` (@ `src/compressed-textures/dds/parseDDS.ts`) -> Impact: **119.8** | LOC: 75
- `recursive` (@ `src/scene/graphics/shared/buildCommands/buildAdaptiveBezier.ts`) -> Impact: **116.7** | LOC: 187
- `describe` (@ `src/rendering/renderers/shared/__tests__/GCSystem.test.ts`) -> Impact: **96.1** | LOC: 813

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 5 | 5049.44 | 2.12% | 0.0% |
| `transcoders/basis` | 1 | 2175.78 | 99.39% | 99.87% |
| `scripts/plugins` | 8 | 610.06 | 17.53% | 50.62% |
| `examples` | 87 | 230.39 | 35.62% | 0.0% |
| `src/scene/container/__tests__` | 32 | 207.12 | 9.3% | 3.12% |
| `.stackblitz/bunny-mark/src` | 2 | 197.52 | 71.34% | 35.07% |
| `src/events` | 14 | 160.3 | 16.09% | 14.34% |
| `src/scene/container/container-mixins` | 11 | 155.03 | 33.3% | 94.04% |
| `src/scene/graphics/shared` | 7 | 139.84 | 32.46% | 51.74% |
| `src/rendering/renderers/shared/texture/sources` | 8 | 128.51 | 23.89% | 19.85% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/build-status.mjs` -> **100.0%** Exposure
- `src/assets/utils/createStringVariations.ts` -> **100.0%** Exposure
- `src/filters/defaults/alpha/AlphaFilter.ts` -> **100.0%** Exposure
- `src/filters/defaults/blur/BlurFilter.ts` -> **100.0%** Exposure
- `src/rendering/high-shader/compiler/utils/compileInputs.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.stackblitz/bunny-mark/src/Bunny.js` -> **100.0%** Exposure
- `transcoders/basis/basis_transcoder.js` -> **100.0%** Exposure
- `scripts/utils/autoGenerateUnsafeEvalFunctions.ts` -> **100.0%** Exposure
- `src/accessibility/AccessibilitySystem.ts` -> **100.0%** Exposure
- `src/app/ResizePlugin.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/scene/text/canvas/__tests__/CanvasTextMetrics.test.ts` -> **1** Orphaned Functions | **108** Duplicates
- `src/scene/text/__tests__/TextMetrics.test.ts` -> **1** Orphaned Functions | **84** Duplicates
- `src/scene/sprite-animated/__tests__/AnimatedSprite.test.ts` -> **0** Orphaned Functions | **81** Duplicates
- `src/scene/container/__tests__/Container.test.ts` -> **0** Orphaned Functions | **78** Duplicates
- `src/rendering/renderers/shared/__tests__/GCSystem.test.ts` -> **1** Orphaned Functions | **67** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/scene/text/canvas/CanvasTextGenerator.ts`** -> AI Confidence: **99.48%**
2. **`src/scene/graphics/canvas/CanvasGraphicsAdaptor.ts`** -> AI Confidence: **99.39%**
3. **`src/scene/text-bitmap/DynamicBitmapFont.ts`** -> AI Confidence: **99.35%**
4. **`src/rendering/renderers/shared/shader/utils/uniformParsers.ts`** -> AI Confidence: **99.34%**
5. **`src/scene/graphics/shared/svg/parseSVGPath.ts`** -> AI Confidence: **99.32%**
6. **`src/scene/text-bitmap/utils/getBitmapTextLayout.ts`** -> AI Confidence: **99.32%**
7. **`src/accessibility/AccessibilitySystem.ts`** -> AI Confidence: **99.31%**
8. **`src/assets/loader/Loader.ts`** -> AI Confidence: **99.31%**
9. **`src/assets/loader/parsers/textures/loadVideoTextures.ts`** -> AI Confidence: **99.31%**
10. **`src/assets/resolver/Resolver.ts`** -> AI Confidence: **99.31%**
11. **`src/events/EventBoundary.ts`** -> AI Confidence: **99.31%**
12. **`src/events/EventSystem.ts`** -> AI Confidence: **99.31%**
13. **`src/filters/defaults/blur/BlurFilter.ts`** -> AI Confidence: **99.31%**
14. **`src/prepare/PrepareUpload.ts`** -> AI Confidence: **99.31%**
15. **`src/rendering/batcher/canvas/CanvasBatchAdaptor.ts`** -> AI Confidence: **99.31%**
16. **`src/rendering/batcher/shared/Batcher.ts`** -> AI Confidence: **99.31%**
17. **`src/rendering/mask/stencil/CanvasStencilMaskPipe.ts`** -> AI Confidence: **99.31%**
18. **`src/rendering/renderers/canvas/CanvasFilterSystem.ts`** -> AI Confidence: **99.31%**
19. **`src/rendering/renderers/gl/context/GlContextSystem.ts`** -> AI Confidence: **99.31%**
20. **`src/rendering/renderers/gl/geometry/GlGeometrySystem.ts`** -> AI Confidence: **99.31%**
21. **`src/rendering/renderers/gl/renderTarget/GlRenderTargetAdaptor.ts`** -> AI Confidence: **99.31%**
22. **`src/rendering/renderers/gl/state/GlStateSystem.ts`** -> AI Confidence: **99.31%**
23. **`src/rendering/renderers/gpu/GpuEncoderSystem.ts`** -> AI Confidence: **99.31%**
24. **`src/rendering/renderers/gpu/renderTarget/GpuRenderTargetAdaptor.ts`** -> AI Confidence: **99.31%**
25. **`src/rendering/renderers/shared/texture/Texture.ts`** -> AI Confidence: **99.31%**
26. **`src/rendering/renderers/shared/texture/sources/TextureSource.ts`** -> AI Confidence: **99.31%**
27. **`src/scene/container/RenderGroupSystem.ts`** -> AI Confidence: **99.31%**
28. **`src/scene/container/container-mixins/effectsMixin.ts`** -> AI Confidence: **99.31%**
29. **`src/scene/graphics/shared/Graphics.ts`** -> AI Confidence: **99.31%**
30. **`src/scene/graphics/shared/GraphicsContext.ts`** -> AI Confidence: **99.31%**
31. **`src/scene/graphics/shared/fill/FillGradient.ts`** -> AI Confidence: **99.31%**
32. **`src/scene/graphics/shared/path/GraphicsPath.ts`** -> AI Confidence: **99.31%**
33. **`src/scene/sprite-nine-slice/canvas/CanvasNineSliceSpritePipe.ts`** -> AI Confidence: **99.31%**
34. **`src/scene/text-bitmap/utils/bitmapTextSplit.ts`** -> AI Confidence: **99.31%**
35. **`src/scene/text/AbstractText.ts`** -> AI Confidence: **99.31%**
36. **`src/scene/text/TextStyle.ts`** -> AI Confidence: **99.31%**
37. **`src/scene/text/canvas/CanvasTextMetrics.ts`** -> AI Confidence: **99.31%**
38. **`src/scene/text/canvas/utils/getCanvasFillStyle.ts`** -> AI Confidence: **99.31%**
39. **`src/scene/text/utils/canvasTextSplit.ts`** -> AI Confidence: **99.31%**
40. **`src/unsafe-eval/shader/generateShaderSyncPolyfill.ts`** -> AI Confidence: **99.31%**
41. **`src/rendering/renderers/canvas/utils/mapCanvasBlendModesToPixi.ts`** -> AI Confidence: **99.29%**
42. **`src/rendering/renderers/gl/texture/utils/applyStyleParams.ts`** -> AI Confidence: **99.29%**
43. **`src/rendering/renderers/shared/buffer/utils/fastCopy.ts`** -> AI Confidence: **99.29%**
44. **`src/scene/container/utils/clearList.ts`** -> AI Confidence: **99.29%**
45. **`src/scene/graphics/shared/buildCommands/buildArc.ts`** -> AI Confidence: **99.29%**
46. **`src/scene/graphics/shared/buildCommands/buildLine.ts`** -> AI Confidence: **99.29%**
47. **`src/scene/sprite-nine-slice/NineSliceGeometry.ts`** -> AI Confidence: **99.29%**
48. **`src/scene/text-bitmap/utils/resolveCharacters.ts`** -> AI Confidence: **99.29%**
49. **`src/unsafe-eval/uniforms/uniformSyncFunctions.ts`** -> AI Confidence: **99.29%**
50. **`src/assets/loader/parsers/loadWebFont.ts`** -> AI Confidence: **99.24%**
51. **`src/filters/FilterSystem.ts`** -> AI Confidence: **99.24%**
52. **`src/gif/GifSprite.ts`** -> AI Confidence: **99.24%**
53. **`src/prepare/PrepareBase.ts`** -> AI Confidence: **99.24%**
54. **`src/prepare/PrepareQueue.ts`** -> AI Confidence: **99.24%**
55. **`src/rendering/renderers/canvas/renderTarget/CanvasRenderTargetAdaptor.ts`** -> AI Confidence: **99.24%**
56. **`src/rendering/renderers/shared/geometry/Geometry.ts`** -> AI Confidence: **99.24%**
57. **`src/rendering/renderers/shared/renderTarget/RenderTargetSystem.ts`** -> AI Confidence: **99.24%**
58. **`src/scene/particle-container/shared/ParticleContainer.ts`** -> AI Confidence: **99.24%**
59. **`src/scene/sprite-nine-slice/NineSliceSprite.ts`** -> AI Confidence: **99.24%**
60. **`src/scene/sprite-tiling/TilingSprite.ts`** -> AI Confidence: **99.24%**
61. **`src/scene/sprite-tiling/canvas/CanvasTilingSpritePipe.ts`** -> AI Confidence: **99.24%**
62. **`src/scene/sprite/Sprite.ts`** -> AI Confidence: **99.24%**
63. **`src/scene/text-html/HTMLTextPipe.ts`** -> AI Confidence: **99.24%**
64. **`src/scene/text/canvas/CanvasTextPipe.ts`** -> AI Confidence: **99.24%**
65. **`src/scene/text/shared/AbstractTextSystem.ts`** -> AI Confidence: **99.24%**
66. **`src/spritesheet/spritesheetAsset.ts`** -> AI Confidence: **99.24%**
67. **`src/events/FederatedEventTarget.ts`** -> AI Confidence: **99.23%**
68. **`src/rendering/batcher/shared/BatcherPipe.ts`** -> AI Confidence: **99.23%**
69. **`src/rendering/renderers/autoDetectRenderer.ts`** -> AI Confidence: **99.23%**
70. **`src/rendering/renderers/gl/buffer/GlBufferSystem.ts`** -> AI Confidence: **99.23%**
71. **`src/scene/container/container-mixins/measureMixin.ts`** -> AI Confidence: **99.23%**
72. **`src/scene/text/canvas/utils/measureTaggedText.ts`** -> AI Confidence: **99.23%**
73. **`src/utils/path.ts`** -> AI Confidence: **99.23%**
74. **`scripts/plugins/typedoc-plugin-llms-txt.mjs`** -> AI Confidence: **99.2%**
75. **`src/compressed-textures/dds/parseDDS.ts`** -> AI Confidence: **99.2%**
76. **`playground/src/app/App.tsx`** -> AI Confidence: **99.18%**
77. **`src/assets/Assets.ts`** -> AI Confidence: **99.18%**
78. **`src/culling/__tests__/Culler.test.ts`** -> AI Confidence: **99.18%**
79. **`src/filters/Filter.ts`** -> AI Confidence: **99.18%**
80. **`src/filters/FilterPipe.ts`** -> AI Confidence: **99.18%**
81. **`src/filters/defaults/color-matrix/ColorMatrixFilter.ts`** -> AI Confidence: **99.18%**
82. **`src/filters/defaults/displacement/DisplacementFilter.ts`** -> AI Confidence: **99.18%**
83. **`src/rendering/mask/alpha/AlphaMaskPipe.ts`** -> AI Confidence: **99.18%**
84. **`src/rendering/renderers/__tests__/BindGroup.test.ts`** -> AI Confidence: **99.18%**
85. **`src/rendering/renderers/__tests__/RenderTarget.test.ts`** -> AI Confidence: **99.18%**
86. **`src/rendering/renderers/gl/GlBackBufferSystem.ts`** -> AI Confidence: **99.18%**
87. **`src/rendering/renderers/gl/shader/GlUniformGroupSystem.ts`** -> AI Confidence: **99.18%**
88. **`src/rendering/renderers/gl/shader/program/generateProgram.ts`** -> AI Confidence: **99.18%**
89. **`src/rendering/renderers/gl/texture/GlTextureSystem.ts`** -> AI Confidence: **99.18%**
90. **`src/rendering/renderers/gpu/buffer/GpuBufferSystem.ts`** -> AI Confidence: **99.18%**
91. **`src/rendering/renderers/gpu/shader/GpuProgram.ts`** -> AI Confidence: **99.18%**
92. **`src/rendering/renderers/shared/instructions/RenderPipe.ts`** -> AI Confidence: **99.18%**
93. **`src/rendering/renderers/shared/renderTarget/GlobalUniformSystem.ts`** -> AI Confidence: **99.18%**
94. **`src/scene/container/RenderContainer.ts`** -> AI Confidence: **99.18%**
95. **`src/scene/container/__tests__/getLocalBounds.test.ts`** -> AI Confidence: **99.18%**
96. **`src/scene/graphics/shared/GraphicsPipe.ts`** -> AI Confidence: **99.18%**
97. **`src/scene/mesh/shared/BatchableMesh.ts`** -> AI Confidence: **99.18%**
98. **`src/scene/text-bitmap/BitmapFont.ts`** -> AI Confidence: **99.18%**
99. **`src/scene/text-html/HTMLTextSystem.ts`** -> AI Confidence: **99.18%**
100. **`tests/visual/tester.ts`** -> AI Confidence: **99.18%**
101. **`scripts/plugins/eslint-require-export.mjs`** -> AI Confidence: **99.17%**
102. **`src/filters/blend-modes/hls/GLhls.ts`** -> AI Confidence: **99.17%**
103. **`src/maths/misc/squaredDistanceToLineSegment.ts`** -> AI Confidence: **99.17%**
104. **`src/rendering/high-shader/compiler/utils/addBits.ts`** -> AI Confidence: **99.17%**
105. **`src/rendering/renderers/gl/texture/utils/unpremultiplyAlpha.ts`** -> AI Confidence: **99.17%**
106. **`src/scene/graphics/shared/path/roundShape.ts`** -> AI Confidence: **99.17%**
107. **`src/scene/graphics/shared/utils/getMaxMiterRatio.ts`** -> AI Confidence: **99.17%**
108. **`src/scene/mesh-plane/PlaneGeometry.ts`** -> AI Confidence: **99.17%**
109. **`src/scene/particle-container/shared/utils/createIndicesForQuads.ts`** -> AI Confidence: **99.17%**
110. **`src/scene/text-bitmap/asset/bitmapFontTextParser.ts`** -> AI Confidence: **99.17%**
111. **`src/scene/text-bitmap/asset/bitmapFontXMLParser.ts`** -> AI Confidence: **99.17%**
112. **`src/assets/loader/parsers/textures/loadSVG.ts`** -> AI Confidence: **99.16%**
113. **`src/assets/loader/parsers/textures/loadTextures.ts`** -> AI Confidence: **99.16%**
114. **`src/filters/defaults/blur/BlurFilterPass.ts`** -> AI Confidence: **99.16%**
115. **`src/filters/index.ts`** -> AI Confidence: **99.16%**
116. **`src/rendering/mask/stencil/StencilMaskPipe.ts`** -> AI Confidence: **99.16%**
117. **`src/rendering/renderers/gpu/BindGroupSystem.ts`** -> AI Confidence: **99.16%**
118. **`src/rendering/renderers/gpu/pipeline/PipelineSystem.ts`** -> AI Confidence: **99.16%**
119. **`src/rendering/renderers/gpu/texture/GpuTextureSystem.ts`** -> AI Confidence: **99.16%**
120. **`src/rendering/renderers/shared/blendModes/BlendModePipe.ts`** -> AI Confidence: **99.16%**
121. **`src/rendering/renderers/shared/extract/ExtractSystem.ts`** -> AI Confidence: **99.16%**
122. **`src/rendering/renderers/shared/extract/GenerateTextureSystem.ts`** -> AI Confidence: **99.16%**
123. **`src/rendering/renderers/shared/view/ViewSystem.ts`** -> AI Confidence: **99.16%**
124. **`src/scene/container/Container.ts`** -> AI Confidence: **99.16%**
125. **`src/scene/container/RenderGroup.ts`** -> AI Confidence: **99.16%**
126. **`src/scene/graphics/shared/GraphicsContextSystem.ts`** -> AI Confidence: **99.16%**
127. **`src/scene/graphics/shared/path/ShapePath.ts`** -> AI Confidence: **99.16%**
128. **`src/scene/graphics/shared/utils/buildContextBatches.ts`** -> AI Confidence: **99.16%**
129. **`src/scene/mesh/shared/Mesh.ts`** -> AI Confidence: **99.16%**
130. **`src/scene/mesh/shared/MeshPipe.ts`** -> AI Confidence: **99.16%**
131. **`src/scene/sprite-tiling/TilingSpritePipe.ts`** -> AI Confidence: **99.16%**
132. **`src/scene/text-bitmap/AbstractBitmapTextPipe.ts`** -> AI Confidence: **99.16%**
133. **`src/assets/resolver/__tests__/Resolver.test.ts`** -> AI Confidence: **99.15%**
134. **`src/compressed-textures/ktx2/worker/ktx.worker.ts`** -> AI Confidence: **99.15%**
135. **`src/filters/blend-modes/BlendModeFilter.ts`** -> AI Confidence: **99.15%**
136. **`src/rendering/renderers/canvas/utils/canvasUtils.ts`** -> AI Confidence: **99.15%**
137. **`src/rendering/renderers/gl/GlEncoderSystem.ts`** -> AI Confidence: **99.15%**
138. **`src/rendering/renderers/gl/shader/GlProgram.ts`** -> AI Confidence: **99.15%**
139. **`src/rendering/renderers/gpu/GpuUniformBatchPipe.ts`** -> AI Confidence: **99.15%**
140. **`src/rendering/renderers/shared/GCSystem.ts`** -> AI Confidence: **99.15%**
141. **`src/rendering/renderers/shared/buffer/Buffer.ts`** -> AI Confidence: **99.15%**
142. **`src/rendering/renderers/shared/texture/utils/textureFrom.ts`** -> AI Confidence: **99.15%**
143. **`src/scene/container/RenderGroupPipe.ts`** -> AI Confidence: **99.15%**
144. **`src/scene/graphics/canvas/CanvasGraphicsContextSystem.ts`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1241` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/scene/sprite-tiling/TilingSpritePipe.ts` (TYPESCRIPT) -> Cumulative Risk: **634.67**
- **Archetype:** `file_cluster_13` (Distance: 11.105 IQR)
- **Magnitude:** 15.35 | **LOC:** 261 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9808%), Tech Debt (99.7206%)
- **Heaviest Functions:** `addRenderable` (Impact: 14.2), `updateRenderable` (Impact: 11.4), `_updateCanBatch` (Impact: 8.8)

### 2. `src/scene/graphics/shared/GraphicsPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **633.22**
- **Archetype:** `file_cluster_13` (Distance: 11.681 IQR)
- **Magnitude:** 15.45 | **LOC:** 244 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.5283%)
- **Heaviest Functions:** `addRenderable` (Impact: 9.8), `execute` (Impact: 9.4), `validateRenderable` (Impact: 6.9)

### 3. `src/scene/text-bitmap/AbstractBitmapTextPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **630.24**
- **Archetype:** `file_cluster_13` (Distance: 11.476 IQR)
- **Magnitude:** 14.72 | **LOC:** 247 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9954%), Tech Debt (99.9877%), Safety Score (88.1652%)
- **Heaviest Functions:** `_updateContext` (Impact: 25.5), `addRenderable` (Impact: 6.2), `updateRenderable` (Impact: 4.7)

### 4. `transcoders/basis/basis_transcoder.js` (JAVASCRIPT) -> Cumulative Risk: **616.28**
- **Archetype:** `file_cluster_11` (Distance: 15.544 IQR)
- **Magnitude:** 2175.78 | **LOC:** 1265 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8668%), Cognitive Load (99.3917%)
- **Heaviest Functions:** `craftInvokerFunction` (Impact: 67.4), `__embind_register_std_string` (Impact: 51.4), `registerType` (Impact: 51.1)

### 5. `src/rendering/mask/stencil/CanvasStencilMaskPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **615.77**
- **Archetype:** `file_cluster_13` (Distance: 11.969 IQR)
- **Magnitude:** 33.28 | **LOC:** 397 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.825%), Verification (80.0%), Tech Debt (78.9619%)
- **Heaviest Functions:** `execute` (Impact: 91.5), `buildShapePath` (Impact: 42.1), `addHolePaths` (Impact: 20.7)

### 6. `src/rendering/mask/alpha/AlphaMaskPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **604.82**
- **Archetype:** `file_cluster_13` (Distance: 11.139 IQR)
- **Magnitude:** 13.04 | **LOC:** 281 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.926%), State Flux (99.9014%), Verification (80.0%)
- **Heaviest Functions:** `execute` (Impact: 20.4), `push` (Impact: 14.2), `pop` (Impact: 4.7)

### 7. `src/rendering/renderers/gpu/GpuEncoderSystem.ts` (TYPESCRIPT) -> Cumulative Risk: **599.19**
- **Archetype:** `file_cluster_13` (Distance: 13.021 IQR)
- **Magnitude:** 28.8 | **LOC:** 318 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.1366%), Documentation (85.1279%)
- **Heaviest Functions:** `_setShaderBindGroups` (Impact: 7.7), `draw` (Impact: 7.5), `restoreRenderPass` (Impact: 7.1)

### 8. `src/rendering/batcher/shared/BatcherPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **597.63**
- **Archetype:** `file_cluster_13` (Distance: 12.724 IQR)
- **Magnitude:** 20.73 | **LOC:** 185 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.6865%), Documentation (91.9808%)
- **Heaviest Functions:** `execute` (Impact: 40.8), `buildStart` (Impact: 13.1), `addToBatch` (Impact: 7.9)

### 9. `src/scene/text-html/HTMLTextPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **587.12**
- **Archetype:** `file_cluster_13` (Distance: 11.962 IQR)
- **Magnitude:** 15.57 | **LOC:** 194 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.1925%), Concurrency (81.1041%)
- **Heaviest Functions:** `_updateGpuText` (Impact: 18.0), `addRenderable` (Impact: 11.6), `resolutionChange` (Impact: 7.5)

### 10. `src/scene/text-bitmap/utils/getBitmapTextLayout.ts` (TYPESCRIPT) -> Cumulative Risk: **576.53**
- **Archetype:** `file_cluster_8` (Distance: 11.174 IQR)
- **Magnitude:** 39.53 | **LOC:** 388 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9042%), Safety Score (82.6187%)
- **Heaviest Functions:** `getBitmapTextLayout` (Impact: 157.3), `checkIsOverflow` (Impact: 69.3), `nextWord` (Impact: 10.2)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `transcoders/basis/basis_transcoder.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.544 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.141 IQR)
- **Top Global Matches:** file_cluster_11: 15.544, file_cluster_17: 15.576, file_cluster_4: 15.759
- **Magnitude:** 2175.78 | **LOC:** 1265 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.3917%), Tech Debt (99.8668%)
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` (Impact: 67.4)
  * `__embind_register_std_string` (Impact: 51.4)
  * `registerType` (Impact: 51.1)
  * `genericPointerToWireType` (Impact: 46.7)
  * `stringToUTF8Array` (Impact: 43.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 382`, `args: 220`, `func_start: 206`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 777`, `duplicate_logic: 31`, `orphaned_logic: 9`
* *Architecture:* `io: 32`, `api: 2`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 198`, `test: 4`, `immutability_locks: 194`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugins/typedoc-plugin-stackblitz.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.927 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.231 IQR)
- **Top Global Matches:** file_cluster_8: 9.927, file_cluster_13: 10.437, file_cluster_17: 10.585
- **Magnitude:** 132.34 | **LOC:** 481 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.676%), Tech Debt (56.1854%)
**Top Internal Functions/Classes:**
  * `scanExampleDir` (Impact: 21.6)
  * `scanExamples` (Impact: 20.0)
  * `findExampleDirs` (Impact: 17.3)
    * *Intent:* // Find all __docs__/examples/ directories under src/
  * `readDirRecursive` (Impact: 15.4)
  * `buildProjectData` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 71`, `args: 24`, `func_start: 22`
* *Risk/State:* `state_mutation: 34`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 15`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path, typescript, mini-shiki, typedoc, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugins/typedoc-plugin-llms-txt.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.235 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.003 IQR)
- **Top Global Matches:** file_cluster_13: 12.235, file_cluster_8: 12.247, file_cluster_0: 12.464
- **Magnitude:** 131.9 | **LOC:** 165 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.9387%), Tech Debt (96.7987%)
**Top Internal Functions/Classes:**
  * `buildLlmsTxt` (Impact: 30.3)
  * `getDescription` (Impact: 22.1)
  * `isAdvanced` (Impact: 15.9)
    * *Intent:* /**
  * `collectDocEntries` (Impact: 10.8)
  * `buildUrlMap` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 16`, `args: 8`, `func_start: 10`
* *Risk/State:* `state_mutation: 30`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 3`
* *Defense:* `safety: 13`, `doc: 4`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path, fs, typedoc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugins/eslint-require-export.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.477 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.358 IQR)
- **Top Global Matches:** file_cluster_8: 10.477, file_cluster_0: 10.512, file_cluster_13: 10.947
- **Magnitude:** 124.02 | **LOC:** 132 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0599%), Tech Debt (93.6355%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 52.4)
  * `TSTypeAliasDeclaration` (Impact: 13.5)
  * `ExportDefaultDeclaration` (Impact: 13.4)
  * `TSInterfaceDeclaration` (Impact: 13.4)
  * `ExportNamedDeclaration` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 14`, `args: 8`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 19`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsdoccomment, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.stackblitz/bunny-mark/src/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.852 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.815 IQR)
- **Top Global Matches:** file_cluster_4: 10.852, file_cluster_8: 11.055, file_cluster_13: 11.343
- **Magnitude:** 111.58 | **LOC:** 195 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.8155%), Tech Debt (70.1334%)
**Top Internal Functions/Classes:**
  * `renderUpdate` (Impact: 12.9)
  * `onclick` (Impact: 5.5)
  * `onclick` (Impact: 3.7)
  * `addBunnies` (Impact: 3.6)
  * `loadAssets` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 14`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 1`, `concurrency: 32`, `import: 3`
* *Defense:* `safety: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bunny, stats.js, pixi.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/path.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.401 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.594 IQR)
- **Top Global Matches:** file_cluster_8: 12.401, file_cluster_0: 12.556, file_cluster_7: 12.621
- **Magnitude:** 88.58 | **LOC:** 940 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.0481%), Tech Debt (90.1764%)
**Top Internal Functions/Classes:**
  * `isDataUrl` (Impact: 245.0)
  * `normalizeStringPosix` (Impact: 67.5)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `parse` (Impact: 60.7)
  * `basename` (Impact: 53.1)
    * *Intent:* /** * Returns the protocol of the path e.g. http://, https://, file:///, data:, blob:, C:/ * @param ...
  * `extname` (Impact: 36.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 40`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 190`, `dead_code: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 121`, `api: 4`, `import: 1`
* *Defense:* `safety: 5`, `doc: 40`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.167
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` adapter, pixi.js
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `.stackblitz/bunny-mark/src/Bunny.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.049 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.979 IQR)
- **Top Global Matches:** file_cluster_8: 13.049, file_cluster_13: 13.127, file_cluster_7: 13.358
- **Magnitude:** 85.94 | **LOC:** 65 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.8592%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 13.2)
  * `constructor` (Impact: 2.0)
  * `destroy` (Impact: 1.7)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 8`, `args: 3`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.514
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pixi.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/plugins/typedoc-plugin-router.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.436 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.642 IQR)
- **Top Global Matches:** file_cluster_8: 8.436, file_cluster_7: 9.311, file_cluster_13: 9.44
- **Magnitude:** 85.74 | **LOC:** 160 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.9303%), Tech Debt (35.2958%)
**Top Internal Functions/Classes:**
  * `createNormalizedUrl` (Impact: 31.1)
  * `getIdealBaseName` (Impact: 18.8)
  * `isalpha` (Impact: 3.7)
  * `isdigit` (Impact: 3.7)
  * `isalnum` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 16`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typedoc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/text/TextStyle.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.226 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.43 IQR)
- **Top Global Matches:** file_cluster_0: 13.226, file_cluster_13: 13.313, file_cluster_8: 13.424
- **Magnitude:** 80.35 | **LOC:** 1549 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.3013%), Tech Debt (99.9958%)
**Top Internal Functions/Classes:**
  * `convertV7Tov8Style` (Impact: 78.9)
  * `destroy` (Impact: 36.1)
  * `dropShadow` (Impact: 15.4)
    * *Intent:* /** * The angle of the drop shadow in radians. * - 0 = right * - Math.PI/2 = down * - Math.PI = left...
  * `_isFillStyle` (Impact: 12.2)
  * `_toObject` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 112`, `args: 65`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 396`, `duplicate_logic: 46`
* *Architecture:* `api: 37`, `import: 13`
* *Defense:* `safety: 35`, `doc: 90`, `immutability_locks: 33`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.287
  * `Choke Point (Betweenness):` 0.002042 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` fontStringFromTextStyle, GraphicsContext, convertFillInputToFillStyle, uid, pixi.js, warn, deprecation, eventemitter3...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `src/events/EventBoundary.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.577 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.019 IQR)
- **Top Global Matches:** file_cluster_13: 13.577, file_cluster_0: 13.688, file_cluster_11: 13.756
- **Magnitude:** 68.64 | **LOC:** 1487 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.0259%), Tech Debt (9.129%)
**Top Internal Functions/Classes:**
  * `pruneFn` (Impact: 148.1)
  * `warn` (Impact: 28.2)
  * `propagate` (Impact: 21.2)
    * *Intent:* /**
  * `mapPointerUpOutside` (Impact: 20.1)
  * `createPointerEvent` (Impact: 17.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 89`, `args: 32`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 270`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 12`, `import: 12`
* *Defense:* `safety: 28`, `doc: 77`, `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.729
  * `Choke Point (Betweenness):` 0.000273 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` pixi-spatial-hash, EventTicker, FederatedEvent, pixi.js, FederatedPointerEvent, warn, Renderable, eventemitter3...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/color/Color.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.206 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.808 IQR)
- **Top Global Matches:** file_cluster_13: 13.206, file_cluster_8: 13.222, file_cluster_7: 13.284
- **Magnitude:** 65.08 | **LOC:** 1195 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.9543%), Tech Debt (22.8879%)
**Top Internal Functions/Classes:**
  * `extend` (Impact: 166.1)
  * `isColorLike` (Impact: 66.5)
    * *Intent:* /** * Convert to a RGBA color object with normalized components (0-1). * @example * ```ts * import {...
  * `_normalize` (Impact: 36.9)
    * *Intent:* * color.value = 0xff0000; // Hex number * color.value = '#ff0000'; // Hex string * color.value = [1,...
  * `_isSourceEqual` (Impact: 30.0)
    * *Intent:* * new Color(new Float32Array([1, 0, 0, 0.5])).toArray(); // [1, 0, 0, 0.5] * new Color(new Uint8Arra...
  * `value` (Impact: 18.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 55`, `args: 33`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 173`, `duplicate_logic: 2`
* *Architecture:* `api: 38`, `import: 3`
* *Defense:* `safety: 4`, `doc: 78`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.206
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pixi.js, colord, names
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `scripts/plugins/eslint-require-modifier.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.306 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.937 IQR)
- **Top Global Matches:** file_cluster_0: 10.306, file_cluster_8: 10.57, file_cluster_13: 10.766
- **Magnitude:** 63.04 | **LOC:** 234 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.838%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 24.8)
  * `getComment` (Impact: 17.8)
  * `isClassInternal` (Impact: 9.7)
  * `isExported` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 11`, `args: 5`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 4`, `import: 2`
* *Defense:* `safety: 7`, `doc: 6`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsdoccomment, types, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugins/eslint-require-tilde-imports.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.682 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.79 IQR)
- **Top Global Matches:** file_cluster_8: 8.682, file_cluster_7: 9.595, file_cluster_13: 9.614
- **Magnitude:** 59.72 | **LOC:** 101 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.4215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 30.3)
  * `checkImport` (Impact: 19.8)
  * `fix` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 10`, `args: 3`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 10`, `api: 2`, `import: 1`
* *Defense:* `safety: 8`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/rendering/renderers/shared/texture/sources/VideoSource.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.597 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.131 IQR)
- **Top Global Matches:** file_cluster_13: 14.597, file_cluster_4: 14.638, file_cluster_11: 14.847
- **Magnitude:** 57.93 | **LOC:** 575 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.2361%), Tech Debt (58.8349%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 27.3)
  * `_configureAutoUpdate` (Impact: 25.2)
  * `updateFrame` (Impact: 13.4)
  * `constructor` (Impact: 13.2)
  * `_mediaReady` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 35`, `args: 28`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 369`, `duplicate_logic: 4`
* *Architecture:* `api: 14`, `concurrency: 31`, `import: 8`
* *Defense:* `safety: 24`, `doc: 50`, `test: 1`, `immutability_locks: 11`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.439
  * `Choke Point (Betweenness):` 0.000163 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` detectVideoAlphaMode, Extensions, TextureSource, const, types, Ticker
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/GraphicsContext.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.598 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.685 IQR)
- **Top Global Matches:** file_cluster_13: 13.598, file_cluster_8: 13.95, file_cluster_7: 13.964
- **Magnitude:** 52.71 | **LOC:** 1285 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.9287%), Tech Debt (79.2797%)
**Top Internal Functions/Classes:**
  * `containsPoint` (Impact: 41.4)
  * `destroy` (Impact: 33.9)
  * `texture` (Impact: 32.9)
  * `fill` (Impact: 21.3)
    * *Intent:* /** * Sets the current stroke style of the graphics context. Similar to fill styles, stroke styles c...
  * `roundShape` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 73`, `args: 35`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `state_mutation: 236`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 17`, `api: 50`, `import: 19`
* *Defense:* `safety: 9`, `doc: 169`, `immutability_locks: 30`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.313
  * `Choke Point (Betweenness):` 0.004529 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` destroyTypes, Bounds, GraphicsContextSystem, FillTypes, GCSystem, Shader, convertFillInputToFillStyle, GraphicsPath...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/assets/loader/Loader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.31 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.332 IQR)
- **Top Global Matches:** file_cluster_4: 12.31, file_cluster_13: 12.649, file_cluster_0: 12.746
- **Magnitude:** 52.6 | **LOC:** 475 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.0748%), Tech Debt (82.0434%)
**Top Internal Functions/Classes:**
  * `promise` (Impact: 59.9)
  * `_getLoadPromiseAndParser` (Impact: 54.6)
    * *Intent:* /** * Delay in milliseconds between retry attempts * @default 250 * @example * ```ts * const options...
  * `warn` (Impact: 48.0)
    * *Intent:* /** * Default options for loading assets * @example * ```ts * // Change default load options globall...
  * `_loadAssetWithRetry` (Impact: 38.8)
  * `wait` (Impact: 34.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 56`, `args: 26`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 80`, `duplicate_logic: 5`
* *Architecture:* `io: 4`, `api: 12`, `concurrency: 99`, `import: 8`
* *Defense:* `safety: 17`, `doc: 26`, `immutability_locks: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.549
  * `Choke Point (Betweenness):` 0.001834 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` path, warn, Assets, types, LoaderParser, types, isSingleItem, convertToList
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/accessibility/AccessibilitySystem.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.94 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.14 IQR)
- **Top Global Matches:** file_cluster_13: 13.94, file_cluster_8: 14.206, file_cluster_7: 14.277
- **Magnitude:** 50.24 | **LOC:** 913 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.812%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `postrender` (Impact: 39.5)
  * `_addChild` (Impact: 31.5)
  * `_deactivate` (Impact: 21.7)
  * `_activate` (Impact: 17.1)
  * `_updateAccessibleObjects` (Impact: 15.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 44`, `args: 26`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `state_mutation: 281`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 21`, `doc: 58`, `immutability_locks: 25`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.81
  * `Choke Point (Betweenness):` 0.004216 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` accessibilityTarget, pixi.js, types, Extensions, System, FederatedEvent, Container, isMobile...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/assets/resolver/Resolver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.78 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.765 IQR)
- **Top Global Matches:** file_cluster_0: 12.78, file_cluster_17: 12.888, file_cluster_13: 12.892
- **Magnitude:** 49.11 | **LOC:** 881 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (29.3168%), Tech Debt (57.8722%)
**Top Internal Functions/Classes:**
  * `warn` (Impact: 73.8)
  * `add` (Impact: 60.0)
  * `getAlias` (Impact: 18.9)
    * *Intent:* /**
  * `resolve` (Impact: 18.7)
  * `addBundle` (Impact: 14.9)
    * *Intent:* /** * Set the base path to prepend to all urls when resolving * @example
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 79`, `args: 54`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 175`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 23`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 34`, `doc: 48`, `immutability_locks: 39`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.3
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` path, createStringVariations, warn, types, types, isSingleItem, convertToList
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/scene/container/bounds/Bounds.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.167 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.229 IQR)
- **Top Global Matches:** file_cluster_8: 14.167, file_cluster_7: 14.206, file_cluster_13: 14.222
- **Magnitude:** 46.21 | **LOC:** 1017 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.0638%), Tech Debt (99.9889%)
**Top Internal Functions/Classes:**
  * `addFrame` (Impact: 49.2)
    * *Intent:* /** * The maximum X coordinate of the bounds. * Represents the rightmost edge of the bounding box.
  * `addVertexData` (Impact: 19.6)
  * `fitBounds` (Impact: 11.7)
    * *Intent:* /** * Checks if bounds are empty, meaning either width or height is zero or negative. * Empty bounds...
  * `fit` (Impact: 10.5)
    * *Intent:* /** * Creates a new Bounds object. * @param minX - The minimum X coordinate of the bounds. * @param ...
  * `rectangle` (Impact: 9.8)
    * *Intent:* // TODO optimisations // 1 - get rectangle could use a dirty flag, rather than setting the data each...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 29`, `args: 31`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `state_mutation: 254`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 35`, `import: 2`
* *Defense:* `safety: 2`, `doc: 80`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.633
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Matrix, Rectangle
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `src/rendering/batcher/shared/Batcher.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.093 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.338 IQR)
- **Top Global Matches:** file_cluster_13: 13.093, file_cluster_8: 13.352, file_cluster_7: 13.426
- **Magnitude:** 45.45 | **LOC:** 827 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.2472%), Tech Debt (73.7534%)
**Top Internal Functions/Classes:**
  * `break` (Impact: 43.0)
  * `_resizeIndexBuffer` (Impact: 11.4)
    * *Intent:* // create a batch...
  * `_finishBatch` (Impact: 7.8)
  * `clear` (Impact: 7.6)
  * `updateElement` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 51`, `args: 26`, `func_start: 26`, `class_start: 6`
* *Risk/State:* `state_mutation: 253`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 55`, `import: 17`
* *Defense:* `safety: 4`, `doc: 93`, `immutability_locks: 28`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.566
  * `Choke Point (Betweenness):` 0.00208 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` getAdjustedBlendModeBlend, ViewableBuffer, InstructionSet, Bounds, uid, Texture, maxRecommendedTextures, BindGroup...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/rendering/renderers/shared/__tests__/GCSystem.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.332 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.098 IQR)
- **Top Global Matches:** file_cluster_8: 10.332, file_cluster_13: 11.03, file_cluster_7: 11.034
- **Magnitude:** 44.5 | **LOC:** 1041 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.5548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 96.1)
  * `describe` (Impact: 25.8)
  * `describe` (Impact: 18.6)
  * `describe` (Impact: 13.2)
  * `describe` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 103`, `args: 166`, `func_start: 161`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 23`, `duplicate_logic: 67`, `orphaned_logic: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 19`, `test: 158`, `immutability_locks: 85`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utils, types, GCSystem
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/text/canvas/__tests__/CanvasTextMetrics.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.341 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.267 IQR)
- **Top Global Matches:** file_cluster_8: 9.341, file_cluster_7: 10.122, file_cluster_1: 10.225
- **Magnitude:** 44.33 | **LOC:** 1037 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.8656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 84.5)
  * `describe` (Impact: 21.1)
  * `describe` (Impact: 12.2)
  * `describe` (Impact: 8.4)
  * `describe` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 130`, `args: 259`, `func_start: 259`
* *Risk/State:* `safety_bypasses: 5`, `duplicate_logic: 108`, `orphaned_logic: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 11`, `test: 259`, `immutability_locks: 173`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` CanvasTextMetrics, browserAll, TextStyle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/assets/__tests__/Assets.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.083 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.237 IQR)
- **Top Global Matches:** file_cluster_4: 10.083, file_cluster_8: 10.127, file_cluster_0: 10.69
- **Magnitude:** 42.61 | **LOC:** 711 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.7101%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 54.2)
  * `it` (Impact: 6.9)
  * `it` (Impact: 6.1)
  * `it` (Impact: 5.9)
  * `it` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 117`, `args: 118`, `func_start: 115`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `duplicate_logic: 35`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `concurrency: 223`, `import: 5`
* *Defense:* `safety: 5`, `doc: 2`, `test: 113`, `immutability_locks: 61`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Assets, assets, promises, rendering, init, @test-utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/maths/matrix/Matrix.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.841 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.798 IQR)
- **Top Global Matches:** file_cluster_8: 13.841, file_cluster_13: 13.883, file_cluster_7: 13.885
- **Magnitude:** 39.91 | **LOC:** 1006 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.9215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toArray` (Impact: 13.9)
  * `equals` (Impact: 12.3)
  * `prepend` (Impact: 11.0)
  * `isIdentity` (Impact: 10.6)
    * *Intent:* /** * Get a new position with the inverse of the current transformation applied. * * Can be used to ...
  * `decompose` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 30`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `state_mutation: 236`
* *Architecture:* `api: 49`, `import: 3`
* *Defense:* `safety: 1`, `doc: 96`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.907
  * `Choke Point (Betweenness):` 0.000192 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` const, Point, PointData
  * `Imported By (In-Degree: 68):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/assets/utils/__tests__/createStringVariations.test.ts` (TYPESCRIPT) | Magnitude: 0.72 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, decorators: 11, args: 5, func_start: 5
- `src/scene/sprite-animated/AnimatedSprite.ts` (TYPESCRIPT) | Magnitude: 35.2 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 213, indent_spaces: 209, branch: 52, doc: 38
- `src/rendering/high-shader/shader-bits/generateTextureBatchBit.ts` (TYPESCRIPT) | Magnitude: 13.67 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 70, branch: 21, structural_boundaries: 15
- `src/ticker/Ticker.ts` (TYPESCRIPT) | Magnitude: 4.64 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 19, doc: 10, structural_boundaries: 9
- `src/rendering/high-shader/compiler/utils/compileInputs.ts` (TYPESCRIPT) | Magnitude: 3.82 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 16, args: 6, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/environment/ImageLike.ts` (TYPESCRIPT) | Magnitude: 3.11 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, doc: 9, structural_boundaries: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `transcoders/basis/basis_transcoder.js` (JAVASCRIPT) | Magnitude: 2175.78 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 945, state_mutation: 777, branch: 521, structural_boundaries: 382
- `src/utils/pool/Pool.ts` (TYPESCRIPT) | Magnitude: 5.21 | Delta: **0.202 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 30, structural_boundaries: 13, doc: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/math-extras/pointExtras.ts` (TYPESCRIPT) | Magnitude: 13.47 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 98, state_mutation: 66, structural_boundaries: 24, branch: 17
- `tests/visual/scenes/sprite/sprite-trim.scene.ts` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, concurrency: 7, immutability_locks: 5
- `src/scene/graphics/shared/buildCommands/buildPixelLine.ts` (TYPESCRIPT) | Magnitude: 4.01 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 18, immutability_locks: 10, branch: 6
- `scripts/index/index.mts` (TYPESCRIPT) | Magnitude: 1.53 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 8, io: 5, structural_boundaries: 4, import: 3
- `src/scene/text/utils/getPo2TextureFromSource.ts` (TYPESCRIPT) | Magnitude: 1.0 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 12, doc: 7, decorators: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/rendering/renderers/gl/state/mapWebGLBlendModesToPixi.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 7, generics: 6, ui_framework: 4
- `src/assets/AssetExtension.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, generics: 11, indent_spaces: 11, doc: 8
- `src/rendering/renderers/shared/texture/sources/CubeTextureSource.ts` (TYPESCRIPT) | Magnitude: 8.2 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, immutability_locks: 22, state_mutation: 17, branch: 16
- `src/scene/container/utils/assignWithIgnore.ts` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, doc: 4, branch: 3, structural_boundaries: 2
- `src/rendering/high-shader/compiler/utils/compileHooks.ts` (TYPESCRIPT) | Magnitude: 1.11 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, branch: 4, structural_boundaries: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/test.mts` (TYPESCRIPT) | Magnitude: 8.3 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 81, branch: 29, immutability_locks: 25, structural_boundaries: 19
- `src/assets/loader/parsers/loadWebFont.ts` (TYPESCRIPT) | Magnitude: 7.81 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 31, branch: 20, immutability_locks: 16
- `src/extensions/Extensions.ts` (TYPESCRIPT) | Magnitude: 17.56 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 73, doc: 72, state_mutation: 44
- `src/utils/pool/GlobalResourceRegistry.ts` (TYPESCRIPT) | Magnitude: 3.0 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, doc: 14, args: 8, state_mutation: 8
- `src/spritesheet/spritesheetAsset.ts` (TYPESCRIPT) | Magnitude: 8.07 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 42, branch: 32, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `playground/src/hooks/useIframeScene.ts` (TYPESCRIPT) | Magnitude: 6.69 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 17, args: 14, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/visual/scenes/container/root-container-visibility.scene.ts` (TYPESCRIPT) | Magnitude: 1.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, concurrency: 7, import: 4
- `examples/sprite_svg.ts` (TYPESCRIPT) | Magnitude: 2.24 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, state_mutation: 4, immutability_locks: 4
- `examples/container_tinting.ts` (TYPESCRIPT) | Magnitude: 4.0 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, scientific: 18, state_mutation: 16, branch: 8
- `playground/src/hooks/useBuildStatus.ts` (TYPESCRIPT) | Magnitude: 8.8 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 12, branch: 11, args: 7
- `examples/rendering_render-texture_basic.ts` (TYPESCRIPT) | Magnitude: 2.76 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, concurrency: 8, immutability_locks: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/visual/scenes/text-bitmap/bitmap-text-stroke-alpha.scene.ts` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, immutability_locks: 4, import: 3
- `src/events/FederatedWheelEvent.ts` (TYPESCRIPT) | Magnitude: 2.63 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: api: 11, doc: 11, indent_spaces: 10, immutability_locks: 6
- `src/utils/logging/logScene.ts` (TYPESCRIPT) | Magnitude: 3.67 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, state_mutation: 27, branch: 11, doc: 11
- `tests/visual/scenes/particle-container/particle.scene.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 9, immutability_locks: 8, import: 4
- `src/scene/text/shared/GpuTextSystem.ts` (TYPESCRIPT) | Magnitude: 0.52 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, api: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/scene/container/__tests__/Container.Culling.test.ts` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 4, args: 3, func_start: 3, test: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/rendering/mask/stencil/CanvasStencilMaskPipe.ts` -> Churn: **55.79%** | Cog Load: 76.2414% | Debt: 78.9619%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/plugins/typedoc-plugin-stackblitz.mjs` -> **Zyie** (100.0% isolated ownership) | Magnitude: 132.34
- `scripts/plugins/typedoc-plugin-llms-txt.mjs` -> **Zyie** (100.0% isolated ownership) | Magnitude: 131.9
- `src/scene/text/TextStyle.ts` -> **Zyie** (100.0% isolated ownership) | Magnitude: 80.35
- `src/color/Color.ts` -> **Shashwat Raj** (100.0% isolated ownership) | Magnitude: 65.08
- `scripts/plugins/eslint-require-tilde-imports.mjs` -> **Zyie** (100.0% isolated ownership) | Magnitude: 59.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/rendering/renderers/shared/system/AbstractRenderer.ts` -> **Severity: 2.201** (Bridge: 0.022 * Flux: 100.0%)
- `src/rendering/renderers/shared/texture/sources/TextureSource.ts` -> **Severity: 1.941** (Bridge: 0.0194 * Flux: 100.0%)
- `src/scene/container/Container.ts` -> **Severity: 1.619** (Bridge: 0.0162 * Flux: 100.0%)
- `src/rendering/renderers/gpu/texture/GpuTextureSystem.ts` -> **Severity: 1.308** (Bridge: 0.0131 * Flux: 100.0%)
- `src/filters/FilterSystem.ts` -> **Severity: 1.142** (Bridge: 0.0114 * Flux: 99.9956%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/rendering/renderers/shared/instructions/InstructionSet.ts` -> **Severity: 361.255** (Blast Radius: 3.68 * Doc Risk: 98.1671%)
- `src/scene/container/Container.ts` -> **Severity: 280.257** (Blast Radius: 15.674 * Doc Risk: 17.8804%)
- `src/scene/view/ViewContainer.ts` -> **Severity: 264.814** (Blast Radius: 7.706 * Doc Risk: 34.3646%)
- `src/extensions/Extensions.ts` -> **Severity: 242.685** (Blast Radius: 20.359 * Doc Risk: 11.9203%)
- `src/scene/container/RenderGroup.ts` -> **Severity: 229.159** (Blast Radius: 2.674 * Doc Risk: 85.6989%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
