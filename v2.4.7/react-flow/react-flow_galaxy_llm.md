# ARCHITECTURAL_BRIEF: react-flow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/react-flow` |
| **Timestamp** | `2026-08-07T04:27:40.008757+00:00` |
| **Scan Duration** | `1.35s` |
| **Git Branch** | `main` |
| **Git Commit** | `a58568f11bc0e1a1bdca1b3549e959e2e1ca0cdd` |
| **Git Remote** | `https://github.com/wbkd/react-flow.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 444 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.407`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 389 | 60.1% |
| file_cluster_13 | 169 | 26.1% |
| file_cluster_2 | 26 | 4.0% |
| file_cluster_17 | 12 | 1.9% |
| file_cluster_16 | 9 | 1.4% |
| Unknown | 5 | 0.8% |
| file_cluster_0 | 4 | 0.6% |
| file_cluster_4 | 3 | 0.5% |
| file_cluster_9 | 2 | 0.3% |

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
| Cognitive Load Exposure | 0.0 | 96.6 | 10.9 | 5.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 93.4 | 22.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.8 | 0.2 | 0.0 |
| API Exposure | 0.0 | 19.4 | 4.2 | 3.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 93.0 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.5 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 16.7 | 3.2 | 0.0 |
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

- `getInitialStore` (@ `packages/svelte/src/lib/store/initial-store.svelte.ts`) -> Impact: **184.9** | LOC: 360
- `createStore` (@ `packages/svelte/src/lib/store/index.ts`) -> Impact: **152.2** | LOC: 386
- `createWithEqualityFn` (@ `packages/react/src/store/index.ts`) -> Impact: **122.3** | LOC: 381
- `getInternalNode` (@ `packages/svelte/src/lib/hooks/useSvelteFlow.svelte.ts`) -> Impact: **120.6** | LOC: 212
  * *Intent:* /** * Converts a screen / client position to a flow position.
- `useReactFlow` (@ `packages/react/src/hooks/useReactFlow.ts`) -> Impact: **94.7** | LOC: 254
  * *Intent:* /**
- `getNodesInside` (@ `packages/system/src/utils/graph.ts`) -> Impact: **68.1** | LOC: 40
  * *Intent:* /**
- `handleExpandParent` (@ `packages/system/src/utils/store.ts`) -> Impact: **57.9** | LOC: 84
- `useViewportHelper` (@ `packages/react/src/hooks/useViewportHelper.ts`) -> Impact: **57.1** | LOC: 103
  * *Intent:* /**
- `getUpperExtentClamp` (@ `packages/system/src/xyresizer/utils.ts`) -> Impact: **55.5** | LOC: 35
- `describe` (@ `examples/react/cypress/components/utils/adopt-user-nodes.cy.ts`) -> Impact: **55.0** | LOC: 199

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/svelte` | 9 | 10072.08 | 2.38% | 0.0% |
| `examples/svelte` | 8 | 5053.21 | 4.32% | 0.0% |
| `__monolith__` | 10 | 5051.44 | 2.0% | 0.0% |
| `packages/react` | 5 | 5040.7 | 1.0% | 0.0% |
| `packages/system/src/types` | 8 | 295.86 | 7.7% | 0.0% |
| `examples/svelte/src/routes/examples/interaction` | 1 | 235.1 | 9.67% | 0.0% |
| `packages/svelte/src/lib/container/Pane` | 3 | 196.34 | 14.44% | 0.0% |
| `packages/svelte/src/lib/components/NodeWrapper` | 3 | 134.89 | 17.36% | 0.0% |
| `packages/svelte/src/lib/plugins/NodeResizer` | 4 | 125.64 | 18.84% | 0.0% |
| `packages/svelte/src/lib/components/Handle` | 3 | 121.71 | 12.69% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/react/src/hooks/useOnEdgesChangeMiddleware.ts` -> **100.0%** Exposure
- `packages/react/src/hooks/useOnNodesChangeMiddleware.ts` -> **100.0%** Exposure
- `packages/react/src/hooks/useOnViewportChange.ts` -> **100.0%** Exposure
- `packages/svelte/src/lib/actions/portal/portal.svelte.ts` -> **100.0%** Exposure
- `packages/svelte/src/lib/components/edges/index.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/react/src/components/BatchProvider/types.ts` -> **100.0%** Exposure
- `packages/react/src/components/Edges/EdgeAnchor.tsx` -> **100.0%** Exposure
- `packages/react/src/components/NodeWrapper/useNodeObserver.ts` -> **100.0%** Exposure
- `packages/react/src/components/Nodes/utils.ts` -> **100.0%** Exposure
- `packages/system/src/utils/marker.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/react/cypress/components/reactflow/basic-props.cy.tsx` -> **0** Orphaned Functions | **32** Duplicates
- `packages/react/src/store/index.ts` -> **12** Orphaned Functions | **20** Duplicates
- `examples/react/cypress/components/reactflow/view-props.cy.tsx` -> **0** Orphaned Functions | **29** Duplicates
- `examples/react/cypress/e2e/interaction.cy.ts` -> **2** Orphaned Functions | **21** Duplicates
- `examples/react/cypress/components/reactflow/event-handlers.cy.tsx` -> **0** Orphaned Functions | **21** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `743` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT) -> Cumulative Risk: **696.55**
- **Archetype:** `file_cluster_2` (Distance: 13.775 IQR)
- **Magnitude:** 48.09 | **LOC:** 489 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (96.6391%), State Flux (85.0%), Verification (80.0%)
- **Heaviest Functions:** `getInitialStore` (Impact: 184.9), `getInitialViewport` (Impact: 30.0), `filter` (Impact: 12.4)

### 2. `packages/system/src/utils/store.ts` (TYPESCRIPT) -> Cumulative Risk: **589.53**
- **Archetype:** `file_cluster_13` (Distance: 11.835 IQR)
- **Magnitude:** 31.64 | **LOC:** 601 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Verification (80.0%), State Flux (69.6135%)
- **Heaviest Functions:** `handleExpandParent` (Impact: 57.9), `parseHandles` (Impact: 24.1), `calculateChildXYZ` (Impact: 17.6)

### 3. `packages/react/src/store/index.ts` (TYPESCRIPT) -> Cumulative Risk: **513.26**
- **Archetype:** `file_cluster_8` (Distance: 10.865 IQR)
- **Magnitude:** 34.78 | **LOC:** 455 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Churn (92.51%), Verification (80.0%)
- **Heaviest Functions:** `createWithEqualityFn` (Impact: 122.3), `updateNodePositions` (Impact: 35.6), `updateNodeInternals` (Impact: 16.1)

### 4. `packages/system/src/xyresizer/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **499.43**
- **Archetype:** `file_cluster_8` (Distance: 11.037 IQR)
- **Magnitude:** 23.31 | **LOC:** 281 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9359%), State Flux (96.4916%), Verification (80.0%)
- **Heaviest Functions:** `getUpperExtentClamp` (Impact: 55.5), `getUpperExtentClamp` (Impact: 38.1), `getLowerExtentClamp` (Impact: 32.5)

### 5. `packages/svelte/src/lib/actions/portal/portal.svelte.ts` (TYPESCRIPT) -> Cumulative Risk: **498.94**
- **Archetype:** `file_cluster_4` (Distance: 15.817 IQR)
- **Magnitude:** 5.36 | **LOC:** 47 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Dead Code (72.9345%), Documentation (66.3818%)
- **Heaviest Functions:** `portal` (Impact: 11.9), `tryToMount` (Impact: 10.6), `tryToMount` (Impact: 8.8)

### 6. `packages/react/src/components/StoreUpdater/index.tsx` (TYPESCRIPT) -> Cumulative Risk: **493.54**
- **Archetype:** `file_cluster_13` (Distance: 10.012 IQR)
- **Magnitude:** 10.63 | **LOC:** 178 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (85.2622%), Verification (80.0%), State Flux (66.8267%)
- **Heaviest Functions:** `useIsomorphicLayoutEffect` (Impact: 42.9), `StoreUpdater` (Impact: 37.1), `selector` (Impact: 2.5)

### 7. `packages/svelte/src/lib/hooks/useSvelteFlow.svelte.ts` (TYPESCRIPT) -> Cumulative Risk: **491.21**
- **Archetype:** `file_cluster_8` (Distance: 11.805 IQR)
- **Magnitude:** 28.36 | **LOC:** 578 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9993%), Concurrency (87.6104%), Verification (80.0%)
- **Heaviest Functions:** `getInternalNode` (Impact: 120.6), `useSvelteFlow` (Impact: 30.2), `fitBounds` (Impact: 16.7)

### 8. `packages/svelte/src/lib/store/index.ts` (TYPESCRIPT) -> Cumulative Risk: **487.75**
- **Archetype:** `file_cluster_8` (Distance: 10.247 IQR)
- **Magnitude:** 41.48 | **LOC:** 420 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.5072%), Verification (80.0%), Concurrency (47.1304%)
- **Heaviest Functions:** `createStore` (Impact: 152.2), `updateNodeInternals` (Impact: 35.4), `moveSelectedNodes` (Impact: 26.5)

### 9. `packages/react/src/hooks/useReactFlow.ts` (TYPESCRIPT) -> Cumulative Risk: **465.24**
- **Archetype:** `file_cluster_17` (Distance: 10.749 IQR)
- **Magnitude:** 24.19 | **LOC:** 316 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.6305%), Verification (80.0%), Documentation (65.2935%)
- **Heaviest Functions:** `useReactFlow` (Impact: 94.7), `getIntersectingNodes` (Impact: 25.4), `isNodeIntersecting` (Impact: 12.8)

### 10. `packages/system/src/xydrag/XYDrag.ts` (TYPESCRIPT) -> Cumulative Risk: **460.04**
- **Archetype:** `file_cluster_8` (Distance: 10.562 IQR)
- **Magnitude:** 23.28 | **LOC:** 410 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9815%), Verification (80.0%), Safety Score (47.4046%)
- **Heaviest Functions:** `startDrag` (Impact: 42.3), `updateNodes` (Impact: 20.2), `autoPan` (Impact: 18.6)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `packages/system/src/types/general.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.198 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.932 IQR)
- **Top Global Matches:** file_cluster_13: 11.198, file_cluster_8: 11.257, file_cluster_16: 11.325
- **Magnitude:** 227.2 | **LOC:** 380 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (5.4255%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 176`, `args: 27`, `func_start: 1`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 64`, `concurrency: 7`, `import: 10`
* *Defense:* `safety: 34`, `doc: 46`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` d3-selection, handles, panzoom, .., nodes, d3-drag, d3-zoom, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/container/Pane/Pane.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.074 IQR)
- **Top Global Matches:** file_cluster_8: 11.074, file_cluster_17: 11.124, file_cluster_13: 11.294
- **Magnitude:** 193.42 | **LOC:** 267 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (33.3235%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onPointerMove` (Impact: 51.4)
  * `onPointerDownCapture` (Impact: 30.1)
    * *Intent:* // We start the selection process when the user clicks down on the pane
  * `onPointerUp` (Impact: 25.2)
  * `getNodesInside` (Impact: 21.9)
  * `onClick` (Impact: 8.7)
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

### `packages/svelte/src/lib/components/NodeWrapper/NodeWrapper.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.388 IQR)
- **Top Global Matches:** file_cluster_8: 11.388, file_cluster_13: 11.491, file_cluster_0: 11.614
- **Magnitude:** 132.02 | **LOC:** 320 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (42.0929%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 21.2)
  * `onFocus` (Impact: 18.7)
  * `onSelectNodeHandler` (Impact: 15.1)
  * `setNodeConnectableContext` (Impact: 5.7)
  * `onDestroy` (Impact: 5.4)
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

### `packages/svelte/src/lib/components/Handle/Handle.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.166 IQR)
- **Top Global Matches:** file_cluster_8: 11.166, file_cluster_13: 11.459, file_cluster_0: 11.483
- **Magnitude:** 118.84 | **LOC:** 234 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (28.072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onclick` (Impact: 30.4)
  * `handleConnectionChange` (Impact: 26.0)
  * `onpointerdown` (Impact: 26.0)
  * `onConnectExtended` (Impact: 8.5)
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

### `packages/svelte/src/lib/plugins/NodeResizer/ResizeControl.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.573 IQR)
- **Top Global Matches:** file_cluster_13: 11.573, file_cluster_8: 11.591, file_cluster_0: 11.767
- **Magnitude:** 105.7 | **LOC:** 139 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.6123%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onMount` (Impact: 38.8)
  * `onChange` (Impact: 30.8)
  * `getStoreItems` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 27`, `args: 8`, `func_start: 3`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 13`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/components/EdgeReconnectAnchor/EdgeReconnectAnchor.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.067 IQR)
- **Top Global Matches:** file_cluster_8: 10.067, file_cluster_13: 10.288, file_cluster_0: 10.542
- **Magnitude:** 70.84 | **LOC:** 130 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (14.2376%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onPointerDown` (Impact: 44.1)
  * `onConnect` (Impact: 9.3)
  * `OnConnectStart` (Impact: 5.4)
  * `onReconnectEnd` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 20`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 14`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.206
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001548
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/types/panzoom.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.61 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.5 IQR)
- **Top Global Matches:** file_cluster_8: 10.61, file_cluster_13: 10.912, file_cluster_4: 11.094
- **Magnitude:** 53.59 | **LOC:** 66 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
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

### `packages/svelte/src/lib/components/KeyHandler/KeyHandler.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.526 IQR)
- **Top Global Matches:** file_cluster_8: 9.526, file_cluster_13: 9.795, file_cluster_17: 9.796
- **Magnitude:** 48.54 | **LOC:** 133 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.0139%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getKeyString` (Impact: 12.6)
  * `getModifier` (Impact: 9.9)
  * `isKeyObject` (Impact: 7.5)
  * `callback` (Impact: 4.7)
  * `handleDelete` (Impact: 2.2)
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
- **Global Archetype:** `file_cluster_8` (Drift: 9.736 IQR)
- **Top Global Matches:** file_cluster_8: 9.736, file_cluster_13: 9.946, file_cluster_0: 10.153
- **Magnitude:** 48.46 | **LOC:** 174 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.1272%), Tech Debt (82.9907%)
**Top Internal Functions/Classes:**
  * `onkeydown` (Impact: 14.7)
  * `onclick` (Impact: 8.4)
  * `callback` (Impact: 1.1)
  * `callback` (Impact: 1.1)
  * `unselectNodesAndEdges` (Impact: 1.1)
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

### `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.775 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.368 IQR)
- **Top Global Matches:** file_cluster_2: 13.775, file_cluster_17: 13.789, file_cluster_13: 13.824
- **Magnitude:** 48.09 | **LOC:** 489 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (96.6391%), Tech Debt (76.9183%)
**Top Internal Functions/Classes:**
  * `getInitialStore` (Impact: 184.9)
  * `getInitialViewport` (Impact: 30.0)
  * `filter` (Impact: 12.4)
  * `warnIfDeeplyReactive` (Impact: 10.8)
  * `resolveFitView` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 75`, `args: 30`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 177`, `duplicate_logic: 6`
* *Architecture:* `api: 8`, `concurrency: 12`, `import: 10`
* *Defense:* `safety: 46`, `doc: 4`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` InputNode.svelte, visibleElements, GroupNode.svelte, edges, DefaultNode.svelte, system, types, reactivity...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/store/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.247 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.089 IQR)
- **Top Global Matches:** file_cluster_8: 10.247, file_cluster_17: 10.512, file_cluster_13: 10.623
- **Magnitude:** 41.48 | **LOC:** 420 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 70.0%
- **Risk Profile:** Cognitive Load (37.4697%), Tech Debt (99.5072%)
**Top Internal Functions/Classes:**
  * `createStore` (Impact: 152.2)
  * `updateNodeInternals` (Impact: 35.4)
  * `moveSelectedNodes` (Impact: 26.5)
  * `handleNodeSelection` (Impact: 20.9)
  * `handleEdgeSelection` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 56`, `args: 42`, `func_start: 37`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 10`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 20`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` useStore, initial-store.svelte, system, types, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/plugins/Background/Background.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.527 IQR)
- **Top Global Matches:** file_cluster_13: 11.527, file_cluster_8: 11.532, file_cluster_0: 11.622
- **Magnitude:** 40.26 | **LOC:** 72 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
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

### `packages/svelte/src/lib/plugins/NodeToolbar/NodeToolbar.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.479 IQR)
- **Top Global Matches:** file_cluster_13: 11.479, file_cluster_17: 11.55, file_cluster_8: 11.768
- **Magnitude:** 35.34 | **LOC:** 85 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
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

### `packages/react/src/store/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.865 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.454 IQR)
- **Top Global Matches:** file_cluster_8: 10.865, file_cluster_13: 11.293, file_cluster_17: 11.427
- **Magnitude:** 34.78 | **LOC:** 455 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (34.5022%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `createWithEqualityFn` (Impact: 122.3)
  * `updateNodePositions` (Impact: 35.6)
  * `updateNodeInternals` (Impact: 16.1)
  * `setCenter` (Impact: 15.0)
  * `setNodes` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 46`, `args: 63`, `func_start: 59`
* *Risk/State:* `state_mutation: 18`, `duplicate_logic: 20`, `orphaned_logic: 12`
* *Architecture:* `api: 1`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` initialState, changes, system, traditional, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/src/routes/examples/stress/+page.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.976 IQR)
- **Top Global Matches:** file_cluster_8: 9.976, file_cluster_0: 10.486, file_cluster_13: 10.505
- **Magnitude:** 32.96 | **LOC:** 58 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
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

### `examples/svelte/src/routes/examples/overview/Flow.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.805 IQR)
- **Top Global Matches:** file_cluster_8: 7.805, file_cluster_13: 8.479, file_cluster_0: 8.594
- **Magnitude:** 32.36 | **LOC:** 278 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.4353%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changeEdgeType` (Impact: 7.3)
  * `moveNode` (Impact: 2.1)
  * `hideUnhide` (Impact: 1.9)
  * `updateNode` (Impact: 1.8)
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

### `packages/system/src/utils/store.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.835 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.566 IQR)
- **Top Global Matches:** file_cluster_13: 11.835, file_cluster_8: 11.849, file_cluster_2: 11.865
- **Magnitude:** 31.64 | **LOC:** 601 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (35.5664%), Tech Debt (64.2543%)
**Top Internal Functions/Classes:**
  * `handleExpandParent` (Impact: 57.9)
  * `parseHandles` (Impact: 24.1)
  * `calculateChildXYZ` (Impact: 17.6)
  * `addConnectionToLookup` (Impact: 14.4)
  * `updateAbsolutePositions` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 53`, `args: 23`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 12`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 15`, `doc: 8`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dom, general, .., graph, types, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/container/SvelteFlow/SvelteFlow.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.124 IQR)
- **Top Global Matches:** file_cluster_8: 7.124, file_cluster_13: 7.527, file_cluster_2: 7.873
- **Magnitude:** 29.58 | **LOC:** 227 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (7.2746%), Tech Debt (99.3901%)
**Top Internal Functions/Classes:**
  * `untrack` (Impact: 5.4)
  * `setContext` (Impact: 2.0)
    * *Intent:* // Overwrite store context to give children direct access
  * `nodes` (Impact: 1.9)
  * `nodes` (Impact: 1.9)
  * `edges` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 33`, `args: 10`, `func_start: 11`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003096
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/container/SvelteFlow/Wrapper.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.394 IQR)
- **Top Global Matches:** file_cluster_8: 7.394, file_cluster_13: 7.581, file_cluster_2: 8.018
- **Magnitude:** 29.34 | **LOC:** 160 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.3315%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 9`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 1`, `test: 1`
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
- `packages/react/src/utils/changes.ts` (TYPESCRIPT) | Magnitude: 10.45 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 35, branch: 23, immutability_locks: 17
- `examples/svelte/src/app.d.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 6, branch: 5, generics: 2
- `examples/svelte/svelte.config.js` (JAVASCRIPT) | Magnitude: 16.3 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 3, doc: 2, decorators: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/svelte/src/lib/plugins/Background/Background.svelte` (HTML) | Magnitude: 40.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, state_mutation: 24, structural_boundaries: 15, branch: 9
- `examples/react/cypress/components/hooks/useEdges.cy.tsx` (TYPESCRIPT) | Magnitude: 1.09 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 10, args: 6, func_start: 6
- `packages/react/src/components/ReactFlowProvider/index.tsx` (TYPESCRIPT) | Magnitude: 0.61 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 13, doc: 11, branch: 10
- `packages/react/src/components/StoreUpdater/index.tsx` (TYPESCRIPT) | Magnitude: 10.63 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, branch: 23, structural_boundaries: 23, state_mutation: 16
- `packages/system/src/utils/store.ts` (TYPESCRIPT) | Magnitude: 31.64 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 430, branch: 131, state_mutation: 86, immutability_locks: 77

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
- `examples/react/src/examples/MultiSetNodes/index.tsx` (TYPESCRIPT) | Magnitude: 2.86 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 21, args: 13, ui_framework: 10
- `examples/svelte/src/routes/examples/node-toolbar/SelectedNodesToolbar.svelte` (HTML) | Magnitude: 18.22 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 6, state_mutation: 3, args: 2
- `packages/react/src/hooks/useReactFlow.ts` (TYPESCRIPT) | Magnitude: 24.19 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 234, structural_boundaries: 79, branch: 57, immutability_locks: 44
- `examples/react/src/examples/NodeToolbar/SelectedNodesToolbar.tsx` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, args: 4, immutability_locks: 3
- `examples/react/src/examples/EdgeToolbar/CustomEdge.tsx` (TYPESCRIPT) | Magnitude: 3.61 | Delta: **0.169 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, branch: 12, structural_boundaries: 12, ui_framework: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/react/src/examples/CustomNode/ColorSelectorNode.tsx` (TYPESCRIPT) | Magnitude: 0.41 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, ui_framework: 9, args: 7
- `packages/react/src/additional-components/MiniMap/types.ts` (TYPESCRIPT) | Magnitude: 1.87 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, branch: 20, doc: 19, structural_boundaries: 18
- `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT) | Magnitude: 48.09 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 380, state_mutation: 177, branch: 134, ui_framework: 87
- `examples/react/src/examples/AddNodeOnEdgeDrop/index.tsx` (TYPESCRIPT) | Magnitude: 2.64 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, immutability_locks: 16, structural_boundaries: 15, ui_framework: 12
- `packages/svelte/src/lib/components/NodeSelection/types.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, ui_framework: 5, generics: 5, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/svelte/src/lib/actions/portal/portal.svelte.ts` (TYPESCRIPT) | Magnitude: 5.36 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 30, args: 10, branch: 9, structural_boundaries: 8
- `examples/react/src/examples/CancelConnection/hooks/useCountdown.ts` (TYPESCRIPT) | Magnitude: 3.12 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 10, args: 10, func_start: 9
- `examples/react/src/examples/Stress/performanceUtils.ts` (TYPESCRIPT) | Magnitude: 9.51 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 82, concurrency: 38, state_mutation: 21, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/react/src/examples/Validation/index.tsx` (TYPESCRIPT) | Magnitude: 1.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 26, ui_framework: 17, immutability_locks: 14
- `packages/react/src/additional-components/MiniMap/MiniMapNodes.tsx` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 25, ui_framework: 16, generics: 14
- `packages/react/src/types/store.ts` (TYPESCRIPT) | Magnitude: 0.93 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 64, ui_framework: 33, generics: 32
- `examples/react/src/examples/NodeResizer/HorizontalResizer.tsx` (TYPESCRIPT) | Magnitude: 0.29 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 37, indent_spaces: 33, safety: 18, structural_boundaries: 7
- `examples/react/src/examples/NodeResizer/VerticalResizer.tsx` (TYPESCRIPT) | Magnitude: 0.29 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
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

- `packages/system/src/utils/store.ts` -> Churn: **100.0%** | Cog Load: 35.5664% | Debt: 64.2543%
- `packages/react/src/store/index.ts` -> Churn: **92.51%** | Cog Load: 34.5022% | Debt: 99.9999%
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> Churn: **79.25%** | Cog Load: 96.6391% | Debt: 76.9183%
- `packages/react/src/components/StoreUpdater/index.tsx` -> Churn: **58.05%** | Cog Load: 21.0748% | Debt: 85.2622%
- `packages/svelte/src/lib/hooks/useSvelteFlow.svelte.ts` -> Churn: **55.99%** | Cog Load: 21.4127% | Debt: 99.9993%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/svelte/src/lib/components/NodeWrapper/NodeWrapper.svelte` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 132.02
- `packages/svelte/src/lib/plugins/NodeResizer/ResizeControl.svelte` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 105.7
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

- `packages/svelte/src/lib/store/context.ts` -> **Severity: 228.702** (Blast Radius: 2.975 * Doc Risk: 76.8746%)
- `packages/system/src/xypanzoom/eventhandler.ts` -> **Severity: 227.839** (Blast Radius: 3.009 * Doc Risk: 75.7191%)
- `packages/system/src/types/panzoom.ts` -> **Severity: 203.8** (Blast Radius: 2.038 * Doc Risk: 100.0%)
- `packages/react/src/contexts/NodeIdContext.ts` -> **Severity: 200.95** (Blast Radius: 3.653 * Doc Risk: 55.0096%)
- `packages/system/src/utils/dom.ts` -> **Severity: 161.16** (Blast Radius: 1.704 * Doc Risk: 94.5772%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
