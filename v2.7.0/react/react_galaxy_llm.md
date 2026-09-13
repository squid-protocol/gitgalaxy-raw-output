# ARCHITECTURAL_BRIEF: react
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/facebook/react.git` |
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
| Total Artifacts | 6879 |
| Analyzed Artifacts (Scanned) | 6373 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 506 |
| Total LOC | 590439 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 92.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2684 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 305 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 3687 | 520498 | 57.9% |
| MARKDOWN | 1803 | 0 | 28.3% |
| TYPESCRIPT | 515 | 61075 | 8.1% |
| PLAINTEXT | 128 | 2 | 2.0% |
| CSS | 112 | 4332 | 1.8% |
| HTML | 79 | 3116 | 1.2% |
| JSON | 28 | 1213 | 0.4% |
| SHELL | 12 | 195 | 0.2% |
| XML | 9 | 8 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4434 | 69.6% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1929 | 30.3% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 506*

**Composition by Extension & Reason:**
- `.js`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 52x Excluded (Saturation: Line 14 exceeds 500 chars), 13x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.md`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2745 LOC), 1x Excluded (Machine-Generated Source Code Signature: 64 LOC)
- `.map`: 67x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Unsupported Extension: '.map')
- `no_extension`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace'), 1x Unsupported Format (.undeterminable)
- `.lock`: 42x Excluded (Unsupported Extension: '.lock'), 1x Excluded (Machine-Generated Source Code Signature: 1743 LOC), 1x Unsupported Format (.lock)
- `.png`: 33x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12828 LOC)
- `.ico`: 10x Excluded (Explicitly Denied Extension: '.ico')
- `.snap`: 5x Unsupported Format (.snap), 1x Excluded (Unsupported Extension: '.snap')
- `.tsx`: 1x Excluded (Saturation: Line 20 exceeds 500 chars), 1x Excluded (Saturation: Line 22 exceeds 500 chars)
- `.ts`: 1x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (Saturation: Line 82 exceeds 500 chars)
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')
- `.wasm`: 1x Excluded (Unsupported Extension: '.wasm')
- `.webmanifest`: 1x Excluded (Unsupported Extension: '.webmanifest')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.4 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 38.4 | 52.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.4 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 12.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.4 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 96.1 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 82.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 27.0 | 3.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 52.0 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 667 | 233 | 0 | `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts` |
| cleanup | 513 | 173 | 0 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |
| guards | 21575 | 1495 | 5 | `packages/react-devtools-shared/src/backend/fiber/renderer.js` |
| danger | 11891 | 1293 | 3 | `flow-typed/environments/node.js` |
| concurrency | 22689 | 751 | 2 | `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` |
| connectivity | 12045 | 3216 | 3 | `packages/react-reconciler/src/forks/ReactFiberConfig.custom.js` |
| io | 1738 | 313 | 0 | `compiler/packages/snap/src/minimize.ts` |
| crypto | 6 | 5 | 0 | `packages/react-server/src/__tests__/ReactFlightAsyncDebugInfo-test.js` |
| ipc | 159 | 64 | 0 | `flow-typed/environments/node.js` |
| time | 555 | 178 | 0 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |
| serialization | 335 | 130 | 0 | `packages/react-reconciler/src/__tests__/ReactIncremental-test.js` |
| regex | 468 | 190 | 0 | `packages/react-devtools-timeline/src/import-worker/preprocessData.js` |
| events | 5259 | 589 | 0 | `compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts` |
| tests | 24179 | 467 | 0 | `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` |
| docs | 3949 | 2069 | 1 | `packages/react-devtools-extensions/flow-typed/jest.js` |
| debt | 8548 | 975 | 1 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |
| mutation | 115506 | 3850 | 34 | `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` |
| dead_code | 2207 | 1121 | 1 | `flow-typed/environments/node.js` |
| credential | 13 | 8 | 0 | `packages/react-devtools-shared/src/__tests__/utils-test.js` |
| threat | 1365 | 334 | 0 | `packages/react-dom/src/__tests__/ReactDOMInput-test.js` |
| ml_ai | 61 | 30 | 0 | `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/InferReactiveScopeVariables.ts` |
| ui | 34559 | 2296 | 6 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `compiler/packages/snap/src/minimize.ts` (Hits: 150)
- `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts` (Hits: 56)
- `flow-typed/environments/node.js` (Hits: 52)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **shared-runtime.ts** (`compiler/packages/snap/src/sprout/shared-runtime.ts`) — 550 inbound connections
2. **ReactTypes.js** (`packages/shared/ReactTypes.js`) — 200 inbound connections
3. **client.js** (`packages/react-dom/client.js`) — 192 inbound connections
4. **ReactFeatureFlags.js** (`packages/shared/ReactFeatureFlags.js`) — 117 inbound connections
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

- `attach` (@ `packages/react-devtools-shared/src/backend/fiber/renderer.js`) -> Impact: **1191.5** | LOC: 1882
- `visitFunctionWithDependencies` (@ `packages/eslint-plugin-react-hooks/src/rules/ExhaustiveDeps.ts`) -> Impact: **737.2** | LOC: 1144
  * *Intent:* /** * Visitor for both function expressions and arrow function expressions. */
- `lowerStatement` (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **683.0** | LOC: 1300
  * *Intent:* // Helper to lower a statement
- `setProp` (@ `packages/react-dom-bindings/src/client/ReactDOMComponent.js`) -> Impact: **590.8** | LOC: 599
- `create` (@ `packages/eslint-plugin-react-hooks/src/rules/ExhaustiveDeps.ts`) -> Impact: **528.0** | LOC: 1453
- `createChildReconciler` (@ `packages/react-reconciler/src/ReactChildFiber.js`) -> Impact: **510.7** | LOC: 1672
  * *Intent:* // This wrapper function exists because I expect to clone the code in each path // to be able to optimize each path individually by branching early. T...
- `lowerExpression` (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **482.1** | LOC: 1189
- `completeWork` (@ `packages/react-reconciler/src/ReactFiberCompleteWork.js`) -> Impact: **452.6** | LOC: 1012
- `commitMutationEffectsOnFiber` (@ `packages/react-reconciler/src/ReactFiberCommitWork.js`) -> Impact: **413.4** | LOC: 707
- `lowerAssignment` (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **405.0** | LOC: 587

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/react-dom/src/__tests__` | 129 | 32441.6 | 48.84% | 51.0% |
| `packages/react-reconciler/src` | 81 | 27934.22 | 30.25% | 29.92% |
| `packages/react-reconciler/src/__tests__` | 76 | 19254.22 | 57.47% | 62.15% |
| `packages/react-server/src` | 37 | 12533.76 | 34.89% | 18.75% |
| `packages/react-dom-bindings/src/client` | 28 | 9957.14 | 24.47% | 8.58% |
| `compiler/packages/babel-plugin-react-compiler/src/HIR` | 28 | 8276.9 | 20.65% | 7.09% |
| `packages/react-devtools-shared/src/__tests__` | 34 | 7466.32 | 30.49% | 55.51% |
| `packages/react-devtools-shared/src/backend/fiber` | 2 | 6703.28 | 54.96% | 12.74% |
| `packages/react-dom-bindings/src/server` | 7 | 5675.58 | 26.48% | 5.16% |
| `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes` | 30 | 5648.44 | 30.72% | 2.7% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/todo.bail.rules-of-hooks-fadd52c1e460.js` -> **100.0%** Exposure
- `packages/react-client/src/forks/ReactFlightClientConfig.markup.js` -> **100.0%** Exposure
- `packages/react-dom/src/__tests__/ReactComponentLifeCycle-test.js` -> **100.0%** Exposure
- `packages/react-dom/src/__tests__/ReactDOMFizzShellHydration-test.js` -> **100.0%** Exposure
- `packages/react-dom/src/__tests__/ReactDOMServerIntegrationLegacyContextDisabled-test.internal.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/conditional-early-return.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/conditional-early-return.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/sequentially-constant-progagatable-if-test-conditions.js` -> **100.0%** Exposure
- `fixtures/concurrent/time-slicing/src/Clock.js` -> **100.0%** Exposure
- `fixtures/dom/src/components/Fixture.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `flow-typed/environments/node.js` -> **187** Orphaned Functions | **4** Duplicates
- `packages/react-refresh/src/__tests__/ReactFresh-test.js` -> **6** Orphaned Functions | **122** Duplicates
- `packages/react-dom/src/__tests__/ReactDOMEventPropagation-test.js` -> **18** Orphaned Functions | **100** Duplicates
- `packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js` -> **1** Orphaned Functions | **109** Duplicates
- `packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMBrowser-test.js` -> **1** Orphaned Functions | **102** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `scripts/tasks/danger.js` -> **100.0%** Exposure
- `compiler/packages/react-mcp-server/src/utils/algolia.ts` -> **99.9946%** Exposure
- `packages/react-client/src/__tests__/ReactFlight-test.js` -> **19.6339%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5925` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/react-reconciler/src/ReactProfilerTimer.js` (JAVASCRIPT) -> Cumulative Risk: **773.06**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 730.52 | **LOC:** 712 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 87.5%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.6965%)
- **Heaviest Functions:** `startUpdateTimerByLane` (Impact: 57.9), `startHostActionTimer` (Impact: 26.4), `startPingTimerByLanes` (Impact: 16.9)

### 2. `packages/react-devtools-shared/src/__tests__/TimelineProfiler-test.js` (JAVASCRIPT) -> Cumulative Risk: **769.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1131.38 | **LOC:** 2644 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9969%), State Flux (99.9478%)
- **Heaviest Functions:** `createUserTimingPolyfill` (Impact: 11.3), `filterMarkData` (Impact: 10.4), `stopProfilingAndGetTimelineData` (Impact: 8.0)

### 3. `packages/react-dom-bindings/src/server/fizz-instruction-set/ReactDOMFizzInstructionSetShared.js` (JAVASCRIPT) -> Cumulative Risk: **765.52**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 525.82 | **LOC:** 654 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.0809%)
- **Heaviest Functions:** `revealCompletedBoundariesWithViewTransitions` (Impact: 103.2), `completeBoundaryWithStyles` (Impact: 50.2), `revealCompletedBoundaries` (Impact: 33.2)

### 4. `packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMNode-test.js` (JAVASCRIPT) -> Cumulative Risk: **765.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 810.88 | **LOC:** 1913 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 46.2%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.8252%), Documentation (98.7805%)
- **Heaviest Functions:** `filterStackFrame` (Impact: 10.9), `reencodeFlightStream` (Impact: 9.8), `normalizeCodeLocInfo` (Impact: 9.6)

### 5. `packages/react-dom/src/__tests__/ReactUpdates-test.js` (JAVASCRIPT) -> Cumulative Risk: **758.95**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1061.68 | **LOC:** 2049 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.7868%)
- **Heaviest Functions:** `error` (Impact: 9.7), `normalizeCodeLocInfo` (Impact: 7.7), `testUpdates` (Impact: 7.2)

### 6. `packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js` (JAVASCRIPT) -> Cumulative Risk: **754.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 4367.24 | **LOC:** 6652 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 56.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.7585%), State Flux (99.5721%), Churn (88.76%)
- **Heaviest Functions:** `isHostHoistableType` (Impact: 146.8), `canHydrateInstance` (Impact: 116.8), `animateGesture` (Impact: 94.5)

### 7. `packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMEdge-test.js` (JAVASCRIPT) -> Cumulative Risk: **751.91**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1054.66 | **LOC:** 2407 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 36.4%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.3103%)
- **Heaviest Functions:** `dripStream` (Impact: 18.3), `passThrough` (Impact: 11.0), `start` (Impact: 10.7)

### 8. `packages/react-client/src/ReactFlightClient.js` (JAVASCRIPT) -> Cumulative Risk: **748.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3356.54 | **LOC:** 5407 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 47.8%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9911%), Documentation (99.2647%), Churn (86.57%)
- **Heaviest Functions:** `flushComponentPerformance` (Impact: 151.0), `fulfillReference` (Impact: 144.5), `parseModelString` (Impact: 139.6)

### 9. `packages/react-reconciler/src/__tests__/StrictEffectsMode-test.js` (JAVASCRIPT) -> Cumulative Risk: **747.13**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 485.34 | **LOC:** 968 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (98.9049%)
- **Heaviest Functions:** `Child` (Impact: 5.8), `App` (Impact: 3.7), `App` (Impact: 2.7)

### 10. `packages/react-dom/src/__tests__/ReactDOMEventPropagation-test.js` (JAVASCRIPT) -> Cumulative Risk: **745.7**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1461.76 | **LOC:** 3015 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9414%), Tech Debt (99.9208%)
- **Heaviest Functions:** `testNativeStopPropagationInInnerEmulatedBubblePhase` (Impact: 6.4), `testNativeStopPropagationInInnerCapturePhase` (Impact: 6.3), `testNativeStopPropagationInOuterCapturePhase` (Impact: 6.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/react-devtools-shared/src/backend/fiber/renderer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6545.86 | **LOC:** 8154 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 54.3%
- **Risk Profile:** Cognitive Load (60.6848%), Tech Debt (11.3996%)
**Top Internal Functions/Classes:**
  * `attach` (Impact: 1191.5)
  * `updateFiberRecursively` (Impact: 362.1)
    * *Intent:* // Returns whether closest unfiltered fiber parent needs to reset its child list.
  * `mountFiberRecursively` (Impact: 156.0)
  * `updateVirtualChildrenRecursively` (Impact: 139.2)
  * `inspectFiberInstanceRaw` (Impact: 129.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 555 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 1770
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1617`, `structural_boundaries: 683`, `args: 193`, `func_start: 169`
* *Risk/State:* `safety_bypasses: 156`, `state_mutation: 660`, `dead_code: 6`, `planned_debt: 36`, `fragile_debt: 7`
* *Architecture:* `api: 5`, `concurrency: 8`, `import: 30`
* *Defense:* `safety: 917`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 7.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` constants, utils, profilingHooks, DevToolsOwnerStack, DevToolsServerComponentLogs, ReactSymbols, types, utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-dom-bindings/src/server/ReactFizzConfigDOM.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5150.04 | **LOC:** 7160 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (47.906%), Tech Debt (11.383%)
**Top Internal Functions/Classes:**
  * `pushAttribute` (Impact: 275.8)
  * `pushStartInstance` (Impact: 199.9)
  * `pushLink` (Impact: 147.3)
  * `pushImg` (Impact: 140.4)
  * `createRenderState` (Impact: 124.2)
    * *Intent:* // Allows us to keep track of what we've already written so we can refer back to it. // if passed ex...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 411 instances
* *High Risk Execution (weighted view):* 16
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 1325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1403`, `structural_boundaries: 610`, `args: 155`, `func_start: 147`
* *Risk/State:* `safety_bypasses: 143`, `high_risk_execution: 35`, `state_mutation: 503`, `dead_code: 9`, `planned_debt: 24`, `fragile_debt: 9`
* *Architecture:* `api: 64`, `concurrency: 10`, `import: 28`
* *Defense:* `safety: 451`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.549
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` ReactControlledValuePropTypes, ReactDOMFormActions, ReactDOMInvalidARIAHook, ReactDOMNullInputValuePropHook, ReactDOMResourceValidation, ReactDOMUnknownPropertyHook, crossOriginStrings, getAttributeAlias...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.109
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-server/src/ReactFlightServer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4515.0 | **LOC:** 6445 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (81.7465%), Tech Debt (23.1855%)
**Top Internal Functions/Classes:**
  * `renderModelDestructive` (Impact: 395.7)
  * `renderDebugModel` (Impact: 290.5)
    * *Intent:* // This is a forked version of renderModel which should never error, never suspend and is limited //...
  * `visitAsyncNodeImpl` (Impact: 179.1)
  * `renderElement` (Impact: 100.8)
  * `serializeAsyncIterable` (Impact: 85.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 424 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 1371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1098`, `structural_boundaries: 589`, `args: 202`, `func_start: 163`
* *Risk/State:* `safety_bypasses: 142`, `state_mutation: 523`, `dead_code: 5`, `planned_debt: 33`, `fragile_debt: 15`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `concurrency: 42`, `import: 29`
* *Defense:* `safety: 638`, `doc: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.093
  * `Choke Point (Betweenness):` 0.000592 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` ReactFlightAsyncSequence, ReactFlightCallUserSpace, ReactFlightHooks, ReactFlightServerConfig, ReactFlightServerTemporaryReferences, ReactFlightThenable, ReactServerStreamConfig, ReactSharedInternalsServer...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4367.24 | **LOC:** 6652 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 56.0%
- **Risk Profile:** Cognitive Load (71.1909%), Tech Debt (14.9235%)
**Top Internal Functions/Classes:**
  * `isHostHoistableType` (Impact: 146.8)
  * `canHydrateInstance` (Impact: 116.8)
  * `animateGesture` (Impact: 94.5)
  * `hydrateHoistable` (Impact: 88.5)
  * `createInstance` (Impact: 84.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 322 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 106
* *State Mutation (weighted view):* 1066
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1293`, `structural_boundaries: 774`, `args: 287`, `func_start: 266`
* *Risk/State:* `safety_bypasses: 199`, `high_risk_execution: 7`, `state_mutation: 422`, `dead_code: 9`, `planned_debt: 36`, `fragile_debt: 15`
* *Architecture:* `api: 189`, `concurrency: 51`, `import: 43`
* *Defense:* `safety: 552`, `doc: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.363
  * `Choke Point (Betweenness):` 0.000327 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 40):` DOMEventNames, DOMPluginEventSystem, ReactDOMEventListener, ReactDOMEventReplaying, ReactDOMFormActions, ReactDOMResourceValidation, DOMAccessibilityRoles, DOMNamespaces...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `packages/react-server/src/ReactFizzServer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4058.34 | **LOC:** 6256 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (57.6297%), Tech Debt (14.4263%)
**Top Internal Functions/Classes:**
  * `finishedTask` (Impact: 102.9)
  * `retryNode` (Impact: 100.9)
  * `renderElement` (Impact: 96.1)
  * `renderSuspenseListRows` (Impact: 94.9)
  * `abortTask` (Impact: 88.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 479 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 1567
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 860`, `structural_boundaries: 345`, `args: 155`, `func_start: 127`
* *Risk/State:* `safety_bypasses: 139`, `state_mutation: 609`, `dead_code: 7`, `planned_debt: 23`, `fragile_debt: 16`
* *Architecture:* `api: 23`, `concurrency: 4`, `import: 31`
* *Defense:* `safety: 545`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` ReactFizzAsyncDispatcher, ReactFizzCallUserSpace, ReactFizzClassComponent, ReactFizzComponentStack, ReactFizzConfig, ReactFizzCurrentTask, ReactFizzHooks, ReactFizzLegacyContext...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `packages/react-client/src/ReactFlightClient.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3356.54 | **LOC:** 5407 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 47.8%
- **Risk Profile:** Cognitive Load (66.1086%), Tech Debt (23.0916%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 151.0)
  * `fulfillReference` (Impact: 144.5)
  * `parseModelString` (Impact: 139.6)
  * `processBinaryChunk` (Impact: 100.2)
  * `processStringChunk` (Impact: 93.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 425 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 128
* *State Mutation (weighted view):* 1314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 953`, `structural_boundaries: 463`, `args: 157`, `func_start: 108`
* *Risk/State:* `safety_bypasses: 135`, `high_risk_execution: 5`, `state_mutation: 464`, `dead_code: 7`, `planned_debt: 27`, `fragile_debt: 13`, `duplicate_logic: 2`
* *Architecture:* `api: 16`, `concurrency: 28`, `import: 22`
* *Defense:* `safety: 394`, `doc: 2`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.556
  * `Choke Point (Betweenness):` 0.000397 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ReactFlightClientConfig, ReactFlightClientDevToolsHook, ReactFlightPerformanceTrack, ReactFlightReplyClient, ReactFlightTemporaryReferences, react, ReactFlightServerConfig, ReactLazy...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberCommitWork.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3216.3 | **LOC:** 5350 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 30.8%
- **Risk Profile:** Cognitive Load (27.4741%), Tech Debt (18.9343%)
**Top Internal Functions/Classes:**
  * `commitMutationEffectsOnFiber` (Impact: 413.4)
  * `commitPassiveMountOnFiber` (Impact: 378.4)
  * `commitLayoutEffectOnFiber` (Impact: 190.7)
  * `commitDeletionEffectsOnFiber` (Impact: 153.3)
  * `reconnectPassiveEffects` (Impact: 119.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 558
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1099`, `structural_boundaries: 329`, `args: 79`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 206`, `dead_code: 4`, `planned_debt: 72`, `fragile_debt: 6`
* *Architecture:* `api: 16`, `concurrency: 1`, `import: 39`
* *Defense:* `safety: 336`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` ReactFiberActivityComponent, ReactFiberCacheComponent, ReactFiberClassUpdateQueue, ReactFiberCommitEffects, ReactFiberCommitHostEffects, ReactFiberCommitViewTransitions, ReactFiberConfig, ReactFiberDevToolsHook...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberWorkLoop.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3112.02 | **LOC:** 5622 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 76.2%
- **Risk Profile:** Cognitive Load (45.7464%), Tech Debt (16.5354%)
**Top Internal Functions/Classes:**
  * `completeRoot` (Impact: 166.7)
  * `commitRoot` (Impact: 117.4)
  * `renderRootConcurrent` (Impact: 100.4)
  * `prepareFreshStack` (Impact: 98.4)
  * `performWorkOnRoot` (Impact: 93.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 315 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1044
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 830`, `structural_boundaries: 415`, `args: 141`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 414`, `dead_code: 8`, `planned_debt: 48`, `fragile_debt: 8`
* *Architecture:* `api: 69`, `concurrency: 2`, `import: 65`
* *Defense:* `safety: 342`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.687
  * `Choke Point (Betweenness):` 0.001014 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` ReactCapturedValue, ReactChildFiber, ReactCurrentFiber, ReactEventPriorities, ReactFiber, ReactFiberAct, ReactFiberActivityComponent, ReactFiberApplyGesture...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2912.14 | **LOC:** 9605 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (78.0514%), Tech Debt (10.2146%)
**Top Internal Functions/Classes:**
  * `act` (Impact: 41.8)
  * `expectErrors` (Impact: 14.8)
  * `readText` (Impact: 14.3)
  * `error` (Impact: 13.3)
  * `App` (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 186 instances
* *Amplified Cascading Flux:* 76 instances
* *High Risk Execution (weighted view):* 10
* *Concurrency (weighted view):* 1662
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 1534`, `args: 1008`, `func_start: 433`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 12`, `state_mutation: 289`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 732`, `import: 13`
* *Defense:* `safety: 52`, `doc: 1`, `test: 629`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` FizzTestUtils, immutable, internal-test-utils, jsdom, prop-types, react, react-dom, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom-bindings/src/client/ReactDOMComponent.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2903.4 | **LOC:** 3380 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.9353%), Tech Debt (14.2869%)
**Top Internal Functions/Classes:**
  * `setProp` (Impact: 590.8)
  * `updateProperties` (Impact: 403.2)
  * `diffHydratedGenericElement` (Impact: 370.6)
  * `setInitialProperties` (Impact: 233.3)
  * `setPropOnCustomElement` (Impact: 113.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Cascading Flux:* 86 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 975`, `structural_boundaries: 371`, `args: 36`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 107`, `high_risk_execution: 25`, `state_mutation: 90`, `dead_code: 9`, `planned_debt: 38`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 27`
* *Defense:* `safety: 288`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.193
  * `Choke Point (Betweenness):` 0.000141 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` DOMPluginEventSystem, EventRegistry, ReactControlledValuePropTypes, ReactDOMInvalidARIAHook, ReactDOMNullInputValuePropHook, ReactDOMUnknownPropertyHook, getAttributeAlias, isCustomElement...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2692.64 | **LOC:** 4556 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (33.5283%), Tech Debt (15.2882%)
**Top Internal Functions/Classes:**
  * `lowerStatement` (Impact: 683.0)
    * *Intent:* // Helper to lower a statement
  * `lowerExpression` (Impact: 482.1)
  * `lowerAssignment` (Impact: 405.0)
  * `lower` (Impact: 123.6)
    * *Intent:* * ************************************* Lowering to HIR ************************************* * ****...
  * `isReorderableExpression` (Impact: 98.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 106 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 966`, `structural_boundaries: 425`, `args: 90`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 113`, `planned_debt: 59`, `fragile_debt: 2`
* *Architecture:* `io: 56`, `api: 8`, `concurrency: 4`, `import: 9`
* *Defense:* `safety: 224`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.134
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` &&
        expr.node.property.name ===, CompilerError, utils, Environment, HIR, HIRBuilder, ObjectShape, traverse...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberBeginWork.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2413.84 | **LOC:** 4449 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 53.8%
- **Risk Profile:** Cognitive Load (38.6201%), Tech Debt (14.832%)
**Top Internal Functions/Classes:**
  * `beginWork` (Impact: 126.2)
  * `updateDehydratedSuspenseComponent` (Impact: 101.3)
  * `attemptEarlyBailoutIfNoScheduledUpdate` (Impact: 93.3)
  * `updateSuspenseComponent` (Impact: 81.2)
  * `updateOffscreenComponent` (Impact: 76.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 235 instances
* *State Mutation (weighted view):* 775
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 573`, `structural_boundaries: 308`, `args: 71`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 305`, `dead_code: 2`, `planned_debt: 25`, `fragile_debt: 8`
* *Architecture:* `api: 7`, `import: 54`
* *Defense:* `safety: 218`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.133
  * `Choke Point (Betweenness):` 0.00012 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 44):` ReactCapturedValue, ReactChildFiber, ReactCurrentFiber, ReactFiber, ReactFiberActivityComponent, ReactFiberCacheComponent, ReactFiberCallUserSpace, ReactFiberClassComponent...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin-react-hooks/src/rules/ExhaustiveDeps.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2170.6 | **LOC:** 2139 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (52.4669%), Tech Debt (9.9984%)
**Top Internal Functions/Classes:**
  * `visitFunctionWithDependencies` (Impact: 737.2)
    * *Intent:* /** * Visitor for both function expressions and arrow function expressions. */
  * `create` (Impact: 528.0)
  * `isStableKnownHookValue` (Impact: 81.9)
    * *Intent:* // tell if some values don't have to be declared as deps. // Some are known to be stable based on Ho...
  * `visitCallExpression` (Impact: 79.3)
  * `gatherDependenciesRecursively` (Impact: 47.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 472`, `structural_boundaries: 325`, `args: 72`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 88`, `dead_code: 5`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `api: 2`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 26`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.132
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Utils, eslint, estree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactChildFiber.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2156.18 | **LOC:** 2253 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (62.13%), Tech Debt (12.8909%)
**Top Internal Functions/Classes:**
  * `createChildReconciler` (Impact: 510.7)
    * *Intent:* // This wrapper function exists because I expect to clone the code in each path // to be able to opt...
  * `reconcileChildrenIterator` (Impact: 91.7)
  * `reconcileChildrenArray` (Impact: 87.9)
  * `updateFromMap` (Impact: 86.0)
  * `updateSlot` (Impact: 67.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 215`, `args: 47`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 193`, `dead_code: 2`, `planned_debt: 14`, `fragile_debt: 2`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 256`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.125
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` ReactCurrentFiber, ReactFiber, ReactFiberFlags, ReactFiberHotReloading, ReactFiberHydrationContext, ReactFiberLane, ReactFiberNewContext, ReactFiberThenable...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2141.82 | **LOC:** 2976 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 77.8%
- **Risk Profile:** Cognitive Load (64.6624%), Tech Debt (9.363%)
**Top Internal Functions/Classes:**
  * `applyEffect` (Impact: 369.8)
  * `computeEffectsForSignature` (Impact: 224.7)
  * `computeSignatureForInstruction` (Impact: 223.1)
    * *Intent:* /** * Computes an effect signature for the instruction _without_ looking at the inference state, * a...
  * `computeEffectsForLegacySignature` (Impact: 109.7)
    * *Intent:* /** * Creates a set of aliasing effects given a legacy FunctionSignature. This makes all of the * ol...
  * `findNonMutatedDestructureSpreads` (Impact: 67.5)
    * *Intent:* * The primary use case for this is props spreading: * * ``` * function Component({prop, ...otherProp...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 536
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 227`, `args: 55`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 194`, `planned_debt: 8`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 6`, `import: 10`
* *Defense:* `safety: 53`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .., CompilerError, HIR, HIRBuilder, ObjectShape, PrintHIR, visitors, utils...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2071.2 | **LOC:** 4231 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (89.3339%), Tech Debt (99.9953%)
**Top Internal Functions/Classes:**
  * `dispatchMouseEvent` (Impact: 11.2)
  * `Child` (Impact: 7.7)
  * `Sibling` (Impact: 6.0)
  * `Component` (Impact: 5.1)
  * `Component` (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 172 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 1162
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 683`, `args: 389`, `func_start: 200`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 60`, `state_mutation: 273`, `fragile_debt: 2`, `duplicate_logic: 109`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 302`, `import: 10`
* *Defense:* `safety: 4`, `doc: 1`, `test: 312`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` internal-test-utils, react, react-dom, client, server, constants, scheduler, ReactFeatureFlags
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/packages/snap/src/minimize.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1681.2 | **LOC:** 2143 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.367%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `simplifyForStatements` (Impact: 37.6)
    * *Intent:* /** * Generator that simplifies for statements: * - Replace with init (if expression) * - Replace wi...
  * `simplifyCallExpressions` (Impact: 34.0)
    * *Intent:* /** * Generator that simplifies call expressions by replacing them with their arguments. * For singl...
  * `minimize` (Impact: 29.5)
    * *Intent:* /** * Core minimization loop that attempts to reduce the input source code * while preserving the co...
  * `simplifySinglePropertyObjects` (Impact: 28.6)
    * *Intent:* /** * Generator that replaces single-property objects with the property value. * For regular propert...
  * `simplifyForInStatements` (Impact: 26.6)
    * *Intent:* /** * Generator that simplifies for-in statements: * - Replace with left (variable declaration or ex...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 668
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 149`, `args: 98`, `func_start: 84`
* *Risk/State:* `state_mutation: 228`
* *Architecture:* `io: 150`, `api: 8`, `import: 9`
* *Defense:* `safety: 8`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.124
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` compiler.js, constants.js, core, generator, traverse, types, TestUtils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberHooks.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1552.16 | **LOC:** 5238 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (71.657%), Tech Debt (45.3891%)
**Top Internal Functions/Classes:**
  * `useMemoCache` (Impact: 29.6)
  * `areHookInputsEqual` (Impact: 19.7)
  * `updateWorkInProgressHook` (Impact: 17.5)
  * `warnOnHookMismatchInDev` (Impact: 13.6)
  * `requestFormReset` (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 325 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 1139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 518`, `structural_boundaries: 680`, `args: 330`, `func_start: 186`
* *Risk/State:* `safety_bypasses: 293`, `state_mutation: 489`, `dead_code: 7`, `planned_debt: 25`, `fragile_debt: 9`, `duplicate_logic: 15`
* *Architecture:* `api: 17`, `concurrency: 6`, `import: 40`
* *Defense:* `safety: 297`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.000183 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` ReactEventPriorities, ReactFiberAsyncAction, ReactFiberBeginWork, ReactFiberCacheComponent, ReactFiberCallUserSpace, ReactFiberClassUpdateQueue, ReactFiberConcurrentUpdates, ReactFiberConfig...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1479.06 | **LOC:** 2480 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (61.3234%), Tech Debt (11.0128%)
**Top Internal Functions/Classes:**
  * `codegenInstructionValue` (Impact: 259.8)
  * `codegenTerminal` (Impact: 157.1)
  * `codegenInstructionNullable` (Impact: 85.6)
  * `codegenFunction` (Impact: 59.6)
  * `codegenReactiveScope` (Impact: 42.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 132 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 297`, `args: 70`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 156`, `planned_debt: 9`, `fragile_debt: 3`
* *Architecture:* `io: 13`, `api: 6`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 30`, `doc: 9`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` , CompilerError, Entrypoint, HIR, Environment, HIR, PrintHIR, visitors...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `flow-typed/environments/node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1475.1 | **LOC:** 4287 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.9272%), Tech Debt (99.6245%)
**Top Internal Functions/Classes:**
  * `child_process$execFileCallback` (Impact: 101.3)
  * `child_process$execCallback` (Impact: 51.9)
  * `isWebAssemblyCompiledModule` (Impact: 42.6)
  * `scryptSync` (Impact: 23.0)
  * `start` (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Sec Tainted Injection (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1020`, `structural_boundaries: 614`, `args: 482`, `func_start: 437`
* *Risk/State:* `safety_bypasses: 577`, `high_risk_execution: 4`, `dead_code: 2`, `planned_debt: 8`, `duplicate_logic: 4`, `unreferenced_by_name: 187`
* *Architecture:* `io: 52`, `api: 17`, `concurrency: 74`
* *Defense:* `safety: 22`, `doc: 45`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1467.36 | **LOC:** 2980 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.3421%), Tech Debt (99.4731%)
**Top Internal Functions/Classes:**
  * `dispatchMouseEvent` (Impact: 11.2)
  * `Child` (Impact: 7.7)
  * `Child2` (Impact: 6.0)
  * `Child` (Impact: 6.0)
  * `Component` (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 119 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 803
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 492`, `args: 265`, `func_start: 131`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 38`, `state_mutation: 204`, `duplicate_logic: 72`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 208`, `import: 10`
* *Defense:* `safety: 3`, `doc: 1`, `test: 215`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` internal-test-utils, react, react-dom, client, server, constants, scheduler, ReactFeatureFlags
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom/src/__tests__/ReactDOMEventPropagation-test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1461.76 | **LOC:** 3015 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (77.7746%), Tech Debt (99.9208%)
**Top Internal Functions/Classes:**
  * `testNativeStopPropagationInInnerEmulatedBubblePhase` (Impact: 6.4)
  * `testNativeStopPropagationInInnerCapturePhase` (Impact: 6.3)
  * `testNativeStopPropagationInOuterCapturePhase` (Impact: 6.2)
  * `testNativeStopPropagationInOuterBubblePhase` (Impact: 6.2)
  * `testReactStopPropagationInInnerBubblePhase` (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 332
* *State Mutation (weighted view):* 499
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 451`, `args: 412`, `func_start: 287`
* *Risk/State:* `state_mutation: 443`, `duplicate_logic: 100`, `unreferenced_by_name: 18`
* *Architecture:* `concurrency: 247`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`, `test: 172`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` internal-test-utils, react, react-dom, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1434.18 | **LOC:** 9641 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (27.1884%), Tech Debt (7.8067%)
**Top Internal Functions/Classes:**
  * `act` (Impact: 41.9)
  * `getMeaningfulChildren` (Impact: 33.6)
  * `readText` (Impact: 14.3)
  * `resolveLoadables` (Impact: 14.2)
  * `requestAnimationFrame` (Impact: 10.7)
    * *Intent:* // The Fizz runtime assumes requestAnimationFrame exists so we need to polyfill it.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 36 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 785
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 459`, `structural_boundaries: 859`, `args: 489`, `func_start: 94`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 10`, `state_mutation: 81`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `concurrency: 635`, `import: 9`
* *Defense:* `safety: 30`, `doc: 6`, `test: 433`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` FizzTestUtils, internal-test-utils, jsdom, react, react-dom, client, server, unstable_mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-devtools-shared/src/backend/fiber/renderer.js` -> Churn: **100.0%** | Cog Load: 60.6848% | Debt: 11.3996%
- `packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js` -> Churn: **88.76%** | Cog Load: 71.1909% | Debt: 14.9235%
- `packages/react-client/src/ReactFlightClient.js` -> Churn: **86.57%** | Cog Load: 66.1086% | Debt: 23.0916%
- `packages/react-server/src/ReactFlightServer.js` -> Churn: **84.2%** | Cog Load: 81.7465% | Debt: 23.1855%
- `packages/react-devtools-shared/src/devtools/store.js` -> Churn: **80.65%** | Cog Load: 82.6728% | Debt: 11.1189%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/react-dom-bindings/src/client/ReactDOMComponent.js` -> **Sebastian Markbåge** (100.0% isolated ownership) | Magnitude: 2903.4
- `compiler/packages/snap/src/minimize.ts` -> **Joseph Savona** (100.0% isolated ownership) | Magnitude: 1681.2
- `packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js` -> **Sebastian "Sebbie" Silbermann** (100.0% isolated ownership) | Magnitude: 1467.36
- `packages/react-devtools-shared/src/__tests__/TimelineProfiler-test.js` -> **Sebastian "Sebbie" Silbermann** (100.0% isolated ownership) | Magnitude: 1131.38
- `packages/react-reconciler/src/__tests__/ReactSuspenseWithNoopRenderer-test.js` -> **dan** (100.0% isolated ownership) | Magnitude: 1122.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react-reconciler/src/ReactFiberReconciler.js` -> **Severity: 0.114** (Bridge: 0.0011 * Flux: 99.8598%)
- `packages/react-reconciler/src/ReactFiberWorkLoop.js` -> **Severity: 0.101** (Bridge: 0.001 * Flux: 99.9506%)
- `packages/react-dom/src/client/ReactDOMClient.js` -> **Severity: 0.075** (Bridge: 0.0018 * Flux: 42.6845%)
- `packages/react-dom/src/client/ReactDOMRoot.js` -> **Severity: 0.075** (Bridge: 0.0008 * Flux: 98.9988%)
- `packages/react-server/src/ReactFlightServer.js` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 99.9736%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `compiler/packages/snap/src/sprout/shared-runtime.ts` -> **Severity: 2388.953** (Blast Radius: 50.995 * Doc Risk: 46.8468%)
- `packages/shared/ReactTypes.js` -> **Severity: 1366.5** (Blast Radius: 13.665 * Doc Risk: 100.0%)
- `packages/react-dom/src/client/ReactDOMClient.js` -> **Severity: 1000.8** (Blast Radius: 10.008 * Doc Risk: 100.0%)
- `compiler/packages/babel-plugin-react-compiler/src/HIR/HIR.ts` -> **Severity: 715.116** (Blast Radius: 7.773 * Doc Risk: 92.0%)
- `packages/react-reconciler/src/ReactInternalTypes.js` -> **Severity: 484.8** (Blast Radius: 4.848 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
