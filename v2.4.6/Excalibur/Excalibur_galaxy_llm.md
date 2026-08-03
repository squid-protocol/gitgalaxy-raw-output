# ARCHITECTURAL_BRIEF: Excalibur
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/Excalibur` |
| **Timestamp** | `2026-08-03T19:49:05.480071+00:00` |
| **Scan Duration** | `2.59s` |
| **Git Branch** | `main` |
| **Git Commit** | `3aa48c717952d2a01339eee72acc8036d087137a` |
| **Git Remote** | `https://github.com/excaliburjs/Excalibur.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 577 malicious artifacts.

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
| Total Artifacts | 1797 |
| Analyzed Artifacts (Scanned) | 736 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1061 |
| Total LOC | 73444 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 41.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5361 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2755 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 19.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3249 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 19 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 546 | 64122 | 74.2% |
| HTML | 119 | 1816 | 16.2% |
| JSON | 19 | 604 | 2.6% |
| GLSL | 19 | 459 | 2.6% |
| JAVASCRIPT | 10 | 5951 | 1.4% |
| PLAINTEXT | 8 | 1 | 1.1% |
| MARKDOWN | 6 | 0 | 0.8% |
| CSS | 4 | 434 | 0.5% |
| XML | 3 | 0 | 0.4% |
| PYTHON | 2 | 57 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.815`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 476 | 64.7% |
| file_cluster_13 | 187 | 25.4% |
| file_cluster_4 | 25 | 3.4% |
| file_cluster_16 | 11 | 1.5% |
| file_cluster_2 | 7 | 1.0% |
| file_cluster_0 | 6 | 0.8% |
| file_cluster_17 | 5 | 0.7% |
| file_cluster_1 | 2 | 0.3% |
| file_cluster_11 | 2 | 0.3% |
| Unknown | 1 | 0.1% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1061*

**Composition by Extension & Reason:**
- `.png`: 597x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 73x Excluded (Explicitly Denied Extension: '.gif')
- `.ts`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.md`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3214 LOC)
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14105 LOC), 1x Excluded (Static Asset Blob without Intent: 2081 LOC)
- `.mp3`: 18x Excluded (Explicitly Denied Extension: '.mp3')
- `.jpg`: 13x Excluded (Explicitly Denied Extension: '.jpg')
- `.mp4`: 12x Excluded (Explicitly Denied Extension: '.mp4')
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 9x Excluded (Explicitly Denied Extension: '.woff2')
- `.svg`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 20.2 | 7.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 44.0 | 43.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.6 | 4.6 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 28.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 68.0 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.7 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 27.3 | 1.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.7 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 21.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sandbox/index.html` (Hits: 132)
- `src/spec/vitest/graph-spec.ts` (Hits: 25)
- `playground/index.html` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vector.ts** (`src/engine/math/vector.ts`) — 96 inbound connections
2. **color.ts** (`src/engine/color.ts`) — 47 inbound connections
3. **test-utils.ts** (`src/spec/__util__/test-utils.ts`) — 45 inbound connections
4. **engine.ts** (`src/engine/engine.ts`) — 41 inbound connections
5. **log.ts** (`src/engine/util/log.ts`) — 41 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/engine/index.ts`) — 67 outbound dependencies
2. **index.ts** (`src/engine/graphics/index.ts`) — 46 outbound dependencies
3. **index.ts** (`src/engine/collision/index.ts`) — 37 outbound dependencies
4. **engine.ts** (`src/engine/engine.ts`) — 37 outbound dependencies
5. **excalibur-graphics-context-webgl.ts** (`src/engine/graphics/context/excalibur-graphics-context-webgl.ts`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `rayCast` (@ `src/engine/collision/detection/sparse-hash-grid-collision-processor.ts`) -> Impact: **404.3** | LOC: 119
- `describe` (@ `src/spec/vitest/engine-spec.ts`) -> Impact: **270.2** | LOC: 1073
- `draw` (@ `src/engine/graphics/context/material-renderer/material-renderer.ts`) -> Impact: **254.6** | LOC: 158
- `describe` (@ `src/spec/vitest/text-spec.ts`) -> Impact: **254.0** | LOC: 1061
- `coroutine` (@ `src/engine/util/coroutine.ts`) -> Impact: **246.4** | LOC: 129
  * *Intent:* /** * Excalibur coroutine helper, returns a [[CoroutineInstance]] which is promise-like when complete. Coroutines run before frame update by default. ...
- `_createColliderFromData` (@ `src/engine/collision/collider-component.ts`) -> Impact: **223.5** | LOC: 30
- `describe` (@ `src/spec/vitest/action-spec.ts`) -> Impact: **201.1** | LOC: 1632
- `describe` (@ `src/spec/vitest/excalibur-graphics-context-spec.ts`) -> Impact: **200.9** | LOC: 1109
- `rayCast` (@ `src/engine/collision/detection/dynamic-tree-collision-processor.ts`) -> Impact: **182.3** | LOC: 44
- `constructor` (@ `src/engine/actor.ts`) -> Impact: **168.8** | LOC: 120
  * *Intent:* /**

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `add` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `shouldneverhappen` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `title` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `title` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `remove` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `function` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `add` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `add` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `add` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**
- `addInput` (@ `sandbox/excalibur-dev-tools/dev-tools.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `applyResolutionAndViewport` (@ `src/engine/screen.ts`) -> DB Complexity: **162**
- `draw` (@ `src/engine/graphics/context/image-renderer/image-renderer.ts`) -> DB Complexity: **132**
- `_initialize` (@ `src/engine/graphics/nine-slice.ts`) -> DB Complexity: **122**
- `updatePhysicsConfig` (@ `src/engine/collision/body-component.ts`) -> DB Complexity: **117**
- `_drawImage` (@ `src/engine/graphics/nine-slice.ts`) -> DB Complexity: **94**
- `drawLine` (@ `src/engine/graphics/context/rectangle-renderer/rectangle-renderer.ts`) -> DB Complexity: **88**
- `describe` (@ `src/spec/vitest/graph-spec.ts`) -> DB Complexity: **76**
- `drawRectangle` (@ `src/engine/graphics/context/rectangle-renderer/rectangle-renderer.ts`) -> DB Complexity: **75**
- `draw` (@ `src/engine/graphics/context/debug-circle-renderer/debug-circle-renderer.ts`) -> DB Complexity: **71**
- `draw` (@ `src/engine/graphics/context/circle-renderer/circle-renderer.ts`) -> DB Complexity: **67**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sandbox/excalibur-dev-tools` | 2 | 5975.72 | 48.33% | 50.0% |
| `__monolith__` | 16 | 5144.21 | 7.67% | 4.96% |
| `src/engine/graphics` | 33 | 668.77 | 37.55% | 25.15% |
| `src/spec/vitest` | 127 | 663.65 | 4.56% | 0.0% |
| `src/engine/graphics/context` | 19 | 509.89 | 39.16% | 34.16% |
| `src/engine` | 24 | 504.63 | 27.57% | 29.31% |
| `src/engine/actions/action` | 22 | 375.2 | 54.74% | 27.27% |
| `src/engine/math` | 19 | 332.96 | 33.86% | 26.33% |
| `src/engine/collision/detection` | 11 | 319.64 | 28.87% | 29.47% |
| `src/engine/util` | 28 | 262.32 | 32.1% | 10.55% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **100.0%** Exposure
- `sandbox/tests/bezier/index.ts` -> **100.0%** Exposure
- `sandbox/tests/coordinates/coordinates.ts` -> **100.0%** Exposure
- `sandbox/tests/engine/timescale.ts` -> **100.0%** Exposure
- `sandbox/tests/fitscreen/fitscreen.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **100.0%** Exposure
- `sandbox/tests/screen/screen.ts` -> **100.0%** Exposure
- `src/engine/actor.ts` -> **100.0%** Exposure
- `src/engine/camera.ts` -> **100.0%** Exposure
- `src/engine/collision/body-component.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **0** Orphaned Functions | **152** Duplicates
- `src/engine/events.ts` -> **0** Orphaned Functions | **43** Duplicates
- `src/engine/tile-map/tile-map.ts` -> **0** Orphaned Functions | **31** Duplicates
- `src/engine/math/transform.ts` -> **0** Orphaned Functions | **22** Duplicates
- `src/engine/entity-component-system/components/transform-component.ts` -> **0** Orphaned Functions | **18** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/engine/graphics/font-text-instance.ts`** -> AI Confidence: **99.48%**
2. **`src/engine/graphics/context/material-renderer/material-renderer.ts`** -> AI Confidence: **99.39%**
3. **`src/engine/graphics/font.ts`** -> AI Confidence: **99.39%**
4. **`src/engine/particles/particles.ts`** -> AI Confidence: **99.39%**
5. **`src/engine/particles/particle-emitter.ts`** -> AI Confidence: **99.34%**
6. **`scripts/apidocs.js`** -> AI Confidence: **99.32%**
7. **`playground/src/main.ts`** -> AI Confidence: **99.31%**
8. **`src/engine/actor.ts`** -> AI Confidence: **99.31%**
9. **`src/engine/collision/bounding-box.ts`** -> AI Confidence: **99.31%**
10. **`src/engine/collision/collider-component.ts`** -> AI Confidence: **99.31%**
11. **`src/engine/collision/colliders/circle-collider.ts`** -> AI Confidence: **99.31%**
12. **`src/engine/collision/colliders/collision-jump-table.ts`** -> AI Confidence: **99.31%**
13. **`src/engine/collision/colliders/composite-collider.ts`** -> AI Confidence: **99.31%**
14. **`src/engine/collision/colliders/polygon-collider.ts`** -> AI Confidence: **99.31%**
15. **`src/engine/collision/detection/dynamic-tree-collision-processor.ts`** -> AI Confidence: **99.31%**
16. **`src/engine/collision/detection/dynamic-tree.ts`** -> AI Confidence: **99.31%**
17. **`src/engine/collision/detection/sparse-hash-grid-collision-processor.ts`** -> AI Confidence: **99.31%**
18. **`src/engine/collision/motion-system.ts`** -> AI Confidence: **99.31%**
19. **`src/engine/collision/solver/arcade-solver.ts`** -> AI Confidence: **99.31%**
20. **`src/engine/collision/solver/realistic-solver.ts`** -> AI Confidence: **99.31%**
21. **`src/engine/director/loader.ts`** -> AI Confidence: **99.31%**
22. **`src/engine/director/transition.ts`** -> AI Confidence: **99.31%**
23. **`src/engine/graphics/context/excalibur-graphics-context-2d-canvas.ts`** -> AI Confidence: **99.31%**
24. **`src/engine/graphics/context/excalibur-graphics-context-webgl.ts`** -> AI Confidence: **99.31%**
25. **`src/engine/graphics/context/image-renderer-v2/image-renderer-v2.ts`** -> AI Confidence: **99.31%**
26. **`src/engine/graphics/context/image-renderer/image-renderer.ts`** -> AI Confidence: **99.31%**
27. **`src/engine/graphics/context/material.ts`** -> AI Confidence: **99.31%**
28. **`src/engine/graphics/context/particle-renderer/particle-renderer.ts`** -> AI Confidence: **99.31%**
29. **`src/engine/graphics/graphics-component.ts`** -> AI Confidence: **99.31%**
30. **`src/engine/graphics/graphics-system.ts`** -> AI Confidence: **99.31%**
31. **`src/engine/graphics/image-source.ts`** -> AI Confidence: **99.31%**
32. **`src/engine/graphics/sprite-font.ts`** -> AI Confidence: **99.31%**
33. **`src/engine/input/pointer-event-receiver.ts`** -> AI Confidence: **99.31%**
34. **`src/engine/label.ts`** -> AI Confidence: **99.31%**
35. **`src/engine/particles/gpu-particle-emitter.ts`** -> AI Confidence: **99.31%**
36. **`src/engine/particles/gpu-particle-renderer.ts`** -> AI Confidence: **99.31%**
37. **`src/engine/resources/sound/sound.ts`** -> AI Confidence: **99.31%**
38. **`src/engine/screen.ts`** -> AI Confidence: **99.31%**
39. **`src/engine/tile-map/isometric-map.ts`** -> AI Confidence: **99.31%**
40. **`src/engine/tile-map/tile-map.ts`** -> AI Confidence: **99.31%**
41. **`src/engine/actions/action-context.ts`** -> AI Confidence: **99.24%**
42. **`src/engine/actions/action/move-by.ts`** -> AI Confidence: **99.24%**
43. **`src/engine/collision/body-component.ts`** -> AI Confidence: **99.24%**
44. **`src/engine/entity-component-system/entity.ts`** -> AI Confidence: **99.24%**
45. **`src/engine/graphics/context/excalibur-graphics-context.ts`** -> AI Confidence: **99.24%**
46. **`src/engine/util/serializer.ts`** -> AI Confidence: **99.24%**
47. **`src/engine/collision/colliders/closest-line-jump-table.ts`** -> AI Confidence: **99.23%**
48. **`src/engine/collision/colliders/separating-axis.ts`** -> AI Confidence: **99.23%**
49. **`src/engine/collision/physics-config.ts`** -> AI Confidence: **99.23%**
50. **`src/engine/director/director.ts`** -> AI Confidence: **99.23%**
51. **`src/engine/graphics/context/debug-text.ts`** -> AI Confidence: **99.23%**
52. **`src/engine/input/pointer-system.ts`** -> AI Confidence: **99.23%**
53. **`src/engine/actions/actions-component.ts`** -> AI Confidence: **99.18%**
54. **`src/engine/camera.ts`** -> AI Confidence: **99.18%**
55. **`src/engine/collision/collision-system.ts`** -> AI Confidence: **99.18%**
56. **`src/engine/collision/physics-world.ts`** -> AI Confidence: **99.18%**
57. **`src/engine/entity-component-system/components/transform-component.ts`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **100.0%** Exposure
- `wallaby.js` -> **100.0%** Exposure
- `sandbox/tests/ecs/index.ts` -> **100.0%** Exposure
- `sandbox/tests/high-gravity-arcade/index.ts` -> **100.0%** Exposure
- `src/engine/actions/action/flash.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `sandbox/tests/scenepredraw/index.ts` -> **100.0%** Exposure
- `src/engine/actions/actions-system.ts` -> **100.0%** Exposure
- `src/engine/collision/detection/dynamic-tree-collision-processor.ts` -> **100.0%** Exposure
- `src/engine/collision/motion-system.ts` -> **100.0%** Exposure
- `src/engine/graphics/graphics-system.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **100.0%** Exposure
- `wallaby.js` -> **100.0%** Exposure
- `sandbox/tests/high-gravity-arcade/index.ts` -> **100.0%** Exposure
- `sandbox/tests/input/gamepad.ts` -> **100.0%** Exposure
- `sandbox/vite.config.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `280` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/engine/tile-map/tile-map.ts` (TYPESCRIPT) -> Cumulative Risk: **951.24**
- **Archetype:** `file_cluster_13` (Distance: 15.135 IQR)
- **Magnitude:** 147.36 | **LOC:** 1004 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `_updateColliders` (Impact: 91.6), `debug` (Impact: 86.0), `constructor` (Impact: 45.3)

### 2. `src/engine/resources/sound/sound.ts` (TYPESCRIPT) -> Cumulative Risk: **949.12**
- **Archetype:** `file_cluster_4` (Distance: 15.099 IQR)
- **Magnitude:** 92.62 | **LOC:** 555 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 65.4), `play` (Impact: 60.3), `load` (Impact: 28.5)

### 3. `sandbox/excalibur-dev-tools/dev-tools.js` (JAVASCRIPT) -> Cumulative Risk: **878.61**
- **Archetype:** `file_cluster_17` (Distance: 14.777 IQR)
- **Magnitude:** 5970.84 | **LOC:** 5255 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_processPointerToEntity` (Impact: 110.2), `S` (Impact: 86.7), `add` (Impact: 42.2)

### 4. `src/engine/util/state-machine.ts` (TYPESCRIPT) -> Cumulative Risk: **858.68**
- **Archetype:** `file_cluster_2` (Distance: 12.915 IQR)
- **Magnitude:** 13.65 | **LOC:** 115 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.5354%)
- **Heaviest Functions:** `go` (Impact: 35.0), `create` (Impact: 17.4), `update` (Impact: 3.7)

### 5. `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` (TYPESCRIPT) -> Cumulative Risk: **847.7**
- **Archetype:** `file_cluster_13` (Distance: 14.144 IQR)
- **Magnitude:** 126.97 | **LOC:** 861 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `flush` (Impact: 152.8), `drawImage` (Impact: 101.6), `constructor` (Impact: 75.7)

### 6. `src/engine/director/default-loader.ts` (TYPESCRIPT) -> Cumulative Risk: **843.03**
- **Archetype:** `file_cluster_4` (Distance: 13.955 IQR)
- **Magnitude:** 38.05 | **LOC:** 288 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `load` (Impact: 50.6), `isLoaderConstructor` (Impact: 12.2), `constructor` (Impact: 8.9)

### 7. `src/engine/input/pointer-system.ts` (TYPESCRIPT) -> Cumulative Risk: **841.2**
- **Archetype:** `file_cluster_13` (Distance: 13.591 IQR)
- **Magnitude:** 30.15 | **LOC:** 169 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `update` (Impact: 78.2), `constructor` (Impact: 34.5), `preupdate` (Impact: 11.2)

### 8. `src/engine/actions/action/rotate-to.ts` (TYPESCRIPT) -> Cumulative Risk: **840.0**
- **Archetype:** `file_cluster_13` (Distance: 14.075 IQR)
- **Magnitude:** 41.3 | **LOC:** 197 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9996%)
- **Heaviest Functions:** `update` (Impact: 91.1), `update` (Impact: 7.9), `constructor` (Impact: 7.6)

### 9. `src/engine/actions/action/rotate-by.ts` (TYPESCRIPT) -> Cumulative Risk: **839.09**
- **Archetype:** `file_cluster_13` (Distance: 14.106 IQR)
- **Magnitude:** 42.88 | **LOC:** 204 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9993%)
- **Heaviest Functions:** `update` (Impact: 91.2), `update` (Impact: 7.9), `constructor` (Impact: 7.6)

### 10. `src/engine/collision/detection/dynamic-tree-collision-processor.ts` (TYPESCRIPT) -> Cumulative Risk: **836.82**
- **Archetype:** `file_cluster_13` (Distance: 13.453 IQR)
- **Magnitude:** 63.49 | **LOC:** 323 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `rayCast` (Impact: 182.3), `broadphase` (Impact: 130.3), `untrack` (Impact: 43.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sandbox/excalibur-dev-tools/dev-tools.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.777 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.849 IQR)
- **Top Global Matches:** file_cluster_17: 14.777, file_cluster_8: 14.819, file_cluster_11: 14.868
- **Magnitude:** 5970.84 | **LOC:** 5255 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (94.6385%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_processPointerToEntity` (Impact: 110.2 | O(N^6) | DB: 8)
  * `S` (Impact: 86.7 | O(N^6) | DB: 2)
  * `add` (Impact: 42.2 | O(2^N) | DB: 12)
  * `onSetAdd_` (Impact: 39.4 | O(N^5) | DB: 11)
  * `onSetRemove_` (Impact: 39.1 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 823`, `structural_boundaries: 1051`, `args: 981`, `func_start: 806`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 212`, `high_risk_execution: 1`, `state_mutation: 3562`, `duplicate_logic: 152`
* *Architecture:* `io: 9`, `api: 5`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 353`, `test: 2`, `immutability_locks: 490`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/tile-map/tile-map.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.135 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.971 IQR)
- **Top Global Matches:** file_cluster_13: 15.135, file_cluster_11: 15.443, file_cluster_2: 15.466
- **Magnitude:** 147.36 | **LOC:** 1004 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (47.7508%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_updateColliders` (Impact: 91.6 | O(N^3) | DB: 30)
  * `debug` (Impact: 86.0 | O(2^N) | DB: 28)
  * `constructor` (Impact: 45.3 | O(N^3) | DB: 64)
  * `update` (Impact: 32.5 | O(N^3) | DB: 19)
  * `scale` (Impact: 27.3 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 120`, `args: 67`, `func_start: 79`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 735`, `planned_debt: 1`, `duplicate_logic: 31`
* *Architecture:* `api: 103`, `concurrency: 33`, `import: 29`
* *Defense:* `safety: 46`, `doc: 51`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.366
  * `Choke Point (Betweenness):` 0.006009 | `Ripple Effect (Closeness):` 0.08637
  * `Imports (Out-Degree: 22):` body-component, transform-component, collider, collider-component, util, log, vector, composite-collider...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.144 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.364 IQR)
- **Top Global Matches:** file_cluster_13: 14.144, file_cluster_11: 14.48, file_cluster_17: 14.575
- **Magnitude:** 126.97 | **LOC:** 861 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (65.0587%), Tech Debt (99.8058%)
**Top Internal Functions/Classes:**
  * `flush` (Impact: 152.8 | O(2^N) | DB: 57)
  * `drawImage` (Impact: 101.6 | O(N^2) | DB: 9)
  * `constructor` (Impact: 75.7 | O(N^2) | DB: 32)
  * `draw` (Impact: 39.0 | O(2^N) | DB: 20)
  * `updatePostProcessors` (Impact: 19.1 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 105`, `args: 68`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 574`, `fragile_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 70`, `import: 35`
* *Defense:* `safety: 37`, `doc: 25`, `immutability_locks: 30`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.945
  * `Choke Point (Betweenness):` 0.012392 | `Ripple Effect (Closeness):` 0.065721
  * `Imports (Out-Degree: 31):` screen, debug-point-renderer, flags, material-renderer, image-renderer, screen-pass-painter, draw-call, particle-renderer...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/engine/screen.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.066 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.726 IQR)
- **Top Global Matches:** file_cluster_13: 14.066, file_cluster_11: 14.306, file_cluster_8: 14.341
- **Magnitude:** 97.02 | **LOC:** 1232 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 162
- **Risk Profile:** Cognitive Load (44.1153%), Tech Debt (54.0982%)
**Top Internal Functions/Classes:**
  * `applyResolutionAndViewport` (Impact: 127.9 | O(N^3) | DB: 162)
  * `parent` (Impact: 24.6 | O(N^2) | DB: 2)
  * `constructor` (Impact: 16.5 | O(N^1) | DB: 19)
    * *Intent:* /** * Canvas element to build a screen on
  * `dispose` (Impact: 14.0 | O(N^2) | DB: 18)
  * `_listenForPixelRatio` (Impact: 9.4 | O(N^1) | DB: 11)
    * *Intent:* /** * Optionally set the image rendering CSS hint on the canvas element, default is auto */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 81`, `args: 53`, `func_start: 52`, `class_start: 7`
* *Risk/State:* `state_mutation: 609`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 63`, `import: 10`
* *Defense:* `safety: 15`, `doc: 35`, `immutability_locks: 28`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` event-emitter, util, excalibur-graphics-context-webgl, camera, browser, log, vector, excalibur-graphics-context-2d-canvas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/resources/sound/sound.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.099 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.19 IQR)
- **Top Global Matches:** file_cluster_4: 15.099, file_cluster_13: 15.317, file_cluster_17: 15.468
- **Magnitude:** 92.62 | **LOC:** 555 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (49.9928%), Tech Debt (99.7808%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 65.4 | O(N^2) | DB: 37)
  * `play` (Impact: 60.3 | O(N^2) | DB: 19)
  * `load` (Impact: 28.5 | O(2^N) | DB: 8)
  * `_resumePlayback` (Impact: 22.3 | O(N^3) | DB: 13)
  * `wireEngine` (Impact: 19.4 | O(N^2) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 90`, `args: 52`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 352`, `duplicate_logic: 12`
* *Architecture:* `io: 19`, `api: 56`, `concurrency: 135`, `import: 12`
* *Defense:* `safety: 33`, `doc: 32`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` engine, index, log, media-events, web-audio-instance, event-emitter, audio-implementation, audio-context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.078 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.364 IQR)
- **Top Global Matches:** file_cluster_4: 10.078, file_cluster_8: 10.242, file_cluster_13: 10.463
- **Magnitude:** 89.48 | **LOC:** 106 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (85.9182%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 46.0 | O(N^2) | DB: 6)
  * `question` (Impact: 3.6 | O(2^N))
  * `generatePatchVersion` (Impact: 2.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `io: 2`, `concurrency: 26`, `import: 4`
* *Defense:* `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` child_process, semver, readline, version
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/collision/colliders/polygon-collider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.832 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.174 IQR)
- **Top Global Matches:** file_cluster_13: 13.832, file_cluster_11: 14.188, file_cluster_8: 14.218
- **Magnitude:** 85.9 | **LOC:** 739 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (34.1846%), Tech Debt (37.2312%)
**Top Internal Functions/Classes:**
  * `triangulate` (Impact: 83.5 | O(N^3) | DB: 13)
  * `isConvex` (Impact: 33.1 | O(N^2) | DB: 13)
  * `collide` (Impact: 28.6 | O(2^N))
  * `rayCast` (Impact: 19.7 | O(N^2) | DB: 6)
  * `constructor` (Impact: 18.3 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 78`, `args: 49`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 434`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 48`, `import: 18`
* *Defense:* `safety: 6`, `doc: 40`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.67
  * `Choke Point (Betweenness):` 0.000321 | `Ripple Effect (Closeness):` 0.061679
  * `Imports (Out-Degree: 16):` shape, line-segment, vector, color, ray-cast-hit, collision-contact, edge-collider, collider...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/engine/interfaces/pointer-event-handlers.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.725 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.858 IQR)
- **Top Global Matches:** file_cluster_8: 15.725, file_cluster_13: 15.737, file_cluster_1: 15.806
- **Magnitude:** 81.31 | **LOC:** 44 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.8325%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 44`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 72`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.07007
  * `Imports (Out-Degree: 3):` pointer-event, wheel-event, events
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/collision/detection/sparse-hash-grid-collision-processor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.855 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.246 IQR)
- **Top Global Matches:** file_cluster_13: 13.855, file_cluster_11: 14.031, file_cluster_17: 14.236
- **Magnitude:** 80.39 | **LOC:** 407 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (47.1266%), Tech Debt (99.4185%)
**Top Internal Functions/Classes:**
  * `rayCast` (Impact: 404.3 | O(2^N) | DB: 22)
  * `_canCollide` (Impact: 126.9 | O(2^N) | DB: 11)
  * `track` (Impact: 21.5 | O(2^N) | DB: 2)
  * `narrowphase` (Impact: 16.5 | O(N^2) | DB: 5)
    * *Intent:* // if both are fixed short circuit
  * `update` (Impact: 14.4 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 53`, `args: 20`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 175`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 5`, `import: 20`
* *Defense:* `safety: 19`, `doc: 20`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001361
  * `Imports (Out-Degree: 17):` collision-type, ray-cast-hit, collision-group, ray-cast-options, body-component, pair, vector, collision-processor...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/entity-component-system/entity.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.547 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.814 IQR)
- **Top Global Matches:** file_cluster_13: 14.547, file_cluster_2: 14.707, file_cluster_4: 14.76
- **Magnitude:** 74.52 | **LOC:** 709 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (48.8406%), Tech Debt (90.8142%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 32.2 | O(N^2) | DB: 4)
    * *Intent:* /** * An Entity is the base type of anything that can have behavior in Excalibur, they are part of t...
  * `hasChild` (Impact: 32.0 | O(2^N) | DB: 1)
  * `addComponent` (Impact: 25.6 | O(2^N) | DB: 11)
    * *Intent:* /** * Remove an entity from children if it exists * @param entity
  * `clone` (Impact: 21.4 | O(2^N) | DB: 3)
  * `removeComponent` (Impact: 13.7 | O(N^2) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 107`, `args: 51`, `func_start: 64`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 298`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 89`, `concurrency: 39`, `import: 13`
* *Defense:* `safety: 23`, `doc: 69`, `immutability_locks: 26`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.203
  * `Choke Point (Betweenness):` 0.019323 | `Ripple Effect (Closeness):` 0.109116
  * `Imports (Out-Degree: 8):` scene, event-emitter, lifecycle-events, util, engine, observable, component, events...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `src/engine/graphics/graphics-component.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.868 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.544 IQR)
- **Top Global Matches:** file_cluster_13: 14.868, file_cluster_11: 15.159, file_cluster_8: 15.207
- **Magnitude:** 71.88 | **LOC:** 581 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (47.7184%), Tech Debt (86.9759%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 72.5 | O(N^2) | DB: 27)
    * *Intent:* /** * Component to manage drawings, using with the position component
  * `deserialize` (Impact: 67.5 | O(N^2) | DB: 13)
    * *Intent:* /** * Hide currently shown graphic
  * `add` (Impact: 29.2 | O(N^1) | DB: 8)
  * `serialize` (Impact: 26.0 | O(N^2) | DB: 24)
  * `recalculateBounds` (Impact: 20.5 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 53`, `args: 35`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 368`, `duplicate_logic: 6`
* *Architecture:* `api: 41`, `import: 14`
* *Defense:* `safety: 32`, `doc: 33`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.019
  * `Choke Point (Betweenness):` 0.007071 | `Ripple Effect (Closeness):` 0.074352
  * `Imports (Out-Degree: 12):` index, animation, log, vector, raster, color, watch-vector, text...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/engine/resources/gif.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.041 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.594 IQR)
- **Top Global Matches:** file_cluster_4: 14.041, file_cluster_13: 14.163, file_cluster_11: 14.201
- **Magnitude:** 69.46 | **LOC:** 635 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (56.2982%), Tech Debt (88.2144%)
**Top Internal Functions/Classes:**
  * `parseBlocks` (Impact: 63.8 | O(2^N) | DB: 9)
  * `arrayToImage` (Impact: 52.5 | O(N^2) | DB: 25)
  * `lzwDecode` (Impact: 50.3 | O(N^2) | DB: 17)
  * `parseImg` (Impact: 33.1 | O(N^2) | DB: 28)
  * `toAnimation` (Impact: 21.9 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 59`, `args: 39`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 341`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 24`, `concurrency: 30`, `import: 6`
* *Defense:* `safety: 15`, `doc: 13`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001361
  * `Imports (Out-Degree: 4):` sprite, index, sprite-sheet, image-source, animation, resource
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/graphics/font-text-instance.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.779 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.236 IQR)
- **Top Global Matches:** file_cluster_13: 13.779, file_cluster_8: 13.837, file_cluster_7: 14.103
- **Magnitude:** 69.07 | **LOC:** 393 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (56.2308%), Tech Debt (67.2127%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 40.1 | O(N^2) | DB: 42)
  * `_yAnchorFromBaseline` (Impact: 34.9 | O(N^2) | DB: 4)
  * `_xAnchorFromAlignment` (Impact: 34.8 | O(N^2) | DB: 3)
  * `_xFromAlignment` (Impact: 34.8 | O(N^2) | DB: 7)
  * `_getLinesFromText` (Impact: 27.7 | O(N^2) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 22`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 377`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `import: 7`
* *Defense:* `safety: 7`, `doc: 8`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.001237 | `Ripple Effect (Closeness):` 0.048332
  * `Imports (Out-Degree: 5):` math, color, string, excalibur-graphics-context-webgl, excalibur-graphics-context, bounding-box, font
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/tile-map/isometric-map.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.957 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.335 IQR)
- **Top Global Matches:** file_cluster_13: 13.957, file_cluster_11: 14.407, file_cluster_8: 14.437
- **Magnitude:** 68.83 | **LOC:** 576 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (43.6907%), Tech Debt (89.6694%)
**Top Internal Functions/Classes:**
  * `debug` (Impact: 92.0 | O(2^N) | DB: 14)
  * `constructor` (Impact: 31.6 | O(N^2) | DB: 34)
  * `draw` (Impact: 16.3 | O(2^N) | DB: 6)
  * `constructor` (Impact: 15.4 | O(N^2) | DB: 24)
  * `updateColliders` (Impact: 14.8 | O(N^3) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 61`, `args: 35`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 364`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 53`, `import: 22`
* *Defense:* `safety: 8`, `doc: 52`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.469
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.048129
  * `Imports (Out-Degree: 16):` body-component, vector, composite-collider, debug, pointer-component, collision-type, event-emitter, math...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context-2d-canvas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.849 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.443 IQR)
- **Top Global Matches:** file_cluster_13: 14.849, file_cluster_11: 15.146, file_cluster_8: 15.176
- **Magnitude:** 68.08 | **LOC:** 409 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (54.1476%), Tech Debt (99.9903%)
**Top Internal Functions/Classes:**
  * `drawImage` (Impact: 108.9 | O(2^N) | DB: 5)
  * `constructor` (Impact: 34.5 | O(N^2) | DB: 8)
  * `drawCircle` (Impact: 20.8 | O(N^1) | DB: 12)
  * `drawCircle` (Impact: 20.8 | O(N^1) | DB: 12)
  * `drawLine` (Impact: 11.9 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 36`, `args: 45`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 302`, `duplicate_logic: 14`
* *Architecture:* `api: 46`, `import: 10`
* *Defense:* `safety: 25`, `doc: 21`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.864
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002721
  * `Imports (Out-Degree: 9):` vector, color, screen, affine-matrix, debug-text, graphics-diagnostics, state-stack, excalibur-graphics-context...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.978 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.517 IQR)
- **Top Global Matches:** file_cluster_13: 10.978, file_cluster_8: 11.158, file_cluster_16: 11.247
- **Magnitude:** 67.28 | **LOC:** 410 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.3323%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 31`, `args: 7`, `func_start: 7`, `class_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 6`, `doc: 30`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.55
  * `Choke Point (Betweenness):` 0.007724 | `Ripple Effect (Closeness):` 0.097074
  * `Imports (Out-Degree: 6):` vector, color, screen, affine-matrix, material, post-processor, filtering
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `src/engine/color.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.533 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.035 IQR)
- **Top Global Matches:** file_cluster_8: 13.533, file_cluster_7: 13.565, file_cluster_13: 13.671
- **Magnitude:** 66.22 | **LOC:** 677 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^2) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (45.0176%), Tech Debt (94.5194%)
**Top Internal Functions/Classes:**
  * `fromRGBA` (Impact: 41.7 | O(N^2) | DB: 1)
  * `fromRGBString` (Impact: 31.0 | O(N^2) | DB: 2)
  * `toString` (Impact: 29.1 | O(N^2) | DB: 3)
  * `fromHex` (Impact: 20.9 | O(N^2) | DB: 2)
  * `lerp` (Impact: 17.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 73`, `args: 64`, `func_start: 62`, `class_start: 2`
* *Risk/State:* `state_mutation: 211`, `duplicate_logic: 8`
* *Architecture:* `api: 107`, `import: 1`
* *Defense:* `safety: 4`, `doc: 90`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.1331
  * `Imports (Out-Degree: 0):` math
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `sandbox/stats/stats.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.207 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.58 IQR)
- **Top Global Matches:** file_cluster_8: 11.207, file_cluster_7: 11.836, file_cluster_15: 11.863
- **Magnitude:** 66.04 | **LOC:** 109 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (38.7474%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f` (Impact: 28.6 | O(N^2) | DB: 7)
  * `Panel` (Impact: 8.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 14`, `args: 11`, `func_start: 10`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 1`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/scene.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.063 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.091 IQR)
- **Top Global Matches:** file_cluster_13: 15.063, file_cluster_4: 15.26, file_cluster_11: 15.428
- **Magnitude:** 65.22 | **LOC:** 775 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (49.6256%), Tech Debt (9.6735%)
**Top Internal Functions/Classes:**
  * `_initialize` (Impact: 48.5 | O(2^N) | DB: 13)
    * *Intent:* /** * Event hook fired directly before transition, either "in" or "out" of the scene * * This overri...
  * `update` (Impact: 25.9 | O(2^N) | DB: 15)
  * `remove` (Impact: 24.6 | O(2^N) | DB: 3)
    * *Intent:* /** * It is not recommended that internal excalibur methods be overridden, do so at your own risk. *
  * `_collectActorStats` (Impact: 18.9 | O(N^2) | DB: 3)
  * `transfer` (Impact: 14.7 | O(N^1) | DB: 2)
    * *Intent:* /** * It is not recommended that internal excalibur methods be overridden, do so at your own risk. *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 90`, `args: 55`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 237`, `planned_debt: 2`
* *Architecture:* `api: 81`, `concurrency: 64`, `import: 34`
* *Defense:* `safety: 50`, `doc: 67`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.316
  * `Choke Point (Betweenness):` 0.026378 | `Ripple Effect (Closeness):` 0.09724
  * `Imports (Out-Degree: 28):` offscreen-system, director, system, lifecycle-events, pointer-system, physics-config, trigger, isometric-entity-system...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/engine/collision/detection/dynamic-tree-collision-processor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.453 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.166 IQR)
- **Top Global Matches:** file_cluster_13: 13.453, file_cluster_11: 13.775, file_cluster_17: 13.797
- **Magnitude:** 63.49 | **LOC:** 323 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (57.0767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rayCast` (Impact: 182.3 | O(2^N) | DB: 3)
  * `broadphase` (Impact: 130.3 | O(N^4) | DB: 33)
  * `untrack` (Impact: 43.1 | O(2^N) | DB: 8)
  * `track` (Impact: 30.9 | O(2^N) | DB: 6)
  * `query` (Impact: 23.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 58`, `args: 19`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 166`, `dead_code: 2`
* *Architecture:* `api: 15`, `import: 20`
* *Defense:* `safety: 15`, `doc: 6`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.88
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.058945
  * `Imports (Out-Degree: 20):` collision-type, ray-cast-hit, collision-group, ray-cast-options, body-component, pair, vector, collision-contact...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/director/loader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.425 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.827 IQR)
- **Top Global Matches:** file_cluster_4: 14.425, file_cluster_13: 14.606, file_cluster_11: 14.925
- **Magnitude:** 62.35 | **LOC:** 451 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (49.3584%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `startButtonHandler` (Impact: 41.3 | O(N^4) | DB: 10)
  * `_positionPlayButton` (Impact: 24.8 | O(N^2) | DB: 16)
  * `startButtonFactory` (Impact: 24.7 | O(N^2) | DB: 3)
    * *Intent:* // logo drawing stuff
  * `onDraw` (Impact: 20.7 | O(N^1) | DB: 34)
  * `_playButton` (Impact: 11.1 | O(N^1) | DB: 17)
    * *Intent:* * ```typescript * const loader = new ex.Loader([playerTexture]); * * // The loaders button text can ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 44`, `args: 25`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 333`
* *Architecture:* `api: 32`, `concurrency: 84`, `import: 14`
* *Defense:* `safety: 15`, `doc: 20`, `immutability_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.602
  * `Choke Point (Betweenness):` 0.000505 | `Ripple Effect (Closeness):` 0.082626
  * `Imports (Out-Degree: 9):` log, vector, event-emitter, default-loader, color, util, engine, draw-util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/image-renderer/image-renderer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.778 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.46 IQR)
- **Top Global Matches:** file_cluster_13: 13.778, file_cluster_8: 14.089, file_cluster_17: 14.172
- **Magnitude:** 61.25 | **LOC:** 409 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 132
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 147.0 | O(N^1) | DB: 132)
  * `_transformFragmentSource` (Impact: 21.6 | O(N^2) | DB: 3)
  * `_addImageAsTexture` (Impact: 16.3 | O(N^2) | DB: 10)
  * `_getTextureIdForImage` (Impact: 8.3 | O(N^1) | DB: 2)
  * `_bindTextures` (Impact: 6.3 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 39`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 364`
* *Architecture:* `api: 11`, `import: 17`
* *Defense:* `safety: 16`, `immutability_locks: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.555
  * `Choke Point (Betweenness):` 0.00012 | `Ripple Effect (Closeness):` 0.053337
  * `Imports (Out-Degree: 13):` vertex-buffer, vertex-layout, shader, graphics-diagnostics, excalibur-graphics-context, image-source, excalibur-graphics-context-webgl, webgl-util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/shader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.793 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.853 IQR)
- **Top Global Matches:** file_cluster_13: 12.793, file_cluster_8: 12.821, file_cluster_17: 13.053
- **Magnitude:** 60.27 | **LOC:** 940 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (42.0607%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_setUniforms` (Impact: 97.0 | O(N^4) | DB: 12)
  * `glTypeToUniformTypeName` (Impact: 71.4 | O(N^1))
  * `_setImages` (Impact: 37.4 | O(N^3) | DB: 12)
  * `constructor` (Impact: 32.4 | O(N^2) | DB: 25)
  * `_loadImageSource` (Impact: 13.2 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 90`, `args: 25`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 268`
* *Architecture:* `io: 1`, `api: 17`, `import: 6`
* *Defense:* `safety: 13`, `doc: 25`, `immutability_locks: 44`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.685
  * `Choke Point (Betweenness):` 0.000746 | `Ripple Effect (Closeness):` 0.066855
  * `Imports (Out-Degree: 4):` matrix, .., watch, uniform-buffer, webgl-util
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/engine/graphics/nine-slice.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.746 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.365 IQR)
- **Top Global Matches:** file_cluster_13: 13.746, file_cluster_8: 13.776, file_cluster_7: 13.947
- **Magnitude:** 59.86 | **LOC:** 603 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 122
- **Risk Profile:** Cognitive Load (29.5927%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_drawTile` (Impact: 32.2 | O(N^2) | DB: 10)
  * `_drawImage` (Impact: 24.0 | O(N^3) | DB: 94)
  * `_initialize` (Impact: 23.3 | O(N^1) | DB: 122)
  * `_getNumberOfTiles` (Impact: 15.5 | O(N^2))
  * `setStretch` (Impact: 12.7 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 29`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `state_mutation: 450`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 11`, `import: 6`
* *Defense:* `safety: 11`, `doc: 32`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.782
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001361
  * `Imports (Out-Degree: 5):` log, vector, image-source, graphic, excalibur-graphics-context
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/spec/vitest/decorator-spec.ts` (TYPESCRIPT) | Magnitude: 3.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, args: 35, func_start: 35, test: 30
- `sandbox/tests/loader-lockup/index.ts` (TYPESCRIPT) | Magnitude: 0.98 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 6, args: 3, state_mutation: 3
- `sandbox/tests/memory-leaker/index.ts` (TYPESCRIPT) | Magnitude: 1.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 9, structural_boundaries: 5, args: 2
- `sandbox/tests/text-bounds/index.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 9, structural_boundaries: 5, branch: 1
- `sandbox/tests/pointer/index.html` (HTML) | Magnitude: 16.46 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 4, listeners: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/spec/vitest/event-emitter-spec.ts` (TYPESCRIPT) | Magnitude: 4.28 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 206, events: 105, args: 68, func_start: 52
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 20.7 | Delta: **0.235 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 179, doc: 40, decorators: 39, events: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/engine/util/coroutine.ts` (TYPESCRIPT) | Magnitude: 29.61 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 45, branch: 40, args: 27
- `src/engine/collision/detection/sparse-hash-grid.ts` (TYPESCRIPT) | Magnitude: 45.09 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 233, indent_spaces: 207, branch: 36, immutability_locks: 35
- `sandbox/tests/high-gravity-arcade/index.ts` (TYPESCRIPT) | Magnitude: 17.05 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, state_mutation: 75, branch: 16, immutability_locks: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/engine/entity-component-system/query.ts` (TYPESCRIPT) | Magnitude: 30.63 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 129, branch: 70, structural_boundaries: 43
- `src/stories/utils.ts` (TYPESCRIPT) | Magnitude: 6.62 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 26, branch: 15, args: 13
- `src/engine/math/bezier-curve.ts` (TYPESCRIPT) | Magnitude: 16.2 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 90, immutability_locks: 19, structural_boundaries: 18
- `src/engine/collision/colliders/shape.ts` (TYPESCRIPT) | Magnitude: 4.36 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 90, doc: 19, decorators: 18, structural_boundaries: 17
- `src/engine/interfaces/evented.ts` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 4, args: 4, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/engine/entity-component-system/components/tags-component.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, class_start: 1, generics: 1
- `src/engine/util/observable.ts` (TYPESCRIPT) | Magnitude: 8.3 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 50, indent_spaces: 37, doc: 17, structural_boundaries: 12
- `src/engine/interfaces/clonable.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1
- `src/spec/__matchers__/expect.visual.ts` (TYPESCRIPT) | Magnitude: 0.92 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, generics: 6, indent_spaces: 6, class_start: 3
- `src/engine/math/graph.ts` (TYPESCRIPT) | Magnitude: 34.85 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 214, state_mutation: 165, doc: 54, structural_boundaries: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/engine/collision/island.ts` (TYPESCRIPT) | Magnitude: 14.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 63, branch: 26, structural_boundaries: 14
- `src/engine/resources/sound/sound-manager.ts` (TYPESCRIPT) | Magnitude: 48.77 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 233, indent_spaces: 216, structural_boundaries: 52, branch: 50
- `src/engine/actions/action/parallel-actions.ts` (TYPESCRIPT) | Magnitude: 3.42 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 13, structural_boundaries: 12, args: 8
- `sandbox/excalibur-dev-tools/dev-tools.js` (JAVASCRIPT) | Magnitude: 5970.84 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5249, state_mutation: 3562, structural_boundaries: 1051, args: 981
- `src/engine/entity-component-system/entity-manager.ts` (TYPESCRIPT) | Magnitude: 30.87 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 140, indent_spaces: 117, branch: 27, args: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/spec/vitest/toaster-spec.ts` (TYPESCRIPT) | Magnitude: 1.21 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, args: 20, func_start: 20, test: 20
- `src/engine/util/browser.ts` (TYPESCRIPT) | Magnitude: 12.13 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 57, args: 19, structural_boundaries: 18
- `sandbox/tests/camera/strategy.ts` (TYPESCRIPT) | Magnitude: 2.27 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 11, args: 7, state_mutation: 7
- `src/engine/context.ts` (TYPESCRIPT) | Magnitude: 3.34 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, ui_framework: 7, branch: 6
- `src/engine/util/state-machine.ts` (TYPESCRIPT) | Magnitude: 13.65 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 92, state_mutation: 53, branch: 27, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/engine/input/gamepad.ts` (TYPESCRIPT) | Magnitude: 49.89 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 252, state_mutation: 200, structural_boundaries: 70, api: 62
- `src/engine/director/director.ts` (TYPESCRIPT) | Magnitude: 23.09 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 118, indent_spaces: 110, concurrency: 48, structural_boundaries: 41
- `src/stories/anchors.stories.ts` (TYPESCRIPT) | Magnitude: 10.02 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, memory_alloc: 52, immutability_locks: 46, state_mutation: 45
- `sandbox/tests/culling/culling2.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 8, structural_boundaries: 4, args: 3
- `playground/src/main.ts` (TYPESCRIPT) | Magnitude: 12.49 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 45, branch: 44, immutability_locks: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/engine/entity-component-system/component.ts` (TYPESCRIPT) | Magnitude: 27.65 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, branch: 65, structural_boundaries: 38, state_mutation: 33
- `playground/vite.config.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, api: 1, globals: 1
- `src/engine/interfaces/pointer-event-handlers.ts` (TYPESCRIPT) | Magnitude: 81.31 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 72, structural_boundaries: 44, args: 36, func_start: 36
- `src/stories/audio.stories.ts` (TYPESCRIPT) | Magnitude: 6.96 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 37, immutability_locks: 32, args: 27
- `sandbox/tests/screen/screen.ts` (TYPESCRIPT) | Magnitude: 1.93 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, state_mutation: 4, globals: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sandbox/tests/polygon-rendering/index.ts` (TYPESCRIPT) | Magnitude: 1.2 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 9, state_mutation: 8, dead_code: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` -> **keasy9** (100.0% isolated ownership) | Magnitude: 126.97
- `src/engine/resources/sound/sound.ts` -> **Girts Silis** (100.0% isolated ownership) | Magnitude: 92.62
- `src/engine/graphics/graphics-component.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 71.88
- `src/engine/graphics/font-text-instance.ts` -> **Erik Onarheim** (100.0% isolated ownership) | Magnitude: 69.07
- `src/engine/scene.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 65.22

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/engine/engine.ts` -> **Severity: 3.282** (Bridge: 0.0328 * Flux: 99.9684%)
- `src/engine/scene.ts` -> **Severity: 2.638** (Bridge: 0.0264 * Flux: 100.0%)
- `src/engine/actor.ts` -> **Severity: 1.977** (Bridge: 0.0198 * Flux: 100.0%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 1.932** (Bridge: 0.0193 * Flux: 100.0%)
- `src/engine/util/log.ts` -> **Severity: 1.154** (Bridge: 0.0115 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/engine/math/vector.ts` -> **Severity: 17.086** (Embedded: 0.1793 * Error Risk: 95.3124%)
- `src/engine/color.ts` -> **Severity: 12.559** (Embedded: 0.1331 * Error Risk: 94.3601%)
- `src/engine/util/log.ts` -> **Severity: 11.886** (Embedded: 0.1257 * Error Risk: 94.5847%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 10.633** (Embedded: 0.1091 * Error Risk: 97.4473%)
- `src/engine/collision/bounding-box.ts` -> **Severity: 9.606** (Embedded: 0.0967 * Error Risk: 99.2871%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/engine/math/vector.ts` -> **Severity: 3989.338** (Blast Radius: 41.749 * Doc Risk: 95.5553%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 2518.758** (Blast Radius: 26.203 * Doc Risk: 96.1248%)
- `src/engine/color.ts` -> **Severity: 1405.9** (Blast Radius: 14.059 * Doc Risk: 100.0%)
- `src/engine/scene.ts` -> **Severity: 931.6** (Blast Radius: 9.316 * Doc Risk: 100.0%)
- `src/engine/events.ts` -> **Severity: 835.2** (Blast Radius: 8.352 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
