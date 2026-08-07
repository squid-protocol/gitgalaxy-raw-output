# ARCHITECTURAL_BRIEF: ionic-framework
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/ionic-framework` |
| **Timestamp** | `2026-08-07T04:15:19.051442+00:00` |
| **Scan Duration** | `6.26s` |
| **Git Branch** | `main` |
| **Git Commit** | `4d81b026a72e57a4b330de15a2053fa86f0084ca` |
| **Git Remote** | `https://github.com/ionic-team/ionic-framework.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1372 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.973`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1629 | 69.0% |
| file_cluster_13 | 368 | 15.6% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 19.6 | 5.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 22.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.8 | 4.0 | 3.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 31.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 57.3 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 87.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.9 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 85.0 | 1.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 15.9 | 0.0 | 0.0 |
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

- `isViewVisible` (@ `packages/react-router/src/ReactRouter/StackManager.tsx`) -> Impact: **210.8** | LOC: 375
- `onDragEnd` (@ `core/src/components/modal/gestures/sheet.ts`) -> Impact: **203.7** | LOC: 554
  * *Intent:* /**
- `handleFocus` (@ `core/src/components/menu/menu.tsx`) -> Impact: **180.2** | LOC: 443
- `createIonRouter` (@ `packages/vue-router/src/router.ts`) -> Impact: **155.6** | LOC: 341
  * *Intent:* // TODO(FW-2969): types
- `handleHistoryChange` (@ `packages/vue-router/src/router.ts`) -> Impact: **129.5** | LOC: 219
  * *Intent:* /** * We need to exclude tab switches/tab
- `componentWillLoad` (@ `core/src/components/modal/modal.tsx`) -> Impact: **118.1** | LOC: 382
  * *Intent:* * If `true`, the modal will animate. */ /** * The element that presented the modal. This is used for card presentation effects * and for stacking mult...
- `iosTransitionAnimation` (@ `core/src/utils/transition/ios.transition.ts`) -> Impact: **117.7** | LOC: 344
  * *Intent:* /** * The scaled title should (roughly) overlap the back button. This ensures that * the back button and title overlap during the animation. Note that...
- `setup` (@ `packages/vue/src/components/IonRouterOutlet.ts`) -> Impact: **109.4** | LOC: 378
- `renderMonth` (@ `core/src/components/datetime/datetime.tsx`) -> Impact: **102.6** | LOC: 216
- `moveToNextBreakpoint` (@ `core/src/components/modal/modal.tsx`) -> Impact: **100.5** | LOC: 209
  * *Intent:* * Emitted before the modal has presented, but after the component * has been mounted in the DOM. * This event exists so iOS can run the entering * tra...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/docs` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/vue/test/base/src/views` | 21 | 542.03 | 7.84% | 0.0% |
| `core/src/components/action-sheet/test/basic` | 5 | 231.08 | 48.75% | 0.0% |
| `core/src/themes/test/css-variables` | 1 | 180.12 | 11.69% | 0.0% |
| `packages/react-router/src/ReactRouter` | 8 | 168.74 | 56.27% | 29.68% |
| `packages/react-router` | 7 | 162.19 | 5.71% | 0.0% |
| `core/src/components/action-sheet/test/standalone` | 1 | 160.36 | 0.0% | 0.0% |
| `core/src/components/action-sheet/test/translucent` | 2 | 148.71 | 63.42% | 0.0% |
| `packages/react/src/components` | 26 | 147.15 | 26.03% | 13.23% |
| `core/scripts` | 6 | 144.1 | 21.22% | 16.62% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/react/jest.setup.js` -> **100.0%** Exposure
- `core/src/components/header/header.utils.ts` -> **100.0%** Exposure
- `core/src/components/reorder-group/reorder-group-interface.ts` -> **100.0%** Exposure
- `core/src/utils/animation/animation.ts` -> **100.0%** Exposure
- `core/src/utils/content/content.utils.spec.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `core/src/components/accordion-group/accordion-group.tsx` -> **100.0%** Exposure
- `core/src/components/accordion/accordion.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/action-sheet.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/test/basic/fixture.ts` -> **100.0%** Exposure
- `core/src/components/alert/alert.tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/src/components/datetime/test/manipulation.spec.ts` -> **0** Orphaned Functions | **114** Duplicates
- `core/src/components/router/test/matching.spec.tsx` -> **0** Orphaned Functions | **67** Duplicates
- `core/src/utils/keyboard/test/keyboard.spec.ts` -> **0** Orphaned Functions | **63** Duplicates
- `core/src/utils/animation/test/animation.spec.ts` -> **1** Orphaned Functions | **59** Duplicates
- `core/src/components/range/test/range.spec.ts` -> **1** Orphaned Functions | **52** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2793` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `core/src/components/header/header.tsx` (TYPESCRIPT) -> Cumulative Risk: **675.71**
- **Archetype:** `file_cluster_4` (Distance: 12.731 IQR)
- **Magnitude:** 24.32 | **LOC:** 238 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.7079%)
- **Heaviest Functions:** `checkCollapsibleHeader` (Impact: 17.9), `setupCondenseHeader` (Impact: 16.5), `destroyCollapsibleHeader` (Impact: 9.5)

### 2. `packages/react/src/components/createControllerComponent.tsx` (TYPESCRIPT) -> Cumulative Risk: **675.06**
- **Archetype:** `file_cluster_4` (Distance: 14.519 IQR)
- **Magnitude:** 21.35 | **LOC:** 128 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1999%)
- **Heaviest Functions:** `present` (Impact: 17.4), `dismiss` (Impact: 12.6), `componentDidUpdate` (Impact: 12.4)

### 3. `packages/angular/common/src/directives/control-value-accessors/value-accessor.ts` (TYPESCRIPT) -> Cumulative Risk: **668.3**
- **Archetype:** `file_cluster_11` (Distance: 13.929 IQR)
- **Magnitude:** 17.15 | **LOC:** 158 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (92.4835%)
- **Heaviest Functions:** `setIonicClasses` (Impact: 12.0), `ngAfterViewInit` (Impact: 11.5), `getClasses` (Impact: 8.6)

### 4. `packages/react/src/components/react-component-lib/createOverlayComponent.tsx` (TYPESCRIPT) -> Cumulative Risk: **645.05**
- **Archetype:** `file_cluster_4` (Distance: 14.431 IQR)
- **Magnitude:** 24.43 | **LOC:** 143 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.615%)
- **Heaviest Functions:** `componentDidUpdate` (Impact: 14.8), `dismiss` (Impact: 14.4), `present` (Impact: 11.1)

### 5. `core/src/components/img/img.tsx` (TYPESCRIPT) -> Cumulative Risk: **639.95**
- **Archetype:** `file_cluster_13` (Distance: 13.1 IQR)
- **Magnitude:** 12.95 | **LOC:** 157 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (93.066%)
- **Heaviest Functions:** `addIO` (Impact: 17.0), `isDraggable` (Impact: 16.4), `removeIO` (Impact: 3.8)

### 6. `core/src/utils/tap-click/index.ts` (TYPESCRIPT) -> Cumulative Risk: **639.8**
- **Archetype:** `file_cluster_4` (Distance: 11.343 IQR)
- **Magnitude:** 21.99 | **LOC:** 182 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.8625%), State Flux (90.064%)
- **Heaviest Functions:** `startTapClick` (Impact: 64.8), `setActivatedElement` (Impact: 21.2), `getActivatableTarget` (Impact: 16.7)

### 7. `core/src/components/picker/picker.tsx` (TYPESCRIPT) -> Cumulative Risk: **628.81**
- **Archetype:** `file_cluster_11` (Distance: 12.768 IQR)
- **Magnitude:** 26.26 | **LOC:** 571 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9229%)
- **Heaviest Functions:** `onPointerDown` (Impact: 21.9), `selectSingleColumn` (Impact: 18.0), `enterInputMode` (Impact: 13.8)

### 8. `packages/react-router/src/ReactRouter/StackManager.tsx` (TYPESCRIPT) -> Cumulative Risk: **628.24**
- **Archetype:** `file_cluster_4` (Distance: 13.276 IQR)
- **Magnitude:** 85.79 | **LOC:** 468 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.993%), Safety Score (97.9349%)
- **Heaviest Functions:** `isViewVisible` (Impact: 210.8), `transitionPage` (Impact: 72.4), `handlePageTransition` (Impact: 72.0)

### 9. `core/src/components/menu/menu.tsx` (TYPESCRIPT) -> Cumulative Risk: **621.56**
- **Archetype:** `file_cluster_4` (Distance: 13.858 IQR)
- **Magnitude:** 84.08 | **LOC:** 885 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4778%)
- **Heaviest Functions:** `handleFocus` (Impact: 180.2), `onEnd` (Impact: 39.2), `assert` (Impact: 20.4)

### 10. `core/src/components/item-sliding/item-sliding.tsx` (TYPESCRIPT) -> Cumulative Risk: **613.89**
- **Archetype:** `file_cluster_4` (Distance: 13.969 IQR)
- **Magnitude:** 72.47 | **LOC:** 519 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.8339%)
- **Heaviest Functions:** `open` (Impact: 36.5), `onMove` (Impact: 31.6), `setOpenAmount` (Impact: 23.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/docs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `core/src/components/action-sheet/test/basic/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.412 IQR)
- **Top Global Matches:** file_cluster_8: 8.412, file_cluster_7: 9.232, file_cluster_0: 9.247
- **Magnitude:** 205.88 | **LOC:** 512 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.4093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `presentBasic` (Impact: 8.6)
  * `presentScroll` (Impact: 7.2)
  * `presentWithCssClass` (Impact: 6.2)
  * `presentScrollNoCancel` (Impact: 6.0)
  * `presentIcons` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 72`, `args: 64`, `func_start: 60`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 3`, `duplicate_logic: 50`
* *Architecture:* `io: 2`, `api: 20`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/themes/test/css-variables/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.638 IQR)
- **Top Global Matches:** file_cluster_8: 9.638, file_cluster_0: 9.887, file_cluster_7: 10.269
- **Magnitude:** 180.12 | **LOC:** 1190 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.6883%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `togglePalette` (Impact: 26.2)
  * `createModal` (Impact: 6.6)
  * `presentActionSheet` (Impact: 4.3)
  * `presentLoading` (Impact: 2.6)
  * `presentAlert` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 66`, `args: 149`, `func_start: 17`, `class_start: 535`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 20`, `dead_code: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 40`, `api: 61`, `concurrency: 15`
* *Defense:* `safety: 10`, `doc: 5`, `immutability_locks: 21`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, default.css, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vue/test/base/src/views/Overlays.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.713 IQR)
- **Top Global Matches:** file_cluster_8: 8.713, file_cluster_1: 9.31, file_cluster_7: 9.473
- **Magnitude:** 178.84 | **LOC:** 421 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (17.3105%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `present` (Impact: 45.2)
  * `setup` (Impact: 43.8)
  * `openModal` (Impact: 4.3)
  * `onIonModalDidDismiss` (Impact: 4.1)
  * `openPopover` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 68`, `args: 49`, `func_start: 35`, `class_start: 39`
* *Risk/State:* `high_risk_execution: 3`, `duplicate_logic: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 19`, `concurrency: 20`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 50`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/action-sheet/test/standalone/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.781 IQR)
- **Top Global Matches:** file_cluster_8: 7.781, file_cluster_7: 8.726, file_cluster_1: 8.783
- **Magnitude:** 160.36 | **LOC:** 378 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `presentScroll` (Impact: 6.0)
  * `presentScrollNoCancel` (Impact: 5.7)
  * `openActionSheet` (Impact: 5.6)
  * `openActionSheet` (Impact: 5.3)
  * `presentBasic` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `args: 55`, `func_start: 59`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 51`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 3`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, core.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/action-sheet/test/translucent/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.551 IQR)
- **Top Global Matches:** file_cluster_8: 8.551, file_cluster_0: 9.324, file_cluster_7: 9.395
- **Magnitude:** 147.86 | **LOC:** 388 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.4385%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `presentBasic` (Impact: 8.3)
  * `presentScroll` (Impact: 6.5)
  * `presentScrollNoCancel` (Impact: 6.0)
  * `presentNoBackdropDismiss` (Impact: 3.4)
  * `presentAlert` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 49`, `args: 46`, `func_start: 43`, `class_start: 26`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 36`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/test/multiple/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.186 IQR)
- **Top Global Matches:** file_cluster_8: 7.186, file_cluster_2: 7.557, file_cluster_0: 7.953
- **Magnitude:** 110.88 | **LOC:** 128 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 15`, `func_start: 1`, `class_start: 15`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 9`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, scripts.js, ionic.bundle.css, styles.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/segment/test/custom/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.533 IQR)
- **Top Global Matches:** file_cluster_8: 8.533, file_cluster_0: 9.133, file_cluster_7: 9.414
- **Magnitude:** 104.18 | **LOC:** 401 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 90`, `class_start: 151`
* *Risk/State:* `safety_bypasses: 20`
* *Architecture:* `io: 2`, `api: 82`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/button/test/perf/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.512 IQR)
- **Top Global Matches:** file_cluster_8: 9.512, file_cluster_7: 10.394, file_cluster_1: 10.514
- **Magnitude:** 103.66 | **LOC:** 4452 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changeColor` (Impact: 3.9)
  * `toggleDisabled` (Impact: 2.0)
  * `clickedButton` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 6`, `func_start: 3`, `class_start: 4415`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/datetime.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.796 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.283 IQR)
- **Top Global Matches:** file_cluster_8: 12.796, file_cluster_13: 12.818, file_cluster_0: 12.93
- **Magnitude:** 92.1 | **LOC:** 2764 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (54.304%), Tech Debt (26.9479%)
**Top Internal Functions/Classes:**
  * `renderMonth` (Impact: 102.6)
  * `processValue` (Impact: 65.2)
    * *Intent:* /** * When defined, will force the datetime to render the month * containing the specified date. Cur...
  * `renderIndividualDatePickerColumns` (Impact: 33.5)
    * *Intent:* /** * Which values you want to select. `"date"` will show * a calendar picker to select the month, d...
  * `renderDatetime` (Impact: 28.2)
  * `getHeaderSelectedDateText` (Impact: 25.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 140`, `args: 64`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 418`, `dead_code: 3`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 13`, `import: 21`
* *Defense:* `safety: 28`, `doc: 24`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` data, theme, logging, helpers, interface, core, datetime-interface, focus-visible...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/test/show-adjacent-days/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.961 IQR)
- **Top Global Matches:** file_cluster_8: 8.961, file_cluster_2: 9.18, file_cluster_0: 9.276
- **Magnitude:** 91.86 | **LOC:** 329 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.745%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isDateEnabled` (Impact: 9.2)
  * `isDateEnabled` (Impact: 7.3)
  * `initCalendarMonthChangeObserver` (Impact: 5.9)
  * `isDateEnabled` (Impact: 5.6)
  * `constructor` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 53`, `args: 37`, `func_start: 16`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 16`, `duplicate_logic: 9`
* *Architecture:* `io: 2`, `api: 24`, `concurrency: 4`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, scripts.js, ionic.bundle.css, styles.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/modal.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.023 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.58 IQR)
- **Top Global Matches:** file_cluster_4: 14.023, file_cluster_13: 14.046, file_cluster_0: 14.129
- **Magnitude:** 87.13 | **LOC:** 1669 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (49.9288%), Tech Debt (34.1081%)
**Top Internal Functions/Classes:**
  * `componentWillLoad` (Impact: 118.1)
    * *Intent:* * If `true`, the modal will animate. */ /** * The element that presented the modal. This is used for...
  * `moveToNextBreakpoint` (Impact: 100.5)
    * *Intent:* * Emitted before the modal has presented, but after the component * has been mounted in the DOM. * T...
  * `initParentRemovalObserver` (Impact: 80.2)
  * `cardOnDismiss` (Impact: 24.1)
  * `render` (Impact: 22.2)
    * *Intent:* /** * When binding values in frameworks such as Angular * it is possible for the value to be set aft...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 93`, `args: 43`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 267`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `concurrency: 111`, `import: 28`
* *Defense:* `safety: 15`, `doc: 59`, `sync_locks: 1`, `immutability_locks: 31`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` ios.enter, sheet, ios.leave, content, theme, logging, framework-delegate, overlays-interface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/segment/test/basic/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.381 IQR)
- **Top Global Matches:** file_cluster_8: 11.381, file_cluster_0: 11.503, file_cluster_7: 11.941
- **Magnitude:** 86.76 | **LOC:** 319 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.2411%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toggleValue` (Impact: 11.1)
  * `toggleDisabled` (Impact: 9.2)
  * `updateSegmentButtons` (Impact: 5.8)
  * `toggleSwipeGesture` (Impact: 3.8)
  * `listenForEvent` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 18`, `args: 73`, `func_start: 8`, `class_start: 117`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `io: 2`, `api: 19`, `concurrency: 2`
* *Defense:* `safety: 21`, `doc: 1`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/src/ReactRouter/StackManager.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.276 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.971 IQR)
- **Top Global Matches:** file_cluster_4: 13.276, file_cluster_13: 13.466, file_cluster_11: 13.568
- **Magnitude:** 85.79 | **LOC:** 468 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.7706%), Tech Debt (43.4325%)
**Top Internal Functions/Classes:**
  * `isViewVisible` (Impact: 210.8)
  * `transitionPage` (Impact: 72.4)
  * `handlePageTransition` (Impact: 72.0)
  * `setupRouterOutlet` (Impact: 51.0)
    * *Intent:* /** * The view should only be transitioned in the following cases: * 1. Performing a replace or pop ...
  * `onEnd` (Impact: 19.8)
    * *Intent:* /** * The root url '/' is treated as
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 42`, `args: 27`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 251`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 57`, `import: 5`
* *Defense:* `safety: 11`, `doc: 14`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` react, matchPath, clonePageElement, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/components/menu/menu.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.858 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.536 IQR)
- **Top Global Matches:** file_cluster_4: 13.858, file_cluster_13: 13.978, file_cluster_0: 14.058
- **Magnitude:** 84.08 | **LOC:** 885 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.944%), Tech Debt (62.0582%)
**Top Internal Functions/Classes:**
  * `handleFocus` (Impact: 180.2)
  * `onEnd` (Impact: 39.2)
    * *Intent:* /** * Toggles the menu. If the menu is already open, it will try to close, * otherwise it will try t...
  * `assert` (Impact: 20.4)
    * *Intent:* /** * Toggles the menu. If the menu is already open, it will try to close, * otherwise it will try t...
  * `connectedCallback` (Impact: 18.0)
  * `_setOpen` (Impact: 15.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 78`, `args: 44`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 290`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `concurrency: 100`, `import: 18`
* *Defense:* `safety: 8`, `doc: 39`, `test: 3`, `immutability_locks: 39`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` focus-trap, core, platform, hardware-back-button, cubic-bezier, menu-interface, helpers, interface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/rollup.config.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.897 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.254 IQR)
- **Top Global Matches:** file_cluster_8: 6.897, file_cluster_0: 7.421, file_cluster_13: 7.712
- **Magnitude:** 81.07 | **LOC:** 21 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
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

### `core/src/components/range/test/custom/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.565 IQR)
- **Top Global Matches:** file_cluster_8: 7.565, file_cluster_7: 8.265, file_cluster_2: 8.464
- **Magnitude:** 74.36 | **LOC:** 446 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateDisplayedKnobValues` (Impact: 2.1)
  * `updateDisplayedKnobValues` (Impact: 2.0)
  * `updateDisplayedKnobValues` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 60`, `func_start: 4`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 42`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 61`
* *Defense:* `safety: 9`, `doc: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/test/safe-area/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.055 IQR)
- **Top Global Matches:** file_cluster_8: 8.055, file_cluster_7: 8.795, file_cluster_0: 8.839
- **Magnitude:** 74.26 | **LOC:** 263 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (42.4421%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateModalDiagnostics` (Impact: 11.1)
  * `createModalContent` (Impact: 5.9)
  * `presentCenteredDialog` (Impact: 5.5)
  * `updateDiagnostics` (Impact: 3.7)
    * *Intent:* // Update diagnostic info
  * `presentSheetModal` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 37`, `args: 20`, `func_start: 15`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 15`, `concurrency: 15`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/popover/utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.448 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.822 IQR)
- **Top Global Matches:** file_cluster_8: 10.448, file_cluster_7: 10.782, file_cluster_15: 10.987
- **Magnitude:** 73.78 | **LOC:** 1028 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.1224%), Tech Debt (99.9937%)
**Top Internal Functions/Classes:**
  * `calculateWindowAdjustment` (Impact: 65.0)
    * *Intent:* /** * Calculates where the arrow positioning * should be relative to the popover content.
  * `configureKeyboardInteraction` (Impact: 64.0)
  * `callback` (Impact: 63.8)
  * `getPopoverPosition` (Impact: 60.1)
    * *Intent:* /** * Returns `true` if `el` has been designated * as a trigger element for an ion-popover. */
  * `calculateArrowPosition` (Impact: 34.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 133`, `args: 53`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`, `planned_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `api: 25`, `concurrency: 15`, `import: 2`
* *Defense:* `safety: 10`, `doc: 53`, `immutability_locks: 68`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` popover-interface, helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/fab/test/states/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.961 IQR)
- **Top Global Matches:** file_cluster_8: 7.961, file_cluster_0: 8.451, file_cluster_7: 8.851
- **Magnitude:** 72.78 | **LOC:** 208 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 40`, `class_start: 80`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 54`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/item-sliding/item-sliding.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.969 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.356 IQR)
- **Top Global Matches:** file_cluster_4: 13.969, file_cluster_13: 14.158, file_cluster_0: 14.324
- **Magnitude:** 72.47 | **LOC:** 519 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1698%), Tech Debt (72.8766%)
**Top Internal Functions/Classes:**
  * `open` (Impact: 36.5)
    * *Intent:* /** * Get the amount the item is open in pixels. */
  * `onMove` (Impact: 31.6)
  * `setOpenAmount` (Impact: 23.5)
  * `onEnd` (Impact: 19.4)
  * `updateOptions` (Impact: 17.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 54`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 393`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 1`, `concurrency: 88`, `import: 10`
* *Defense:* `safety: 2`, `doc: 19`, `immutability_locks: 28`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` core, menu-interface, helpers, interface, watch-options, ionic-global, content, gesture...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/alert/test/translucent/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.88 IQR)
- **Top Global Matches:** file_cluster_8: 6.88, file_cluster_7: 8.011, file_cluster_0: 8.07
- **Magnitude:** 70.32 | **LOC:** 362 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `presentAlertPrompt` (Impact: 4.2)
  * `presentAlertRadio` (Impact: 4.2)
  * `presentAlertCheckbox` (Impact: 4.2)
  * `openAlert` (Impact: 3.4)
  * `openAlert` (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `args: 20`, `func_start: 25`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `duplicate_logic: 17`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 3`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ionic.esm.js, ionic.bundle.css, styles.css, scripts.js, ionic.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vue/rollup.config.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.837 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.892 IQR)
- **Top Global Matches:** file_cluster_8: 6.837, file_cluster_13: 7.445, file_cluster_0: 7.476
- **Magnitude:** 70.05 | **LOC:** 27 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2784%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`, `args: 1`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin-node-resolve, plugin-typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/scripts/treeshaking.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.502 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.948 IQR)
- **Top Global Matches:** file_cluster_8: 9.502, file_cluster_13: 9.725, file_cluster_4: 9.909
- **Magnitude:** 66.64 | **LOC:** 95 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.6579%), Tech Debt (99.7379%)
**Top Internal Functions/Classes:**
  * `getMainEntry` (Impact: 9.5)
  * `resolve` (Impact: 9.0)
  * `main` (Impact: 8.6)
  * `check` (Impact: 7.6)
  * `isDirectory` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 17`, `args: 9`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 1`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `api: 4`, `concurrency: 5`, `import: 4`
* *Defense:* `safety: 5`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.323
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fs, rollup, path, plugin-virtual
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `core/src/components/fab-button/fab-button.tsx` (TYPESCRIPT) | Magnitude: 5.57 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 39, state_mutation: 26, decorators: 24
- `core/src/components/item-sliding/test/basic/index.html` (HTML) | Magnitude: 43.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 169, class_start: 63, api: 24, structural_boundaries: 21
- `core/src/components/breadcrumbs/breadcrumbs.tsx` (TYPESCRIPT) | Magnitude: 9.47 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 28, structural_boundaries: 27, branch: 23
- `packages/angular/common/src/providers/dom-controller.ts` (TYPESCRIPT) | Magnitude: 2.05 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 14, args: 10, func_start: 9
- `core/src/components/back-button/test/basic/index.html` (HTML) | Magnitude: 29.48 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 171, class_start: 80, decorators: 38, api: 18

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
- `core/src/components/picker/picker.tsx` (TYPESCRIPT) | Magnitude: 26.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, state_mutation: 106, branch: 53, structural_boundaries: 53
- `packages/angular/common/src/utils/proxy.ts` (TYPESCRIPT) | Magnitude: 4.84 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, args: 16, func_start: 10
- `packages/angular/common/src/directives/control-value-accessors/value-accessor.ts` (TYPESCRIPT) | Magnitude: 17.15 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, state_mutation: 62, args: 29, structural_boundaries: 25
- `core/src/utils/input-shims/hacks/input-blurring.ts` (TYPESCRIPT) | Magnitude: 5.06 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 14, args: 8, immutability_locks: 8
- `packages/react/src/contexts/NavContext.ts` (TYPESCRIPT) | Magnitude: 5.32 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 28, args: 20, func_start: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `core/src/components/loading/loading.tsx` (TYPESCRIPT) | Magnitude: 22.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 170, concurrency: 73, state_mutation: 70, structural_boundaries: 47
- `core/src/components/fab/test/custom-size/fab.e2e.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, args: 4, concurrency: 4
- `packages/angular/src/directives/navigation/ion-back-button.ts` (TYPESCRIPT) | Magnitude: 0.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, decorators: 4, import: 3
- `packages/vue/test/base/src/shims-vue.d.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, branch: 1, api: 1
- `core/src/components/img/img.tsx` (TYPESCRIPT) | Magnitude: 12.95 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
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
- `packages/angular/common/src/directives/navigation/nav-params.ts` (TYPESCRIPT) | Magnitude: 0.77 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, api: 3, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `core/src/components/select-popover/select-popover.tsx` (TYPESCRIPT) | Magnitude: 9.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 41, state_mutation: 33, args: 22
- `core/src/global/config.ts` (TYPESCRIPT) | Magnitude: 7.01 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 30, branch: 14, args: 14
- `core/src/components/select-modal/select-modal.tsx` (TYPESCRIPT) | Magnitude: 10.11 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 48, structural_boundaries: 39, args: 22
- `packages/vue/src/components/IonTabBar.ts` (TYPESCRIPT) | Magnitude: 14.38 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 176, branch: 48, structural_boundaries: 32, immutability_locks: 29
- `packages/react/src/components/CreateAnimation.tsx` (TYPESCRIPT) | Magnitude: 4.14 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 151, branch: 80, structural_boundaries: 27, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/react/test/base/src/pages/Tabs.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, ui_framework: 10, generics: 10, structural_boundaries: 9
- `packages/react/src/components/IonOverlayManager.tsx` (TYPESCRIPT) | Magnitude: 1.02 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 14, args: 8, func_start: 8
- `packages/react/src/components/react-component-lib/createComponent.tsx` (TYPESCRIPT) | Magnitude: 7.17 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 24, branch: 15, state_mutation: 15
- `packages/react-router/test/base/src/pages/routing/Tabs.tsx` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, ui_framework: 22, generics: 22, structural_boundaries: 15
- `packages/react/test/base/src/pages/overlay-hooks/ModalHook.tsx` (TYPESCRIPT) | Magnitude: 4.56 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 36, args: 30, ui_framework: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `core/src/components/infinite-scroll/infinite-scroll.tsx` (TYPESCRIPT) | Magnitude: 13.75 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 76, structural_boundaries: 16, branch: 14
- `core/src/components/popover/test/inline/popover.e2e.ts` (TYPESCRIPT) | Magnitude: 2.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 18, concurrency: 14, args: 7
- `core/src/utils/animation/test/hooks/animation.e2e.ts` (TYPESCRIPT) | Magnitude: 3.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 37, indent_spaces: 30, concurrency: 28, test: 14
- `core/src/components/nav/test/nav-controller.spec.ts` (TYPESCRIPT) | Magnitude: 59.85 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 716, args: 388, func_start: 383, test: 343
- `core/src/utils/animation/test/basic/animation.e2e.ts` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, concurrency: 8, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/react/src/hooks/__tests__/hooks.spec.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.275 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, test: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `core/src/components/toast/animations/md.enter.ts` (TYPESCRIPT) | Magnitude: 1.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 12, branch: 7, immutability_locks: 7
- `core/src/components/picker-column-option/test/a11y/index.html` (HTML) | Magnitude: 16.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, class_start: 5, structural_boundaries: 4, decorators: 4
- `core/src/utils/test/playwright/matchers/index.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, import: 3, indent_spaces: 3, api: 1
- `packages/angular/test/base/e2e/src/lazy/standalone-routing.spec.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, test: 4, concurrency: 4
- `packages/angular/src/directives/angular-component-lib/utils.ts` (TYPESCRIPT) | Magnitude: 5.79 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 20, args: 17, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/angular/test/base/src/environments/environment.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, dead_code: 1, immutability_locks: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `core/src/components/datetime/datetime.tsx` -> Churn: **57.89%** | Cog Load: 54.304% | Debt: 26.9479%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/components/modal/modal.tsx` -> **Shane** (83.3% isolated ownership) | Magnitude: 87.13
- `core/src/components/menu/menu.tsx` -> **José Rio** (100.0% isolated ownership) | Magnitude: 84.08
- `core/src/components/range/test/custom/index.html` -> **Brandy Smith** (100.0% isolated ownership) | Magnitude: 74.36
- `core/src/components/modal/test/safe-area/index.html` -> **Shane** (100.0% isolated ownership) | Magnitude: 74.26
- `core/src/components/popover/utils.ts` -> **Shane** (100.0% isolated ownership) | Magnitude: 73.78

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

- `core/src/components/router/utils/interface.ts` -> **Severity: 2668.224** (Blast Radius: 26.826 * Doc Risk: 99.4641%)
- `core/src/components/route/route-interface.ts` -> **Severity: 731.422** (Blast Radius: 23.277 * Doc Risk: 31.4225%)
- `core/src/components/datetime/datetime-interface.ts` -> **Severity: 386.328** (Blast Radius: 3.912 * Doc Risk: 98.7546%)
- `core/src/utils/theme.ts` -> **Severity: 339.248** (Blast Radius: 3.549 * Doc Risk: 95.5897%)
- `core/src/global/ionic-global.ts` -> **Severity: 335.31** (Blast Radius: 7.54 * Doc Risk: 44.4708%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
