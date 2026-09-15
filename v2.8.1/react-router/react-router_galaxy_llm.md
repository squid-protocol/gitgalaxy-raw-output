# ARCHITECTURAL_BRIEF: react-router
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/remix-run/react-router.git` |
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
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.66; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Declarative / Non-Code 20%, Interface Declarations Files 12%, Callbacks & Closures Files 8%, Large Core Modules 6%
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
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 23.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.2 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.1 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 64.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 11.0 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 71.7 | 4.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 48.5 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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

- `createRouter` **(Compute Cores)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **583.0** | LOC: 2100
  * *Intent:* //#endregion //////////////////////////////////////////////////////////////////////////////// //#region createRouter /////////////////////////////////...
- `getMatchesToLoad` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **277.7** | LOC: 300
- `createStaticHandler` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **267.2** | LOC: 944
- `reactRouterRSCVitePlugin` **(Compute Cores)** (@ `packages/react-router-dev/vite/rsc/plugin.ts`) -> Impact: **232.9** | LOC: 938
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

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/react-router/lib/rsc/server.rsc.ts` (TYPESCRIPT) -> Cumulative Risk: **782.32**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.33)
- **Magnitude:** 818.96 | **LOC:** 1502 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 43.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9332%), Documentation (96.1538%), State Flux (90.7625%)
- **Heaviest Functions:** `processServerAction` (Many-Argument Workhorses, Impact: 80.2), `replace` (Compute Cores, Impact: 79.8), `generateMiddlewareResponse` (Defensive Guards, Impact: 34.9)

### 2. `packages/react-router/__tests__/router/utils/data-router-setup.ts` (TYPESCRIPT) -> Cumulative Risk: **758.3**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.88)
- **Magnitude:** 706.06 | **LOC:** 763 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `setup` (Compute Cores, Impact: 134.2), `getFetcherHelpers` (Many-Argument Workhorses, Impact: 42.0), `fetch` (Many-Argument Workhorses, Impact: 30.7)

### 3. `packages/react-router/lib/router/router.ts` (TYPESCRIPT) -> Cumulative Risk: **747.73**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.01)
- **Magnitude:** 5361.48 | **LOC:** 7322 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 81.8%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.751%), Concurrency (96.166%), Documentation (83.4171%)
- **Heaviest Functions:** `createRouter` (Compute Cores, Impact: 583.0), `getMatchesToLoad` (Many-Argument Workhorses, Impact: 277.7), `createStaticHandler` (Many-Argument Workhorses, Impact: 267.2)

### 4. `packages/react-router-dev/cli/commands.ts` (TYPESCRIPT) -> Cumulative Risk: **722.76**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.36)
- **Magnitude:** 313.62 | **LOC:** 309 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.451%)
- **Heaviest Functions:** `generateEntry` (Many-Argument Workhorses, Impact: 63.0), `routes` (Defensive Guards, Impact: 16.7), `typegen` (Defensive Guards, Impact: 15.7)

### 5. `packages/react-router-dev/vite/rsc/plugin.ts` (TYPESCRIPT) -> Cumulative Risk: **719.96**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.20)
- **Magnitude:** 930.58 | **LOC:** 982 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 45.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8888%), State Flux (84.1895%)
- **Heaviest Functions:** `reactRouterRSCVitePlugin` (Compute Cores, Impact: 232.9), `postProcess` (Many-Argument Workhorses, Impact: 117.8), `config` (Many-Argument Workhorses, Impact: 93.9)

### 6. `packages/react-router/lib/dom/ssr/single-fetch.tsx` (TYPESCRIPT) -> Cumulative Risk: **718.71**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.80)
- **Magnitude:** 480.22 | **LOC:** 858 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (95.4622%)
- **Heaviest Functions:** `fetchAndDecodeViaTurboStream` (Many-Argument Workhorses, Impact: 49.2), `singleFetchUrl` (Many-Argument Workhorses, Impact: 28.7), `unwrapSingleFetchResult` (Compute Cores, Impact: 24.3)

### 7. `integration/helpers/vite.ts` (TYPESCRIPT) -> Cumulative Risk: **715.35**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.16)
- **Magnitude:** 456.78 | **LOC:** 616 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 44.4%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `EXPRESS_SERVER` (Defensive Guards, Impact: 35.8), `reactRouterConfig` (Compute Cores, Impact: 25.0), `basic` (Compute Cores, Impact: 23.6)

### 8. `packages/react-router/lib/dom/ssr/fog-of-war.ts` (TYPESCRIPT) -> Cumulative Risk: **707.41**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.79)
- **Magnitude:** 262.48 | **LOC:** 365 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9974%), State Flux (99.012%)
- **Heaviest Functions:** `fetchAndApplyManifestPatches` (Many-Argument Workhorses, Impact: 69.5), `useFogOFWarDiscovery` (Many-Argument Workhorses, Impact: 33.7), `getPatchRoutesOnNavigationFunction` (Many-Argument Workhorses, Impact: 15.9)

### 9. `packages/react-router-dev/config/config.ts` (TYPESCRIPT) -> Cumulative Risk: **703.27**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.58)
- **Magnitude:** 762.3 | **LOC:** 1198 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 35.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9089%), Documentation (97.2973%)
- **Heaviest Functions:** `resolveConfig` (Defensive Guards, Impact: 145.5), `isValidPrerenderPathsConfig` (Defensive Guards, Impact: 112.6), `createConfigLoader` (Compute Cores, Impact: 58.8)

### 10. `packages/react-router-dev/vite/plugin.ts` (TYPESCRIPT) -> Cumulative Risk: **694.1**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.15)
- **Magnitude:** 2601.32 | **LOC:** 4372 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 16.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9514%), Documentation (98.2353%), Verification (80.0%)
- **Heaviest Functions:** `getEnvironmentOptionsResolvers` (Defensive Guards, Impact: 109.3), `handlePrerender` (Many-Argument Workhorses, Impact: 66.7), `handler` (Defensive Guards, Impact: 53.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/react-router-dev/vite/route-chunks-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 27698.11 | **LOC:** 1636 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5053%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 22058.16 | **LOC:** 2729 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.6045%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7828.39 | **LOC:** 1284 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (69.2711%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5361.48 | **LOC:** 7322 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 81.8%
- **Risk Profile:** Cognitive Load (62.2338%), Tech Debt (9.697%)
**Top Internal Functions/Classes:**
  * `createRouter` **(Compute Cores)** (Impact: 583.0)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Risk Profile:** Cognitive Load (99.976%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2665.31 | **LOC:** 668 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (17.592%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2601.32 | **LOC:** 4372 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (44.5655%), Tech Debt (8.4608%)
**Top Internal Functions/Classes:**
  * `getEnvironmentOptionsResolvers` **(Defensive Guards)** (Impact: 109.3)
  * `handlePrerender` **(Many-Argument Workhorses)** (Impact: 66.7)
  * `handler` **(Defensive Guards)** (Impact: 53.5)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2442.71 | **LOC:** 473 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.2681%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2399.32 | **LOC:** 4669 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (99.3316%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `error` **(Tests & Verification)** (Impact: 7.7)
  * `error` **(Tests & Verification)** (Impact: 6.1)
  * `error` **(Tests & Verification)** (Impact: 3.2)
  * `error` **(Tests & Verification)** (Impact: 2.7)
  * `error` **(Tests & Verification)** (Impact: 2.7)
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
- **Risk Profile:** Cognitive Load (90.6651%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1749.04 | **LOC:** 368 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.5593%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1743.06 | **LOC:** 3924 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (96.6706%), Tech Debt (99.5148%)
**Top Internal Functions/Classes:**
  * `respondWithJson` **(Defensive Guards)** (Impact: 6.4)
  * `generateMiddlewareResponse` **(Tests & Verification)** (Impact: 4.0)
  * `generateMiddlewareResponse` **(Tests & Verification)** (Impact: 4.0)
  * `pushOrderContext` **(Callbacks & Closures)** (Impact: 3.8)
  * `generateMiddlewareResponse` **(Tests & Verification)** (Impact: 3.8)
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
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1714.18 | **LOC:** 3072 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (95.7345%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createFixture` **(Compute Cores)** (Impact: 20.6)
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
- **Risk Profile:** Cognitive Load (87.4098%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1685.0 | **LOC:** 8843 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (20.812%), Tech Debt (93.255%)
**Top Internal Functions/Classes:**
  * `testDomRouter` **(Many-Argument Workhorses)** (Impact: 117.9)
  * `assertLocation` **(State Mutators)** (Impact: 12.7)
    * *Intent:* // Utility to assert location info based on the type of router
  * `setupTest` **(Many-Argument Workhorses)** (Impact: 9.7)
  * `Component` **(Tests & Verification)** (Impact: 7.0)
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
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1643.38 | **LOC:** 2959 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (99.0638%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `error` **(Callbacks & Closures)** (Impact: 34.7)
  * `error` **(Tests & Verification)** (Impact: 5.7)
  * `error` **(Tests & Verification)** (Impact: 4.0)
  * `log` **(Tests & Verification)** (Impact: 3.9)
  * `error` **(Tests & Verification)** (Impact: 3.9)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1630.97 | **LOC:** 232 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.3931%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1470.72 | **LOC:** 468 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.8149%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1372.22 | **LOC:** 261 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.7395%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1151.2 | **LOC:** 288 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.7949%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1011.4 | **LOC:** 2292 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.524%), Tech Debt (11.2045%)
**Top Internal Functions/Classes:**
  * `loader` **(Callbacks & Closures)** (Impact: 8.0)
  * `queryRoute` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `action` **(Tests & Verification)** (Impact: 4.9)
  * `setupFlexRouteTest` **(Interface Declarations)** (Impact: 4.9)
  * `loader` **(Tests & Verification)** (Impact: 4.0)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1007.04 | **LOC:** 2617 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.0329%), Tech Debt (95.0992%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 979.38 | **LOC:** 323 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (96.2995%), Tech Debt (13.3483%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 968.45 | **LOC:** 277 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.0398%), Tech Debt (0.0%)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-router/lib/rsc/server.rsc.ts` -> Churn: **68.97%** | Cog Load: 76.1524% | Debt: 34.248%
- `packages/react-router/lib/router/router.ts` -> Churn: **68.02%** | Cog Load: 62.2338% | Debt: 9.697%
- `packages/react-router-dev/vite/rsc/plugin.ts` -> Churn: **60.36%** | Cog Load: 77.6626% | Debt: 8.2024%
- `integration/client-data-test.ts` -> Churn: **53.26%** | Cog Load: 99.3723% | Debt: 10.3775%
- `integration/helpers/vite.ts` -> Churn: **52.54%** | Cog Load: 100.0% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `integration/rsc/rsc-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 22058.16
- `packages/react-router/lib/router/router.ts` -> **Matt Brophy** (81.8% isolated ownership) | Magnitude: 5361.48
- `integration/fetcher-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 3236.51
- `integration/passthrough-requests-test.ts` -> **Matt Brophy** (100.0% isolated ownership) | Magnitude: 1630.97
- `integration/rsc/rsc-nojs-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 1372.22

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
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

- `packages/react-router/lib/router/history.ts` -> **Severity: 5.326** (Embedded: 0.0678 * Error Risk: 78.5869%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 3.541** (Embedded: 0.0505 * Error Risk: 70.1118%)
- `packages/react-router/lib/router/instrumentation.ts` -> **Severity: 2.336** (Embedded: 0.0339 * Error Risk: 68.8885%)
- `packages/react-router/lib/server-runtime/urls.ts` -> **Severity: 1.905** (Embedded: 0.0214 * Error Risk: 89.2283%)
- `packages/react-router/lib/server-runtime/data.ts` -> **Severity: 1.673** (Embedded: 0.0262 * Error Risk: 63.8242%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/react-router/lib/router/history.ts` -> **Severity: 2275.838** (Blast Radius: 39.195 * Doc Risk: 58.0645%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 1724.148** (Blast Radius: 20.669 * Doc Risk: 83.4171%)
- `integration/helpers/express.ts` -> **Severity: 1433.3** (Blast Radius: 14.333 * Doc Risk: 100.0%)
- `packages/react-router/lib/router/instrumentation.ts` -> **Severity: 1160.1** (Blast Radius: 11.601 * Doc Risk: 100.0%)
- `packages/create-react-router/__tests__/github-mocks.ts` -> **Severity: 714.8** (Blast Radius: 7.148 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
