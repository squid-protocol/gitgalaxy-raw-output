# ARCHITECTURAL_BRIEF: react-flow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/react-flow` |
| **Timestamp** | `2026-08-03T20:06:53.770537+00:00` |
| **Scan Duration** | `1.42s` |
| **Git Branch** | `main` |
| **Git Commit** | `a58568f11bc0e1a1bdca1b3549e959e2e1ca0cdd` |
| **Git Remote** | `https://github.com/wbkd/react-flow.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 444 malicious artifacts.

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
| Total Artifacts | 685 |
| Analyzed Artifacts (Scanned) | 647 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 38 |
| Total LOC | 35742 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 94.5% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.406 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4529 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5931 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 29 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 436 | 27595 | 67.4% |
| HTML | 129 | 6619 | 19.9% |
| CSS | 27 | 1097 | 4.2% |
| MARKDOWN | 17 | 0 | 2.6% |
| PLAINTEXT | 16 | 5 | 2.5% |
| JSON | 12 | 169 | 1.9% |
| JAVASCRIPT | 8 | 244 | 1.2% |
| YAML | 2 | 13 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.422`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 391 | 60.4% |
| file_cluster_13 | 167 | 25.8% |
| file_cluster_2 | 27 | 4.2% |
| file_cluster_17 | 12 | 1.9% |
| file_cluster_16 | 9 | 1.4% |
| Unknown | 5 | 0.8% |
| file_cluster_0 | 4 | 0.6% |
| file_cluster_9 | 2 | 0.3% |
| file_cluster_4 | 1 | 0.2% |
| file_cluster_11 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 28 | 4.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 38*

**Composition by Extension & Reason:**
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2245 LOC)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14167 LOC)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 83.5 | 10.7 | 5.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 93.4 | 12.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.0 | 0.2 | 0.0 |
| API Exposure | 0.0 | 19.4 | 4.1 | 3.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 93.0 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.5 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.3 | 6.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `examples/react/src/App/routes.ts` (Hits: 66)
- `packages/react/src/components/ConnectionLine/index.tsx` (Hits: 9)
- `packages/svelte/src/lib/components/ConnectionLine/ConnectionLine.svelte` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.json** (`tooling/tsconfig/react.json`) — 237 inbound connections
2. **simpleflow.ts** (`examples/react/cypress/fixtures/simpleflow.ts`) — 9 inbound connections
3. **NodeIdContext.ts** (`packages/react/src/contexts/NodeIdContext.ts`) — 7 inbound connections
4. **Handle.svelte** (`packages/svelte/src/lib/components/Handle/Handle.svelte`) — 5 inbound connections
5. **Panel.svelte** (`packages/svelte/src/lib/container/Panel/Panel.svelte`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **routes.ts** (`examples/react/src/App/routes.ts`) — 65 outbound dependencies
2. **index.ts** (`packages/react/src/index.ts`) — 37 outbound dependencies
3. **index.ts** (`packages/svelte/src/lib/index.ts`) — 33 outbound dependencies
4. **Controls.tsx** (`packages/react/src/additional-components/Controls/Controls.tsx`) — 15 outbound dependencies
5. **index.tsx** (`packages/react/src/container/ReactFlow/index.tsx`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getInitialStore` (@ `packages/svelte/src/lib/store/initial-store.svelte.ts`) -> Impact: **490.0** | LOC: 360
- `createStore` (@ `packages/svelte/src/lib/store/index.ts`) -> Impact: **395.3** | LOC: 386
- `getInternalNode` (@ `packages/svelte/src/lib/hooks/useSvelteFlow.svelte.ts`) -> Impact: **340.6** | LOC: 212
  * *Intent:* /** * Converts a screen / client position to a flow position.
- `createWithEqualityFn` (@ `packages/react/src/store/index.ts`) -> Impact: **335.1** | LOC: 381
- `getUpperExtentClamp` (@ `packages/system/src/xyresizer/utils.ts`) -> Impact: **216.7** | LOC: 35
- `useReactFlow` (@ `packages/react/src/hooks/useReactFlow.ts`) -> Impact: **213.6** | LOC: 254
  * *Intent:* /**
- `onPointerDown` (@ `packages/svelte/src/lib/components/EdgeReconnectAnchor/EdgeReconnectAnchor.svelte`) -> Impact: **164.2** | LOC: 83
- `handleExpandParent` (@ `packages/system/src/utils/store.ts`) -> Impact: **151.2** | LOC: 84
- `applyChanges` (@ `packages/react/src/utils/changes.ts`) -> Impact: **132.5** | LOC: 155
  * *Intent:* /*
- `onPointerDown` (@ `packages/react/src/components/Handle/index.tsx`) -> Impact: **112.5** | LOC: 45

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `describe` (@ `examples/react/cypress/components/reactflow/event-handlers.cy.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `examples/react/cypress/components/reactflow/multiple-instance.cy.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `examples/react/cypress/components/reactflow/view-props.cy.tsx`) -> **O(2^N) [Recursive]**
- `getUpperExtentClamp` (@ `packages/system/src/xyresizer/utils.ts`) -> **O(2^N) [Recursive]**
- `onPointerDown` (@ `packages/svelte/src/lib/components/EdgeReconnectAnchor/EdgeReconnectAnchor.svelte`) -> **O(2^N) [Recursive]**
- `describe` (@ `examples/react/cypress/components/reactflow/basic-props.cy.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `examples/react/cypress/components/utils/graph-utils.cy.ts`) -> **O(2^N) [Recursive]**
- `onReconnectMouseOut` (@ `packages/react/src/components/EdgeWrapper/EdgeUpdateAnchors.tsx`) -> **O(2^N) [Recursive]**
- `onPointerDown` (@ `packages/react/src/components/Handle/index.tsx`) -> **O(2^N) [Recursive]**
- `applyChanges` (@ `packages/react/src/utils/changes.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /*

### Highest Data Gravity (Database Complexity)
- `getInitialStore` (@ `packages/svelte/src/lib/store/initial-store.svelte.ts`) -> DB Complexity: **77**
- `StressFlow` (@ `examples/react/src/examples/Stress/index.tsx`) -> DB Complexity: **18**
- `Header` (@ `examples/react/src/App/header.tsx`) -> DB Complexity: **12**
- `CustomEdge` (@ `examples/react/cypress/components/reactflow/multiple-instance.cy.tsx`) -> DB Complexity: **9**
- `getNodeToolbarTransform` (@ `packages/system/src/utils/node-toolbar.ts`) -> DB Complexity: **9**
- `constructor` (@ `examples/react/src/examples/Stress/performanceUtils.ts`) -> DB Complexity: **7**
  * *Intent:* /** * Measures and outputs the duration of every frame that happens between the * instance is created and `endRecording()` is called. * * Usage: *
- `useEffect` (@ `packages/react/src/hooks/useKeyPress.ts`) -> DB Complexity: **7**
  * *Intent:* /** * The key code (string or array of strings) specifies which key(s) should trigger * an action. * * A **string** can represent: * - A **single key*...
- `addConnectionToLookup` (@ `packages/system/src/utils/store.ts`) -> DB Complexity: **7**
- `ResizeIcon` (@ `examples/react/src/examples/NodeResizer/ResizeIcon.tsx`) -> DB Complexity: **6**
- `getNodesAndEdges` (@ `examples/react/src/examples/Stress/utils.ts`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/svelte` | 9 | 10072.08 | 2.38% | 0.0% |
| `examples/svelte` | 8 | 5053.21 | 4.32% | 0.0% |
| `__monolith__` | 10 | 5051.44 | 2.0% | 0.0% |
| `packages/react` | 5 | 5040.7 | 1.0% | 0.0% |
| `examples/svelte/src/routes/examples/interaction` | 1 | 235.1 | 9.67% | 0.0% |
| `packages/svelte/src/lib/container/Pane` | 3 | 213.84 | 14.44% | 0.0% |
| `packages/svelte/src/lib/components/EdgeReconnectAnchor` | 3 | 173.47 | 8.08% | 0.0% |
| `packages/svelte/src/lib/components/Handle` | 3 | 160.21 | 12.69% | 0.0% |
| `packages/svelte/src/lib/components/NodeWrapper` | 3 | 160.19 | 17.36% | 0.0% |
| `packages/svelte/src/lib/plugins/NodeResizer` | 4 | 141.74 | 18.84% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/react/src/hooks/useOnViewportChange.ts` -> **100.0%** Exposure
- `packages/svelte/src/lib/components/edges/index.ts` -> **100.0%** Exposure
- `packages/svelte/src/lib/hooks/useNodesData.svelte.ts` -> **100.0%** Exposure
- `packages/react/src/hooks/useGlobalKeyHandler.ts` -> **99.9999%** Exposure
- `packages/react/src/components/NodeWrapper/useNodeObserver.ts` -> **99.9985%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/react/src/components/BatchProvider/types.ts` -> **100.0%** Exposure
- `packages/react/src/components/Edges/EdgeAnchor.tsx` -> **100.0%** Exposure
- `packages/react/src/components/NodeWrapper/useNodeObserver.ts` -> **100.0%** Exposure
- `packages/react/src/components/Nodes/utils.ts` -> **100.0%** Exposure
- `packages/system/src/utils/marker.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/react/cypress/e2e/interaction.cy.ts` -> **2** Orphaned Functions | **21** Duplicates
- `examples/react/cypress/e2e/basic.cy.ts` -> **2** Orphaned Functions | **17** Duplicates
- `examples/react/cypress/e2e/controls.cy.ts` -> **2** Orphaned Functions | **7** Duplicates
- `examples/react/cypress/e2e/figma.cy.ts` -> **2** Orphaned Functions | **5** Duplicates
- `examples/react/cypress/e2e/hidden.cy.ts` -> **2** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/svelte/src/lib/container/SvelteFlow/types.ts`** -> AI Confidence: **99.48%**
2. **`packages/system/src/utils/edges/positions.ts`** -> AI Confidence: **99.34%**
3. **`packages/system/src/xyresizer/utils.ts`** -> AI Confidence: **99.32%**
4. **`tooling/rollup-config/src/index.js`** -> AI Confidence: **99.31%**
5. **`packages/react/src/additional-components/MiniMap/MiniMap.tsx`** -> AI Confidence: **99.31%**
6. **`packages/react/src/additional-components/NodeResizer/NodeResizeControl.tsx`** -> AI Confidence: **99.31%**
7. **`packages/react/src/additional-components/NodeToolbar/NodeToolbar.tsx`** -> AI Confidence: **99.31%**
8. **`packages/react/src/components/BatchProvider/index.tsx`** -> AI Confidence: **99.31%**
9. **`packages/react/src/components/EdgeWrapper/index.tsx`** -> AI Confidence: **99.31%**
10. **`packages/react/src/components/Handle/index.tsx`** -> AI Confidence: **99.31%**
11. **`packages/react/src/components/NodeWrapper/index.tsx`** -> AI Confidence: **99.31%**
12. **`packages/react/src/components/StoreUpdater/index.tsx`** -> AI Confidence: **99.31%**
13. **`packages/react/src/container/Pane/index.tsx`** -> AI Confidence: **99.31%**
14. **`packages/svelte/src/lib/store/initial-store.svelte.ts`** -> AI Confidence: **99.31%**
15. **`packages/system/src/xypanzoom/XYPanZoom.ts`** -> AI Confidence: **99.31%**
16. **`examples/react/src/examples/NodeResizer/HorizontalResizer.tsx`** -> AI Confidence: **99.29%**
17. **`examples/react/src/examples/NodeResizer/VerticalResizer.tsx`** -> AI Confidence: **99.29%**
18. **`packages/react/src/store/initialState.ts`** -> AI Confidence: **99.29%**
19. **`packages/system/src/utils/edges/smoothstep-edge.ts`** -> AI Confidence: **99.29%**
20. **`packages/react/src/additional-components/Background/Background.tsx`** -> AI Confidence: **99.24%**
21. **`packages/react/src/components/ConnectionLine/index.tsx`** -> AI Confidence: **99.24%**
22. **`packages/react/src/components/ReactFlowProvider/index.tsx`** -> AI Confidence: **99.23%**
23. **`packages/react/src/hooks/useReactFlow.ts`** -> AI Confidence: **99.23%**
24. **`packages/system/src/xydrag/XYDrag.ts`** -> AI Confidence: **99.23%**
25. **`packages/react/src/types/component-props.ts`** -> AI Confidence: **99.22%**
26. **`packages/system/src/utils/store.ts`** -> AI Confidence: **99.22%**
27. **`packages/system/src/xyresizer/XYResizer.ts`** -> AI Confidence: **99.22%**
28. **`examples/react/src/examples/NodeResizer/CustomResizer.tsx`** -> AI Confidence: **99.2%**
29. **`packages/react/src/additional-components/MiniMap/MiniMapNodes.tsx`** -> AI Confidence: **99.18%**
30. **`examples/react/src/examples/NodeResizer/DefaultResizer.tsx`** -> AI Confidence: **99.17%**
31. **`packages/react/src/additional-components/NodeResizer/types.ts`** -> AI Confidence: **99.17%**
32. **`packages/react/src/additional-components/Controls/Controls.tsx`** -> AI Confidence: **99.16%**
33. **`packages/react/src/container/FlowRenderer/index.tsx`** -> AI Confidence: **99.16%**
34. **`packages/react/src/additional-components/EdgeToolbar/EdgeToolbar.tsx`** -> AI Confidence: **99.15%**
35. **`packages/react/src/components/NodesSelection/index.tsx`** -> AI Confidence: **99.15%**
36. **`packages/react/src/container/ZoomPane/index.tsx`** -> AI Confidence: **99.15%**
37. **`packages/react/src/components/NodeWrapper/utils.tsx`** -> AI Confidence: **99.13%**
38. **`packages/react/src/container/ReactFlow/Wrapper.tsx`** -> AI Confidence: **99.13%**
39. **`packages/react/src/hooks/useNodeConnections.ts`** -> AI Confidence: **99.13%**
40. **`packages/react/src/store/index.ts`** -> AI Confidence: **99.13%**
41. **`packages/svelte/src/lib/store/index.ts`** -> AI Confidence: **99.13%**
42. **`packages/system/src/xypanzoom/eventhandler.ts`** -> AI Confidence: **99.13%**
43. **`examples/react/src/App/routes.ts`** -> AI Confidence: **99.09%**
44. **`packages/react/src/additional-components/Controls/types.ts`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> **100.0%** Exposure
- `packages/system/src/utils/store.ts` -> **100.0%** Exposure
- `packages/system/src/xyresizer/utils.ts` -> **100.0%** Exposure
- `packages/svelte/src/lib/components/NodeWrapper/NodeWrapper.svelte` -> **100.0%** Exposure
- `packages/react/src/hooks/useKeyPress.ts` -> **99.8866%** Exposure
### Weaponizable Injection Vectors
- `packages/svelte/src/lib/types/edges.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `examples/react/src/App/header.tsx` -> **100.0%** Exposure
- `examples/react/src/examples/Stress/index.tsx` -> **100.0%** Exposure
- `examples/react/src/examples/Stress/performanceUtils.ts` -> **100.0%** Exposure
- `packages/react/src/hooks/useKeyPress.ts` -> **100.0%** Exposure
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `743` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT) -> Cumulative Risk: **834.9**
- **Archetype:** `file_cluster_2` (Distance: 13.826 IQR)
- **Magnitude:** 73.39 | **LOC:** 489 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getInitialStore` (Impact: 490.0), `getInitialViewport` (Impact: 30.0), `warnIfDeeplyReactive` (Impact: 10.8)

### 2. `packages/system/src/utils/store.ts` (TYPESCRIPT) -> Cumulative Risk: **760.73**
- **Archetype:** `file_cluster_13` (Distance: 11.829 IQR)
- **Magnitude:** 40.02 | **LOC:** 601 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `handleExpandParent` (Impact: 151.2), `parseHandles` (Impact: 24.1), `calculateChildXYZ` (Impact: 17.6)

### 3. `packages/system/src/xyresizer/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **665.62**
- **Archetype:** `file_cluster_8` (Distance: 10.997 IQR)
- **Magnitude:** 29.43 | **LOC:** 281 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (96.4916%), Verification (80.0%)
- **Heaviest Functions:** `getUpperExtentClamp` (Impact: 216.7), `getUpperExtentClamp` (Impact: 10.7), `getControlDirection` (Impact: 6.7)

### 4. `packages/react/src/store/index.ts` (TYPESCRIPT) -> Cumulative Risk: **564.71**
- **Archetype:** `file_cluster_8` (Distance: 10.774 IQR)
- **Magnitude:** 37.0 | **LOC:** 455 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9775%), Churn (92.51%)
- **Heaviest Functions:** `createWithEqualityFn` (Impact: 335.1), `createStore` (Impact: 1.5)

### 5. `packages/system/src/xydrag/XYDrag.ts` (TYPESCRIPT) -> Cumulative Risk: **554.63**
- **Archetype:** `file_cluster_8` (Distance: 10.558 IQR)
- **Magnitude:** 24.84 | **LOC:** 410 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (87.4118%), Verification (80.0%), Concurrency (78.6807%)
- **Heaviest Functions:** `startDrag` (Impact: 62.3), `autoPan` (Impact: 53.3), `updateNodes` (Impact: 38.6)

### 6. `packages/react/src/components/StoreUpdater/index.tsx` (TYPESCRIPT) -> Cumulative Risk: **543.53**
- **Archetype:** `file_cluster_13` (Distance: 10.07 IQR)
- **Magnitude:** 9.75 | **LOC:** 178 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.913%), Verification (80.0%), State Flux (66.8267%)
- **Heaviest Functions:** `StoreUpdater` (Impact: 75.2), `selector` (Impact: 2.5)

### 7. `packages/react/src/components/NodeWrapper/useNodeObserver.ts` (TYPESCRIPT) -> Cumulative Risk: **526.64**
- **Archetype:** `file_cluster_13` (Distance: 11.53 IQR)
- **Magnitude:** 5.51 | **LOC:** 74 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9985%), Algorithmic Dos (95.7293%)
- **Heaviest Functions:** `useEffect` (Impact: 17.4), `useEffect` (Impact: 11.5), `useEffect` (Impact: 6.8)

### 8. `packages/system/src/utils/node-toolbar.ts` (TYPESCRIPT) -> Cumulative Risk: **517.09**
- **Archetype:** `file_cluster_8` (Distance: 11.396 IQR)
- **Magnitude:** 7.25 | **LOC:** 52 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (93.4364%)
- **Heaviest Functions:** `getNodeToolbarTransform` (Impact: 42.7)

### 9. `packages/react/src/container/Pane/index.tsx` (TYPESCRIPT) -> Cumulative Risk: **504.82**
- **Archetype:** `file_cluster_13` (Distance: 11.648 IQR)
- **Magnitude:** 22.94 | **LOC:** 293 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 61.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Algorithmic Dos (76.9757%), Churn (57.43%)
- **Heaviest Functions:** `onPointerMove` (Impact: 77.8), `onPointerDownCapture` (Impact: 48.8), `onPointerUp` (Impact: 31.2)

### 10. `packages/react/src/hooks/useOnInitHandler.ts` (TYPESCRIPT) -> Cumulative Risk: **498.18**
- **Archetype:** `file_cluster_13` (Distance: 11.978 IQR)
- **Magnitude:** 2.0 | **LOC:** 24 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9955%), State Flux (94.947%), Documentation (82.7308%)
- **Heaviest Functions:** `useOnInitHandler` (Impact: 8.7)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/src/routes/examples/interaction/+page.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.036 IQR)
- **Top Global Matches:** file_cluster_8: 8.036, file_cluster_0: 8.647, file_cluster_7: 8.954
- **Magnitude:** 235.1 | **LOC:** 214 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.6667%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 36`, `args: 25`, `func_start: 8`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/container/Pane/Pane.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.077 IQR)
- **Top Global Matches:** file_cluster_8: 11.077, file_cluster_17: 11.127, file_cluster_13: 11.297
- **Magnitude:** 210.92 | **LOC:** 267 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (33.3235%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onPointerMove` (Impact: 75.4 | O(N^2) | DB: 1)
  * `onPointerDownCapture` (Impact: 30.1 | O(N^1))
    * *Intent:* // We start the selection process when the user clicks down on the pane
  * `onPointerUp` (Impact: 25.2 | O(N^1))
  * `handler` (Impact: 18.5 | O(2^N))
  * `isSetEqual` (Impact: 11.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 41`, `args: 12`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 23`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 24`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001548
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/components/EdgeReconnectAnchor/EdgeReconnectAnchor.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.067 IQR)
- **Top Global Matches:** file_cluster_8: 10.067, file_cluster_13: 10.35, file_cluster_0: 10.628
- **Magnitude:** 170.54 | **LOC:** 130 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (14.2376%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onPointerDown` (Impact: 164.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 20`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `import: 6`
* *Defense:* `safety: 14`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.206
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001548
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/components/Handle/Handle.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.166 IQR)
- **Top Global Matches:** file_cluster_8: 11.166, file_cluster_13: 11.459, file_cluster_0: 11.483
- **Magnitude:** 157.34 | **LOC:** 234 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (28.072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onclick` (Impact: 44.4 | O(N^2))
  * `onpointerdown` (Impact: 38.3 | O(N^2))
  * `handleConnectionChange` (Impact: 38.2 | O(N^2) | DB: 1)
  * `onConnectExtended` (Impact: 8.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 26`, `args: 14`, `func_start: 9`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 25`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00774
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/components/NodeWrapper/NodeWrapper.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.397 IQR)
- **Top Global Matches:** file_cluster_8: 11.397, file_cluster_13: 11.499, file_cluster_0: 11.622
- **Magnitude:** 157.32 | **LOC:** 320 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.0929%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 31.2 | O(N^2))
  * `onFocus` (Impact: 27.3 | O(N^2))
  * `onSelectNodeHandler` (Impact: 15.1 | O(N^1))
  * `requestAnimationFrame` (Impact: 9.5 | O(N^4))
  * `setNodeConnectableContext` (Impact: 8.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 46`, `args: 14`, `func_start: 10`
* *Risk/State:* `state_mutation: 48`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 26`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001548
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/plugins/NodeResizer/ResizeControl.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.569 IQR)
- **Top Global Matches:** file_cluster_8: 11.569, file_cluster_13: 11.607, file_cluster_0: 11.824
- **Magnitude:** 121.8 | **LOC:** 139 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (48.6123%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onMount` (Impact: 93.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 27`, `args: 8`, `func_start: 3`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `import: 5`
* *Defense:* `safety: 13`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.826 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.4 IQR)
- **Top Global Matches:** file_cluster_2: 13.826, file_cluster_17: 13.853, file_cluster_13: 13.895
- **Magnitude:** 73.39 | **LOC:** 489 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (83.549%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getInitialStore` (Impact: 490.0 | O(N^3) | DB: 77)
  * `getInitialViewport` (Impact: 30.0 | O(N^1))
  * `warnIfDeeplyReactive` (Impact: 10.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 75`, `args: 30`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 179`
* *Architecture:* `api: 4`, `concurrency: 12`, `import: 10`
* *Defense:* `safety: 46`, `doc: 4`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DefaultNode.svelte, GroupNode.svelte, types, reactivity, types, visibleElements, edges, OutputNode.svelte...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/components/KeyHandler/KeyHandler.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.544 IQR)
- **Top Global Matches:** file_cluster_8: 9.544, file_cluster_13: 9.811, file_cluster_17: 9.813
- **Magnitude:** 55.34 | **LOC:** 133 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.0139%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 12.7 | O(2^N))
  * `getKeyString` (Impact: 12.6 | O(N^1))
  * `getModifier` (Impact: 9.9 | O(N^1))
  * `isKeyObject` (Impact: 7.5 | O(N^1))
  * `handleDelete` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 18`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/components/EdgeWrapper/EdgeWrapper.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.747 IQR)
- **Top Global Matches:** file_cluster_8: 9.747, file_cluster_13: 9.956, file_cluster_0: 10.162
- **Magnitude:** 54.26 | **LOC:** 174 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.1272%), Tech Debt (82.9907%)
**Top Internal Functions/Classes:**
  * `onkeydown` (Impact: 21.6 | O(N^2))
  * `onclick` (Impact: 8.4 | O(N^1))
  * `callback` (Impact: 1.1 | O(N^1))
  * `callback` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 6`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001548
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/types/panzoom.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.61 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.5 IQR)
- **Top Global Matches:** file_cluster_8: 10.61, file_cluster_13: 10.912, file_cluster_4: 11.094
- **Magnitude:** 53.59 | **LOC:** 66 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.5636%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 36`, `args: 16`, `func_start: 11`
* *Risk/State:* None
* *Architecture:* `api: 7`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.038
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003096
  * `Imports (Out-Degree: 0):` , d3-zoom
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/store/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.285 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.071 IQR)
- **Top Global Matches:** file_cluster_8: 10.285, file_cluster_17: 10.578, file_cluster_13: 10.676
- **Magnitude:** 42.2 | **LOC:** 420 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 70.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (23.0015%), Tech Debt (9.9777%)
**Top Internal Functions/Classes:**
  * `createStore` (Impact: 395.3 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 56`, `args: 42`, `func_start: 37`
* *Risk/State:* `state_mutation: 10`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 20`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, types, useStore, initial-store.svelte, system
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/hooks/useSvelteFlow.svelte.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.836 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.039 IQR)
- **Top Global Matches:** file_cluster_8: 11.836, file_cluster_2: 11.859, file_cluster_16: 11.862
- **Magnitude:** 42.09 | **LOC:** 578 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.01%), Tech Debt (9.9301%)
**Top Internal Functions/Classes:**
  * `getInternalNode` (Impact: 340.6 | O(2^N))
    * *Intent:* /** * Converts a screen / client position to a flow position.
  * `useSvelteFlow` (Impact: 35.9 | O(N^1))
    * *Intent:* /**
  * `getElements` (Impact: 10.7 | O(N^1) | DB: 1)
  * `updateNode` (Impact: 1.9 | O(N^1))
    * *Intent:* /** * Checks if the given node or rect intersects with the passed rect. * * @param node - the node o...
  * `updateEdge` (Impact: 1.9 | O(N^1))
    * *Intent:* /** * Deletes nodes and edges.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 115`, `args: 65`, `func_start: 51`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 24`, `doc: 91`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` store, types, svelte, utils, system
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/plugins/Background/Background.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.527 IQR)
- **Top Global Matches:** file_cluster_13: 11.527, file_cluster_8: 11.532, file_cluster_0: 11.622
- **Magnitude:** 40.26 | **LOC:** 72 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.9527%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 15`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `import: 4`
* *Defense:* `safety: 5`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/system/src/utils/store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.829 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.564 IQR)
- **Top Global Matches:** file_cluster_13: 11.829, file_cluster_8: 11.842, file_cluster_2: 11.858
- **Magnitude:** 40.02 | **LOC:** 601 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (35.5664%), Tech Debt (51.7996%)
**Top Internal Functions/Classes:**
  * `handleExpandParent` (Impact: 151.2 | O(N^4) | DB: 4)
  * `parseHandles` (Impact: 24.1 | O(N^1) | DB: 2)
  * `calculateChildXYZ` (Impact: 17.6 | O(N^1) | DB: 1)
  * `addConnectionToLookup` (Impact: 14.4 | O(N^1) | DB: 7)
  * `updateAbsolutePositions` (Impact: 12.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 53`, `args: 22`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `dead_code: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 12`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 15`, `doc: 8`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types, general, .., dom, types, graph
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/container/SvelteFlow/SvelteFlow.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.13 IQR)
- **Top Global Matches:** file_cluster_8: 7.13, file_cluster_13: 7.566, file_cluster_2: 7.883
- **Magnitude:** 37.48 | **LOC:** 227 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.2655%), Tech Debt (99.3901%)
**Top Internal Functions/Classes:**
  * `untrack` (Impact: 5.4 | O(N^1))
  * `nodes` (Impact: 3.6 | O(2^N))
  * `nodes` (Impact: 3.6 | O(2^N))
  * `edges` (Impact: 3.6 | O(2^N))
  * `edges` (Impact: 3.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 33`, `args: 10`, `func_start: 11`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 6`
* *Architecture:* `import: 19`
* *Defense:* `safety: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003096
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react/src/store/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.774 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.161 IQR)
- **Top Global Matches:** file_cluster_8: 10.774, file_cluster_13: 11.233, file_cluster_17: 11.383
- **Magnitude:** 37.0 | **LOC:** 455 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (20.9359%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createWithEqualityFn` (Impact: 335.1 | O(N^4) | DB: 6)
  * `createStore` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 46`, `args: 63`, `func_start: 59`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 1`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` initialState, system, changes, types, traditional
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/plugins/NodeToolbar/NodeToolbar.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.479 IQR)
- **Top Global Matches:** file_cluster_13: 11.479, file_cluster_17: 11.55, file_cluster_8: 11.768
- **Magnitude:** 35.34 | **LOC:** 85 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (61.1311%), Tech Debt (83.2643%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 23`, `args: 7`
* *Risk/State:* `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 7`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/src/routes/examples/stress/+page.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.976 IQR)
- **Top Global Matches:** file_cluster_8: 9.976, file_cluster_0: 10.486, file_cluster_13: 10.505
- **Magnitude:** 32.96 | **LOC:** 58 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (70.6017%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 7`, `args: 2`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/components/NodeSelection/NodeSelection.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.78 IQR)
- **Top Global Matches:** file_cluster_8: 9.78, file_cluster_13: 9.816, file_cluster_17: 9.914
- **Magnitude:** 31.54 | **LOC:** 106 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.6849%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `filter` (Impact: 8.0 | O(N^2))
  * `onkeydown` (Impact: 6.3 | O(N^1))
  * `oncontextmenu` (Impact: 4.2 | O(N^1))
  * `onclick` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 8`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `import: 6`
* *Defense:* `safety: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/src/routes/examples/overview/Flow.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.805 IQR)
- **Top Global Matches:** file_cluster_8: 7.805, file_cluster_13: 8.479, file_cluster_0: 8.594
- **Magnitude:** 30.56 | **LOC:** 278 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.2102%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changeEdgeType` (Impact: 7.3 | O(N^1))
  * `moveNode` (Impact: 2.1 | O(N^1))
  * `hideUnhide` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `args: 11`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/svelte/src/routes/tests/generic/[topic]/[example]/Flow.svelte` (HTML) | Magnitude: 24.58 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 25, state_mutation: 9, branch: 6, structural_boundaries: 5
- `packages/react/src/utils/changes.ts` (TYPESCRIPT) | Magnitude: 15.85 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 35, branch: 23, immutability_locks: 17
- `examples/svelte/src/app.d.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 6, branch: 5, generics: 2
- `examples/svelte/svelte.config.js` (JAVASCRIPT) | Magnitude: 16.3 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 3, doc: 2, decorators: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/svelte/src/lib/actions/portal/portal.svelte.ts` (TYPESCRIPT) | Magnitude: 3.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 30, args: 10, branch: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/react/src/components/StoreUpdater/index.tsx` (TYPESCRIPT) | Magnitude: 9.75 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, branch: 23, structural_boundaries: 23, state_mutation: 16
- `packages/svelte/src/lib/plugins/Background/Background.svelte` (HTML) | Magnitude: 40.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, state_mutation: 24, structural_boundaries: 15, branch: 9
- `packages/react/src/components/ReactFlowProvider/index.tsx` (TYPESCRIPT) | Magnitude: 0.61 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 13, doc: 11, branch: 10
- `packages/system/src/utils/store.ts` (TYPESCRIPT) | Magnitude: 40.02 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 430, branch: 131, state_mutation: 86, immutability_locks: 77
- `packages/svelte/src/lib/hooks/useNodeConnections.svelte.ts` (TYPESCRIPT) | Magnitude: 2.0 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 16, branch: 15, doc: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/system/src/types/nodes.ts` (TYPESCRIPT) | Magnitude: 3.37 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 40, branch: 35, doc: 25
- `packages/react/src/types/edges.ts` (TYPESCRIPT) | Magnitude: 4.68 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 63, branch: 60, generics: 48
- `packages/svelte/src/lib/types/events.ts` (TYPESCRIPT) | Magnitude: 2.41 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 37, indent_spaces: 32, generics: 17, branch: 16
- `packages/system/src/xyresizer/types.ts` (TYPESCRIPT) | Magnitude: 2.85 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 28, api: 13, indent_spaces: 7, doc: 6
- `packages/react/src/types/general.ts` (TYPESCRIPT) | Magnitude: 2.48 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 71, indent_spaces: 52, doc: 46, generics: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/react/src/examples/MultiSetNodes/index.tsx` (TYPESCRIPT) | Magnitude: 2.1 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 21, args: 14, ui_framework: 10
- `examples/svelte/src/routes/examples/node-toolbar/SelectedNodesToolbar.svelte` (HTML) | Magnitude: 18.22 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 6, state_mutation: 3, args: 2
- `packages/react/src/hooks/useReactFlow.ts` (TYPESCRIPT) | Magnitude: 23.55 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 234, structural_boundaries: 79, branch: 57, args: 45
- `examples/react/src/examples/NodeToolbar/SelectedNodesToolbar.tsx` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, args: 5, immutability_locks: 3
- `examples/react/src/examples/EdgeToolbar/CustomEdge.tsx` (TYPESCRIPT) | Magnitude: 4.15 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, branch: 12, structural_boundaries: 12, ui_framework: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/react/src/examples/CancelConnection/hooks/useCountdown.ts` (TYPESCRIPT) | Magnitude: 1.81 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 10, args: 10, func_start: 9
- `examples/react/src/examples/CustomNode/ColorSelectorNode.tsx` (TYPESCRIPT) | Magnitude: 0.41 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, ui_framework: 9, args: 7
- `packages/react/src/additional-components/MiniMap/types.ts` (TYPESCRIPT) | Magnitude: 1.87 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, branch: 20, doc: 19, structural_boundaries: 18
- `examples/react/src/examples/AddNodeOnEdgeDrop/index.tsx` (TYPESCRIPT) | Magnitude: 3.51 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, immutability_locks: 16, structural_boundaries: 15, ui_framework: 12
- `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT) | Magnitude: 73.39 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 380, state_mutation: 179, branch: 134, ui_framework: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/react/src/examples/Stress/performanceUtils.ts` (TYPESCRIPT) | Magnitude: 9.37 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 82, concurrency: 38, state_mutation: 21, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/react/src/additional-components/MiniMap/MiniMapNodes.tsx` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 25, ui_framework: 16, generics: 14
- `packages/react/src/types/store.ts` (TYPESCRIPT) | Magnitude: 0.93 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 64, ui_framework: 33, generics: 32
- `examples/react/cypress/components/hooks/useEdges.cy.tsx` (TYPESCRIPT) | Magnitude: 0.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 10, args: 6, func_start: 6
- `examples/react/src/examples/Validation/index.tsx` (TYPESCRIPT) | Magnitude: 1.17 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 26, ui_framework: 17, args: 14
- `examples/react/src/examples/NodeResizer/HorizontalResizer.tsx` (TYPESCRIPT) | Magnitude: 0.29 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 37, indent_spaces: 33, safety: 18, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/svelte/src/routes/+page.svelte.d.ts` (TYPESCRIPT) | Magnitude: 1.61 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 7, doc: 6, api: 4, dead_code: 2
- `packages/system/src/xypanzoom/filter.ts` (TYPESCRIPT) | Magnitude: 1.49 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 71, branch: 43, structural_boundaries: 24, dead_code: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/system/src/utils/store.ts` -> Churn: **100.0%** | Cog Load: 35.5664% | Debt: 51.7996%
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> Churn: **79.25%** | Cog Load: 83.549% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/svelte/src/lib/components/NodeWrapper/NodeWrapper.svelte` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 157.32
- `packages/svelte/src/lib/plugins/NodeResizer/ResizeControl.svelte` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 121.8
- `packages/svelte/src/lib/components/KeyHandler/KeyHandler.svelte` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 55.34
- `packages/svelte/src/lib/components/EdgeWrapper/EdgeWrapper.svelte` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 54.26
- `packages/system/src/types/panzoom.ts` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 53.59

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react/src/hooks/useOnInitHandler.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 94.947%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/react/src/hooks/useReactFlow.ts` -> **Severity: 0.316** (Embedded: 0.007 * Error Risk: 45.2949%)
- `packages/react/src/hooks/useKeyPress.ts` -> **Severity: 0.211** (Embedded: 0.0062 * Error Risk: 34.1429%)
- `packages/system/src/utils/graph.ts` -> **Severity: 0.197** (Embedded: 0.0046 * Error Risk: 42.4315%)
- `packages/react/src/hooks/useMoveSelectedNodes.ts` -> **Severity: 0.181** (Embedded: 0.0031 * Error Risk: 58.3583%)
- `packages/react/src/additional-components/MiniMap/MiniMapNodes.tsx` -> **Severity: 0.158** (Embedded: 0.0028 * Error Risk: 56.6798%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/svelte/src/lib/store/context.ts` -> **Severity: 297.5** (Blast Radius: 2.975 * Doc Risk: 100.0%)
- `packages/system/src/xypanzoom/eventhandler.ts` -> **Severity: 249.325** (Blast Radius: 3.009 * Doc Risk: 82.8596%)
- `packages/react/src/contexts/NodeIdContext.ts` -> **Severity: 219.179** (Blast Radius: 3.653 * Doc Risk: 59.9997%)
- `packages/svelte/src/lib/store/visibleElements.ts` -> **Severity: 203.8** (Blast Radius: 2.038 * Doc Risk: 100.0%)
- `packages/system/src/types/panzoom.ts` -> **Severity: 203.8** (Blast Radius: 2.038 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
