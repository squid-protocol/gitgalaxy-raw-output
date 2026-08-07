# ARCHITECTURAL_BRIEF: react
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/react` |
| **Timestamp** | `2026-08-07T04:27:33.211783+00:00` |
| **Scan Duration** | `13.71s` |
| **Git Branch** | `main` |
| **Git Commit** | `1b45e2439289fd8e094c44161c89e06c5488671e` |
| **Git Remote** | `https://github.com/facebook/react.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4128 malicious artifacts.

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
> **Architectural Drift Z-Score:** `3.686`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2709 | 43.2% |
| file_cluster_13 | 875 | 14.0% |
| file_cluster_2 | 578 | 9.2% |
| file_cluster_4 | 96 | 1.5% |
| file_cluster_17 | 58 | 0.9% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 17.8 | 5.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 32.7 | 33.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 35.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.7 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.6 | 4.1 | 4.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 49.2 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 32.3 | 4.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.7 | 12.0 | 11.9 |
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

- `initializeDebugChunk` (@ `packages/react-client/src/ReactFlightClient.js`) -> Impact: **927.6** | LOC: 2112
- `lowerStatement` (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **910.7** | LOC: 1578
- `commitSuspenseHydrationCallbacks` (@ `packages/react-reconciler/src/ReactFiberCommitWork.js`) -> Impact: **897.0** | LOC: 1741
- `applyEffect` (@ `compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts`) -> Impact: **740.3** | LOC: 844
- `throwTaintViolation` (@ `packages/react-server/src/ReactFlightServer.js`) -> Impact: **642.7** | LOC: 1562
- `computeEffectsForLegacySignature` (@ `compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts`) -> Impact: **615.3** | LOC: 539
- `markRef` (@ `packages/react-reconciler/src/ReactFiberBeginWork.js`) -> Impact: **612.6** | LOC: 1181
- `lowerExpression` (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **595.5** | LOC: 1189
- `updateHostHoistable` (@ `packages/react-reconciler/src/ReactFiberBeginWork.js`) -> Impact: **564.7** | LOC: 1186
- `insertNewOutlinedFunctionNode` (@ `compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Program.ts`) -> Impact: **563.9** | LOC: 857

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/react-dom/src/__tests__` | 129 | 37480.08 | 47.98% | 96.06% |
| `packages/react-reconciler/src` | 81 | 27975.26 | 18.96% | 61.0% |
| `packages/react-reconciler/src/__tests__` | 76 | 20266.52 | 60.94% | 99.74% |
| `packages/react-devtools-shared/src/__tests__` | 34 | 8924.74 | 22.4% | 93.59% |
| `packages/react-server/src` | 37 | 8860.7 | 24.23% | 36.7% |
| `packages/react/src/__tests__` | 26 | 5475.88 | 45.1% | 95.83% |
| `packages/react-client/src` | 14 | 5072.32 | 25.72% | 41.96% |
| `fixtures/fiber-debugger` | 3 | 5000.0 | 0.0% | 0.0% |
| `fixtures/nesting` | 3 | 5000.0 | 0.0% | 0.0% |
| `packages/react-server-dom-webpack/src/__tests__` | 7 | 4039.26 | 77.18% | 99.98% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `babel.config-react-compiler.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/e2e/constant-prop.e2e.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-capture-in-method-receiver.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-computed-load.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allocating-primitive-as-dep.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-capture-in-method-receiver.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/alias-while.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/capturing-function-conditional-capture-mutate.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/conditional-break-labeled.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/conditional-early-return.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` -> **3** Orphaned Functions | **300** Duplicates
- `packages/react-refresh/src/__tests__/ReactFresh-test.js` -> **5** Orphaned Functions | **274** Duplicates
- `packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMBrowser-test.js` -> **2** Orphaned Functions | **258** Duplicates
- `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` -> **5** Orphaned Functions | **245** Duplicates
- `packages/react-devtools-shared/src/__tests__/store-test.js` -> **3** Orphaned Functions | **244** Duplicates

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
306. **`scripts/ci/check_license.sh`** -> AI Confidence: **99.29%**
307. **`scripts/react-compiler/build-compiler.sh`** -> AI Confidence: **99.29%**
308. **`packages/react-devtools-extensions/src/main/index.js`** -> AI Confidence: **99.24%**
309. **`packages/react-devtools-shared/src/devtools/ProfilerStore.js`** -> AI Confidence: **99.24%**
310. **`packages/react-devtools-shared/src/devtools/views/Components/NewArrayValue.js`** -> AI Confidence: **99.24%**
311. **`packages/react-devtools-shared/src/devtools/views/Components/OwnersStack.js`** -> AI Confidence: **99.24%**
312. **`packages/react-devtools-shared/src/devtools/views/Profiler/HoveredFiberInfo.js`** -> AI Confidence: **99.24%**
313. **`packages/react-devtools-shared/src/devtools/views/Settings/GeneralSettings.js`** -> AI Confidence: **99.24%**
314. **`packages/react-devtools-shared/src/devtools/views/Settings/SettingsContext.js`** -> AI Confidence: **99.24%**
315. **`packages/react-devtools-shared/src/devtools/views/SuspenseTab/SuspenseBreadcrumbs.js`** -> AI Confidence: **99.24%**
316. **`packages/react-devtools-shared/src/hookNamesCache.js`** -> AI Confidence: **99.24%**
317. **`packages/react-dom-bindings/src/client/ReactDOMEventHandle.js`** -> AI Confidence: **99.24%**
318. **`packages/react-dom-bindings/src/events/plugins/BeforeInputEventPlugin.js`** -> AI Confidence: **99.24%**
319. **`packages/react-dom-bindings/src/events/plugins/FormActionEventPlugin.js`** -> AI Confidence: **99.24%**
320. **`packages/react-dom-bindings/src/events/plugins/SelectEventPlugin.js`** -> AI Confidence: **99.24%**
321. **`packages/react-dom-bindings/src/server/ReactFizzConfigDOM.js`** -> AI Confidence: **99.24%**
322. **`packages/react-native-renderer/src/ReactFabric.js`** -> AI Confidence: **99.24%**
323. **`packages/react-reconciler/src/ReactFiberRootScheduler.js`** -> AI Confidence: **99.24%**
324. **`packages/react-server/src/ReactFizzHooks.js`** -> AI Confidence: **99.24%**
325. **`scripts/devtools/prepare-release.js`** -> AI Confidence: **99.24%**
326. **`scripts/jest/setupTests.js`** -> AI Confidence: **99.24%**
327. **`compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Pipeline.ts`** -> AI Confidence: **99.24%**
328. **`compiler/packages/snap/src/sprout/evaluator.ts`** -> AI Confidence: **99.24%**
329. **`compiler/scripts/enable-feature-flag.js`** -> AI Confidence: **99.23%**
330. **`packages/react-devtools-shared/src/devtools/views/Profiler/CommitTreeBuilder.js`** -> AI Confidence: **99.23%**
331. **`packages/react-devtools-shared/src/devtools/views/SuspenseTab/SuspenseScrubber.js`** -> AI Confidence: **99.23%**
332. **`packages/react-server-dom-turbopack/src/client/ReactFlightDOMClientNode.js`** -> AI Confidence: **99.23%**
333. **`packages/react-server-dom-unbundled/src/client/ReactFlightDOMClientNode.js`** -> AI Confidence: **99.23%**
334. **`packages/react-server-dom-webpack/src/client/ReactFlightDOMClientNode.js`** -> AI Confidence: **99.23%**
335. **`packages/shared/ReactPerformanceTrackProperties.js`** -> AI Confidence: **99.23%**
336. **`scripts/devtools/publish-release.js`** -> AI Confidence: **99.23%**
337. **`scripts/devtools/utils.js`** -> AI Confidence: **99.23%**
338. **`compiler/packages/babel-plugin-react-compiler/src/HIR/FindContextIdentifiers.ts`** -> AI Confidence: **99.23%**
339. **`compiler/packages/babel-plugin-react-compiler/src/Optimization/ConstantPropagation.ts`** -> AI Confidence: **99.23%**
340. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoFreezingKnownMutableFunctions.ts`** -> AI Confidence: **99.23%**
341. **`compiler/packages/snap/src/reporter.ts`** -> AI Confidence: **99.23%**
342. **`packages/eslint-plugin-react-hooks/src/shared/RunReactCompiler.ts`** -> AI Confidence: **99.23%**
343. **`fixtures/ssr/server/index.js`** -> AI Confidence: **99.22%**
344. **`packages/react-dom-bindings/src/client/CSSPropertyOperations.js`** -> AI Confidence: **99.22%**
345. **`packages/react-reconciler/src/ReactFiberComponentStack.js`** -> AI Confidence: **99.22%**
346. **`compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateContextVariableLValues.ts`** -> AI Confidence: **99.22%**
347. **`fixtures/devtools/scheduling-profiler/run.js`** -> AI Confidence: **99.2%**
348. **`fixtures/fizz/scripts/build.js`** -> AI Confidence: **99.2%**
349. **`fixtures/ssr2/scripts/build.js`** -> AI Confidence: **99.2%**
350. **`packages/react-dom-bindings/src/server/ReactDOMFlightServerHostDispatcher.js`** -> AI Confidence: **99.2%**
351. **`packages/react-dom-bindings/src/server/ReactFlightServerConfigDOM.js`** -> AI Confidence: **99.2%**
352. **`scripts/error-codes/extract-errors.js`** -> AI Confidence: **99.2%**
353. **`compiler/packages/babel-plugin-react-compiler/src/Optimization/DeadCodeElimination.ts`** -> AI Confidence: **99.2%**
354. **`fixtures/dom/src/components/fixtures/input-change-events/index.js`** -> AI Confidence: **99.18%**
355. **`fixtures/flight-ssr-bench/bench.js`** -> AI Confidence: **99.18%**
356. **`packages/react-client/src/__tests__/ReactFlight-test.js`** -> AI Confidence: **99.18%**
357. **`packages/react-devtools-shared/src/backend/types.js`** -> AI Confidence: **99.18%**
358. **`packages/react-devtools-shared/src/backendAPI.js`** -> AI Confidence: **99.18%**
359. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementContext.js`** -> AI Confidence: **99.18%**
360. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementContextTree.js`** -> AI Confidence: **99.18%**
361. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementSourcePanel.js`** -> AI Confidence: **99.18%**
362. **`packages/react-devtools-shared/src/devtools/views/Components/InspectedElementStateTree.js`** -> AI Confidence: **99.18%**
363. **`packages/react-devtools-shared/src/devtools/views/Components/KeyValueContextMenuContainer.js`** -> AI Confidence: **99.18%**
364. **`packages/react-devtools-shared/src/devtools/views/Components/NativeStyleEditor/StyleEditor.js`** -> AI Confidence: **99.18%**
365. **`packages/react-devtools-shared/src/devtools/views/Components/NativeStyleEditor/index.js`** -> AI Confidence: **99.18%**
366. **`packages/react-devtools-shared/src/devtools/views/Components/OwnersListContext.js`** -> AI Confidence: **99.18%**
367. **`packages/react-devtools-shared/src/devtools/views/Editor/EditorPane.js`** -> AI Confidence: **99.18%**
368. **`packages/react-devtools-shared/src/devtools/views/Profiler/ProfilingImportExportButtons.js`** -> AI Confidence: **99.18%**
369. **`packages/react-devtools-shared/src/devtools/views/Profiler/SidebarEventInfo.js`** -> AI Confidence: **99.18%**
370. **`packages/react-devtools-shared/src/devtools/views/UnsupportedBridgeProtocolDialog.js`** -> AI Confidence: **99.18%**
371. **`packages/react-devtools-shared/src/inspectedElementCache.js`** -> AI Confidence: **99.18%**
372. **`packages/react-devtools-timeline/src/content-views/FlamechartView.js`** -> AI Confidence: **99.18%**
373. **`packages/react-dom-bindings/src/events/plugins/ScrollEndEventPlugin.js`** -> AI Confidence: **99.18%**
374. **`packages/react-dom-bindings/src/events/plugins/SimpleEventPlugin.js`** -> AI Confidence: **99.18%**
375. **`packages/react-dom/src/__tests__/ReactClassComponentPropResolutionFizz-test.js`** -> AI Confidence: **99.18%**
376. **`packages/react-dom/src/__tests__/ReactDOMFizzShellHydration-test.js`** -> AI Confidence: **99.18%**
377. **`packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js`** -> AI Confidence: **99.18%**
378. **`packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js`** -> AI Confidence: **99.18%**
379. **`packages/react-dom/src/__tests__/ReactDOMServerSelectiveHydrationActivity-test.internal.js`** -> AI Confidence: **99.18%**
380. **`packages/react-native-renderer/src/ReactFabricEventEmitter.js`** -> AI Confidence: **99.18%**
381. **`packages/react-reconciler/src/ReactFiberThenable.js`** -> AI Confidence: **99.18%**
382. **`packages/react-reconciler/src/__tests__/ReactSuspenseFuzz-test.internal.js`** -> AI Confidence: **99.18%**
383. **`packages/react-refresh/src/__tests__/ReactFreshIntegration-test.js`** -> AI Confidence: **99.18%**
384. **`packages/react-refresh/src/__tests__/ReactFreshMultipleRenderer-test.internal.js`** -> AI Confidence: **99.18%**
385. **`packages/react-server-dom-turbopack/src/__tests__/ReactFlightTurbopackDOMEdge-test.js`** -> AI Confidence: **99.18%**
386. **`packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMNode-test.js`** -> AI Confidence: **99.18%**
387. **`packages/react-server/src/__tests__/ReactFlightAsyncDebugInfo-test.js`** -> AI Confidence: **99.18%**
388. **`packages/react-server/src/__tests__/ReactFlightServer-test.js`** -> AI Confidence: **99.18%**
389. **`packages/react-server/src/forks/ReactFlightServerConfig.dom-edge-parcel.js`** -> AI Confidence: **99.18%**
390. **`packages/react-server/src/forks/ReactFlightServerConfig.dom-edge-turbopack.js`** -> AI Confidence: **99.18%**
391. **`packages/react-server/src/forks/ReactFlightServerConfig.dom-edge.js`** -> AI Confidence: **99.18%**
392. **`packages/react/src/__tests__/ReactMismatchedVersions-test.js`** -> AI Confidence: **99.18%**
393. **`scripts/devtools/build-and-test.js`** -> AI Confidence: **99.18%**
394. **`compiler/apps/playground/components/Editor/Input.tsx`** -> AI Confidence: **99.18%**
395. **`compiler/packages/snap/src/compiler.ts`** -> AI Confidence: **99.18%**
396. **`fixtures/flight-parcel/src/server.tsx`** -> AI Confidence: **99.18%**
397. **`compiler/packages/babel-plugin-react-compiler/scripts/eslint-plugin-react-hooks-test-cases.js`** -> AI Confidence: **99.17%**
398. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/debugger.js`** -> AI Confidence: **99.17%**
399. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/dominator.js`** -> AI Confidence: **99.17%**
400. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/mutable-lifetime-with-aliasing.js`** -> AI Confidence: **99.17%**
401. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/optional-call-chained.js`** -> AI Confidence: **99.17%**
402. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/optional-member-expression-with-optional-member-expr-as-property.js`** -> AI Confidence: **99.17%**
403. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/switch-non-final-default.js`** -> AI Confidence: **99.17%**
404. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-memoize-for-of-collection-when-loop-body-returns.js`** -> AI Confidence: **99.17%**
405. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-optional-methodcall.js`** -> AI Confidence: **99.17%**
406. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-optional-property.js`** -> AI Confidence: **99.17%**
407. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-optionalcall.js`** -> AI Confidence: **99.17%**
408. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/ssa-sibling-phis.js`** -> AI Confidence: **99.17%**
409. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/switch-non-final-default.js`** -> AI Confidence: **99.17%**
410. **`compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/unused-logical-assigned-to-variable.js`** -> AI Confidence: **99.17%**
411. **`fixtures/dom/src/components/fixtures/fragment-refs/CompareDocumentPositionFragmentContainer.js`** -> AI Confidence: **99.17%**
412. **`fixtures/owner-stacks/src/App.js`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `scripts/tasks/danger.js` -> **100.0%** Exposure
- `compiler/packages/react-mcp-server/src/utils/algolia.ts` -> **99.9946%** Exposure
- `packages/react-client/src/__tests__/ReactFlight-test.js` -> **68.6348%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5787` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `fixtures/flight-parcel/src/actions.ts` (TYPESCRIPT) -> Cumulative Risk: **705.41**
- **Archetype:** `file_cluster_4` (Distance: 13.004 IQR)
- **Magnitude:** 19.76 | **LOC:** 76 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `createTodo` (Impact: 10.8), `updateTodo` (Impact: 9.4), `getTodos` (Impact: 5.6)

### 2. `fixtures/concurrent/time-slicing/src/index.js` (JAVASCRIPT) -> Cumulative Risk: **681.31**
- **Archetype:** `file_cluster_17` (Distance: 12.934 IQR)
- **Magnitude:** 0.16 | **LOC:** 147 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9307%), Tech Debt (98.6169%)
- **Heaviest Functions:** `handleChange` (Impact: 18.3), `handleChartClick` (Impact: 9.9), `getStreamData` (Impact: 6.6)

### 3. `packages/scheduler/src/forks/Scheduler.js` (JAVASCRIPT) -> Cumulative Risk: **681.04**
- **Archetype:** `file_cluster_8` (Distance: 12.658 IQR)
- **Magnitude:** 781.18 | **LOC:** 599 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.8007%), Concurrency (95.7324%)
- **Heaviest Functions:** `workLoop` (Impact: 175.4), `advanceTimers` (Impact: 153.9), `pop` (Impact: 128.9)

### 4. `packages/react-server-dom-unbundled/src/ReactFlightUnbundledNodeLoader.js` (JAVASCRIPT) -> Cumulative Risk: **669.42**
- **Archetype:** `file_cluster_8` (Distance: 11.441 IQR)
- **Magnitude:** 671.24 | **LOC:** 805 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.6089%), Tech Debt (99.5197%), State Flux (97.2385%)
- **Heaviest Functions:** `transformServerModule` (Impact: 240.4), `parseExportNamesInto` (Impact: 59.4), `transformModuleIfNeeded` (Impact: 47.5)

### 5. `packages/react-dom/src/__tests__/ReactCompositeComponentState-test.js` (JAVASCRIPT) -> Cumulative Risk: **667.19**
- **Archetype:** `file_cluster_8` (Distance: 11.668 IQR)
- **Magnitude:** 419.72 | **LOC:** 612 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.998%), State Flux (99.9959%)
- **Heaviest Functions:** `describe` (Impact: 19.0), `beforeEach` (Impact: 11.3), `it` (Impact: 6.4)

### 6. `packages/react-server-dom-turbopack/src/__tests__/ReactFlightTurbopackDOMEdge-test.js` (JAVASCRIPT) -> Cumulative Risk: **659.69**
- **Archetype:** `file_cluster_13` (Distance: 10.955 IQR)
- **Magnitude:** 92.46 | **LOC:** 335 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9995%), Tech Debt (99.708%), State Flux (93.0332%)
- **Heaviest Functions:** `describe` (Impact: 21.5), `createDelayedStream` (Impact: 7.9), `start` (Impact: 7.6)

### 7. `flow-typed/environments/serviceworkers.js` (JAVASCRIPT) -> Cumulative Risk: **659.44**
- **Archetype:** `file_cluster_2` (Distance: 10.13 IQR)
- **Magnitude:** 122.98 | **LOC:** 249 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (99.6272%), State Flux (88.4293%)
- **Heaviest Functions:** `startMessages` (Impact: 5.8), `unregister` (Impact: 5.7), `respondWith` (Impact: 5.5)

### 8. `packages/react-devtools-shared/src/backend/agent.js` (JAVASCRIPT) -> Cumulative Risk: **655.06**
- **Archetype:** `file_cluster_13` (Distance: 12.869 IQR)
- **Magnitude:** 320.78 | **LOC:** 1211 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9997%), Safety Score (89.3219%)
- **Heaviest Functions:** `void` (Impact: 31.5), `any` (Impact: 7.8), `registerRendererInterface` (Impact: 6.8)

### 9. `packages/react-reconciler/src/__tests__/ReactUpdatePriority-test.js` (JAVASCRIPT) -> Cumulative Risk: **646.2**
- **Archetype:** `file_cluster_2` (Distance: 10.792 IQR)
- **Magnitude:** 118.64 | **LOC:** 157 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (97.538%)
- **Heaviest Functions:** `describe` (Impact: 15.7), `it` (Impact: 7.6), `it` (Impact: 5.6)

### 10. `fixtures/dom/public/renderer.js` (JAVASCRIPT) -> Cumulative Risk: **646.01**
- **Archetype:** `file_cluster_4` (Distance: 11.059 IQR)
- **Magnitude:** 0.17 | **LOC:** 202 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9998%), State Flux (97.9443%)
- **Heaviest Functions:** `render` (Impact: 15.1), `loadScript` (Impact: 11.6), `prerender` (Impact: 10.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/react-reconciler/src/ReactFiberCommitWork.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.867 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.239 IQR)
- **Top Global Matches:** file_cluster_8: 11.867, file_cluster_13: 12.246, file_cluster_7: 12.411
- **Magnitude:** 5204.12 | **LOC:** 5350 | **CtrlFlow:** 83.4% | **Authorship Centralization:** 31.2%
- **Risk Profile:** Cognitive Load (24.3969%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `commitSuspenseHydrationCallbacks` (Impact: 897.0)
  * `commitBeforeMutationEffects_begin` (Impact: 527.0)
    * *Intent:* // Used during the commit phase to track the state of the Offscreen component stack.
  * `commitHostHydratedSuspense` (Impact: 315.6)
    * *Intent:* // Cut off the return pointer to disconnect it from the tree. // This enables us to detect and warn ...
  * `recursivelyTraverseReconnectPassiveEffec` (Impact: 311.6)
  * `accumulateSuspenseyCommitOnFiber` (Impact: 302.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 128`, `args: 48`, `func_start: 281`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 97`, `dead_code: 1`, `planned_debt: 39`, `fragile_debt: 5`, `duplicate_logic: 121`
* *Architecture:* `api: 28`, `concurrency: 1`, `import: 39`
* *Defense:* `safety: 169`, `doc: 1`, `immutability_locks: 183`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` ReactFiberDuplicateViewTransitions, ReactFiberWorkLoop, ReactStartTransition, ReactInternalTypes, ReactFiberCommitEffects, ReactTypes, ReactFeatureFlags, ReactFiberLane...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fixtures/fiber-debugger/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `packages/react-client/src/ReactFlightClient.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.013 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.111 IQR)
- **Top Global Matches:** file_cluster_8: 13.013, file_cluster_13: 13.168, file_cluster_11: 13.237
- **Magnitude:** 4136.46 | **LOC:** 5407 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 44.1%
- **Risk Profile:** Cognitive Load (49.044%), Tech Debt (99.9975%)
**Top Internal Functions/Classes:**
  * `initializeDebugChunk` (Impact: 927.6)
  * `waitForReference` (Impact: 510.8)
  * `flushComponentPerformance` (Impact: 290.3)
  * `map` (Impact: 180.1)
  * `processFullStringRow` (Impact: 146.9)
    * *Intent:* // $FlowFixMe[invalid-constructor]: the shapes are exact here but Flow doesn't like constructors
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 561`, `structural_boundaries: 232`, `args: 97`, `func_start: 179`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 305`, `dead_code: 5`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 78`
* *Architecture:* `io: 12`, `api: 28`, `concurrency: 28`, `import: 22`
* *Defense:* `safety: 189`, `doc: 1`, `test: 1`, `immutability_locks: 210`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ReactVersion, ReactFlightServerConfig, ReactTypes, ReactFeatureFlags, react, ReactFlightClientDevToolsHook, ReactSharedInternalsServer, ReactFlightClientConfig...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/react-server/src/ReactFlightServer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.633 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.136 IQR)
- **Top Global Matches:** file_cluster_8: 13.633, file_cluster_13: 13.774, file_cluster_17: 13.779
- **Magnitude:** 4108.08 | **LOC:** 6445 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 40.7%
- **Risk Profile:** Cognitive Load (52.2587%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `throwTaintViolation` (Impact: 642.7)
  * `serializeIONode` (Impact: 516.3)
  * `serializeEval` (Impact: 442.3)
  * `renderElement` (Impact: 145.3)
  * `createTask` (Impact: 127.6)
    * *Intent:* // We don't have a chunk to assign debug info. We need to outline this
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 691`, `structural_boundaries: 356`, `args: 134`, `func_start: 299`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 374`, `dead_code: 2`, `planned_debt: 22`, `fragile_debt: 14`, `duplicate_logic: 107`
* *Architecture:* `io: 1`, `api: 41`, `concurrency: 58`, `import: 29`
* *Defense:* `safety: 399`, `doc: 1`, `test: 1`, `immutability_locks: 284`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.126
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` ReactFeatureFlags, ReactTypes, noop, ReactFlightHooks, ReactFlightAsyncDispatcher, ReactSerializationErrors, getPrototypeOf, ReactComponentInfoStack...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.601 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.787 IQR)
- **Top Global Matches:** file_cluster_8: 11.601, file_cluster_2: 11.751, file_cluster_4: 11.791
- **Magnitude:** 3227.76 | **LOC:** 9605 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (76.4058%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 206.3)
  * `act` (Impact: 182.4)
  * `it` (Impact: 143.4)
  * `it` (Impact: 35.8)
  * `it` (Impact: 26.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 1045`, `args: 695`, `func_start: 970`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 30`, `state_mutation: 273`, `planned_debt: 6`, `fragile_debt: 5`, `duplicate_logic: 300`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `concurrency: 1126`, `import: 12`
* *Defense:* `safety: 32`, `doc: 1`, `test: 469`, `immutability_locks: 313`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` jsdom, immutable, internal-test-utils, with-selector, react-dom, client, server, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/bench/benchmarks/pe-class-components/benchmark.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.368 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.79 IQR)
- **Top Global Matches:** file_cluster_8: 13.368, file_cluster_2: 13.439, file_cluster_17: 13.519
- **Magnitude:** 2939.1 | **LOC:** 5586 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.9001%), Tech Debt (99.9863%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 72.4)
  * `render` (Impact: 67.9)
  * `render` (Impact: 58.2)
  * `render` (Impact: 55.2)
  * `render` (Impact: 52.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 501`, `structural_boundaries: 867`, `args: 280`, `func_start: 248`, `class_start: 183`
* *Risk/State:* `state_mutation: 1497`, `duplicate_logic: 246`
* *Architecture:* `api: 2`
* *Defense:* `safety: 498`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-devtools-shared/src/backend/fiber/renderer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.728 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.893 IQR)
- **Top Global Matches:** file_cluster_8: 13.728, file_cluster_17: 13.882, file_cluster_13: 13.902
- **Magnitude:** 2859.78 | **LOC:** 8154 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 52.5%
- **Risk Profile:** Cognitive Load (48.3691%), Tech Debt (99.7923%)
**Top Internal Functions/Classes:**
  * `recordVirtualDisconnect` (Impact: 238.7)
    * *Intent:* // TODO: Consider using a WeakMap instead. The only thing where that doesn't work // is React Native...
  * `mountVirtualChildrenRecursively` (Impact: 169.9)
  * `getSuspendedByRange` (Impact: 167.9)
  * `updateVirtualChildrenRecursively` (Impact: 143.6)
  * `overrideSuspense` (Impact: 127.8)
    * *Intent:* // Next, we'll pop back out of the SuspenseNode that we added above and now we'll
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 670`, `structural_boundaries: 285`, `args: 87`, `func_start: 214`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 374`, `dead_code: 3`, `planned_debt: 11`, `fragile_debt: 7`, `duplicate_logic: 60`
* *Architecture:* `io: 9`, `api: 24`, `concurrency: 16`, `import: 30`
* *Defense:* `safety: 366`, `doc: 2`, `test: 2`, `immutability_locks: 244`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` DevToolsFiberComponentStack, DevToolsFiberInternalReactConstants, react-devtools-feature-flags, DevToolsFiberSuspense, DevToolsOwnerStack, ReactTypes, ReactDebugHooks, react-debug-tools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/bench/benchmarks/pe-no-components/benchmark.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.492 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.024 IQR)
- **Top Global Matches:** file_cluster_8: 12.492, file_cluster_7: 13.098, file_cluster_11: 13.109
- **Magnitude:** 2678.86 | **LOC:** 4944 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1242%), Tech Debt (99.9971%)
**Top Internal Functions/Classes:**
  * `TransitionCell142` (Impact: 82.5)
  * `FixedDataTableCell143` (Impact: 75.6)
  * `ReactImage0` (Impact: 68.7)
  * `AbstractButton3` (Impact: 63.5)
  * `AdsPETableHeader141` (Impact: 61.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 501`, `structural_boundaries: 682`, `args: 280`, `func_start: 540`
* *Risk/State:* `state_mutation: 552`, `duplicate_logic: 246`
* *Architecture:* `api: 28`
* *Defense:* `safety: 498`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactFiberBeginWork.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.306 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.675 IQR)
- **Top Global Matches:** file_cluster_8: 11.306, file_cluster_13: 11.49, file_cluster_7: 11.881
- **Magnitude:** 2553.08 | **LOC:** 4449 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (18.0598%), Tech Debt (67.3622%)
**Top Internal Functions/Classes:**
  * `markRef` (Impact: 612.6)
  * `updateHostHoistable` (Impact: 564.7)
  * `updateSuspenseOffscreenState` (Impact: 420.8)
    * *Intent:* // Something suspended inside a hidden tree
  * `updateDehydratedSuspenseComponent` (Impact: 259.0)
  * `validateRevealOrder` (Impact: 58.8)
    * *Intent:* // We called retryActivityComponentWithoutHydrating and tried client rendering // but now we suspend...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 140`, `args: 22`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 54`, `planned_debt: 5`, `fragile_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 13`, `import: 54`
* *Defense:* `safety: 80`, `doc: 1`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` ReactFiberTransition, ReactFiberHotReloading, ReactCapturedValue, ReactFiberWorkLoop, ReactInternalTypes, ReactFiberSuspenseContext, getComponentNameFromFiber, ReactTypes...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.344 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.868 IQR)
- **Top Global Matches:** file_cluster_8: 10.344, file_cluster_2: 10.908, file_cluster_7: 11.006
- **Magnitude:** 2530.84 | **LOC:** 9641 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (20.6548%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 76.4)
  * `describe` (Impact: 70.5)
  * `it` (Impact: 63.1)
  * `describe` (Impact: 53.4)
  * `act` (Impact: 44.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 601`, `args: 343`, `func_start: 557`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 8`, `state_mutation: 72`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 245`, `orphaned_logic: 5`
* *Architecture:* `io: 22`, `concurrency: 470`, `import: 9`
* *Defense:* `safety: 20`, `doc: 4`, `test: 298`, `immutability_locks: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jsdom, internal-test-utils, react-dom, client, server, react, unstable_mock, stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactFiberWorkLoop.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.568 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.114 IQR)
- **Top Global Matches:** file_cluster_8: 12.568, file_cluster_13: 12.648, file_cluster_11: 12.886
- **Magnitude:** 2299.68 | **LOC:** 5622 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 68.0%
- **Risk Profile:** Cognitive Load (22.6388%), Tech Debt (99.992%)
**Top Internal Functions/Classes:**
  * `performWorkOnRoot` (Impact: 377.6)
  * `unwindUnitOfWork` (Impact: 201.6)
  * `isRenderConsistentWithExternalStores` (Impact: 194.3)
    * *Intent:* // Check if the work loop is currently suspended and waiting for data to
  * `finishConcurrentRender` (Impact: 65.3)
  * `resetWorkInProgressStack` (Impact: 64.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 445`, `structural_boundaries: 196`, `args: 69`, `func_start: 241`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 120`, `dead_code: 4`, `planned_debt: 29`, `fragile_debt: 7`, `duplicate_logic: 58`
* *Architecture:* `api: 69`, `import: 65`
* *Defense:* `safety: 168`, `doc: 3`, `immutability_locks: 122`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.699
  * `Choke Point (Betweenness):` 0.000563 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` ReactFiberTransition, ReactCapturedValue, ReactStartTransition, ReactInternalTypes, ReactFiberSuspenseContext, ReactRootTags, getComponentNameFromFiber, ReactTypes...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `scripts/bench/benchmarks/pe-functional-components/benchmark.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.531 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.366 IQR)
- **Top Global Matches:** file_cluster_8: 12.531, file_cluster_2: 12.631, file_cluster_17: 12.817
- **Magnitude:** 2240.28 | **LOC:** 5180 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.2794%), Tech Debt (64.8793%)
**Top Internal Functions/Classes:**
  * `TransitionCell142` (Impact: 82.5)
  * `FixedDataTableCell143` (Impact: 75.6)
  * `ReactImage0` (Impact: 68.7)
  * `AbstractButton3` (Impact: 63.5)
  * `AdsPETableHeader141` (Impact: 61.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 501`, `structural_boundaries: 684`, `args: 280`, `func_start: 248`
* *Risk/State:* `state_mutation: 552`, `duplicate_logic: 62`
* *Architecture:* `api: 33`
* *Defense:* `safety: 498`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `flow-typed/environments/node.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.336 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.11 IQR)
- **Top Global Matches:** file_cluster_8: 11.336, file_cluster_7: 11.764, file_cluster_2: 11.831
- **Magnitude:** 2088.56 | **LOC:** 4287 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.1232%), Tech Debt (99.7926%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 354.3)
  * `writeProcessing` (Impact: 57.9)
  * `setTimeout` (Impact: 57.8)
  * `createUnzip` (Impact: 55.5)
  * `callback` (Impact: 54.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1019`, `structural_boundaries: 614`, `args: 482`, `func_start: 967`
* *Risk/State:* `safety_bypasses: 576`, `high_risk_execution: 2`, `state_mutation: 234`, `dead_code: 2`, `planned_debt: 7`, `duplicate_logic: 61`, `orphaned_logic: 60`
* *Architecture:* `io: 186`, `api: 17`, `concurrency: 89`
* *Defense:* `safety: 22`, `doc: 47`, `test: 5`, `immutability_locks: 5`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.652
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `packages/react-server/src/ReactFizzServer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.759 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.932 IQR)
- **Top Global Matches:** file_cluster_8: 12.759, file_cluster_13: 12.915, file_cluster_17: 12.998
- **Magnitude:** 2014.24 | **LOC:** 6256 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 52.9%
- **Risk Profile:** Cognitive Load (17.1527%), Tech Debt (99.9898%)
**Top Internal Functions/Classes:**
  * `erroredReplay` (Impact: 198.7)
    * *Intent:* // We finished rendering this node, so now we can consume this
  * `retryRenderTask` (Impact: 100.4)
  * `fatalError` (Impact: 83.9)
  * `getThrownInfo` (Impact: 62.9)
  * `startWork` (Impact: 56.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 358`, `structural_boundaries: 189`, `args: 95`, `func_start: 206`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 226`, `dead_code: 4`, `planned_debt: 6`, `fragile_debt: 16`, `duplicate_logic: 62`
* *Architecture:* `api: 52`, `import: 30`
* *Defense:* `safety: 225`, `doc: 1`, `immutability_locks: 173`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` ReactFizzCallUserSpace, ReactTypes, ReactFeatureFlags, ReactFizzViewTransitionComponent, noop, ReactFizzConfig, ReactFizzLegacyContext, ReactFizzAsyncDispatcher...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMBrowser-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.093 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.187 IQR)
- **Top Global Matches:** file_cluster_4: 11.093, file_cluster_8: 11.313, file_cluster_2: 11.409
- **Magnitude:** 1901.76 | **LOC:** 3141 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 54.5%
- **Risk Profile:** Cognitive Load (94.8485%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 193.0)
  * `it` (Impact: 105.4)
  * `it` (Impact: 23.3)
  * `it` (Impact: 19.4)
  * `it` (Impact: 19.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 610`, `args: 366`, `func_start: 399`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 43`, `state_mutation: 175`, `fragile_debt: 1`, `duplicate_logic: 258`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `concurrency: 634`, `import: 22`
* *Defense:* `safety: 21`, `doc: 1`, `test: 187`, `immutability_locks: 322`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` server.browser, patchMessageChannel, client, internal-test-utils, react.react-server, static.browser, es6, WebpackMock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.545 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.398 IQR)
- **Top Global Matches:** file_cluster_4: 11.545, file_cluster_2: 11.602, file_cluster_8: 11.644
- **Magnitude:** 1885.02 | **LOC:** 4231 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (90.262%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 302.4)
  * `it` (Impact: 59.2)
  * `it` (Impact: 17.2)
  * `it` (Impact: 16.9)
  * `it` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 412`, `args: 227`, `func_start: 356`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 78`, `state_mutation: 201`, `fragile_debt: 2`, `duplicate_logic: 179`, `orphaned_logic: 5`
* *Architecture:* `concurrency: 475`, `import: 10`
* *Defense:* `safety: 2`, `doc: 1`, `test: 199`, `immutability_locks: 173`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` internal-test-utils, constants, react-dom, client, ReactFeatureFlags, server, react, scheduler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactChildFiber.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.51 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.126 IQR)
- **Top Global Matches:** file_cluster_8: 11.51, file_cluster_13: 11.633, file_cluster_11: 11.874
- **Magnitude:** 1847.56 | **LOC:** 2253 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (36.486%), Tech Debt (99.9794%)
**Top Internal Functions/Classes:**
  * `warnForMissingKey` (Impact: 355.0)
    * *Intent:* // If we have two debugInfo, we need to create a new one. This makes the array no longer // live so ...
  * `validateFragmentProps` (Impact: 321.0)
  * `pushDebugInfo` (Impact: 293.6)
  * `createChildReconciler` (Impact: 243.8)
  * `pushTreeFork` (Impact: 194.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 78`, `args: 15`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 52`, `planned_debt: 11`, `fragile_debt: 2`, `duplicate_logic: 17`
* *Architecture:* `api: 4`, `import: 19`
* *Defense:* `safety: 74`, `doc: 1`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ReactFiberTreeContext, ReactFiber, ReactFiberThenable, ReactInternalTypes, ReactTypeOfMode, getComponentNameFromFiber, ReactFiberNewContext, ReactTypes...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberCompleteWork.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.985 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.304 IQR)
- **Top Global Matches:** file_cluster_8: 11.985, file_cluster_13: 12.063, file_cluster_11: 12.444
- **Magnitude:** 1834.92 | **LOC:** 2082 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (29.9046%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `updateHostComponent` (Impact: 404.2)
  * `updateHostText` (Impact: 365.2)
  * `markUpdate` (Impact: 300.1)
  * `completeWork` (Impact: 131.5)
  * `appendAllChildren` (Impact: 100.7)
    * *Intent:* // TODO: If we move the `doesRequireClone` call after `bubbleProperties`
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 111`, `args: 12`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 69`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 6`, `duplicate_logic: 32`
* *Architecture:* `api: 6`, `import: 34`
* *Defense:* `safety: 96`, `doc: 4`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` ReactFiberTransition, ReactFiberWorkLoop, ReactInternalTypes, ReactFiberSuspenseContext, ReactFiberCacheComponent, ReactTypes, ReactFeatureFlags, ReactFiberLane...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberHooks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.247 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.225 IQR)
- **Top Global Matches:** file_cluster_13: 12.247, file_cluster_8: 12.338, file_cluster_11: 12.474
- **Magnitude:** 1612.7 | **LOC:** 5238 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (32.2532%), Tech Debt (99.9949%)
**Top Internal Functions/Classes:**
  * `useMemoCache` (Impact: 360.1)
  * `updateWorkInProgressHook` (Impact: 359.3)
    * *Intent:* // This is reset by checkDidRenderIdHook
  * `checkDepsAreArrayDev` (Impact: 104.6)
  * `notifyActionListeners` (Impact: 99.8)
  * `entangleTransitionUpdate` (Impact: 37.6)
    * *Intent:* // Check if the subscribe function changed. We can save some memory by
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 182`, `args: 65`, `func_start: 93`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 106`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 8`, `duplicate_logic: 38`
* *Architecture:* `io: 2`, `api: 32`, `concurrency: 15`, `import: 40`
* *Defense:* `safety: 122`, `doc: 1`, `immutability_locks: 122`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.000112 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` ReactFiberTransition, ReactFiberWorkLoop, ReactStartTransition, ReactInternalTypes, getComponentNameFromFiber, ReactTypes, ReactFeatureFlags, ReactFiberLane...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/react-refresh/src/__tests__/ReactFresh-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.564 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.408 IQR)
- **Top Global Matches:** file_cluster_8: 10.564, file_cluster_2: 10.722, file_cluster_4: 10.869
- **Magnitude:** 1450.26 | **LOC:** 3836 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.6742%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 153.3)
  * `testRemountingWithWrapper` (Impact: 24.3)
  * `it` (Impact: 15.5)
  * `it` (Impact: 15.3)
  * `it` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 733`, `args: 462`, `func_start: 570`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 24`, `state_mutation: 79`, `duplicate_logic: 274`, `orphaned_logic: 5`
* *Architecture:* `concurrency: 325`, `import: 8`
* *Defense:* `safety: 7`, `doc: 1`, `test: 417`, `immutability_locks: 190`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` internal-test-utils, factory, react-dom, runtime, client, react, scheduler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactFiberPerformanceTrack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.286 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.719 IQR)
- **Top Global Matches:** file_cluster_8: 10.286, file_cluster_7: 10.887, file_cluster_13: 10.944
- **Magnitude:** 1423.4 | **LOC:** 1721 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 56.2%
- **Risk Profile:** Cognitive Load (19.2899%), Tech Debt (41.7746%)
**Top Internal Functions/Classes:**
  * `logComponentErrored` (Impact: 554.9)
    * *Intent:* // $FlowFixMe[method-unbinding]
  * `logTransitionStart` (Impact: 117.9)
  * `logGestureStart` (Impact: 88.2)
  * `logComponentRender` (Impact: 75.4)
  * `logRecoveredRenderPhase` (Impact: 37.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 66`, `args: 29`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 47`, `planned_debt: 6`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 55`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 39`, `doc: 1`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.124
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ReactCapturedValue, ReactInternalTypes, getComponentNameFromFiber, ReactFeatureFlags, ReactPerformanceTrackProperties, ReactFiberLane, ReactWorkTags
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react-devtools-shared/src/__tests__/store-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_2` (Drift: 10.32 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.965 IQR)
- **Top Global Matches:** file_cluster_2: 10.32, file_cluster_8: 10.624, file_cluster_17: 11.134
- **Magnitude:** 1407.16 | **LOC:** 4039 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 89.3%
- **Risk Profile:** Cognitive Load (30.2012%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 121.4)
    * *Intent:* /** * Copyright (c) Meta Platforms, Inc. and affiliates. * * This source code is licensed under the ...
  * `describe` (Impact: 110.3)
  * `describe` (Impact: 59.9)
  * `describe` (Impact: 33.9)
  * `describe` (Impact: 32.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 545`, `args: 374`, `func_start: 462`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 42`, `planned_debt: 1`, `duplicate_logic: 244`, `orphaned_logic: 3`
* *Architecture:* `concurrency: 271`, `import: 10`
* *Defense:* `safety: 2`, `doc: 1`, `test: 256`, `immutability_locks: 172`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` react-dom, backendAPI, semver, client, react, ReactVersions, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.383 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.361 IQR)
- **Top Global Matches:** file_cluster_4: 11.383, file_cluster_2: 11.481, file_cluster_8: 11.508
- **Magnitude:** 1292.22 | **LOC:** 2980 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (91.2723%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 193.5)
  * `it` (Impact: 22.8)
  * `it` (Impact: 22.2)
  * `it` (Impact: 16.7)
  * `it` (Impact: 16.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 305`, `args: 162`, `func_start: 248`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 53`, `state_mutation: 154`, `duplicate_logic: 115`, `orphaned_logic: 3`
* *Architecture:* `concurrency: 341`, `import: 10`
* *Defense:* `safety: 3`, `doc: 1`, `test: 134`, `immutability_locks: 109`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` internal-test-utils, constants, react-dom, client, ReactFeatureFlags, server, react, scheduler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom/src/__tests__/ReactDOMHydrationDiff-test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 10.416 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.007 IQR)
- **Top Global Matches:** file_cluster_2: 10.416, file_cluster_8: 10.553, file_cluster_0: 11.014
- **Magnitude:** 1070.18 | **LOC:** 1648 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.1416%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 94.1)
  * `describe` (Impact: 75.9)
  * `describe` (Impact: 72.2)
  * `describe` (Impact: 71.8)
  * `describe` (Impact: 68.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 99`, `args: 96`, `func_start: 131`
* *Risk/State:* `safety_bypasses: 71`, `high_risk_execution: 2`, `state_mutation: 6`, `planned_debt: 2`, `duplicate_logic: 88`, `orphaned_logic: 1`
* *Architecture:* `io: 35`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 72`, `doc: 1`, `test: 83`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.11
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` react, client, util, server
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/react-dom-bindings/src/client/ReactInputSelection.js` (JAVASCRIPT) | Magnitude: 144.82 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, branch: 52, structural_boundaries: 31, safety: 21
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/labeled-break-within-label-switch.ts` (TYPESCRIPT) | Magnitude: 1.98 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 9, branch: 4, structural_boundaries: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/unlabeled-break-within-label-switch.ts` (TYPESCRIPT) | Magnitude: 1.98 | Delta: **0.177 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 9, branch: 4, structural_boundaries: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/labeled-break-within-label-loop.ts` (TYPESCRIPT) | Magnitude: 2.1 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 12, branch: 3, decorators: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/unlabeled-break-within-label-loop.ts` (TYPESCRIPT) | Magnitude: 2.1 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 12, branch: 3, decorators: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/react-native-renderer/src/__mocks__/react-native/Libraries/ReactPrivate/RawEventEmitter.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, api: 1, doc: 1, test: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/react-devtools-shared/src/backend/shared/DevToolsComponentStackFrame.js` (JAVASCRIPT) | Magnitude: 73.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, branch: 22, state_mutation: 12, structural_boundaries: 11
- `fixtures/legacy-jsx-runtimes/react-17/cjs/react-jsx-runtime.development.js` (JAVASCRIPT) | Magnitude: 0.62 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 355, state_mutation: 166, branch: 139, structural_boundaries: 116

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/shared/assign.js` (JAVASCRIPT) | Magnitude: 12.04 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, api: 1, doc: 1
- `packages/shared/hasOwnProperty.js` (JAVASCRIPT) | Magnitude: 12.04 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, api: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/react-devtools-shared/src/devtools/views/ErrorBoundary/UpdateExistingIssue.js` (JAVASCRIPT) | Magnitude: 3.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 6, ui_framework: 5, import: 4
- `packages/use-sync-external-store/src/__tests__/useSyncExternalStoreShimServer-test.js` (JAVASCRIPT) | Magnitude: 34.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 23, args: 15, func_start: 11
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/infer-component-props-non-null.tsx` (TYPESCRIPT) | Magnitude: 0.81 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, state_mutation: 3, ui_framework: 3
- `packages/react-dom/src/__tests__/ReactDOMserverIntegrationProgress-test.js` (JAVASCRIPT) | Magnitude: 16.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, func_start: 7, test: 5
- `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildReactiveScopeTerminalsHIR.ts` (TYPESCRIPT) | Magnitude: 9.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 163, state_mutation: 34, immutability_locks: 18, branch: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/todo-optional-call-chain-in-optional.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, branch: 3, structural_boundaries: 3, safety: 3
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/todo-optional-call-chain-in-optional.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, branch: 3, structural_boundaries: 3, safety: 3
- `compiler/packages/babel-plugin-react-compiler/src/Utils/Result.ts` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, args: 3, func_start: 3
- `compiler/packages/snap/src/sprout/shared-runtime.ts` (TYPESCRIPT) | Magnitude: 27.54 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 189, structural_boundaries: 127, api: 95, func_start: 61
- `fixtures/flight-parcel/types.d.ts` (TYPESCRIPT) | Magnitude: 2.76 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, args: 12, indent_spaces: 12, api: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/optional-member-expression-inverted-optionals-parallel-paths.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 6, branch: 5, safety: 5
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/optional-member-expression-inverted-optionals-parallel-paths.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 6, branch: 5, safety: 5
- `packages/react-reconciler/src/__tests__/useMemoCache-test.js` (JAVASCRIPT) | Magnitude: 346.46 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 290, structural_boundaries: 79, state_mutation: 57, func_start: 51
- `fixtures/legacy-jsx-runtimes/react-15/cjs/react-jsx-runtime.development.js` (JAVASCRIPT) | Magnitude: 0.84 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 286, state_mutation: 155, branch: 131, structural_boundaries: 104
- `packages/react-reconciler/src/ReactStrictModeWarnings.js` (JAVASCRIPT) | Magnitude: 107.58 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 37, branch: 31, state_mutation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-dont-memoize-array-with-capturing-map-after-hook.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, args: 4, ui_framework: 4
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-dont-memoize-array-with-mutable-map-after-hook.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, args: 4, ui_framework: 4
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-hook-if-alternate.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, state_mutation: 3, branch: 2, structural_boundaries: 2
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/valid-setState-in-useEffect-via-useEffectEvent-with-ref.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, immutability_locks: 12, ui_framework: 11, structural_boundaries: 9
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/type-provider-store-capture-namespace-import.tsx` (TYPESCRIPT) | Magnitude: 0.37 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, ui_framework: 7, immutability_locks: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/react-native-renderer/src/__tests__/ReactFabricFragmentRefs-test.internal.js` (JAVASCRIPT) | Magnitude: 53.66 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 22, concurrency: 20, args: 12
- `packages/react-reconciler/src/__tests__/ReactCPUSuspense-test.js` (JAVASCRIPT) | Magnitude: 176.16 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 44, func_start: 30, ui_framework: 30
- `packages/react/src/__tests__/ReactStartTransition-test.js` (JAVASCRIPT) | Magnitude: 67.6 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 26, concurrency: 19, state_mutation: 16
- `packages/react-reconciler/src/__tests__/ReactIsomorphicAct-test.js` (JAVASCRIPT) | Magnitude: 126.5 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 65, func_start: 36, concurrency: 36
- `packages/react-dom/src/test-utils/FizzTestUtils.js` (JAVASCRIPT) | Magnitude: 163.86 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 138, branch: 47, state_mutation: 24, safety: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/react/src/ReactContext.js` (JAVASCRIPT) | Magnitude: 16.44 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 4, safety: 2, import: 2
- `packages/react/src/BadMapPolyfill.js` (JAVASCRIPT) | Magnitude: 19.22 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, branch: 3, state_mutation: 3, structural_boundaries: 2
- `packages/react-devtools-fusebox/src/frontend.d.ts` (TYPESCRIPT) | Magnitude: 4.32 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 43, indent_spaces: 40, api: 19, args: 14
- `compiler/packages/babel-plugin-react-compiler/src/Utils/todo.ts` (TYPESCRIPT) | Magnitude: 0.87 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, safety: 3, planned_debt: 3, branch: 2
- `packages/react-native-renderer/src/NativeMethodsMixinUtils.js` (JAVASCRIPT) | Magnitude: 25.76 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, branch: 8, structural_boundaries: 6, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/eslint-plugin-react-hooks/src/code-path-analysis/code-path-segment.js` (JAVASCRIPT) | Magnitude: 85.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, doc: 48, state_mutation: 32, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/react-devtools-shared/src/devtools/views/Profiler/SnapshotCommitListItem.js` (JAVASCRIPT) | Magnitude: 11.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 12, branch: 8, immutability_locks: 7
- `packages/react-devtools-shared/src/devtools/views/utils.js` (JAVASCRIPT) | Magnitude: 107.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, branch: 39, structural_boundaries: 36, api: 11
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/error.invalid-mutate-props-via-for-of-iterator.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, state_mutation: 3, immutability_locks: 2, branch: 1
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/error.invalid-rules-of-hooks-c906cace44e9.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: func_start: 2, indent_spaces: 2, branch: 1, structural_boundaries: 1
- `packages/react-devtools-shared/src/devtools/views/Components/ElementBadges.js` (JAVASCRIPT) | Magnitude: 3.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, branch: 12, structural_boundaries: 7, safety_bypasses: 5

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

- `packages/react-devtools-shared/src/backend/fiber/renderer.js` -> Churn: **100.0%** | Cog Load: 48.3691% | Debt: 99.7923%
- `packages/react-client/src/ReactFlightClient.js` -> Churn: **84.38%** | Cog Load: 49.044% | Debt: 99.9975%
- `packages/react-server/src/ReactFlightServer.js` -> Churn: **79.09%** | Cog Load: 52.2587% | Debt: 99.9994%
- `packages/react-reconciler/src/ReactFiberWorkLoop.js` -> Churn: **77.33%** | Cog Load: 22.6388% | Debt: 99.992%
- `packages/react-devtools-shared/src/devtools/store.js` -> Churn: **77.3%** | Cog Load: 64.5306% | Debt: 99.9772%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `flow-typed/environments/node.js` -> **Jan Kassens** (100.0% isolated ownership) | Magnitude: 2088.56
- `packages/react-devtools-shared/src/__tests__/store-test.js` -> **Sebastian "Sebbie" Silbermann** (89.3% isolated ownership) | Magnitude: 1407.16
- `packages/react-dom/src/__tests__/ReactDOMHydrationDiff-test.js` -> **o-m12a** (100.0% isolated ownership) | Magnitude: 1070.18
- `packages/react-reconciler/src/__tests__/ReactTransitionTracing-test.js` -> **Ricky** (100.0% isolated ownership) | Magnitude: 1042.88
- `packages/react-devtools-shared/src/__tests__/preprocessData-test.js` -> **Sebastian "Sebbie" Silbermann** (100.0% isolated ownership) | Magnitude: 977.46

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
- `packages/react-devtools-shared/src/storage.js` -> **Severity: 235.197** (Blast Radius: 2.354 * Doc Risk: 99.9139%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
