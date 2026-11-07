# ARCHITECTURAL_BRIEF: ionic-framework
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ionic-team/ionic-framework.git` |
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
- **Scope:** 2546 analyzed artifact(s), 171780 LOC.
- **Load-bearing artifact:** `core/scripts/testing/scripts.js` -- 346 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/react/src/components/proxies.ts` -- pulls in 74 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/docs/.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 9447 |
| Analyzed Artifacts (Scanned) | 2546 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6901 |
| Total LOC | 171780 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 27.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8085 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2761 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0184 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 172 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1365 | 97706 | 53.6% |
| HTML | 485 | 50349 | 19.0% |
| CSS | 432 | 15962 | 17.0% |
| JAVASCRIPT | 69 | 3488 | 2.7% |
| JSON | 53 | 1774 | 2.1% |
| YAML | 37 | 1988 | 1.5% |
| MARKDOWN | 28 | 0 | 1.1% |
| PLAINTEXT | 26 | 1 | 1.0% |
| XML | 22 | 0 | 0.9% |
| SHELL | 21 | 342 | 0.8% |
| GROOVY | 3 | 67 | 0.1% |
| JAVA | 3 | 37 | 0.1% |
| DOCKERFILE | 1 | 2 | 0.0% |
| BATCH | 1 | 64 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2545 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Declarative / Non-Code 35%, Callbacks & Closures Files 9%, Large Core Modules 4%, State Mutators Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2491 | 97.8% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 53 | 2.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6901*

**Composition by Extension & Reason:**
- `.png`: 6781x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.md`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4075 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2740 LOC)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9833 LOC), 1x Excluded (Massive Static Asset Blob: 13851 LOC)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 10123 LOC), 1x Excluded (Saturation: Line 16 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2631 LOC)
- `.map`: 3x Unresolved Ambiguity (No Retainable Structure), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.html`: 1x Excluded (Saturation: Line 61 exceeds 500 chars), 1x Excluded (Saturation: Line 30 exceeds 500 chars), 1x Excluded (Saturation: Line 41 exceeds 500 chars)
- `.jpg`: 3x Excluded (Explicitly Denied Extension: '.jpg')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 1x Excluded (Machine-Generated Source Code Signature: 20 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.txt`: 1x Excluded (Embedded Array/Matrix Payload: 8000 commas in 2143 LOC)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.pro`: 1x Excluded (Unsupported Extension: '.pro')
- `.xml`: 1x Excluded (Saturation: Line 31 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.6 | 19.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.3 | 4.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 29.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 87.3 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 85.4 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 33.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 640 | 214 | 0 | `core/src/components/datetime/test/manipulation.spec.ts` |
| cleanup | 204 | 99 | 0 | `core/src/components/modal/modal.tsx` |
| guards | 4070 | 824 | 4 | `core/src/components/datetime/datetime.tsx` |
| danger | 2204 | 541 | 2 | `core/src/components/range/test/range.spec.ts` |
| concurrency | 13400 | 823 | 14 | `core/src/components/input-otp/test/basic/input-otp.e2e.ts` |
| connectivity | 8147 | 1462 | 8 | `packages/react/test/base/src/theme/variables.css` |
| io | 3063 | 605 | 5 | `core/src/components/router/test/path.spec.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `packages/angular/scripts/build-core.js` |
| time | 223 | 104 | 0 | `core/src/components/searchbar/searchbar.tsx` |
| serialization | 45 | 18 | 0 | `packages/angular/test/base/e2e/src/standalone/value-accessors.spec.ts` |
| regex | 75 | 39 | 0 | `packages/angular/test/base/e2e/src/lazy/router-link.spec.ts` |
| events | 2814 | 740 | 4 | `core/src/components/button/test/wrap/button.e2e.ts` |
| tests | 10915 | 626 | 10 | `packages/vue/test/base/tests/e2e/specs/tabs.cy.js` |
| docs | 4498 | 1109 | 3 | `core/src/components/datetime/datetime.tsx` |
| debt | 805 | 330 | 1 | `core/src/components/action-sheet/test/standalone/index.html` |
| mutation | 38274 | 1623 | 35 | `core/src/components/button/test/perf/index.html` |
| dead_code | 275 | 128 | 0 | `core/src/components/nav/test/nav-controller.spec.ts` |
| credential | 1 | 1 | 0 | `.github/workflows/nightly.yml` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 163 | 39 | 0 | `core/src/utils/animation/cubic-bezier.ts` |
| ui | 4718 | 808 | 5 | `core/src/themes/test/colors/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `core/src/components/router/test/path.spec.tsx` (Hits: 84)
- `packages/angular/test/base/src/app/standalone/app-standalone/app.routes.ts` (Hits: 56)
- `core/src/components/breadcrumbs/test/collapsed/index.html` (Hits: 50)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **scripts.js** (`core/scripts/testing/scripts.js`) — 346 inbound connections
2. **styles.css** (`core/scripts/testing/styles.css`) — 346 inbound connections
3. **interface.ts** (`core/src/components/router/utils/interface.ts`) — 128 inbound connections
4. **ionic-global.ts** (`core/src/global/ionic-global.ts`) — 94 inbound connections
5. **ionic.globals.scss** (`core/src/themes/ionic.globals.scss`) — 92 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **proxies.ts** (`packages/react/src/components/proxies.ts`) — 74 outbound dependencies
2. **app.routes.ts** (`packages/angular/test/base/src/app/standalone/app-standalone/app.routes.ts`) — 50 outbound dependencies
3. **index.ts** (`packages/vue/test/base/src/router/index.ts`) — 41 outbound dependencies
4. **interface.d.ts** (`core/src/interface.d.ts`) — 40 outbound dependencies
5. **app.routes.ts** (`packages/angular/test/base/src/app/lazy/app-lazy/app.routes.ts`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handleHistoryChange` **(Many-Argument Workhorses)** (@ `packages/vue-router/src/router.ts`) -> Impact: **148.3** | LOC: 283
  * *Intent:* // TODO RouteLocationNormalized
- `iosTransitionAnimation` **(Many-Argument Workhorses)** (@ `core/src/utils/transition/ios.transition.ts`) -> Impact: **127.6** | LOC: 370
- `setup` **(I/O & Config Routines)** (@ `packages/vue/src/components/IonRouterOutlet.ts`) -> Impact: **87.5** | LOC: 510
- `generateTime` **(Many-Argument Workhorses)** (@ `core/src/components/datetime/utils/data.ts`) -> Impact: **85.2** | LOC: 121
  * *Intent:* /** * Given a local, reference datetime parts and option * max/min bound datetime parts, calculate the acceptable * hour and minute values according t...
- `renderMonth` **(Many-Argument Workhorses)** (@ `core/src/components/datetime/datetime.tsx`) -> Impact: **78.3** | LOC: 216
- `handleHistoryChange` **(Many-Argument Workhorses)** (@ `packages/react-router/src/ReactRouter/IonRouter.tsx`) -> Impact: **75.0** | LOC: 114
- `getClosestValidDate` **(Compute Cores)** (@ `core/src/components/datetime/utils/manipulation.ts`) -> Impact: **74.6** | LOC: 134
  * *Intent:* /** * Returns the closest date to refParts * that also meets the constraints of * the *Values params. */
- `transitionPage` **(Many-Argument Workhorses)** (@ `packages/react-router/src/ReactRouter/StackManager.tsx`) -> Impact: **65.1** | LOC: 77
- `attachView` **(Many-Argument Workhorses)** (@ `packages/angular/common/src/providers/angular-delegate.ts`) -> Impact: **61.8** | LOC: 114
- `calculateWindowAdjustment` **(Many-Argument Workhorses)** (@ `core/src/components/popover/utils.ts`) -> Impact: **58.1** | LOC: 122
  * *Intent:* /** * Adjusts popover positioning coordinates * such that popover does not appear offscreen * or overlapping safe area bounds. * */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/docs` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/angular/test/base/e2e/src/lazy` | 23 | 2972.44 | 16.68% | 0.0% |
| `core/src/components/range/test/custom` | 2 | 1994.67 | 14.79% | 0.0% |
| `packages/angular/test/base/e2e/src/standalone` | 23 | 1400.95 | 7.14% | 0.0% |
| `core/src/components/datetime/utils` | 8 | 1319.16 | 21.92% | 1.35% |
| `core/src/utils` | 16 | 1237.04 | 23.32% | 20.81% |
| `packages/react-router/src/ReactRouter` | 8 | 930.56 | 36.95% | 11.55% |
| `core/src/components/datetime` | 7 | 887.41 | 4.26% | 4.25% |
| `packages/react/src/components` | 26 | 886.4 | 12.03% | 7.71% |
| `core/src/components/popover` | 9 | 832.05 | 9.71% | 7.8% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/angular/common/src/directives/navigation/router-link-delegate.ts` -> **99.9999%** Exposure
- `core/src/utils/overlays-interface.ts` -> **99.9447%** Exposure
- `packages/react/src/components/createControllerComponent.tsx` -> **99.8629%** Exposure
- `core/src/components/item-options/item-options.tsx` -> **99.3307%** Exposure
- `core/src/components/route/route.tsx` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `core/src/components/accordion-group/accordion-group.tsx` -> **100.0%** Exposure
- `core/src/components/accordion/accordion.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/action-sheet.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/test/action-sheet-id.spec.tsx` -> **100.0%** Exposure
- `core/src/components/action-sheet/test/basic/fixture.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/src/components/menu/menu.tsx` -> **10** Orphaned Functions | **0** Duplicates
- `packages/react/src/components/createControllerComponent.tsx` -> **9** Orphaned Functions | **0** Duplicates
- `core/src/components/tabs/tabs.tsx` -> **8** Orphaned Functions | **0** Duplicates
- `core/src/components/action-sheet/test/standalone/index.html` -> **0** Orphaned Functions | **8** Duplicates
- `core/src/components/item-sliding/item-sliding.tsx` -> **6** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `2909` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/docs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/range/test/custom/range.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.062)
- **Top Global Matches:** file_cluster_12: 7.062, file_cluster_10: 7.432, file_cluster_7: 8.138
- **Magnitude:** 1923.11 | **LOC:** 426 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (36.5%), Complexity Load (formerly Cognitive Load) (29.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 125`, `args: 43`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`
* *Architecture:* `api: 21`, `concurrency: 54`, `import: 2`
* *Defense:* `safety: 45`, `doc: 1`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/angular/test/base/e2e/src/lazy/tabs.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.311)
- **Top Global Matches:** file_cluster_10: 5.311, file_cluster_2: 7.807, file_cluster_13: 7.973
- **Magnitude:** 962.81 | **LOC:** 517 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (41.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 82 instances
* *Concurrency (weighted view):* 687
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 299`, `args: 42`, `func_start: 24`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `concurrency: 277`, `import: 2`
* *Defense:* `safety: 1`, `doc: 3`, `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-utils, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/datetime.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.775)
- **Top Global Matches:** file_cluster_16: 7.775, file_cluster_12: 8.357, file_cluster_4: 8.745
- **Magnitude:** 858.14 | **LOC:** 2764 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 0.668; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (72.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.8%), Guard Balance (formerly Safety Score) (55.5%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderMonth` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `processValue` **(Compute Cores)** (Impact: 35.7)
  * `renderDatetime` **(Stateful Encapsulated Methods)** (Impact: 20.6)
    * *Intent:* /** * Render entry point * All presentation types are rendered from here. */
  * `setActiveParts` **(Compute Cores)** (Impact: 17.8)
  * `renderIndividualDatePickerColumns` **(Compute Cores)** (Impact: 17.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 70 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 253`, `args: 134`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 91`, `dead_code: 2`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `api: 18`, `concurrency: 14`, `import: 21`
* *Defense:* `safety: 26`, `doc: 115`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.668
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.001176
  * `Imports (Out-Degree: 12):` ionic-global, interface, datetime-interface, comparison, data, format, helpers, manipulation...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `core/src/components/nav/nav.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.051)
- **Top Global Matches:** file_cluster_12: 8.051, file_cluster_4: 8.174, file_cluster_5: 9.173
- **Magnitude:** 681.74 | **LOC:** 1101 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.272; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.5%), Complexity Load (formerly Cognitive Load) (39.9%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postViewInit` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* /** * Adds and Removes the views from the navigation stack. * */
  * `prepareTI` **(Compute Cores)** (Impact: 28.4)
  * `setRouteId` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* /** * Called by the router to update the view. * * */
  * `queueTrns` **(Stateful Encapsulated Methods)** (Impact: 24.8)
    * *Intent:* /** * Adds a navigation stack change to the queue and schedules it to run. * */
  * `runTransition` **(Stateful Encapsulated Methods)** (Impact: 24.1)
    * *Intent:* /** Executes all the transition instruction from the queue. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 71
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 99`, `args: 56`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 66`
* *Architecture:* `api: 16`, `concurrency: 41`, `import: 16`
* *Defense:* `safety: 17`, `doc: 43`, `test: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000392
  * `Imports (Out-Degree: 7):` config, ionic-global, interface, swipe-back, interface, constants, nav-interface, view-controller...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/components/input-otp/test/basic/input-otp.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.065)
- **Top Global Matches:** file_cluster_10: 7.065, file_cluster_15: 9.165, file_cluster_12: 9.581
- **Magnitude:** 632.66 | **LOC:** 1224 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (37.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simulatePaste` **(Callbacks & Closures)** (Impact: 4.1)
    * *Intent:* /** * Simulates a paste event in an input element with the given value */
  * `verifyInputValues` **(Parameter Forwarders)** (Impact: 4.0)
    * *Intent:* /** * Helper function to verify input values in both the input * boxes and the input-otp component's...
  * `simulateAutofill` **(Type Conversions)** (Impact: 2.0)
    * *Intent:* /** * Simulates an autofill event in an input element with the given value */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 597
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 593`, `args: 109`, `func_start: 80`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 7`
* *Architecture:* `io: 1`, `concurrency: 487`, `import: 3`
* *Defense:* `safety: 40`, `doc: 6`, `test: 159`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/modal.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.435)
- **Top Global Matches:** file_cluster_12: 7.435, file_cluster_5: 9.051, file_cluster_16: 9.137
- **Magnitude:** 632.1 | **LOC:** 1669 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **25**; blast radius 0.986; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.5%)
- **Documentation Coverage:** 51.7241% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dismiss` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* /** * Dismiss the modal overlay after it has been presented. * This is a no-op if the overlay has no...
  * `present` **(I/O & Config Routines)** (Impact: 20.5)
    * *Intent:* /** * Present the modal overlay after it has been created. */
  * `initParentRemovalObserver` **(I/O & Config Routines)** (Impact: 20.1)
  * `setupChildRoutePassthrough` **(Defensive Guards)** (Impact: 16.6)
    * *Intent:* /** * For sheet modals that allow background interaction, sets up pointer-events * passthrough on ch...
  * `render` **(I/O & Config Routines)** (Impact: 16.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 173`, `args: 84`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 71`, `planned_debt: 1`
* *Architecture:* `api: 11`, `concurrency: 37`, `import: 28`
* *Defense:* `safety: 14`, `doc: 88`, `sync_locks: 3`, `immutability_locks: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.001961
  * `Imports (Out-Degree: 10):` config, ionic-global, interface, keyboard, overlays-interface, ios.enter, ios.leave, ios.transition...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `core/src/components/refresher/refresher.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.558)
- **Top Global Matches:** file_cluster_4: 8.558, file_cluster_12: 11.161, file_cluster_6: 12.23
- **Magnitude:** 584.6 | **LOC:** 928 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.224; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (46.6%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setupiOSNativeRefresher` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `setupMDNativeRefresher` **(Many-Argument Workhorses)** (Impact: 33.2)
  * `onMove` **(Compute Cores)** (Impact: 27.8)
  * `scrollListenerCallback` **(I/O & Config Routines)** (Impact: 21.1)
  * `setCss` **(Many-Argument Workhorses)** (Impact: 18.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 97
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 97`, `args: 55`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 79`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `concurrency: 22`, `import: 14`
* *Defense:* `safety: 7`, `doc: 34`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ionic-global, interface, gesture, refresher-interface, refresher.utils, core, cubic-bezier, content...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/modal/test/safe-area/modal.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.014)
- **Top Global Matches:** file_cluster_10: 5.014, file_cluster_13: 7.963, file_cluster_2: 7.99
- **Magnitude:** 578.52 | **LOC:** 371 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Concurrency (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 160`, `args: 48`, `func_start: 11`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `io: 11`, `concurrency: 86`, `import: 2`
* *Defense:* `doc: 2`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/test/custom/datetime.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.354)
- **Top Global Matches:** file_cluster_10: 4.354, file_cluster_2: 6.779, file_cluster_13: 7.048
- **Magnitude:** 560.44 | **LOC:** 394 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.0%), Guard Balance (formerly Safety Score) (44.6%), Mutation Surface (formerly State Flux) (22.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Concurrency (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 105`, `args: 34`, `func_start: 13`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 8`, `api: 12`, `concurrency: 60`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/popover/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.597)
- **Top Global Matches:** file_cluster_15: 7.597, file_cluster_4: 7.975, file_cluster_10: 8.236
- **Magnitude:** 549.12 | **LOC:** 1028 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 0.708; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (69.9%), Debt Markers (formerly Tech Debt) (61.6%), Guard Balance (formerly Safety Score) (55.6%)
- **Documentation Coverage:** 29.7872% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calculateWindowAdjustment` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* /** * Adjusts popover positioning coordinates * such that popover does not appear offscreen * or ove...
  * `getPopoverPosition` **(Many-Argument Workhorses)** (Impact: 54.4)
    * *Intent:* /** * Positions a popover by taking into account * the reference point, preferred side, alignment * ...
  * `calculateArrowPosition` **(Many-Argument Workhorses)** (Impact: 35.2)
    * *Intent:* /** * Calculates where the arrow positioning * should be relative to the popover content. */
  * `callback` **(Compute Cores)** (Impact: 34.8)
  * `calculatePopoverSide` **(Many-Argument Workhorses)** (Impact: 30.2)
    * *Intent:* /** * Calculates the required top/left * values needed to position the popover * content on the side...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 148`, `args: 47`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 16`, `concurrency: 5`, `import: 2`
* *Defense:* `safety: 6`, `doc: 53`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.708
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001765
  * `Imports (Out-Degree: 1):` popover-interface, helpers
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `core/src/components/range/range.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.095)
- **Top Global Matches:** file_cluster_12: 7.095, file_cluster_16: 8.385, file_cluster_10: 9.261
- **Magnitude:** 483.24 | **LOC:** 1258 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.3%), Concurrency Surface (formerly Concurrency) (37.5%), Complexity Load (formerly Cognitive Load) (26.3%)
- **Documentation Coverage:** 56.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderRangeSlider` **(I/O & Config Routines)** (Impact: 24.1)
  * `render` **(I/O & Config Routines)** (Impact: 23.1)
  * `getKnobPosition` **(Compute Cores)** (Impact: 16.4)
    * *Intent:* /** * Returns whether the given knob is at the lower or upper position based * on current ratios for...
  * `handleKeyboard` **(Compute Cores)** (Impact: 9.7)
  * `onEnd` **(Stateful Encapsulated Methods)** (Impact: 9.0)
    * *Intent:* /** * The value should be updated on touch end: * - When the user lifts their finger from the screen...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 65 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 111`, `args: 65`, `func_start: 51`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 73`, `planned_debt: 1`
* *Architecture:* `api: 10`, `concurrency: 3`, `import: 13`
* *Defense:* `safety: 12`, `doc: 54`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001176
  * `Imports (Out-Degree: 6):` ionic-global, interface, floating-point, gesture, range-interface, core, content, helpers...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `core/src/components/select/test/basic/select.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.219)
- **Top Global Matches:** file_cluster_10: 5.219, file_cluster_2: 7.354, file_cluster_13: 7.566
- **Magnitude:** 480.53 | **LOC:** 608 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.0%), Mutation Surface (formerly State Flux) (12.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 198`, `args: 41`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4`, `planned_debt: 2`
* *Architecture:* `io: 3`, `concurrency: 153`, `import: 3`
* *Defense:* `doc: 3`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/utils/animation/animation.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.12)
- **Top Global Matches:** file_cluster_12: 7.12, file_cluster_10: 7.815, file_cluster_7: 9.536
- **Magnitude:** 480.52 | **LOC:** 996 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **4**; blast radius 0.735; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.5%), Complexity Load (formerly Cognitive Load) (35.0%), Connectivity (formerly Api Exposure) (22.9%)
- **Documentation Coverage:** 78.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `progressEnd` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `play` **(Callbacks & Closures)** (Impact: 11.6)
  * `createAnimation` **(I/O & Config Routines)** (Impact: 11.3)
  * `addElement` **(Type Conversions)** (Impact: 10.6)
  * `from` **(Type Conversions)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 178`, `args: 101`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 85`, `planned_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 3`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.735
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.003529
  * `Imports (Out-Degree: 3):` browser, animation-interface, animation-utils, logging
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `core/src/components/modal/test/sheet/modal.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.993)
- **Top Global Matches:** file_cluster_10: 4.993, file_cluster_2: 7.611, file_cluster_13: 7.643
- **Magnitude:** 479.88 | **LOC:** 403 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (40.1%), Mutation Surface (formerly State Flux) (38.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 177
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 174`, `args: 47`, `func_start: 16`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 1`, `concurrency: 142`, `import: 2`
* *Defense:* `safety: 9`, `doc: 2`, `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/angular/test/base/e2e/src/standalone/value-accessors.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.093)
- **Top Global Matches:** file_cluster_10: 6.093, file_cluster_13: 8.695, file_cluster_2: 8.705
- **Magnitude:** 453.44 | **LOC:** 248 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (30.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Concurrency (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 140`, `args: 30`, `func_start: 11`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `concurrency: 129`, `import: 1`
* *Defense:* `test: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/datetime/utils/data.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.334)
- **Top Global Matches:** file_cluster_6: 7.334, file_cluster_4: 12.984, file_cluster_8: 14.047
- **Magnitude:** 452.48 | **LOC:** 666 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 0.394; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.0%), Connectivity (formerly Api Exposure) (48.8%), Complexity Load (formerly Cognitive Load) (37.0%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateTime` **(Many-Argument Workhorses)** (Impact: 85.2)
    * *Intent:* /** * Given a local, reference datetime parts and option * max/min bound datetime parts, calculate t...
  * `getDayColumnData` **(Many-Argument Workhorses)** (Impact: 55.4)
    * *Intent:* /** * Returns information regarding * selectable dates (i.e 1st, 2nd, 3rd, etc) * within a reference...
  * `getMonthColumnData` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `getYearColumnData` **(Defensive Guards)** (Impact: 38.3)
  * `getDaysOfMonth` **(Many-Argument Workhorses)** (Impact: 26.0)
    * *Intent:* /** * Returns an array containing all of the * days in a month for a given year. Values are * aligne...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 77`, `args: 30`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 48`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 12`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.394
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001569
  * `Imports (Out-Degree: 6):` interface, datetime-interface, comparison, format, helpers, manipulation
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `core/src/utils/overlays.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.363)
- **Top Global Matches:** file_cluster_5: 9.363, file_cluster_12: 9.443, file_cluster_4: 10.096
- **Magnitude:** 451.22 | **LOC:** 1003 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.241; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (95.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.9%)
- **Documentation Coverage:** 50.8772% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dismiss` **(Many-Argument Workhorses)** (Impact: 55.8)
  * `present` **(Many-Argument Workhorses)** (Impact: 46.4)
  * `overlayAnimation` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `trapScopedFocus` **(I/O & Config Routines)** (Impact: 15.6)
  * `connectListeners` **(Callbacks & Closures)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 151`, `args: 57`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 25`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 29`, `concurrency: 22`, `import: 12`
* *Defense:* `safety: 16`, `doc: 50`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000706
  * `Imports (Out-Degree: 7):` config, ionic-global, interface, framework-delegate, gesture-controller, hardware-back-button, helpers, browser...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/components/select/select.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.17)
- **Top Global Matches:** file_cluster_12: 7.17, file_cluster_16: 8.997, file_cluster_5: 9.066
- **Magnitude:** 436.68 | **LOC:** 1332 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (58.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.1%)
- **Documentation Coverage:** 74.1379% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Compute Cores)** (Impact: 27.4)
    * *Intent:* /** * Open the select overlay. The overlay is either an alert, action sheet, or popover, * depending...
  * `render` **(I/O & Config Routines)** (Impact: 17.9)
  * `openPopover` **(I/O & Config Routines)** (Impact: 14.8)
  * `createOverlay` **(Stateful Encapsulated Methods)** (Impact: 14.1)
  * `generateText` **(Compute Cores)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 165`, `args: 71`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 41`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `concurrency: 14`, `import: 19`
* *Defense:* `safety: 3`, `doc: 63`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000392
  * `Imports (Out-Degree: 7):` ionic-global, interface, action-sheet-interface, alert-interface, select-popover-interface, select-interface, core, forms...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `core/src/components/segment/test/segment-events.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.171)
- **Top Global Matches:** file_cluster_10: 4.171, file_cluster_2: 5.979, file_cluster_13: 6.35
- **Magnitude:** 435.51 | **LOC:** 285 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (73.1%), Guard Balance (formerly Safety Score) (42.6%), Mutation Surface (formerly State Flux) (12.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 69`, `args: 23`, `func_start: 8`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `concurrency: 50`, `import: 2`
* *Defense:* `safety: 5`, `doc: 1`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/angular/test/base/e2e/src/lazy/form.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.707)
- **Top Global Matches:** file_cluster_12: 7.707, file_cluster_10: 7.881, file_cluster_15: 8.834
- **Magnitude:** 432.92 | **LOC:** 298 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.224; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testData` **(Parameter Forwarders)** (Impact: 2.0)
  * `testStatus` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* // Helper functions
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 56 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 392
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 116`, `args: 22`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 30`
* *Architecture:* `concurrency: 112`, `import: 1`
* *Defense:* `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/input-otp/input-otp.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.945)
- **Top Global Matches:** file_cluster_4: 6.945, file_cluster_16: 10.995, file_cluster_6: 11.508
- **Magnitude:** 419.76 | **LOC:** 881 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.224; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.9%), Concurrency Surface (formerly Concurrency) (58.9%)
- **Documentation Coverage:** 27.5862% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onInput` **(Compute Cores)** (Impact: 48.8)
    * *Intent:* /** * Processes all input scenarios for each input box. * * This function manages: * 1. Autofill han...
  * `onKeyDown` **(Compute Cores)** (Impact: 44.4)
    * *Intent:* /** * Handles keyboard navigation for the OTP component. * * Navigation: * - Backspace: Clears curre...
  * `processSeparators` **(I/O & Config Routines)** (Impact: 13.6)
    * *Intent:* /** * Processes the separators prop into an array of numbers. * * If the separators prop is not prov...
  * `onPaste` **(Defensive Guards)** (Impact: 13.4)
    * *Intent:* /** * Handles pasting text into the input OTP component. * This function prevents the default paste ...
  * `onFocus` **(Defensive Guards)** (Impact: 11.4)
    * *Intent:* /** * Handles the focus behavior for the input OTP component. * * Focus behavior: * 1. Keyboard navi...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 86`, `args: 47`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 62`
* *Architecture:* `api: 6`, `concurrency: 3`, `import: 11`
* *Defense:* `safety: 13`, `doc: 40`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ionic-global, interface, input-otp-interface, core, helpers, logging, rtl, theme...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/popover/test/basic/popover.e2e.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.791)
- **Top Global Matches:** file_cluster_10: 4.791, file_cluster_13: 7.404, file_cluster_2: 7.479
- **Magnitude:** 407.23 | **LOC:** 264 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.224; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (87.6%), Guard Balance (formerly Safety Score) (41.5%), Mutation Surface (formerly State Flux) (18.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Concurrency (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 104`, `args: 27`, `func_start: 17`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 89`, `import: 3`
* *Defense:* `doc: 4`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fixture, test, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/menu/menu.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.459)
- **Top Global Matches:** file_cluster_12: 7.459, file_cluster_16: 8.473, file_cluster_4: 8.794
- **Magnitude:** 406.16 | **LOC:** 885 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.224; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 70.7317% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onEnd` **(Compute Cores)** (Impact: 29.8)
  * `afterAnimation` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `beforeAnimation` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `startAnimation` **(Stateful Encapsulated Methods)** (Impact: 15.2)
  * `_setOpen` **(Compute Cores)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 93`, `args: 44`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 38`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 1`, `concurrency: 26`, `import: 18`
* *Defense:* `safety: 2`, `doc: 46`, `test: 4`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` config, ionic-global, interface, gesture, menu-interface, core, cubic-bezier, focus-trap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/components/item-sliding/item-sliding.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.72)
- **Top Global Matches:** file_cluster_16: 7.72, file_cluster_15: 7.917, file_cluster_12: 8.462
- **Magnitude:** 399.08 | **LOC:** 519 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.224; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%)
- **Documentation Coverage:** 65.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setOpenAmount` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `open` **(Compute Cores)** (Impact: 21.3)
    * *Intent:* /** * Open the sliding item. * */
  * `onMove` **(Stateful Encapsulated Methods)** (Impact: 17.2)
  * `onEnd` **(Stateful Encapsulated Methods)** (Impact: 14.1)
  * `getOptions` **(Stateful Encapsulated Methods)** (Impact: 10.3)
    * *Intent:* /** * Given an optional side, return the ion-item-options element. * * return the first one availabl...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 53 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 58`, `args: 26`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 60`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 10`
* *Defense:* `safety: 2`, `doc: 17`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.224
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ionic-global, interface, gesture, menu-interface, core, content, helpers, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `core/src/utils/content/index.ts` (TYPESCRIPT) | Magnitude: 56.62 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 37, core_var_decl: 18, design_camel_case: 12
- `packages/react/src/routing/PageManager.tsx` (TYPESCRIPT) | Magnitude: 37.5 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 15, args: 10, func_start: 9
- `core/src/components/label/label.tsx` (TYPESCRIPT) | Magnitude: 32.64 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 14, decorators: 12, args: 9
- `core/src/utils/browser/index.ts` (TYPESCRIPT) | Magnitude: 44.12 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 51, indent_spaces: 48, args: 13, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `core/src/components/radio/radio.tsx` (TYPESCRIPT) | Magnitude: 78.14 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 30, core_var_decl: 28, decorators: 21
- `core/src/components/radio-group/test/supporting-text/index.html` (HTML) | Magnitude: 7.16 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 190, class_start: 79, core_var_decl: 72, design_snake_case: 71
- `core/src/components/breadcrumb/breadcrumb.tsx` (TYPESCRIPT) | Magnitude: 38.18 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 35, core_var_decl: 30, decorators: 23
- `core/src/components/datetime/test/disable-dates/index.html` (HTML) | Magnitude: 40.4 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, core_var_decl: 26, structural_boundaries: 24, design_snake_case: 22
- `core/src/components/toast/test/trigger/index.html` (HTML) | Magnitude: 50.25 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, core_var_decl: 14, design_snake_case: 13, class_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `core/src/components/button/test/perf/index.html` (HTML) | Magnitude: 111.96 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4440, class_start: 4415, core_var_decl: 4409, design_snake_case: 4405
- `core/src/components/item/test/reorder/index.html` (HTML) | Magnitude: 63.34 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 129, core_var_decl: 39, design_snake_case: 31, class_start: 18
- `core/src/components/breadcrumbs/test/collapsed/index.html` (HTML) | Magnitude: 44.74 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 204, class_start: 72, core_var_decl: 67, design_snake_case: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `core/src/components/refresher/test/basic/refresher.e2e.ts` (TYPESCRIPT) | Magnitude: 113.34 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 36, concurrency: 27, test: 22
- `core/src/components/select/test/highlight/select.e2e.ts` (TYPESCRIPT) | Magnitude: 249.85 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 439, structural_boundaries: 97, core_var_decl: 96, design_snake_case: 96
- `core/src/components/infinite-scroll/test/scroll-target/index.html` (HTML) | Magnitude: 20.52 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 16, design_snake_case: 15, structural_boundaries: 10
- `core/src/components/modal/animations/ios.enter.ts` (TYPESCRIPT) | Magnitude: 39.34 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 18, core_var_decl: 18, design_camel_case: 17
- `core/src/utils/test/playwright/matchers/toHaveReceivedEvent.ts` (TYPESCRIPT) | Magnitude: 12.04 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, args: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/angular/test/base/src/app/standalone/modal-custom-injector/test.service.ts` (TYPESCRIPT) | Magnitude: 6.92 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, api: 3, args: 2
- `packages/angular/test/base/src/app/standalone/popover-custom-injector/test.service.ts` (TYPESCRIPT) | Magnitude: 6.92 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, api: 3, args: 2
- `packages/angular/standalone/src/navigation/tabs.ts` (TYPESCRIPT) | Magnitude: 17.02 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 9, decorators: 8, import: 5
- `packages/react/src/components/index.ts` (TYPESCRIPT) | Magnitude: 43.3 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 38, api: 34, import: 34
- `core/src/components/toggle/test/basic/index.html` (HTML) | Magnitude: 56.06 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 52, class_start: 13, core_var_decl: 12, design_snake_case: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `core/src/utils/floating-point/floating-point.spec.ts` (TYPESCRIPT) | Magnitude: 48.08 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 26, test: 17, structural_boundaries: 10, args: 8
- `core/src/components/modal/test/modal-attributes.spec.tsx` (TYPESCRIPT) | Magnitude: 6.74 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 9, test: 8, core_var_decl: 7
- `packages/angular/test/base/src/app/lazy/tabs-basic/tabs-basic.component.css` (CSS) | Magnitude: 0.63 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 3, class_start: 1, safety_bypasses: 1, ui_framework: 1
- `packages/angular/test/base/src/app/lazy/tabs/tabs.component.css` (CSS) | Magnitude: 0.63 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 3, class_start: 1, safety_bypasses: 1, ui_framework: 1
- `packages/angular/test/base/src/app/standalone/tabs-basic/tabs-basic.component.css` (CSS) | Magnitude: 0.63 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 3, class_start: 1, safety_bypasses: 1, ui_framework: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `core/src/components/modal/test/sheet/index.html` (HTML) | Magnitude: 54.04 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 234, core_var_decl: 60, design_snake_case: 55, structural_boundaries: 25
- `core/src/components/picker-legacy-column/test/standalone/index.html` (HTML) | Magnitude: 33.98 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 66, core_var_decl: 19, design_snake_case: 17, structural_boundaries: 13
- `packages/angular/test/base/src/app/standalone/popover-custom-injector/popover-custom-injector.component.ts` (TYPESCRIPT) | Magnitude: 7.08 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 9, core_var_decl: 7, import: 4
- `core/src/components/toast/animations/ios.enter.ts` (TYPESCRIPT) | Magnitude: 14.44 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 15, core_var_decl: 6, import: 5
- `core/src/components/toast/animations/md.enter.ts` (TYPESCRIPT) | Magnitude: 14.58 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 15, core_var_decl: 6, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `core/src/components/segment-view/segment-view.tsx` (TYPESCRIPT) | Magnitude: 65.16 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 16, decorators: 13, core_var_decl: 12
- `packages/angular/common/src/directives/navigation/back-button.ts` (TYPESCRIPT) | Magnitude: 21.1 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, decorators: 6, import: 6
- `core/src/components/backdrop/backdrop.tsx` (TYPESCRIPT) | Magnitude: 12.76 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 10, decorators: 8, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/react/src/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/react/src/routing/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/react-router/test/base/src/react-app-env.d.ts` (TYPESCRIPT) | Magnitude: 1.35 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 28, branch: 11, api: 11
- `core/src/css/text-alignment.scss` (CSS) | Magnitude: 0.78 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, class_start: 8, immutability_locks: 8, import: 2
- `.github/workflows/assign-issues.yml` (YAML) | Magnitude: 16.32 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, args: 3, structural_boundaries: 2, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `core/src/utils/animation/test/animationbuilder/index.html` (HTML) | Magnitude: 19.98 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 121, core_var_decl: 26, design_snake_case: 24, structural_boundaries: 22
- `core/src/components/progress-bar/test/basic/index.html` (HTML) | Magnitude: 81.84 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, class_start: 42, core_var_decl: 22, design_snake_case: 22
- `packages/vue/test/base/src/views/VersionTest.vue` (HTML) | Magnitude: 45.04 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, class_start: 8, structural_boundaries: 3, decorators: 3
- `core/src/css/float-elements.scss` (CSS) | Magnitude: 0.77 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, class_start: 4, immutability_locks: 4, import: 2
- `packages/angular/test/base/src/app/lazy/router-link/router-link.component.html` (HTML) | Magnitude: 33.68 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 24, api: 18, core_var_decl: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/react/src/components/navigation/IonTabBar.tsx` (TYPESCRIPT) | Magnitude: 153.04 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 228, branch: 68, structural_boundaries: 64, ui_framework: 57
- `core/src/components/modal/gestures/swipe-to-close.ts` (TYPESCRIPT) | Magnitude: 115.2 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 146, core_var_decl: 53, structural_boundaries: 42, branch: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/vue/src/hooks/lifecycle.ts` (TYPESCRIPT) | Magnitude: 24.22 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 19, core_var_decl: 11, design_camel_case: 7
- `core/src/utils/overlays.ts` (TYPESCRIPT) | Magnitude: 451.22 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 402, structural_boundaries: 151, branch: 119, core_var_decl: 106
- `packages/angular/common/src/providers/angular-delegate.ts` (TYPESCRIPT) | Magnitude: 140.56 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 46, branch: 25, core_var_decl: 25
- `packages/angular/common/src/types/interfaces.ts` (TYPESCRIPT) | Magnitude: 16.16 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, branch: 3, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/vue/src/components/IonBackButton.ts` (TYPESCRIPT) | Magnitude: 6.4 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, branch: 6, core_var_decl: 5
- `packages/angular/common/src/directives/navigation/router-outlet.ts` (TYPESCRIPT) | Magnitude: 270.98 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 317, structural_boundaries: 68, branch: 49, args: 45
- `core/src/components/reorder-group/reorder-group-interface.ts` (TYPESCRIPT) | Magnitude: 21.52 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 14, class_start: 6, api: 6
- `core/src/components/refresher/test/scroll-target/refresher.e2e.ts` (TYPESCRIPT) | Magnitude: 63.12 | Delta: **0.164** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 19, concurrency: 11, test: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `core/src/utils/test/playwright/page/utils/set-ion-viewport.ts` (TYPESCRIPT) | Magnitude: 26.06 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, branch: 9, core_var_decl: 7
- `core/src/components/refresher-content/refresher-content.tsx` (TYPESCRIPT) | Magnitude: 36.72 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 34, core_var_decl: 24, branch: 22

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/src/components/range/test/custom/range.e2e.ts` -> **Brandy Smith** (100.0% isolated ownership) | Magnitude: 1923.11
- `core/src/components/input-otp/test/basic/input-otp.e2e.ts` -> **Kanhaiya Pandey** (100.0% isolated ownership) | Magnitude: 632.66
- `core/src/components/refresher/refresher.tsx` -> **Shane** (100.0% isolated ownership) | Magnitude: 584.6
- `core/src/components/modal/test/safe-area/modal.e2e.ts` -> **Shane** (100.0% isolated ownership) | Magnitude: 578.52
- `core/src/components/datetime/test/custom/datetime.e2e.ts` -> **Maria Hutt** (100.0% isolated ownership) | Magnitude: 560.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/src/global/ionic-global.ts` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)
- `core/src/components/modal/modal.tsx` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `core/src/utils/gesture/index.ts` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `core/src/components/datetime/datetime.tsx` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `core/src/components/modal/gestures/swipe-to-close.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `core/scripts/testing/scripts.js` -> **Severity: 7.191** (Embedded: 0.1357 * Error Risk: 52.9964%)
- `core/src/global/ionic-global.ts` -> **Severity: 3.402** (Embedded: 0.0425 * Error Risk: 80.0%)
- `core/src/components/router/utils/interface.ts` -> **Severity: 3.302** (Embedded: 0.0614 * Error Risk: 53.743%)
- `core/src/global/config.ts` -> **Severity: 2.424** (Embedded: 0.0303 * Error Risk: 80.0%)
- `core/src/utils/platform.ts` -> **Severity: 1.685** (Embedded: 0.0254 * Error Risk: 66.4583%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/src/components/router/utils/interface.ts` -> **Severity: 2726.9** (Blast Radius: 27.269 * Doc Risk: 100.0%)
- `core/src/global/ionic-global.ts` -> **Severity: 970.3** (Blast Radius: 9.703 * Doc Risk: 100.0%)
- `core/src/global/config.ts` -> **Severity: 791.1** (Blast Radius: 7.911 * Doc Risk: 100.0%)
- `packages/react/src/components/react-component-lib/utils/case.ts` -> **Severity: 343.2** (Blast Radius: 3.432 * Doc Risk: 100.0%)
- `core/src/utils/platform.ts` -> **Severity: 310.0** (Blast Radius: 3.1 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 460 literal sites + 4 sites through wrappers = 464
- **`panics_and_aborts`:** 158 literal sites + 3 sites through wrappers = 161

- `error` (function, debug_prints, primitive): 3 call sites in 1 files -- `core/scripts/treeshaking.js`
- `error` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `core/scripts/treeshaking.js`
- `printRequiredElementError` (function, debug_prints, primitive): 1 call sites in 1 files -- `core/src/utils/logging/index.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9051 call pairs -- scoped 27.3%, unique 0.0%, ambiguous 15.6%, external 57.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 7634 | 30.0% | 0.0% | 18.3% | 51.8% |
| html | 1190 | 13.4% | 0.0% | 0.0% | 86.6% |
| javascript | 166 | 12.7% | 0.0% | 8.4% | 78.9% |
| shell | 54 | 0.0% | 0.0% | 0.0% | 100.0% |
| java | 5 | 0.0% | 0.0% | 0.0% | 100.0% |
| groovy | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
