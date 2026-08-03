# ARCHITECTURAL_BRIEF: pixijs
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/pixijs` |
| **Timestamp** | `2026-08-03T19:56:19.929294+00:00` |
| **Scan Duration** | `7.81s` |
| **Git Branch** | `dev` |
| **Git Commit** | `627a356cf297c027019195a7a27f1bf4b46c4767` |
| **Git Remote** | `https://github.com/pixijs/pixijs.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1444 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.514`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 900 | 58.8% |
| file_cluster_13 | 461 | 30.1% |
| file_cluster_4 | 47 | 3.1% |
| file_cluster_16 | 25 | 1.6% |
| file_cluster_0 | 24 | 1.6% |
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
| Cognitive Load Exposure | 0.0 | 99.8 | 15.0 | 6.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 34.0 | 34.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 20.0 | 4.2 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 39.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 37.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 93.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.2 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 67.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.4 | 6.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 37.9 | 6.9 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `isDataUrl` (@ `src/utils/path.ts`) -> Impact: **1575.2** | LOC: 465
- `pruneFn` (@ `src/events/EventBoundary.ts`) -> Impact: **906.7** | LOC: 433
- `recursive` (@ `src/scene/graphics/shared/buildCommands/buildAdaptiveBezier.ts`) -> Impact: **761.1** | LOC: 187
- `wordWrapTaggedLines` (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **518.3** | LOC: 268
- `replaceChild` (@ `src/scene/container/container-mixins/childrenHelperMixin.ts`) -> Impact: **490.5** | LOC: 249
  * *Intent:* /** * Adds a child to the container at a specified index. If the index is out of bounds an error will be thrown. * If the child is already in this con...
- `buildLine` (@ `src/scene/graphics/shared/buildCommands/buildLine.ts`) -> Impact: **454.8** | LOC: 385
- `execute` (@ `src/scene/graphics/canvas/CanvasGraphicsAdaptor.ts`) -> Impact: **454.7** | LOC: 244
- `extend` (@ `src/color/Color.ts`) -> Impact: **446.1** | LOC: 521
- `getBitmapTextLayout` (@ `src/scene/text-bitmap/utils/getBitmapTextLayout.ts`) -> Impact: **443.5** | LOC: 284
  * *Intent:* // / spaces: number
- `_getGlobalBoundsRecursive` (@ `src/scene/container/container-mixins/getFastGlobalBoundsMixin.ts`) -> Impact: **397.7** | LOC: 128

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `attachFinalizer` (@ `transcoders/basis/basis_transcoder.js`) -> **O(2^N) [Recursive]**
- `onSelect` (@ `playground/src/panels/TreeView.tsx`) -> **O(2^N) [Recursive]**
- `pruneFn` (@ `src/events/EventBoundary.ts`) -> **O(2^N) [Recursive]**
- `base64` (@ `src/rendering/renderers/shared/extract/ExtractSystem.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * The region of the target to extract. If not specified, extracts the entire target. * @example * ```ts * // Extract a specific region * renderer....
- `load` (@ `src/rendering/renderers/shared/texture/sources/VideoSource.ts`) -> **O(2^N) [Recursive]**
- `_updateCachedRenderGroups` (@ `src/scene/container/RenderGroupSystem.ts`) -> **O(2^N) [Recursive]**
- `_getGlobalBoundsRecursive` (@ `src/scene/container/container-mixins/getFastGlobalBoundsMixin.ts`) -> **O(2^N) [Recursive]**
- `containsPoint` (@ `src/scene/graphics/shared/GraphicsContext.ts`) -> **O(2^N) [Recursive]**
- `recursive` (@ `src/scene/graphics/shared/buildCommands/buildAdaptiveBezier.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `src/scene/sprite-animated/__tests__/AnimatedSprite.test.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `src/utils/__tests__/path.test.ts`) -> DB Complexity: **1174**
- `isDataUrl` (@ `src/utils/path.ts`) -> DB Complexity: **368**
- `describe` (@ `src/scene/graphics/shared/__tests__/SVGParser.test.ts`) -> DB Complexity: **102**
- `extend` (@ `src/color/Color.ts`) -> DB Complexity: **83**
- `describe` (@ `src/assets/resolver/__tests__/Resolver.test.ts`) -> DB Complexity: **79**
- `parseSVGPath` (@ `src/scene/graphics/shared/svg/parseSVGPath.ts`) -> DB Complexity: **72**
  * *Intent:* /**
- `pruneFn` (@ `src/events/EventBoundary.ts`) -> DB Complexity: **66**
- `contextChange` (@ `src/rendering/renderers/gl/texture/GlTextureSystem.ts`) -> DB Complexity: **54**
- `buildLine` (@ `src/scene/graphics/shared/buildCommands/buildLine.ts`) -> DB Complexity: **50**
- `break` (@ `src/rendering/batcher/shared/Batcher.ts`) -> DB Complexity: **48**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 5 | 5049.44 | 2.12% | 0.0% |
| `transcoders/basis` | 1 | 4158.58 | 95.32% | 50.39% |
| `scripts/plugins` | 8 | 925.77 | 17.53% | 22.83% |
| `src/scene/container/container-mixins` | 11 | 269.61 | 32.55% | 10.9% |
| `src/events` | 14 | 267.47 | 16.68% | 13.78% |
| `src/scene/graphics/shared` | 7 | 260.79 | 32.46% | 46.63% |
| `.stackblitz/bunny-mark/src` | 2 | 255.52 | 71.34% | 35.07% |
| `examples` | 87 | 232.06 | 35.65% | 0.0% |
| `src/scene/graphics/shared/buildCommands` | 12 | 230.29 | 20.0% | 0.83% |
| `src/utils` | 6 | 213.39 | 12.37% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/build-status.mjs` -> **100.0%** Exposure
- `src/filters/defaults/alpha/AlphaFilter.ts` -> **100.0%** Exposure
- `src/filters/defaults/blur/BlurFilter.ts` -> **100.0%** Exposure
- `src/rendering/renderers/shared/texture/TextureGCSystem.ts` -> **100.0%** Exposure
- `src/rendering/renderers/shared/texture/TextureStyle.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.stackblitz/bunny-mark/src/Bunny.js` -> **100.0%** Exposure
- `transcoders/basis/basis_transcoder.js` -> **100.0%** Exposure
- `scripts/utils/autoGenerateUnsafeEvalFunctions.ts` -> **100.0%** Exposure
- `src/accessibility/AccessibilitySystem.ts` -> **100.0%** Exposure
- `src/app/ResizePlugin.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/scene/text/TextStyle.ts` -> **0** Orphaned Functions | **44** Duplicates
- `src/rendering/renderers/shared/texture/sources/TextureSource.ts` -> **0** Orphaned Functions | **20** Duplicates
- `src/scene/container/Container.ts` -> **0** Orphaned Functions | **18** Duplicates
- `src/filters/defaults/blur/BlurFilter.ts` -> **0** Orphaned Functions | **16** Duplicates
- `src/scene/sprite-nine-slice/NineSliceSprite.ts` -> **0** Orphaned Functions | **14** Duplicates

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

### Exploit Generation Surface
- `.stackblitz/bunny-mark/src/Bunny.js` -> **100.0%** Exposure
- `.stackblitz/bunny-mark/src/index.js` -> **100.0%** Exposure
- `transcoders/basis/basis_transcoder.js` -> **100.0%** Exposure
- `playground/src/hooks/useIframeScene.ts` -> **100.0%** Exposure
- `playground/vite.config.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/utils/autoGenerateUnsafeEvalFunctions.ts` -> **100.0%** Exposure
- `src/filters/FilterPipe.ts` -> **100.0%** Exposure
- `src/rendering/batcher/canvas/CanvasBatchAdaptor.ts` -> **100.0%** Exposure
- `src/rendering/batcher/gpu/GpuBatchAdaptor.ts` -> **100.0%** Exposure
- `src/rendering/batcher/shared/BatcherPipe.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `.stackblitz/bunny-mark/src/Bunny.js` -> **100.0%** Exposure
- `.stackblitz/bunny-mark/src/index.js` -> **100.0%** Exposure
- `scripts/plugins/eslint-require-tilde-imports.mjs` -> **100.0%** Exposure
- `scripts/plugins/typedoc-plugin-llms-txt.mjs` -> **100.0%** Exposure
- `transcoders/basis/basis_transcoder.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1241` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/rendering/mask/alpha/AlphaMaskPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **943.94**
- **Archetype:** `file_cluster_13` (Distance: 11.171 IQR)
- **Magnitude:** 20.34 | **LOC:** 281 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `execute` (Impact: 52.4), `push` (Impact: 32.2), `pop` (Impact: 8.7)

### 2. `src/scene/sprite-tiling/TilingSpritePipe.ts` (TYPESCRIPT) -> Cumulative Risk: **934.67**
- **Archetype:** `file_cluster_13` (Distance: 11.116 IQR)
- **Magnitude:** 22.26 | **LOC:** 261 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `addRenderable` (Impact: 32.4), `updateRenderable` (Impact: 26.4), `_updateCanBatch` (Impact: 16.8)

### 3. `src/scene/graphics/shared/GraphicsPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **923.87**
- **Archetype:** `file_cluster_13` (Distance: 11.685 IQR)
- **Magnitude:** 21.92 | **LOC:** 244 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `execute` (Impact: 33.5), `addRenderable` (Impact: 18.4), `validateRenderable` (Impact: 12.9)

### 4. `src/rendering/mask/stencil/CanvasStencilMaskPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **888.2**
- **Archetype:** `file_cluster_13` (Distance: 11.977 IQR)
- **Magnitude:** 59.96 | **LOC:** 397 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `execute` (Impact: 301.5), `buildShapePath` (Impact: 99.2), `addHolePaths` (Impact: 39.7)

### 5. `src/scene/text-bitmap/AbstractBitmapTextPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **867.23**
- **Archetype:** `file_cluster_13` (Distance: 11.485 IQR)
- **Magnitude:** 24.16 | **LOC:** 247 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_updateContext` (Impact: 77.4), `addRenderable` (Impact: 21.8), `updateRenderable` (Impact: 16.7)

### 6. `transcoders/basis/basis_transcoder.js` (JAVASCRIPT) -> Cumulative Risk: **865.59**
- **Archetype:** `file_cluster_11` (Distance: 15.54 IQR)
- **Magnitude:** 4158.58 | **LOC:** 1265 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `craftInvokerFunction` (Impact: 232.8), `__embind_register_std_string` (Impact: 172.6), `genericPointerToWireType` (Impact: 159.3)

### 7. `.stackblitz/bunny-mark/src/index.js` (JAVASCRIPT) -> Cumulative Risk: **862.43**
- **Archetype:** `file_cluster_4` (Distance: 10.852 IQR)
- **Magnitude:** 148.98 | **LOC:** 195 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `renderUpdate` (Impact: 29.8), `init` (Impact: 9.6), `onclick` (Impact: 8.1)

### 8. `src/rendering/renderers/gpu/GpuEncoderSystem.ts` (TYPESCRIPT) -> Cumulative Risk: **859.65**
- **Archetype:** `file_cluster_13` (Distance: 13.021 IQR)
- **Magnitude:** 36.92 | **LOC:** 318 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_setShaderBindGroups` (Impact: 18.1), `_syncBindGroup` (Impact: 15.6), `setBindGroup` (Impact: 12.7)

### 9. `src/rendering/renderers/shared/texture/TextureMatrix.ts` (TYPESCRIPT) -> Cumulative Risk: **848.36**
- **Archetype:** `file_cluster_13` (Distance: 12.953 IQR)
- **Magnitude:** 15.73 | **LOC:** 197 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `update` (Impact: 19.5), `constructor` (Impact: 18.4), `multiplyUvs` (Impact: 14.9)

### 10. `src/scene/text-html/HTMLTextPipe.ts` (TYPESCRIPT) -> Cumulative Risk: **845.59**
- **Archetype:** `file_cluster_13` (Distance: 11.962 IQR)
- **Magnitude:** 23.05 | **LOC:** 194 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_updateGpuText` (Impact: 41.5), `addRenderable` (Impact: 32.4), `resolutionChange` (Impact: 17.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `transcoders/basis/basis_transcoder.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.54 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.835 IQR)
- **Top Global Matches:** file_cluster_11: 15.54, file_cluster_17: 15.579, file_cluster_8: 15.752
- **Magnitude:** 4158.58 | **LOC:** 1265 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (95.3233%), Tech Debt (50.3931%)
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` (Impact: 232.8 | O(N^6) | DB: 18)
  * `__embind_register_std_string` (Impact: 172.6 | O(N^6) | DB: 9)
  * `genericPointerToWireType` (Impact: 159.3 | O(N^6) | DB: 18)
  * `stringToUTF8Array` (Impact: 149.7 | O(N^6) | DB: 2)
  * `__embind_register_class` (Impact: 119.1 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 382`, `args: 220`, `func_start: 206`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 777`, `duplicate_logic: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 32`, `api: 2`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 198`, `test: 4`, `immutability_locks: 194`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugins/typedoc-plugin-stackblitz.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.956 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.146 IQR)
- **Top Global Matches:** file_cluster_8: 9.956, file_cluster_13: 10.472, file_cluster_17: 10.627
- **Magnitude:** 226.04 | **LOC:** 481 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `scanExampleDir` (Impact: 59.7 | O(N^5) | DB: 3)
  * `readDirRecursive` (Impact: 57.5 | O(2^N) | DB: 2)
  * `scanExamples` (Impact: 54.6 | O(N^5) | DB: 2)
  * `buildProjectData` (Impact: 6.5 | O(N^2))
  * `getPixiVersion` (Impact: 2.1 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 71`, `args: 24`, `func_start: 22`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 15`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path, fs, typescript, typedoc, mini-shiki
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugins/typedoc-plugin-llms-txt.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.259 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.872 IQR)
- **Top Global Matches:** file_cluster_8: 12.259, file_cluster_13: 12.259, file_cluster_0: 12.49
- **Magnitude:** 215.2 | **LOC:** 165 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (47.9387%), Tech Debt (24.2989%)
**Top Internal Functions/Classes:**
  * `buildLlmsTxt` (Impact: 71.8 | O(N^4) | DB: 8)
  * `collectDocEntries` (Impact: 40.9 | O(2^N) | DB: 1)
  * `getDescription` (Impact: 32.5 | O(N^2))
  * `isAdvanced` (Impact: 15.9 | O(N^1))
    * *Intent:* /**
  * `buildUrlMap` (Impact: 11.1 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 16`, `args: 8`, `func_start: 10`
* *Risk/State:* `state_mutation: 30`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 3`
* *Defense:* `safety: 13`, `doc: 4`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fs, path, typedoc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/path.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.424 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.613 IQR)
- **Top Global Matches:** file_cluster_8: 12.424, file_cluster_0: 12.612, file_cluster_7: 12.653
- **Magnitude:** 202.06 | **LOC:** 940 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 368
- **Risk Profile:** Cognitive Load (50.2132%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isDataUrl` (Impact: 1575.2 | O(2^N) | DB: 368)
  * `normalizeStringPosix` (Impact: 223.4 | O(N^6) | DB: 24)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `assertPath` (Impact: 6.3 | O(N^2) | DB: 11)
  * `removeUrlParams` (Impact: 4.3 | O(N^1))
  * `escapeRegExp` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 40`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 190`, `dead_code: 1`
* *Architecture:* `io: 121`, `api: 2`, `import: 1`
* *Defense:* `safety: 5`, `doc: 40`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.167
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pixi.js, adapter
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `scripts/plugins/eslint-require-export.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.426 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.221 IQR)
- **Top Global Matches:** file_cluster_8: 10.426, file_cluster_0: 10.525, file_cluster_13: 10.943
- **Magnitude:** 155.62 | **LOC:** 132 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.0599%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 148.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 14`, `args: 8`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 19`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsdoccomment, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugins/typedoc-plugin-router.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.436 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.642 IQR)
- **Top Global Matches:** file_cluster_8: 8.436, file_cluster_7: 9.311, file_cluster_13: 9.44
- **Magnitude:** 155.44 | **LOC:** 160 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (18.9303%), Tech Debt (35.2958%)
**Top Internal Functions/Classes:**
  * `createNormalizedUrl` (Impact: 75.3 | O(N^4) | DB: 1)
  * `getIdealBaseName` (Impact: 44.3 | O(N^4) | DB: 3)
  * `isalpha` (Impact: 3.7 | O(N^1))
  * `isdigit` (Impact: 3.7 | O(N^1))
  * `isalnum` (Impact: 3.7 | O(N^1))
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

### `.stackblitz/bunny-mark/src/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.852 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.815 IQR)
- **Top Global Matches:** file_cluster_4: 10.852, file_cluster_8: 11.055, file_cluster_13: 11.343
- **Magnitude:** 148.98 | **LOC:** 195 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (97.8155%), Tech Debt (70.1334%)
**Top Internal Functions/Classes:**
  * `renderUpdate` (Impact: 29.8 | O(N^4) | DB: 7)
  * `init` (Impact: 9.6 | O(2^N) | DB: 7)
  * `onclick` (Impact: 8.1 | O(N^2))
  * `addBunnies` (Impact: 7.8 | O(N^4) | DB: 3)
  * `loadAssets` (Impact: 4.5 | O(N^3) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 14`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 1`, `concurrency: 32`, `import: 3`
* *Defense:* `safety: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pixi.js, Bunny, stats.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/events/EventBoundary.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.591 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.029 IQR)
- **Top Global Matches:** file_cluster_13: 13.591, file_cluster_0: 13.704, file_cluster_11: 13.769
- **Magnitude:** 139.33 | **LOC:** 1487 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (47.1686%), Tech Debt (9.129%)
**Top Internal Functions/Classes:**
  * `pruneFn` (Impact: 906.7 | O(2^N) | DB: 66)
  * `propagationPath` (Impact: 51.0 | O(2^N) | DB: 7)
  * `propagate` (Impact: 40.2 | O(N^3) | DB: 5)
    * *Intent:* /**
  * `mapEvent` (Impact: 31.1 | O(N^4) | DB: 3)
  * `all` (Impact: 25.9 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 89`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 276`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 10`, `import: 12`
* *Defense:* `safety: 28`, `doc: 77`, `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.729
  * `Choke Point (Betweenness):` 0.000273 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Point, pixi.js, eventemitter3, pixi-spatial-hash, FederatedPointerEvent, EventBoundaryTypes, FederatedMouseEvent, FederatedWheelEvent...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/GraphicsContext.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.599 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.685 IQR)
- **Top Global Matches:** file_cluster_13: 13.599, file_cluster_8: 13.952, file_cluster_7: 13.965
- **Magnitude:** 130.02 | **LOC:** 1285 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (46.8688%), Tech Debt (79.2797%)
**Top Internal Functions/Classes:**
  * `containsPoint` (Impact: 269.4 | O(2^N) | DB: 18)
  * `destroy` (Impact: 193.2 | O(2^N) | DB: 25)
  * `texture` (Impact: 159.9 | O(2^N) | DB: 5)
  * `fill` (Impact: 97.5 | O(2^N) | DB: 30)
    * *Intent:* /** * Sets the current stroke style of the graphics context. Similar to fill styles, stroke styles c...
  * `bezierCurveTo` (Impact: 23.6 | O(2^N) | DB: 3)
    * *Intent:* // #if _DEBUG
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 73`, `args: 35`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `state_mutation: 236`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 17`, `api: 50`, `import: 19`
* *Defense:* `safety: 9`, `doc: 169`, `immutability_locks: 30`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.313
  * `Choke Point (Betweenness):` 0.004529 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Color, eventemitter3, PointData, destroyTypes, roundShape, SVGParser, Bounds, GCSystem...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/scene/text/TextStyle.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.232 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.428 IQR)
- **Top Global Matches:** file_cluster_0: 13.232, file_cluster_13: 13.319, file_cluster_8: 13.43
- **Magnitude:** 115.21 | **LOC:** 1549 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (45.348%), Tech Debt (99.9928%)
**Top Internal Functions/Classes:**
  * `destroy` (Impact: 173.3 | O(2^N) | DB: 14)
  * `convertV7Tov8Style` (Impact: 152.9 | O(N^3) | DB: 1)
  * `dropShadow` (Impact: 30.1 | O(N^3) | DB: 6)
    * *Intent:* /** * The angle of the drop shadow in radians. * - 0 = right * - Math.PI/2 = down * - Math.PI = left...
  * `fill` (Impact: 25.1 | O(N^5) | DB: 9)
    * *Intent:* * // Create a basic text style * const style = new TextStyle({ * fontFamily: ['Helvetica', 'Arial', ...
  * `_isFillStyle` (Impact: 24.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 112`, `args: 66`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 398`, `duplicate_logic: 44`
* *Architecture:* `api: 37`, `import: 13`
* *Defense:* `safety: 35`, `doc: 90`, `immutability_locks: 33`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.287
  * `Choke Point (Betweenness):` 0.002042 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` FillGradient, pixi.js, eventemitter3, Filter, convertFillInputToFillStyle, warn, GraphicsContext, fontStringFromTextStyle...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `.stackblitz/bunny-mark/src/Bunny.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.049 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.979 IQR)
- **Top Global Matches:** file_cluster_8: 13.049, file_cluster_13: 13.127, file_cluster_7: 13.358
- **Magnitude:** 106.54 | **LOC:** 65 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (44.8592%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 30.2 | O(N^4) | DB: 23)
  * `destroy` (Impact: 4.5 | O(2^N) | DB: 1)
    * *Intent:* /**
  * `constructor` (Impact: 2.8 | O(N^2) | DB: 1)
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

### `src/scene/graphics/shared/path/GraphicsPath.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.227 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.877 IQR)
- **Top Global Matches:** file_cluster_13: 13.227, file_cluster_8: 13.348, file_cluster_7: 13.396
- **Magnitude:** 88.83 | **LOC:** 863 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (48.0917%), Tech Debt (9.907%)
**Top Internal Functions/Classes:**
  * `transform` (Impact: 330.0 | O(2^N) | DB: 12)
    * *Intent:* /** * Draws an ellipse at the specified location and with the given x and y radii. * An optional tra...
  * `getLastPoint` (Impact: 172.8 | O(2^N) | DB: 5)
  * `bezierCurveToShort` (Impact: 26.1 | O(N^3) | DB: 8)
    * *Intent:* /**
  * `quadraticCurveToShort` (Impact: 21.6 | O(N^3) | DB: 8)
  * `rect` (Impact: 15.1 | O(2^N) | DB: 3)
    * *Intent:* /** * Adds a cubic Bezier curve to the path. * It requires three points: the first two are control p...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 42`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 148`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 37`, `import: 9`
* *Defense:* `safety: 5`, `doc: 117`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.473
  * `Choke Point (Betweenness):` 0.000644 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` parseSVGPath, ShapePath, Bounds, uid, roundShape, Matrix, warn, PointData...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `scripts/plugins/eslint-require-tilde-imports.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.668 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.79 IQR)
- **Top Global Matches:** file_cluster_8: 8.668, file_cluster_7: 9.583, file_cluster_13: 9.604
- **Magnitude:** 87.72 | **LOC:** 101 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (13.4215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 84.1 | O(N^5) | DB: 24)
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
- **Global Archetype:** `file_cluster_13` (Drift: 14.607 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.133 IQR)
- **Top Global Matches:** file_cluster_13: 14.607, file_cluster_4: 14.648, file_cluster_8: 14.856
- **Magnitude:** 86.35 | **LOC:** 575 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (47.2361%), Tech Debt (58.8349%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 171.3 | O(2^N) | DB: 20)
  * `_configureAutoUpdate` (Impact: 70.2 | O(N^5) | DB: 16)
  * `_videoFrameRequestCallback` (Impact: 26.7 | O(2^N) | DB: 6)
  * `updateFrame` (Impact: 25.5 | O(N^3) | DB: 12)
  * `constructor` (Impact: 24.4 | O(N^3) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 35`, `args: 30`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 369`, `duplicate_logic: 4`
* *Architecture:* `api: 13`, `concurrency: 31`, `import: 8`
* *Defense:* `safety: 24`, `doc: 50`, `test: 1`, `immutability_locks: 11`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.439
  * `Choke Point (Betweenness):` 0.000163 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Extensions, Ticker, TextureSource, const, types, detectVideoAlphaMode
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/buildCommands/buildAdaptiveBezier.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.867 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.533 IQR)
- **Top Global Matches:** file_cluster_8: 11.867, file_cluster_13: 12.136, file_cluster_7: 12.144
- **Magnitude:** 84.74 | **LOC:** 257 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (30.7341%), Tech Debt (9.907%)
**Top Internal Functions/Classes:**
  * `recursive` (Impact: 761.1 | O(2^N) | DB: 17)
  * `buildAdaptiveBezier` (Impact: 21.9 | O(N^2) | DB: 1)
    * *Intent:* /**
  * `begin` (Impact: 4.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 15`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 55`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `doc: 11`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.589
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GraphicsContextSystem
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/rendering/renderers/gl/renderTarget/GlRenderTargetAdaptor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.63 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.443 IQR)
- **Top Global Matches:** file_cluster_13: 11.63, file_cluster_8: 11.752, file_cluster_17: 11.779
- **Magnitude:** 84.08 | **LOC:** 676 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (39.4219%), Tech Debt (9.1531%)
**Top Internal Functions/Classes:**
  * `startRenderPass` (Impact: 294.8 | O(N^6) | DB: 12)
  * `clear` (Impact: 187.7 | O(2^N) | DB: 3)
  * `_initColor` (Impact: 77.9 | O(N^5) | DB: 2)
  * `_resizeStencil` (Impact: 25.6 | O(N^5) | DB: 2)
  * `_resizeColor` (Impact: 18.6 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 38`, `args: 24`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 111`, `dead_code: 4`, `planned_debt: 2`
* *Architecture:* `api: 20`, `import: 12`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Texture, Color, RenderTargetSystem, const, RenderTarget, GlRenderTarget, CanvasSource, WebGLRenderer...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/scene/graphics/canvas/CanvasGraphicsAdaptor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.651 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.343 IQR)
- **Top Global Matches:** file_cluster_8: 10.651, file_cluster_13: 10.758, file_cluster_7: 11.226
- **Magnitude:** 74.55 | **LOC:** 529 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (28.7972%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `execute` (Impact: 454.7 | O(N^6) | DB: 8)
  * `buildShapePath` (Impact: 99.1 | O(N^4) | DB: 1)
  * `getCanvasStyle` (Impact: 90.6 | O(N^5))
  * `addHolePaths` (Impact: 39.6 | O(N^3) | DB: 1)
  * `fillTriangles` (Impact: 7.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 45`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `io: 2`, `api: 9`, `import: 21`
* *Defense:* `safety: 26`, `doc: 2`, `immutability_locks: 81`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.312
  * `Choke Point (Betweenness):` 0.001836 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` Extensions, Graphics, CanvasRenderer, CanvasContextSystem, multiplyHexColors, generateTextureFillMatrix, ShapePath, GraphicsPipe...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/CanvasTextGenerator.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.632 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.665 IQR)
- **Top Global Matches:** file_cluster_13: 12.632, file_cluster_8: 12.737, file_cluster_7: 12.961
- **Magnitude:** 73.9 | **LOC:** 785 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (25.9853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_renderTextToCanvas` (Impact: 300.0 | O(N^6) | DB: 14)
    * *Intent:* /** * Utility for generating and managing canvas-based text rendering. * * This class is responsible...
  * `_renderTaggedTextToCanvas` (Impact: 292.4 | O(N^6) | DB: 15)
  * `_setFillAndStrokeStyles` (Impact: 29.4 | O(N^4))
  * `countSpaces` (Impact: 9.6 | O(N^2) | DB: 2)
    * *Intent:* /** * Temporary rectangle for getting the bounding box of the text. * @internal
  * `returnCanvasAndContext` (Impact: 6.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 13`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 87`, `dead_code: 2`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 19`, `doc: 29`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.465
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` pixi.js, CanvasTextMetrics, Rectangle, getCanvasBoundingBox, CanvasPool, Color, getCanvasFillStyle, fontStringFromTextStyle...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/buildCommands/buildLine.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.397 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.737 IQR)
- **Top Global Matches:** file_cluster_8: 12.397, file_cluster_13: 12.628, file_cluster_7: 12.633
- **Magnitude:** 73.41 | **LOC:** 555 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (33.1048%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildLine` (Impact: 454.8 | O(N^6) | DB: 50)
  * `round` (Impact: 82.5 | O(N^4) | DB: 17)
  * `square` (Impact: 15.7 | O(N^2) | DB: 4)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 171`, `dead_code: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 1`, `doc: 27`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.328
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` const, FillTypes, Point, getOrientationOfPoints
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/assets/resolver/Resolver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.799 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.771 IQR)
- **Top Global Matches:** file_cluster_0: 12.799, file_cluster_17: 12.907, file_cluster_13: 12.91
- **Magnitude:** 70.92 | **LOC:** 881 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (29.663%), Tech Debt (26.422%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 194.2 | O(N^6) | DB: 11)
  * `resolve` (Impact: 58.7 | O(N^6) | DB: 9)
  * `getAlias` (Impact: 45.9 | O(N^4))
    * *Intent:* /**
  * `addBundle` (Impact: 39.2 | O(N^5) | DB: 8)
    * *Intent:* /** * Set the base path to prepend to all urls when resolving * @example
  * `resolveBundle` (Impact: 25.6 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 79`, `args: 55`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 177`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 23`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 34`, `doc: 48`, `immutability_locks: 39`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.3
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` warn, types, createStringVariations, types, path, convertToList, isSingleItem
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/utils/measureTaggedText.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.527 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.961 IQR)
- **Top Global Matches:** file_cluster_8: 11.527, file_cluster_13: 11.771, file_cluster_7: 11.796
- **Magnitude:** 68.06 | **LOC:** 633 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (20.075%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wordWrapTaggedLines` (Impact: 518.3 | O(N^6) | DB: 17)
  * `measureTaggedText` (Impact: 90.5 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 25`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `state_mutation: 62`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 6`, `doc: 34`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.374
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ICanvasRenderingContext2D, parseTaggedText, types, TextStyle, textTokenization
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/scene/sprite-animated/AnimatedSprite.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.187 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.662 IQR)
- **Top Global Matches:** file_cluster_0: 14.187, file_cluster_13: 14.203, file_cluster_11: 14.386
- **Magnitude:** 66.13 | **LOC:** 1086 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (35.924%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 354.9 | O(2^N) | DB: 48)
    * *Intent:* /** * User-assigned function to call when `loop` is true, * and an AnimatedSprite is played and loop...
  * `constructor` (Impact: 37.4 | O(N^4) | DB: 16)
    * *Intent:* /** * The speed that the AnimatedSprite will play at. Higher is faster, lower is slower. * @example ...
  * `stop` (Impact: 14.6 | O(N^3) | DB: 6)
    * *Intent:* /** * Whether or not the animation repeats after playing. * @default true */
  * `play` (Impact: 14.6 | O(N^3) | DB: 7)
    * *Intent:* /** * User-assigned function to call when an AnimatedSprite finishes playing. * @example * ```ts * a...
  * `gotoAndStop` (Impact: 3.2 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 27`, `args: 19`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 215`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `safety: 12`, `doc: 38`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pixi.js, destroyTypes, Texture, Sprite, const, Ticker
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/accessibility/AccessibilitySystem.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.954 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.148 IQR)
- **Top Global Matches:** file_cluster_13: 13.954, file_cluster_8: 14.214, file_cluster_7: 14.289
- **Magnitude:** 66.06 | **LOC:** 913 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (33.812%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `postrender` (Impact: 105.3 | O(N^5) | DB: 40)
  * `_updateAccessibleObjects` (Impact: 71.4 | O(2^N) | DB: 4)
  * `_deactivate` (Impact: 59.8 | O(N^5) | DB: 16)
  * `_activate` (Impact: 44.8 | O(N^5) | DB: 21)
  * `init` (Impact: 26.1 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 44`, `args: 25`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `state_mutation: 287`
* *Architecture:* `api: 14`, `import: 11`
* *Defense:* `safety: 21`, `doc: 58`, `immutability_locks: 25`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.81
  * `Choke Point (Betweenness):` 0.004216 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` pixi.js, Extensions, FederatedEvent, removeItems, isMobile, CanvasObserver, Container, System...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/color/Color.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.208 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.836 IQR)
- **Top Global Matches:** file_cluster_8: 13.208, file_cluster_13: 13.221, file_cluster_7: 13.287
- **Magnitude:** 65.79 | **LOC:** 1195 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (36.6286%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extend` (Impact: 446.1 | O(N^5) | DB: 83)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 55`, `args: 34`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 183`
* *Architecture:* `api: 21`, `import: 3`
* *Defense:* `safety: 4`, `doc: 78`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.206
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pixi.js, colord, names
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/assets/utils/__tests__/createStringVariations.test.ts` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, decorators: 11, args: 5, func_start: 5
- `src/rendering/high-shader/compiler/utils/compileInputs.ts` (TYPESCRIPT) | Magnitude: 3.8 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 16, args: 6, structural_boundaries: 4
- `src/scene/sprite-animated/AnimatedSprite.ts` (TYPESCRIPT) | Magnitude: 66.13 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 215, indent_spaces: 209, branch: 52, doc: 38
- `src/rendering/high-shader/shader-bits/generateTextureBatchBit.ts` (TYPESCRIPT) | Magnitude: 21.03 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 70, branch: 21, structural_boundaries: 15
- `src/ticker/Ticker.ts` (TYPESCRIPT) | Magnitude: 6.99 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 19, doc: 10, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/environment/ImageLike.ts` (TYPESCRIPT) | Magnitude: 3.11 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, doc: 9, structural_boundaries: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `transcoders/basis/basis_transcoder.js` (JAVASCRIPT) | Magnitude: 4158.58 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 945, state_mutation: 777, branch: 521, structural_boundaries: 382
- `src/utils/pool/Pool.ts` (TYPESCRIPT) | Magnitude: 6.52 | Delta: **0.202 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 30, structural_boundaries: 13, doc: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/visual/scenes/sprite/sprite-trim.scene.ts` (TYPESCRIPT) | Magnitude: 1.45 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, concurrency: 7, immutability_locks: 5
- `src/scene/graphics/shared/buildCommands/buildPixelLine.ts` (TYPESCRIPT) | Magnitude: 4.87 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 18, immutability_locks: 10, branch: 6
- `scripts/index/index.mts` (TYPESCRIPT) | Magnitude: 1.53 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 8, io: 5, structural_boundaries: 4, import: 3
- `src/scene/text/utils/getPo2TextureFromSource.ts` (TYPESCRIPT) | Magnitude: 1.24 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 12, doc: 7, decorators: 7
- `src/spritesheet/Spritesheet.ts` (TYPESCRIPT) | Magnitude: 44.33 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 251, state_mutation: 193, doc: 49, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/math-extras/pointExtras.ts` (TYPESCRIPT) | Magnitude: 14.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, state_mutation: 66, structural_boundaries: 24, branch: 17
- `src/rendering/renderers/gl/state/mapWebGLBlendModesToPixi.ts` (TYPESCRIPT) | Magnitude: 2.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 7, generics: 6, ui_framework: 4
- `src/assets/AssetExtension.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, generics: 11, indent_spaces: 11, doc: 8
- `src/scene/container/utils/assignWithIgnore.ts` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, doc: 4, branch: 3, structural_boundaries: 2
- `src/rendering/renderers/shared/texture/sources/CubeTextureSource.ts` (TYPESCRIPT) | Magnitude: 16.69 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, immutability_locks: 22, branch: 16, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/test.mts` (TYPESCRIPT) | Magnitude: 9.32 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 81, branch: 29, immutability_locks: 25, structural_boundaries: 19
- `src/assets/loader/parsers/loadWebFont.ts` (TYPESCRIPT) | Magnitude: 22.94 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 31, branch: 20, immutability_locks: 16
- `src/utils/pool/GlobalResourceRegistry.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, doc: 14, args: 8, state_mutation: 8
- `src/extensions/Extensions.ts` (TYPESCRIPT) | Magnitude: 27.86 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 73, doc: 72, state_mutation: 44
- `src/spritesheet/spritesheetAsset.ts` (TYPESCRIPT) | Magnitude: 13.69 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 42, branch: 32, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `playground/src/hooks/useIframeScene.ts` (TYPESCRIPT) | Magnitude: 5.88 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 17, args: 14, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/visual/scenes/container/root-container-visibility.scene.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, concurrency: 7, import: 4
- `examples/sprite_svg.ts` (TYPESCRIPT) | Magnitude: 2.24 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, state_mutation: 4, immutability_locks: 4
- `examples/container_tinting.ts` (TYPESCRIPT) | Magnitude: 4.0 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, scientific: 18, state_mutation: 16, branch: 8
- `examples/rendering_render-texture_basic.ts` (TYPESCRIPT) | Magnitude: 2.76 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, concurrency: 8, immutability_locks: 6, structural_boundaries: 5
- `src/rendering/renderers/gpu/GpuDeviceSystem.ts` (TYPESCRIPT) | Magnitude: 9.42 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, concurrency: 28, structural_boundaries: 23, state_mutation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scripts/plugins/typedoc-plugin-llms-txt.mjs` (JAVASCRIPT) | Magnitude: 215.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, branch: 43, state_mutation: 30, immutability_locks: 21
- `tests/visual/scenes/text-bitmap/bitmap-text-stroke-alpha.scene.ts` (TYPESCRIPT) | Magnitude: 0.93 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, immutability_locks: 4, import: 3
- `src/compressed-textures/__tests__/CompressedTextures.test.ts` (TYPESCRIPT) | Magnitude: 4.95 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 93, concurrency: 27, structural_boundaries: 20, args: 20
- `src/events/FederatedWheelEvent.ts` (TYPESCRIPT) | Magnitude: 2.63 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: api: 11, doc: 11, indent_spaces: 10, immutability_locks: 6
- `src/utils/logging/logScene.ts` (TYPESCRIPT) | Magnitude: 3.67 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, state_mutation: 27, branch: 11, doc: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/scene/container/__tests__/Container.Culling.test.ts` (TYPESCRIPT) | Magnitude: 0.52 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 4, args: 3, func_start: 3, test: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/rendering/mask/stencil/CanvasStencilMaskPipe.ts` -> Churn: **55.79%** | Cog Load: 76.2527% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/plugins/typedoc-plugin-stackblitz.mjs` -> **Zyie** (100.0% isolated ownership) | Magnitude: 226.04
- `scripts/plugins/typedoc-plugin-llms-txt.mjs` -> **Zyie** (100.0% isolated ownership) | Magnitude: 215.2
- `src/scene/graphics/shared/GraphicsContext.ts` -> **Mat Groves** (100.0% isolated ownership) | Magnitude: 130.02
- `src/scene/text/TextStyle.ts` -> **Zyie** (100.0% isolated ownership) | Magnitude: 115.21
- `scripts/plugins/eslint-require-tilde-imports.mjs` -> **Zyie** (100.0% isolated ownership) | Magnitude: 87.72

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

- `src/rendering/renderers/shared/texture/sources/TextureSource.ts` -> **Severity: 770.897** (Blast Radius: 9.62 * Doc Risk: 80.1348%)
- `src/scene/view/ViewContainer.ts` -> **Severity: 770.6** (Blast Radius: 7.706 * Doc Risk: 100.0%)
- `src/ticker/TickerListener.ts` -> **Severity: 686.647** (Blast Radius: 6.872 * Doc Risk: 99.9195%)
- `src/rendering/renderers/gpu/shader/BindGroup.ts` -> **Severity: 641.5** (Blast Radius: 6.415 * Doc Risk: 100.0%)
- `src/utils/logging/deprecation.ts` -> **Severity: 476.677** (Blast Radius: 7.065 * Doc Risk: 67.4702%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
