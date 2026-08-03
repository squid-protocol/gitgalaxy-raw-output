# ARCHITECTURAL_BRIEF: react
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/react` |
| **Timestamp** | `2026-08-03T20:06:47.081998+00:00` |
| **Scan Duration** | `13.3s` |
| **Git Branch** | `main` |
| **Git Commit** | `1b45e2439289fd8e094c44161c89e06c5488671e` |
| **Git Remote** | `https://github.com/facebook/react.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4128 malicious artifacts.

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
| Total Artifacts | 6879 |
| Analyzed Artifacts (Scanned) | 6271 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 608 |
| Total LOC | 395958 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.2% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2789 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 226 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 3620 | 339526 | 57.7% |
| MARKDOWN | 1800 | 0 | 28.7% |
| TYPESCRIPT | 496 | 47691 | 7.9% |
| PLAINTEXT | 115 | 2 | 1.8% |
| CSS | 112 | 4332 | 1.8% |
| HTML | 79 | 2996 | 1.3% |
| JSON | 28 | 1213 | 0.4% |
| SHELL | 12 | 190 | 0.2% |
| XML | 9 | 8 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.7`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2726 | 43.5% |
| file_cluster_13 | 855 | 13.6% |
| file_cluster_2 | 578 | 9.2% |
| file_cluster_4 | 101 | 1.6% |
| file_cluster_17 | 56 | 0.9% |
| file_cluster_16 | 10 | 0.2% |
| file_cluster_0 | 6 | 0.1% |
| file_cluster_6 | 6 | 0.1% |
| file_cluster_9 | 4 | 0.1% |
| Unknown | 2 | 0.0% |
| file_cluster_11 | 2 | 0.0% |
| file_cluster_12 | 2 | 0.0% |
| file_cluster_7 | 1 | 0.0% |
| file_cluster_1 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1913 | 30.5% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 608*

**Composition by Extension & Reason:**
- `.js`: 117x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 52x Excluded (Saturation: Line 14 exceeds 500 chars), 13x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.md`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2745 LOC), 1x Excluded (Machine-Generated Source Code Signature: 64 LOC)
- `.map`: 67x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Unsupported Extension: '.map')
- `no_extension`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace'), 1x Unsupported Format (.undeterminable)
- `.lock`: 42x Excluded (Unsupported Extension: '.lock'), 1x Excluded (Machine-Generated Source Code Signature: 1743 LOC), 1x Unsupported Format (.lock)
- `.png`: 33x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (Saturation: Line 82 exceeds 500 chars)
- `.txt`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12828 LOC)
- `.ico`: 10x Excluded (Explicitly Denied Extension: '.ico')
- `.mjs`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 5x Unsupported Format (.snap), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 22 exceeds 500 chars)
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.2 | 5.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.5 | 13.9 | 3.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.8 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.6 | 4.0 | 4.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 28.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 49.2 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 32.7 | 4.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 30.7 | 13.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.2 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `flow-typed/environments/node.js` (Hits: 186)
- `compiler/packages/snap/src/minimize.ts` (Hits: 101)
- `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts` (Hits: 60)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **shared-runtime.ts** (`compiler/packages/snap/src/sprout/shared-runtime.ts`) — 550 inbound connections
2. **client.js** (`packages/react-dom/client.js`) — 190 inbound connections
3. **ReactTypes.js** (`packages/shared/ReactTypes.js`) — 186 inbound connections
4. **ReactFeatureFlags.js** (`packages/shared/ReactFeatureFlags.js`) — 113 inbound connections
5. **ReactInternalTypes.js** (`packages/react-reconciler/src/ReactInternalTypes.js`) — 105 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ReactFiberWorkLoop.js** (`packages/react-reconciler/src/ReactFiberWorkLoop.js`) — 59 outbound dependencies
2. **ReactFiberBeginWork.js** (`packages/react-reconciler/src/ReactFiberBeginWork.js`) — 45 outbound dependencies
3. **ReactFiberConfigDOM.js** (`packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js`) — 42 outbound dependencies
4. **Pipeline.ts** (`compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Pipeline.ts`) — 38 outbound dependencies
5. **ReactFiberHooks.js** (`packages/react-reconciler/src/ReactFiberHooks.js`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `initializeDebugChunk` (@ `packages/react-client/src/ReactFlightClient.js`) -> Impact: **5037.6** | LOC: 2112
- `lowerStatement` (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **4238.0** | LOC: 1578
- `applyEffect` (@ `compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts`) -> Impact: **3532.7** | LOC: 844
- `throwTaintViolation` (@ `packages/react-server/src/ReactFlightServer.js`) -> Impact: **2901.3** | LOC: 1562
- `lowerAssignment` (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **2795.6** | LOC: 587
- `updateHostHoistable` (@ `packages/react-reconciler/src/ReactFiberBeginWork.js`) -> Impact: **2586.1** | LOC: 1186
- `insertNewOutlinedFunctionNode` (@ `compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Program.ts`) -> Impact: **2126.9** | LOC: 857
- `commitSuspenseHydrationCallbacks` (@ `packages/react-reconciler/src/ReactFiberCommitWork.js`) -> Impact: **2112.1** | LOC: 1741
- `codegenInstructionValue` (@ `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts`) -> Impact: **2106.9** | LOC: 618
- `visitBlock` (@ `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/BuildReactiveFunction.ts`) -> Impact: **1567.1** | LOC: 685

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `describe` (@ `packages/react-debug-tools/src/__tests__/ReactHooksInspection-test.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/react-devtools-shared/src/__tests__/TimelineProfiler-test.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/react-devtools-shared/src/__tests__/TimelineProfiler-test.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/react-devtools-shared/src/__tests__/storeComponentFilters-test.js`) -> **O(2^N) [Recursive]**
- `debug` (@ `packages/react-devtools-shared/src/devtools/store.js`) -> **O(2^N) [Recursive]**
- `CanViewElementSource` (@ `packages/react-devtools-shared/src/devtools/views/DevTools.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/react-dom/src/__tests__/ReactDOMServerIntegrationClassContextType-test.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // Make them available to the helpers.
- `describe` (@ `packages/react-dom/src/__tests__/ReactDOMServerIntegrationNewContext-test.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // Make them available to the helpers.
- `validateNoRefAccessInRenderImpl` (@ `compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoRefAccessInRender.ts`) -> **O(2^N) [Recursive]**
- `initializeDebugChunk` (@ `packages/react-client/src/ReactFlightClient.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/react-dom/src/__tests__/ReactLegacyErrorBoundaries-test.internal.js`) -> DB Complexity: **231**
- `describe` (@ `packages/react-reconciler/src/__tests__/ReactIncremental-test.js`) -> DB Complexity: **204**
- `visitBlock` (@ `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/BuildReactiveFunction.ts`) -> DB Complexity: **172**
- `describe` (@ `packages/react-devtools-shared/src/__tests__/editing-test.js`) -> DB Complexity: **151**
  * *Intent:* /** * Copyright (c) Meta Platforms, Inc. and affiliates. * * This source code is licensed under the MIT license found in the * LICENSE file in the roo...
- `insertNewOutlinedFunctionNode` (@ `compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Program.ts`) -> DB Complexity: **143**
- `isPathAllowed` (@ `packages/react-devtools-shared/src/hydration.js`) -> DB Complexity: **123**
- `initializeDebugChunk` (@ `packages/react-client/src/ReactFlightClient.js`) -> DB Complexity: **113**
- `describe` (@ `packages/react-dom/src/__tests__/ReactUpdates-test.js`) -> DB Complexity: **109**
- `describe` (@ `packages/react-devtools-shared/src/__tests__/inspectedElement-test.js`) -> DB Complexity: **107**
- `describe` (@ `packages/react-dom/src/__tests__/ReactDOMFiberAsync-test.js`) -> DB Complexity: **105**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/react-reconciler/src` | 81 | 29454.96 | 18.72% | 40.2% |
| `packages/react-dom/src/__tests__` | 129 | 29264.18 | 42.78% | 36.93% |
| `packages/react-reconciler/src/__tests__` | 76 | 14165.42 | 48.09% | 33.56% |
| `packages/react-server/src` | 37 | 10559.1 | 23.92% | 25.99% |
| `packages/react-client/src` | 14 | 7534.52 | 27.54% | 28.55% |
| `packages/react-devtools-shared/src/__tests__` | 34 | 5974.54 | 16.83% | 27.61% |
| `fixtures/fiber-debugger` | 3 | 5000.0 | 0.0% | 0.0% |
| `fixtures/nesting` | 3 | 5000.0 | 0.0% | 0.0% |
| `packages/react-dom-bindings/src/client` | 28 | 4825.44 | 18.15% | 17.45% |
| `packages/react-devtools-shared/src/backend/fiber` | 2 | 4315.88 | 39.07% | 22.06% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `babel.config-react-compiler.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-capture-in-method-receiver.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-computed-load.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allocating-primitive-as-dep.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allow-assigning-to-global-in-function-spread-as-jsx.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-capture-in-method-receiver.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-while.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/capturing-function-conditional-capture-mutate.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/conditional-break-labeled.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/conditional-early-return.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/bench/benchmarks/pe-class-components/benchmark.js` -> **0** Orphaned Functions | **184** Duplicates
- `flow-typed/environments/node.js` -> **46** Orphaned Functions | **38** Duplicates
- `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` -> **2** Orphaned Functions | **59** Duplicates
- `flow-typed/environments/bom.js` -> **21** Orphaned Functions | **38** Duplicates
- `compiler/packages/babel-plugin-react-compiler/src/HIR/Globals.ts` -> **0** Orphaned Functions | **57** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`fixtures/flight/server/global.js`** -> AI Confidence: **99.48%**
2. **`packages/react-dom-bindings/src/client/ReactDOMComponent.js`** -> AI Confidence: **99.48%**
3. **`packages/react-dom-bindings/src/client/ReactDOMInput.js`** -> AI Confidence: **99.48%**
4. **`packages/react-reconciler/src/ReactFiberApplyGesture.js`** -> AI Confidence: **99.48%**
5. **`packages/react-reconciler/src/ReactFiberCommitWork.js`** -> AI Confidence: **99.48%**
6. **`packages/react-reconciler/src/ReactFiberPerformanceTrack.js`** -> AI Confidence: **99.48%**
7. **`packages/react-server/src/ReactFizzClassComponent.js`** -> AI Confidence: **99.48%**
8. **`scripts/rollup/build-all-release-channels.js`** -> AI Confidence: **99.48%**
9. **`compiler/packages/babel-plugin-react-compiler/src/Inference/AnalyseFunctions.ts`** -> AI Confidence: **99.48%**
10. **`compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts`** -> AI Confidence: **99.48%**
11. **`compiler/packages/babel-plugin-react-compiler/src/Optimization/OutlineJsx.ts`** -> AI Confidence: **99.48%**
12. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateHooksUsage.ts`** -> AI Confidence: **99.48%**
13. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoSetStateInEffects.ts`** -> AI Confidence: **99.48%**
14. **`compiler/packages/babel-plugin-react-compiler/scripts/build-react-hooks-fixures.js`** -> AI Confidence: **99.39%**
15. **`fixtures/flight/config/webpack.config.js`** -> AI Confidence: **99.39%**
16. **`packages/react-client/src/ReactFlightClient.js`** -> AI Confidence: **99.39%**
17. **`packages/react-native-renderer/src/legacy-events/ResponderEventPlugin.js`** -> AI Confidence: **99.39%**
18. **`packages/react-reconciler/src/ReactFiberClassComponent.js`** -> AI Confidence: **99.39%**
19. **`packages/react-reconciler/src/ReactFiberCommitEffects.js`** -> AI Confidence: **99.39%**
20. **`packages/react-server/src/ReactFlightServerConfigDebugNode.js`** -> AI Confidence: **99.39%**
21. **`packages/react/src/ReactStartTransition.js`** -> AI Confidence: **99.39%**
22. **`scripts/jest/preprocessor.js`** -> AI Confidence: **99.39%**
23. **`scripts/rollup/build.js`** -> AI Confidence: **99.39%**
24. **`compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`** -> AI Confidence: **99.39%**
25. **`compiler/packages/babel-plugin-react-compiler/src/Utils/TestUtils.ts`** -> AI Confidence: **99.39%**
26. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoDerivedComputationsInEffects_exp.ts`** -> AI Confidence: **99.39%**
27. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidatePreservedManualMemoization.ts`** -> AI Confidence: **99.39%**
28. **`compiler/packages/snap/src/minimize.ts`** -> AI Confidence: **99.39%**
29. **`packages/react-devtools-shared/src/backend/fiber/renderer.js`** -> AI Confidence: **99.35%**
30. **`packages/react-reconciler/src/ReactFiberWorkLoop.js`** -> AI Confidence: **99.35%**
31. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts`** -> AI Confidence: **99.35%**
32. **`dangerfile.js`** -> AI Confidence: **99.34%**
33. **`packages/react-devtools-fusebox/webpack.config.frontend.js`** -> AI Confidence: **99.34%**
34. **`packages/react-devtools-shared/src/backend/profilingHooks.js`** -> AI Confidence: **99.34%**
35. **`packages/react-devtools-shared/src/devtools/views/Components/TreeContext.js`** -> AI Confidence: **99.34%**
36. **`packages/react-devtools-timeline/src/import-worker/preprocessData.js`** -> AI Confidence: **99.34%**
37. **`scripts/jest/jest-cli.js`** -> AI Confidence: **99.34%**
38. **`compiler/packages/babel-plugin-react-compiler/src/HIR/PrintHIR.ts`** -> AI Confidence: **99.34%**
39. **`compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingRanges.ts`** -> AI Confidence: **99.34%**
40. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/InferReactiveScopeVariables.ts`** -> AI Confidence: **99.34%**
41. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/PromoteUsedTemporaries.ts`** -> AI Confidence: **99.34%**
42. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateExhaustiveDependencies.ts`** -> AI Confidence: **99.34%**
43. **`packages/react-dom/src/shared/ReactDOMFloat.js`** -> AI Confidence: **99.32%**
44. **`compiler/packages/babel-plugin-react-compiler/src/HIR/visitors.ts`** -> AI Confidence: **99.32%**
45. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/MemoizeFbtAndMacroOperandsInSameScope.ts`** -> AI Confidence: **99.32%**
46. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/visitors.ts`** -> AI Confidence: **99.32%**
47. **`compiler/packages/babel-plugin-react-compiler/src/SSA/EliminateRedundantPhi.ts`** -> AI Confidence: **99.32%**
48. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateStaticComponents.ts`** -> AI Confidence: **99.32%**
49. **`compiler/scripts/anonymize.js`** -> AI Confidence: **99.31%**
50. **`fixtures/attribute-behavior/src/App.js`** -> AI Confidence: **99.31%**
51. **`fixtures/fizz/server/server.js`** -> AI Confidence: **99.31%**
52. **`fixtures/flight-esm/server/global.js`** -> AI Confidence: **99.31%**
53. **`fixtures/flight-esm/server/region.js`** -> AI Confidence: **99.31%**
54. **`fixtures/flight-ssr-bench/bench-server.js`** -> AI Confidence: **99.31%**
55. **`fixtures/flight/server/region.js`** -> AI Confidence: **99.31%**
56. **`fixtures/ssr2/server/server.js`** -> AI Confidence: **99.31%**
57. **`packages/react-art/src/ReactFiberConfigART.js`** -> AI Confidence: **99.31%**
58. **`packages/react-client/src/ReactFlightReplyClient.js`** -> AI Confidence: **99.31%**
59. **`packages/react-debug-tools/src/ReactDebugHooks.js`** -> AI Confidence: **99.31%**
60. **`packages/react-devtools-core/src/backend.js`** -> AI Confidence: **99.31%**
61. **`packages/react-devtools-extensions/webpack.config.js`** -> AI Confidence: **99.31%**
62. **`packages/react-devtools-shared/src/__tests__/setupTests.js`** -> AI Confidence: **99.31%**
63. **`packages/react-devtools-shared/src/backend/agent.js`** -> AI Confidence: **99.31%**
64. **`packages/react-devtools-shared/src/backend/legacy/renderer.js`** -> AI Confidence: **99.31%**
65. **`packages/react-devtools-shared/src/devtools/store.js`** -> AI Confidence: **99.31%**
66. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElement.js`** -> AI Confidence: **99.31%**
67. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementSuspendedBy.js`** -> AI Confidence: **99.31%**
68. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementView.js`** -> AI Confidence: **99.31%**
69. **`packages/react-devtools-shared/src/devtools/views/Components/KeyValue.js`** -> AI Confidence: **99.31%**
70. **`packages/react-devtools-shared/src/devtools/views/Components/Tree.js`** -> AI Confidence: **99.31%**
71. **`packages/react-devtools-shared/src/devtools/views/ErrorBoundary/ErrorBoundary.js`** -> AI Confidence: **99.31%**
72. **`packages/react-devtools-shared/src/devtools/views/Profiler/Profiler.js`** -> AI Confidence: **99.31%**
73. **`packages/react-devtools-shared/src/devtools/views/Profiler/SidebarCommitInfo.js`** -> AI Confidence: **99.31%**
74. **`packages/react-devtools-shared/src/devtools/views/Profiler/SidebarSelectedFiberInfo.js`** -> AI Confidence: **99.31%**
75. **`packages/react-devtools-shared/src/devtools/views/Profiler/SnapshotSelector.js`** -> AI Confidence: **99.31%**
76. **`packages/react-devtools-shared/src/devtools/views/Settings/ComponentsSettings.js`** -> AI Confidence: **99.31%**
77. **`packages/react-devtools-shared/src/devtools/views/SuspenseTab/ActivityList.js`** -> AI Confidence: **99.31%**
78. **`packages/react-devtools-shared/src/devtools/views/SuspenseTab/SuspenseRects.js`** -> AI Confidence: **99.31%**
79. **`packages/react-devtools-shared/src/devtools/views/useOpenResource.js`** -> AI Confidence: **99.31%**
80. **`packages/react-devtools-shared/src/hooks/__tests__/updateMockSourceMaps.js`** -> AI Confidence: **99.31%**
81. **`packages/react-devtools-shared/src/hooks/parseHookNames/parseSourceAndMetadata.js`** -> AI Confidence: **99.31%**
82. **`packages/react-devtools-shared/src/inspectedElementMutableSource.js`** -> AI Confidence: **99.31%**
83. **`packages/react-devtools-shared/src/utils.js`** -> AI Confidence: **99.31%**
84. **`packages/react-devtools-shell/webpack-server.js`** -> AI Confidence: **99.31%**
85. **`packages/react-devtools-timeline/src/CanvasPage.js`** -> AI Confidence: **99.31%**
86. **`packages/react-devtools-timeline/src/EventTooltip.js`** -> AI Confidence: **99.31%**
87. **`packages/react-devtools-timeline/src/view-base/HorizontalPanAndZoomView.js`** -> AI Confidence: **99.31%**
88. **`packages/react-devtools-timeline/src/view-base/resizable/ResizableView.js`** -> AI Confidence: **99.31%**
89. **`packages/react-devtools-timeline/src/view-base/resizable/ResizeBarView.js`** -> AI Confidence: **99.31%**
90. **`packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js`** -> AI Confidence: **99.31%**
91. **`packages/react-dom-bindings/src/events/DOMPluginEventSystem.js`** -> AI Confidence: **99.31%**
92. **`packages/react-dom-bindings/src/events/ReactDOMEventReplaying.js`** -> AI Confidence: **99.31%**
93. **`packages/react-dom-bindings/src/events/plugins/ChangeEventPlugin.js`** -> AI Confidence: **99.31%**
94. **`packages/react-dom-bindings/src/events/plugins/EnterLeaveEventPlugin.js`** -> AI Confidence: **99.31%**
95. **`packages/react-dom/src/client/ReactDOMClientFB.js`** -> AI Confidence: **99.31%**
96. **`packages/react-dom/src/client/ReactDOMRoot.js`** -> AI Confidence: **99.31%**
97. **`packages/react-dom/src/client/ReactDOMRootFB.js`** -> AI Confidence: **99.31%**
98. **`packages/react-dom/src/server/ReactDOMFizzServerNode.js`** -> AI Confidence: **99.31%**
99. **`packages/react-dom/src/server/ReactDOMFizzStaticNode.js`** -> AI Confidence: **99.31%**
100. **`packages/react-dom/src/shared/ReactDOM.js`** -> AI Confidence: **99.31%**
101. **`packages/react-markup/src/ReactMarkupServer.js`** -> AI Confidence: **99.31%**
102. **`packages/react-native-renderer/src/ReactNativeBridgeEventPlugin.js`** -> AI Confidence: **99.31%**
103. **`packages/react-native-renderer/src/ReactNativeEventEmitter.js`** -> AI Confidence: **99.31%**
104. **`packages/react-native-renderer/src/ReactNativePublicCompat.js`** -> AI Confidence: **99.31%**
105. **`packages/react-noop-renderer/src/createReactNoop.js`** -> AI Confidence: **99.31%**
106. **`packages/react-reconciler/src/ReactChildFiber.js`** -> AI Confidence: **99.31%**
107. **`packages/react-reconciler/src/ReactFiber.js`** -> AI Confidence: **99.31%**
108. **`packages/react-reconciler/src/ReactFiberBeginWork.js`** -> AI Confidence: **99.31%**
109. **`packages/react-reconciler/src/ReactFiberClassUpdateQueue.js`** -> AI Confidence: **99.31%**
110. **`packages/react-reconciler/src/ReactFiberCommitHostEffects.js`** -> AI Confidence: **99.31%**
111. **`packages/react-reconciler/src/ReactFiberCommitViewTransitions.js`** -> AI Confidence: **99.31%**
112. **`packages/react-reconciler/src/ReactFiberCompleteWork.js`** -> AI Confidence: **99.31%**
113. **`packages/react-reconciler/src/ReactFiberDevToolsHook.js`** -> AI Confidence: **99.31%**
114. **`packages/react-reconciler/src/ReactFiberErrorLogger.js`** -> AI Confidence: **99.31%**
115. **`packages/react-reconciler/src/ReactFiberHooks.js`** -> AI Confidence: **99.31%**
116. **`packages/react-reconciler/src/ReactFiberHotReloading.js`** -> AI Confidence: **99.31%**
117. **`packages/react-reconciler/src/ReactFiberHydrationContext.js`** -> AI Confidence: **99.31%**
118. **`packages/react-reconciler/src/ReactFiberHydrationDiffs.js`** -> AI Confidence: **99.31%**
119. **`packages/react-reconciler/src/ReactFiberLane.js`** -> AI Confidence: **99.31%**
120. **`packages/react-reconciler/src/ReactFiberNewContext.js`** -> AI Confidence: **99.31%**
121. **`packages/react-reconciler/src/ReactFiberReconciler.js`** -> AI Confidence: **99.31%**
122. **`packages/react-reconciler/src/ReactFiberRoot.js`** -> AI Confidence: **99.31%**
123. **`packages/react-reconciler/src/ReactFiberThrow.js`** -> AI Confidence: **99.31%**
124. **`packages/react-reconciler/src/ReactFiberTreeReflection.js`** -> AI Confidence: **99.31%**
125. **`packages/react-reconciler/src/ReactFiberUnwindWork.js`** -> AI Confidence: **99.31%**
126. **`packages/react-reconciler/src/getComponentNameFromFiber.js`** -> AI Confidence: **99.31%**
127. **`packages/react-server-dom-esm/src/server/ReactFlightDOMServerNode.js`** -> AI Confidence: **99.31%**
128. **`packages/react-server-dom-parcel/src/server/ReactFlightDOMServerBrowser.js`** -> AI Confidence: **99.31%**
129. **`packages/react-server-dom-parcel/src/server/ReactFlightDOMServerEdge.js`** -> AI Confidence: **99.31%**
130. **`packages/react-server-dom-parcel/src/server/ReactFlightDOMServerNode.js`** -> AI Confidence: **99.31%**
131. **`packages/react-server-dom-turbopack/src/server/ReactFlightDOMServerBrowser.js`** -> AI Confidence: **99.31%**
132. **`packages/react-server-dom-turbopack/src/server/ReactFlightDOMServerEdge.js`** -> AI Confidence: **99.31%**
133. **`packages/react-server-dom-turbopack/src/server/ReactFlightDOMServerNode.js`** -> AI Confidence: **99.31%**
134. **`packages/react-server-dom-unbundled/src/server/ReactFlightDOMServerNode.js`** -> AI Confidence: **99.31%**
135. **`packages/react-server-dom-webpack/src/ReactFlightWebpackPlugin.js`** -> AI Confidence: **99.31%**
136. **`packages/react-server-dom-webpack/src/server/ReactFlightDOMServerBrowser.js`** -> AI Confidence: **99.31%**
137. **`packages/react-server-dom-webpack/src/server/ReactFlightDOMServerEdge.js`** -> AI Confidence: **99.31%**
138. **`packages/react-server-dom-webpack/src/server/ReactFlightDOMServerNode.js`** -> AI Confidence: **99.31%**
139. **`packages/react-server/src/ReactFizzServer.js`** -> AI Confidence: **99.31%**
140. **`packages/react-server/src/ReactFlightReplyServer.js`** -> AI Confidence: **99.31%**
141. **`packages/react-server/src/ReactFlightServer.js`** -> AI Confidence: **99.31%**
142. **`packages/react-test-renderer/src/ReactTestRenderer.js`** -> AI Confidence: **99.31%**
143. **`packages/react/src/ReactChildren.js`** -> AI Confidence: **99.31%**
144. **`packages/react/src/jsx/ReactJSXElement.js`** -> AI Confidence: **99.31%**
145. **`scripts/bench/runner.js`** -> AI Confidence: **99.31%**
146. **`scripts/flags/flags.js`** -> AI Confidence: **99.31%**
147. **`compiler/apps/playground/components/Editor/Output.tsx`** -> AI Confidence: **99.31%**
148. **`compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Gating.ts`** -> AI Confidence: **99.31%**
149. **`compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Program.ts`** -> AI Confidence: **99.31%**
150. **`compiler/packages/babel-plugin-react-compiler/src/HIR/Environment.ts`** -> AI Confidence: **99.31%**
151. **`compiler/packages/babel-plugin-react-compiler/src/HIR/Globals.ts`** -> AI Confidence: **99.31%**
152. **`compiler/packages/babel-plugin-react-compiler/src/HIR/HIRBuilder.ts`** -> AI Confidence: **99.31%**
153. **`compiler/packages/babel-plugin-react-compiler/src/HIR/PropagateScopeDependenciesHIR.ts`** -> AI Confidence: **99.31%**
154. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/MergeReactiveScopesThatInvalidateTogether.ts`** -> AI Confidence: **99.31%**
155. **`compiler/packages/babel-plugin-react-compiler/src/TypeInference/InferTypes.ts`** -> AI Confidence: **99.31%**
156. **`compiler/packages/snap/src/runner-worker.ts`** -> AI Confidence: **99.31%**
157. **`compiler/packages/snap/src/runner.ts`** -> AI Confidence: **99.31%**
158. **`babel.config-react-compiler.js`** -> AI Confidence: **99.29%**
159. **`compiler/packages/babel-plugin-react-compiler/scripts/jest/makeE2EConfig.js`** -> AI Confidence: **99.29%**
160. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/error.unconditional-set-state-in-render-after-loop-break.js`** -> AI Confidence: **99.29%**
161. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/error.unconditional-set-state-in-render-with-loop-throw.js`** -> AI Confidence: **99.29%**
162. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/for-in-statement-continue.js`** -> AI Confidence: **99.29%**
163. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/optional-call-with-optional-property-load.js`** -> AI Confidence: **99.29%**
164. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-propagate-type-of-ternary-nested.js`** -> AI Confidence: **99.29%**
165. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/reverse-postorder.js`** -> AI Confidence: **99.29%**
166. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-conditionally-call-prop-named-like-hook.js`** -> AI Confidence: **99.29%**
167. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-2aabd222fc6a.js`** -> AI Confidence: **99.29%**
168. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-49d341e5d68f.js`** -> AI Confidence: **99.29%**
169. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-79128a755612.js`** -> AI Confidence: **99.29%**
170. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-9bf17c174134.js`** -> AI Confidence: **99.29%**
171. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-b4dcda3d60ed.js`** -> AI Confidence: **99.29%**
172. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-d740d54e9c21.js`** -> AI Confidence: **99.29%**
173. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-d85c144bdf40.js`** -> AI Confidence: **99.29%**
174. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-ea7c2fb545a9.js`** -> AI Confidence: **99.29%**
175. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-0e2214abc294.js`** -> AI Confidence: **99.29%**
176. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-2e405c78cb80.js`** -> AI Confidence: **99.29%**
177. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-485bf041f55f.js`** -> AI Confidence: **99.29%**
178. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-69521d94fa03.js`** -> AI Confidence: **99.29%**
179. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-c1e8c7f4c191.js`** -> AI Confidence: **99.29%**
180. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-c5d1f3143c4c.js`** -> AI Confidence: **99.29%**
181. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-e5dd6caf4084.js`** -> AI Confidence: **99.29%**
182. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/rules-of-hooks-fe6042f7628b.js`** -> AI Confidence: **99.29%**
183. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/todo.bail.rules-of-hooks-6949b255e7eb.js`** -> AI Confidence: **99.29%**
184. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/todo.error.invalid-rules-of-hooks-a0058f0b446d.js`** -> AI Confidence: **99.29%**
185. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/todo.error.rules-of-hooks-e29c874aa913.js`** -> AI Confidence: **99.29%**
186. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/switch-with-fallthrough.js`** -> AI Confidence: **99.29%**
187. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/ternary-expression.js`** -> AI Confidence: **99.29%**
188. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/todo.memoize-loops-that-produce-memoizeable-values.js`** -> AI Confidence: **99.29%**
189. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/try-catch-nested-optional-chaining.js`** -> AI Confidence: **99.29%**
190. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/try-catch-nullish-coalescing.js`** -> AI Confidence: **99.29%**
191. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/while-conditional-continue.js`** -> AI Confidence: **99.29%**
192. **`fixtures/dom/src/components/fixtures/home.js`** -> AI Confidence: **99.29%**
193. **`fixtures/flight-ssr-bench/webpack.config.js`** -> AI Confidence: **99.29%**
194. **`fixtures/legacy-jsx-runtimes/react-14/jsx-dev-runtime.js`** -> AI Confidence: **99.29%**
195. **`fixtures/legacy-jsx-runtimes/react-14/jsx-runtime.js`** -> AI Confidence: **99.29%**
196. **`fixtures/legacy-jsx-runtimes/react-15/jsx-dev-runtime.js`** -> AI Confidence: **99.29%**
197. **`fixtures/legacy-jsx-runtimes/react-15/jsx-runtime.js`** -> AI Confidence: **99.29%**
198. **`fixtures/legacy-jsx-runtimes/react-16/jsx-dev-runtime.js`** -> AI Confidence: **99.29%**
199. **`fixtures/legacy-jsx-runtimes/react-16/jsx-runtime.js`** -> AI Confidence: **99.29%**
200. **`fixtures/legacy-jsx-runtimes/react-17/jsx-dev-runtime.js`** -> AI Confidence: **99.29%**
201. **`fixtures/legacy-jsx-runtimes/react-17/jsx-runtime.js`** -> AI Confidence: **99.29%**
202. **`flow-typed/environments/geometry.js`** -> AI Confidence: **99.29%**
203. **`flow-typed/npm/error-stack-parser_v2.x.x.js`** -> AI Confidence: **99.29%**
204. **`flow-typed/npm/minimist_v1.x.x.js`** -> AI Confidence: **99.29%**
205. **`packages/eslint-plugin-react-hooks/npm/index.js`** -> AI Confidence: **99.29%**
206. **`packages/eslint-plugin-react-hooks/src/code-path-analysis/assert.js`** -> AI Confidence: **99.29%**
207. **`packages/eslint-plugin-react-hooks/src/code-path-analysis/code-path-analyzer.js`** -> AI Confidence: **99.29%**
208. **`packages/eslint-plugin-react-hooks/src/code-path-analysis/code-path.js`** -> AI Confidence: **99.29%**
209. **`packages/jest-react/npm/index.js`** -> AI Confidence: **99.29%**
210. **`packages/react-art/npm/index.js`** -> AI Confidence: **99.29%**
211. **`packages/react-cache/npm/index.js`** -> AI Confidence: **99.29%**
212. **`packages/react-client/npm/flight.js`** -> AI Confidence: **99.29%**
213. **`packages/react-client/src/ReactClientDebugConfigNode.js`** -> AI Confidence: **99.29%**
214. **`packages/react-client/src/ReactFlightPerformanceTrack.js`** -> AI Confidence: **99.29%**
215. **`packages/react-debug-tools/npm/index.js`** -> AI Confidence: **99.29%**
216. **`packages/react-devtools-core/webpack.backend.js`** -> AI Confidence: **99.29%**
217. **`packages/react-devtools-core/webpack.standalone.js`** -> AI Confidence: **99.29%**
218. **`packages/react-devtools-inline/webpack.config.js`** -> AI Confidence: **99.29%**
219. **`packages/react-devtools-shared/buildUtils.js`** -> AI Confidence: **99.29%**
220. **`packages/react-devtools-shared/src/backend/NativeStyleEditor/resolveBoxStyle.js`** -> AI Confidence: **99.29%**
221. **`packages/react-devtools-shared/src/devtools/views/ButtonIcon.js`** -> AI Confidence: **99.29%**
222. **`packages/react-devtools-shared/src/devtools/views/Icon.js`** -> AI Confidence: **99.29%**
223. **`packages/react-devtools/bin.js`** -> AI Confidence: **99.29%**
224. **`packages/react-dom-bindings/src/shared/ReactControlledValuePropTypes.js`** -> AI Confidence: **99.29%**
225. **`packages/react-dom-bindings/src/shared/ReactDOMNullInputValuePropHook.js`** -> AI Confidence: **99.29%**
226. **`packages/react-dom-bindings/src/shared/warnValidStyle.js`** -> AI Confidence: **99.29%**
227. **`packages/react-dom/npm/client.js`** -> AI Confidence: **99.29%**
228. **`packages/react-dom/npm/index.js`** -> AI Confidence: **99.29%**
229. **`packages/react-dom/npm/profiling.js`** -> AI Confidence: **99.29%**
230. **`packages/react-dom/npm/react-dom.react-server.js`** -> AI Confidence: **99.29%**
231. **`packages/react-dom/npm/unstable_testing.js`** -> AI Confidence: **99.29%**
232. **`packages/react-is/npm/index.js`** -> AI Confidence: **99.29%**
233. **`packages/react-markup/npm/index.js`** -> AI Confidence: **99.29%**
234. **`packages/react-markup/npm/react-markup.react-server.js`** -> AI Confidence: **99.29%**
235. **`packages/react-native-renderer/src/ReactFabricGlobalResponderHandler.js`** -> AI Confidence: **99.29%**
236. **`packages/react-native-renderer/src/__mocks__/react-native/Libraries/ReactPrivate/RawEventEmitter.js`** -> AI Confidence: **99.29%**
237. **`packages/react-noop-renderer/npm/flight-client.js`** -> AI Confidence: **99.29%**
238. **`packages/react-noop-renderer/npm/flight-server.js`** -> AI Confidence: **99.29%**
239. **`packages/react-noop-renderer/npm/index.js`** -> AI Confidence: **99.29%**
240. **`packages/react-noop-renderer/npm/persistent.js`** -> AI Confidence: **99.29%**
241. **`packages/react-noop-renderer/npm/server.js`** -> AI Confidence: **99.29%**
242. **`packages/react-reconciler/npm/constants.js`** -> AI Confidence: **99.29%**
243. **`packages/react-reconciler/npm/index.js`** -> AI Confidence: **99.29%**
244. **`packages/react-reconciler/npm/reflection.js`** -> AI Confidence: **99.29%**
245. **`packages/react-refresh/npm/babel.js`** -> AI Confidence: **99.29%**
246. **`packages/react-refresh/npm/runtime.js`** -> AI Confidence: **99.29%**
247. **`packages/react-server-dom-esm/npm/client.browser.js`** -> AI Confidence: **99.29%**
248. **`packages/react-server-dom-esm/npm/client.node.js`** -> AI Confidence: **99.29%**
249. **`packages/react-server-dom-parcel/npm/client.browser.js`** -> AI Confidence: **99.29%**
250. **`packages/react-server-dom-parcel/npm/client.edge.js`** -> AI Confidence: **99.29%**
251. **`packages/react-server-dom-parcel/npm/client.node.js`** -> AI Confidence: **99.29%**
252. **`packages/react-server-dom-turbopack/npm/client.browser.js`** -> AI Confidence: **99.29%**
253. **`packages/react-server-dom-turbopack/npm/client.edge.js`** -> AI Confidence: **99.29%**
254. **`packages/react-server-dom-turbopack/npm/client.node.js`** -> AI Confidence: **99.29%**
255. **`packages/react-server-dom-unbundled/npm/client.js`** -> AI Confidence: **99.29%**
256. **`packages/react-server-dom-webpack/npm/client.browser.js`** -> AI Confidence: **99.29%**
257. **`packages/react-server-dom-webpack/npm/client.edge.js`** -> AI Confidence: **99.29%**
258. **`packages/react-server-dom-webpack/npm/client.node.js`** -> AI Confidence: **99.29%**
259. **`packages/react-server-dom-webpack/npm/client.node.unbundled.js`** -> AI Confidence: **99.29%**
260. **`packages/react-server/npm/flight.js`** -> AI Confidence: **99.29%**
261. **`packages/react-server/npm/index.js`** -> AI Confidence: **99.29%**
262. **`packages/react/npm/compiler-runtime.js`** -> AI Confidence: **99.29%**
263. **`packages/react/npm/index.js`** -> AI Confidence: **99.29%**
264. **`packages/react/npm/jsx-dev-runtime.js`** -> AI Confidence: **99.29%**
265. **`packages/react/npm/jsx-dev-runtime.react-server.js`** -> AI Confidence: **99.29%**
266. **`packages/react/npm/jsx-runtime.js`** -> AI Confidence: **99.29%**
267. **`packages/react/npm/jsx-runtime.react-server.js`** -> AI Confidence: **99.29%**
268. **`packages/react/npm/react.react-server.js`** -> AI Confidence: **99.29%**
269. **`packages/react/npm/unstable-cache.js`** -> AI Confidence: **99.29%**
270. **`packages/scheduler/npm/index.js`** -> AI Confidence: **99.29%**
271. **`packages/scheduler/npm/index.native.js`** -> AI Confidence: **99.29%**
272. **`packages/scheduler/npm/unstable_post_task.js`** -> AI Confidence: **99.29%**
273. **`packages/use-subscription/npm/index.js`** -> AI Confidence: **99.29%**
274. **`packages/use-sync-external-store/npm/index.js`** -> AI Confidence: **99.29%**
275. **`packages/use-sync-external-store/npm/shim/index.js`** -> AI Confidence: **99.29%**
276. **`packages/use-sync-external-store/npm/shim/index.native.js`** -> AI Confidence: **99.29%**
277. **`packages/use-sync-external-store/npm/shim/with-selector.js`** -> AI Confidence: **99.29%**
278. **`packages/use-sync-external-store/npm/with-selector.js`** -> AI Confidence: **99.29%**
279. **`scripts/babel/transform-test-gate-pragma.js`** -> AI Confidence: **99.29%**
280. **`scripts/bench/benchmarks/hacker-news/top-stories.js`** -> AI Confidence: **99.29%**
281. **`scripts/eslint-rules/__tests__/no-primitive-constructors-test.internal.js`** -> AI Confidence: **99.29%**
282. **`scripts/eslint-rules/__tests__/no-production-logging-test.internal.js`** -> AI Confidence: **99.29%**
283. **`scripts/eslint-rules/__tests__/safe-string-coercion-test.internal.js`** -> AI Confidence: **99.29%**
284. **`scripts/eslint-rules/no-primitive-constructors.js`** -> AI Confidence: **99.29%**
285. **`scripts/flow/runFlow.js`** -> AI Confidence: **99.29%**
286. **`scripts/jest/TestFlags.js`** -> AI Confidence: **99.29%**
287. **`scripts/jest/config.base.js`** -> AI Confidence: **99.29%**
288. **`scripts/jest/devtools/config.build-devtools-regression.js`** -> AI Confidence: **99.29%**
289. **`scripts/jest/setupEnvironment.js`** -> AI Confidence: **99.29%**
290. **`scripts/tasks/danger.js`** -> AI Confidence: **99.29%**
291. **`scripts/tasks/generate-changelog/args.js`** -> AI Confidence: **99.29%**
292. **`scripts/tasks/linc.js`** -> AI Confidence: **99.29%**
293. **`compiler/packages/babel-plugin-react-compiler/src/HIR/PruneUnusedLabelsHIR.ts`** -> AI Confidence: **99.29%**
294. **`compiler/packages/babel-plugin-react-compiler/src/Optimization/OptimizeForSSR.ts`** -> AI Confidence: **99.29%**
295. **`compiler/packages/babel-plugin-react-compiler/src/Optimization/OutlineFunctions.ts`** -> AI Confidence: **99.29%**
296. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/AlignMethodCallScopes.ts`** -> AI Confidence: **99.29%**
297. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/BuildReactiveFunction.ts`** -> AI Confidence: **99.29%**
298. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/FlattenReactiveLoopsHIR.ts`** -> AI Confidence: **99.29%**
299. **`compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/PruneNonReactiveDependencies.ts`** -> AI Confidence: **99.29%**
300. **`compiler/packages/babel-plugin-react-compiler/src/SSA/RewriteInstructionKindsBasedOnReassignment.ts`** -> AI Confidence: **99.29%**
301. **`compiler/packages/babel-plugin-react-compiler/src/Transform/NameAnonymousFunctions.ts`** -> AI Confidence: **99.29%**
302. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateUseMemo.ts`** -> AI Confidence: **99.29%**
303. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/reduce-reactive-deps/memberexpr-join-optional-chain2.ts`** -> AI Confidence: **99.29%**
304. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/reduce-reactive-deps/memberexpr-join-optional-chain2.ts`** -> AI Confidence: **99.29%**
305. **`compiler/packages/babel-plugin-react-compiler/scripts/ts-analyze-trace.sh`** -> AI Confidence: **99.29%**
306. **`scripts/react-compiler/build-compiler.sh`** -> AI Confidence: **99.29%**
307. **`packages/react-devtools-extensions/src/main/index.js`** -> AI Confidence: **99.24%**
308. **`packages/react-devtools-shared/src/devtools/ProfilerStore.js`** -> AI Confidence: **99.24%**
309. **`packages/react-devtools-shared/src/devtools/views/Components/NewArrayValue.js`** -> AI Confidence: **99.24%**
310. **`packages/react-devtools-shared/src/devtools/views/Components/OwnersStack.js`** -> AI Confidence: **99.24%**
311. **`packages/react-devtools-shared/src/devtools/views/Profiler/HoveredFiberInfo.js`** -> AI Confidence: **99.24%**
312. **`packages/react-devtools-shared/src/devtools/views/Settings/GeneralSettings.js`** -> AI Confidence: **99.24%**
313. **`packages/react-devtools-shared/src/devtools/views/Settings/SettingsContext.js`** -> AI Confidence: **99.24%**
314. **`packages/react-devtools-shared/src/devtools/views/SuspenseTab/SuspenseBreadcrumbs.js`** -> AI Confidence: **99.24%**
315. **`packages/react-devtools-shared/src/hookNamesCache.js`** -> AI Confidence: **99.24%**
316. **`packages/react-dom-bindings/src/client/ReactDOMEventHandle.js`** -> AI Confidence: **99.24%**
317. **`packages/react-dom-bindings/src/events/plugins/BeforeInputEventPlugin.js`** -> AI Confidence: **99.24%**
318. **`packages/react-dom-bindings/src/events/plugins/FormActionEventPlugin.js`** -> AI Confidence: **99.24%**
319. **`packages/react-dom-bindings/src/events/plugins/SelectEventPlugin.js`** -> AI Confidence: **99.24%**
320. **`packages/react-dom-bindings/src/server/ReactFizzConfigDOM.js`** -> AI Confidence: **99.24%**
321. **`packages/react-native-renderer/src/ReactFabric.js`** -> AI Confidence: **99.24%**
322. **`packages/react-reconciler/src/ReactFiberRootScheduler.js`** -> AI Confidence: **99.24%**
323. **`packages/react-server/src/ReactFizzHooks.js`** -> AI Confidence: **99.24%**
324. **`scripts/devtools/prepare-release.js`** -> AI Confidence: **99.24%**
325. **`scripts/jest/setupTests.js`** -> AI Confidence: **99.24%**
326. **`compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Pipeline.ts`** -> AI Confidence: **99.24%**
327. **`compiler/packages/snap/src/sprout/evaluator.ts`** -> AI Confidence: **99.24%**
328. **`compiler/scripts/enable-feature-flag.js`** -> AI Confidence: **99.23%**
329. **`packages/react-devtools-shared/src/devtools/views/Profiler/CommitTreeBuilder.js`** -> AI Confidence: **99.23%**
330. **`packages/react-devtools-shared/src/devtools/views/SuspenseTab/SuspenseScrubber.js`** -> AI Confidence: **99.23%**
331. **`packages/react-server-dom-turbopack/src/client/ReactFlightDOMClientNode.js`** -> AI Confidence: **99.23%**
332. **`packages/react-server-dom-unbundled/src/client/ReactFlightDOMClientNode.js`** -> AI Confidence: **99.23%**
333. **`packages/react-server-dom-webpack/src/client/ReactFlightDOMClientNode.js`** -> AI Confidence: **99.23%**
334. **`packages/shared/ReactPerformanceTrackProperties.js`** -> AI Confidence: **99.23%**
335. **`scripts/devtools/publish-release.js`** -> AI Confidence: **99.23%**
336. **`scripts/devtools/utils.js`** -> AI Confidence: **99.23%**
337. **`compiler/packages/babel-plugin-react-compiler/src/HIR/FindContextIdentifiers.ts`** -> AI Confidence: **99.23%**
338. **`compiler/packages/babel-plugin-react-compiler/src/Optimization/ConstantPropagation.ts`** -> AI Confidence: **99.23%**
339. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoFreezingKnownMutableFunctions.ts`** -> AI Confidence: **99.23%**
340. **`compiler/packages/snap/src/reporter.ts`** -> AI Confidence: **99.23%**
341. **`packages/eslint-plugin-react-hooks/src/shared/RunReactCompiler.ts`** -> AI Confidence: **99.23%**
342. **`fixtures/ssr/server/index.js`** -> AI Confidence: **99.22%**
343. **`packages/react-dom-bindings/src/client/CSSPropertyOperations.js`** -> AI Confidence: **99.22%**
344. **`packages/react-reconciler/src/ReactFiberComponentStack.js`** -> AI Confidence: **99.22%**
345. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateContextVariableLValues.ts`** -> AI Confidence: **99.22%**
346. **`fixtures/devtools/scheduling-profiler/run.js`** -> AI Confidence: **99.2%**
347. **`fixtures/fizz/scripts/build.js`** -> AI Confidence: **99.2%**
348. **`fixtures/ssr2/scripts/build.js`** -> AI Confidence: **99.2%**
349. **`packages/react-dom-bindings/src/server/ReactDOMFlightServerHostDispatcher.js`** -> AI Confidence: **99.2%**
350. **`packages/react-dom-bindings/src/server/ReactFlightServerConfigDOM.js`** -> AI Confidence: **99.2%**
351. **`scripts/error-codes/extract-errors.js`** -> AI Confidence: **99.2%**
352. **`compiler/packages/babel-plugin-react-compiler/src/Optimization/DeadCodeElimination.ts`** -> AI Confidence: **99.2%**
353. **`fixtures/dom/src/components/fixtures/input-change-events/index.js`** -> AI Confidence: **99.18%**
354. **`fixtures/flight-ssr-bench/bench.js`** -> AI Confidence: **99.18%**
355. **`packages/react-client/src/__tests__/ReactFlight-test.js`** -> AI Confidence: **99.18%**
356. **`packages/react-devtools-shared/src/backend/types.js`** -> AI Confidence: **99.18%**
357. **`packages/react-devtools-shared/src/backendAPI.js`** -> AI Confidence: **99.18%**
358. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementContext.js`** -> AI Confidence: **99.18%**
359. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementContextTree.js`** -> AI Confidence: **99.18%**
360. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementSourcePanel.js`** -> AI Confidence: **99.18%**
361. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementStateTree.js`** -> AI Confidence: **99.18%**
362. **`packages/react-devtools-shared/src/devtools/views/Components/KeyValueContextMenuContainer.js`** -> AI Confidence: **99.18%**
363. **`packages/react-devtools-shared/src/devtools/views/Components/NativeStyleEditor/StyleEditor.js`** -> AI Confidence: **99.18%**
364. **`packages/react-devtools-shared/src/devtools/views/Components/NativeStyleEditor/index.js`** -> AI Confidence: **99.18%**
365. **`packages/react-devtools-shared/src/devtools/views/Components/OwnersListContext.js`** -> AI Confidence: **99.18%**
366. **`packages/react-devtools-shared/src/devtools/views/Editor/EditorPane.js`** -> AI Confidence: **99.18%**
367. **`packages/react-devtools-shared/src/devtools/views/Profiler/ProfilingImportExportButtons.js`** -> AI Confidence: **99.18%**
368. **`packages/react-devtools-shared/src/devtools/views/Profiler/SidebarEventInfo.js`** -> AI Confidence: **99.18%**
369. **`packages/react-devtools-shared/src/devtools/views/UnsupportedBridgeProtocolDialog.js`** -> AI Confidence: **99.18%**
370. **`packages/react-devtools-shared/src/inspectedElementCache.js`** -> AI Confidence: **99.18%**
371. **`packages/react-devtools-timeline/src/content-views/FlamechartView.js`** -> AI Confidence: **99.18%**
372. **`packages/react-dom-bindings/src/events/plugins/ScrollEndEventPlugin.js`** -> AI Confidence: **99.18%**
373. **`packages/react-dom-bindings/src/events/plugins/SimpleEventPlugin.js`** -> AI Confidence: **99.18%**
374. **`packages/react-dom/src/__tests__/ReactClassComponentPropResolutionFizz-test.js`** -> AI Confidence: **99.18%**
375. **`packages/react-dom/src/__tests__/ReactDOMFizzShellHydration-test.js`** -> AI Confidence: **99.18%**
376. **`packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js`** -> AI Confidence: **99.18%**
377. **`packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js`** -> AI Confidence: **99.18%**
378. **`packages/react-dom/src/__tests__/ReactDOMServerSelectiveHydrationActivity-test.internal.js`** -> AI Confidence: **99.18%**
379. **`packages/react-native-renderer/src/ReactFabricEventEmitter.js`** -> AI Confidence: **99.18%**
380. **`packages/react-reconciler/src/ReactFiberThenable.js`** -> AI Confidence: **99.18%**
381. **`packages/react-reconciler/src/__tests__/ReactSuspenseFuzz-test.internal.js`** -> AI Confidence: **99.18%**
382. **`packages/react-refresh/src/__tests__/ReactFreshIntegration-test.js`** -> AI Confidence: **99.18%**
383. **`packages/react-refresh/src/__tests__/ReactFreshMultipleRenderer-test.internal.js`** -> AI Confidence: **99.18%**
384. **`packages/react-server-dom-turbopack/src/__tests__/ReactFlightTurbopackDOMEdge-test.js`** -> AI Confidence: **99.18%**
385. **`packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMNode-test.js`** -> AI Confidence: **99.18%**
386. **`packages/react-server/src/__tests__/ReactFlightAsyncDebugInfo-test.js`** -> AI Confidence: **99.18%**
387. **`packages/react-server/src/__tests__/ReactFlightServer-test.js`** -> AI Confidence: **99.18%**
388. **`packages/react-server/src/forks/ReactFlightServerConfig.dom-edge-parcel.js`** -> AI Confidence: **99.18%**
389. **`packages/react-server/src/forks/ReactFlightServerConfig.dom-edge-turbopack.js`** -> AI Confidence: **99.18%**
390. **`packages/react-server/src/forks/ReactFlightServerConfig.dom-edge.js`** -> AI Confidence: **99.18%**
391. **`packages/react/src/__tests__/ReactMismatchedVersions-test.js`** -> AI Confidence: **99.18%**
392. **`scripts/devtools/build-and-test.js`** -> AI Confidence: **99.18%**
393. **`compiler/apps/playground/components/Editor/Input.tsx`** -> AI Confidence: **99.18%**
394. **`compiler/packages/snap/src/compiler.ts`** -> AI Confidence: **99.18%**
395. **`fixtures/flight-parcel/src/server.tsx`** -> AI Confidence: **99.18%**
396. **`compiler/packages/babel-plugin-react-compiler/scripts/eslint-plugin-react-hooks-test-cases.js`** -> AI Confidence: **99.17%**
397. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/debugger.js`** -> AI Confidence: **99.17%**
398. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/dominator.js`** -> AI Confidence: **99.17%**
399. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/mutable-lifetime-with-aliasing.js`** -> AI Confidence: **99.17%**
400. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/optional-call-chained.js`** -> AI Confidence: **99.17%**
401. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/optional-member-expression-with-optional-member-expr-as-property.js`** -> AI Confidence: **99.17%**
402. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/switch-non-final-default.js`** -> AI Confidence: **99.17%**
403. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-memoize-for-of-collection-when-loop-body-returns.js`** -> AI Confidence: **99.17%**
404. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-optional-methodcall.js`** -> AI Confidence: **99.17%**
405. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-optional-property.js`** -> AI Confidence: **99.17%**
406. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-optionalcall.js`** -> AI Confidence: **99.17%**
407. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/ssa-sibling-phis.js`** -> AI Confidence: **99.17%**
408. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/switch-non-final-default.js`** -> AI Confidence: **99.17%**
409. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/unused-logical-assigned-to-variable.js`** -> AI Confidence: **99.17%**
410. **`fixtures/dom/src/components/fixtures/fragment-refs/CompareDocumentPositionFragmentContainer.js`** -> AI Confidence: **99.17%**
411. **`fixtures/owner-stacks/src/App.js`** -> AI Confidence: **99.17%**
412. **`flow-typed/environments/dom.js`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `packages/react-devtools-shared/src/hooks/__tests__/updateMockSourceMaps.js` -> **0.2199%** Exposure
### Exploit Generation Surface
- `fixtures/art/VectorWidget.js` -> **100.0%** Exposure
- `fixtures/attribute-behavior/src/App.js` -> **100.0%** Exposure
- `fixtures/concurrent/time-slicing/src/Clock.js` -> **100.0%** Exposure
- `fixtures/concurrent/time-slicing/src/index.js` -> **100.0%** Exposure
- `fixtures/devtools/regression/shared.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `compiler/scripts/copyright.js` -> **100.0%** Exposure
- `fixtures/fiber-debugger/src/App.js` -> **100.0%** Exposure
- `fixtures/flight-esm/server/global.js` -> **100.0%** Exposure
- `fixtures/flight/config/paths.js` -> **100.0%** Exposure
- `fixtures/flight/server/global.js` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `scripts/tasks/danger.js` -> **100.0%** Exposure
- `compiler/packages/react-mcp-server/src/utils/algolia.ts` -> **99.9946%** Exposure
- `packages/react-client/src/__tests__/ReactFlight-test.js` -> **68.6348%** Exposure
### Algorithmic DoS Exposure
- `compiler/apps/playground/next.config.js` -> **100.0%** Exposure
- `compiler/scripts/anonymize.js` -> **100.0%** Exposure
- `fixtures/attribute-behavior/src/App.js` -> **100.0%** Exposure
- `fixtures/concurrent/time-slicing/src/Clock.js` -> **100.0%** Exposure
- `fixtures/concurrent/time-slicing/src/index.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5787` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `fixtures/concurrent/time-slicing/src/Clock.js` (JAVASCRIPT) -> Cumulative Risk: **853.57**
- **Archetype:** `file_cluster_4` (Distance: 12.857 IQR)
- **Magnitude:** 0.17 | **LOC:** 106 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `animate` (Impact: 33.3), `render` (Impact: 6.8), `componentDidMount` (Impact: 3.1)

### 2. `packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js` (JAVASCRIPT) -> Cumulative Risk: **850.44**
- **Archetype:** `file_cluster_4` (Distance: 11.599 IQR)
- **Magnitude:** 1428.22 | **LOC:** 4231 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `describe` (Impact: 606.4), `it` (Impact: 17.9), `it` (Impact: 15.4)

### 3. `packages/react-devtools-shared/src/backend/agent.js` (JAVASCRIPT) -> Cumulative Risk: **850.07**
- **Archetype:** `file_cluster_13` (Distance: 12.872 IQR)
- **Magnitude:** 397.58 | **LOC:** 1211 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `void` (Impact: 114.7), `setTimeout` (Impact: 8.9), `registerRendererInterface` (Impact: 6.8)

### 4. `packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js` (JAVASCRIPT) -> Cumulative Risk: **842.72**
- **Archetype:** `file_cluster_4` (Distance: 11.443 IQR)
- **Magnitude:** 989.72 | **LOC:** 2980 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `describe` (Impact: 325.2), `it` (Impact: 24.6), `it` (Impact: 21.8)

### 5. `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/visitors.ts` (TYPESCRIPT) -> Cumulative Risk: **809.01**
- **Archetype:** `file_cluster_8` (Distance: 12.851 IQR)
- **Magnitude:** 120.72 | **LOC:** 667 | **CtrlFlow:** 90.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `traverseTerminal` (Impact: 221.9), `traverseTerminal` (Impact: 160.1), `fn` (Impact: 119.9)

### 6. `fixtures/dom/src/components/fixtures/error-handling/index.js` (JAVASCRIPT) -> Cumulative Risk: **803.53**
- **Archetype:** `file_cluster_2` (Distance: 11.164 IQR)
- **Magnitude:** 0.27 | **LOC:** 407 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `render` (Impact: 46.1), `render` (Impact: 11.3), `triggerErrorAndCatch` (Impact: 11.1)

### 7. `fixtures/dom/src/components/fixtures/suspense/index.js` (JAVASCRIPT) -> Cumulative Risk: **799.01**
- **Archetype:** `file_cluster_2` (Distance: 9.915 IQR)
- **Magnitude:** 0.14 | **LOC:** 324 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `render` (Impact: 35.2), `render` (Impact: 8.1), `onKeydown` (Impact: 5.4)

### 8. `fixtures/concurrent/time-slicing/src/index.js` (JAVASCRIPT) -> Cumulative Risk: **796.9**
- **Archetype:** `file_cluster_17` (Distance: 13.084 IQR)
- **Magnitude:** 0.19 | **LOC:** 147 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `handleChange` (Impact: 27.0), `handleChartClick` (Impact: 14.2), `render` (Impact: 9.8)

### 9. `packages/react-dom/src/__tests__/ReactCompositeComponentState-test.js` (JAVASCRIPT) -> Cumulative Risk: **793.3**
- **Archetype:** `file_cluster_8` (Distance: 11.77 IQR)
- **Magnitude:** 334.72 | **LOC:** 612 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `describe` (Impact: 24.2), `it` (Impact: 7.5), `it` (Impact: 7.1)

### 10. `flow-typed/environments/node.js` (JAVASCRIPT) -> Cumulative Risk: **793.05**
- **Archetype:** `file_cluster_8` (Distance: 11.19 IQR)
- **Magnitude:** 1622.96 | **LOC:** 4287 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9157%)
- **Heaviest Functions:** `writeFile` (Impact: 221.6), `zlib$brotliAsyncFn` (Impact: 69.1), `writeProcessing` (Impact: 57.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/react-client/src/ReactFlightClient.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.026 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.738 IQR)
- **Top Global Matches:** file_cluster_8: 13.026, file_cluster_13: 13.215, file_cluster_17: 13.276
- **Magnitude:** 6219.46 | **LOC:** 5407 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 44.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (52.0896%), Tech Debt (49.4347%)
**Top Internal Functions/Classes:**
  * `initializeDebugChunk` (Impact: 5037.6 | O(2^N) | DB: 113)
  * `processFullStringRow` (Impact: 551.7 | O(2^N) | DB: 14)
    * *Intent:* // $FlowFixMe[invalid-constructor]: the shapes are exact here but Flow doesn't like constructors
  * `rejectChunk` (Impact: 47.9 | O(2^N))
  * `resolve` (Impact: 31.7 | O(2^N) | DB: 1)
  * `resolveModelChunk` (Impact: 14.3 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 561`, `structural_boundaries: 232`, `args: 97`, `func_start: 179`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 307`, `dead_code: 5`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 6`
* *Architecture:* `io: 12`, `api: 10`, `concurrency: 33`, `import: 22`
* *Defense:* `safety: 189`, `doc: 1`, `test: 1`, `immutability_locks: 210`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ReactSharedInternalsServer, ReactFlightReplyClient, hasOwnProperty, ReactFlightClientDevToolsHook, ReactFlightPerformanceTrack, ReactFlightPropertyAccess, ReactLazy, ReactSharedInternalsClient...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `fixtures/fiber-debugger/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/nesting/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-server/src/ReactFlightServer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.668 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.711 IQR)
- **Top Global Matches:** file_cluster_8: 13.668, file_cluster_13: 13.83, file_cluster_17: 13.837
- **Magnitude:** 4912.48 | **LOC:** 6445 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 40.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (52.9329%), Tech Debt (33.3869%)
**Top Internal Functions/Classes:**
  * `throwTaintViolation` (Impact: 2901.3 | O(2^N) | DB: 61)
  * `createTask` (Impact: 470.6 | O(2^N) | DB: 8)
    * *Intent:* // We don't have a chunk to assign debug info. We need to outline this
  * `serializeThenable` (Impact: 226.3 | O(N^3) | DB: 7)
  * `getAsyncIterator` (Impact: 221.0 | O(N^4) | DB: 4)
  * `findCalledFunctionNameFromStackTrace` (Impact: 111.1 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 691`, `structural_boundaries: 356`, `args: 134`, `func_start: 299`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 380`, `dead_code: 2`, `planned_debt: 22`, `fragile_debt: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 27`, `concurrency: 58`, `import: 29`
* *Defense:* `safety: 399`, `doc: 1`, `test: 1`, `immutability_locks: 284`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.126
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` ReactOwnerStackReset, ReactFlightServerConfig, hasOwnProperty, ReactFlightServerTemporaryReferences, ReactFlightCurrentOwner, ReactServerStreamConfig, ReactFlightAsyncSequence, ReactSharedInternalsServer...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `packages/react-devtools-shared/src/backend/fiber/renderer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.779 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.671 IQR)
- **Top Global Matches:** file_cluster_8: 13.779, file_cluster_17: 13.952, file_cluster_13: 13.978
- **Magnitude:** 4181.18 | **LOC:** 8154 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 48.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (49.1671%), Tech Debt (29.7589%)
**Top Internal Functions/Classes:**
  * `getSuspendedByRange` (Impact: 614.8 | O(2^N) | DB: 29)
  * `recordVirtualDisconnect` (Impact: 562.7 | O(N^4) | DB: 21)
    * *Intent:* // TODO: Consider using a WeakMap instead. The only thing where that doesn't work // is React Native...
  * `overrideSuspense` (Impact: 465.5 | O(2^N) | DB: 19)
    * *Intent:* // Next, we'll pop back out of the SuspenseNode that we added above and now we'll
  * `recordSuspenseUnmount` (Impact: 411.9 | O(2^N) | DB: 13)
  * `updateVirtualChildrenRecursively` (Impact: 408.2 | O(N^5) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 670`, `structural_boundaries: 285`, `args: 87`, `func_start: 214`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 374`, `dead_code: 3`, `planned_debt: 11`, `fragile_debt: 7`, `duplicate_logic: 6`
* *Architecture:* `io: 9`, `api: 8`, `concurrency: 16`, `import: 30`
* *Defense:* `safety: 366`, `doc: 2`, `test: 2`, `immutability_locks: 244`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` constants, DevToolsFiberChangeDetection, DevToolsFiberSuspense, DevToolsOwnerStack, DevToolsFiberInspection, ReactIODescription, DevToolsFiberInternalReactConstants, ReactSymbols...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberCommitWork.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.919 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.597 IQR)
- **Top Global Matches:** file_cluster_8: 11.919, file_cluster_13: 12.337, file_cluster_7: 12.474
- **Magnitude:** 3752.22 | **LOC:** 5350 | **CtrlFlow:** 83.4% | **Authorship Centralization:** 31.2%
- **Algorithmic:** O(N^5) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (16.0611%), Tech Debt (19.7399%)
**Top Internal Functions/Classes:**
  * `commitSuspenseHydrationCallbacks` (Impact: 2112.1 | O(N^4) | DB: 21)
  * `commitBeforeMutationEffects_begin` (Impact: 1483.0 | O(N^5) | DB: 12)
    * *Intent:* // Used during the commit phase to track the state of the Offscreen component stack.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 128`, `args: 48`, `func_start: 281`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 97`, `dead_code: 1`, `planned_debt: 39`, `fragile_debt: 5`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 39`
* *Defense:* `safety: 169`, `doc: 1`, `immutability_locks: 183`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` ReactFiberCommitEffects, ReactFiberCommitHostEffects, ReactFiberSuspenseComponent, ReactFiberCommitViewTransitions, ReactFiberMutationTracking, ReactFiberFlags, ReactHookEffectTags, ReactFiberRootScheduler...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/bench/benchmarks/pe-class-components/benchmark.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.36 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.61 IQR)
- **Top Global Matches:** file_cluster_8: 13.36, file_cluster_2: 13.432, file_cluster_17: 13.516
- **Magnitude:** 3538.4 | **LOC:** 5586 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (39.9001%), Tech Debt (99.7595%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 114.9 | O(N^3) | DB: 29)
  * `render` (Impact: 110.3 | O(N^3) | DB: 29)
  * `render` (Impact: 104.8 | O(N^3) | DB: 32)
  * `render` (Impact: 93.6 | O(N^3) | DB: 28)
  * `render` (Impact: 92.0 | O(N^3) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 501`, `structural_boundaries: 867`, `args: 280`, `func_start: 248`, `class_start: 183`
* *Risk/State:* `state_mutation: 1497`, `duplicate_logic: 184`
* *Architecture:* `api: 1`
* *Defense:* `safety: 498`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.647 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.137 IQR)
- **Top Global Matches:** file_cluster_8: 11.647, file_cluster_2: 11.8, file_cluster_4: 11.855
- **Magnitude:** 2941.56 | **LOC:** 9605 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (79.0185%), Tech Debt (44.7589%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 812.5 | O(2^N) | DB: 36)
  * `it` (Impact: 278.5 | O(N^5) | DB: 47)
  * `it` (Impact: 34.8 | O(N^3) | DB: 4)
  * `it` (Impact: 28.6 | O(N^4) | DB: 2)
  * `it` (Impact: 22.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 1039`, `args: 693`, `func_start: 970`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 30`, `state_mutation: 285`, `planned_debt: 6`, `fragile_debt: 5`, `duplicate_logic: 31`
* *Architecture:* `io: 1`, `concurrency: 1146`, `import: 12`
* *Defense:* `safety: 32`, `doc: 1`, `test: 469`, `immutability_locks: 313`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` client, jsdom, scheduler, FizzTestUtils, server, static, stream, prop-types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactFiberBeginWork.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.309 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.656 IQR)
- **Top Global Matches:** file_cluster_8: 11.309, file_cluster_13: 11.533, file_cluster_7: 11.904
- **Magnitude:** 2773.68 | **LOC:** 4449 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (17.1642%), Tech Debt (13.79%)
**Top Internal Functions/Classes:**
  * `updateHostHoistable` (Impact: 2586.1 | O(2^N) | DB: 18)
  * `updateClassComponent` (Impact: 100.0 | O(N^3) | DB: 2)
  * `markComponentRenderStopped` (Impact: 3.4 | O(N^1))
  * `prepareToReadContext` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 140`, `args: 22`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 54`, `planned_debt: 5`, `fragile_debt: 4`
* *Architecture:* `api: 1`, `import: 54`
* *Defense:* `safety: 80`, `doc: 1`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` ReactChildFiber, ReactFiberHotReloading, shallowEqual, ReactFiberCallUserSpace, ReactCurrentFiber, ReactFiberSuspenseComponent, ReactFiberTransition, ReactLazy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.357 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.342 IQR)
- **Top Global Matches:** file_cluster_8: 10.357, file_cluster_2: 10.925, file_cluster_7: 11.02
- **Magnitude:** 2647.64 | **LOC:** 9641 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (14.1393%), Tech Debt (74.018%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 167.5 | O(N^5))
  * `it` (Impact: 163.4 | O(N^4))
  * `describe` (Impact: 163.0 | O(N^5) | DB: 24)
  * `describe` (Impact: 98.5 | O(N^3) | DB: 5)
  * `it` (Impact: 86.9 | O(N^6))
    * *Intent:* // When binding a stylesheet that was SSR'd in a boundary reveal there is a loadingState promise // ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 601`, `args: 343`, `func_start: 557`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 8`, `state_mutation: 72`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 59`, `orphaned_logic: 2`
* *Architecture:* `io: 22`, `concurrency: 470`, `import: 9`
* *Defense:* `safety: 20`, `doc: 4`, `test: 298`, `immutability_locks: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jsdom, FizzTestUtils, server, stream, unstable_mock, react-dom, react, internal-test-utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/bench/benchmarks/pe-functional-components/benchmark.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.535 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.272 IQR)
- **Top Global Matches:** file_cluster_8: 12.535, file_cluster_2: 12.639, file_cluster_17: 12.837
- **Magnitude:** 2626.68 | **LOC:** 5180 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.2794%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TransitionCell142` (Impact: 134.4 | O(N^3))
  * `FixedDataTableCell143` (Impact: 127.6 | O(N^3))
  * `ReactImage0` (Impact: 97.2 | O(N^2))
  * `AdsPETableHeader141` (Impact: 86.9 | O(N^2))
  * `AbstractButton3` (Impact: 86.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 501`, `structural_boundaries: 684`, `args: 280`, `func_start: 248`
* *Risk/State:* `state_mutation: 552`
* *Architecture:* `api: 32`
* *Defense:* `safety: 498`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/bench/benchmarks/pe-no-components/benchmark.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.508 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.307 IQR)
- **Top Global Matches:** file_cluster_8: 12.508, file_cluster_7: 13.115, file_cluster_11: 13.132
- **Magnitude:** 2534.66 | **LOC:** 4944 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.1242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TransitionCell142` (Impact: 134.4 | O(N^3))
  * `FixedDataTableCell143` (Impact: 127.6 | O(N^3))
  * `ReactImage0` (Impact: 97.2 | O(N^2))
  * `AdsPETableHeader141` (Impact: 86.9 | O(N^2))
  * `AbstractButton3` (Impact: 86.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 501`, `structural_boundaries: 682`, `args: 280`, `func_start: 540`
* *Risk/State:* `state_mutation: 552`
* *Architecture:* `api: 31`
* *Defense:* `safety: 498`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactFiberWorkLoop.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.582 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.797 IQR)
- **Top Global Matches:** file_cluster_8: 12.582, file_cluster_13: 12.688, file_cluster_11: 12.92
- **Magnitude:** 2219.28 | **LOC:** 5622 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 68.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (23.1746%), Tech Debt (58.2608%)
**Top Internal Functions/Classes:**
  * `performWorkOnRoot` (Impact: 880.7 | O(N^4) | DB: 8)
  * `unwindUnitOfWork` (Impact: 378.3 | O(N^3) | DB: 7)
  * `renderRootConcurrent` (Impact: 150.4 | O(N^5) | DB: 1)
  * `warnAboutRenderPhaseUpdatesInDEV` (Impact: 86.8 | O(N^3) | DB: 1)
  * `applyGestureOnRoot` (Impact: 77.0 | O(N^3) | DB: 2)
    * *Intent:* // This is conceptually like a suspend, but it's not associated with // a particular wakeable. It's ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 445`, `structural_boundaries: 196`, `args: 69`, `func_start: 241`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 120`, `dead_code: 4`, `planned_debt: 29`, `fragile_debt: 7`, `duplicate_logic: 6`
* *Architecture:* `api: 46`, `import: 65`
* *Defense:* `safety: 168`, `doc: 3`, `immutability_locks: 122`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.699
  * `Choke Point (Betweenness):` 0.000563 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` ReactFiberGestureScheduler, ReactOwnerStackReset, ReactChildFiber, ReactTestSelectors, ReactFiberTransition, ReactFiberSuspenseComponent, ReactFiberShellHydration, ReactCurrentFiber...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberHooks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.309 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.916 IQR)
- **Top Global Matches:** file_cluster_13: 12.309, file_cluster_8: 12.372, file_cluster_11: 12.528
- **Magnitude:** 2001.3 | **LOC:** 5238 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (33.0722%), Tech Debt (21.7929%)
**Top Internal Functions/Classes:**
  * `updateWorkInProgressHook` (Impact: 1557.9 | O(2^N) | DB: 23)
    * *Intent:* // This is reset by checkDidRenderIdHook
  * `checkDepsAreArrayDev` (Impact: 196.6 | O(N^3) | DB: 4)
  * `resetHooksOnUnwind` (Impact: 16.8 | O(N^2) | DB: 1)
  * `updateHookTypesDev` (Impact: 11.0 | O(N^2))
    * *Intent:* // In DEV, this list ensures that hooks are called in the same order between renders. // The list st...
  * `TransitionAwareHostComponent` (Impact: 9.9 | O(N^1) | DB: 1)
    * *Intent:* // In Strict Mode, during development, user functions are double invoked to // help detect side effe...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 182`, `args: 65`, `func_start: 93`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 108`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 8`
* *Architecture:* `io: 2`, `api: 20`, `concurrency: 15`, `import: 40`
* *Defense:* `safety: 122`, `doc: 1`, `immutability_locks: 122`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.000112 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` ReactFiberGestureScheduler, ReactFiberCallUserSpace, ReactFiberTransition, ReactHookEffectTags, ReactFiberFlags, ReactSharedInternals, ReactFiberNewContext, ReactFiberRootScheduler...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/react-server/src/ReactFizzServer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.806 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.623 IQR)
- **Top Global Matches:** file_cluster_8: 12.806, file_cluster_13: 12.987, file_cluster_17: 13.07
- **Magnitude:** 1983.14 | **LOC:** 6256 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 52.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (17.1527%), Tech Debt (20.9857%)
**Top Internal Functions/Classes:**
  * `erroredReplay` (Impact: 384.7 | O(N^3) | DB: 6)
    * *Intent:* // We finished rendering this node, so now we can consume this
  * `retryRenderTask` (Impact: 187.6 | O(N^3) | DB: 11)
  * `warnForMissingKey` (Impact: 123.3 | O(2^N) | DB: 3)
    * *Intent:* // We can reuse the current context and task to render the content immediately without // context sw...
  * `getThrownInfo` (Impact: 88.6 | O(N^2) | DB: 4)
  * `startWork` (Impact: 80.0 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 358`, `structural_boundaries: 189`, `args: 95`, `func_start: 206`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 226`, `dead_code: 4`, `planned_debt: 6`, `fragile_debt: 16`
* *Architecture:* `api: 35`, `import: 30`
* *Defense:* `safety: 225`, `doc: 1`, `immutability_locks: 173`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` ReactOwnerStackReset, ReactServerStreamConfig, ReactFizzTreeContext, ReactLazy, ReactFizzLegacyContext, ReactFizzComponentStack, ReactSerializationErrors, ReactFizzThenable...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `flow-typed/environments/node.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.19 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.935 IQR)
- **Top Global Matches:** file_cluster_8: 11.19, file_cluster_7: 11.667, file_cluster_2: 11.725
- **Magnitude:** 1622.96 | **LOC:** 4287 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (15.1827%), Tech Debt (96.4799%)
**Top Internal Functions/Classes:**
  * `writeFile` (Impact: 221.6 | O(2^N) | DB: 75)
  * `zlib$brotliAsyncFn` (Impact: 69.1 | O(2^N) | DB: 63)
  * `writeProcessing` (Impact: 57.9 | O(N^1) | DB: 9)
  * `ifError` (Impact: 53.5 | O(2^N))
  * `start` (Impact: 47.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1019`, `structural_boundaries: 614`, `args: 482`, `func_start: 967`
* *Risk/State:* `safety_bypasses: 576`, `high_risk_execution: 2`, `state_mutation: 230`, `dead_code: 2`, `planned_debt: 7`, `duplicate_logic: 38`, `orphaned_logic: 46`
* *Architecture:* `io: 186`, `api: 17`, `concurrency: 84`
* *Defense:* `safety: 22`, `doc: 47`, `test: 5`, `immutability_locks: 5`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.652
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberCompleteWork.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.065 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.874 IQR)
- **Top Global Matches:** file_cluster_8: 12.065, file_cluster_13: 12.173, file_cluster_11: 12.542
- **Magnitude:** 1537.62 | **LOC:** 2082 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (28.8199%), Tech Debt (27.8873%)
**Top Internal Functions/Classes:**
  * `updateHostComponent` (Impact: 955.8 | O(N^4) | DB: 14)
  * `appendAllChildren` (Impact: 291.7 | O(2^N) | DB: 4)
    * *Intent:* // TODO: If we move the `doesRequireClone` call after `bubbleProperties`
  * `appendAllChildrenToContainer` (Impact: 173.0 | O(2^N) | DB: 4)
  * `doesRequireClone` (Impact: 13.4 | O(N^1) | DB: 1)
  * `updateHostContainer` (Impact: 9.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 111`, `args: 12`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 69`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 6`
* *Architecture:* `api: 2`, `import: 34`
* *Defense:* `safety: 96`, `doc: 4`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` ReactChildFiber, ReactFiberTransition, ReactFiberSuspenseComponent, ReactFiberLegacyContext, ReactFiberFlags, ReactFiberNewContext, ReactFiberCacheComponent, ReactTypeOfMode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-devtools-shared/src/backend/profilingHooks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.33 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.665 IQR)
- **Top Global Matches:** file_cluster_8: 11.33, file_cluster_13: 11.641, file_cluster_11: 11.702
- **Magnitude:** 1460.92 | **LOC:** 990 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (41.3147%), Tech Debt (16.3117%)
**Top Internal Functions/Classes:**
  * `recordReactMeasureCompleted` (Impact: 1330.3 | O(2^N) | DB: 21)
  * `recordReactMeasureStarted` (Impact: 23.2 | O(N^2) | DB: 6)
    * *Intent:* // $FlowFixMe[method-unbinding]
  * `get` (Impact: 1.9 | O(N^1))
  * `set` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 53`, `args: 35`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 90`, `dead_code: 1`, `planned_debt: 10`
* *Architecture:* `concurrency: 1`, `import: 7`
* *Defense:* `safety: 29`, `doc: 1`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` types, isArray, constants, ReactInternalTypes, types, DevToolsFiberComponentStack, ReactTypes
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.599 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.014 IQR)
- **Top Global Matches:** file_cluster_4: 11.599, file_cluster_2: 11.625, file_cluster_8: 11.658
- **Magnitude:** 1428.22 | **LOC:** 4231 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^4) | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (96.6045%), Tech Debt (37.7317%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 606.4 | O(N^4) | DB: 63)
  * `it` (Impact: 17.9 | O(N^3) | DB: 3)
  * `it` (Impact: 15.4 | O(N^2) | DB: 2)
  * `it` (Impact: 13.6 | O(N^3) | DB: 3)
  * `dispatchMouseEvent` (Impact: 11.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 412`, `args: 227`, `func_start: 356`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 78`, `state_mutation: 203`, `fragile_debt: 2`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 475`, `import: 10`
* *Defense:* `safety: 2`, `doc: 1`, `test: 199`, `immutability_locks: 173`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` scheduler, constants, server, ReactFeatureFlags, react-dom, react, internal-test-utils, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom-bindings/src/client/ReactDOMComponent.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.681 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.828 IQR)
- **Top Global Matches:** file_cluster_8: 11.681, file_cluster_13: 11.719, file_cluster_17: 11.913
- **Magnitude:** 1417.98 | **LOC:** 3380 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (38.7369%), Tech Debt (96.7272%)
**Top Internal Functions/Classes:**
  * `checkAttributeStringCoercion` (Impact: 390.4 | O(2^N))
  * `validateFormActionInDevelopment` (Impact: 215.6 | O(N^3))
  * `hydrateProperties` (Impact: 138.4 | O(N^2) | DB: 1)
    * *Intent:* // Mostly a port of Void Element logic with special casing to ensure srcset and src are set last
  * `setPropOnCustomElement` (Impact: 98.7 | O(N^3) | DB: 3)
  * `setProp` (Impact: 73.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 85`, `args: 20`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 1`, `state_mutation: 46`, `dead_code: 5`, `planned_debt: 15`, `fragile_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 1`, `import: 27`
* *Defense:* `safety: 102`, `doc: 1`, `immutability_locks: 61`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.196
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` setTextContent, ReactDOMInvalidARIAHook, ReactDOMSelect, DOMNamespaces, CheckStringCoercion, ReactFiberMutationTracking, ReactControlledValuePropTypes, getAttributeAlias...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberPerformanceTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.31 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.714 IQR)
- **Top Global Matches:** file_cluster_8: 10.31, file_cluster_7: 10.918, file_cluster_13: 10.98
- **Magnitude:** 1403.9 | **LOC:** 1721 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 56.2%
- **Algorithmic:** O(N^4) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (21.3648%), Tech Debt (9.739%)
**Top Internal Functions/Classes:**
  * `logComponentErrored` (Impact: 1057.0 | O(N^3) | DB: 13)
    * *Intent:* // $FlowFixMe[method-unbinding]
  * `logComponentRender` (Impact: 178.6 | O(N^4) | DB: 2)
  * `logComponentTrigger` (Impact: 19.8 | O(N^2))
  * `markAllLanesInOrder` (Impact: 10.3 | O(N^2))
  * `popDeepEquality` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 66`, `args: 29`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 51`, `planned_debt: 6`
* *Architecture:* `io: 1`, `api: 38`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 39`, `doc: 1`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.124
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ReactInternalTypes, ReactWorkTags, ReactFiberLane, ReactFeatureFlags, getComponentNameFromFiber, ReactPerformanceTrackProperties, ReactCapturedValue
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberClassComponent.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.883 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.062 IQR)
- **Top Global Matches:** file_cluster_8: 12.883, file_cluster_13: 12.907, file_cluster_0: 13.213
- **Magnitude:** 1386.3 | **LOC:** 1225 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (32.7895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructClassInstance` (Impact: 819.4 | O(2^N) | DB: 17)
  * `checkClassInstance` (Impact: 247.6 | O(N^3) | DB: 21)
  * `checkShouldComponentUpdate` (Impact: 68.5 | O(N^3) | DB: 1)
  * `getDerivedStateFromProps` (Impact: 43.2 | O(2^N) | DB: 1)
  * `enqueueReplaceState` (Impact: 19.3 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 59`, `args: 10`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 97`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 7`, `import: 21`
* *Defense:* `safety: 133`, `doc: 1`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` shallowEqual, ReactInstanceMap, ReactStrictModeWarnings, ReactFiberLegacyContext, ReactFiberFlags, ReactFiberNewContext, getComponentNameFromType, ReactFiberClassUpdateQueue...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactChildFiber.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.513 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.884 IQR)
- **Top Global Matches:** file_cluster_8: 11.513, file_cluster_13: 11.678, file_cluster_11: 11.914
- **Magnitude:** 1371.16 | **LOC:** 2253 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (22.8327%), Tech Debt (22.7977%)
**Top Internal Functions/Classes:**
  * `pushDebugInfo` (Impact: 1305.1 | O(2^N) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 76`, `args: 15`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 52`, `planned_debt: 11`, `fragile_debt: 2`
* *Architecture:* `import: 19`
* *Defense:* `safety: 74`, `doc: 1`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ReactInternalTypes, ReactTypeOfMode, isArray, ReactFiberHotReloading, ReactWorkTags, ReactFiberTreeContext, ReactFiberLane, ReactFiberThenable...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMHydrationDiff-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 10.448 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.65 IQR)
- **Top Global Matches:** file_cluster_2: 10.448, file_cluster_8: 10.578, file_cluster_0: 11.06
- **Magnitude:** 1361.08 | **LOC:** 1648 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (7.9137%), Tech Debt (44.1731%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 466.5 | O(2^N) | DB: 24)
  * `describe` (Impact: 300.8 | O(2^N) | DB: 24)
  * `describe` (Impact: 300.4 | O(2^N) | DB: 24)
  * `describe` (Impact: 148.5 | O(N^4) | DB: 18)
  * `describe` (Impact: 54.0 | O(N^4) | DB: 6)
    * *Intent:* // @gate __DEV__
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 99`, `args: 96`, `func_start: 131`
* *Risk/State:* `safety_bypasses: 71`, `high_risk_execution: 2`, `state_mutation: 6`, `planned_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `io: 35`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 72`, `doc: 1`, `test: 83`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` client, server, react, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactFiber.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.061 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.519 IQR)
- **Top Global Matches:** file_cluster_8: 11.061, file_cluster_13: 11.089, file_cluster_7: 11.631
- **Magnitude:** 1323.28 | **LOC:** 960 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (19.9944%), Tech Debt (12.827%)
**Top Internal Functions/Classes:**
  * `FiberNode` (Impact: 1241.0 | O(2^N) | DB: 30)
    * *Intent:* // eslint-disable-next-line no-new
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 71`, `args: 14`, `func_start: 15`
* *Risk/State:* `state_mutation: 57`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `import: 28`
* *Defense:* `safety: 26`, `doc: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` ReactFiberHotReloading, ReactElementType, ReactRootTags, ReactFiberFlags, getComponentNameFromType, isArray, ReactTypeOfMode, ReactFiberLane...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/react-dom-bindings/src/client/ReactInputSelection.js` (JAVASCRIPT) | Magnitude: 181.32 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, branch: 52, structural_boundaries: 31, safety: 21
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/labeled-break-within-label-switch.ts` (TYPESCRIPT) | Magnitude: 2.41 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 9, branch: 4, structural_boundaries: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/unlabeled-break-within-label-switch.ts` (TYPESCRIPT) | Magnitude: 2.41 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 9, branch: 4, structural_boundaries: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/labeled-break-within-label-loop.ts` (TYPESCRIPT) | Magnitude: 2.45 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 12, branch: 3, decorators: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/unlabeled-break-within-label-loop.ts` (TYPESCRIPT) | Magnitude: 2.45 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 12, branch: 3, decorators: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/react-native-renderer/src/__mocks__/react-native/Libraries/ReactPrivate/RawEventEmitter.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, api: 1, doc: 1, test: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/react-devtools-shared/src/backend/shared/DevToolsComponentStackFrame.js` (JAVASCRIPT) | Magnitude: 171.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, branch: 22, state_mutation: 12, structural_boundaries: 11
- `fixtures/legacy-jsx-runtimes/react-17/cjs/react-jsx-runtime.development.js` (JAVASCRIPT) | Magnitude: 0.76 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 355, state_mutation: 166, branch: 139, structural_boundaries: 116

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/shared/assign.js` (JAVASCRIPT) | Magnitude: 12.04 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, api: 1, doc: 1
- `packages/shared/hasOwnProperty.js` (JAVASCRIPT) | Magnitude: 12.04 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, api: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/react-devtools-shared/src/devtools/views/ErrorBoundary/UpdateExistingIssue.js` (JAVASCRIPT) | Magnitude: 3.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 6, ui_framework: 5, import: 4
- `packages/react-devtools-shared/src/devtools/views/utils.js` (JAVASCRIPT) | Magnitude: 109.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, branch: 39, structural_boundaries: 36, api: 11
- `packages/use-sync-external-store/src/__tests__/useSyncExternalStoreShimServer-test.js` (JAVASCRIPT) | Magnitude: 17.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 23, args: 15, func_start: 11
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/infer-component-props-non-null.tsx` (TYPESCRIPT) | Magnitude: 0.81 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, state_mutation: 3, ui_framework: 3
- `packages/react-dom/src/__tests__/ReactDOMserverIntegrationProgress-test.js` (JAVASCRIPT) | Magnitude: 11.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, func_start: 7, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/todo-optional-call-chain-in-optional.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, branch: 3, structural_boundaries: 3, safety: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/todo-optional-call-chain-in-optional.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, branch: 3, structural_boundaries: 3, safety: 3
- `compiler/packages/babel-plugin-react-compiler/src/Utils/Result.ts` (TYPESCRIPT) | Magnitude: 0.83 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, func_start: 3, api: 3
- `compiler/packages/snap/src/sprout/shared-runtime.ts` (TYPESCRIPT) | Magnitude: 28.43 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 189, structural_boundaries: 127, api: 94, func_start: 61
- `fixtures/flight-parcel/types.d.ts` (TYPESCRIPT) | Magnitude: 2.31 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, args: 12, indent_spaces: 12, api: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/optional-member-expression-inverted-optionals-parallel-paths.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 6, branch: 5, safety: 5
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/optional-member-expression-inverted-optionals-parallel-paths.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 6, branch: 5, safety: 5
- `packages/react-reconciler/src/ReactFiberTracingMarkerComponent.js` (JAVASCRIPT) | Magnitude: 116.04 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 26, state_mutation: 19, branch: 18
- `scripts/tasks/generate-changelog/summaries.js` (JAVASCRIPT) | Magnitude: 219.04 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 248, branch: 59, immutability_locks: 42, state_mutation: 41
- `packages/react-reconciler/src/ReactStrictModeWarnings.js` (JAVASCRIPT) | Magnitude: 137.58 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 37, branch: 31, state_mutation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-dont-memoize-array-with-capturing-map-after-hook.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, args: 4, ui_framework: 4
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-dont-memoize-array-with-mutable-map-after-hook.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, args: 4, ui_framework: 4
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-if-alternate.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, state_mutation: 3, branch: 2, structural_boundaries: 2
- `packages/react-devtools-shared/src/devtools/views/Profiler/useCommitFilteringAndNavigation.js` (JAVASCRIPT) | Magnitude: 119.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 153, structural_boundaries: 33, branch: 24, func_start: 18
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/valid-setState-in-useEffect-via-useEffectEvent-with-ref.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, immutability_locks: 12, ui_framework: 11, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/react-reconciler/src/__tests__/ReactIsomorphicAct-test.js` (JAVASCRIPT) | Magnitude: 81.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 65, concurrency: 41, func_start: 36
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/valid-setState-in-useEffect-listener.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, concurrency: 6, structural_boundaries: 4, ui_framework: 4
- `packages/react-reconciler/src/__tests__/ReactCPUSuspense-test.js` (JAVASCRIPT) | Magnitude: 126.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 44, func_start: 30, ui_framework: 30
- `packages/react/src/__tests__/ReactPureComponent-test.js` (JAVASCRIPT) | Magnitude: 28.06 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 19, concurrency: 14, func_start: 12
- `packages/react/src/__tests__/ReactStartTransition-test.js` (JAVASCRIPT) | Magnitude: 53.8 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 26, state_mutation: 20, concurrency: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/react/src/ReactContext.js` (JAVASCRIPT) | Magnitude: 16.44 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 4, safety: 2, import: 2
- `packages/react/src/BadMapPolyfill.js` (JAVASCRIPT) | Magnitude: 19.22 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, branch: 3, state_mutation: 3, structural_boundaries: 2
- `packages/react-devtools-fusebox/src/frontend.d.ts` (TYPESCRIPT) | Magnitude: 3.94 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 43, indent_spaces: 40, api: 19, args: 14
- `compiler/packages/babel-plugin-react-compiler/src/Utils/todo.ts` (TYPESCRIPT) | Magnitude: 0.87 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, safety: 3, planned_debt: 3, branch: 2
- `packages/react-native-renderer/src/NativeMethodsMixinUtils.js` (JAVASCRIPT) | Magnitude: 39.46 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, branch: 8, structural_boundaries: 6, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/eslint-plugin-react-hooks/src/code-path-analysis/code-path-segment.js` (JAVASCRIPT) | Magnitude: 105.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, doc: 48, state_mutation: 32, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/react-devtools-shared/src/devtools/views/Profiler/SnapshotCommitListItem.js` (JAVASCRIPT) | Magnitude: 12.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 12, branch: 8, immutability_locks: 7
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/error.invalid-mutate-props-via-for-of-iterator.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, state_mutation: 3, immutability_locks: 2, branch: 1
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-c906cace44e9.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: func_start: 2, indent_spaces: 2, branch: 1, structural_boundaries: 1
- `packages/react-devtools-shared/src/devtools/views/Components/ElementBadges.js` (JAVASCRIPT) | Magnitude: 3.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, branch: 12, structural_boundaries: 7, safety_bypasses: 5
- `packages/react-dom/src/server/ReactDOMFizzServerBrowser.js` (JAVASCRIPT) | Magnitude: 82.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, branch: 32, concurrency: 22, structural_boundaries: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scripts/react-compiler/link-compiler.sh` (SHELL) | Magnitude: 1.21 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 6, structural_boundaries: 4, state_mutation: 3, safety: 1
- `compiler/apps/playground/scripts/link-compiler.sh` (SHELL) | Magnitude: 0.89 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, branch: 4, state_mutation: 3, safety: 1
- `compiler/packages/babel-plugin-react-compiler/scripts/ts-analyze-trace.sh` (SHELL) | Magnitude: 0.67 | Delta: **0.44 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 3, safety: 2, safety_bypasses: 2, branch: 1
- `compiler/scripts/hash.sh` (SHELL) | Magnitude: 0.21 | Delta: **0.534 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: io: 6, structural_boundaries: 4, args: 2, safety_bypasses: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-client/src/ReactFlightClient.js` -> Churn: **82.76%** | Cog Load: 52.0896% | Debt: 49.4347%
- `packages/react-server/src/ReactFlightServer.js` -> Churn: **77.56%** | Cog Load: 52.9329% | Debt: 33.3869%
- `packages/react-reconciler/src/ReactFiberWorkLoop.js` -> Churn: **75.84%** | Cog Load: 23.1746% | Debt: 58.2608%
- `packages/react-devtools-shared/src/devtools/store.js` -> Churn: **75.81%** | Cog Load: 64.5306% | Debt: 99.2536%
- `packages/react-devtools-shared/src/__tests__/store-test.js` -> Churn: **75.05%** | Cog Load: 28.5695% | Debt: 64.5851%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `flow-typed/environments/node.js` -> **Jan Kassens** (100.0% isolated ownership) | Magnitude: 1622.96
- `packages/react-devtools-shared/src/backend/profilingHooks.js` -> **Jan Kassens** (100.0% isolated ownership) | Magnitude: 1460.92
- `packages/react-dom-bindings/src/client/ReactDOMComponent.js` -> **Sebastian Markbåge** (100.0% isolated ownership) | Magnitude: 1417.98
- `packages/react-reconciler/src/ReactFiberClassComponent.js` -> **Ruslan Lesiutin** (100.0% isolated ownership) | Magnitude: 1386.3
- `packages/react-dom/src/__tests__/ReactDOMHydrationDiff-test.js` -> **o-m12a** (100.0% isolated ownership) | Magnitude: 1361.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react-dom/src/client/ReactDOMRoot.js` -> **Severity: 0.036** (Bridge: 0.0004 * Flux: 92.8683%)
- `packages/react-devtools-shared/src/bridge.js` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 88.1396%)
- `packages/react-reconciler/src/ReactFiberWorkLoop.js` -> **Severity: 0.013** (Bridge: 0.0006 * Flux: 23.5186%)
- `packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js` -> **Severity: 0.012** (Bridge: 0.0003 * Flux: 44.4386%)
- `packages/react-reconciler/src/ReactFiberTracingMarkerComponent.js` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 92.4584%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `compiler/packages/snap/src/sprout/shared-runtime.ts` -> **Severity: 5176.9** (Blast Radius: 51.769 * Doc Risk: 100.0%)
- `packages/shared/ReactTypes.js` -> **Severity: 1359.2** (Blast Radius: 13.592 * Doc Risk: 100.0%)
- `compiler/packages/babel-plugin-react-compiler/src/HIR/HIR.ts` -> **Severity: 1088.6** (Blast Radius: 10.886 * Doc Risk: 100.0%)
- `packages/react-devtools-shared/src/frontend/types.js` -> **Severity: 401.1** (Blast Radius: 4.011 * Doc Risk: 100.0%)
- `packages/react-dom/src/client/ReactDOMClient.js` -> **Severity: 236.051** (Blast Radius: 10.171 * Doc Risk: 23.2082%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
