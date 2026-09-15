# ARCHITECTURAL_BRIEF: react-flow
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wbkd/react-flow.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 685 |
| Analyzed Artifacts (Scanned) | 652 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 33 |
| Total LOC | 36464 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 95.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.517 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3773 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.1689 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 62 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 441 | 28255 | 67.6% |
| HTML | 129 | 6681 | 19.8% |
| CSS | 27 | 1097 | 4.1% |
| MARKDOWN | 17 | 0 | 2.6% |
| PLAINTEXT | 16 | 5 | 2.5% |
| JSON | 12 | 169 | 1.8% |
| JAVASCRIPT | 8 | 244 | 1.2% |
| YAML | 2 | 13 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.32; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 39%, Declarative / Non-Code 19%, Callbacks & Closures Files 14%, Interface Declarations Files 7%, Defensive Guards Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 619 | 94.9% |
| Unknown | 5 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 28 | 4.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 33*

**Composition by Extension & Reason:**
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2245 LOC)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14167 LOC)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.9 | 7.9 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.6 | 17.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.7 | 3.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.8 | 4.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 93.0 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 72.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.3 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 44.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 183 | 97 | 1 | `packages/react/src/hooks/useReactFlow.ts` |
| cleanup | 23 | 14 | 0 | `packages/react/src/hooks/useKeyPress.ts` |
| guards | 965 | 157 | 4 | `packages/system/src/utils/general.ts` |
| danger | 203 | 71 | 1 | `examples/react/cypress/components/utils/adopt-user-nodes.cy.ts` |
| concurrency | 446 | 42 | 0 | `tests/playwright/e2e/nodes.spec.ts` |
| connectivity | 1240 | 456 | 4 | `packages/system/src/types/general.ts` |
| io | 176 | 52 | 0 | `examples/react/src/App/routes.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 22 | 9 | 0 | `packages/system/src/xypanzoom/eventhandler.ts` |
| serialization | 6 | 4 | 0 | `tooling/rollup-config/src/index.js` |
| regex | 15 | 13 | 0 | `packages/react/src/hooks/useKeyPress.ts` |
| events | 263 | 87 | 1 | `packages/system/src/xypanzoom/XYPanZoom.ts` |
| tests | 602 | 35 | 0 | `tests/playwright/e2e/nodes.spec.ts` |
| docs | 849 | 133 | 2 | `packages/react/src/types/component-props.ts` |
| debt | 213 | 73 | 1 | `examples/react/src/examples/Overview/index.tsx` |
| mutation | 7055 | 490 | 27 | `packages/react/src/container/ReactFlow/index.tsx` |
| dead_code | 175 | 118 | 1 | `packages/react/src/store/index.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 34 | 26 | 0 | `packages/react/src/components/NodeWrapper/index.tsx` |
| ml_ai | 239 | 54 | 0 | `packages/system/src/utils/general.ts` |
| ui | 1468 | 286 | 8 | `packages/svelte/src/lib/store/initial-store.svelte.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `examples/react/src/App/routes.ts` (Hits: 66)
- `packages/react/src/components/ConnectionLine/index.tsx` (Hits: 9)
- `examples/react/src/App/index.tsx` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.json** (`tooling/tsconfig/react.json`) — 240 inbound connections
2. **simpleflow.ts** (`examples/react/cypress/fixtures/simpleflow.ts`) — 9 inbound connections
3. **NodeIdContext.ts** (`packages/react/src/contexts/NodeIdContext.ts`) — 7 inbound connections
4. **Handle.svelte** (`packages/svelte/src/lib/components/Handle/Handle.svelte`) — 6 inbound connections
5. **Panel.svelte** (`packages/svelte/src/lib/container/Panel/Panel.svelte`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **routes.ts** (`examples/react/src/App/routes.ts`) — 65 outbound dependencies
2. **index.ts** (`packages/react/src/index.ts`) — 37 outbound dependencies
3. **index.ts** (`packages/svelte/src/lib/index.ts`) — 33 outbound dependencies
4. **Controls.tsx** (`packages/react/src/additional-components/Controls/Controls.tsx`) — 15 outbound dependencies
5. **index.tsx** (`packages/react/src/container/ReactFlow/index.tsx`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getDimensionsAfterResize` **(Many-Argument Workhorses)** (@ `packages/system/src/xyresizer/utils.ts`) -> Impact: **254.3** | LOC: 167
  * *Intent:* * with expandParent or extent: 'parent' set and oh yeah, these things also have to work with keepAspectRatio! * The way this is done is by determining...
- `getInitialStore` **(Defensive Guards)** (@ `packages/svelte/src/lib/store/initial-store.svelte.ts`) -> Impact: **185.2** | LOC: 366
- `createStore` **(Compute Cores)** (@ `packages/svelte/src/lib/store/index.ts`) -> Impact: **146.7** | LOC: 389
- `update` **(Compute Cores)** (@ `packages/system/src/xydrag/XYDrag.ts`) -> Impact: **138.9** | LOC: 289
  * *Intent:* // public functions
- `XYResizer` **(Compute Cores)** (@ `packages/system/src/xyresizer/XYResizer.ts`) -> Impact: **108.6** | LOC: 249
- `update` **(Compute Cores)** (@ `packages/system/src/xyresizer/XYResizer.ts`) -> Impact: **107.4** | LOC: 225
- `NodeWrapper` **(Compute Cores)** (@ `packages/react/src/components/NodeWrapper/index.tsx`) -> Impact: **102.0** | LOC: 229
- `EdgeWrapper` **(Compute Cores)** (@ `packages/react/src/components/EdgeWrapper/index.tsx`) -> Impact: **101.5** | LOC: 249
- `Pane` **(Compute Cores)** (@ `packages/react/src/container/Pane/index.tsx`) -> Impact: **99.3** | LOC: 232
- `XYPanZoom` **(Defensive Guards)** (@ `packages/system/src/xypanzoom/XYPanZoom.ts`) -> Impact: **79.8** | LOC: 266

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/svelte` | 9 | 10085.58 | 1.02% | 0.0% |
| `examples/svelte` | 8 | 5081.36 | 1.79% | 0.0% |
| `__monolith__` | 10 | 5051.44 | 0.0% | 0.0% |
| `packages/react` | 5 | 5040.7 | 0.0% | 0.0% |
| `tests/playwright/e2e` | 7 | 1539.59 | 22.2% | 0.0% |
| `packages/system/src/utils` | 11 | 1412.2 | 26.88% | 0.0% |
| `packages/svelte/src/lib/store` | 5 | 885.67 | 42.92% | 2.13% |
| `packages/react/src/hooks` | 29 | 863.88 | 9.52% | 1.85% |
| `packages/system/src/xyresizer` | 4 | 741.97 | 36.26% | 0.0% |
| `packages/system/src/xypanzoom` | 5 | 474.84 | 21.05% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/svelte/src/lib/hooks/useUpdateNodeInternals.svelte.ts` -> **99.6827%** Exposure
- `packages/svelte/src/lib/plugins/Minimap/interactive.ts` -> **98.2014%** Exposure
- `packages/svelte/src/lib/utils/index.ts` -> **98.2014%** Exposure
- `packages/svelte/src/lib/hooks/useNodesEdgesViewport.svelte.ts` -> **97.121%** Exposure
- `tooling/postcss-config/postcss.config.js` -> **95.2574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/react/src/components/BatchProvider/index.tsx` -> **100.0%** Exposure
- `packages/react/src/components/NodeWrapper/useNodeObserver.ts` -> **100.0%** Exposure
- `packages/react/src/utils/changes.ts` -> **100.0%** Exposure
- `packages/system/src/utils/edges/positions.ts` -> **100.0%** Exposure
- `packages/system/src/utils/edges/smoothstep-edge.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/react/src/store/index.ts` -> **13** Orphaned Functions | **0** Duplicates
- `packages/react/src/container/ZoomPane/index.tsx` -> **5** Orphaned Functions | **0** Duplicates
- `packages/react/src/components/Handle/index.tsx` -> **4** Orphaned Functions | **0** Duplicates
- `examples/react/src/examples/Overview/index.tsx` -> **3** Orphaned Functions | **0** Duplicates
- `packages/svelte/src/lib/hooks/useNodesEdgesViewport.svelte.ts` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `752` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/system/src/xypanzoom/eventhandler.ts` (TYPESCRIPT) -> Cumulative Risk: **707.4**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.35)
- **Magnitude:** 153.48 | **LOC:** 252 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.6464%), Concurrency (91.5565%)
- **Heaviest Functions:** `createPanOnScrollHandler` (Compute Cores, Impact: 28.1), `createPanZoomEndHandler` (Defensive Guards, Impact: 19.1), `createPanZoomHandler` (Defensive Guards, Impact: 15.2)

### 2. `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT) -> Cumulative Risk: **683.97**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.14)
- **Magnitude:** 381.6 | **LOC:** 489 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (93.75%), Cognitive Load (87.9296%), State Flux (84.9353%)
- **Heaviest Functions:** `getInitialStore` (Defensive Guards, Impact: 185.2), `getInitialViewport` (Many-Argument Workhorses, Impact: 30.0), `filter` (Defensive Guards, Impact: 10.3)

### 3. `packages/svelte/src/lib/store/index.ts` (TYPESCRIPT) -> Cumulative Risk: **677.62**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.09)
- **Magnitude:** 443.16 | **LOC:** 420 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Cognitive Load (94.9188%), State Flux (84.9443%)
- **Heaviest Functions:** `createStore` (Compute Cores, Impact: 146.7), `updateNodeInternals` (Defensive Guards, Impact: 31.1), `moveSelectedNodes` (Defensive Guards, Impact: 24.9)

### 4. `packages/system/src/utils/store.ts` (TYPESCRIPT) -> Cumulative Risk: **666.62**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.04)
- **Magnitude:** 478.12 | **LOC:** 601 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (90.4762%), State Flux (84.9681%)
- **Heaviest Functions:** `updateNodeInternals` (Many-Argument Workhorses, Impact: 76.0), `handleExpandParent` (Many-Argument Workhorses, Impact: 55.8), `adoptUserNodes` (Many-Argument Workhorses, Impact: 47.9)

### 5. `packages/system/src/xydrag/XYDrag.ts` (TYPESCRIPT) -> Cumulative Risk: **636.15**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.50)
- **Magnitude:** 326.86 | **LOC:** 410 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8633%), Verification (80.0%)
- **Heaviest Functions:** `update` (Compute Cores, Impact: 138.9), `updateNodes` (Compute Cores, Impact: 43.2), `startDrag` (Defensive Guards, Impact: 30.6)

### 6. `packages/react/src/store/index.ts` (TYPESCRIPT) -> Cumulative Risk: **601.85**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.83)
- **Magnitude:** 213.22 | **LOC:** 455 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 27.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Churn (91.76%), Verification (80.0%)
- **Heaviest Functions:** `updateNodePositions` (Defensive Guards, Impact: 35.6), `createStore` (Compute Cores, Impact: 21.3), `setCenter` (Defensive Guards, Impact: 15.0)

### 7. `packages/react/src/utils/changes.ts` (TYPESCRIPT) -> Cumulative Risk: **586.5**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.48)
- **Magnitude:** 179.58 | **LOC:** 325 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.5998%), Verification (80.0%)
- **Heaviest Functions:** `applyChanges` (Compute Cores, Impact: 33.7), `applyChange` (Compute Cores, Impact: 26.4), `getElementsDiffChanges` (Defensive Guards, Impact: 17.2)

### 8. `packages/system/src/xyhandle/XYHandle.ts` (TYPESCRIPT) -> Cumulative Risk: **574.19**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.55)
- **Magnitude:** 209.48 | **LOC:** 324 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.9785%), Verification (80.0%)
- **Heaviest Functions:** `onPointerDown` (Many-Argument Workhorses, Impact: 68.4), `isValidHandle` (Compute Cores, Impact: 41.6), `onPointerMove` (Compute Cores, Impact: 22.0)

### 9. `packages/system/src/xyresizer/XYResizer.ts` (TYPESCRIPT) -> Cumulative Risk: **572.13**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.35)
- **Magnitude:** 329.94 | **LOC:** 353 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9903%), Safety Score (82.9673%)
- **Heaviest Functions:** `XYResizer` (Compute Cores, Impact: 108.6), `update` (Compute Cores, Impact: 107.4), `nodeToChildExtent` (Defensive Guards, Impact: 10.7)

### 10. `packages/system/src/xyhandle/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **569.96**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.70)
- **Magnitude:** 155.26 | **LOC:** 128 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7916%), Verification (80.0%)
- **Heaviest Functions:** `getClosestHandle` (Many-Argument Workhorses, Impact: 51.6), `getHandle` (Defensive Guards, Impact: 46.1), `getHandleType` (Defensive Guards, Impact: 14.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/playwright/e2e/node-toolbar.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 601.67 | **LOC:** 95 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.8924%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 32`, `args: 9`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1`
* *Architecture:* `concurrency: 17`, `import: 2`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constants, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/system/src/utils/store.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 478.12 | **LOC:** 601 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (56.2166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateNodeInternals` **(Many-Argument Workhorses)** (Impact: 76.0)
  * `handleExpandParent` **(Many-Argument Workhorses)** (Impact: 55.8)
  * `adoptUserNodes` **(Many-Argument Workhorses)** (Impact: 47.9)
  * `updateChildNode` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* /** * Updates positionAbsolute and zIndex of a child node and the parentLookup. */
  * `parseHandles` **(Defensive Guards)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 57`, `args: 17`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `dead_code: 1`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 14`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., types, dom, general, graph, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/store/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 443.16 | **LOC:** 420 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 70.0%
- **Risk Profile:** Cognitive Load (94.9188%), Tech Debt (10.6726%)
**Top Internal Functions/Classes:**
  * `createStore` **(Compute Cores)** (Impact: 146.7)
  * `updateNodeInternals` **(Defensive Guards)** (Impact: 31.1)
  * `moveSelectedNodes` **(Defensive Guards)** (Impact: 24.9)
  * `handleNodeSelection` **(Defensive Guards)** (Impact: 20.9)
  * `setCenter` **(Defensive Guards)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 60`, `args: 33`, `func_start: 25`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types, useStore, initial-store.svelte, types, system
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/system/src/xyresizer/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 397.56 | **LOC:** 281 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.2889%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDimensionsAfterResize` **(Many-Argument Workhorses)** (Impact: 254.3)
    * *Intent:* * with expandParent or extent: 'parent' set and oh yeah, these things also have to work with keepAsp...
  * `getResizeDirection` **(Compute Cores)** (Impact: 13.8)
    * *Intent:* /** * Get all connecting edges for a given set of nodes * @param width - new width of the node * @pa...
  * `getControlDirection` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* /** * Parses the control position that is being dragged to dimensions that are being resized * @para...
  * `xor` **(Parameter Forwarders)** (Impact: 3.6)
  * `getSizeClamp` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 16`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, utils, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/playwright/e2e/nodes.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 392.63 | **LOC:** 289 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3889%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 147`, `args: 28`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 12`
* *Architecture:* `concurrency: 125`, `import: 2`
* *Defense:* `test: 77`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constants, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/store/initial-store.svelte.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 381.6 | **LOC:** 489 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (87.9296%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getInitialStore` **(Defensive Guards)** (Impact: 185.2)
  * `getInitialViewport` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `filter` **(Defensive Guards)** (Impact: 10.3)
  * `resolveFitView` **(I/O & Config Routines)** (Impact: 8.9)
  * `warnIfDeeplyReactive` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* // Only way to check if an object is a proxy // is to see if it fails to perform a structured clone
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 76`, `args: 24`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 45`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.748
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.003456
  * `Imports (Out-Degree: 5):` edges, DefaultNode.svelte, GroupNode.svelte, InputNode.svelte, OutputNode.svelte, types, types, visibleElements...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/svelte/src/lib/plugins/NodeToolbar/NodeToolbar.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 377.25 | **LOC:** 85 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.2857%), Tech Debt (43.507%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 23`, `args: 7`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`, `fragile_debt: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001536
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/utils/general.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 330.84 | **LOC:** 427 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.8963%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parsePaddings` **(Defensive Guards)** (Impact: 41.4)
    * *Intent:* /** * Parses the paddings to an object with top, right, bottom, left, x and y paddings * @internal *...
  * `getNodeDimensions` **(Defensive Guards)** (Impact: 31.7)
  * `nodeToRect` **(Defensive Guards)** (Impact: 28.4)
  * `nodeToBox` **(Defensive Guards)** (Impact: 28.4)
  * `evaluateAbsolutePosition` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /** * Convert child position to absolute position * * @internal * @param position * @param parentId ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 94`, `args: 35`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`
* *Architecture:* `io: 1`, `api: 26`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 50`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` constants, types, graph
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/system/src/xyresizer/XYResizer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 329.94 | **LOC:** 353 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.7618%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `XYResizer` **(Compute Cores)** (Impact: 108.6)
  * `update` **(Compute Cores)** (Impact: 107.4)
  * `nodeToChildExtent` **(Defensive Guards)** (Impact: 10.7)
  * `getStoreItems` **(Callbacks & Closures)** (Impact: 5.6)
  * `nodeToParentExtent` **(Interface Declarations)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 38`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 29`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001536
  * `Imports (Out-Degree: 0):` types, utils, types, utils, d3-drag, d3-selection
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/xydrag/XYDrag.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 326.86 | **LOC:** 410 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.1269%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` **(Compute Cores)** (Impact: 138.9)
    * *Intent:* // public functions
  * `updateNodes` **(Compute Cores)** (Impact: 43.2)
  * `startDrag` **(Defensive Guards)** (Impact: 30.6)
  * `autoPan` **(Defensive Guards)** (Impact: 11.3)
  * `destroy` **(Defensive Guards)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 46`, `args: 16`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 28`, `dead_code: 1`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 15`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001536
  * `Imports (Out-Degree: 0):` types, utils, utils, d3-drag, d3-selection
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/utils/graph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 324.46 | **LOC:** 526 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (29.9366%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getNodesInside` **(Many-Argument Workhorses)** (Impact: 67.1)
  * `calculateNodePosition` **(Defensive Guards)** (Impact: 41.1)
    * *Intent:* /** * This function calculates the next position of a node, taking into account the node's extent, p...
  * `fitViewport` **(Defensive Guards)** (Impact: 27.6)
  * `getNodesBounds` **(Compute Cores)** (Impact: 24.8)
    * *Intent:* * height: 25, * }, * { * id: 'b', * position: { x: 100, y: 100 }, * data: { label: 'b' }, * width: 5...
  * `getElementsToRemove` **(Compute Cores)** (Impact: 22.9)
    * *Intent:* /** * Pass in nodes & edges to delete, get arrays of nodes and edges that actually can be deleted * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 96`, `args: 29`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`
* *Architecture:* `api: 15`, `concurrency: 8`, `import: 4`
* *Defense:* `safety: 28`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.498
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.004608
  * `Imports (Out-Degree: 1):` constants, types, general, react
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/playwright/e2e/pane.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 287.76 | **LOC:** 184 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.4787%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 71`, `args: 16`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `concurrency: 62`, `import: 3`
* *Defense:* `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constants, utils, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/hooks/useSvelteFlow.svelte.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 261.58 | **LOC:** 578 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (16.4399%), Tech Debt (10.6095%)
**Top Internal Functions/Classes:**
  * `useSvelteFlow` **(I/O & Config Routines)** (Impact: 28.0)
    * *Intent:* /** * Hook for accessing the SvelteFlow instance. * * @public * @returns A set of helper functions *...
  * `getIntersectingNodes` **(Compute Cores)** (Impact: 23.4)
  * `fitBounds` **(Defensive Guards)** (Impact: 16.7)
  * `setViewport` **(Defensive Guards)** (Impact: 14.8)
  * `getNodeRect` **(Defensive Guards)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 118`, `args: 63`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 21`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001536
  * `Imports (Out-Degree: 0):` store, types, utils, system, svelte
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react/src/hooks/useReactFlow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 260.44 | **LOC:** 316 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `useReactFlow` **(Callbacks & Closures)** (Impact: 70.9)
    * *Intent:* * setCount(reactFlow.getNodes().length); * // you need to pass it as a dependency if you are using i...
  * `getIntersectingNodes` **(Compute Cores)** (Impact: 25.4)
  * `getNodeRect` **(Defensive Guards)** (Impact: 13.7)
  * `deleteElements` **(Defensive Guards)** (Impact: 13.4)
  * `isNodeIntersecting` **(Compute Cores)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 79`, `args: 40`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 16`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.098
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.006912
  * `Imports (Out-Degree: 2):` BatchProvider, types, utils, useStore, useViewportHelper, react, system, react
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/react/src/container/Pane/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 247.98 | **LOC:** 293 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 61.1%
- **Risk Profile:** Cognitive Load (33.1456%), Tech Debt (17.3851%)
**Top Internal Functions/Classes:**
  * `Pane` **(Compute Cores)** (Impact: 99.3)
  * `onPointerMove` **(Compute Cores)** (Impact: 33.8)
  * `onPointerUp` **(Defensive Guards)** (Impact: 28.0)
  * `onPointerDownCapture` **(Defensive Guards)** (Impact: 21.7)
    * *Intent:* // We are using capture here in order to prevent other pointer events // to be able to create a sele...
  * `onContextMenu` **(Defensive Guards)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 42`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 13`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` UserSelection, useStore, utils, types, utils, system, classcat, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/src/store/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 213.22 | **LOC:** 455 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (21.6798%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `updateNodePositions` **(Defensive Guards)** (Impact: 35.6)
  * `createStore` **(Compute Cores)** (Impact: 21.3)
  * `setCenter` **(Defensive Guards)** (Impact: 15.0)
  * `updateNodeInternals` **(Compute Cores)** (Impact: 13.5)
  * `unselectNodesAndEdges` **(Compute Cores)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 48`, `args: 27`, `func_start: 22`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 13`
* *Architecture:* `api: 1`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 19`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types, changes, initialState, system, traditional
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/system/src/xyhandle/XYHandle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 209.48 | **LOC:** 324 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (31.2696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onPointerDown` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `isValidHandle` **(Compute Cores)** (Impact: 41.6)
    * *Intent:* // checks if and returns connection in form of an object { source: 123, target: 312 }
  * `onPointerMove` **(Compute Cores)** (Impact: 22.0)
  * `onPointerUp` **(Defensive Guards)** (Impact: 20.5)
  * `autoPan` **(Interface Declarations)** (Impact: 3.5)
    * *Intent:* // when the user is moving the mouse close to the edge of the canvas while connecting we move the ca...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 19`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 9`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001536
  * `Imports (Out-Degree: 0):` types, utils, types, utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/system/src/xypanzoom/XYPanZoom.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 202.78 | **LOC:** 302 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.969%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `XYPanZoom` **(Defensive Guards)** (Impact: 79.8)
  * `update` **(Compute Cores)** (Impact: 22.4)
    * *Intent:* // public functions
  * `setTransform` **(Defensive Guards)** (Impact: 14.5)
  * `scaleTo` **(Defensive Guards)** (Impact: 14.5)
  * `scaleBy` **(Defensive Guards)** (Impact: 14.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 35`, `args: 21`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 2`, `concurrency: 15`, `import: 9`
* *Defense:* `safety: 17`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.375
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.003072
  * `Imports (Out-Degree: 2):` types, utils, eventhandler, filter, utils, d3-interpolate, d3-selection, d3-transition...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react/src/components/Handle/index.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 201.4 | **LOC:** 286 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.2704%), Tech Debt (34.25%)
**Top Internal Functions/Classes:**
  * `HandleComponent` **(Many-Argument Workhorses)** (Impact: 75.5)
  * `connectingSelector` **(Defensive Guards)** (Impact: 45.0)
  * `onClick` **(Compute Cores)** (Impact: 31.6)
  * `onPointerDown` **(Compute Cores)** (Impact: 9.9)
  * `onConnectEnd` **(Defensive Guards)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 52`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 22`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` NodeIdContext, useStore, types, utils, react, system, classcat, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/svelte/src/lib/components/ConnectionLine/ConnectionLine.svelte` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 194.0 | **LOC:** 79 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.724%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/system/src/utils/store.ts` -> Churn: **100.0%** | Cog Load: 56.2166% | Debt: 0.0%
- `packages/react/src/store/index.ts` -> Churn: **91.76%** | Cog Load: 21.6798% | Debt: 74.4868%
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> Churn: **71.86%** | Cog Load: 87.9296% | Debt: 0.0%
- `packages/svelte/src/lib/container/Pane/Pane.svelte` -> Churn: **51.6%** | Cog Load: 60.4817% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/svelte/src/lib/plugins/NodeToolbar/NodeToolbar.svelte` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 377.25
- `packages/system/src/utils/general.ts` -> **Yaroslav Halchenko** (100.0% isolated ownership) | Magnitude: 330.84
- `packages/system/src/xyresizer/XYResizer.ts` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 329.94
- `packages/system/src/xypanzoom/XYPanZoom.ts` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 202.78
- `packages/react/src/components/Handle/index.tsx` -> **peterkogo** (100.0% isolated ownership) | Magnitude: 201.4

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 84.9353%)
- `packages/react/src/additional-components/MiniMap/MiniMap.tsx` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 98.6166%)
- `packages/react/src/additional-components/NodeResizer/NodeResizeControl.tsx` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 79.0094%)
- `packages/react/src/hooks/useReactFlow.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 69.8226%)
- `packages/system/src/utils/graph.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/react/src/utils/changes.ts` -> **Severity: 0.445** (Embedded: 0.0046 * Error Risk: 96.5998%)
- `examples/react/cypress/support/ControlledFlow.tsx` -> **Severity: 0.434** (Embedded: 0.0061 * Error Risk: 70.6822%)
- `packages/react/src/hooks/useReactFlow.ts` -> **Severity: 0.385** (Embedded: 0.0069 * Error Risk: 55.7419%)
- `packages/react/src/hooks/useKeyPress.ts` -> **Severity: 0.357** (Embedded: 0.0061 * Error Risk: 58.1555%)
- `packages/system/src/utils/graph.ts` -> **Severity: 0.254** (Embedded: 0.0046 * Error Risk: 55.0704%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/system/src/xypanzoom/XYPanZoom.ts` -> **Severity: 437.5** (Blast Radius: 4.375 * Doc Risk: 100.0%)
- `packages/system/src/xypanzoom/eventhandler.ts` -> **Severity: 284.3** (Blast Radius: 2.843 * Doc Risk: 100.0%)
- `packages/system/src/xypanzoom/filter.ts` -> **Severity: 284.3** (Blast Radius: 2.843 * Doc Risk: 100.0%)
- `packages/svelte/src/lib/store/initial-store.svelte.ts` -> **Severity: 257.625** (Blast Radius: 2.748 * Doc Risk: 93.75%)
- `examples/react/cypress/support/ControlledFlow.tsx` -> **Severity: 237.2** (Blast Radius: 2.372 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
