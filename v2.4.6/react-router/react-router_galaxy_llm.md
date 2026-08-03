# ARCHITECTURAL_BRIEF: react-router
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/react-router` |
| **Timestamp** | `2026-08-03T19:56:55.158667+00:00` |
| **Scan Duration** | `1.88s` |
| **Git Branch** | `main` |
| **Git Commit** | `201cd41be3e2fadf0fe851d9ac6c836458707ca3` |
| **Git Remote** | `https://github.com/remix-run/react-router.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 514 malicious artifacts.

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
| Total Artifacts | 1480 |
| Analyzed Artifacts (Scanned) | 800 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 680 |
| Total LOC | 27482 |
| Volatility Index | 0.031 |
| % Scanned of codebase = | 54.1% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8036 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2804 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5542 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 442 | 22576 | 55.2% |
| MARKDOWN | 88 | 0 | 11.0% |
| JAVASCRIPT | 67 | 1808 | 8.4% |
| JSON | 66 | 1371 | 8.2% |
| PLAINTEXT | 64 | 1 | 8.0% |
| CSS | 41 | 792 | 5.1% |
| HTML | 25 | 303 | 3.1% |
| SHELL | 5 | 119 | 0.6% |
| YAML | 2 | 512 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.256`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 399 | 49.9% |
| file_cluster_13 | 110 | 13.8% |
| file_cluster_4 | 68 | 8.5% |
| file_cluster_0 | 34 | 4.2% |
| file_cluster_2 | 27 | 3.4% |
| file_cluster_16 | 3 | 0.4% |
| file_cluster_17 | 3 | 0.4% |
| file_cluster_12 | 2 | 0.2% |
| file_cluster_11 | 1 | 0.1% |
| Unknown | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 151 | 18.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 680*

**Composition by Extension & Reason:**
- `.ts`: 204x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 159 LOC)
- `.md`: 206x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 126 LOC)
- `.tsx`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 71 LOC), 1x Excluded (Machine-Generated Source Code Signature: 73 LOC)
- `no_extension`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 8x Excluded (Static Asset Blob without Intent: 1476 LOC), 5x Excluded (Static Asset Blob without Intent: 1542 LOC), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 23x Excluded (Explicitly Denied Extension: '.ico')
- `.yml`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gz`: 3x Excluded (Explicitly Denied Extension: '.gz')
- `.patch`: 3x Excluded (Unsupported Extension: '.patch')
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 1x Excluded (Explicitly Denied Extension: '.tgz')
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 19.7 | 5.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 16.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.2 | 0.9 | 0.0 |
| API Exposure | 0.0 | 14.9 | 4.5 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 21.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 98.1 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 76.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 13.2 | 1.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 95.8 | 3.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.7 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/react-router-dev/vite/plugin.ts` (Hits: 64)
- `packages/react-router-dev/vite/route-chunks.ts` (Hits: 49)
- `integration/helpers/create-fixture.ts` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **express.ts** (`integration/helpers/express.ts`) — 17 inbound connections
2. **invariant.ts** (`packages/react-router-dev/invariant.ts`) — 7 inbound connections
3. **babel.ts** (`packages/react-router-dev/vite/babel.ts`) — 7 inbound connections
4. **contexts.ts** (`playground/middleware/app/contexts.ts`) — 6 inbound connections
5. **counter.tsx** (`playground/rsc-vite/src/counter.tsx`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **plugin.ts** (`packages/react-router-dev/vite/plugin.ts`) — 46 outbound dependencies
2. **index.ts** (`packages/react-router/index.ts`) — 39 outbound dependencies
3. **vite.ts** (`integration/helpers/vite.ts`) — 27 outbound dependencies
4. **plugin.ts** (`packages/react-router-dev/vite/rsc/plugin.ts`) — 23 outbound dependencies
5. **config.ts** (`packages/react-router-dev/config/config.ts`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `prerender` (@ `packages/react-router-dev/vite/plugins/prerender.ts`) -> Impact: **682.8** | LOC: 215
  * *Intent:* * Metadata flows through to postProcess and logFile hooks. * * If no requests are returned, prerendering is skipped. * * @example * ```ts * requests()...
- `reactRouterRSCVitePlugin` (@ `packages/react-router-dev/vite/rsc/plugin.ts`) -> Impact: **618.3** | LOC: 485
- `ReactRouterVitePlugin` (@ `packages/react-router-dev/vite/plugin.ts`) -> Impact: **587.2** | LOC: 624
- `hasChunkableExport` (@ `packages/react-router-dev/vite/route-chunks.ts`) -> Impact: **516.8** | LOC: 293
- `getEnvironmentOptionsResolvers` (@ `packages/react-router-dev/vite/plugin.ts`) -> Impact: **409.6** | LOC: 211
  * *Intent:* // This isn't honored by the SSR environment config (which seems
- `getExportDependencies` (@ `packages/react-router-dev/vite/route-chunks.ts`) -> Impact: **388.4** | LOC: 165
- `getContext` (@ `packages/create-react-router/index.ts`) -> Impact: **335.4** | LOC: 409
- `copyTemplateFromLocalFilePath` (@ `packages/create-react-router/copy-template.ts`) -> Impact: **296.0** | LOC: 320
- `onChange` (@ `packages/react-router-dev/config/config.ts`) -> Impact: **275.9** | LOC: 119
- `removeExports` (@ `packages/react-router-dev/vite/remove-exports.ts`) -> Impact: **217.6** | LOC: 151

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `prerender` (@ `packages/react-router-dev/vite/plugins/prerender.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* * Metadata flows through to postProcess and logFile hooks. * * If no requests are returned, prerendering is skipped. * * @example * ```ts * requests()...
- `render` (@ `packages/create-react-router/prompts-multi-select.ts`) -> **O(2^N) [Recursive]**
- `lazy` (@ `examples/lazy-loading-router-provider/src/App.tsx`) -> **O(2^N) [Recursive]**
  * *Intent:* // Single route in lazy file
- `Gallery` (@ `examples/modal-route-with-outlet/src/App.tsx`) -> **O(2^N) [Recursive]**
- `Gallery` (@ `examples/modal/src/App.tsx`) -> **O(2^N) [Recursive]**
- `reject` (@ `integration/helpers/create-fixture.ts`) -> **O(2^N) [Recursive]**
- `render` (@ `packages/create-react-router/prompts-select.ts`) -> **O(2^N) [Recursive]**
- `onChange` (@ `packages/react-router-dev/config/config.ts`) -> **O(2^N) [Recursive]**
- `hasChunkableExport` (@ `packages/react-router-dev/vite/route-chunks.ts`) -> **O(2^N) [Recursive]**
- `getExportDependencies` (@ `packages/react-router-dev/vite/route-chunks.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `ReactRouterVitePlugin` (@ `packages/react-router-dev/vite/plugin.ts`) -> DB Complexity: **117**
- `removeExports` (@ `packages/react-router-dev/vite/remove-exports.ts`) -> DB Complexity: **113**
- `flatRoutesUniversal` (@ `packages/react-router-fs-routes/flatRoutes.ts`) -> DB Complexity: **105**
- `getContext` (@ `packages/create-react-router/index.ts`) -> DB Complexity: **86**
- `getExportDependencies` (@ `packages/react-router-dev/vite/route-chunks.ts`) -> DB Complexity: **67**
- `createAppFixture` (@ `integration/helpers/create-fixture.ts`) -> DB Complexity: **66**
  * *Intent:* /** * @deprecated Use `integration/helpers/vite.ts`'s `test` instead * * This implementation sometimes runs a request handler in memory, forcing tests...
- `copyTemplateFromLocalFilePath` (@ `packages/create-react-router/copy-template.ts`) -> DB Complexity: **63**
- `createFixture` (@ `integration/helpers/create-fixture.ts`) -> DB Complexity: **58**
- `reactRouterRSCVitePlugin` (@ `packages/react-router-dev/vite/rsc/plugin.ts`) -> DB Complexity: **50**
- `render` (@ `packages/create-react-router/prompts-text.ts`) -> DB Complexity: **33**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 17 | 5186.63 | 1.33% | 0.0% |
| `scripts` | 18 | 600.65 | 54.62% | 42.84% |
| `packages/react-router-dev/vite` | 22 | 461.51 | 43.84% | 4.57% |
| `packages/create-react-router` | 16 | 400.81 | 54.27% | 5.78% |
| `integration/helpers` | 8 | 223.18 | 56.53% | 36.91% |
| `packages/react-router-dev/vite/static` | 2 | 215.54 | 84.68% | 0.0% |
| `packages/react-router-dev` | 14 | 213.68 | 8.45% | 8.99% |
| `examples/ssr-data-router` | 6 | 200.82 | 16.31% | 0.0% |
| `packages/react-router` | 15 | 162.83 | 3.71% | 0.65% |
| `examples/ssr` | 6 | 159.24 | 15.69% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `integration/rsc/utils.ts` -> **100.0%** Exposure
- `packages/react-router/__tests__/dom/components/LazyComponent.tsx` -> **100.0%** Exposure
- `packages/react-router/__tests__/dom/polyfills/drop-FormData-submitter.ts` -> **100.0%** Exposure
- `packages/react-router/__tests__/router/TestSequences/InitialLocationDefaultKey.ts` -> **100.0%** Exposure
- `packages/react-router/__tests__/router/TestSequences/InitialLocationHasKey.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `integration/helpers/create-fixture.ts` -> **100.0%** Exposure
- `integration/helpers/playwright-fixture.ts` -> **100.0%** Exposure
- `integration/helpers/vite.ts` -> **100.0%** Exposure
- `packages/create-react-router/__tests__/setupAfterEnv.ts` -> **100.0%** Exposure
- `packages/create-react-router/prompts-confirm.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `integration/helpers/vite.ts` -> **0** Orphaned Functions | **13** Duplicates
- `examples/view-transitions/src/main.tsx` -> **0** Orphaned Functions | **11** Duplicates
- `integration/helpers/playwright-fixture.ts` -> **7** Orphaned Functions | **2** Duplicates
- `integration/rsc/utils.ts` -> **0** Orphaned Functions | **8** Duplicates
- `scripts/bench/passthrough-requests.bench.mjs` -> **1** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/react-router/__tests__/setup.ts`** -> AI Confidence: **99.32%**
2. **`packages/create-react-router/copy-template.ts`** -> AI Confidence: **99.31%**
3. **`packages/create-react-router/index.ts`** -> AI Confidence: **99.31%**
4. **`packages/react-router-dev/config/config.ts`** -> AI Confidence: **99.31%**
5. **`packages/react-router-dev/vite/rsc/plugin.ts`** -> AI Confidence: **99.31%**
6. **`scripts/docs.ts`** -> AI Confidence: **99.31%**
7. **`jest/jest.config.shared.js`** -> AI Confidence: **99.29%**
8. **`packages/react-router-dev/module-sync-enabled/false.cjs`** -> AI Confidence: **99.29%**
9. **`packages/react-router-serve/bin.js`** -> AI Confidence: **99.29%**
10. **`packages/react-router/node-main-dom-export.js`** -> AI Confidence: **99.29%**
11. **`packages/react-router/node-main.js`** -> AI Confidence: **99.29%**
12. **`scripts/finish-stable-release.sh`** -> AI Confidence: **99.29%**
13. **`scripts/start-prerelease.sh`** -> AI Confidence: **99.29%**
14. **`integration/helpers/create-fixture.ts`** -> AI Confidence: **99.24%**
15. **`packages/create-react-router/utils.ts`** -> AI Confidence: **99.24%**
16. **`packages/react-router-dev/cli/commands.ts`** -> AI Confidence: **99.24%**
17. **`packages/react-router-dev/vite/plugin.ts`** -> AI Confidence: **99.24%**
18. **`packages/react-router-dev/vite/styles.ts`** -> AI Confidence: **99.24%**
19. **`packages/react-router/__tests__/server-runtime/utils.ts`** -> AI Confidence: **99.24%**
20. **`packages/react-router-dev/vite/rsc/virtual-route-modules.ts`** -> AI Confidence: **99.23%**
21. **`eslint.config.ts`** -> AI Confidence: **99.18%**
22. **`packages/react-router-dev/invariant.ts`** -> AI Confidence: **99.17%**
23. **`packages/react-router-dev/bin.js`** -> AI Confidence: **99.17%**
24. **`packages/react-router-dev/vite/cloudflare-dev-proxy.ts`** -> AI Confidence: **99.15%**
25. **`scripts/remove-prerelease-changelogs.mjs`** -> AI Confidence: **99.15%**
26. **`packages/create-react-router/prompts-prompt-base.ts`** -> AI Confidence: **99.13%**
27. **`packages/react-router-dev/cli/run.ts`** -> AI Confidence: **99.13%**
28. **`packages/react-router-dev/vite/route-chunks.ts`** -> AI Confidence: **99.13%**
29. **`packages/react-router-fs-routes/flatRoutes.ts`** -> AI Confidence: **99.13%**
30. **`packages/create-react-router/prompts-confirm.ts`** -> AI Confidence: **99.09%**
31. **`packages/create-react-router/prompts-select.ts`** -> AI Confidence: **99.09%**
32. **`packages/create-react-router/prompts-text.ts`** -> AI Confidence: **99.09%**
33. **`packages/react-router-dev/vite/plugins/warn-on-client-source-maps.ts`** -> AI Confidence: **99.09%**
34. **`packages/react-router-dev/vite/remove-exports.ts`** -> AI Confidence: **99.09%**
35. **`packages/react-router/__tests__/utils/MemoryNavigate.tsx`** -> AI Confidence: **99.09%**
36. **`packages/react-router/index.ts`** -> AI Confidence: **99.09%**
37. **`integration/helpers/express.ts`** -> AI Confidence: **99.08%**
38. **`integration/helpers/vite.ts`** -> AI Confidence: **99.08%**
39. **`packages/react-router/index-react-server.ts`** -> AI Confidence: **99.08%**
40. **`playground/rsc-vite/src/routes.ts`** -> AI Confidence: **99.08%**
41. **`integration/helpers/fixtures.ts`** -> AI Confidence: **99.07%**
42. **`examples/modal-data-router/src/App.tsx`** -> AI Confidence: **99.06%**
43. **`examples/modal-route-with-outlet/src/images.ts`** -> AI Confidence: **99.06%**
44. **`examples/modal/src/App.tsx`** -> AI Confidence: **99.06%**
45. **`examples/modal/src/images.ts`** -> AI Confidence: **99.06%**
46. **`examples/ssr/src/App.tsx`** -> AI Confidence: **99.06%**
47. **`integration/playwright.config.ts`** -> AI Confidence: **99.06%**
48. **`packages/create-react-router/__tests__/setupAfterEnv.ts`** -> AI Confidence: **99.06%**
49. **`packages/create-react-router/prompts-multi-select.ts`** -> AI Confidence: **99.06%**
50. **`packages/react-router-dev/__tests__/fixtures/basic/app/routes.ts`** -> AI Confidence: **99.06%**
51. **`packages/react-router-dev/__tests__/setupAfterEnv.ts`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `examples/data-router/src/app.tsx` -> **100.0%** Exposure
- `examples/view-transitions/src/main.tsx` -> **100.0%** Exposure
- `integration/helpers/create-fixture.ts` -> **100.0%** Exposure
- `integration/helpers/playwright-fixture.ts` -> **100.0%** Exposure
- `packages/create-react-router/copy-template.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `packages/react-router-dev/cli/commands.ts` -> **100.0%** Exposure
- `examples/ssr-data-router/server.js` -> **100.0%** Exposure
- `examples/ssr/server.js` -> **100.0%** Exposure
- `integration/helpers/cleanup.mjs` -> **100.0%** Exposure
- `scripts/docs.ts` -> **1.455%** Exposure
### Algorithmic DoS Exposure
- `examples/auth-router-provider/vite.config.ts` -> **100.0%** Exposure
- `examples/auth/src/App.tsx` -> **100.0%** Exposure
- `examples/auth/vite.config.ts` -> **100.0%** Exposure
- `examples/basic-data-router/vite.config.ts` -> **100.0%** Exposure
- `examples/basic/src/App.tsx` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `898` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `integration/helpers/create-fixture.ts` (TYPESCRIPT) -> Cumulative Risk: **906.05**
- **Archetype:** `file_cluster_4` (Distance: 12.686 IQR)
- **Magnitude:** 85.34 | **LOC:** 550 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `createFixture` (Impact: 105.3), `reject` (Impact: 96.2), `createAppFixture` (Impact: 94.1)

### 2. `packages/react-router-dev/vite/cloudflare-dev-proxy.ts` (TYPESCRIPT) -> Cumulative Risk: **873.06**
- **Archetype:** `file_cluster_4` (Distance: 12.393 IQR)
- **Magnitude:** 22.63 | **LOC:** 160 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `configureServer` (Impact: 32.1), `config` (Impact: 29.5), `configEnvironment` (Impact: 21.4)

### 3. `packages/react-router/__tests__/router/utils/data-router-setup.ts` (TYPESCRIPT) -> Cumulative Risk: **862.1**
- **Archetype:** `file_cluster_4` (Distance: 11.704 IQR)
- **Magnitude:** 64.2 | **LOC:** 763 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `enhanceRoutes` (Impact: 153.6), `fetch` (Impact: 97.2), `addHelpers` (Impact: 58.9)

### 4. `packages/react-router-dev/vite/plugin.ts` (TYPESCRIPT) -> Cumulative Risk: **861.55**
- **Archetype:** `file_cluster_4` (Distance: 13.595 IQR)
- **Magnitude:** 214.13 | **LOC:** 4372 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 34.6%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `ReactRouterVitePlugin` (Impact: 587.2), `getEnvironmentOptionsResolvers` (Impact: 409.6), `getAddressableRoutes` (Impact: 34.1)

### 5. `packages/react-router-node/sessions/fileStorage.ts` (TYPESCRIPT) -> Cumulative Risk: **857.63**
- **Archetype:** `file_cluster_4` (Distance: 12.191 IQR)
- **Magnitude:** 18.04 | **LOC:** 126 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `readData` (Impact: 32.5), `createData` (Impact: 22.0), `deleteData` (Impact: 16.4)

### 6. `integration/helpers/playwright-fixture.ts` (TYPESCRIPT) -> Cumulative Risk: **854.99**
- **Archetype:** `file_cluster_4` (Distance: 13.375 IQR)
- **Magnitude:** 66.4 | **LOC:** 385 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `action` (Impact: 55.7), `goto` (Impact: 49.6), `getPageContent` (Impact: 25.1)

### 7. `packages/create-react-router/prompts-text.ts` (TYPESCRIPT) -> Cumulative Risk: **838.43**
- **Archetype:** `file_cluster_4` (Distance: 14.33 IQR)
- **Magnitude:** 68.1 | **LOC:** 285 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `render` (Impact: 64.8), `value` (Impact: 8.6), `deleteForward` (Impact: 7.9)

### 8. `packages/react-router-node/stream.ts` (TYPESCRIPT) -> Cumulative Risk: **831.95**
- **Archetype:** `file_cluster_4` (Distance: 14.092 IQR)
- **Magnitude:** 37.68 | **LOC:** 179 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `enqueue` (Impact: 63.6), `writeReadableStreamToWritable` (Impact: 25.3), `constructor` (Impact: 24.6)

### 9. `packages/react-router-dev/config/config.ts` (TYPESCRIPT) -> Cumulative Risk: **818.37**
- **Archetype:** `file_cluster_4` (Distance: 13.313 IQR)
- **Magnitude:** 106.05 | **LOC:** 1198 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `onChange` (Impact: 275.9), `mergeReactRouterConfig` (Impact: 74.8), `deepFreeze` (Impact: 61.0)

### 10. `packages/create-react-router/copy-template.ts` (TYPESCRIPT) -> Cumulative Risk: **807.56**
- **Archetype:** `file_cluster_4` (Distance: 11.674 IQR)
- **Magnitude:** 53.22 | **LOC:** 563 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `copyTemplateFromLocalFilePath` (Impact: 296.0), `isLocalFilePath` (Impact: 15.6), `log` (Impact: 13.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/plugin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.595 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.136 IQR)
- **Top Global Matches:** file_cluster_4: 13.595, file_cluster_17: 13.921, file_cluster_13: 13.954
- **Magnitude:** 214.13 | **LOC:** 4372 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 34.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 117
- **Risk Profile:** Cognitive Load (98.4652%), Tech Debt (8.5906%)
**Top Internal Functions/Classes:**
  * `ReactRouterVitePlugin` (Impact: 587.2 | O(N^5) | DB: 117)
  * `getEnvironmentOptionsResolvers` (Impact: 409.6 | O(N^6) | DB: 32)
    * *Intent:* // This isn't honored by the SSR environment config (which seems
  * `getAddressableRoutes` (Impact: 34.1 | O(N^3) | DB: 14)
  * `prerenderRoute` (Impact: 27.4 | O(N^2) | DB: 12)
  * `detectRouteChunksIfEnabled` (Impact: 24.1 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 367`, `args: 105`, `func_start: 97`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 455`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `io: 64`, `api: 26`, `concurrency: 411`, `import: 52`
* *Defense:* `safety: 102`, `doc: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` kebabCase, vite, exportName, optimize-deps-entries, react-router, $routeFileName, babel, $getRouteChunkModuleId(
            chunkBasePath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/ssr-data-router/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.44 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.484 IQR)
- **Top Global Matches:** file_cluster_4: 12.44, file_cluster_13: 12.925, file_cluster_8: 13.266
- **Magnitude:** 153.9 | **LOC:** 80 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (73.8268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createServer` (Impact: 81.0 | O(2^N) | DB: 7)
  * `resolve` (Impact: 3.6 | O(2^N) | DB: 3)
  * `createServer` (Impact: 2.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 26`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `concurrency: 40`, `import: 6`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` promises, compression, vite, express, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/remove-prerelease-changelogs.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.013 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.696 IQR)
- **Top Global Matches:** file_cluster_4: 13.013, file_cluster_13: 13.272, file_cluster_8: 13.705
- **Magnitude:** 147.12 | **LOC:** 124 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (49.7425%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `removePreReleaseSectionFromMarkdown` (Impact: 46.9 | O(N^3) | DB: 3)
  * `removePreReleaseChangelogs` (Impact: 17.8 | O(N^3) | DB: 20)
  * `isPrereleaseMode` (Impact: 5.6 | O(N^1) | DB: 7)
  * `main` (Impact: 4.4 | O(N^1))
  * `isPrereleaseVersion` (Impact: 3.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 36`, `args: 8`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`
* *Architecture:* `io: 11`, `concurrency: 33`, `import: 9`
* *Defense:* `safety: 8`, `doc: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` remark-parse, node:path, node:fs, unist, unified, remark-gfm, remark-stringify, get-packages...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/publish.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.203 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.092 IQR)
- **Top Global Matches:** file_cluster_4: 12.203, file_cluster_13: 12.482, file_cluster_8: 12.644
- **Magnitude:** 128.86 | **LOC:** 155 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (46.8622%), Tech Debt (93.0383%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 48.0 | O(2^N) | DB: 9)
  * `publishBuild` (Impact: 17.2 | O(N^1) | DB: 8)
  * `invariant` (Impact: 3.6 | O(N^1))
    * *Intent:* /**
  * `ensureBuildVersion` (Impact: 2.1 | O(N^1) | DB: 5)
    * *Intent:* /** * @returns {string} */
  * `getTaggedVersion` (Impact: 1.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 24`, `args: 6`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 27`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `concurrency: 25`, `import: 4`
* *Defense:* `safety: 6`, `doc: 14`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` path, child_process, jsonfile, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/static/refresh-utils.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.061 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.311 IQR)
- **Top Global Matches:** file_cluster_4: 12.061, file_cluster_17: 12.448, file_cluster_11: 12.533
- **Magnitude:** 123.16 | **LOC:** 171 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (92.4648%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateRefreshBoundaryAndEnqueueUpdate` (Impact: 24.5 | O(N^1) | DB: 5)
  * `predicateOnExport` (Impact: 12.6 | O(N^1) | DB: 2)
  * `registerExportsForReactRefresh` (Impact: 9.3 | O(N^1) | DB: 2)
    * *Intent:* // Taken from https://github.com/pmmmwh/react-refresh-webpack-plugin/blob/main/lib/runtime/RefreshUt...
  * `debounce` (Impact: 2.1 | O(N^1) | DB: 1)
    * *Intent:* // adapted from https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/src/refr...
  * `__hmr_import` (Impact: 1.9 | O(N^1))
    * *Intent:* // Hides vite-ignored dynamic import so that Vite can skip analysis if no other // dynamic import is...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 38`, `args: 13`, `func_start: 7`
* *Risk/State:* `state_mutation: 40`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 19`, `import: 1`
* *Defense:* `safety: 11`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/multi-app/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.331 IQR)
- **Local Micro-Species:** `Cluster 5: I/O, UI & Routing Configuration` (Drift: 5.149 IQR)
- **Top Global Matches:** file_cluster_4: 12.331, file_cluster_13: 12.828, file_cluster_8: 13.183
- **Magnitude:** 120.6 | **LOC:** 67 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (65.9839%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createServer` (Impact: 62.6 | O(2^N) | DB: 18)
  * `createServer` (Impact: 2.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 24`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `concurrency: 31`, `import: 5`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` promises, compression, vite, express, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/route-chunks.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.999 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.784 IQR)
- **Top Global Matches:** file_cluster_17: 13.999, file_cluster_11: 14.45, file_cluster_0: 14.584
- **Magnitude:** 120.46 | **LOC:** 1007 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (76.4263%), Tech Debt (17.4908%)
**Top Internal Functions/Classes:**
  * `hasChunkableExport` (Impact: 516.8 | O(2^N) | DB: 17)
  * `getExportDependencies` (Impact: 388.4 | O(2^N) | DB: 67)
  * `getIdentifiersForPatternPath` (Impact: 36.0 | O(N^2) | DB: 9)
  * `assertNodePathIsStatement` (Impact: 10.9 | O(N^1) | DB: 24)
  * `assertNodePathIsVariableDeclarator` (Impact: 10.9 | O(N^1) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 119`, `args: 73`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 144`, `dead_code: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 49`, `api: 20`, `import: 4`
* *Defense:* `safety: 24`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001252
  * `Imports (Out-Degree: 3):` generator, babel, invariant, cache, module
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/ssr/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.884 IQR)
- **Local Micro-Species:** `Cluster 5: I/O, UI & Routing Configuration` (Drift: 5.663 IQR)
- **Top Global Matches:** file_cluster_4: 11.884, file_cluster_13: 12.334, file_cluster_8: 12.683
- **Magnitude:** 112.34 | **LOC:** 72 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (70.1448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createServer` (Impact: 50.6 | O(2^N) | DB: 6)
  * `resolve` (Impact: 3.6 | O(2^N) | DB: 3)
  * `createServer` (Impact: 2.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 23`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 21`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `concurrency: 34`, `import: 6`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` promises, compression, vite, express, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/config/config.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.313 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.974 IQR)
- **Top Global Matches:** file_cluster_4: 13.313, file_cluster_13: 13.495, file_cluster_11: 13.603
- **Magnitude:** 106.05 | **LOC:** 1198 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (46.5246%), Tech Debt (16.1536%)
**Top Internal Functions/Classes:**
  * `onChange` (Impact: 275.9 | O(2^N) | DB: 27)
  * `mergeReactRouterConfig` (Impact: 74.8 | O(N^4) | DB: 2)
    * *Intent:* /** * A function that is called after the full React Router build is complete.
  * `deepFreeze` (Impact: 61.0 | O(2^N) | DB: 2)
    * *Intent:* /**
  * `presets` (Impact: 61.0 | O(2^N) | DB: 1)
  * `getStaticPaths` (Impact: 56.4 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 169`, `args: 61`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 259`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 23`, `api: 23`, `concurrency: 136`, `import: 19`
* *Defense:* `safety: 81`, `doc: 31`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` routes, express, vite, node:fs, express, pathe, isEqual, react-router...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/notes/src/notes.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.136 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.883 IQR)
- **Top Global Matches:** file_cluster_4: 13.136, file_cluster_17: 14.092, file_cluster_13: 14.221
- **Magnitude:** 104.54 | **LOC:** 38 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getNote` (Impact: 6.2 | O(N^1) | DB: 2)
  * `deleteNote` (Impact: 4.5 | O(N^1) | DB: 3)
  * `getNotes` (Impact: 4.2 | O(N^1) | DB: 1)
  * `set` (Impact: 1.9 | O(N^1))
  * `createNote` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 27`, `args: 7`, `func_start: 5`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 7`, `concurrency: 55`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` localforage
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.735 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.055 IQR)
- **Top Global Matches:** file_cluster_4: 12.735, file_cluster_13: 13.24, file_cluster_8: 13.615
- **Magnitude:** 97.68 | **LOC:** 94 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.9997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fileExists` (Impact: 6.4 | O(N^1))
  * `ensureCleanWorkingDirectory` (Impact: 5.6 | O(N^1) | DB: 2)
    * *Intent:* /** * @param {string} packageName * @returns {Promise<string | undefined>} */
  * `updateExamplesPackageConfig` (Impact: 3.9 | O(N^1) | DB: 5)
  * `invariant` (Impact: 3.6 | O(N^1))
  * `getPackageVersion` (Impact: 2.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 21`, `args: 8`, `func_start: 10`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 56`, `import: 5`
* *Defense:* `safety: 3`, `doc: 22`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fs, constants, jsonfile, path, child_process, type-fest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 95.72 | **LOC:** 4786 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/static/rsc-refresh-utils.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.256 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.717 IQR)
- **Top Global Matches:** file_cluster_4: 10.256, file_cluster_8: 10.486, file_cluster_13: 10.825
- **Magnitude:** 92.38 | **LOC:** 127 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (76.8884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateRefreshBoundaryAndEnqueueUpdate` (Impact: 24.5 | O(N^1) | DB: 4)
  * `predicateOnExport` (Impact: 12.6 | O(N^1))
  * `registerExportsForReactRefresh` (Impact: 9.3 | O(N^1))
    * *Intent:* // Taken from https://github.com/pmmmwh/react-refresh-webpack-plugin/blob/main/lib/runtime/RefreshUt...
  * `debounce` (Impact: 2.1 | O(N^1) | DB: 1)
    * *Intent:* // adapted from https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/src/refr...
  * `__hmr_import` (Impact: 1.9 | O(N^1))
    * *Intent:* // Hides vite-ignored dynamic import so that Vite can skip analysis if no other // dynamic import is...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 25`, `args: 11`, `func_start: 8`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 19`, `import: 1`
* *Defense:* `safety: 5`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/bin.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.18 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.655 IQR)
- **Top Global Matches:** file_cluster_13: 14.18, file_cluster_8: 14.665, file_cluster_17: 14.701
- **Magnitude:** 90.68 | **LOC:** 16 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` arg, index
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/helpers/create-fixture.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.686 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.146 IQR)
- **Top Global Matches:** file_cluster_4: 12.686, file_cluster_13: 13.237, file_cluster_11: 13.347
- **Magnitude:** 85.34 | **LOC:** 550 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (98.4954%), Tech Debt (18.6441%)
**Top Internal Functions/Classes:**
  * `createFixture` (Impact: 105.3 | O(N^3) | DB: 58)
  * `reject` (Impact: 96.2 | O(2^N) | DB: 2)
  * `createAppFixture` (Impact: 94.1 | O(N^4) | DB: 66)
    * *Intent:* /** * @deprecated Use `integration/helpers/vite.ts`'s `test` instead * * This implementation sometim...
  * `reactRouterBuild` (Impact: 29.1 | O(N^1) | DB: 4)
  * `reject` (Impact: 12.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 118`, `args: 50`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 194`, `duplicate_logic: 2`
* *Architecture:* `io: 34`, `api: 14`, `concurrency: 287`, `import: 17`
* *Defense:* `safety: 18`, `doc: 3`, `immutability_locks: 8`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` promises, node:stream, express, node, node:path, node:fs, express, vite.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-fs-routes/flatRoutes.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.43 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.156 IQR)
- **Top Global Matches:** file_cluster_8: 12.43, file_cluster_13: 12.517, file_cluster_17: 12.55
- **Magnitude:** 84.3 | **LOC:** 565 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (72.1741%), Tech Debt (18.9727%)
**Top Internal Functions/Classes:**
  * `flatRoutesUniversal` (Impact: 214.3 | O(N^3) | DB: 105)
  * `getRouteSegments` (Impact: 174.5 | O(N^3) | DB: 14)
  * `flatRoutes` (Impact: 32.8 | O(N^2) | DB: 22)
  * `findRouteModuleForFolder` (Impact: 28.3 | O(N^2) | DB: 12)
  * `createRoutePath` (Impact: 23.9 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 61`, `args: 27`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 269`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 34`, `api: 15`, `import: 6`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001252
  * `Imports (Out-Degree: 0):` minimatch, node:path, node:fs, manifest, normalizeSlashes
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-router-dev/vite/rsc/plugin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.074 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.108 IQR)
- **Top Global Matches:** file_cluster_13: 12.074, file_cluster_4: 12.079, file_cluster_8: 12.155
- **Magnitude:** 80.38 | **LOC:** 982 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(N^6) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (59.4625%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `reactRouterRSCVitePlugin` (Impact: 618.3 | O(N^6) | DB: 50)
  * `getPrerenderConcurrencyConfig` (Impact: 9.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 114`, `args: 37`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 93`
* *Architecture:* `io: 13`, `api: 4`, `concurrency: 67`, `import: 28`
* *Defense:* `safety: 27`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` fs, prerender, plugin, vite, optimize-deps-entries, es-module-lexer, virtual-module, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/plugins/prerender.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.07 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.83 IQR)
- **Top Global Matches:** file_cluster_2: 11.07, file_cluster_4: 11.093, file_cluster_8: 11.097
- **Magnitude:** 78.42 | **LOC:** 483 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (34.6599%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prerender` (Impact: 682.8 | O(2^N) | DB: 25)
    * *Intent:* * Metadata flows through to postProcess and logFile hooks. * * If no requests are returned, prerende...
  * `defaultHandleError` (Impact: 9.3 | O(N^1))
  * `startPreviewServer` (Impact: 8.8 | O(N^2))
  * `defaultPostProcess` (Impact: 7.0 | O(N^1) | DB: 3)
  * `getResolvedUrl` (Impact: 6.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 73`, `args: 25`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `io: 12`, `api: 6`, `concurrency: 49`, `import: 5`
* *Defense:* `safety: 28`, `doc: 17`, `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002503
  * `Imports (Out-Degree: 0):` promises, node:path, p-map, vite
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/create-react-router/prompts-text.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.33 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.239 IQR)
- **Top Global Matches:** file_cluster_4: 14.33, file_cluster_8: 14.543, file_cluster_13: 14.616
- **Magnitude:** 68.1 | **LOC:** 285 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (83.6903%), Tech Debt (38.1338%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 64.8 | O(2^N) | DB: 33)
  * `value` (Impact: 8.6 | O(N^1) | DB: 9)
  * `deleteForward` (Impact: 7.9 | O(N^1) | DB: 19)
  * `constructor` (Impact: 7.7 | O(N^1) | DB: 16)
  * `delete` (Impact: 6.5 | O(N^1) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 31`, `args: 29`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 491`, `duplicate_logic: 2`
* *Architecture:* `api: 14`, `concurrency: 25`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.463
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001669
  * `Imports (Out-Degree: 1):` prompts-prompt-base, utils, sisteransi
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `integration/helpers/playwright-fixture.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.375 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.075 IQR)
- **Top Global Matches:** file_cluster_4: 13.375, file_cluster_13: 14.099, file_cluster_11: 14.25
- **Magnitude:** 66.4 | **LOC:** 385 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (52.5%), Tech Debt (89.4089%)
**Top Internal Functions/Classes:**
  * `action` (Impact: 55.7 | O(2^N) | DB: 16)
    * *Intent:* /** * Keeps the fixture running for as many seconds as you want so you can go * poke around in the b...
  * `goto` (Impact: 49.6 | O(2^N) | DB: 4)
    * *Intent:* /**
  * `getPageContent` (Impact: 25.1 | O(N^2) | DB: 1)
  * `collectResponses` (Impact: 12.6 | O(N^2) | DB: 3)
    * *Intent:* /**
  * `clickElement` (Impact: 6.3 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 82`, `args: 44`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 154`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 310`, `import: 6`
* *Defense:* `safety: 7`, `doc: 22`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-fixture.js, prettier, cheerio, test, node:child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/utils/data-router-setup.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.704 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.463 IQR)
- **Top Global Matches:** file_cluster_4: 11.704, file_cluster_11: 11.943, file_cluster_17: 11.997
- **Magnitude:** 64.2 | **LOC:** 763 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (84.9131%), Tech Debt (40.3811%)
**Top Internal Functions/Classes:**
  * `enhanceRoutes` (Impact: 153.6 | O(2^N) | DB: 17)
  * `fetch` (Impact: 97.2 | O(2^N) | DB: 16)
  * `addHelpers` (Impact: 58.9 | O(2^N) | DB: 7)
  * `revalidate` (Impact: 49.6 | O(2^N) | DB: 12)
  * `fetchers` (Impact: 21.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 86`, `args: 57`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 106`, `dead_code: 1`, `planned_debt: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 23`, `api: 13`, `concurrency: 76`, `import: 8`
* *Defense:* `safety: 15`, `test: 2`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils, utils, router, history
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/docs.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.228 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.015 IQR)
- **Top Global Matches:** file_cluster_4: 12.228, file_cluster_17: 12.264, file_cluster_13: 12.505
- **Magnitude:** 63.78 | **LOC:** 769 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^3) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (63.3807%), Tech Debt (27.0019%)
**Top Internal Functions/Classes:**
  * `generateMarkdownForComment` (Impact: 134.3 | O(N^3) | DB: 11)
  * `simplifyComment` (Impact: 105.5 | O(N^3) | DB: 23)
  * `getSignature` (Impact: 32.1 | O(N^2) | DB: 6)
  * `generateMarkdownDocs` (Impact: 30.5 | O(N^2) | DB: 2)
  * `processTypedocModule` (Impact: 25.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 106`, `args: 55`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 150`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 22`, `api: 10`, `concurrency: 56`, `import: 8`
* *Defense:* `safety: 21`, `doc: 12`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typedoc, prettier, node:util, node:path, dox, node:fs, fast-glob, typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/create-react-router/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.684 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.32 IQR)
- **Top Global Matches:** file_cluster_4: 11.684, file_cluster_8: 12.069, file_cluster_13: 12.123
- **Magnitude:** 59.46 | **LOC:** 706 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 86
- **Risk Profile:** Cognitive Load (96.6382%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getContext` (Impact: 335.4 | O(N^4) | DB: 86)
  * `createReactRouter` (Impact: 15.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 57`, `args: 42`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 93`
* *Architecture:* `io: 21`, `api: 2`, `concurrency: 140`, `import: 15`
* *Defense:* `safety: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` promises, arg, sort-package-json, copy-template, node:path, node:fs, semver, package.json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 59.34 | **LOC:** 2967 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/react-router-dev/vite/plugins/validate-plugin-order.ts` (TYPESCRIPT) | Magnitude: 3.57 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 13, structural_boundaries: 7, branch: 6
- `playground/split-route-modules-spa/react-router.config.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 1, safety: 1
- `playground/middleware/react-router.config.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 1, safety: 1
- `playground/split-route-modules-spa/app/routes.ts` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 4, func_start: 4, indent_spaces: 4
- `playground/split-route-modules/app/routes.ts` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 4, func_start: 4, indent_spaces: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/data-router/src/todos.ts` (TYPESCRIPT) | Magnitude: 3.59 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 13, args: 12, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/delete-nightly-tags.sh` (SHELL) | Magnitude: 3.87 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 24, debug_prints: 14, branch: 9, structural_boundaries: 9
- `scripts/delete-pre-tags.sh` (SHELL) | Magnitude: 2.09 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, io: 9, debug_prints: 9, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `playground/rsc-vite/src/routes/redirect.ts` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, branch: 1, args: 1
- `packages/react-router-dev/vite/rsc/plugin.ts` (TYPESCRIPT) | Magnitude: 80.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 548, branch: 129, structural_boundaries: 114, state_mutation: 93
- `examples/ssr-data-router/src/lazy.tsx` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, concurrency: 5, args: 4
- `packages/react-router/__tests__/router/TestSequences/InitialLocationDefaultKey.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, branch: 2, args: 2, func_start: 2
- `packages/create-react-router/__tests__/msw-register.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, args: 1, closures: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/react-router/__tests__/router/utils/custom-matchers.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, generics: 7, branch: 6
- `packages/create-react-router/prompt.ts` (TYPESCRIPT) | Magnitude: 6.85 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 80, generics: 62, state_mutation: 34
- `packages/react-router-dev/vite/cache.ts` (TYPESCRIPT) | Magnitude: 2.91 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 12, structural_boundaries: 8, generics: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/react-router-dev/vite/remove-exports.ts` (TYPESCRIPT) | Magnitude: 43.1 | Delta: **0.188 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 170, branch: 65, state_mutation: 51, structural_boundaries: 45
- `scripts/find-release-from-changeset.js` (JAVASCRIPT) | Magnitude: 19.44 | Delta: **0.255 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 9, doc: 7, structural_boundaries: 6
- `packages/react-router-dev/vite/route-chunks.ts` (TYPESCRIPT) | Magnitude: 120.46 | Delta: **0.451 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 453, state_mutation: 144, structural_boundaries: 119, branch: 112

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/notes/src/main.jsx` (JAVASCRIPT) | Magnitude: 14.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, ui_framework: 3, import: 3, indent_spaces: 3
- `examples/multi-app/home/main.jsx` (JAVASCRIPT) | Magnitude: 15.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, ui_framework: 4, import: 4
- `examples/multi-app/inbox/main.jsx` (JAVASCRIPT) | Magnitude: 15.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, ui_framework: 4, import: 4
- `packages/react-router-dev/vite/plugins/prerender.ts` (TYPESCRIPT) | Magnitude: 78.42 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 276, structural_boundaries: 73, branch: 59, concurrency: 49
- `examples/modal/src/App.tsx` (TYPESCRIPT) | Magnitude: 15.74 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 267, state_mutation: 40, ui_framework: 33, branch: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/react-router/__tests__/utils/waitForRedirect.tsx` (TYPESCRIPT) | Magnitude: 0.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, branch: 1
- `packages/react-router-dev/config/defaults/entry.server.node.tsx` (TYPESCRIPT) | Magnitude: 6.78 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, concurrency: 18, structural_boundaries: 15, args: 11
- `packages/create-react-router/__tests__/msw.ts` (TYPESCRIPT) | Magnitude: 3.17 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 18, io: 15, concurrency: 12
- `packages/react-router-node/server.ts` (TYPESCRIPT) | Magnitude: 2.46 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 18, concurrency: 14, generics: 6
- `examples/search-params/src/App.tsx` (TYPESCRIPT) | Magnitude: 9.07 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 102, state_mutation: 20, concurrency: 18, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `prettier.config.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `playground/rsc-vite-7-framework/app/routes/client-loader-hydrate/route.tsx` (TYPESCRIPT) | Magnitude: 1.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, args: 4, import: 4
- `examples/multi-app/home/App.jsx` (JAVASCRIPT) | Magnitude: 15.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, ui_framework: 12, structural_boundaries: 8, args: 4
- `playground/rsc-vite/src/routes/home/home.client.tsx` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 20, args: 7, api: 7
- `playground/split-route-modules/app/routes/splittable.tsx` (TYPESCRIPT) | Magnitude: 1.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, args: 5, func_start: 4
- `playground/rsc-vite-framework/app/routes/client-loader-hydrate/route.tsx` (TYPESCRIPT) | Magnitude: 1.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, args: 4, import: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-router-dev/vite/rsc/plugin.ts` -> Churn: **74.88%** | Cog Load: 59.4625% | Debt: 0.0%
- `packages/react-router-dev/vite/plugin.ts` -> Churn: **73.27%** | Cog Load: 98.4652% | Debt: 8.5906%
- `integration/helpers/vite.ts` -> Churn: **59.65%** | Cog Load: 100.0% | Debt: 99.9998%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/react-router-dev/vite/route-chunks.ts` -> **Matt Brophy** (100.0% isolated ownership) | Magnitude: 120.46
- `packages/react-router-dev/vite/static/rsc-refresh-utils.mjs` -> **Mark Dalgleish** (100.0% isolated ownership) | Magnitude: 92.38
- `packages/react-router-fs-routes/flatRoutes.ts` -> **Fróði Karlsson** (100.0% isolated ownership) | Magnitude: 84.3
- `integration/helpers/playwright-fixture.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 66.4
- `packages/react-router/__tests__/router/utils/data-router-setup.ts` -> **Matt Brophy** (100.0% isolated ownership) | Magnitude: 64.2

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react-router-dev/__tests__/utils/cli.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/create-react-router/prompts-prompt-base.ts` -> **Severity: 0.497** (Embedded: 0.005 * Error Risk: 99.2492%)
- `packages/create-react-router/prompts-select.ts` -> **Severity: 0.281** (Embedded: 0.0028 * Error Risk: 99.9544%)
- `packages/react-router-dev/vite/profiler.ts` -> **Severity: 0.242** (Embedded: 0.0033 * Error Risk: 72.3979%)
- `packages/react-router-dev/invariant.ts` -> **Severity: 0.237** (Embedded: 0.0078 * Error Risk: 30.2941%)
- `packages/react-router-dev/vite/remove-exports.ts` -> **Severity: 0.223** (Embedded: 0.0028 * Error Risk: 79.1936%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `integration/helpers/express.ts` -> **Severity: 1694.7** (Blast Radius: 16.947 * Doc Risk: 100.0%)
- `packages/react-router-dev/vite/node-adapter.ts` -> **Severity: 371.9** (Blast Radius: 3.719 * Doc Risk: 100.0%)
- `playground/rsc-vite/src/counter.tsx` -> **Severity: 363.472** (Blast Radius: 5.547 * Doc Risk: 65.5259%)
- `packages/react-router-dev/vite/babel.ts` -> **Severity: 341.344** (Blast Radius: 5.213 * Doc Risk: 65.4793%)
- `packages/react-router-dev/vite/cloudflare-dev-proxy.ts` -> **Severity: 295.8** (Blast Radius: 2.958 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
