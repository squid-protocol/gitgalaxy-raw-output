# ARCHITECTURAL_BRIEF: Excalibur
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/Excalibur` |
| **Timestamp** | `2026-08-07T04:09:54.261382+00:00` |
| **Scan Duration** | `2.56s` |
| **Git Branch** | `main` |
| **Git Commit** | `3aa48c717952d2a01339eee72acc8036d087137a` |
| **Git Remote** | `https://github.com/excaliburjs/Excalibur.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 577 malicious artifacts.

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
| Total Artifacts | 1797 |
| Analyzed Artifacts (Scanned) | 736 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1061 |
| Total LOC | 73444 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 41.0% |
| Dominant Lang | JAVASCRIPT |

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
> **Architectural Drift Z-Score:** `5.825`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 477 | 64.8% |
| file_cluster_13 | 187 | 25.4% |
| file_cluster_4 | 24 | 3.3% |
| file_cluster_16 | 11 | 1.5% |
| file_cluster_17 | 6 | 0.8% |
| file_cluster_0 | 6 | 0.8% |
| file_cluster_2 | 6 | 0.8% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 20.6 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 44.5 | 48.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 12.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.6 | 4.7 | 4.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 28.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 68.0 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.7 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 27.3 | 1.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 24.2 | 0.0 | 0.0 |
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

- `draw` (@ `src/engine/graphics/context/material-renderer/material-renderer.ts`) -> Impact: **172.3** | LOC: 158
- `draw` (@ `src/engine/graphics/context/image-renderer/image-renderer.ts`) -> Impact: **147.0** | LOC: 157
- `draw` (@ `src/engine/graphics/context/image-renderer-v2/image-renderer-v2.ts`) -> Impact: **143.9** | LOC: 95
- `describe` (@ `src/spec/vitest/action-spec.ts`) -> Impact: **121.4** | LOC: 1632
- `describe` (@ `src/spec/vitest/text-spec.ts`) -> Impact: **103.3** | LOC: 1061
- `updatePhysicsConfig` (@ `src/engine/collision/body-component.ts`) -> Impact: **97.5** | LOC: 351
- `describe` (@ `src/spec/vitest/engine-spec.ts`) -> Impact: **97.0** | LOC: 1073
- `describe` (@ `src/spec/vitest/excalibur-graphics-context-spec.ts`) -> Impact: **91.8** | LOC: 1109
- `constructor` (@ `src/engine/actor.ts`) -> Impact: **87.4** | LOC: 120
  * *Intent:* /**
- `describe` (@ `src/spec/vitest/actor-spec.ts`) -> Impact: **86.6** | LOC: 1377

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sandbox/excalibur-dev-tools` | 2 | 6336.02 | 47.95% | 50.0% |
| `__monolith__` | 16 | 5138.84 | 7.58% | 6.73% |
| `src/spec/vitest` | 127 | 1206.9 | 5.6% | 0.0% |
| `src/engine/graphics` | 33 | 594.44 | 38.32% | 28.18% |
| `src/engine` | 24 | 477.08 | 28.51% | 29.31% |
| `src/engine/graphics/context` | 19 | 450.83 | 39.16% | 34.16% |
| `src/engine/actions/action` | 22 | 356.0 | 54.74% | 27.27% |
| `src/engine/math` | 19 | 318.31 | 33.85% | 31.59% |
| `src/engine/collision/detection` | 11 | 220.52 | 28.87% | 35.53% |
| `src/engine/entity-component-system` | 13 | 217.58 | 28.95% | 8.82% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **100.0%** Exposure
- `sandbox/stats/stats.js` -> **100.0%** Exposure
- `sandbox/tests/bezier/index.ts` -> **100.0%** Exposure
- `sandbox/tests/coordinates/coordinates.ts` -> **100.0%** Exposure
- `sandbox/tests/engine/timescale.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **100.0%** Exposure
- `sandbox/tests/screen/screen.ts` -> **100.0%** Exposure
- `src/engine/actor.ts` -> **100.0%** Exposure
- `src/engine/camera.ts` -> **100.0%** Exposure
- `src/engine/collision/body-component.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sandbox/excalibur-dev-tools/dev-tools.js` -> **0** Orphaned Functions | **495** Duplicates
- `src/spec/vitest/action-spec.ts` -> **2** Orphaned Functions | **155** Duplicates
- `src/spec/vitest/serializer-spec.ts` -> **1** Orphaned Functions | **87** Duplicates
- `src/spec/vitest/actor-spec.ts` -> **3** Orphaned Functions | **83** Duplicates
- `src/spec/vitest/engine-spec.ts` -> **2** Orphaned Functions | **80** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `280` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/engine/entity-component-system/components/transform-component.ts` (TYPESCRIPT) -> Cumulative Risk: **752.24**
- **Archetype:** `file_cluster_13` (Distance: 12.778 IQR)
- **Magnitude:** 20.6 | **LOC:** 199 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `coordPlane` (Impact: 9.4), `deserialize` (Impact: 6.6), `onAdd` (Impact: 5.8)

### 2. `src/engine/resources/sound/sound.ts` (TYPESCRIPT) -> Cumulative Risk: **749.12**
- **Archetype:** `file_cluster_4` (Distance: 15.126 IQR)
- **Magnitude:** 79.75 | **LOC:** 555 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 44.2), `play` (Impact: 40.7), `load` (Impact: 14.5)

### 3. `src/engine/input/gamepad.ts` (TYPESCRIPT) -> Cumulative Risk: **738.18**
- **Archetype:** `file_cluster_4` (Distance: 14.797 IQR)
- **Magnitude:** 48.61 | **LOC:** 564 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9917%), Tech Debt (99.8536%), Documentation (97.7627%)
- **Heaviest Functions:** `update` (Impact: 58.3), `_clonePad` (Impact: 10.9), `_isGamepadValid` (Impact: 10.8)

### 4. `src/engine/tile-map/tile-map.ts` (TYPESCRIPT) -> Cumulative Risk: **732.49**
- **Archetype:** `file_cluster_13` (Distance: 15.172 IQR)
- **Magnitude:** 129.86 | **LOC:** 1004 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_updateColliders` (Impact: 48.3), `debug` (Impact: 30.6), `constructor` (Impact: 24.5)

### 5. `src/engine/entity-component-system/entity.ts` (TYPESCRIPT) -> Cumulative Risk: **731.96**
- **Archetype:** `file_cluster_13` (Distance: 14.598 IQR)
- **Magnitude:** 67.26 | **LOC:** 709 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.4634%), Safety Score (97.4473%)
- **Heaviest Functions:** `constructor` (Impact: 21.8), `removeComponent` (Impact: 15.6), `addComponent` (Impact: 15.4)

### 6. `src/engine/scene.ts` (TYPESCRIPT) -> Cumulative Risk: **662.02**
- **Archetype:** `file_cluster_13` (Distance: 15.091 IQR)
- **Magnitude:** 57.71 | **LOC:** 775 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9979%)
- **Heaviest Functions:** `_initialize` (Impact: 17.2), `transfer` (Impact: 14.7), `_activate` (Impact: 13.9)

### 7. `src/engine/resources/gif.ts` (TYPESCRIPT) -> Cumulative Risk: **660.22**
- **Archetype:** `file_cluster_4` (Distance: 14.022 IQR)
- **Magnitude:** 61.58 | **LOC:** 635 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8187%), Safety Score (99.6491%)
- **Heaviest Functions:** `lzwDecode` (Impact: 34.7), `arrayToImage` (Impact: 28.1), `parseImg` (Impact: 23.1)

### 8. `src/engine/resources/sound/sound-manager.ts` (TYPESCRIPT) -> Cumulative Risk: **655.44**
- **Archetype:** `file_cluster_17` (Distance: 14.352 IQR)
- **Magnitude:** 43.43 | **LOC:** 416 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.6493%), Safety Score (99.2033%)
- **Heaviest Functions:** `toggle` (Impact: 17.2), `addChannel` (Impact: 13.3), `track` (Impact: 11.4)

### 9. `src/engine/collision/body-component.ts` (TYPESCRIPT) -> Cumulative Risk: **653.22**
- **Archetype:** `file_cluster_13` (Distance: 14.275 IQR)
- **Magnitude:** 65.56 | **LOC:** 678 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `updatePhysicsConfig` (Impact: 97.5), `deserialize` (Impact: 33.3), `constructor` (Impact: 18.2)

### 10. `src/engine/util/state-machine.ts` (TYPESCRIPT) -> Cumulative Risk: **652.23**
- **Archetype:** `file_cluster_2` (Distance: 12.937 IQR)
- **Magnitude:** 12.23 | **LOC:** 115 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (97.8793%), Safety Score (93.5697%), Documentation (93.0915%)
- **Heaviest Functions:** `go` (Impact: 23.7), `create` (Impact: 15.3), `update` (Impact: 3.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sandbox/excalibur-dev-tools/dev-tools.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.709 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.941 IQR)
- **Top Global Matches:** file_cluster_17: 14.709, file_cluster_8: 14.762, file_cluster_11: 14.81
- **Magnitude:** 6331.14 | **LOC:** 5255 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.8885%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_processPointerToEntity` (Impact: 32.5)
  * `S` (Impact: 26.0)
  * `createMonitor` (Impact: 23.9)
  * `vn` (Impact: 23.2)
  * `rgb` (Impact: 23.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 823`, `structural_boundaries: 1051`, `args: 981`, `func_start: 806`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 212`, `high_risk_execution: 1`, `state_mutation: 3404`, `duplicate_logic: 495`
* *Architecture:* `io: 9`, `api: 8`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 353`, `test: 2`, `immutability_locks: 490`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/tile-map/tile-map.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.172 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.969 IQR)
- **Top Global Matches:** file_cluster_13: 15.172, file_cluster_11: 15.479, file_cluster_2: 15.503
- **Magnitude:** 129.86 | **LOC:** 1004 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (40.6884%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_updateColliders` (Impact: 48.3)
  * `debug` (Impact: 30.6)
  * `constructor` (Impact: 24.5)
  * `onPostDraw` (Impact: 20.1)
  * `update` (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 120`, `args: 82`, `func_start: 79`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 735`, `planned_debt: 1`, `duplicate_logic: 31`
* *Architecture:* `api: 104`, `concurrency: 33`, `import: 29`
* *Defense:* `safety: 46`, `doc: 51`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.366
  * `Choke Point (Betweenness):` 0.006009 | `Ripple Effect (Closeness):` 0.08637
  * `Imports (Out-Degree: 22):` bounding-box, shape, pointer-event-receiver, log, motion-component, engine, body-component, pointer-event...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.151 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.364 IQR)
- **Top Global Matches:** file_cluster_13: 14.151, file_cluster_11: 14.487, file_cluster_17: 14.582
- **Magnitude:** 102.11 | **LOC:** 861 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.0587%), Tech Debt (99.8058%)
**Top Internal Functions/Classes:**
  * `drawImage` (Impact: 68.4)
  * `constructor` (Impact: 51.5)
  * `flush` (Impact: 42.5)
  * `draw` (Impact: 23.8)
  * `drawLine` (Impact: 18.6)
    * *Intent:* /** * Draw a debugging rectangle to the graphics context * * Debugging draws are independent of scal...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 105`, `args: 70`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 574`, `fragile_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 70`, `import: 35`
* *Defense:* `safety: 37`, `doc: 25`, `immutability_locks: 30`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.945
  * `Choke Point (Betweenness):` 0.012392 | `Ripple Effect (Closeness):` 0.065721
  * `Imports (Out-Degree: 31):` transform-stack, vector, shader, graphics-diagnostics, screen, particle-renderer, debug-text, state-stack...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/engine/screen.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.05 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_13: 14.05, file_cluster_11: 14.29, file_cluster_8: 14.326
- **Magnitude:** 99.58 | **LOC:** 1232 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8217%), Tech Debt (54.0982%)
**Top Internal Functions/Classes:**
  * `applyResolutionAndViewport` (Impact: 72.5)
  * `_setResolutionAndViewportByDisplayMode` (Impact: 24.7)
  * `_computeFitAndZoom` (Impact: 18.4)
    * *Intent:* // Fall back to 'crisp-edges' if 'pixelated' is not supported
  * `parent` (Impact: 16.6)
  * `constructor` (Impact: 16.5)
    * *Intent:* /** * Canvas element to build a screen on
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 81`, `args: 53`, `func_start: 52`, `class_start: 7`
* *Risk/State:* `state_mutation: 603`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 66`, `import: 10`
* *Defense:* `safety: 15`, `doc: 35`, `immutability_locks: 28`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` log, excalibur-graphics-context-webgl, vector, index, event-emitter, browser, excalibur-graphics-context, excalibur-graphics-context-2d-canvas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sandbox/stats/stats.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.209 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.13 IQR)
- **Top Global Matches:** file_cluster_8: 11.209, file_cluster_7: 11.823, file_cluster_0: 11.831
- **Magnitude:** 88.84 | **LOC:** 109 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.7474%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `f` (Impact: 19.9)
  * `u` (Impact: 9.9)
  * `end` (Impact: 7.4)
  * `Panel` (Impact: 6.3)
  * `u` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 14`, `args: 11`, `func_start: 10`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 4`
* *Architecture:* `api: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/interfaces/pointer-event-handlers.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.725 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.858 IQR)
- **Top Global Matches:** file_cluster_8: 15.725, file_cluster_13: 15.737, file_cluster_1: 15.806
- **Magnitude:** 81.31 | **LOC:** 44 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8325%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 44`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 72`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.002
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.07007
  * `Imports (Out-Degree: 3):` events, wheel-event, pointer-event
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/collision/colliders/polygon-collider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.802 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.17 IQR)
- **Top Global Matches:** file_cluster_13: 13.802, file_cluster_11: 14.162, file_cluster_8: 14.192
- **Magnitude:** 79.95 | **LOC:** 739 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.1846%), Tech Debt (92.5552%)
**Top Internal Functions/Classes:**
  * `triangulate` (Impact: 45.4)
  * `findEarTip` (Impact: 24.6)
  * `isConvex` (Impact: 22.7)
  * `getClosestLineBetween` (Impact: 14.6)
    * *Intent:* /** * Given a direction vector find the local space side that is most in that direction * @param dir...
  * `collide` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 78`, `args: 48`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `state_mutation: 428`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 49`, `import: 18`
* *Defense:* `safety: 6`, `doc: 40`, `immutability_locks: 74`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.67
  * `Choke Point (Betweenness):` 0.000321 | `Ripple Effect (Closeness):` 0.061679
  * `Imports (Out-Degree: 16):` edge-collider, vector, color, collider, composite-collider, line-segment, collision-contact, ray...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/engine/resources/sound/sound.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.126 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.189 IQR)
- **Top Global Matches:** file_cluster_4: 15.126, file_cluster_13: 15.343, file_cluster_17: 15.494
- **Magnitude:** 79.75 | **LOC:** 555 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.9928%), Tech Debt (99.7808%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 44.2)
  * `play` (Impact: 40.7)
  * `load` (Impact: 14.5)
  * `wireEngine` (Impact: 13.4)
  * `decodeAudio` (Impact: 11.8)
    * *Intent:* /** * Schedule time to play in milliseconds from the audio context origin * * Compute using the audi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 90`, `args: 59`, `func_start: 49`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 352`, `duplicate_logic: 12`
* *Architecture:* `io: 19`, `api: 56`, `concurrency: 135`, `import: 12`
* *Defense:* `safety: 33`, `doc: 32`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` log, audio, resource, event-emitter, media-events, audio-context, sound, web-audio-instance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.057 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.364 IQR)
- **Top Global Matches:** file_cluster_4: 10.057, file_cluster_8: 10.222, file_cluster_13: 10.444
- **Magnitude:** 76.28 | **LOC:** 106 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.1414%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 32.0)
  * `execSync` (Impact: 2.5)
  * `generatePatchVersion` (Impact: 2.0)
  * `question` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `io: 2`, `concurrency: 26`, `import: 4`
* *Defense:* `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` version, readline, child_process, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/spec/vitest/action-spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.842 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.027 IQR)
- **Top Global Matches:** file_cluster_8: 10.842, file_cluster_7: 11.507, file_cluster_1: 11.571
- **Magnitude:** 74.24 | **LOC:** 1636 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6743%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 121.4)
  * `describe` (Impact: 15.2)
  * `describe` (Impact: 13.8)
  * `describe` (Impact: 13.2)
  * `describe` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 150`, `args: 624`, `func_start: 571`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 62`, `planned_debt: 3`, `duplicate_logic: 155`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 19`, `import: 2`
* *Defense:* `safety: 5`, `test: 568`, `immutability_locks: 47`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-utils, @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/engine/graphics/context/excalibur-graphics-context.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.978 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.517 IQR)
- **Top Global Matches:** file_cluster_13: 10.978, file_cluster_8: 11.158, file_cluster_16: 11.247
- **Magnitude:** 67.28 | **LOC:** 410 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3323%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 31`, `args: 7`, `func_start: 7`, `class_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 6`, `doc: 30`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.55
  * `Choke Point (Betweenness):` 0.007724 | `Ripple Effect (Closeness):` 0.097074
  * `Imports (Out-Degree: 6):` filtering, vector, color, material, screen, post-processor, affine-matrix
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `src/engine/entity-component-system/entity.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.598 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.813 IQR)
- **Top Global Matches:** file_cluster_13: 14.598, file_cluster_2: 14.758, file_cluster_4: 14.81
- **Magnitude:** 67.26 | **LOC:** 709 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.8406%), Tech Debt (90.8142%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 21.8)
    * *Intent:* /** * An Entity is the base type of anything that can have behavior in Excalibur, they are part of t...
  * `removeComponent` (Impact: 15.6)
  * `addComponent` (Impact: 15.4)
    * *Intent:* /** * Remove an entity from children if it exists * @param entity
  * `_getClassHierarchyRoot` (Impact: 12.5)
  * `hasChild` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 107`, `args: 64`, `func_start: 64`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 298`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 89`, `concurrency: 39`, `import: 13`
* *Defense:* `safety: 23`, `doc: 69`, `immutability_locks: 26`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.203
  * `Choke Point (Betweenness):` 0.019323 | `Ripple Effect (Closeness):` 0.109116
  * `Imports (Out-Degree: 8):` events, lifecycle-events, scene, util, observable, event-emitter, types, component...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `src/engine/collision/body-component.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.275 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.571 IQR)
- **Top Global Matches:** file_cluster_13: 14.275, file_cluster_11: 14.759, file_cluster_8: 14.776
- **Magnitude:** 65.56 | **LOC:** 678 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.3771%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `updatePhysicsConfig` (Impact: 97.5)
  * `deserialize` (Impact: 33.3)
  * `constructor` (Impact: 18.2)
  * `super` (Impact: 11.8)
  * `applyImpulse` (Impact: 9.7)
    * *Intent:* /** * The coefficient of friction on this actor. * * The {@apilink SolverStrategy.Arcade} does not s...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 68`, `args: 49`, `func_start: 48`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 267`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `api: 79`, `import: 17`
* *Defense:* `safety: 18`, `doc: 48`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.398
  * `Choke Point (Betweenness):` 0.002448 | `Ripple Effect (Closeness):` 0.07811
  * `Imports (Out-Degree: 13):` util, entity-component-system, collision-type, physics-config, collider-component, vector, island, event-emitter...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/engine/graphics/graphics-component.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.866 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.543 IQR)
- **Top Global Matches:** file_cluster_13: 14.866, file_cluster_11: 15.157, file_cluster_8: 15.205
- **Magnitude:** 65.28 | **LOC:** 581 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.7585%), Tech Debt (86.9759%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 49.2)
    * *Intent:* /** * Component to manage drawings, using with the position component
  * `deserialize` (Impact: 45.5)
    * *Intent:* /** * Hide currently shown graphic
  * `add` (Impact: 29.2)
  * `recalculateBounds` (Impact: 20.5)
  * `serialize` (Impact: 18.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 53`, `args: 36`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 366`, `duplicate_logic: 6`
* *Architecture:* `api: 42`, `import: 14`
* *Defense:* `safety: 32`, `doc: 33`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.019
  * `Choke Point (Betweenness):` 0.007071 | `Ripple Effect (Closeness):` 0.074352
  * `Imports (Out-Degree: 12):` entity-component-system, watch-vector, excalibur-graphics-context, vector, raster, material, text, graphics-group...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/engine/color.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.533 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.035 IQR)
- **Top Global Matches:** file_cluster_8: 13.533, file_cluster_7: 13.565, file_cluster_13: 13.671
- **Magnitude:** 61.69 | **LOC:** 677 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (45.0176%), Tech Debt (94.5194%)
**Top Internal Functions/Classes:**
  * `fromRGBA` (Impact: 28.3)
  * `fromRGBString` (Impact: 20.9)
  * `toString` (Impact: 19.6)
  * `fromFloatArray` (Impact: 15.9)
  * `fromHex` (Impact: 14.2)
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

### `src/engine/resources/gif.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.022 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.58 IQR)
- **Top Global Matches:** file_cluster_4: 14.022, file_cluster_13: 14.148, file_cluster_11: 14.189
- **Magnitude:** 61.58 | **LOC:** 635 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.2982%), Tech Debt (99.8187%)
**Top Internal Functions/Classes:**
  * `lzwDecode` (Impact: 34.7)
  * `arrayToImage` (Impact: 28.1)
  * `parseImg` (Impact: 23.1)
  * `parseBlocks` (Impact: 22.2)
  * `toAnimation` (Impact: 14.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 59`, `args: 38`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 341`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 2`, `api: 24`, `concurrency: 30`, `import: 6`
* *Defense:* `safety: 15`, `doc: 13`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001361
  * `Imports (Out-Degree: 4):` sprite-sheet, image-source, sprite, index, resource, animation
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/graphics/font-text-instance.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.779 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.236 IQR)
- **Top Global Matches:** file_cluster_13: 13.779, file_cluster_8: 13.837, file_cluster_7: 14.103
- **Magnitude:** 60.55 | **LOC:** 393 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.2308%), Tech Debt (67.2127%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 27.8)
  * `_xAnchorFromAlignment` (Impact: 23.6)
  * `_xFromAlignment` (Impact: 23.6)
  * `_yAnchorFromBaseline` (Impact: 23.6)
  * `_getLinesFromText` (Impact: 19.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 22`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 377`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `import: 7`
* *Defense:* `safety: 7`, `doc: 8`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.024
  * `Choke Point (Betweenness):` 0.001237 | `Ripple Effect (Closeness):` 0.048332
  * `Imports (Out-Degree: 5):` bounding-box, font, excalibur-graphics-context, excalibur-graphics-context-webgl, math, string, color
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/image-renderer/image-renderer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.778 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.46 IQR)
- **Top Global Matches:** file_cluster_13: 13.778, file_cluster_8: 14.089, file_cluster_17: 14.172
- **Magnitude:** 59.8 | **LOC:** 409 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 147.0)
  * `_transformFragmentSource` (Impact: 14.7)
  * `_addImageAsTexture` (Impact: 11.3)
  * `_getTextureIdForImage` (Impact: 8.3)
  * `_bindTextures` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 39`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 364`
* *Architecture:* `api: 11`, `import: 17`
* *Defense:* `safety: 16`, `immutability_locks: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.555
  * `Choke Point (Betweenness):` 0.00012 | `Ripple Effect (Closeness):` 0.053337
  * `Imports (Out-Degree: 13):` renderer, graphics-diagnostics, excalibur-graphics-context-webgl, image-renderer.vert.glsl?raw, image-source, wrapping, filtering, excalibur-graphics-context...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/tile-map/isometric-map.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.939 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.337 IQR)
- **Top Global Matches:** file_cluster_13: 13.939, file_cluster_11: 14.392, file_cluster_8: 14.421
- **Magnitude:** 59.1 | **LOC:** 576 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.6158%), Tech Debt (98.6342%)
**Top Internal Functions/Classes:**
  * `debug` (Impact: 24.4)
  * `constructor` (Impact: 22.1)
  * `constructor` (Impact: 10.9)
  * `_getOrSetColliderOriginalOffset` (Impact: 10.4)
  * `getTile` (Impact: 9.0)
    * *Intent:* /** * @internal */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 61`, `args: 35`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 360`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 54`, `import: 22`
* *Defense:* `safety: 8`, `doc: 52`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.469
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.048129
  * `Imports (Out-Degree: 16):` bounding-box, collider-component, debug, pointer-component, entity, isometric-entity-component, vector, math...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/director/loader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.41 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.848 IQR)
- **Top Global Matches:** file_cluster_4: 14.41, file_cluster_13: 14.591, file_cluster_11: 14.911
- **Magnitude:** 58.23 | **LOC:** 451 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3584%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDraw` (Impact: 20.7)
  * `startButtonHandler` (Impact: 17.3)
  * `_positionPlayButton` (Impact: 17.0)
  * `startButtonFactory` (Impact: 16.9)
    * *Intent:* // logo drawing stuff
  * `_playButton` (Impact: 11.1)
    * *Intent:* * ```typescript * const loader = new ex.Loader([playerTexture]); * * // The loaders button text can ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 44`, `args: 25`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 331`
* *Architecture:* `api: 33`, `concurrency: 84`, `import: 14`
* *Defense:* `safety: 15`, `doc: 20`, `immutability_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.602
  * `Choke Point (Betweenness):` 0.000505 | `Ripple Effect (Closeness):` 0.082626
  * `Imports (Out-Degree: 9):` util, Loader.logo.png, vector, Loader.css?inline, event-emitter, default-loader, engine, screen...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/engine/graphics/context/excalibur-graphics-context-2d-canvas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.849 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.443 IQR)
- **Top Global Matches:** file_cluster_13: 14.849, file_cluster_11: 15.145, file_cluster_8: 15.175
- **Magnitude:** 57.82 | **LOC:** 409 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.1476%), Tech Debt (99.9903%)
**Top Internal Functions/Classes:**
  * `drawImage` (Impact: 55.1)
  * `constructor` (Impact: 23.2)
  * `drawCircle` (Impact: 20.8)
  * `drawCircle` (Impact: 20.8)
  * `drawLine` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 36`, `args: 45`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 302`, `duplicate_logic: 14`
* *Architecture:* `api: 46`, `import: 10`
* *Defense:* `safety: 25`, `doc: 21`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.864
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002721
  * `Imports (Out-Degree: 9):` vector, color, graphics-diagnostics, material, screen, debug-text, post-processor, excalibur-graphics-context...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/engine/graphics/nine-slice.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.743 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.363 IQR)
- **Top Global Matches:** file_cluster_13: 13.743, file_cluster_8: 13.776, file_cluster_7: 13.945
- **Magnitude:** 57.71 | **LOC:** 603 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.5927%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_initialize` (Impact: 23.3)
  * `_drawTile` (Impact: 22.3)
  * `_drawImage` (Impact: 14.0)
  * `setStretch` (Impact: 12.7)
  * `_getNumberOfTiles` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 29`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `state_mutation: 450`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 12`, `import: 6`
* *Defense:* `safety: 11`, `doc: 32`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.782
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001361
  * `Imports (Out-Degree: 5):` excalibur-graphics-context, vector, log, image-source, graphic
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/engine/scene.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.091 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.095 IQR)
- **Top Global Matches:** file_cluster_13: 15.091, file_cluster_4: 15.288, file_cluster_11: 15.455
- **Magnitude:** 57.71 | **LOC:** 775 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.6256%), Tech Debt (9.6735%)
**Top Internal Functions/Classes:**
  * `_initialize` (Impact: 17.2)
    * *Intent:* /** * Event hook fired directly before transition, either "in" or "out" of the scene * * This overri...
  * `transfer` (Impact: 14.7)
    * *Intent:* /** * It is not recommended that internal excalibur methods be overridden, do so at your own risk. *...
  * `_activate` (Impact: 13.9)
    * *Intent:* // will be overridden
  * `update` (Impact: 13.8)
  * `_collectActorStats` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 90`, `args: 63`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 237`, `planned_debt: 2`
* *Architecture:* `api: 81`, `concurrency: 64`, `import: 34`
* *Defense:* `safety: 50`, `doc: 67`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.316
  * `Choke Point (Betweenness):` 0.026378 | `Ripple Effect (Closeness):` 0.09724
  * `Imports (Out-Degree: 28):` pointer-scope, timer, pointer-system, camera, physics-world, entity, lifecycle-events, log...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/spec/vitest/excalibur-graphics-context-spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.365 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.006 IQR)
- **Top Global Matches:** file_cluster_8: 9.365, file_cluster_7: 10.128, file_cluster_4: 10.155
- **Magnitude:** 57.64 | **LOC:** 1223 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.9013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 91.8)
  * `describe` (Impact: 79.9)
  * `describe` (Impact: 68.2)
  * `describe` (Impact: 13.5)
  * `describe` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 95`, `args: 97`, `func_start: 89`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `fragile_debt: 1`, `duplicate_logic: 62`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 71`, `import: 2`
* *Defense:* `safety: 4`, `test: 112`, `immutability_locks: 118`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` @excalibur
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `sandbox/tests/loader-lockup/index.ts` (TYPESCRIPT) | Magnitude: 0.98 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 6, args: 3, state_mutation: 3
- `sandbox/tests/memory-leaker/index.ts` (TYPESCRIPT) | Magnitude: 1.51 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 9, structural_boundaries: 5, args: 2
- `sandbox/tests/text-bounds/index.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 9, structural_boundaries: 5, branch: 1
- `src/spec/vitest/decorator-spec.ts` (TYPESCRIPT) | Magnitude: 7.24 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, args: 35, func_start: 35, test: 30
- `sandbox/tests/pointer/index.html` (HTML) | Magnitude: 16.46 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 4, listeners: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/spec/vitest/event-emitter-spec.ts` (TYPESCRIPT) | Magnitude: 10.36 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 206, events: 105, args: 68, func_start: 52
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 19.7 | Delta: **0.235 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 179, doc: 40, decorators: 39, events: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/engine/collision/detection/sparse-hash-grid.ts` (TYPESCRIPT) | Magnitude: 34.78 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 233, indent_spaces: 207, branch: 36, immutability_locks: 35
- `sandbox/tests/high-gravity-arcade/index.ts` (TYPESCRIPT) | Magnitude: 13.36 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, state_mutation: 75, branch: 16, immutability_locks: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/engine/entity-component-system/query.ts` (TYPESCRIPT) | Magnitude: 27.19 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 129, branch: 70, structural_boundaries: 43
- `src/stories/utils.ts` (TYPESCRIPT) | Magnitude: 4.93 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 26, branch: 15, args: 13
- `src/engine/util/coroutine.ts` (TYPESCRIPT) | Magnitude: 17.69 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 45, branch: 40, args: 27
- `src/engine/math/bezier-curve.ts` (TYPESCRIPT) | Magnitude: 15.27 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 90, immutability_locks: 19, structural_boundaries: 18
- `src/engine/collision/colliders/shape.ts` (TYPESCRIPT) | Magnitude: 3.64 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 90, doc: 19, decorators: 18, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/engine/entity-component-system/components/tags-component.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, class_start: 1, generics: 1
- `src/engine/interfaces/clonable.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1
- `src/engine/util/observable.ts` (TYPESCRIPT) | Magnitude: 9.17 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 42, indent_spaces: 37, doc: 17, structural_boundaries: 12
- `src/spec/__matchers__/expect.visual.ts` (TYPESCRIPT) | Magnitude: 0.92 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, generics: 6, indent_spaces: 6, class_start: 3
- `src/engine/math/graph.ts` (TYPESCRIPT) | Magnitude: 32.84 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 214, state_mutation: 165, doc: 54, structural_boundaries: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/engine/resources/sound/sound-manager.ts` (TYPESCRIPT) | Magnitude: 43.43 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 233, indent_spaces: 216, structural_boundaries: 52, branch: 50
- `src/engine/actions/action/parallel-actions.ts` (TYPESCRIPT) | Magnitude: 2.62 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 13, structural_boundaries: 12, args: 8
- `src/engine/collision/island.ts` (TYPESCRIPT) | Magnitude: 14.74 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 63, branch: 26, structural_boundaries: 14
- `src/engine/util/browser.ts` (TYPESCRIPT) | Magnitude: 11.07 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 49, args: 19, structural_boundaries: 18
- `sandbox/excalibur-dev-tools/dev-tools.js` (JAVASCRIPT) | Magnitude: 6331.14 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5249, state_mutation: 3404, structural_boundaries: 1051, args: 981

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `sandbox/tests/camera/strategy.ts` (TYPESCRIPT) | Magnitude: 2.27 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 11, args: 7, state_mutation: 7
- `src/spec/vitest/toaster-spec.ts` (TYPESCRIPT) | Magnitude: 2.97 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, args: 20, func_start: 20, test: 20
- `src/engine/context.ts` (TYPESCRIPT) | Magnitude: 3.46 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, ui_framework: 7, branch: 6
- `src/engine/util/state-machine.ts` (TYPESCRIPT) | Magnitude: 12.23 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 92, state_mutation: 53, branch: 27, structural_boundaries: 24
- `sandbox/tests/spritefont/spritefont.ts` (TYPESCRIPT) | Magnitude: 3.34 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, state_mutation: 17, ui_framework: 14, globals: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/engine/input/gamepad.ts` (TYPESCRIPT) | Magnitude: 48.61 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 252, state_mutation: 190, api: 71, structural_boundaries: 70
- `src/stories/anchors.stories.ts` (TYPESCRIPT) | Magnitude: 10.52 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, memory_alloc: 52, immutability_locks: 46, state_mutation: 45
- `src/engine/director/director.ts` (TYPESCRIPT) | Magnitude: 22.99 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 118, indent_spaces: 110, concurrency: 48, structural_boundaries: 41
- `playground/src/main.ts` (TYPESCRIPT) | Magnitude: 10.87 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 45, branch: 44, immutability_locks: 37
- `src/spec/vitest/frame-stats-spec.ts` (TYPESCRIPT) | Magnitude: 4.89 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, args: 25, func_start: 25, test: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/engine/entity-component-system/component.ts` (TYPESCRIPT) | Magnitude: 16.93 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, branch: 65, structural_boundaries: 38, state_mutation: 33
- `playground/vite.config.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, api: 1, globals: 1
- `src/stories/audio.stories.ts` (TYPESCRIPT) | Magnitude: 7.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 37, immutability_locks: 32, args: 27
- `src/engine/interfaces/pointer-event-handlers.ts` (TYPESCRIPT) | Magnitude: 81.31 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 72, structural_boundaries: 44, args: 36, func_start: 36
- `src/spec/vitest/debug-system-spec.ts` (TYPESCRIPT) | Magnitude: 17.94 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 187, concurrency: 104, structural_boundaries: 35, test: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sandbox/tests/polygon-rendering/index.ts` (TYPESCRIPT) | Magnitude: 1.2 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 9, state_mutation: 8, dead_code: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/engine/graphics/context/excalibur-graphics-context-webgl.ts` -> **keasy9** (100.0% isolated ownership) | Magnitude: 102.11
- `src/engine/resources/sound/sound.ts` -> **Girts Silis** (100.0% isolated ownership) | Magnitude: 79.75
- `src/engine/collision/body-component.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 65.56
- `src/engine/graphics/graphics-component.ts` -> **Justin Young** (100.0% isolated ownership) | Magnitude: 65.28
- `src/engine/graphics/font-text-instance.ts` -> **Erik Onarheim** (100.0% isolated ownership) | Magnitude: 60.55

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

- `src/engine/math/vector.ts` -> **Severity: 3900.505** (Blast Radius: 41.749 * Doc Risk: 93.4275%)
- `src/engine/entity-component-system/entity.ts` -> **Severity: 2492.063** (Blast Radius: 26.203 * Doc Risk: 95.106%)
- `src/engine/color.ts` -> **Severity: 1405.9** (Blast Radius: 14.059 * Doc Risk: 100.0%)
- `src/engine/scene.ts` -> **Severity: 931.6** (Blast Radius: 9.316 * Doc Risk: 100.0%)
- `src/engine/events.ts` -> **Severity: 835.2** (Blast Radius: 8.352 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
