# ARCHITECTURAL_BRIEF: react-router
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/remix-run/react-router.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1094 analyzed artifact(s), 157347 LOC.
- **Load-bearing artifact:** `packages/react-router/lib/router/history.ts` -- 57 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `integration/rsc/rsc-test.ts` -- pulls in 67 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/react-router-dev/vite/route-chunks-test.ts` at magnitude 27698.11 (structural weight, not risk).
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
| Total Artifacts | 1480 |
| Analyzed Artifacts (Scanned) | 1094 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 386 |
| Total LOC | 157347 |
| Volatility Index | 0.022 |
| % Scanned of codebase = | 73.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6904 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1798 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3226 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 57 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 732 | 152913 | 66.9% |
| MARKDOWN | 88 | 0 | 8.0% |
| JAVASCRIPT | 68 | 1817 | 6.2% |
| PLAINTEXT | 66 | 2 | 6.0% |
| JSON | 66 | 1371 | 6.0% |
| CSS | 43 | 798 | 3.9% |
| HTML | 25 | 303 | 2.3% |
| SHELL | 5 | 119 | 0.5% |
| YAML | 1 | 24 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.998`
> **Composition Archetype:** `Mid Flat Project` (z +3.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Declarative / Non-Code 20%, Callbacks & Closures Files 8%, Generic / Templated Code Files 8%, Large Core Modules (3) 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 940 | 85.9% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 152 | 13.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 386*

**Composition by Extension & Reason:**
- `.md`: 206x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 126 LOC)
- `no_extension`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 8x Excluded (Static Asset Blob without Intent: 1476 LOC), 5x Excluded (Static Asset Blob without Intent: 1542 LOC), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 488, Signals: 0)
- `.ico`: 23x Excluded (Explicitly Denied Extension: '.ico')
- `.ts`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 178 LOC)
- `.gz`: 3x Excluded (Explicitly Denied Extension: '.gz')
- `.tsx`: 1x Excluded (Machine-Generated Source Code Signature: 71 LOC), 1x Excluded (Machine-Generated Source Code Signature: 634 LOC), 1x Excluded (Machine-Generated Source Code Signature: 73 LOC)
- `.patch`: 3x Excluded (Unsupported Extension: '.patch')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 1x Excluded (Explicitly Denied Extension: '.tgz')
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')
- `.snap`: 1x Excluded (Unsupported Extension: '.snap')
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 19359 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 18.9 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 22.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.2 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.1 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.8 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 70.4 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.5 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 835 | 232 | 2 | `packages/react-router/__tests__/router/context-middleware-test.tsx` |
| cleanup | 194 | 98 | 0 | `packages/react-router/__tests__/router/should-revalidate-test.ts` |
| guards | 2573 | 306 | 5 | `packages/react-router-dev/vite/plugin.ts` |
| danger | 1862 | 246 | 3 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| concurrency | 14238 | 339 | 22 | `integration/single-fetch-test.ts` |
| connectivity | 4460 | 633 | 6 | `integration/single-fetch-test.ts` |
| io | 6438 | 370 | 11 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 11 | 0 | `packages/create-react-router/__tests__/create-react-router-test.ts` |
| time | 246 | 104 | 0 | `integration/client-data-test.ts` |
| serialization | 348 | 116 | 1 | `integration/headers-test.ts` |
| regex | 350 | 90 | 0 | `packages/react-router-dev/vite/plugin.ts` |
| events | 1032 | 188 | 2 | `integration/single-fetch-test.ts` |
| tests | 13534 | 241 | 22 | `packages/react-router/__tests__/router/lazy-test.ts` |
| docs | 923 | 147 | 1 | `packages/react-router/lib/router/utils.ts` |
| debt | 1472 | 179 | 2 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| mutation | 22926 | 630 | 50 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| dead_code | 246 | 121 | 1 | `packages/react-router-dev/vite/route-chunks.ts` |
| credential | 50 | 6 | 0 | `tutorials/address-book/app/data.ts` |
| threat | 85 | 38 | 0 | `packages/react-router/lib/components.tsx` |
| ml_ai | 63 | 24 | 0 | `examples/ssr-data-router/src/App.tsx` |
| ui | 5742 | 317 | 10 | `packages/react-router/__tests__/useNavigate-test.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/react-router/__tests__/dom/data-browser-router-test.tsx` (Hits: 391)
- `packages/react-router/__tests__/router/fetchers-test.ts` (Hits: 322)
- `packages/react-router/__tests__/router/context-middleware-test.tsx` (Hits: 240)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **history.ts** (`packages/react-router/lib/router/history.ts`) — 57 inbound connections
2. **router.ts** (`packages/react-router/lib/router/router.ts`) — 45 inbound connections
3. **utils.ts** (`packages/react-router/__tests__/router/utils/utils.ts`) — 26 inbound connections
4. **express.ts** (`integration/helpers/express.ts`) — 21 inbound connections
5. **utils.ts** (`packages/react-router/lib/router/utils.ts`) — 21 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rsc-test.ts** (`integration/rsc/rsc-test.ts`) — 67 outbound dependencies
2. **plugin.ts** (`packages/react-router-dev/vite/plugin.ts`) — 46 outbound dependencies
3. **index.ts** (`packages/react-router/index.ts`) — 39 outbound dependencies
4. **typegen-test.ts** (`integration/typegen-test.ts`) — 33 outbound dependencies
5. **vite.ts** (`integration/helpers/vite.ts`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createRouter` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **583.0** | LOC: 2100
  * *Intent:* //#endregion //////////////////////////////////////////////////////////////////////////////// //#region createRouter /////////////////////////////////...
- `getMatchesToLoad` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **277.7** | LOC: 300
- `createStaticHandler` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **267.2** | LOC: 944
- `reactRouterRSCVitePlugin` **(I/O & Config Routines)** (@ `packages/react-router-dev/vite/rsc/plugin.ts`) -> Impact: **232.9** | LOC: 938
- `handleLoaders` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **192.8** | LOC: 265
  * *Intent:* // Call all applicable loaders for the given matches, handling redirects, // errors, etc.
- `createClientRoutes` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/dom/ssr/routes.tsx`) -> Impact: **173.5** | LOC: 350
- `resolveConfig` **(Defensive Guards)** (@ `packages/react-router-dev/config/config.ts`) -> Impact: **145.5** | LOC: 308
- `useRoutesImpl` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/hooks.tsx`) -> Impact: **145.5** | LOC: 1235
  * *Intent:* // Internal implementation with accept optional param for RouterProvider usage
- `handleFetcherAction` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **135.3** | LOC: 318
  * *Intent:* // Call the action for the matched fetcher.submit(), and then handle redirects, // errors, and revalidation
- `setup` **(Compute Cores)** (@ `packages/react-router/__tests__/router/utils/data-router-setup.ts`) -> Impact: **134.2** | LOC: 535

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `integration` | 87 | 50842.93 | 71.63% | 3.74% |
| `packages/react-router-dev/vite` | 27 | 32043.65 | 19.38% | 2.18% |
| `integration/rsc` | 4 | 23538.1 | 47.41% | 0.0% |
| `packages/react-router/__tests__/router` | 28 | 11793.29 | 35.21% | 28.31% |
| `packages/react-router/lib/router` | 5 | 7003.7 | 28.06% | 11.43% |
| `__monolith__` | 17 | 5176.16 | 0.39% | 0.0% |
| `packages/react-router/__tests__/dom` | 25 | 3320.32 | 9.7% | 38.04% |
| `packages/react-router/__tests__` | 40 | 2415.05 | 10.82% | 21.49% |
| `packages/react-router/lib/dom/ssr` | 16 | 1988.58 | 33.13% | 1.66% |
| `packages/create-react-router` | 16 | 1941.04 | 36.84% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/react-router/__tests__/dom/partial-hydration-test.tsx` -> **99.9997%** Exposure
- `packages/react-router/__tests__/router/instrumentation-test.ts` -> **99.9983%** Exposure
- `packages/react-router/__tests__/dom/navigate-encode-params-test.tsx` -> **99.9976%** Exposure
- `packages/react-router/__tests__/route-depth-order-matching-test.tsx` -> **99.9959%** Exposure
- `packages/react-router/__tests__/dom/client-on-error-test.tsx` -> **99.9952%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `integration/cli-test.ts` -> **100.0%** Exposure
- `integration/helpers/playwright-fixture.ts` -> **100.0%** Exposure
- `integration/helpers/vite-plugin-cloudflare-template/app/entry.server.tsx` -> **100.0%** Exposure
- `packages/create-react-router/prompts-text.ts` -> **100.0%** Exposure
- `packages/react-router-dev/cli/run.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/react-router/__tests__/dom/data-browser-router-test.tsx` -> **0** Orphaned Functions | **166** Duplicates
- `packages/react-router/__tests__/router/context-middleware-test.tsx` -> **0** Orphaned Functions | **115** Duplicates
- `packages/react-router/__tests__/router/instrumentation-test.ts` -> **0** Orphaned Functions | **76** Duplicates
- `packages/react-router/__tests__/data-memory-router-test.tsx` -> **0** Orphaned Functions | **54** Duplicates
- `packages/react-router/__tests__/react-transitions-test.tsx` -> **0** Orphaned Functions | **54** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1548` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/react-router-dev/vite/route-chunks-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 27698.11 | **LOC:** 1636 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (33.9%), Concurrency Surface (formerly Concurrency) (20.9%), Connectivity (formerly Api Exposure) (15.2%), Guard Balance (formerly Safety Score) (13.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 725`, `args: 285`, `func_start: 200`, `class_start: 8`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `io: 6`, `api: 275`, `concurrency: 3`, `import: 127`
* *Defense:* `safety: 123`, `test: 308`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cache, check, defaultMessage, messages, route-chunks, shared, sharedMessage, side-effect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/rsc/rsc-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 22058.16 | **LOC:** 2729 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **67**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (54.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.2%), Guard Balance (formerly Safety Score) (38.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 546
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 899`, `args: 259`, `func_start: 203`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`
* *Architecture:* `io: 120`, `api: 125`, `concurrency: 421`, `import: 156`
* *Defense:* `safety: 31`, `test: 164`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` get-context, request-context, client, dashboard.client, events, home.actions, home.client, redirect.actions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/vite-spa-mode-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 7828.39 | **LOC:** 1284 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (69.3%), Guard Balance (formerly Safety Score) (40.4%), Mutation Surface (formerly State Flux) (28.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 318
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 355`, `args: 115`, `func_start: 96`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `io: 28`, `api: 83`, `concurrency: 148`, `import: 58`
* *Defense:* `safety: 16`, `test: 88`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` routeImportTracker, create-fixture.js, playwright-fixture.js, vite.js, routeImportTracker, test, routes, vite...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/lib/router/router.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5361.48 | **LOC:** 7322 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 81.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **3**; blast radius 20.669; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Concurrency Surface (formerly Concurrency) (96.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.2%)
- **Documentation Coverage:** 83.4171% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createRouter` **(Many-Argument Workhorses)** (Impact: 583.0)
    * *Intent:* //#endregion //////////////////////////////////////////////////////////////////////////////// //#reg...
  * `getMatchesToLoad` **(Many-Argument Workhorses)** (Impact: 277.7)
  * `createStaticHandler` **(Many-Argument Workhorses)** (Impact: 267.2)
  * `handleLoaders` **(Many-Argument Workhorses)** (Impact: 192.8)
    * *Intent:* // Call all applicable loaders for the given matches, handling redirects, // errors, etc.
  * `handleFetcherAction` **(Many-Argument Workhorses)** (Impact: 135.3)
    * *Intent:* // Call the action for the matched fetcher.submit(), and then handle redirects, // errors, and reval...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 265 instances
* *Concurrency (weighted view):* 357
* *State Mutation (weighted view):* 840
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1106`, `structural_boundaries: 771`, `args: 305`, `func_start: 187`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 310`, `dead_code: 5`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 88`, `api: 37`, `concurrency: 182`, `import: 6`
* *Defense:* `safety: 112`, `doc: 76`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.669
  * `Choke Point (Betweenness):` 0.000937 | `Ripple Effect (Closeness):` 0.050501
  * `Imports (Out-Degree: 2):` history, instrumentation, utils
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/fetcher-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3236.51 | **LOC:** 594 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (55.0%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 59 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 434
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 213`, `args: 73`, `func_start: 37`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 20`, `concurrency: 139`, `import: 13`
* *Defense:* `safety: 1`, `test: 20`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, playwright-fixture.js, test, react, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/link-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2665.31 | **LOC:** 668 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Guard Balance (formerly Safety Score) (45.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.3%), Complexity Load (formerly Cognitive Load) (17.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 151`, `args: 52`, `func_start: 39`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 2`, `api: 33`, `concurrency: 40`, `import: 29`
* *Defense:* `safety: 2`, `test: 22`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ), app.css?url, favicon.ico, create-fixture.js, playwright-fixture.js, vite.js, reset.css?url, g)...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/plugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2601.32 | **LOC:** 4372 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 17.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **46**; blast radius 0.966; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.4%), Connectivity (formerly Api Exposure) (66.5%)
- **Documentation Coverage:** 98.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getEnvironmentOptionsResolvers` **(Defensive Guards)** (Impact: 109.3)
  * `handlePrerender` **(Many-Argument Workhorses)** (Impact: 66.7)
  * `handler` **(I/O & Config Routines)** (Impact: 53.5)
    * *Intent:* // After the SSR build is finished, we inspect the Vite manifest for // the SSR build and move serve...
  * `postProcess` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `resolveId` **(Many-Argument Workhorses)** (Impact: 47.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 40 instances
* *Amplified Cascading Flux:* 83 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 434
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 654`, `args: 218`, `func_start: 141`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 102`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 145`, `api: 67`, `concurrency: 234`, `import: 59`
* *Defense:* `safety: 136`, `doc: 3`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.966
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.000914
  * `Imports (Out-Degree: 19):` $getRouteChunkModuleId(
                chunkBasePath, $getRouteChunkModuleId(
            chunkBasePath, $virtualHmrRuntime.id, ), config, routes, invariant, manifest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `integration/headers-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2442.71 | **LOC:** 473 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (39.1%), Complexity Load (formerly Cognitive Load) (23.3%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 130`, `args: 50`, `func_start: 48`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 32`, `concurrency: 42`, `import: 13`
* *Defense:* `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, test, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/single-fetch-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2399.32 | **LOC:** 4669 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.3%), Mutation Surface (formerly State Flux) (74.9%), Guard Balance (formerly Safety Score) (47.8%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `error` **(I/O & Config Routines)** (Impact: 7.7)
  * `error` **(Callbacks & Closures)** (Impact: 6.1)
  * `error` **(I/O & Config Routines)** (Impact: 3.2)
  * `error` **(Annotated & Test Methods)** (Impact: 2.7)
  * `error` **(Annotated & Test Methods)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 178 instances
* *Amplified Cascading Flux:* 100 instances
* *Concurrency (weighted view):* 1603
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 1558`, `args: 454`, `func_start: 400`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 161`
* *Architecture:* `io: 43`, `api: 304`, `concurrency: 713`, `import: 139`
* *Defense:* `safety: 7`, `test: 416`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parent, create-fixture.js, playwright-fixture.js, vite.js, test, vite, node, get-port...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/redirects-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2155.5 | **LOC:** 309 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (90.7%), Guard Balance (formerly Safety Score) (43.8%), Mutation Surface (formerly State Flux) (40.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 120`, `args: 36`, `func_start: 22`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 19`, `concurrency: 48`, `import: 19`
* *Defense:* `safety: 3`, `test: 22`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, playwright-fixture.js, vite.js, test, react, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/revalidate-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1749.04 | **LOC:** 368 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (28.8%), Mutation Surface (formerly State Flux) (9.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 128`, `args: 19`, `func_start: 11`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 8`, `concurrency: 87`, `import: 7`
* *Defense:* `safety: 6`, `test: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, playwright-fixture.js, test, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/context-middleware-test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1743.06 | **LOC:** 3924 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Complexity Load (formerly Cognitive Load) (96.7%), Guard Balance (formerly Safety Score) (44.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `respondWithJson` **(Defensive Guards)** (Impact: 6.4)
  * `generateMiddlewareResponse` **(Type Conversions)** (Impact: 4.0)
  * `generateMiddlewareResponse` **(Type Conversions)** (Impact: 4.0)
  * `pushOrderContext` **(Generic / Templated Code)** (Impact: 3.8)
  * `generateMiddlewareResponse` **(Type Conversions)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 149 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 1213
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 706`, `args: 407`, `func_start: 357`, `class_start: 1`
* *Risk/State:* `state_mutation: 137`, `duplicate_logic: 115`
* *Architecture:* `io: 240`, `concurrency: 468`, `import: 9`
* *Defense:* `safety: 21`, `test: 260`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` components, history, router, utils, data-router-setup, utils, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/vite-prerender-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1714.18 | **LOC:** 3072 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Mutation Surface (formerly State Flux) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.3%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createFixture` **(Generic / Templated Code)** (Impact: 20.6)
  * `listAllFiles` **(Callbacks & Closures)** (Impact: 6.8)
  * `recurse` **(Callbacks & Closures)** (Impact: 6.3)
  * `captureRequests` **(Callbacks & Closures)** (Impact: 4.9)
  * `clearRequests` **(State Mutators)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 138 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 1237
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 1079`, `args: 262`, `func_start: 239`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 111`
* *Architecture:* `io: 24`, `api: 211`, `concurrency: 547`, `import: 108`
* *Defense:* `safety: 55`, `test: 317`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, playwright-fixture.js, vite.js, test, vite, node:fs, node:path, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/vite-build-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1692.71 | **LOC:** 398 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (87.4%), Guard Balance (formerly Safety Score) (40.9%), Mutation Surface (formerly State Flux) (32.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 123
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 134`, `args: 45`, `func_start: 28`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 11`, `api: 24`, `concurrency: 33`, `import: 26`
* *Defense:* `safety: 4`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test.css?url, test.txt?url, code-split-component, ssr-code-split-lib, utils.server, code-split.module.css, vite.js, rollup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/dom/data-browser-router-test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1685.0 | **LOC:** 8843 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.8%), Debt Markers (formerly Tech Debt) (93.3%), Guard Balance (formerly Safety Score) (45.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testDomRouter` **(Many-Argument Workhorses)** (Impact: 117.9)
  * `assertLocation` **(Many-Argument Workhorses)** (Impact: 12.7)
    * *Intent:* // Utility to assert location info based on the type of router
  * `setupTest` **(Many-Argument Workhorses)** (Impact: 9.7)
  * `Component` **(Callbacks & Closures)** (Impact: 7.0)
  * `ErrorBoundary` **(Callbacks & Closures)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 40 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 655
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 1227`, `args: 871`, `func_start: 533`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 46`, `dead_code: 1`, `duplicate_logic: 166`
* *Architecture:* `io: 391`, `concurrency: 455`, `import: 7`
* *Defense:* `safety: 67`, `test: 553`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index, utils, getHtml, getWindow, react, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/middleware-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1643.38 | **LOC:** 2959 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.1%), Mutation Surface (formerly State Flux) (50.3%), Guard Balance (formerly Safety Score) (46.3%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `error` **(Callbacks & Closures)** (Impact: 34.7)
  * `error` **(I/O & Config Routines)** (Impact: 5.7)
  * `error` **(Compute Cores)** (Impact: 4.0)
  * `log` **(Defensive Guards)** (Impact: 3.9)
  * `error` **(Defensive Guards)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 126 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 1050
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 1163`, `args: 386`, `func_start: 299`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 120`
* *Architecture:* `io: 14`, `api: 300`, `concurrency: 420`, `import: 158`
* *Defense:* `safety: 36`, `test: 227`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` context, create-fixture.js, playwright-fixture.js, vite.js, test, vite, node, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/passthrough-requests-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1630.97 | **LOC:** 232 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Mutation Surface (formerly State Flux) (91.1%), Guard Balance (formerly Safety Score) (45.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 109
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 63`, `args: 13`, `func_start: 10`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 19`, `api: 8`, `concurrency: 34`, `import: 6`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, playwright-fixture.js, vite.js, test, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/navigation-state-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1470.72 | **LOC:** 468 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (65.4%), Complexity Load (formerly Cognitive Load) (41.8%), Mutation Surface (formerly State Flux) (17.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 86
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 102`, `args: 21`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 4`
* *Architecture:* `api: 15`, `concurrency: 51`, `import: 11`
* *Defense:* `test: 16`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, playwright-fixture.js, test, react, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/rsc/rsc-nojs-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1372.22 | **LOC:** 261 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (66.7%), Guard Balance (formerly Safety Score) (42.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 87`, `args: 28`, `func_start: 18`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 16`, `api: 7`, `concurrency: 43`, `import: 16`
* *Defense:* `safety: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` home.actions, home.client, home, home, lazy, root, utils, test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/deduped-route-modules-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1151.2 | **LOC:** 288 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (93.2%), Complexity Load (formerly Cognitive Load) (88.8%), Guard Balance (formerly Safety Score) (54.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 110`, `args: 30`, `func_start: 5`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 26`, `concurrency: 27`, `import: 15`
* *Defense:* `safety: 2`, `test: 22`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` client, client-first.a, create-fixture.js, playwright-fixture.js, vite.js, route, test, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/ssr-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1011.4 | **LOC:** 2292 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (97.5%), Mutation Surface (formerly State Flux) (40.2%), Guard Balance (formerly Safety Score) (26.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loader` **(Callbacks & Closures)** (Impact: 8.0)
  * `queryRoute` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `action` **(Callbacks & Closures)** (Impact: 4.9)
  * `setupFlexRouteTest` **(I/O & Config Routines)** (Impact: 4.9)
  * `loader` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 95 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 761
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 382`, `args: 197`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 76`, `duplicate_logic: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 103`, `concurrency: 286`, `import: 6`
* *Defense:* `safety: 75`, `doc: 1`, `test: 341`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` router, utils, data-router-setup, urlDataStrategy, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/lazy-discovery-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1007.04 | **LOC:** 2617 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (95.1%), Complexity Load (formerly Cognitive Load) (88.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 7.6)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 73 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 641
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 301`, `args: 201`, `func_start: 138`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 64`, `planned_debt: 1`, `duplicate_logic: 35`
* *Architecture:* `io: 201`, `concurrency: 276`, `import: 7`
* *Defense:* `safety: 5`, `test: 251`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` history, router, utils, data-router-setup, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/browser-entry-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 979.38 | **LOC:** 323 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.678; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (96.3%), Guard Balance (formerly Safety Score) (45.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Concurrency (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 96`, `args: 31`, `func_start: 22`
* *Risk/State:* `state_mutation: 8`, `fragile_debt: 1`
* *Architecture:* `io: 13`, `api: 12`, `concurrency: 51`, `import: 18`
* *Defense:* `test: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` entry.client, create-fixture.js, playwright-fixture.js, test, react, client, react-router, dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/fetcher-layout-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 968.45 | **LOC:** 277 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.678; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Guard Balance (formerly Safety Score) (44.1%), Mutation Surface (formerly State Flux) (26.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 102
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 93`, `args: 30`, `func_start: 22`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 14`, `concurrency: 47`, `import: 10`
* *Defense:* `test: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, playwright-fixture.js, test, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-router/lib/rsc/server.rsc.ts` -> Churn: **67.47%** | Cog Load: 76.1524% | Debt: 34.248%
- `packages/react-router/lib/router/router.ts` -> Churn: **66.94%** | Cog Load: 62.2338% | Debt: 9.697%
- `integration/client-data-test.ts` -> Churn: **53.26%** | Cog Load: 99.3723% | Debt: 10.3775%
- `packages/react-router-dev/vite/rsc/plugin.ts` -> Churn: **53.26%** | Cog Load: 77.6626% | Debt: 8.2024%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `integration/rsc/rsc-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 22058.16
- `packages/react-router/lib/router/router.ts` -> **Matt Brophy** (81.0% isolated ownership) | Magnitude: 5361.48
- `integration/fetcher-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 3236.51
- `integration/passthrough-requests-test.ts` -> **Matt Brophy** (100.0% isolated ownership) | Magnitude: 1630.97
- `integration/rsc/rsc-nojs-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 1372.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react-router/lib/server-runtime/server.ts` -> **Severity: 0.095** (Bridge: 0.001 * Flux: 97.9202%)
- `packages/react-router/lib/router/instrumentation.ts` -> **Severity: 0.093** (Bridge: 0.001 * Flux: 93.0148%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 0.092** (Bridge: 0.0009 * Flux: 97.751%)
- `packages/react-router/lib/dom/dom.ts` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 99.8466%)
- `packages/react-router/lib/dom/ssr/routes.tsx` -> **Severity: 0.015** (Bridge: 0.0003 * Flux: 52.0678%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/react-router/lib/router/history.ts` -> **Severity: 5.238** (Embedded: 0.0678 * Error Risk: 77.2951%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 3.453** (Embedded: 0.0505 * Error Risk: 68.366%)
- `packages/react-router/lib/router/instrumentation.ts` -> **Severity: 2.236** (Embedded: 0.0339 * Error Risk: 65.9175%)
- `packages/react-router/lib/server-runtime/urls.ts` -> **Severity: 1.893** (Embedded: 0.0214 * Error Risk: 88.6667%)
- `packages/react-router/lib/server-runtime/data.ts` -> **Severity: 1.673** (Embedded: 0.0262 * Error Risk: 63.8242%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/react-router/lib/router/history.ts` -> **Severity: 2275.838** (Blast Radius: 39.195 * Doc Risk: 58.0645%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 1724.148** (Blast Radius: 20.669 * Doc Risk: 83.4171%)
- `integration/helpers/express.ts` -> **Severity: 1433.3** (Blast Radius: 14.333 * Doc Risk: 100.0%)
- `packages/react-router/lib/router/instrumentation.ts` -> **Severity: 1160.1** (Blast Radius: 11.601 * Doc Risk: 100.0%)
- `packages/create-react-router/__tests__/github-mocks.ts` -> **Severity: 714.8** (Blast Radius: 7.148 * Doc Risk: 100.0%)

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
