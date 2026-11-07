# ARCHITECTURAL_BRIEF: react
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/facebook/react` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 6484 analyzed artifact(s), 596871 LOC.
- **Load-bearing artifact:** `packages/shared/ReactTypes.js` -- 200 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/react-reconciler/src/ReactFiberWorkLoop.js` -- pulls in 59 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/react-devtools-shared/src/backend/fiber/renderer.js` at magnitude 10169.06 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 6840 |
| Analyzed Artifacts (Scanned) | 6484 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 356 |
| Total LOC | 596871 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 94.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7888 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1374 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.4149 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 387 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 3765 | 523691 | 58.1% |
| MARKDOWN | 1806 | 0 | 27.9% |
| TYPESCRIPT | 518 | 61568 | 8.0% |
| PLAINTEXT | 127 | 2 | 2.0% |
| CSS | 112 | 4332 | 1.7% |
| HTML | 79 | 3116 | 1.2% |
| YAML | 28 | 2746 | 0.4% |
| JSON | 28 | 1213 | 0.4% |
| SHELL | 12 | 195 | 0.2% |
| XML | 9 | 8 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 6482 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Callbacks & Closures Files 13%, Large Core Modules (2) 8%, Parameter Forwarders Files 8%, Declarative / Non-Code 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4543 | 70.1% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1931 | 29.8% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 356*

**Composition by Extension & Reason:**
- `.map`: 68x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.md`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 13951 LOC)
- `.js`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 9 exceeds 500 chars)
- `no_extension`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace'), 1x Unsupported Format (.undeterminable)
- `.lock`: 41x Excluded (Unsupported Extension: '.lock'), 1x Excluded (Machine-Generated Source Code Signature: 1743 LOC), 1x Unsupported Format (.lock)
- `.png`: 33x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12828 LOC)
- `.ico`: 10x Excluded (Explicitly Denied Extension: '.ico')
- `.snap`: 5x Unsupported Format (.snap), 1x Excluded (Unsupported Extension: '.snap')
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')
- `.wasm`: 1x Excluded (Unsupported Extension: '.wasm')
- `.webmanifest`: 1x Excluded (Unsupported Extension: '.webmanifest')
- `.ts`: 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mp4`: 1x Excluded (Explicitly Denied Extension: '.mp4')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.2 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.9 | 31.9 | 49.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.5 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.2 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.3 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 19.2 | 1.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.5 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 653 | 229 | 0 | `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts` |
| cleanup | 538 | 178 | 0 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |
| guards | 22221 | 1575 | 5 | `packages/react-devtools-shared/src/backend/fiber/renderer.js` |
| danger | 11907 | 1308 | 3 | `flow-typed/environments/node.js` |
| concurrency | 22557 | 752 | 2 | `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` |
| connectivity | 12107 | 3312 | 3 | `packages/react-reconciler/src/forks/ReactFiberConfig.custom.js` |
| io | 1718 | 311 | 0 | `compiler/packages/snap/src/minimize.ts` |
| crypto | 6 | 6 | 0 | `compiler/packages/babel-plugin-react-compiler/scripts/build-react-hooks-fixures.js` |
| ipc | 159 | 64 | 0 | `flow-typed/environments/node.js` |
| time | 543 | 175 | 0 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |
| serialization | 331 | 127 | 0 | `packages/react-reconciler/src/__tests__/ReactIncremental-test.js` |
| regex | 467 | 187 | 0 | `packages/react-devtools-timeline/src/import-worker/preprocessData.js` |
| events | 5279 | 594 | 0 | `compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts` |
| tests | 24145 | 467 | 0 | `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` |
| docs | 4114 | 2126 | 1 | `packages/react-devtools-extensions/flow-typed/jest.js` |
| debt | 9075 | 1005 | 2 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |
| mutation | 116154 | 3952 | 32 | `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` |
| dead_code | 1736 | 828 | 1 | `flow-typed/environments/node.js` |
| credential | 13 | 8 | 0 | `packages/react-devtools-shared/src/__tests__/utils-test.js` |
| threat | 28 | 12 | 0 | `packages/react-devtools-shared/src/hooks/__tests__/updateMockSourceMaps.js` |
| ml_ai | 61 | 30 | 0 | `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/InferReactiveScopeVariables.ts` |
| ui | 34770 | 2361 | 6 | `packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js` |

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

1. **ReactTypes.js** (`packages/shared/ReactTypes.js`) — 200 inbound connections
2. **client.js** (`packages/react-dom/client.js`) — 195 inbound connections
3. **ReactFeatureFlags.js** (`packages/shared/ReactFeatureFlags.js`) — 119 inbound connections
4. **ReactInternalTypes.js** (`packages/react-reconciler/src/ReactInternalTypes.js`) — 105 inbound connections
5. **CompilerError.ts** (`compiler/packages/babel-plugin-react-compiler/src/CompilerError.ts`) — 88 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ReactFiberWorkLoop.js** (`packages/react-reconciler/src/ReactFiberWorkLoop.js`) — 59 outbound dependencies
2. **ReactFiberBeginWork.js** (`packages/react-reconciler/src/ReactFiberBeginWork.js`) — 45 outbound dependencies
3. **ReactFiberConfigDOM.js** (`packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js`) — 42 outbound dependencies
4. **Pipeline.ts** (`compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Pipeline.ts`) — 38 outbound dependencies
5. **ReactFiberHooks.js** (`packages/react-reconciler/src/ReactFiberHooks.js`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `attach` **(Many-Argument Workhorses)** (@ `packages/react-devtools-shared/src/backend/fiber/renderer.js`) -> Impact: **4853.6** | LOC: 7750
- `visitFunctionWithDependencies` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin-react-hooks/src/rules/ExhaustiveDeps.ts`) -> Impact: **708.1** | LOC: 1144
  * *Intent:* /** * Visitor for both function expressions and arrow function expressions. */
- `setProp` **(Many-Argument Workhorses)** (@ `packages/react-dom-bindings/src/client/ReactDOMComponent.js`) -> Impact: **572.3** | LOC: 599
- `createChildReconciler` **(Many-Argument Workhorses)** (@ `packages/react-reconciler/src/ReactChildFiber.js`) -> Impact: **510.7** | LOC: 1672
  * *Intent:* // This wrapper function exists because I expect to clone the code in each path // to be able to optimize each path individually by branching early. T...
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin-react-hooks/src/rules/ExhaustiveDeps.ts`) -> Impact: **509.6** | LOC: 1453
- `lowerStatement` **(Many-Argument Workhorses)** (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **487.0** | LOC: 1300
  * *Intent:* // Helper to lower a statement
- `completeWork` **(Many-Argument Workhorses)** (@ `packages/react-reconciler/src/ReactFiberCompleteWork.js`) -> Impact: **446.6** | LOC: 1012
- `commitMutationEffectsOnFiber` **(Many-Argument Workhorses)** (@ `packages/react-reconciler/src/ReactFiberCommitWork.js`) -> Impact: **413.4** | LOC: 707
- `updateProperties` **(Many-Argument Workhorses)** (@ `packages/react-dom-bindings/src/client/ReactDOMComponent.js`) -> Impact: **398.7** | LOC: 506
- `lowerExpression` **(Many-Argument Workhorses)** (@ `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts`) -> Impact: **392.0** | LOC: 1189

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/react-dom/src/__tests__` | 129 | 31741.1 | 44.52% | 46.64% |
| `packages/react-reconciler/src` | 81 | 27635.72 | 30.44% | 21.52% |
| `packages/react-reconciler/src/__tests__` | 76 | 18776.22 | 56.19% | 63.87% |
| `packages/react-server/src` | 37 | 12392.06 | 35.37% | 13.6% |
| `packages/react-devtools-shared/src/backend/fiber` | 2 | 10326.48 | 69.25% | 10.52% |
| `packages/react-dom-bindings/src/client` | 28 | 9811.64 | 24.33% | 5.83% |
| `compiler/packages/babel-plugin-react-compiler/src/HIR` | 28 | 7505.9 | 19.59% | 6.5% |
| `packages/react-devtools-shared/src/__tests__` | 34 | 6853.02 | 27.22% | 59.42% |
| `packages/react-dom-bindings/src/server` | 7 | 5576.18 | 25.73% | 4.06% |
| `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes` | 30 | 5312.74 | 29.54% | 2.31% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/todo.bail.rules-of-hooks-e0a5db3ae21e.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/rules-of-hooks/todo.bail.rules-of-hooks-fadd52c1e460.js` -> **100.0%** Exposure
- `packages/react-client/src/forks/ReactFlightClientConfig.markup.js` -> **100.0%** Exposure
- `packages/react-dom/src/__tests__/ReactComponentLifeCycle-test.js` -> **100.0%** Exposure
- `packages/react-dom/src/__tests__/ReactDOMFizzShellHydration-test.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/conditional-early-return.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/conditional-early-return.js` -> **100.0%** Exposure
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/sequentially-constant-progagatable-if-test-conditions.js` -> **100.0%** Exposure
- `fixtures/concurrent/time-slicing/src/Clock.js` -> **100.0%** Exposure
- `fixtures/dom/src/components/Fixture.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `flow-typed/environments/node.js` -> **187** Orphaned Functions | **4** Duplicates
- `packages/react-refresh/src/__tests__/ReactFresh-test.js` -> **1** Orphaned Functions | **124** Duplicates
- `packages/react-dom/src/__tests__/ReactDOMEventPropagation-test.js` -> **3** Orphaned Functions | **115** Duplicates
- `packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js` -> **1** Orphaned Functions | **109** Duplicates
- `packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMBrowser-test.js` -> **1** Orphaned Functions | **108** Duplicates

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
- **Binary Anomalies (X-Ray):** `82` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6060` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/react-devtools-shared/src/backend/fiber/renderer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.519)
- **Top Global Matches:** file_cluster_6: 9.519, file_cluster_8: 14.512, file_cluster_4: 14.734
- **Magnitude:** 10169.06 | **LOC:** 8154 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 63.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.125; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Guard Balance (formerly Safety Score) (53.1%)
- **Documentation Coverage:** 98.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `attach` **(Many-Argument Workhorses)** (Impact: 4853.6)
  * `updateFiberRecursively` **(Many-Argument Workhorses)** (Impact: 359.9)
    * *Intent:* // Returns whether closest unfiltered fiber parent needs to reset its child list.
  * `mountFiberRecursively` **(Many-Argument Workhorses)** (Impact: 156.0)
  * `updateVirtualChildrenRecursively` **(Many-Argument Workhorses)** (Impact: 139.2)
  * `inspectFiberInstanceRaw` **(Defensive Guards)** (Impact: 129.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 554 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 1768
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1597`, `structural_boundaries: 683`, `args: 193`, `func_start: 169`
* *Risk/State:* `safety_bypasses: 156`, `state_mutation: 660`, `planned_debt: 36`, `fragile_debt: 7`
* *Architecture:* `api: 5`, `concurrency: 8`, `import: 30`
* *Defense:* `safety: 917`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.125
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.00037
  * `Imports (Out-Degree: 22):` constants, utils, profilingHooks, DevToolsOwnerStack, DevToolsServerComponentLogs, ReactSymbols, types, utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-dom-bindings/src/server/ReactFizzConfigDOM.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.972)
- **Top Global Matches:** file_cluster_6: 7.972, file_cluster_8: 13.012, file_cluster_4: 14.161
- **Magnitude:** 5053.94 | **LOC:** 7160 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **26**; blast radius 0.655; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.8%), Guard Balance (formerly Safety Score) (58.2%)
- **Documentation Coverage:** 99.1071% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 263.8)
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 193.6)
  * `pushLink` **(Many-Argument Workhorses)** (Impact: 147.3)
  * `pushImg` **(Many-Argument Workhorses)** (Impact: 140.4)
  * `createRenderState` **(Many-Argument Workhorses)** (Impact: 124.2)
    * *Intent:* // Allows us to keep track of what we've already written so we can refer back to it. // if passed ex...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 409 instances
* *High Risk Execution (weighted view):* 16
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 1321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1361`, `structural_boundaries: 610`, `args: 155`, `func_start: 147`
* *Risk/State:* `safety_bypasses: 143`, `high_risk_execution: 35`, `state_mutation: 503`, `planned_debt: 24`, `fragile_debt: 9`
* *Architecture:* `api: 64`, `concurrency: 10`, `import: 28`
* *Defense:* `safety: 451`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.655
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.005082
  * `Imports (Out-Degree: 24):` ReactControlledValuePropTypes, ReactDOMFormActions, ReactDOMInvalidARIAHook, ReactDOMNullInputValuePropHook, ReactDOMResourceValidation, ReactDOMUnknownPropertyHook, crossOriginStrings, getAttributeAlias...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `fixtures/fiber-debugger/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/nesting/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-server/src/ReactFlightServer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.808)
- **Top Global Matches:** file_cluster_4: 8.808, file_cluster_6: 9.835, file_cluster_12: 13.999
- **Magnitude:** 4480.8 | **LOC:** 6445 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 41.7%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **23**; blast radius 2.106; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.8%), Connectivity (formerly Api Exposure) (59.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderModelDestructive` **(Many-Argument Workhorses)** (Impact: 383.5)
  * `renderDebugModel` **(Many-Argument Workhorses)** (Impact: 290.5)
    * *Intent:* // This is a forked version of renderModel which should never error, never suspend and is limited //...
  * `visitAsyncNodeImpl` **(Many-Argument Workhorses)** (Impact: 179.1)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 100.8)
  * `serializeAsyncIterable` **(Many-Argument Workhorses)** (Impact: 85.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 424 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 1371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1088`, `structural_boundaries: 589`, `args: 202`, `func_start: 163`
* *Risk/State:* `safety_bypasses: 142`, `state_mutation: 523`, `planned_debt: 33`, `fragile_debt: 15`, `duplicate_logic: 2`
* *Architecture:* `api: 18`, `concurrency: 42`, `import: 29`
* *Defense:* `safety: 638`, `doc: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.106
  * `Choke Point (Betweenness):` 0.000206 | `Ripple Effect (Closeness):` 0.006778
  * `Imports (Out-Degree: 22):` ReactFlightAsyncSequence, ReactFlightCallUserSpace, ReactFlightHooks, ReactFlightServerConfig, ReactFlightServerTemporaryReferences, ReactFlightThenable, ReactServerStreamConfig, ReactSharedInternalsServer...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.75)
- **Top Global Matches:** file_cluster_4: 8.75, file_cluster_12: 11.101, file_cluster_6: 12.543
- **Magnitude:** 4293.14 | **LOC:** 6652 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 38.5%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **42**; blast radius 0.346; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Connectivity (formerly Api Exposure) (86.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.7573% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isHostHoistableType` **(Many-Argument Workhorses)** (Impact: 136.8)
  * `canHydrateInstance` **(Many-Argument Workhorses)** (Impact: 116.8)
  * `animateGesture` **(Many-Argument Workhorses)** (Impact: 94.5)
  * `hydrateHoistable` **(Many-Argument Workhorses)** (Impact: 88.5)
  * `getResource` **(Many-Argument Workhorses)** (Impact: 84.7)
    * *Intent:* // This function is called in begin work and we should always have a currentDocument set
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 322 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 106
* *State Mutation (weighted view):* 1066
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1265`, `structural_boundaries: 774`, `args: 287`, `func_start: 266`
* *Risk/State:* `safety_bypasses: 199`, `high_risk_execution: 7`, `state_mutation: 422`, `dead_code: 1`, `planned_debt: 36`, `fragile_debt: 15`
* *Architecture:* `api: 187`, `concurrency: 51`, `import: 43`
* *Defense:* `safety: 552`, `doc: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.346
  * `Choke Point (Betweenness):` 0.000211 | `Ripple Effect (Closeness):` 0.008154
  * `Imports (Out-Degree: 40):` DOMEventNames, DOMPluginEventSystem, ReactDOMEventListener, ReactDOMEventReplaying, ReactDOMFormActions, ReactDOMResourceValidation, DOMAccessibilityRoles, DOMNamespaces...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `packages/react-server/src/ReactFizzServer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.514)
- **Top Global Matches:** file_cluster_4: 8.514, file_cluster_6: 8.806, file_cluster_12: 13.931
- **Magnitude:** 4020.04 | **LOC:** 6256 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **24**; blast radius 1.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.1%), Connectivity (formerly Api Exposure) (59.2%), Guard Balance (formerly Safety Score) (58.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finishedTask` **(Many-Argument Workhorses)** (Impact: 102.9)
  * `retryNode` **(Many-Argument Workhorses)** (Impact: 99.1)
  * `renderSuspenseListRows` **(Many-Argument Workhorses)** (Impact: 94.9)
  * `abortTask` **(Many-Argument Workhorses)** (Impact: 88.5)
  * `renderSuspenseBoundary` **(Many-Argument Workhorses)** (Impact: 85.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 477 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 1563
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 849`, `structural_boundaries: 345`, `args: 155`, `func_start: 127`
* *Risk/State:* `safety_bypasses: 139`, `state_mutation: 609`, `dead_code: 1`, `planned_debt: 23`, `fragile_debt: 16`, `duplicate_logic: 4`
* *Architecture:* `api: 23`, `concurrency: 4`, `import: 31`
* *Defense:* `safety: 545`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.186
  * `Choke Point (Betweenness):` 0.000131 | `Ripple Effect (Closeness):` 0.005846
  * `Imports (Out-Degree: 23):` ReactFizzAsyncDispatcher, ReactFizzCallUserSpace, ReactFizzClassComponent, ReactFizzComponentStack, ReactFizzConfig, ReactFizzCurrentTask, ReactFizzHooks, ReactFizzLegacyContext...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `packages/react-client/src/ReactFlightClient.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.854)
- **Top Global Matches:** file_cluster_6: 8.854, file_cluster_4: 8.969, file_cluster_12: 14.348
- **Magnitude:** 3312.44 | **LOC:** 5407 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 53.8%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **19**; blast radius 0.786; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.7%)
- **Documentation Coverage:** 99.2754% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` **(Many-Argument Workhorses)** (Impact: 151.0)
  * `fulfillReference` **(Many-Argument Workhorses)** (Impact: 144.5)
  * `parseModelString` **(Many-Argument Workhorses)** (Impact: 139.6)
  * `processBinaryChunk` **(Many-Argument Workhorses)** (Impact: 100.2)
  * `processStringChunk` **(Many-Argument Workhorses)** (Impact: 93.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 424 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 128
* *State Mutation (weighted view):* 1312
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 951`, `structural_boundaries: 463`, `args: 157`, `func_start: 108`
* *Risk/State:* `safety_bypasses: 135`, `high_risk_execution: 5`, `state_mutation: 464`, `planned_debt: 27`, `fragile_debt: 13`, `duplicate_logic: 2`
* *Architecture:* `api: 14`, `concurrency: 28`, `import: 22`
* *Defense:* `safety: 394`, `doc: 2`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.786
  * `Choke Point (Betweenness):` 7.5e-05 | `Ripple Effect (Closeness):` 0.002932
  * `Imports (Out-Degree: 17):` ReactFlightClientConfig, ReactFlightClientDevToolsHook, ReactFlightPerformanceTrack, ReactFlightReplyClient, ReactFlightTemporaryReferences, react, ReactFlightServerConfig, ReactLazy...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberCommitWork.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_8: 6.727, file_cluster_6: 11.28, file_cluster_4: 19.811
- **Magnitude:** 3214.9 | **LOC:** 5350 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **30**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `commitMutationEffectsOnFiber` **(Many-Argument Workhorses)** (Impact: 413.4)
  * `commitPassiveMountOnFiber` **(Many-Argument Workhorses)** (Impact: 378.4)
  * `commitLayoutEffectOnFiber` **(Many-Argument Workhorses)** (Impact: 190.7)
  * `commitDeletionEffectsOnFiber` **(Many-Argument Workhorses)** (Impact: 153.3)
  * `reconnectPassiveEffects` **(Many-Argument Workhorses)** (Impact: 119.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 558
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1098`, `structural_boundaries: 329`, `args: 79`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 206`, `dead_code: 2`, `planned_debt: 72`, `fragile_debt: 6`
* *Architecture:* `api: 16`, `concurrency: 1`, `import: 39`
* *Defense:* `safety: 336`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.022803
  * `Imports (Out-Degree: 30):` ReactFiberActivityComponent, ReactFiberCacheComponent, ReactFiberClassUpdateQueue, ReactFiberCommitEffects, ReactFiberCommitHostEffects, ReactFiberCommitViewTransitions, ReactFiberConfig, ReactFiberDevToolsHook...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberWorkLoop.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.122)
- **Top Global Matches:** file_cluster_4: 7.122, file_cluster_6: 8.594, file_cluster_12: 13.356
- **Magnitude:** 3061.62 | **LOC:** 5622 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **59**; blast radius 0.666; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (81.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.4%)
- **Documentation Coverage:** 98.4375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `completeRoot` **(Many-Argument Workhorses)** (Impact: 162.7)
  * `commitRoot` **(Many-Argument Workhorses)** (Impact: 117.4)
  * `renderRootConcurrent` **(Many-Argument Workhorses)** (Impact: 100.4)
  * `prepareFreshStack` **(Many-Argument Workhorses)** (Impact: 98.4)
  * `performWorkOnRoot` **(Many-Argument Workhorses)** (Impact: 93.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 314 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1042
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 826`, `structural_boundaries: 415`, `args: 141`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 414`, `planned_debt: 48`, `fragile_debt: 8`
* *Architecture:* `api: 68`, `concurrency: 2`, `import: 65`
* *Defense:* `safety: 342`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.666
  * `Choke Point (Betweenness):` 0.000825 | `Ripple Effect (Closeness):` 0.027717
  * `Imports (Out-Degree: 58):` ReactCapturedValue, ReactChildFiber, ReactCurrentFiber, ReactEventPriorities, ReactFiber, ReactFiberAct, ReactFiberActivityComponent, ReactFiberApplyGesture...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `packages/react-dom-bindings/src/client/ReactDOMComponent.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.538)
- **Top Global Matches:** file_cluster_8: 12.538, file_cluster_3: 14.79, file_cluster_6: 24.175
- **Magnitude:** 2843.7 | **LOC:** 3380 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **25**; blast radius 0.188; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.4%), Guard Balance (formerly Safety Score) (51.0%), Connectivity (formerly Api Exposure) (34.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setProp` **(Many-Argument Workhorses)** (Impact: 572.3)
  * `updateProperties` **(Many-Argument Workhorses)** (Impact: 398.7)
  * `diffHydratedGenericElement` **(Many-Argument Workhorses)** (Impact: 354.7)
  * `setInitialProperties` **(Many-Argument Workhorses)** (Impact: 233.3)
  * `setPropOnCustomElement` **(Many-Argument Workhorses)** (Impact: 111.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Cascading Flux:* 85 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 951`, `structural_boundaries: 371`, `args: 36`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 107`, `high_risk_execution: 25`, `state_mutation: 90`, `planned_debt: 38`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 27`
* *Defense:* `safety: 288`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.188
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.006745
  * `Imports (Out-Degree: 25):` DOMPluginEventSystem, EventRegistry, ReactControlledValuePropTypes, ReactDOMInvalidARIAHook, ReactDOMNullInputValuePropHook, ReactDOMUnknownPropertyHook, getAttributeAlias, isCustomElement...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 10.791)
- **Top Global Matches:** file_cluster_10: 10.791, file_cluster_12: 11.136, file_cluster_15: 11.156
- **Magnitude:** 2831.74 | **LOC:** 9605 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `act` **(Compute Cores)** (Impact: 41.8)
  * `expectErrors` **(Compute Cores)** (Impact: 14.8)
  * `readText` **(Defensive Guards)** (Impact: 14.3)
  * `rejectText` **(Defensive Guards)** (Impact: 7.7)
  * `resolveText` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 186 instances
* *Amplified Cascading Flux:* 55 instances
* *High Risk Execution (weighted view):* 10
* *Concurrency (weighted view):* 1662
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 1534`, `args: 1008`, `func_start: 433`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 12`, `state_mutation: 289`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 7`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 732`, `import: 13`
* *Defense:* `safety: 52`, `doc: 1`, `test: 629`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` FizzTestUtils, immutable, internal-test-utils, jsdom, prop-types, react, react-dom, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-reconciler/src/ReactFiberBeginWork.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.596)
- **Top Global Matches:** file_cluster_6: 5.596, file_cluster_4: 10.582, file_cluster_8: 14.594
- **Magnitude:** 2379.84 | **LOC:** 4449 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **45**; blast radius 0.13; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `beginWork` **(Many-Argument Workhorses)** (Impact: 126.2)
  * `updateDehydratedSuspenseComponent` **(Many-Argument Workhorses)** (Impact: 101.3)
  * `attemptEarlyBailoutIfNoScheduledUpdate` **(Many-Argument Workhorses)** (Impact: 93.3)
  * `updateSuspenseComponent` **(Many-Argument Workhorses)** (Impact: 81.2)
  * `updateOffscreenComponent` **(Many-Argument Workhorses)** (Impact: 76.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 234 instances
* *State Mutation (weighted view):* 773
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 308`, `args: 71`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 305`, `planned_debt: 25`, `fragile_debt: 8`
* *Architecture:* `api: 7`, `import: 54`
* *Defense:* `safety: 218`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.000105 | `Ripple Effect (Closeness):` 0.022832
  * `Imports (Out-Degree: 44):` ReactCapturedValue, ReactChildFiber, ReactCurrentFiber, ReactFiber, ReactFiberActivityComponent, ReactFiberCacheComponent, ReactFiberCallUserSpace, ReactFiberClassComponent...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.391)
- **Top Global Matches:** file_cluster_6: 6.391, file_cluster_8: 12.392, file_cluster_4: 13.025
- **Magnitude:** 2239.14 | **LOC:** 4556 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.341; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.2%), Guard Balance (formerly Safety Score) (48.8%)
- **Documentation Coverage:** 97.9167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lowerStatement` **(Many-Argument Workhorses)** (Impact: 487.0)
    * *Intent:* // Helper to lower a statement
  * `lowerExpression` **(Many-Argument Workhorses)** (Impact: 392.0)
  * `lowerAssignment` **(Many-Argument Workhorses)** (Impact: 328.3)
  * `isReorderableExpression` **(Many-Argument Workhorses)** (Impact: 98.5)
  * `lower` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* * ************************************* Lowering to HIR ************************************* * ****...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 106 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 745`, `structural_boundaries: 425`, `args: 90`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 113`, `planned_debt: 59`, `fragile_debt: 2`
* *Architecture:* `io: 56`, `api: 8`, `concurrency: 4`, `import: 9`
* *Defense:* `safety: 224`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.008478
  * `Imports (Out-Degree: 7):` &&
        expr.node.property.name ===, CompilerError, utils, Environment, HIR, HIRBuilder, ObjectShape, traverse...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactChildFiber.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_6: 8.644, file_cluster_8: 9.346, file_cluster_4: 16.609
- **Magnitude:** 2142.98 | **LOC:** 2253 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 0.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.0%), Guard Balance (formerly Safety Score) (52.6%), Connectivity (formerly Api Exposure) (32.2%)
- **Documentation Coverage:** 97.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createChildReconciler` **(Many-Argument Workhorses)** (Impact: 510.7)
    * *Intent:* // This wrapper function exists because I expect to clone the code in each path // to be able to opt...
  * `reconcileChildrenIterator` **(Many-Argument Workhorses)** (Impact: 91.7)
  * `reconcileChildrenArray` **(Many-Argument Workhorses)** (Impact: 87.9)
  * `updateFromMap` **(Many-Argument Workhorses)** (Impact: 86.0)
  * `updateSlot` **(Many-Argument Workhorses)** (Impact: 67.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 215`, `args: 47`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 193`, `planned_debt: 14`, `fragile_debt: 2`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 256`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.022818
  * `Imports (Out-Degree: 17):` ReactCurrentFiber, ReactFiber, ReactFiberFlags, ReactFiberHotReloading, ReactFiberHydrationContext, ReactFiberLane, ReactFiberNewContext, ReactFiberThenable...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin-react-hooks/src/rules/ExhaustiveDeps.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.378)
- **Top Global Matches:** file_cluster_8: 5.378, file_cluster_6: 15.199, file_cluster_3: 21.545
- **Magnitude:** 2116.7 | **LOC:** 2139 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.206; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.2%), Complexity Load (formerly Cognitive Load) (51.3%)
- **Documentation Coverage:** 87.1795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitFunctionWithDependencies` **(Many-Argument Workhorses)** (Impact: 708.1)
    * *Intent:* /** * Visitor for both function expressions and arrow function expressions. */
  * `create` **(Many-Argument Workhorses)** (Impact: 509.6)
  * `isStableKnownHookValue` **(Compute Cores)** (Impact: 81.9)
    * *Intent:* // tell if some values don't have to be declared as deps. // Some are known to be stable based on Ho...
  * `visitCallExpression` **(Compute Cores)** (Impact: 76.5)
  * `gatherDependenciesRecursively` **(Compute Cores)** (Impact: 47.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 325`, `args: 72`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 88`, `dead_code: 7`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `api: 2`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 26`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.206
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000274
  * `Imports (Out-Degree: 1):` Utils, eslint, estree
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.626)
- **Top Global Matches:** file_cluster_10: 7.626, file_cluster_15: 8.395, file_cluster_11: 8.411
- **Magnitude:** 2060.5 | **LOC:** 4231 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (89.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchMouseEvent` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `Child` **(Defensive Guards)** (Impact: 7.7)
  * `Sibling` **(Compute Cores)** (Impact: 6.0)
  * `Component` **(Compute Cores)** (Impact: 5.1)
  * `Component` **(Compute Cores)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 172 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 1162
* *State Mutation (weighted view):* 301
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 683`, `args: 389`, `func_start: 200`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 60`, `state_mutation: 273`, `fragile_debt: 2`, `duplicate_logic: 109`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 302`, `import: 10`
* *Defense:* `safety: 4`, `doc: 1`, `test: 312`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` internal-test-utils, react, react-dom, client, server, constants, scheduler, ReactFeatureFlags
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/packages/babel-plugin-react-compiler/src/Inference/InferMutationAliasingEffects.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.075)
- **Top Global Matches:** file_cluster_8: 6.075, file_cluster_6: 13.592, file_cluster_4: 22.195
- **Magnitude:** 2051.22 | **LOC:** 2976 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 71.4%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 0.183; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.3%), Complexity Load (formerly Cognitive Load) (62.6%)
- **Documentation Coverage:** 35.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyEffect` **(Many-Argument Workhorses)** (Impact: 347.8)
  * `computeSignatureForInstruction` **(Many-Argument Workhorses)** (Impact: 223.1)
    * *Intent:* /** * Computes an effect signature for the instruction _without_ looking at the inference state, * a...
  * `computeEffectsForSignature` **(Many-Argument Workhorses)** (Impact: 202.0)
  * `computeEffectsForLegacySignature` **(Many-Argument Workhorses)** (Impact: 99.1)
    * *Intent:* /** * Creates a set of aliasing effects given a legacy FunctionSignature. This makes all of the * ol...
  * `findNonMutatedDestructureSpreads` **(Compute Cores)** (Impact: 67.5)
    * *Intent:* * The primary use case for this is props spreading: * * ``` * function Component({prop, ...otherProp...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 532
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 227`, `args: 55`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 194`, `planned_debt: 8`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 6`, `import: 10`
* *Defense:* `safety: 53`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.183
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.00503
  * `Imports (Out-Degree: 10):` .., CompilerError, HIR, HIRBuilder, ObjectShape, PrintHIR, visitors, utils...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `compiler/packages/snap/src/minimize.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.171)
- **Top Global Matches:** file_cluster_4: 6.171, file_cluster_9: 9.853, file_cluster_15: 10.272
- **Magnitude:** 1668.9 | **LOC:** 2143 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.119; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.3%), Complexity Load (formerly Cognitive Load) (55.3%)
- **Documentation Coverage:** 50.9615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simplifyForStatements` **(Compute Cores)** (Impact: 37.6)
    * *Intent:* /** * Generator that simplifies for statements: * - Replace with init (if expression) * - Replace wi...
  * `simplifyCallExpressions` **(Compute Cores)** (Impact: 34.0)
    * *Intent:* /** * Generator that simplifies call expressions by replacing them with their arguments. * For singl...
  * `simplifySinglePropertyObjects` **(Compute Cores)** (Impact: 28.6)
    * *Intent:* /** * Generator that replaces single-property objects with the property value. * For regular propert...
  * `minimize` **(Many-Argument Workhorses)** (Impact: 27.3)
    * *Intent:* /** * Core minimization loop that attempts to reduce the input source code * while preserving the co...
  * `simplifyForInStatements` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* /** * Generator that simplifies for-in statements: * - Replace with left (variable declaration or ex...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 668
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 385`, `structural_boundaries: 149`, `args: 98`, `func_start: 84`
* *Risk/State:* `state_mutation: 228`
* *Architecture:* `io: 150`, `api: 8`, `import: 9`
* *Defense:* `safety: 8`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000154
  * `Imports (Out-Degree: 3):` compiler.js, constants.js, core, generator, traverse, types, TestUtils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-reconciler/src/ReactFiberHooks.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.106)
- **Top Global Matches:** file_cluster_12: 8.106, file_cluster_7: 8.174, file_cluster_5: 9.955
- **Magnitude:** 1532.86 | **LOC:** 5238 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **34**; blast radius 0.351; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%), Guard Balance (formerly Safety Score) (66.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useMemoCache` **(Defensive Guards)** (Impact: 28.2)
  * `areHookInputsEqual` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `updateWorkInProgressHook` **(I/O & Config Routines)** (Impact: 17.5)
  * `warnOnHookMismatchInDev` **(Compute Cores)** (Impact: 12.2)
  * `requestFormReset` **(I/O & Config Routines)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 325 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 1139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 504`, `structural_boundaries: 680`, `args: 330`, `func_start: 186`
* *Risk/State:* `safety_bypasses: 293`, `state_mutation: 489`, `dead_code: 8`, `planned_debt: 25`, `fragile_debt: 9`, `duplicate_logic: 17`
* *Architecture:* `api: 16`, `concurrency: 6`, `import: 40`
* *Defense:* `safety: 297`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.351
  * `Choke Point (Betweenness):` 0.000149 | `Ripple Effect (Closeness):` 0.027553
  * `Imports (Out-Degree: 33):` ReactEventPriorities, ReactFiberAsyncAction, ReactFiberBeginWork, ReactFiberCacheComponent, ReactFiberCallUserSpace, ReactFiberClassUpdateQueue, ReactFiberConcurrentUpdates, ReactFiberConfig...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.453)
- **Top Global Matches:** file_cluster_10: 7.453, file_cluster_15: 8.191, file_cluster_11: 8.312
- **Magnitude:** 1450.26 | **LOC:** 2980 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Complexity Load (formerly Cognitive Load) (88.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchMouseEvent` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `Child` **(Defensive Guards)** (Impact: 7.7)
  * `Child2` **(Compute Cores)** (Impact: 6.0)
  * `Child` **(Defensive Guards)** (Impact: 6.0)
  * `Component` **(Compute Cores)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 119 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 803
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 492`, `args: 265`, `func_start: 131`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 38`, `state_mutation: 204`, `duplicate_logic: 72`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 208`, `import: 10`
* *Defense:* `safety: 3`, `doc: 1`, `test: 215`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` internal-test-utils, react, react-dom, client, server, constants, scheduler, ReactFeatureFlags
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dom/src/__tests__/ReactDOMEventPropagation-test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.145)
- **Top Global Matches:** file_cluster_10: 6.145, file_cluster_15: 8.96, file_cluster_2: 9.217
- **Magnitude:** 1405.36 | **LOC:** 3015 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testNativeStopPropagationInInnerEmulatedBubblePhase` **(Callbacks & Closures)** (Impact: 6.4)
  * `testNativeStopPropagationInInnerCapturePhase` **(Callbacks & Closures)** (Impact: 6.3)
  * `testNativeStopPropagationInOuterCapturePhase` **(Callbacks & Closures)** (Impact: 6.2)
  * `testNativeStopPropagationInOuterBubblePhase` **(Callbacks & Closures)** (Impact: 6.2)
  * `testReactStopPropagationInInnerBubblePhase` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 332
* *State Mutation (weighted view):* 483
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 451`, `args: 412`, `func_start: 287`
* *Risk/State:* `state_mutation: 443`, `duplicate_logic: 115`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 247`, `import: 5`
* *Defense:* `safety: 1`, `doc: 1`, `test: 172`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` internal-test-utils, react, react-dom, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.774)
- **Top Global Matches:** file_cluster_6: 5.774, file_cluster_4: 8.011, file_cluster_15: 16.068
- **Magnitude:** 1389.66 | **LOC:** 2480 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 0.159; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.8%), Guard Balance (formerly Safety Score) (58.4%)
- **Documentation Coverage:** 95.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `codegenInstructionValue` **(Many-Argument Workhorses)** (Impact: 244.2)
  * `codegenTerminal` **(Many-Argument Workhorses)** (Impact: 122.4)
  * `codegenInstructionNullable` **(Many-Argument Workhorses)** (Impact: 82.2)
  * `codegenFunction` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `codegenReactiveScope` **(Many-Argument Workhorses)** (Impact: 35.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 131 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 297`, `args: 70`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 156`, `planned_debt: 9`, `fragile_debt: 3`
* *Architecture:* `io: 13`, `api: 6`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 30`, `doc: 9`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.159
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.005196
  * `Imports (Out-Degree: 13):` , CompilerError, Entrypoint, HIR, Environment, HIR, PrintHIR, visitors...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/react-dom/src/__tests__/ReactDOMFloat-test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.946)
- **Top Global Matches:** file_cluster_12: 7.946, file_cluster_15: 8.959, file_cluster_10: 9.054
- **Magnitude:** 1387.38 | **LOC:** 9641 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.106; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `act` **(Compute Cores)** (Impact: 41.9)
  * `getMeaningfulChildren` **(Defensive Guards)** (Impact: 33.6)
  * `readText` **(Defensive Guards)** (Impact: 14.3)
  * `resolveLoadables` **(Many-Argument Workhorses)** (Impact: 14.2)
  * `resolveText` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 34 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 775
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 859`, `args: 489`, `func_start: 94`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 10`, `state_mutation: 81`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `concurrency: 635`, `import: 9`
* *Defense:* `safety: 30`, `doc: 6`, `test: 433`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` FizzTestUtils, internal-test-utils, jsdom, react, react-dom, client, server, unstable_mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/bench/benchmarks/pe-functional-components/benchmark.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.338)
- **Top Global Matches:** file_cluster_10: 8.338, file_cluster_15: 9.386, file_cluster_4: 9.499
- **Magnitude:** 1386.18 | **LOC:** 5180 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (64.7%), Guard Balance (formerly Safety Score) (40.2%), Connectivity (formerly Api Exposure) (17.4%), Mutation Surface (formerly State Flux) (8.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TransitionCell142` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `FixedDataTableCell143` **(Defensive Guards)** (Impact: 66.1)
  * `ReactImage0` **(Defensive Guards)** (Impact: 58.2)
  * `AbstractButton3` **(Defensive Guards)** (Impact: 55.2)
  * `AdsPETableHeader141` **(Defensive Guards)** (Impact: 52.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 498`, `structural_boundaries: 684`, `args: 280`, `func_start: 248`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 62`
* *Architecture:* `api: 2`
* *Defense:* `safety: 498`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/jsx-outlining-separate-nested.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, args: 7, func_start: 6
- `fixtures/dom/src/components/fixtures/event-pooling/mouse-move.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 8, branch: 6, ui_framework: 6
- `packages/react-devtools-shell/src/app/index.js` (JAVASCRIPT) | Magnitude: 20.62 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 30, import: 20, args: 13
- `packages/react-reconciler/src/__tests__/ReactClassComponentPropResolution-test.js` (JAVASCRIPT) | Magnitude: 43.76 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 23, args: 17, func_start: 11
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/jsx-outlining-dupe-attr-after-rename.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 8, args: 6, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/react/src/__tests__/ReactContextValidator-test.js` (JAVASCRIPT) | Magnitude: 153.9 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 557, structural_boundaries: 175, args: 82, core_var_decl: 82
- `packages/react-art/src/ReactART.js` (JAVASCRIPT) | Magnitude: 56.72 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 29, core_var_decl: 18, args: 17
- `packages/react-reconciler/src/__tests__/ReactPersistent-test.js` (JAVASCRIPT) | Magnitude: 61.6 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 173, structural_boundaries: 46, ui_framework: 32, test: 30
- `.github/workflows/runtime_build_and_test.yml` (YAML) | Magnitude: 167.0 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 829, args: 183, branch: 123, func_start: 85
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/jsx-outlining-with-non-jsx-children.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 8, args: 6, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/react-reconciler/src/ReactProfilerTimer.js` (JAVASCRIPT) | Magnitude: 730.52 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 394, structural_boundaries: 206, core_var_decl: 198, design_camel_case: 143
- `fixtures/dom/src/components/fixtures/textareas/index.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 73, core_var_decl: 22, ui_framework: 14, design_snake_case: 13
- `packages/react-devtools-extensions/src/contentScripts/messages.js` (JAVASCRIPT) | Magnitude: 14.24 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, api: 10, core_var_decl: 8
- `packages/react-reconciler/src/ReactFiberTreeReflection.js` (JAVASCRIPT) | Magnitude: 421.28 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 482, structural_boundaries: 145, branch: 128, core_var_decl: 95
- `scripts/babel/__tests__/transform-test-gate-pragma-test.js` (JAVASCRIPT) | Magnitude: 12.64 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 130, test: 62, structural_boundaries: 45, args: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `fixtures/concurrent/time-slicing/public/index.html` (HTML) | Magnitude: 0.02 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, core_var_decl: 7, design_snake_case: 7, structural_boundaries: 4
- `fixtures/attribute-behavior/public/index.html` (HTML) | Magnitude: 0.02 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, core_var_decl: 8, design_snake_case: 8, structural_boundaries: 5
- `packages/shared/noop.js` (JAVASCRIPT) | Magnitude: 2.12 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, args: 1, func_start: 1
- `compiler/packages/react-compiler-healthcheck/tsup.config.ts` (TYPESCRIPT) | Magnitude: 31.78 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, decorators: 7, structural_boundaries: 2, doc: 2
- `fixtures/fizz-ssr-browser/index.html` (HTML) | Magnitude: 0.02 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 19, core_var_decl: 15, design_snake_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scripts/worktree.sh` (SHELL) | Magnitude: 9.73 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 46, branch: 21, state_mutation: 20
- `fixtures/flight-parcel/types.d.ts` (TYPESCRIPT) | Magnitude: 0.03 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 26, args: 12, indent_spaces: 12, api: 10
- `packages/react-server/src/forks/ReactFizzConfig.dom-legacy.js` (JAVASCRIPT) | Magnitude: 16.6 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 5, api: 4, import: 3, safety_bypasses: 1
- `packages/react-server/src/forks/ReactFizzConfig.dom.js` (JAVASCRIPT) | Magnitude: 16.6 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 5, api: 4, import: 3, safety_bypasses: 1
- `packages/react-server/src/forks/ReactFizzConfig.markup.js` (JAVASCRIPT) | Magnitude: 16.6 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 5, api: 4, import: 3, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `fixtures/dom/src/components/fixtures/hydration/code-transformer.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, args: 1, func_start: 1, api: 1
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/propagate-scope-deps-hir-fork/ssa-renaming-with-mutation.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, state_mutation: 4, core_var_decl: 4
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/ssa-renaming-with-mutation.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, state_mutation: 4, core_var_decl: 4
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/align-scopes-reactive-scope-overlaps-label.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 4, core_var_decl: 2, branch: 1
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-no-value-for-temporary-reactive-scope-with-early-return.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, core_var_decl: 4, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/shared/forks/ReactFeatureFlags.readonly.js` (JAVASCRIPT) | Magnitude: 13.04 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 1, state_mutation: 1, doc: 1, import: 1
- `packages/react-client/src/forks/ReactFlightClientConfig.dom-browser-turbopack.js` (JAVASCRIPT) | Magnitude: 25.2 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, api: 10, import: 8, core_var_decl: 2
- `packages/react-client/src/forks/ReactFlightClientConfig.dom-browser.js` (JAVASCRIPT) | Magnitude: 25.2 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, api: 10, import: 8, core_var_decl: 2
- `packages/react-client/src/forks/ReactFlightClientConfig.dom-edge-turbopack.js` (JAVASCRIPT) | Magnitude: 25.2 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, api: 10, import: 8, core_var_decl: 2
- `packages/react-client/src/forks/ReactFlightClientConfig.dom-edge-webpack.js` (JAVASCRIPT) | Magnitude: 25.2 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, api: 10, import: 8, core_var_decl: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/react-client/flight.js` (JAVASCRIPT) | Magnitude: 14.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, safety: 2, api: 2
- `packages/react-devtools-timeline/src/utils/flow.js` (JAVASCRIPT) | Magnitude: 2.82 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, args: 1, func_start: 1
- `packages/react-reconciler/index.js` (JAVASCRIPT) | Magnitude: 14.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, safety: 2, api: 2
- `packages/react-server/flight.js` (JAVASCRIPT) | Magnitude: 14.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, safety: 2, api: 2
- `packages/react-server/index.js` (JAVASCRIPT) | Magnitude: 14.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, safety: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/react-dom/src/server/ReactDOMFizzServerNode.js` (JAVASCRIPT) | Magnitude: 265.28 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 334, branch: 88, structural_boundaries: 60, args: 39
- `packages/react-devtools-shared/src/devtools/views/Components/KeyValue.js` (JAVASCRIPT) | Magnitude: 286.68 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 494, core_var_decl: 217, design_camel_case: 122, branch: 96
- `packages/react-native-renderer/src/ReactFabric.js` (JAVASCRIPT) | Magnitude: 102.46 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 133, branch: 31, structural_boundaries: 29, core_var_decl: 20
- `packages/react-devtools-shared/src/devtools/views/ErrorBoundary/ErrorBoundary.js` (JAVASCRIPT) | Magnitude: 67.34 | Delta: **0.167** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 190, branch: 34, core_var_decl: 34, structural_boundaries: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/new-mutability/transitivity-add-captured-array-to-itself.tsx` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 6, core_var_decl: 6, ui_framework: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/shared/ReactComponentStackFrame.js` (JAVASCRIPT) | Magnitude: 232.96 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 181, branch: 64, safety: 37, core_var_decl: 32
- `packages/react-devtools-shared/src/hook.js` (JAVASCRIPT) | Magnitude: 560.6 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 479, branch: 94, core_var_decl: 59, structural_boundaries: 58
- `packages/react-client/src/ReactFlightClient.js` (JAVASCRIPT) | Magnitude: 3312.44 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 4076, branch: 951, core_var_decl: 561, state_mutation: 464

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/react-reconciler/src/ReactFiberDuplicateViewTransitions.js` (JAVASCRIPT) | Magnitude: 37.08 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 45, branch: 16, structural_boundaries: 8, safety: 8
- `packages/react/src/ReactCacheImpl.js` (JAVASCRIPT) | Magnitude: 46.74 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 93, core_var_decl: 19, branch: 17, structural_boundaries: 17
- `packages/react-devtools-timeline/src/CanvasPageContextMenu.js` (JAVASCRIPT) | Magnitude: 49.72 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 24, args: 12, import: 11
- `fixtures/scheduler/index.html` (HTML) | Magnitude: 0.21 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 565, structural_boundaries: 159, core_var_decl: 93, args: 70
- `packages/react-devtools-shared/src/backend/agent.js` (JAVASCRIPT) | Magnitude: 466.72 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 945, core_var_decl: 138, branch: 135, structural_boundaries: 132

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/react-reconciler/src/ReactFiberCompleteWork.js` (JAVASCRIPT) | Magnitude: 1299.6 | Delta: **0.182** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_spaces: 1430, branch: 366, core_var_decl: 178, safety: 170

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/react-server-dom-turbopack/src/client/ReactFlightClientConfigBundlerTurbopackBrowser.js` (JAVASCRIPT) | Magnitude: 73.68 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 71, core_var_decl: 16, state_mutation: 14, structural_boundaries: 11
- `packages/react/src/ReactAct.js` (JAVASCRIPT) | Magnitude: 183.44 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 221, branch: 49, structural_boundaries: 45, core_var_decl: 36
- `packages/react-dom-bindings/src/client/ReactDOMOption.js` (JAVASCRIPT) | Magnitude: 37.12 | Delta: **0.231** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, branch: 14, safety: 9, structural_boundaries: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-devtools-shared/src/backend/fiber/renderer.js` -> Churn: **100.0%** | Cog Load: 89.2604% | Debt: 11.2838%
- `packages/react-client/src/ReactFlightClient.js` -> Churn: **84.17%** | Cog Load: 66.681% | Debt: 22.6489%
- `packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js` -> Churn: **84.17%** | Cog Load: 70.7768% | Debt: 14.7491%
- `packages/react-client/src/__tests__/ReactFlight-test.js` -> Churn: **81.8%** | Cog Load: 49.9385% | Debt: 99.6736%
- `packages/react-server/src/ReactFlightServer.js` -> Churn: **81.8%** | Cog Load: 81.8525% | Debt: 22.7991%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/react-dom-bindings/src/client/ReactDOMComponent.js` -> **Sebastian Markbåge** (100.0% isolated ownership) | Magnitude: 2843.7
- `packages/eslint-plugin-react-hooks/src/rules/ExhaustiveDeps.ts` -> **Jorge Cabiedes** (100.0% isolated ownership) | Magnitude: 2116.7
- `compiler/packages/snap/src/minimize.ts` -> **Joseph Savona** (100.0% isolated ownership) | Magnitude: 1668.9
- `packages/react-dom/src/__tests__/ReactDOMServerPartialHydrationActivity-test.internal.js` -> **Sebastian "Sebbie" Silbermann** (100.0% isolated ownership) | Magnitude: 1450.26
- `packages/react-devtools-shared/src/devtools/store.js` -> **Sebastian "Sebbie" Silbermann** (81.8% isolated ownership) | Magnitude: 1343.46

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react-reconciler/src/ReactFiberWorkLoop.js` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 99.9496%)
- `packages/react-devtools-shared/src/devtools/views/context.js` -> **Severity: 0.054** (Bridge: 0.0013 * Flux: 42.5%)
- `packages/react-reconciler/src/ReactFiberReconciler.js` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 99.8598%)
- `packages/react-devtools-shared/src/devtools/views/Profiler/Profiler.js` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 100.0%)
- `packages/react-dom/src/client/ReactDOMRoot.js` -> **Severity: 0.039** (Bridge: 0.0004 * Flux: 98.9988%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/shared/ReactTypes.js` -> **Severity: 4.203** (Embedded: 0.057 * Error Risk: 73.7318%)
- `packages/react-reconciler/src/ReactInternalTypes.js` -> **Severity: 3.111** (Embedded: 0.0389 * Error Risk: 80.0%)
- `packages/react-reconciler/src/ReactFiberCallUserSpace.js` -> **Severity: 2.043** (Embedded: 0.0255 * Error Risk: 80.0%)
- `packages/react-reconciler/src/ReactProfilerTimer.js` -> **Severity: 1.956** (Embedded: 0.0243 * Error Risk: 80.5627%)
- `packages/react-reconciler/src/ReactFiberTracingMarkerComponent.js` -> **Severity: 1.954** (Embedded: 0.0299 * Error Risk: 65.2423%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/shared/ReactTypes.js` -> **Severity: 1286.7** (Blast Radius: 12.867 * Doc Risk: 100.0%)
- `packages/shared/ReactSymbols.js` -> **Severity: 1137.5** (Blast Radius: 11.375 * Doc Risk: 100.0%)
- `packages/react-dom/src/client/ReactDOMClient.js` -> **Severity: 817.4** (Blast Radius: 8.174 * Doc Risk: 100.0%)
- `compiler/packages/babel-plugin-react-compiler/src/CompilerError.ts` -> **Severity: 479.193** (Blast Radius: 5.437 * Doc Risk: 88.1356%)
- `packages/react-reconciler/src/ReactInternalTypes.js` -> **Severity: 478.3** (Blast Radius: 4.783 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2771 literal sites + 69 sites through wrappers = 2840
- **`panics_and_aborts`:** 2934 literal sites + 57 sites through wrappers = 2991

- `logError` (function, debug_prints, primitive): 20 call sites in 1 files -- `scripts/jest/jest-cli.js`
- `logBright` (function, debug_prints, primitive): 10 call sites in 1 files -- `scripts/ci/run_devtools_e2e_tests.js`
- `throwInput` (function, panics_and_aborts, primitive): 9 call sites in 9 files -- `compiler/packages/snap/src/sprout/shared-runtime.ts`
- `throwTaintViolation` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `packages/react-server/src/ReactFlightServer.js`
- `warnInvalidHookAccess` (function, debug_prints, primitive): 6 call sites in 1 files -- `packages/react-reconciler/src/ReactFiberHooks.js`
- `throwErrorWithMessage` (function, panics_and_aborts, primitive): 5 call sites in 5 files -- `compiler/packages/snap/src/sprout/shared-runtime.ts`
- `createCancelHandler` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `packages/react-dom/src/server/ReactDOMFizzServerNode.js`
- `log` (function, debug_prints, primitive): 3 call sites in 1 files -- `packages/react-devtools-core/src/standalone.js`
- `useDispatch` (function, debug_prints, primitive): 3 call sites in 3 files -- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-dispatch-spread-event-marks-event-frozen.js`
- `assertExhaustive` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `compiler/packages/eslint-plugin-react-compiler/src/rules/ReactCompilerRule.ts`
- `assertExhaustive` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/eslint-plugin-react-hooks/src/shared/ReactCompiler.ts`
- `bar` (function, debug_prints, primitive): 2 call sites in 1 files -- `compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/repro-retain-source-when-bailout.js`
*(+37 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 42126 call pairs -- scoped 28.7%, unique 0.0%, ambiguous 30.6%, external 40.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 35805 | 26.9% | 0.0% | 31.0% | 42.1% |
| typescript | 6092 | 39.4% | 0.0% | 29.0% | 31.5% |
| html | 188 | 27.7% | 0.0% | 0.0% | 72.3% |
| shell | 41 | 14.6% | 0.0% | 0.0% | 85.4% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
