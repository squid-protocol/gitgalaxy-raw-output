# ARCHITECTURAL_BRIEF: ionic-framework
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/ionic-framework` |
| **Timestamp** | `2026-08-03T19:54:32.132012+00:00` |
| **Scan Duration** | `6.45s` |
| **Git Branch** | `main` |
| **Git Commit** | `4d81b026a72e57a4b330de15a2053fa86f0084ca` |
| **Git Remote** | `https://github.com/ionic-team/ionic-framework.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1372 malicious artifacts.

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
| Total Artifacts | 9447 |
| Analyzed Artifacts (Scanned) | 2360 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7087 |
| Total LOC | 155680 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 25.0% |
| Dominant Lang | HTML |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6141 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3119 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1637 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 65 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1322 | 89186 | 56.0% |
| HTML | 477 | 49376 | 20.2% |
| CSS | 432 | 15501 | 18.3% |
| JAVASCRIPT | 32 | 945 | 1.4% |
| PLAINTEXT | 23 | 1 | 1.0% |
| MARKDOWN | 21 | 0 | 0.9% |
| JSON | 19 | 501 | 0.8% |
| XML | 16 | 0 | 0.7% |
| SHELL | 14 | 131 | 0.6% |
| JAVA | 3 | 37 | 0.1% |
| DOCKERFILE | 1 | 2 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.976`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1630 | 69.1% |
| file_cluster_13 | 367 | 15.6% |
| file_cluster_4 | 197 | 8.3% |
| file_cluster_2 | 57 | 2.4% |
| file_cluster_0 | 29 | 1.2% |
| file_cluster_16 | 16 | 0.7% |
| file_cluster_17 | 9 | 0.4% |
| file_cluster_11 | 5 | 0.2% |
| file_cluster_1 | 4 | 0.2% |
| Unknown | 1 | 0.0% |
| file_cluster_9 | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 43 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7087*

**Composition by Extension & Reason:**
- `.png`: 6781x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9833 LOC), 1x Excluded (Massive Static Asset Blob: 13851 LOC)
- `.ts`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 55 exceeds 500 chars), 1x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.js`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4075 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2740 LOC)
- `no_extension`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.html`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 86 exceeds 500 chars), 1x Excluded (Saturation: Line 92 exceeds 500 chars)
- `.sh`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 3x Excluded (Unsupported Extension: '.map'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 3x Excluded (Explicitly Denied Extension: '.jpg')
- `.properties`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (Embedded Array/Matrix Payload: 8000 commas in 2143 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 19.7 | 5.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 19.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.8 | 4.0 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 32.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 57.3 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 87.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.9 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 83.8 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 20.5 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `core/src/components/router/test/path.spec.tsx` (Hits: 84)
- `packages/angular/test/base/src/app/standalone/app-standalone/app.routes.ts` (Hits: 56)
- `core/src/components/breadcrumbs/test/collapsed/index.html` (Hits: 47)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.scss** (`core/src/css/core.scss`) — 383 inbound connections
2. **interface.ts** (`core/src/components/router/utils/interface.ts`) — 130 inbound connections
3. **ionic-global.ts** (`core/src/global/ionic-global.ts`) — 95 inbound connections
4. **common.ts** (`core/src/utils/input-shims/hacks/common.ts`) — 89 inbound connections
5. **theme.ts** (`core/src/utils/theme.ts`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **proxies.ts** (`packages/react/src/components/proxies.ts`) — 74 outbound dependencies
2. **app.routes.ts** (`packages/angular/test/base/src/app/standalone/app-standalone/app.routes.ts`) — 50 outbound dependencies
3. **index.ts** (`packages/vue/test/base/src/router/index.ts`) — 41 outbound dependencies
4. **interface.d.ts** (`core/src/interface.d.ts`) — 40 outbound dependencies
5. **components.d.ts** (`core/src/components.d.ts`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `onDragEnd` (@ `core/src/components/modal/gestures/sheet.ts`) -> Impact: **1083.7** | LOC: 554
  * *Intent:* /**
- `isViewVisible` (@ `packages/react-router/src/ReactRouter/StackManager.tsx`) -> Impact: **978.8** | LOC: 375
- `renderMonth` (@ `core/src/components/datetime/datetime.tsx`) -> Impact: **332.1** | LOC: 216
- `createIonRouter` (@ `packages/vue-router/src/router.ts`) -> Impact: **294.2** | LOC: 341
  * *Intent:* // TODO(FW-2969): types
- `handleFocus` (@ `core/src/components/menu/menu.tsx`) -> Impact: **259.1** | LOC: 443
- `onDragEnd` (@ `core/src/components/modal/gestures/swipe-to-close.ts`) -> Impact: **249.7** | LOC: 193
- `onDismiss` (@ `core/src/components/toast/gestures/swipe-to-dismiss.ts`) -> Impact: **249.2** | LOC: 273
  * *Intent:* /** * Create a gesture that allows the Toast * to be swiped to dismiss. * @param el - The Toast element
- `createMenuController` (@ `core/src/utils/menu-controller/index.ts`) -> Impact: **221.8** | LOC: 116
- `defineCustomElement` (@ `packages/vue/src/utils/overlays.ts`) -> Impact: **219.1** | LOC: 226
- `iosTransitionAnimation` (@ `core/src/utils/transition/ios.transition.ts`) -> Impact: **218.1** | LOC: 344
  * *Intent:* /** * The scaled title should (roughly) overlap the back button. This ensures that * the back button and title overlap during the animation. Note that...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `onDragEnd` (@ `core/src/components/modal/gestures/sheet.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `describe` (@ `core/src/components/modal/test/can-dismiss/modal.spec.tsx`) -> **O(2^N) [Recursive]**
- `expect` (@ `core/src/components/radio/test/a11y/radio.e2e.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `core/src/components/router/test/parser.spec.tsx`) -> **O(2^N) [Recursive]**
- `expect` (@ `core/src/components/segment/test/segment-events.e2e.ts`) -> **O(2^N) [Recursive]**
- `render` (@ `core/src/components/toast/toast.tsx`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Emitted before the toast has dismissed. */ /** * Emitted after the toast has dismissed. */ /** * Emitted after the toast has presented. * Shorth...
- `render` (@ `packages/react-router/src/ReactRouter/IonRouteInner.tsx`) -> **O(2^N) [Recursive]**
- `isViewVisible` (@ `packages/react-router/src/ReactRouter/StackManager.tsx`) -> **O(2^N) [Recursive]**
- `Menu` (@ `packages/react-router/test/base/src/pages/routing/Menu.tsx`) -> **O(2^N) [Recursive]**
- `Inputs` (@ `packages/react/test/base/src/pages/Inputs.tsx`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `handleFocus` (@ `core/src/components/menu/menu.tsx`) -> DB Complexity: **116**
- `isViewVisible` (@ `packages/react-router/src/ReactRouter/StackManager.tsx`) -> DB Complexity: **103**
- `describe` (@ `core/src/components/router/test/path.spec.tsx`) -> DB Complexity: **102**
- `componentWillLoad` (@ `core/src/components/modal/modal.tsx`) -> DB Complexity: **87**
  * *Intent:* * If `true`, the modal will animate. */ /** * The element that presented the modal. This is used for card presentation effects * and for stacking mult...
- `describe` (@ `core/src/components/router/test/path.spec.tsx`) -> DB Complexity: **72**
- `describe` (@ `core/src/components/router/test/path.spec.tsx`) -> DB Complexity: **69**
- `describe` (@ `core/src/components/router/test/matching.spec.tsx`) -> DB Complexity: **57**
- `describe` (@ `core/src/components/router/test/parser.spec.tsx`) -> DB Complexity: **55**
- `FC` (@ `packages/react-router/test/base/src/App.tsx`) -> DB Complexity: **51**
- `createIonRouter` (@ `packages/vue-router/src/router.ts`) -> DB Complexity: **47**
  * *Intent:* // TODO(FW-2969): types

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/docs` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/vue/test/base/src/views` | 21 | 443.43 | 7.68% | 0.0% |
| `packages/react-router/src/ReactRouter` | 8 | 226.02 | 62.23% | 17.18% |
| `core/src/themes/test/css-variables` | 1 | 209.62 | 13.65% | 0.0% |
| `core/src/components/action-sheet/test/basic` | 5 | 174.09 | 50.13% | 0.0% |
| `packages/react-router` | 7 | 162.19 | 5.71% | 0.0% |
| `packages/react/src/components` | 26 | 145.16 | 26.03% | 10.01% |
| `core/src/components/datetime/test/multiple` | 2 | 141.81 | 50.0% | 0.0% |
| `core/scripts` | 6 | 141.4 | 23.34% | 0.0% |
| `core/src/components/modal/gestures` | 3 | 141.09 | 9.63% | 3.33% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/react/jest.setup.js` -> **100.0%** Exposure
- `core/src/components/reorder-group/reorder-group-interface.ts` -> **100.0%** Exposure
- `core/src/utils/input-shims/hacks/test/scroll-assist.e2e.ts` -> **100.0%** Exposure
- `packages/angular/common/src/directives/navigation/router-link-delegate.ts` -> **100.0%** Exposure
- `packages/react/src/components/IonRoute.tsx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `core/src/components/accordion-group/accordion-group.tsx` -> **100.0%** Exposure
- `core/src/components/accordion/accordion.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/action-sheet.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/test/basic/fixture.ts` -> **100.0%** Exposure
- `core/src/components/alert/alert.tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/src/components/select/test/label/select.e2e.ts` -> **0** Orphaned Functions | **29** Duplicates
- `core/src/components/textarea/test/label-placement/textarea.e2e.ts` -> **0** Orphaned Functions | **25** Duplicates
- `packages/angular/test/base/e2e/src/lazy/tabs.spec.ts` -> **0** Orphaned Functions | **24** Duplicates
- `core/src/components/datetime/test/presentation/datetime.e2e.ts` -> **0** Orphaned Functions | **23** Duplicates
- `core/src/components/input-otp/test/basic/input-otp.e2e.ts` -> **1** Orphaned Functions | **21** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/react-router/src/ReactRouter/IonRouter.tsx`** -> AI Confidence: **99.39%**
2. **`core/src/components.d.ts`** -> AI Confidence: **99.31%**
3. **`core/src/components/action-sheet/action-sheet.tsx`** -> AI Confidence: **99.31%**
4. **`core/src/components/datetime-button/datetime-button.tsx`** -> AI Confidence: **99.31%**
5. **`core/src/components/datetime/datetime.tsx`** -> AI Confidence: **99.31%**
6. **`core/src/components/input-otp/input-otp.tsx`** -> AI Confidence: **99.31%**
7. **`core/src/components/item-sliding/item-sliding.tsx`** -> AI Confidence: **99.31%**
8. **`core/src/components/menu/menu.tsx`** -> AI Confidence: **99.31%**
9. **`core/src/components/modal/gestures/sheet.ts`** -> AI Confidence: **99.31%**
10. **`core/src/components/modal/gestures/swipe-to-close.ts`** -> AI Confidence: **99.31%**
11. **`core/src/components/modal/modal.tsx`** -> AI Confidence: **99.31%**
12. **`core/src/components/nav/nav.tsx`** -> AI Confidence: **99.31%**
13. **`core/src/components/picker-column/picker-column.tsx`** -> AI Confidence: **99.31%**
14. **`core/src/components/picker-legacy-column/picker-column.tsx`** -> AI Confidence: **99.31%**
15. **`core/src/components/range/range.tsx`** -> AI Confidence: **99.31%**
16. **`core/src/components/refresher/refresher.tsx`** -> AI Confidence: **99.31%**
17. **`core/src/components/reorder-group/reorder-group.tsx`** -> AI Confidence: **99.31%**
18. **`core/src/components/segment/segment.tsx`** -> AI Confidence: **99.31%**
19. **`core/src/components/toast/gestures/swipe-to-dismiss.ts`** -> AI Confidence: **99.31%**
20. **`core/src/utils/input-shims/input-shims.ts`** -> AI Confidence: **99.31%**
21. **`core/src/utils/overlays.ts`** -> AI Confidence: **99.31%**
22. **`packages/angular/common/src/directives/navigation/router-outlet.ts`** -> AI Confidence: **99.31%**
23. **`packages/angular/common/src/directives/navigation/stack-controller.ts`** -> AI Confidence: **99.31%**
24. **`core/scripts/testing/scripts.js`** -> AI Confidence: **99.29%**
25. **`packages/vue/scripts/build-web-types.js`** -> AI Confidence: **99.29%**
26. **`core/src/components/alert/alert.tsx`** -> AI Confidence: **99.24%**
27. **`core/src/components/input/input.tsx`** -> AI Confidence: **99.24%**
28. **`core/src/components/refresher-content/refresher-content.tsx`** -> AI Confidence: **99.24%**
29. **`core/src/components/router-outlet/router-outlet.tsx`** -> AI Confidence: **99.24%**
30. **`core/src/components/router/router.tsx`** -> AI Confidence: **99.24%**
31. **`core/src/components/textarea/textarea.tsx`** -> AI Confidence: **99.24%**
32. **`core/src/components/toggle/toggle.tsx`** -> AI Confidence: **99.24%**
33. **`core/src/components/content/content.tsx`** -> AI Confidence: **99.23%**
34. **`core/src/components/spinner/spinner.tsx`** -> AI Confidence: **99.23%**
35. **`packages/react/src/components/createRoutingComponent.tsx`** -> AI Confidence: **99.23%**
36. **`packages/react/src/components/navigation/IonTabBar.tsx`** -> AI Confidence: **99.23%**
37. **`packages/vue-router/src/router.ts`** -> AI Confidence: **99.23%**
38. **`core/src/utils/transition/ios.transition.ts`** -> AI Confidence: **99.2%**
39. **`core/src/components/button/button.tsx`** -> AI Confidence: **99.18%**
40. **`core/src/components/fab-button/fab-button.tsx`** -> AI Confidence: **99.18%**
41. **`core/src/components/infinite-scroll-content/infinite-scroll-content.tsx`** -> AI Confidence: **99.18%**
42. **`core/src/components/select-modal/select-modal.tsx`** -> AI Confidence: **99.18%**
43. **`core/src/components/select/select.tsx`** -> AI Confidence: **99.18%**
44. **`packages/react/src/components/IonRouterOutlet.tsx`** -> AI Confidence: **99.18%**
45. **`packages/react/src/components/navigation/IonTabs.tsx`** -> AI Confidence: **99.18%**
46. **`core/custom-rules/no-playwright-to-match-snapshot-assertion.js`** -> AI Confidence: **99.17%**
47. **`core/src/components/action-sheet/action-sheet-interface.ts`** -> AI Confidence: **99.17%**
48. **`core/src/components/datetime/utils/validate.ts`** -> AI Confidence: **99.17%**
49. **`core/src/components/picker-legacy/picker-interface.ts`** -> AI Confidence: **99.17%**
50. **`packages/react-router/src/ReactRouter/StackManager.tsx`** -> AI Confidence: **99.17%**
51. **`packages/react/src/components/CreateAnimation.tsx`** -> AI Confidence: **99.17%**
52. **`core/src/components/app/app.tsx`** -> AI Confidence: **99.16%**
53. **`core/src/components/loading/loading.tsx`** -> AI Confidence: **99.16%**
54. **`core/src/components/picker-legacy/picker.tsx`** -> AI Confidence: **99.16%**
55. **`core/src/components/popover/popover.tsx`** -> AI Confidence: **99.16%**
56. **`core/src/components/toast/toast.tsx`** -> AI Confidence: **99.16%**
57. **`core/src/components/back-button/back-button.tsx`** -> AI Confidence: **99.15%**
58. **`core/src/components/checkbox/checkbox.tsx`** -> AI Confidence: **99.15%**
59. **`core/src/components/item/item.tsx`** -> AI Confidence: **99.15%**
60. **`core/src/components/segment-button/segment-button.tsx`** -> AI Confidence: **99.15%**
61. **`core/src/components/select-popover/select-popover.tsx`** -> AI Confidence: **99.15%**
62. **`core/src/utils/input-shims/hacks/scroll-assist.ts`** -> AI Confidence: **99.15%**
63. **`core/src/utils/menu-controller/index.ts`** -> AI Confidence: **99.15%**
64. **`core/src/utils/transition/index.ts`** -> AI Confidence: **99.15%**
65. **`packages/react/src/hooks/useOverlay.ts`** -> AI Confidence: **99.15%**
66. **`packages/react/src/routing/NavManager.tsx`** -> AI Confidence: **99.15%**
67. **`core/src/components/accordion/accordion.tsx`** -> AI Confidence: **99.13%**
68. **`core/src/components/datetime/utils/data.ts`** -> AI Confidence: **99.13%**
69. **`core/src/components/datetime/utils/state.ts`** -> AI Confidence: **99.13%**
70. **`core/src/components/radio-group/radio-group.tsx`** -> AI Confidence: **99.13%**
71. **`core/src/global/ionic-global.ts`** -> AI Confidence: **99.13%**
72. **`core/src/utils/config.ts`** -> AI Confidence: **99.13%**
73. **`packages/angular/common/src/providers/nav-controller.ts`** -> AI Confidence: **99.13%**
74. **`packages/react/src/components/IonIcon.tsx`** -> AI Confidence: **99.13%**
75. **`packages/react/src/components/createInlineOverlayComponent.tsx`** -> AI Confidence: **99.13%**
76. **`packages/vue/src/components/IonRouterOutlet.ts`** -> AI Confidence: **99.13%**
77. **`core/src/components/alert/alert-interface.ts`** -> AI Confidence: **99.11%**
78. **`core/src/components/col/col.tsx`** -> AI Confidence: **99.09%**
79. **`core/src/components/img/img.tsx`** -> AI Confidence: **99.09%**
80. **`core/src/components/infinite-scroll/infinite-scroll.tsx`** -> AI Confidence: **99.09%**
81. **`core/src/components/loading/loading-interface.ts`** -> AI Confidence: **99.09%**
82. **`core/src/components/picker/picker.tsx`** -> AI Confidence: **99.09%**
83. **`core/src/components/toast/animations/ios.leave.ts`** -> AI Confidence: **99.09%**
84. **`core/src/css/test/flex-utils.e2e.ts`** -> AI Confidence: **99.09%**
85. **`core/src/index.ts`** -> AI Confidence: **99.09%**
86. **`core/src/interface.d.ts`** -> AI Confidence: **99.09%**
87. **`core/src/utils/gesture/index.ts`** -> AI Confidence: **99.09%**
88. **`core/src/utils/tap-click/index.ts`** -> AI Confidence: **99.09%**
89. **`packages/angular/common/src/directives/navigation/tabs.ts`** -> AI Confidence: **99.09%**
90. **`packages/angular/common/src/index.ts`** -> AI Confidence: **99.09%**
91. **`packages/angular/src/index.ts`** -> AI Confidence: **99.09%**
92. **`packages/angular/src/ionic-module.ts`** -> AI Confidence: **99.09%**
93. **`packages/angular/standalone/src/directives/index.ts`** -> AI Confidence: **99.09%**
94. **`packages/angular/standalone/src/index.ts`** -> AI Confidence: **99.09%**
95. **`packages/angular/test/base/src/app/lazy/app-lazy/app.module.ts`** -> AI Confidence: **99.09%**
96. **`packages/angular/test/base/src/app/lazy/app-lazy/app.routes.ts`** -> AI Confidence: **99.09%**
97. **`packages/angular/test/base/src/app/standalone/app-standalone/app.routes.ts`** -> AI Confidence: **99.09%**
98. **`packages/react-router/src/ReactRouter/ReactRouterViewStack.tsx`** -> AI Confidence: **99.09%**
99. **`packages/react-router/test/base/src/App.tsx`** -> AI Confidence: **99.09%**
100. **`packages/react/src/components/index.ts`** -> AI Confidence: **99.09%**
101. **`packages/react/src/components/proxies.ts`** -> AI Confidence: **99.09%**
102. **`packages/react/src/components/routing-proxies.ts`** -> AI Confidence: **99.09%**
103. **`packages/react/src/hooks/__tests__/hooks.spec.tsx`** -> AI Confidence: **99.09%**
104. **`packages/react/src/models/RouteInfo.ts`** -> AI Confidence: **99.09%**
105. **`packages/react/test/base/src/App.tsx`** -> AI Confidence: **99.09%**
106. **`packages/react/test/base/src/pages/overlay-components/OverlayComponents.tsx`** -> AI Confidence: **99.09%**
107. **`packages/react/test/base/src/pages/overlay-hooks/OverlayHooks.tsx`** -> AI Confidence: **99.09%**
108. **`packages/vue-router/src/types.ts`** -> AI Confidence: **99.09%**
109. **`packages/vue/src/index.ts`** -> AI Confidence: **99.09%**
110. **`packages/vue/test/base/src/main.ts`** -> AI Confidence: **99.09%**
111. **`packages/vue/test/base/src/router/index.ts`** -> AI Confidence: **99.09%**
112. **`core/src/components/breadcrumb/breadcrumb.tsx`** -> AI Confidence: **99.08%**
113. **`core/src/utils/test/playwright/index.ts`** -> AI Confidence: **99.08%**
114. **`packages/angular/test/base/src/app/lazy/modal-dynamic-wrapper/modal-dynamic-wrapper.module.ts`** -> AI Confidence: **99.08%**
115. **`packages/angular/test/base/src/app/lazy/tabs/tabs.module.ts`** -> AI Confidence: **99.08%**
116. **`packages/angular/test/base/src/app/lazy/tabs/tabs.router.module.ts`** -> AI Confidence: **99.08%**
117. **`packages/angular/test/base/src/app/lazy/template-form/template-form.module.ts`** -> AI Confidence: **99.08%**
118. **`packages/react-router/test/base/src/pages/routing/Routing.tsx`** -> AI Confidence: **99.08%**
119. **`packages/react-router/test/base/src/pages/routing/Tabs.tsx`** -> AI Confidence: **99.08%**
120. **`packages/react/src/index.ts`** -> AI Confidence: **99.08%**
121. **`packages/react/src/routing/index.ts`** -> AI Confidence: **99.08%**
122. **`packages/vue/src/components/Overlays.ts`** -> AI Confidence: **99.08%**
123. **`core/src/components/menu-button/menu-button.tsx`** -> AI Confidence: **99.07%**
124. **`packages/angular/common/src/providers/platform.ts`** -> AI Confidence: **99.07%**
125. **`packages/angular/src/schematics/add/index.ts`** -> AI Confidence: **99.07%**
126. **`packages/react/src/components/IonApp.tsx`** -> AI Confidence: **99.07%**
127. **`packages/react/src/components/inner-proxies.ts`** -> AI Confidence: **99.07%**
128. **`packages/vue/src/controllers.ts`** -> AI Confidence: **99.07%**
129. **`core/custom-rules/await-playwright-promise-assertion.js`** -> AI Confidence: **99.06%**
130. **`core/custom-rules/no-component-on-ready-method.js`** -> AI Confidence: **99.06%**
131. **`core/scripts/treeshaking.js`** -> AI Confidence: **99.06%**
132. **`core/scripts/update-readme.js`** -> AI Confidence: **99.06%**
133. **`core/setupJest.js`** -> AI Confidence: **99.06%**
134. **`packages/react-router/rollup.config.mjs`** -> AI Confidence: **99.06%**
135. **`packages/react/jest.setup.js`** -> AI Confidence: **99.06%**
136. **`packages/react/rollup.config.mjs`** -> AI Confidence: **99.06%**
137. **`core/playwright.config.ts`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `core/src/components/accordion/accordion.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/action-sheet.tsx` -> **100.0%** Exposure
- `core/src/components/alert/alert.tsx` -> **100.0%** Exposure
- `core/src/components/back-button/back-button.tsx` -> **100.0%** Exposure
- `core/src/components/button/button.tsx` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `core/scripts/testing/prerender.js` -> **100.0%** Exposure
- `core/src/components/select/test/basic/select.e2e.ts` -> **100.0%** Exposure
- `core/src/utils/sanitization/test/sanitization.spec.ts` -> **100.0%** Exposure
- `packages/angular/test/base/src/app/lazy/app-lazy/app.routes.ts` -> **100.0%** Exposure
- `packages/react/test/base/src/pages/Tabs.tsx` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `core/src/components/accordion/accordion.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/action-sheet.tsx` -> **100.0%** Exposure
- `core/src/components/alert/alert.tsx` -> **100.0%** Exposure
- `core/src/components/back-button/back-button.tsx` -> **100.0%** Exposure
- `core/src/components/button/button.tsx` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2793` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/angular/common/src/directives/control-value-accessors/value-accessor.ts` (TYPESCRIPT) -> Cumulative Risk: **909.99**
- **Archetype:** `file_cluster_11` (Distance: 13.933 IQR)
- **Magnitude:** 16.6 | **LOC:** 158 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.9998%), Algorithmic Dos (99.9989%)
- **Heaviest Functions:** `ngAfterViewInit` (Impact: 21.4), `setIonicClasses` (Impact: 17.6), `getClasses` (Impact: 8.6)

### 2. `core/src/components/infinite-scroll/infinite-scroll.tsx` (TYPESCRIPT) -> Cumulative Risk: **833.21**
- **Archetype:** `file_cluster_4` (Distance: 13.214 IQR)
- **Magnitude:** 15.18 | **LOC:** 237 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `complete` (Impact: 19.1), `enableScrollEvents` (Impact: 12.4), `canStart` (Impact: 7.1)

### 3. `packages/angular/common/src/providers/angular-delegate.ts` (TYPESCRIPT) -> Cumulative Risk: **827.89**
- **Archetype:** `file_cluster_13` (Distance: 11.721 IQR)
- **Magnitude:** 32.22 | **LOC:** 279 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `attachView` (Impact: 176.7), `attachViewToDom` (Impact: 15.0), `create` (Impact: 12.0)

### 4. `packages/angular/common/src/directives/navigation/stack-controller.ts` (TYPESCRIPT) -> Cumulative Risk: **807.44**
- **Archetype:** `file_cluster_4` (Distance: 13.096 IQR)
- **Magnitude:** 47.16 | **LOC:** 354 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setActive` (Impact: 62.6), `transition` (Impact: 41.4), `pop` (Impact: 19.2)

### 5. `packages/react/src/components/createControllerComponent.tsx` (TYPESCRIPT) -> Cumulative Risk: **775.64**
- **Archetype:** `file_cluster_4` (Distance: 14.519 IQR)
- **Magnitude:** 25.11 | **LOC:** 128 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `present` (Impact: 49.4), `componentDidUpdate` (Impact: 18.4), `dismiss` (Impact: 12.6)

### 6. `packages/react-router/src/ReactRouter/StackManager.tsx` (TYPESCRIPT) -> Cumulative Risk: **766.43**
- **Archetype:** `file_cluster_4` (Distance: 13.376 IQR)
- **Magnitude:** 133.26 | **LOC:** 468 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `isViewVisible` (Impact: 978.8), `matchRoute` (Impact: 9.9), `matchComponent` (Impact: 4.5)

### 7. `core/src/components/select-modal/select-modal.tsx` (TYPESCRIPT) -> Cumulative Risk: **765.08**
- **Archetype:** `file_cluster_17` (Distance: 12.574 IQR)
- **Magnitude:** 11.07 | **LOC:** 168 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getValues` (Impact: 12.9), `renderRadioOptions` (Impact: 10.4), `render` (Impact: 9.4)

### 8. `packages/react/src/hooks/useOverlay.ts` (TYPESCRIPT) -> Cumulative Risk: **759.02**
- **Archetype:** `file_cluster_13` (Distance: 12.017 IQR)
- **Magnitude:** 13.26 | **LOC:** 97 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (98.0565%), State Flux (97.0615%)
- **Heaviest Functions:** `defineCustomElement` (Impact: 86.9), `useOverlay` (Impact: 2.1)

### 9. `core/src/components/picker-legacy/picker.tsx` (TYPESCRIPT) -> Cumulative Risk: **754.23**
- **Archetype:** `file_cluster_4` (Distance: 13.127 IQR)
- **Magnitude:** 33.45 | **LOC:** 418 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `dismiss` (Impact: 18.1), `callButtonHandler` (Impact: 12.5), `getSelected` (Impact: 11.0)

### 10. `packages/react/src/components/react-component-lib/createOverlayComponent.tsx` (TYPESCRIPT) -> Cumulative Risk: **747.52**
- **Archetype:** `file_cluster_4` (Distance: 14.427 IQR)
- **Magnitude:** 27.28 | **LOC:** 143 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `present` (Impact: 31.1), `componentDidUpdate` (Impact: 21.8), `dismiss` (Impact: 14.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/docs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/themes/test/css-variables/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.648 IQR)
- **Top Global Matches:** file_cluster_8: 9.648, file_cluster_0: 9.903, file_cluster_7: 10.279
- **Magnitude:** 209.62 | **LOC:** 1190 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (13.6502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `togglePalette` (Impact: 50.4 | O(N^3) | DB: 9)
  * `createModal` (Impact: 10.6 | O(N^3))
  * `presentActionSheet` (Impact: 7.3 | O(N^4))
  * `connectedCallback` (Impact: 4.4 | O(N^4) | DB: 1)
  * `presentLoading` (Impact: 3.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 66`, `args: 149`, `func_start: 17`, `class_start: 535`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 20`, `dead_code: 1`
* *Architecture:* `io: 40`, `api: 61`, `concurrency: 15`
* *Defense:* `safety: 10`, `doc: 5`, `immutability_locks: 21`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` default.css, ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/action-sheet/test/basic/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.439 IQR)
- **Top Global Matches:** file_cluster_8: 8.439, file_cluster_7: 9.26, file_cluster_0: 9.314
- **Magnitude:** 148.98 | **LOC:** 512 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (32.9497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `presentBasic` (Impact: 17.6 | O(N^4))
  * `presentWithCssClass` (Impact: 12.2 | O(N^4) | DB: 1)
  * `presentScroll` (Impact: 10.2 | O(N^4) | DB: 1)
  * `presentScrollNoCancel` (Impact: 8.9 | O(N^4))
  * `presentAlert` (Impact: 8.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 72`, `args: 64`, `func_start: 60`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 20`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/datetime.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.813 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.296 IQR)
- **Top Global Matches:** file_cluster_8: 12.813, file_cluster_13: 12.839, file_cluster_0: 12.951
- **Magnitude:** 133.4 | **LOC:** 2764 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (54.304%), Tech Debt (8.2495%)
**Top Internal Functions/Classes:**
  * `renderMonth` (Impact: 332.1 | O(N^6) | DB: 33)
  * `processValue` (Impact: 127.5 | O(N^3) | DB: 5)
    * *Intent:* /** * When defined, will force the datetime to render the month * containing the specified date. Cur...
  * `renderIndividualDatePickerColumns` (Impact: 63.5 | O(N^3) | DB: 23)
    * *Intent:* /** * Which values you want to select. `"date"` will show * a calendar picker to select the month, d...
  * `renderCalendarHeader` (Impact: 49.1 | O(N^4) | DB: 15)
  * `renderDatetime` (Impact: 41.2 | O(N^2) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 140`, `args: 70`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 418`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 13`, `import: 21`
* *Defense:* `safety: 28`, `doc: 24`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` data, format, state, rtl, core, parse, helpers, datetime-interface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/src/ReactRouter/StackManager.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.376 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.043 IQR)
- **Top Global Matches:** file_cluster_4: 13.376, file_cluster_13: 13.602, file_cluster_17: 13.691
- **Magnitude:** 133.26 | **LOC:** 468 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 103
- **Risk Profile:** Cognitive Load (60.2237%), Tech Debt (8.592%)
**Top Internal Functions/Classes:**
  * `isViewVisible` (Impact: 978.8 | O(2^N) | DB: 103)
  * `matchRoute` (Impact: 9.9 | O(N^1) | DB: 4)
  * `matchComponent` (Impact: 4.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 42`, `args: 28`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 263`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 67`, `import: 5`
* *Defense:* `safety: 11`, `doc: 14`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` matchPath, clonePageElement, react, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/components/segment/test/basic/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.381 IQR)
- **Top Global Matches:** file_cluster_8: 11.381, file_cluster_0: 11.503, file_cluster_7: 11.941
- **Magnitude:** 123.26 | **LOC:** 319 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (17.2411%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toggleValue` (Impact: 26.7 | O(N^4) | DB: 3)
  * `toggleDisabled` (Impact: 17.8 | O(N^3) | DB: 2)
  * `updateSegmentButtons` (Impact: 11.0 | O(N^3) | DB: 1)
  * `toggleSwipeGesture` (Impact: 7.2 | O(N^3) | DB: 1)
  * `listenForEvent` (Impact: 4.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 18`, `args: 73`, `func_start: 8`, `class_start: 117`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `io: 2`, `api: 19`, `concurrency: 2`
* *Defense:* `safety: 21`, `doc: 1`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/searchbar/test/basic/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.152 IQR)
- **Top Global Matches:** file_cluster_0: 10.152, file_cluster_8: 10.518, file_cluster_13: 11.03
- **Magnitude:** 119.58 | **LOC:** 181 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (17.6746%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toggleAttr` (Impact: 75.6 | O(N^4) | DB: 2)
  * `toggleProp` (Impact: 14.7 | O(N^3) | DB: 1)
  * `toggleDisabled` (Impact: 7.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 24`, `args: 22`, `func_start: 3`, `class_start: 22`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 13`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/test/show-adjacent-days/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.968 IQR)
- **Top Global Matches:** file_cluster_8: 8.968, file_cluster_2: 9.189, file_cluster_0: 9.287
- **Magnitude:** 116.06 | **LOC:** 329 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.745%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isDateEnabled` (Impact: 17.8 | O(N^3))
  * `initCalendarMonthChangeObserver` (Impact: 11.1 | O(N^3))
  * `isDateEnabled` (Impact: 10.8 | O(N^2))
  * `constructor` (Impact: 8.8 | O(N^3))
  * `isDateEnabled` (Impact: 8.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 53`, `args: 37`, `func_start: 16`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 16`, `duplicate_logic: 7`
* *Architecture:* `io: 2`, `api: 24`, `concurrency: 4`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/gestures/sheet.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.324 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.347 IQR)
- **Top Global Matches:** file_cluster_8: 11.324, file_cluster_13: 11.603, file_cluster_7: 11.634
- **Magnitude:** 111.57 | **LOC:** 769 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (6.7432%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDragEnd` (Impact: 1083.7 | O(2^N) | DB: 13)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 55`, `args: 45`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 42`, `doc: 46`, `immutability_locks: 57`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` overlays, gesture, gesture, interface, helpers, utils, content, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/test/multiple/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.186 IQR)
- **Top Global Matches:** file_cluster_8: 7.186, file_cluster_2: 7.557, file_cluster_0: 7.953
- **Magnitude:** 110.88 | **LOC:** 128 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 15`, `func_start: 1`, `class_start: 15`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 9`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/button/test/perf/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.512 IQR)
- **Top Global Matches:** file_cluster_8: 9.512, file_cluster_7: 10.394, file_cluster_1: 10.514
- **Magnitude:** 106.96 | **LOC:** 4452 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.2547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changeColor` (Impact: 5.6 | O(N^2))
  * `toggleDisabled` (Impact: 2.8 | O(N^2) | DB: 2)
  * `clickedButton` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 6`, `func_start: 3`, `class_start: 4415`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vue/test/base/src/views/Overlays.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.676 IQR)
- **Top Global Matches:** file_cluster_8: 8.676, file_cluster_1: 9.276, file_cluster_7: 9.442
- **Magnitude:** 106.84 | **LOC:** 421 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.8769%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 60.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 68`, `args: 49`, `func_start: 35`, `class_start: 39`
* *Risk/State:* `high_risk_execution: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 19`, `concurrency: 20`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 50`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/action-sheet/test/translucent/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.577 IQR)
- **Top Global Matches:** file_cluster_8: 8.577, file_cluster_0: 9.39, file_cluster_7: 9.423
- **Magnitude:** 104.36 | **LOC:** 388 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (30.5094%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `presentBasic` (Impact: 17.3 | O(N^4) | DB: 1)
  * `presentScroll` (Impact: 9.4 | O(N^4) | DB: 1)
  * `presentScrollNoCancel` (Impact: 9.0 | O(N^4))
  * `presentNoBackdropDismiss` (Impact: 6.4 | O(N^4))
  * `presentAlert` (Impact: 6.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 49`, `args: 46`, `func_start: 43`, `class_start: 26`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/segment/test/custom/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.533 IQR)
- **Top Global Matches:** file_cluster_8: 8.533, file_cluster_0: 9.133, file_cluster_7: 9.414
- **Magnitude:** 104.18 | **LOC:** 401 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 90`, `class_start: 151`
* *Risk/State:* `safety_bypasses: 20`
* *Architecture:* `io: 2`, `api: 82`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/test/safe-area/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.064 IQR)
- **Top Global Matches:** file_cluster_8: 8.064, file_cluster_7: 8.805, file_cluster_0: 8.859
- **Magnitude:** 97.46 | **LOC:** 263 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (30.3065%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateModalDiagnostics` (Impact: 21.5 | O(N^3))
  * `createModalContent` (Impact: 11.1 | O(N^4))
  * `presentCenteredDialog` (Impact: 9.4 | O(N^3))
  * `updateDiagnostics` (Impact: 5.4 | O(N^2))
    * *Intent:* // Update diagnostic info
  * `presentSheetModal` (Impact: 4.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 37`, `args: 20`, `func_start: 15`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 2`
* *Architecture:* `io: 2`, `api: 15`, `concurrency: 15`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/test/spec/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.686 IQR)
- **Top Global Matches:** file_cluster_8: 7.686, file_cluster_0: 8.242, file_cluster_7: 8.59
- **Magnitude:** 94.48 | **LOC:** 534 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.9639%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createModal` (Impact: 39.5 | O(N^6) | DB: 3)
  * `presentModal` (Impact: 6.3 | O(N^2))
  * `enterAnimation` (Impact: 4.4 | O(N^3))
  * `leaveAnimation` (Impact: 4.4 | O(N^3))
  * `addFavorite` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 32`, `args: 25`, `func_start: 7`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 5`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 13`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/rollup.config.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.897 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.254 IQR)
- **Top Global Matches:** file_cluster_8: 6.897, file_cluster_0: 7.421, file_cluster_13: 7.712
- **Magnitude:** 81.07 | **LOC:** 21 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.8869%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 3`, `args: 1`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin-typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/rollup.config.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.036 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.411 IQR)
- **Top Global Matches:** file_cluster_8: 7.036, file_cluster_0: 7.466, file_cluster_13: 7.759
- **Magnitude:** 80.03 | **LOC:** 18 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.2426%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 3`, `args: 1`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin-typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/popover/test/basic/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.652 IQR)
- **Top Global Matches:** file_cluster_8: 8.652, file_cluster_0: 8.988, file_cluster_7: 9.373
- **Magnitude:** 79.1 | **LOC:** 232 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (59.3059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `connectedCallback` (Impact: 6.6 | O(N^3) | DB: 3)
  * `connectedCallback` (Impact: 3.8 | O(N^3) | DB: 1)
  * `connectedCallback` (Impact: 3.5 | O(N^3) | DB: 1)
  * `connectedCallback` (Impact: 3.5 | O(N^3) | DB: 1)
  * `presentPopover` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 29`, `args: 20`, `func_start: 19`, `class_start: 9`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 14`, `duplicate_logic: 12`
* *Architecture:* `io: 2`, `api: 13`, `concurrency: 3`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/item/test/reorder/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.648 IQR)
- **Top Global Matches:** file_cluster_8: 10.648, file_cluster_0: 10.998, file_cluster_7: 11.175
- **Magnitude:** 78.64 | **LOC:** 138 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (70.7917%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initGroup` (Impact: 11.2 | O(N^2) | DB: 4)
  * `renderSlidingGroup` (Impact: 11.1 | O(N^4) | DB: 2)
  * `renderGroup` (Impact: 7.5 | O(N^3) | DB: 2)
  * `toggle` (Impact: 5.5 | O(N^2) | DB: 2)
  * `clickedButton` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 15`, `args: 9`, `func_start: 8`, `class_start: 18`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 33`
* *Architecture:* `io: 2`, `api: 5`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/popover/utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.486 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.796 IQR)
- **Top Global Matches:** file_cluster_8: 10.486, file_cluster_7: 10.824, file_cluster_15: 11.027
- **Magnitude:** 76.86 | **LOC:** 1028 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (11.1224%), Tech Debt (8.1144%)
**Top Internal Functions/Classes:**
  * `calculateWindowAdjustment` (Impact: 95.0 | O(N^2) | DB: 11)
    * *Intent:* /** * Calculates where the arrow positioning * should be relative to the popover content.
  * `configureKeyboardInteraction` (Impact: 94.0 | O(N^2) | DB: 1)
  * `getPopoverPosition` (Impact: 87.8 | O(N^2) | DB: 1)
    * *Intent:* /** * Returns `true` if `el` has been designated * as a trigger element for an ion-popover. */
  * `configureTriggerInteraction` (Impact: 70.3 | O(N^4) | DB: 2)
  * `configureDismissInteraction` (Impact: 47.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 133`, `args: 53`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`, `planned_debt: 1`
* *Architecture:* `api: 25`, `concurrency: 15`, `import: 2`
* *Defense:* `safety: 10`, `doc: 53`, `immutability_locks: 68`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` helpers, popover-interface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/range/test/custom/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.894 IQR)
- **Top Global Matches:** file_cluster_8: 7.894, file_cluster_7: 8.577, file_cluster_0: 8.749
- **Magnitude:** 76.56 | **LOC:** 446 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateDisplayedKnobValues` (Impact: 5.4 | O(2^N))
  * `updateDisplayedKnobValues` (Impact: 2.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 60`, `func_start: 4`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 42`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 61`
* *Defense:* `safety: 14`, `doc: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.bundle.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/action-sheet/test/standalone/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.776 IQR)
- **Top Global Matches:** file_cluster_8: 7.776, file_cluster_7: 8.726, file_cluster_1: 8.777
- **Magnitude:** 75.46 | **LOC:** 378 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `presentScroll` (Impact: 8.6 | O(N^4) | DB: 1)
  * `presentScrollNoCancel` (Impact: 8.3 | O(N^4))
  * `presentBasic` (Impact: 6.5 | O(N^4))
  * `presentIcons` (Impact: 6.5 | O(N^4))
  * `presentNoBackdropDismiss` (Impact: 5.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `args: 55`, `func_start: 59`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 3`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.css, styles.css, ionic.js, scripts.js, ionic.esm.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/alert/alert.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.185 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.794 IQR)
- **Top Global Matches:** file_cluster_4: 13.185, file_cluster_0: 13.204, file_cluster_17: 13.309
- **Magnitude:** 73.55 | **LOC:** 843 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (49.2246%), Tech Debt (8.2396%)
**Top Internal Functions/Classes:**
  * `renderInput` (Impact: 75.5 | O(N^5) | DB: 1)
  * `render` (Impact: 49.5 | O(N^4) | DB: 11)
  * `onKeydown` (Impact: 47.0 | O(N^2) | DB: 7)
    * *Intent:* /** * If `true`, the alert will animate. */ /** * Additional attributes to pass to the alert. */ /**...
  * `inputsChanged` (Impact: 34.0 | O(N^2) | DB: 4)
    * *Intent:* * Emitted before the alert has presented. * Shorthand for ionAlertWillPresent. */ /** * Emitted befo...
  * `present` (Impact: 32.0 | O(2^N) | DB: 6)
    * *Intent:* // Get the first input that is not disabled and the checked one
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 145`, `args: 67`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 43`, `state_mutation: 209`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 10`, `concurrency: 80`, `import: 21`
* *Defense:* `safety: 21`, `doc: 40`, `sync_locks: 3`, `immutability_locks: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` button-active, ios.leave, gesture, core, sanitization, helpers, config, md.leave...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/item-sliding/item-sliding.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.962 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.344 IQR)
- **Top Global Matches:** file_cluster_4: 13.962, file_cluster_13: 14.148, file_cluster_0: 14.315
- **Magnitude:** 73.03 | **LOC:** 519 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (49.1698%), Tech Debt (31.9556%)
**Top Internal Functions/Classes:**
  * `onMove` (Impact: 46.6 | O(N^2) | DB: 12)
  * `open` (Impact: 36.5 | O(N^1) | DB: 17)
    * *Intent:* /** * Get the amount the item is open in pixels. */
  * `setOpenAmount` (Impact: 33.9 | O(N^2) | DB: 21)
  * `updateOptions` (Impact: 25.4 | O(N^2) | DB: 9)
  * `onEnd` (Impact: 19.4 | O(N^1) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 54`, `args: 32`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 387`, `orphaned_logic: 6`
* *Architecture:* `api: 1`, `concurrency: 88`, `import: 10`
* *Defense:* `safety: 2`, `doc: 19`, `immutability_locks: 28`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` core, gesture, logging, menu-interface, helpers, content, watch-options, ionic-global...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `core/src/components/fab-button/fab-button.tsx` (TYPESCRIPT) | Magnitude: 6.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 39, state_mutation: 26, decorators: 24
- `core/src/components/item-sliding/test/basic/index.html` (HTML) | Magnitude: 51.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 169, class_start: 63, api: 24, structural_boundaries: 21
- `core/src/components/breadcrumbs/breadcrumbs.tsx` (TYPESCRIPT) | Magnitude: 11.27 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 28, structural_boundaries: 27, branch: 23
- `core/src/components/back-button/test/basic/index.html` (HTML) | Magnitude: 30.28 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 171, class_start: 80, decorators: 38, api: 18
- `core/src/components/tab-button/test/a11y/index.html` (HTML) | Magnitude: 25.06 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, class_start: 25, args: 23, decorators: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `core/src/components/toggle/test/enable-on-off-labels/toggle.e2e.ts` (TYPESCRIPT) | Magnitude: 0.94 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 56, events: 38, listeners: 19, structural_boundaries: 10
- `packages/angular/test/base/src/app/standalone/overlay-controllers/overlay-controllers.component.html` (HTML) | Magnitude: 18.64 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 5, events: 5, indent_spaces: 5, structural_boundaries: 1
- `packages/angular/test/apps/ng19/src/app/standalone/programmatic-modal/programmatic-modal.component.html` (HTML) | Magnitude: 10.52 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 1, events: 1
- `packages/angular/test/base/src/app/standalone/programmatic-modal/programmatic-modal.component.html` (HTML) | Magnitude: 10.52 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 1, events: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `core/src/components/picker/picker.tsx` (TYPESCRIPT) | Magnitude: 30.32 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, state_mutation: 114, branch: 53, structural_boundaries: 53
- `packages/angular/common/src/utils/proxy.ts` (TYPESCRIPT) | Magnitude: 3.89 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, args: 16, func_start: 10
- `packages/angular/common/src/directives/control-value-accessors/value-accessor.ts` (TYPESCRIPT) | Magnitude: 16.6 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, state_mutation: 62, args: 29, structural_boundaries: 25
- `core/src/utils/input-shims/hacks/input-blurring.ts` (TYPESCRIPT) | Magnitude: 2.95 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 14, args: 8, immutability_locks: 8
- `packages/react/src/contexts/NavContext.ts` (TYPESCRIPT) | Magnitude: 6.49 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 28, args: 20, func_start: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `core/src/components/loading/loading.tsx` (TYPESCRIPT) | Magnitude: 23.37 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 170, concurrency: 73, state_mutation: 70, structural_boundaries: 47
- `core/src/components/fab/test/custom-size/fab.e2e.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, args: 4, concurrency: 4
- `packages/angular/src/directives/navigation/ion-back-button.ts` (TYPESCRIPT) | Magnitude: 0.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, decorators: 4, import: 3
- `packages/vue/test/base/src/shims-vue.d.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, branch: 1, api: 1
- `core/src/components/img/img.tsx` (TYPESCRIPT) | Magnitude: 13.49 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 62, structural_boundaries: 22, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `core/src/components/input/input-interface.ts` (TYPESCRIPT) | Magnitude: 1.82 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, branch: 4, class_start: 3
- `core/src/components/route/route-interface.ts` (TYPESCRIPT) | Magnitude: 1.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, api: 3, args: 1, class_start: 1
- `core/src/utils/animation/animation-interface.ts` (TYPESCRIPT) | Magnitude: 2.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, args: 34, structural_boundaries: 32, func_start: 32
- `packages/react/src/components/react-component-lib/interfaces.ts` (TYPESCRIPT) | Magnitude: 1.79 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, branch: 10, structural_boundaries: 10, safety_bypasses: 6
- `packages/angular/common/src/directives/navigation/nav-params.ts` (TYPESCRIPT) | Magnitude: 0.64 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, api: 3, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `core/src/components/select-popover/select-popover.tsx` (TYPESCRIPT) | Magnitude: 11.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 41, state_mutation: 33, args: 23
- `core/src/global/config.ts` (TYPESCRIPT) | Magnitude: 8.01 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 30, branch: 14, args: 14
- `core/src/components/select-modal/select-modal.tsx` (TYPESCRIPT) | Magnitude: 11.07 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 48, structural_boundaries: 39, args: 23
- `packages/vue/src/components/IonTabBar.ts` (TYPESCRIPT) | Magnitude: 21.05 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 176, branch: 48, structural_boundaries: 32, immutability_locks: 29
- `packages/react/src/components/CreateAnimation.tsx` (TYPESCRIPT) | Magnitude: 4.21 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 151, branch: 80, structural_boundaries: 27, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/react/test/base/src/pages/Tabs.tsx` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, ui_framework: 10, generics: 10, structural_boundaries: 9
- `packages/react/src/components/IonOverlayManager.tsx` (TYPESCRIPT) | Magnitude: 0.82 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 14, args: 8, func_start: 8
- `packages/react/test/base/src/pages/overlay-hooks/ModalHook.tsx` (TYPESCRIPT) | Magnitude: 2.72 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 36, args: 31, ui_framework: 27
- `packages/react-router/test/base/src/pages/routing/Tabs.tsx` (TYPESCRIPT) | Magnitude: 0.65 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, ui_framework: 22, generics: 22, structural_boundaries: 15
- `packages/react/src/components/react-component-lib/createComponent.tsx` (TYPESCRIPT) | Magnitude: 5.74 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 24, branch: 15, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `core/src/components/popover/test/inline/popover.e2e.ts` (TYPESCRIPT) | Magnitude: 2.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 18, concurrency: 14, args: 7
- `core/src/utils/animation/test/hooks/animation.e2e.ts` (TYPESCRIPT) | Magnitude: 3.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 37, indent_spaces: 30, concurrency: 28, test: 14
- `core/src/utils/animation/test/basic/animation.e2e.ts` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, concurrency: 8, args: 5
- `core/src/components/router/test/guards/test.utils.ts` (TYPESCRIPT) | Magnitude: 1.19 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, api: 4, concurrency: 4, args: 2
- `core/src/components/action-sheet/test/basic/action-sheet-rendering.e2e.ts` (TYPESCRIPT) | Magnitude: 4.25 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 30, concurrency: 27, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/react/src/hooks/__tests__/hooks.spec.tsx` (TYPESCRIPT) | Magnitude: 0.21 | Delta: **0.275 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, test: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `core/src/components/toast/animations/md.enter.ts` (TYPESCRIPT) | Magnitude: 1.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, branch: 7, immutability_locks: 7
- `packages/angular/test/base/e2e/src/lazy/standalone-routing.spec.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, test: 4, concurrency: 4
- `core/src/components/picker-column-option/test/a11y/index.html` (HTML) | Magnitude: 16.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, class_start: 5, structural_boundaries: 4, decorators: 4
- `core/src/utils/test/playwright/matchers/index.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, import: 3, indent_spaces: 3, api: 1
- `core/src/components/popover/test/safe-area/index.html` (HTML) | Magnitude: 46.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 19, class_start: 13, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/angular/test/base/src/environments/environment.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, dead_code: 1, immutability_locks: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `core/src/components/datetime/datetime.tsx` -> Churn: **56.24%** | Cog Load: 54.304% | Debt: 8.2495%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/components/modal/test/safe-area/index.html` -> **Shane** (100.0% isolated ownership) | Magnitude: 97.46
- `core/src/components/popover/utils.ts` -> **Shane** (100.0% isolated ownership) | Magnitude: 76.86
- `core/src/components/range/test/custom/index.html` -> **Brandy Smith** (100.0% isolated ownership) | Magnitude: 76.56
- `core/src/components/textarea/test/validation/index.html` -> **Shane** (100.0% isolated ownership) | Magnitude: 69.76
- `core/src/components/input/test/validation/index.html` -> **Shane** (100.0% isolated ownership) | Magnitude: 69.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/global/ionic-global.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `core/src/components/router/utils/path.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 94.0699%)
- `core/src/utils/animation/animation.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 54.0845%)
- `core/src/utils/test/playwright/page/event-spy.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/components/router/utils/interface.ts` -> **Severity: 2681.701** (Blast Radius: 26.826 * Doc Risk: 99.9665%)
- `core/src/components/route/route-interface.ts` -> **Severity: 775.899** (Blast Radius: 23.277 * Doc Risk: 33.3333%)
- `core/src/global/ionic-global.ts` -> **Severity: 451.728** (Blast Radius: 7.54 * Doc Risk: 59.9109%)
- `core/src/components/datetime/datetime-interface.ts` -> **Severity: 391.057** (Blast Radius: 3.912 * Doc Risk: 99.9635%)
- `core/src/utils/theme.ts` -> **Severity: 353.022** (Blast Radius: 3.549 * Doc Risk: 99.4708%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
