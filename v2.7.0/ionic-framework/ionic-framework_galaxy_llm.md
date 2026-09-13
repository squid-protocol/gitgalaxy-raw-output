# ARCHITECTURAL_BRIEF: ionic-framework
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ionic-team/ionic-framework.git` |
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
| Total Artifacts | 9447 |
| Analyzed Artifacts (Scanned) | 2501 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6946 |
| Total LOC | 173011 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 26.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.773 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3217 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0864 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 214 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1364 | 102200 | 54.5% |
| HTML | 482 | 49167 | 19.3% |
| CSS | 431 | 15869 | 17.2% |
| JAVASCRIPT | 69 | 3488 | 2.8% |
| JSON | 53 | 1774 | 2.1% |
| MARKDOWN | 26 | 0 | 1.0% |
| PLAINTEXT | 25 | 1 | 1.0% |
| XML | 22 | 0 | 0.9% |
| SHELL | 21 | 342 | 0.8% |
| GROOVY | 3 | 67 | 0.1% |
| JAVA | 3 | 37 | 0.1% |
| DOCKERFILE | 1 | 2 | 0.0% |
| BATCH | 1 | 64 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2450 | 98.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 50 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6946*

**Composition by Extension & Reason:**
- `.png`: 6781x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.md`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4075 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2740 LOC)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9833 LOC), 1x Excluded (Massive Static Asset Blob: 13851 LOC)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (Saturation: Line 55 exceeds 500 chars), 1x Excluded (Saturation: Line 16 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2631 LOC)
- `.html`: 1x Excluded (Saturation: Line 86 exceeds 500 chars), 1x Excluded (Saturation: Line 92 exceeds 500 chars), 1x Excluded (Saturation: Line 61 exceeds 500 chars)
- `.map`: 4x Excluded (Unsupported Extension: '.map')
- `.jpg`: 3x Excluded (Explicitly Denied Extension: '.jpg')
- `.gradle`: 1x Excluded (Machine-Generated Source Code Signature: 20 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.txt`: 1x Excluded (Embedded Array/Matrix Payload: 8000 commas in 2143 LOC)
- `.css`: 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.pro`: 1x Excluded (Unsupported Extension: '.pro')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.3 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 29.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 57.3 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 80.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 85.7 | 1.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 33.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 690 | 215 | 0 | `core/src/components.d.ts` |
| cleanup | 253 | 100 | 0 | `core/src/components.d.ts` |
| guards | 4011 | 797 | 4 | `core/src/components/datetime/datetime.tsx` |
| danger | 2508 | 535 | 2 | `core/src/components.d.ts` |
| concurrency | 13485 | 819 | 14 | `core/src/components/input-otp/test/basic/input-otp.e2e.ts` |
| connectivity | 8339 | 1447 | 8 | `packages/react/test/base/src/theme/variables.css` |
| io | 2976 | 591 | 5 | `core/src/components/router/test/path.spec.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `packages/angular/scripts/build-core.js` |
| time | 222 | 103 | 0 | `core/src/components/searchbar/searchbar.tsx` |
| serialization | 45 | 18 | 0 | `packages/angular/test/base/e2e/src/standalone/value-accessors.spec.ts` |
| regex | 75 | 39 | 0 | `packages/angular/test/base/e2e/src/lazy/router-link.spec.ts` |
| events | 2924 | 735 | 4 | `core/src/components.d.ts` |
| tests | 10907 | 625 | 10 | `packages/vue/test/base/tests/e2e/specs/tabs.cy.js` |
| docs | 5939 | 1073 | 3 | `core/src/components.d.ts` |
| debt | 1024 | 316 | 1 | `core/src/components.d.ts` |
| mutation | 38175 | 1617 | 35 | `core/src/components/button/test/perf/index.html` |
| dead_code | 201 | 112 | 0 | `packages/react/src/components/createControllerComponent.tsx` |
| credential | 0 | 0 | 0 | - |
| threat | 658 | 168 | 0 | `core/src/components.d.ts` |
| ml_ai | 163 | 39 | 0 | `core/src/utils/animation/cubic-bezier.ts` |
| ui | 4717 | 807 | 5 | `core/src/themes/test/colors/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `core/src/components/router/test/path.spec.tsx` (Hits: 84)
- `core/src/components/breadcrumbs/test/collapsed/index.html` (Hits: 50)
- `packages/vue/test/base/src/router/index.ts` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.scss** (`core/src/css/core.scss`) — 383 inbound connections
2. **scripts.js** (`core/scripts/testing/scripts.js`) — 343 inbound connections
3. **styles.css** (`packages/angular/test/base/src/styles.css`) — 343 inbound connections
4. **interface.ts** (`core/src/components/router/utils/interface.ts`) — 130 inbound connections
5. **ionic-global.ts** (`core/src/global/ionic-global.ts`) — 95 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **proxies.ts** (`packages/react/src/components/proxies.ts`) — 74 outbound dependencies
2. **index.ts** (`packages/vue/test/base/src/router/index.ts`) — 41 outbound dependencies
3. **interface.d.ts** (`core/src/interface.d.ts`) — 40 outbound dependencies
4. **components.d.ts** (`core/src/components.d.ts`) — 39 outbound dependencies
5. **app.routes.ts** (`packages/angular/test/base/src/app/lazy/app-lazy/app.routes.ts`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handleHistoryChange` (@ `packages/vue-router/src/router.ts`) -> Impact: **150.7** | LOC: 285
  * *Intent:* // TODO RouteLocationNormalized
- `iosTransitionAnimation` (@ `core/src/utils/transition/ios.transition.ts`) -> Impact: **131.6** | LOC: 381
- `renderMonth` (@ `core/src/components/datetime/datetime.tsx`) -> Impact: **90.5** | LOC: 216
- `setup` (@ `packages/vue/src/components/IonRouterOutlet.ts`) -> Impact: **89.5** | LOC: 510
- `generateTime` (@ `core/src/components/datetime/utils/data.ts`) -> Impact: **85.5** | LOC: 127
  * *Intent:* /** * Given a local, reference datetime parts and option * max/min bound datetime parts, calculate the acceptable * hour and minute values according t...
- `getClosestValidDate` (@ `core/src/components/datetime/utils/manipulation.ts`) -> Impact: **75.2** | LOC: 146
  * *Intent:* /** * Returns the closest date to refParts * that also meets the constraints of * the *Values params. */
- `handleHistoryChange` (@ `packages/react-router/src/ReactRouter/IonRouter.tsx`) -> Impact: **75.0** | LOC: 114
- `transitionPage` (@ `packages/react-router/src/ReactRouter/StackManager.tsx`) -> Impact: **67.5** | LOC: 77
- `attachView` (@ `packages/angular/common/src/providers/angular-delegate.ts`) -> Impact: **66.1** | LOC: 124
- `calculateWindowAdjustment` (@ `core/src/components/popover/utils.ts`) -> Impact: **58.2** | LOC: 124
  * *Intent:* /** * Adjusts popover positioning coordinates * such that popover does not appear offscreen * or overlapping safe area bounds. * * @internal - This is...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `core/src/components/range/test/custom` | 2 | 5841.96 | 22.42% | 0.0% |
| `packages/docs` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/angular/test/base/e2e/src/lazy` | 23 | 3705.88 | 47.89% | 0.0% |
| `packages/angular/test/base/e2e/src/standalone` | 23 | 1599.57 | 22.66% | 0.0% |
| `core/src/components/datetime/utils` | 8 | 1400.06 | 22.1% | 1.43% |
| `core/src/utils` | 16 | 1290.44 | 23.41% | 27.36% |
| `core/src/components/select/test/basic` | 2 | 1092.24 | 3.11% | 0.0% |
| `packages/react-router/src/ReactRouter` | 8 | 978.46 | 36.98% | 16.08% |
| `core/src/components/datetime` | 7 | 940.01 | 4.29% | 4.27% |
| `core/src/components/picker/test/keyboard-entry` | 1 | 920.42 | 89.05% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/angular/common/src/directives/navigation/router-link-delegate.ts` -> **99.9999%** Exposure
- `core/src/components.d.ts` -> **99.9998%** Exposure
- `core/src/utils/overlays-interface.ts` -> **99.9665%** Exposure
- `packages/react/src/components/createControllerComponent.tsx` -> **99.8935%** Exposure
- `core/src/components/route/route.tsx` -> **99.6827%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `core/src/components/accordion-group/accordion-group.tsx` -> **100.0%** Exposure
- `core/src/components/accordion/accordion.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/action-sheet.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/test/action-sheet-id.spec.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/test/basic/fixture.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/src/components.d.ts` -> **0** Orphaned Functions | **294** Duplicates
- `packages/react/src/components/createControllerComponent.tsx` -> **9** Orphaned Functions | **0** Duplicates
- `core/src/components/tabs/tabs.tsx` -> **8** Orphaned Functions | **0** Duplicates
- `core/src/components/item-sliding/item-sliding.tsx` -> **6** Orphaned Functions | **0** Duplicates
- `packages/angular/common/src/directives/navigation/router-link-delegate.ts` -> **0** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2883` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/react/src/hooks/useOverlay.ts` (TYPESCRIPT) -> Cumulative Risk: **730.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 100.86 | **LOC:** 97 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.8921%)
- **Heaviest Functions:** `useOverlay` (Impact: 43.1), `handleDismiss` (Impact: 3.3), `[willPresentEventName]` (Impact: 3.1)

### 2. `packages/react/src/components/createControllerComponent.tsx` (TYPESCRIPT) -> Cumulative Risk: **727.09**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 92.68 | **LOC:** 128 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `present` (Impact: 12.7), `createControllerComponent` (Impact: 11.2), `componentDidUpdate` (Impact: 8.9)

### 3. `packages/react/src/components/react-component-lib/createOverlayComponent.tsx` (TYPESCRIPT) -> Cumulative Risk: **684.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 105.04 | **LOC:** 143 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (95.8333%)
- **Heaviest Functions:** `componentDidUpdate` (Impact: 10.9), `createOverlayComponent` (Impact: 9.2), `present` (Impact: 8.2)

### 4. `core/src/utils/tap-click/index.ts` (TYPESCRIPT) -> Cumulative Risk: **679.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 132.22 | **LOC:** 182 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.4401%), Documentation (92.8571%)
- **Heaviest Functions:** `setActivatedElement` (Impact: 17.1), `removeActivated` (Impact: 10.5), `getActivatableTarget` (Impact: 9.6)

### 5. `core/src/utils/input-shims/hacks/input-blurring.ts` (TYPESCRIPT) -> Cumulative Risk: **675.85**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 34.14 | **LOC:** 62 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (98.7872%)
- **Heaviest Functions:** `onTouchend` (Impact: 13.5), `enableInputBlurring` (Impact: 1.3), `onScroll` (Impact: 1.2)

### 6. `core/src/utils/framework-delegate.ts` (TYPESCRIPT) -> Cumulative Risk: **664.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 143.7 | **LOC:** 170 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (90.0%)
- **Heaviest Functions:** `attachComponent` (Impact: 36.0), `attachViewToDom` (Impact: 34.4), `detachComponent` (Impact: 5.8)

### 7. `packages/vue/src/utils/overlays.ts` (TYPESCRIPT) -> Cumulative Risk: **660.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 130.18 | **LOC:** 272 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9979%), Documentation (86.6667%)
- **Heaviest Functions:** `present` (Impact: 19.3), `createInlineComponent` (Impact: 12.5), `renderChildren` (Impact: 9.3)

### 8. `packages/react/src/components/createOverlayComponent.tsx` (TYPESCRIPT) -> Cumulative Risk: **655.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 110.28 | **LOC:** 145 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (87.5%)
- **Heaviest Functions:** `createOverlayComponent` (Impact: 11.2), `componentDidUpdate` (Impact: 10.9), `present` (Impact: 8.3)

### 9. `packages/react-router/src/ReactRouter/StackManager.tsx` (TYPESCRIPT) -> Cumulative Risk: **649.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 410.16 | **LOC:** 468 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9772%), Concurrency (98.9449%), Documentation (90.9091%)
- **Heaviest Functions:** `transitionPage` (Impact: 67.5), `handlePageTransition` (Impact: 53.6), `runCommit` (Impact: 45.1)

### 10. `packages/react/src/hooks/useController.ts` (TYPESCRIPT) -> Cumulative Risk: **642.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 68.16 | **LOC:** 67 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (98.7781%)
- **Heaviest Functions:** `useController` (Impact: 16.7), `[willPresentEventName]` (Impact: 5.1), `handleDismiss` (Impact: 3.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `core/src/components/range/test/custom/range.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5770.4 | **LOC:** 426 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.8495%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 125`, `args: 43`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`
* *Architecture:* `api: 21`, `concurrency: 54`, `import: 2`
* *Defense:* `safety: 45`, `doc: 1`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/angular/test/base/e2e/src/lazy/tabs.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1225.11 | **LOC:** 517 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 82 instances
* *Concurrency (weighted view):* 687
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 299`, `args: 42`, `func_start: 24`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `concurrency: 277`, `import: 2`
* *Defense:* `safety: 1`, `doc: 3`, `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-utils, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/picker/test/keyboard-entry/picker.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 920.42 | **LOC:** 389 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.0509%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 93`, `args: 26`, `func_start: 6`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 3`, `concurrency: 66`, `import: 3`
* *Defense:* `safety: 9`, `doc: 1`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test, playwright, locator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/datetime.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 910.74 | **LOC:** 2764 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (15.4038%), Tech Debt (10.0761%)
**Top Internal Functions/Classes:**
  * `renderMonth` (Impact: 90.5)
  * `processValue` (Impact: 35.8)
  * `destroyKeyboardMO` (Impact: 21.1)
  * `renderDatetime` (Impact: 20.6)
    * *Intent:* /** * Render entry point * All presentation types are rendered from here. */
  * `setActiveParts` (Impact: 17.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 69 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 253`, `args: 134`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 91`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `api: 22`, `concurrency: 14`, `import: 21`
* *Defense:* `safety: 26`, `doc: 115`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ionic-global, interface, datetime-interface, comparison, data, format, helpers, manipulation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/textarea/test/label-placement/textarea.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 793.08 | **LOC:** 325 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.375%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 92`, `args: 35`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `concurrency: 74`, `import: 2`
* *Defense:* `safety: 7`, `doc: 2`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/item/test/custom/item.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 766.26 | **LOC:** 175 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.8699%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 38`, `args: 16`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 9`, `concurrency: 18`, `import: 2`
* *Defense:* `safety: 6`, `doc: 1`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/select/test/label/select.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 757.16 | **LOC:** 380 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.4337%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 106`, `args: 38`, `func_start: 26`
* *Risk/State:* None
* *Architecture:* `concurrency: 87`, `import: 2`
* *Defense:* `safety: 7`, `doc: 1`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime-button/test/basic/datetime-button.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 716.18 | **LOC:** 348 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3861%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 110`, `args: 29`, `func_start: 19`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 2`, `concurrency: 97`, `import: 2`
* *Defense:* `safety: 2`, `doc: 2`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/toast/test/custom/toast.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 714.72 | **LOC:** 134 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.8401%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 37`, `args: 13`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1`
* *Architecture:* `api: 8`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 8`, `doc: 1`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/nav/nav.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 708.54 | **LOC:** 1101 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9051%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `postViewInit` (Impact: 53.9)
    * *Intent:* /** * Adds and Removes the views from the navigation stack. * * @param enteringView The view being e...
  * `prepareTI` (Impact: 31.2)
  * `setRouteId` (Impact: 25.5)
    * *Intent:* /** * Called by the router to update the view. * * @param id The component tag. * @param params The ...
  * `queueTrns` (Impact: 24.8)
    * *Intent:* /** * Adds a navigation stack change to the queue and schedules it to run. * * @returns Whether the ...
  * `runTransition` (Impact: 24.1)
    * *Intent:* /** Executes all the transition instruction from the queue. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 99`, `args: 56`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 66`, `dead_code: 3`
* *Architecture:* `api: 16`, `concurrency: 41`, `import: 16`
* *Defense:* `safety: 17`, `doc: 43`, `test: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` config, ionic-global, interface, swipe-back, interface, constants, nav-interface, view-controller...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/modal.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 641.3 | **LOC:** 1669 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (37.9416%), Tech Debt (8.209%)
**Top Internal Functions/Classes:**
  * `dismiss` (Impact: 32.3)
    * *Intent:* /** * Dismiss the modal overlay after it has been presented. * This is a no-op if the overlay has no...
  * `present` (Impact: 20.5)
    * *Intent:* /** * Present the modal overlay after it has been created. */
  * `initParentRemovalObserver` (Impact: 20.1)
  * `render` (Impact: 17.1)
  * `setupChildRoutePassthrough` (Impact: 16.6)
    * *Intent:* /** * For sheet modals that allow background interaction, sets up pointer-events * passthrough on ch...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 173`, `args: 84`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 71`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 11`, `concurrency: 37`, `import: 28`
* *Defense:* `safety: 14`, `doc: 88`, `sync_locks: 3`, `immutability_locks: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` config, ionic-global, interface, keyboard, overlays-interface, ios.enter, ios.leave, ios.transition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/segment/test/segment-events.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 633.47 | **LOC:** 285 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.158%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 70
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 69`, `args: 23`, `func_start: 8`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `concurrency: 50`, `import: 2`
* *Defense:* `safety: 5`, `doc: 1`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/input-otp/test/basic/input-otp.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 632.66 | **LOC:** 1224 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `simulatePaste` (Impact: 4.1)
    * *Intent:* /** * Simulates a paste event in an input element with the given value */
  * `verifyInputValues` (Impact: 4.0)
    * *Intent:* /** * Helper function to verify input values in both the input * boxes and the input-otp component's...
  * `simulateAutofill` (Impact: 2.0)
    * *Intent:* /** * Simulates an autofill event in an input element with the given value */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 597
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 593`, `args: 109`, `func_start: 80`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 7`
* *Architecture:* `io: 1`, `concurrency: 487`, `import: 3`
* *Defense:* `safety: 40`, `doc: 6`, `test: 159`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/select/test/basic/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 611.71 | **LOC:** 357 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2137%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`, `args: 196`, `func_start: 4`, `class_start: 224`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 5`, `api: 10`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ionic.bundle.css, ionic.esm.js, ionic.js, scripts.js, styles.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/refresher/refresher.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 594.8 | **LOC:** 928 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.7225%), Tech Debt (8.5797%)
**Top Internal Functions/Classes:**
  * `setupiOSNativeRefresher` (Impact: 48.9)
  * `setupMDNativeRefresher` (Impact: 33.2)
  * `onMove` (Impact: 27.8)
  * `scrollListenerCallback` (Impact: 21.6)
  * `setCss` (Impact: 18.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 97
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 97`, `args: 55`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 79`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 22`, `import: 14`
* *Defense:* `safety: 7`, `doc: 34`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ionic-global, interface, gesture, refresher-interface, refresher.utils, core, cubic-bezier, content...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/test/safe-area/modal.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 578.52 | **LOC:** 371 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Concurrency (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 160`, `args: 48`, `func_start: 11`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `io: 11`, `concurrency: 86`, `import: 2`
* *Defense:* `doc: 2`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/range/range.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 575.04 | **LOC:** 1258 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.5762%), Tech Debt (8.2769%)
**Top Internal Functions/Classes:**
  * `knobStyle` (Impact: 52.8)
  * `tickStyle` (Impact: 27.1)
  * `renderRangeSlider` (Impact: 25.1)
  * `render` (Impact: 23.1)
  * `getKnobPosition` (Impact: 16.5)
    * *Intent:* /** * Returns whether the given knob is at the lower or upper position based * on current ratios for...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 65 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 111`, `args: 65`, `func_start: 51`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 73`, `planned_debt: 1`
* *Architecture:* `api: 13`, `concurrency: 3`, `import: 13`
* *Defense:* `safety: 12`, `doc: 54`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ionic-global, interface, floating-point, gesture, range-interface, core, content, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/popover/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 568.42 | **LOC:** 1028 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.6447%), Tech Debt (23.4116%)
**Top Internal Functions/Classes:**
  * `calculateWindowAdjustment` (Impact: 58.2)
    * *Intent:* /** * Adjusts popover positioning coordinates * such that popover does not appear offscreen * or ove...
  * `getPopoverPosition` (Impact: 54.9)
    * *Intent:* /** * Positions a popover by taking into account * the reference point, preferred side, alignment * ...
  * `calculateArrowPosition` (Impact: 35.6)
    * *Intent:* /** * Calculates where the arrow positioning * should be relative to the popover content. */
  * `callback` (Impact: 35.4)
  * `calculatePopoverSide` (Impact: 30.6)
    * *Intent:* /** * Calculates the required top/left * values needed to position the popover * content on the side...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 148`, `args: 47`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 16`, `concurrency: 5`, `import: 2`
* *Defense:* `safety: 6`, `doc: 53`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` popover-interface, helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/test/custom/datetime.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 560.44 | **LOC:** 394 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (98.9681%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Concurrency (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 105`, `args: 34`, `func_start: 13`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 8`, `api: 12`, `concurrency: 60`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/test/sheet/modal.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 549.17 | **LOC:** 403 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 177
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 174`, `args: 47`, `func_start: 16`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 1`, `concurrency: 142`, `import: 2`
* *Defense:* `safety: 9`, `doc: 2`, `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/checkbox/test/bottom-content/checkbox.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 524.07 | **LOC:** 208 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.507%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 64`, `args: 22`, `func_start: 14`
* *Risk/State:* None
* *Architecture:* `api: 4`, `concurrency: 48`, `import: 2`
* *Defense:* `safety: 7`, `doc: 3`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/toggle/test/bottom-content/toggle.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 519.39 | **LOC:** 199 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.8189%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 64`, `args: 22`, `func_start: 14`
* *Risk/State:* None
* *Architecture:* `api: 4`, `concurrency: 48`, `import: 2`
* *Defense:* `safety: 7`, `doc: 3`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/popover/test/basic/popover.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 513.06 | **LOC:** 264 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.573%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Concurrency (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 104`, `args: 27`, `func_start: 17`
* *Risk/State:* `state_mutation: 4`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 89`, `import: 3`
* *Defense:* `doc: 4`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fixture, test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/utils/animation/animation.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 496.32 | **LOC:** 996 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.9828%), Tech Debt (8.3707%)
**Top Internal Functions/Classes:**
  * `progressEnd` (Impact: 30.4)
  * `play` (Impact: 11.6)
  * `createAnimation` (Impact: 11.3)
  * `addElement` (Impact: 10.7)
  * `from` (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 178`, `args: 101`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 85`, `planned_debt: 1`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 3`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.161
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` browser, animation-interface, animation-utils, logging
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/components/range/test/custom/range.e2e.ts` -> **Brandy Smith** (100.0% isolated ownership) | Magnitude: 5770.4
- `core/src/components/item/test/custom/item.e2e.ts` -> **Brandy Smith** (100.0% isolated ownership) | Magnitude: 766.26
- `core/src/components/toast/test/custom/toast.e2e.ts` -> **Shane** (100.0% isolated ownership) | Magnitude: 714.72
- `core/src/components/input-otp/test/basic/input-otp.e2e.ts` -> **Kanhaiya Pandey** (100.0% isolated ownership) | Magnitude: 632.66
- `core/src/components/refresher/refresher.tsx` -> **Shane** (100.0% isolated ownership) | Magnitude: 594.8

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/global/ionic-global.ts` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)
- `packages/react/src/components/navigation/IonTabs.tsx` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)
- `core/src/utils/input-shims/input-shims.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `core/src/utils/platform.ts` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `packages/react-router/src/ReactRouter/IonRouter.tsx` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/components/router/utils/interface.ts` -> **Severity: 1922.4** (Blast Radius: 19.224 * Doc Risk: 100.0%)
- `core/src/utils/input-shims/hacks/common.ts` -> **Severity: 743.75** (Blast Radius: 8.925 * Doc Risk: 83.3333%)
- `core/src/global/ionic-global.ts` -> **Severity: 445.3** (Blast Radius: 4.453 * Doc Risk: 100.0%)
- `core/src/global/config.ts` -> **Severity: 372.9** (Blast Radius: 3.729 * Doc Risk: 100.0%)
- `core/src/utils/animation/animation.ts` -> **Severity: 249.318** (Blast Radius: 3.161 * Doc Risk: 78.8732%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
