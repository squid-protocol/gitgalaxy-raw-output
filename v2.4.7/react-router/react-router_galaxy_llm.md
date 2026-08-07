# ARCHITECTURAL_BRIEF: react-router
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/react-router` |
| **Timestamp** | `2026-08-07T04:17:38.960118+00:00` |
| **Scan Duration** | `1.75s` |
| **Git Branch** | `main` |
| **Git Commit** | `201cd41be3e2fadf0fe851d9ac6c836458707ca3` |
| **Git Remote** | `https://github.com/remix-run/react-router.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 514 malicious artifacts.

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
> **Architectural Drift Z-Score:** `4.267`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 400 | 50.0% |
| file_cluster_13 | 110 | 13.8% |
| file_cluster_4 | 68 | 8.5% |
| file_cluster_0 | 34 | 4.2% |
| file_cluster_2 | 26 | 3.2% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 19.6 | 5.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.8 | 0.9 | 0.0 |
| API Exposure | 0.0 | 14.9 | 4.5 | 5.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 21.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 98.1 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 76.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 13.2 | 1.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 95.3 | 3.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.3 | 12.0 | 0.0 |
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

- `ReactRouterVitePlugin` (@ `packages/react-router-dev/vite/plugin.ts`) -> Impact: **216.5** | LOC: 624
- `reactRouterRSCVitePlugin` (@ `packages/react-router-dev/vite/rsc/plugin.ts`) -> Impact: **194.0** | LOC: 485
- `getContext` (@ `packages/create-react-router/index.ts`) -> Impact: **146.4** | LOC: 409
- `copyTemplateFromLocalFilePath` (@ `packages/create-react-router/copy-template.ts`) -> Impact: **128.0** | LOC: 320
- `getEnvironmentOptionsResolvers` (@ `packages/react-router-dev/vite/plugin.ts`) -> Impact: **124.5** | LOC: 211
  * *Intent:* // This isn't honored by the SSR environment config (which seems
- `hasChunkableExport` (@ `packages/react-router-dev/vite/route-chunks.ts`) -> Impact: **115.1** | LOC: 293
- `flatRoutesUniversal` (@ `packages/react-router-fs-routes/flatRoutes.ts`) -> Impact: **111.5** | LOC: 172
- `removeExports` (@ `packages/react-router-dev/vite/remove-exports.ts`) -> Impact: **91.5** | LOC: 151
- `getRouteSegments` (@ `packages/react-router-fs-routes/flatRoutes.ts`) -> Impact: **90.5** | LOC: 130
- `copyTempDirToAppDirStep` (@ `packages/create-react-router/index.ts`) -> Impact: **87.0** | LOC: 261

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 17 | 5186.28 | 1.33% | 0.0% |
| `scripts` | 18 | 597.49 | 54.62% | 61.45% |
| `packages/react-router-dev/vite` | 22 | 373.42 | 43.58% | 16.92% |
| `packages/create-react-router` | 16 | 367.37 | 54.24% | 12.89% |
| `packages/react-router-dev/vite/static` | 2 | 281.04 | 71.11% | 23.38% |
| `packages/react-router-dev` | 14 | 212.47 | 8.45% | 8.99% |
| `integration/helpers` | 8 | 200.21 | 56.54% | 48.32% |
| `packages/react-router` | 15 | 161.5 | 3.71% | 0.65% |
| `examples/ssr-data-router` | 6 | 143.22 | 16.31% | 0.0% |
| `examples/notes/src` | 5 | 125.11 | 23.8% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `integration/rsc/utils.ts` -> **100.0%** Exposure
- `packages/react-router/__tests__/dom/components/LazyComponent.tsx` -> **100.0%** Exposure
- `packages/react-router/__tests__/dom/polyfills/drop-FormData-submitter.ts` -> **100.0%** Exposure
- `packages/react-router/__tests__/router/TestSequences/EncodedReservedCharacters.ts` -> **100.0%** Exposure
- `packages/react-router/__tests__/router/TestSequences/GoBack.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `integration/helpers/create-fixture.ts` -> **100.0%** Exposure
- `integration/helpers/playwright-fixture.ts` -> **100.0%** Exposure
- `integration/helpers/vite.ts` -> **100.0%** Exposure
- `packages/create-react-router/__tests__/setupAfterEnv.ts` -> **100.0%** Exposure
- `packages/create-react-router/prompts-confirm.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/react-router-dev/vite/plugin.ts` -> **0** Orphaned Functions | **26** Duplicates
- `integration/helpers/create-fixture.ts` -> **0** Orphaned Functions | **21** Duplicates
- `packages/react-router-dev/vite/route-chunks.ts` -> **0** Orphaned Functions | **16** Duplicates
- `integration/helpers/vite.ts` -> **0** Orphaned Functions | **13** Duplicates
- `scripts/bench/passthrough-requests.bench.mjs` -> **1** Orphaned Functions | **12** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `898` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `integration/helpers/create-fixture.ts` (TYPESCRIPT) -> Cumulative Risk: **762.07**
- **Archetype:** `file_cluster_4` (Distance: 12.619 IQR)
- **Magnitude:** 74.16 | **LOC:** 550 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9747%)
- **Heaviest Functions:** `createFixture` (Impact: 56.8), `createAppFixture` (Impact: 42.1), `reactRouterBuild` (Impact: 29.1)

### 2. `packages/react-router-dev/vite/plugin.ts` (TYPESCRIPT) -> Cumulative Risk: **751.68**
- **Archetype:** `file_cluster_4` (Distance: 13.542 IQR)
- **Magnitude:** 196.12 | **LOC:** 4372 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 36.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9939%), Tech Debt (98.661%)
- **Heaviest Functions:** `ReactRouterVitePlugin` (Impact: 216.5), `getEnvironmentOptionsResolvers` (Impact: 124.5), `next` (Impact: 54.5)

### 3. `packages/react-router-dev/vite/remove-exports.ts` (TYPESCRIPT) -> Cumulative Risk: **696.08**
- **Archetype:** `file_cluster_17` (Distance: 16.078 IQR)
- **Magnitude:** 38.31 | **LOC:** 239 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9768%), Tech Debt (99.6801%), Documentation (88.7277%)
- **Heaviest Functions:** `removeExports` (Impact: 91.5), `traverse` (Impact: 62.5), `validateDestructuredExports` (Impact: 53.7)

### 4. `packages/react-router/__tests__/router/utils/data-router-setup.ts` (TYPESCRIPT) -> Cumulative Risk: **679.08**
- **Archetype:** `file_cluster_4` (Distance: 11.69 IQR)
- **Magnitude:** 43.6 | **LOC:** 763 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9253%), Tech Debt (99.1879%)
- **Heaviest Functions:** `enhanceRoutes` (Impact: 33.6), `fetch` (Impact: 33.5), `invariant` (Impact: 19.7)

### 5. `packages/react-router-dev/config/config.ts` (TYPESCRIPT) -> Cumulative Risk: **673.28**
- **Archetype:** `file_cluster_4` (Distance: 13.303 IQR)
- **Magnitude:** 76.6 | **LOC:** 1198 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9873%), Tech Debt (81.0848%)
- **Heaviest Functions:** `onChange` (Impact: 60.0), `getStaticPaths` (Impact: 39.0), `mergeReactRouterConfig` (Impact: 31.2)

### 6. `packages/create-react-router/index.ts` (TYPESCRIPT) -> Cumulative Risk: **666.95**
- **Archetype:** `file_cluster_4` (Distance: 11.544 IQR)
- **Magnitude:** 62.94 | **LOC:** 706 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.655%), Cognitive Load (99.364%)
- **Heaviest Functions:** `getContext` (Impact: 146.4), `copyTempDirToAppDirStep` (Impact: 87.0), `copyTemplateToTempDirStep` (Impact: 30.6)

### 7. `integration/helpers/playwright-fixture.ts` (TYPESCRIPT) -> Cumulative Risk: **665.05**
- **Archetype:** `file_cluster_4` (Distance: 13.365 IQR)
- **Magnitude:** 60.16 | **LOC:** 385 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.3497%)
- **Heaviest Functions:** `action` (Impact: 21.1), `getPageContent` (Impact: 17.1), `goto` (Impact: 13.2)

### 8. `packages/react-router-dev/vite/static/refresh-utils.mjs` (JAVASCRIPT) -> Cumulative Risk: **658.66**
- **Archetype:** `file_cluster_4` (Distance: 12.086 IQR)
- **Magnitude:** 183.06 | **LOC:** 171 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.988%), Concurrency (99.9439%), Cognitive Load (92.4648%)
- **Heaviest Functions:** `clearTimeout` (Impact: 57.7), `validateRefreshBoundaryAndEnqueueUpdate` (Impact: 24.5), `predicateOnExport` (Impact: 12.6)

### 9. `integration/helpers/vite.ts` (TYPESCRIPT) -> Cumulative Risk: **655.78**
- **Archetype:** `file_cluster_4` (Distance: 12.499 IQR)
- **Magnitude:** 32.96 | **LOC:** 616 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 56.2%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `dev` (Impact: 4.3), `customDev` (Impact: 4.3), `vitePreview` (Impact: 4.3)

### 10. `packages/react-router/__tests__/router/utils/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **648.01**
- **Archetype:** `file_cluster_4` (Distance: 12.154 IQR)
- **Magnitude:** 14.5 | **LOC:** 98 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `createDeferred` (Impact: 19.1), `findRouteById` (Impact: 15.1), `invariant` (Impact: 9.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_4` (Drift: 13.542 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.129 IQR)
- **Top Global Matches:** file_cluster_4: 13.542, file_cluster_17: 13.874, file_cluster_13: 13.912
- **Magnitude:** 196.12 | **LOC:** 4372 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 36.0%
- **Risk Profile:** Cognitive Load (98.4282%), Tech Debt (98.661%)
**Top Internal Functions/Classes:**
  * `ReactRouterVitePlugin` (Impact: 216.5)
  * `getEnvironmentOptionsResolvers` (Impact: 124.5)
    * *Intent:* // This isn't honored by the SSR environment config (which seems
  * `next` (Impact: 54.5)
  * `configureServer` (Impact: 44.8)
  * `getHandler` (Impact: 44.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 367`, `args: 105`, `func_start: 97`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 455`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 26`
* *Architecture:* `io: 64`, `api: 29`, `concurrency: 411`, `import: 52`
* *Defense:* `safety: 102`, `doc: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` resolve-file-url, pick, manifest, remove-exports, ), routes, optimize-deps-entries, $virtualHmrRuntime.id...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/static/refresh-utils.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.086 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.332 IQR)
- **Top Global Matches:** file_cluster_4: 12.086, file_cluster_17: 12.472, file_cluster_11: 12.551
- **Magnitude:** 183.06 | **LOC:** 171 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.4648%), Tech Debt (19.5754%)
**Top Internal Functions/Classes:**
  * `clearTimeout` (Impact: 57.7)
  * `validateRefreshBoundaryAndEnqueueUpdate` (Impact: 24.5)
  * `predicateOnExport` (Impact: 12.6)
  * `registerExportsForReactRefresh` (Impact: 9.3)
    * *Intent:* // Taken from https://github.com/pmmmwh/react-refresh-webpack-plugin/blob/main/lib/runtime/RefreshUt...
  * `enqueueUpdate` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 38`, `args: 13`, `func_start: 7`
* *Risk/State:* `state_mutation: 40`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 19`, `import: 1`
* *Defense:* `safety: 11`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/remove-prerelease-changelogs.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.978 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.656 IQR)
- **Top Global Matches:** file_cluster_4: 12.978, file_cluster_13: 13.249, file_cluster_8: 13.694
- **Magnitude:** 177.32 | **LOC:** 124 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7425%), Tech Debt (97.1913%)
**Top Internal Functions/Classes:**
  * `transformer` (Impact: 27.7)
    * *Intent:* /**
  * `removePreReleaseSectionFromMarkdown` (Impact: 24.4)
  * `remove` (Impact: 24.1)
    * *Intent:* /** * @param {import('./unist').RootNode} tree
  * `removePreReleaseChangelogs` (Impact: 9.8)
  * `isPrereleaseVersion` (Impact: 8.9)
    * *Intent:* /** * @param {import("./unist").Node & { __REMOVE__?: boolean }} node * @param {number | null | unde...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 36`, `args: 8`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `concurrency: 33`, `import: 9`
* *Defense:* `safety: 8`, `doc: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` remark-stringify, get-packages, unist-util-remove, node:path, node:url, unified, node:fs, remark-gfm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/publish.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.167 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.359 IQR)
- **Top Global Matches:** file_cluster_4: 12.167, file_cluster_13: 12.455, file_cluster_8: 12.626
- **Magnitude:** 112.86 | **LOC:** 155 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.44%), Tech Debt (99.9993%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 26.0)
  * `publishBuild` (Impact: 17.2)
  * `invariant` (Impact: 3.6)
    * *Intent:* /**
  * `invariant` (Impact: 2.5)
  * `publishBuild` (Impact: 2.4)
    * *Intent:* // 4. Publish to npm
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 24`, `args: 6`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 27`, `duplicate_logic: 6`
* *Architecture:* `io: 8`, `concurrency: 25`, `import: 4`
* *Defense:* `safety: 6`, `doc: 14`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsonfile, semver, child_process, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/notes/src/notes.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.136 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.883 IQR)
- **Top Global Matches:** file_cluster_4: 13.136, file_cluster_17: 14.092, file_cluster_13: 14.221
- **Magnitude:** 104.54 | **LOC:** 38 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getNote` (Impact: 6.2)
  * `deleteNote` (Impact: 4.5)
  * `getNotes` (Impact: 4.2)
  * `set` (Impact: 1.9)
  * `createNote` (Impact: 1.1)
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

### `examples/ssr-data-router/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.416 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.684 IQR)
- **Top Global Matches:** file_cluster_4: 12.416, file_cluster_13: 12.907, file_cluster_8: 13.254
- **Magnitude:** 102.8 | **LOC:** 80 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.8458%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createServer` (Impact: 29.0)
  * `resolve` (Impact: 2.6)
  * `createServer` (Impact: 2.0)
  * `resolve` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 26`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `concurrency: 40`, `import: 6`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` express, vite, compression, path, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/static/rsc-refresh-utils.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.318 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.721 IQR)
- **Top Global Matches:** file_cluster_8: 10.318, file_cluster_4: 10.346, file_cluster_13: 10.664
- **Magnitude:** 97.98 | **LOC:** 127 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7475%), Tech Debt (27.1931%)
**Top Internal Functions/Classes:**
  * `validateRefreshBoundaryAndEnqueueUpdate` (Impact: 24.5)
  * `clearTimeout` (Impact: 13.4)
  * `predicateOnExport` (Impact: 12.6)
  * `registerExportsForReactRefresh` (Impact: 9.3)
    * *Intent:* // Taken from https://github.com/pmmmwh/react-refresh-webpack-plugin/blob/main/lib/runtime/RefreshUt...
  * `enqueueUpdate` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 25`, `args: 11`, `func_start: 8`
* *Risk/State:* `state_mutation: 10`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 5`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 95.72 | **LOC:** 4786 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `packages/react-router-dev/bin.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.18 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.655 IQR)
- **Top Global Matches:** file_cluster_13: 14.18, file_cluster_8: 14.665, file_cluster_17: 14.701
- **Magnitude:** 90.68 | **LOC:** 16 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index, arg
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.675 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.109 IQR)
- **Top Global Matches:** file_cluster_4: 12.675, file_cluster_13: 13.14, file_cluster_17: 13.52
- **Magnitude:** 89.88 | **LOC:** 94 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9975%), Tech Debt (99.9541%)
**Top Internal Functions/Classes:**
  * `fileExists` (Impact: 6.4)
  * `ensureCleanWorkingDirectory` (Impact: 5.6)
    * *Intent:* /** * @param {string} packageName * @returns {Promise<string | undefined>} */
  * `updateExamplesPackageConfig` (Impact: 3.9)
  * `invariant` (Impact: 3.6)
  * `getPackageVersion` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 21`, `args: 8`, `func_start: 10`
* *Risk/State:* `state_mutation: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 46`, `import: 5`
* *Defense:* `safety: 3`, `doc: 22`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jsonfile, child_process, type-fest, path, fs, constants
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/ssr/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.859 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.59 IQR)
- **Top Global Matches:** file_cluster_4: 11.859, file_cluster_13: 12.315, file_cluster_8: 12.671
- **Magnitude:** 82.44 | **LOC:** 72 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.1448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createServer` (Impact: 18.6)
  * `resolve` (Impact: 3.8)
  * `createServer` (Impact: 2.0)
  * `resolve` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 23`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 21`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `concurrency: 34`, `import: 6`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` express, vite, compression, path, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/multi-app/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.331 IQR)
- **Local Micro-Species:** `Cluster 5: I/O, UI & Routing Configuration` (Drift: 5.149 IQR)
- **Top Global Matches:** file_cluster_4: 12.331, file_cluster_13: 12.828, file_cluster_8: 13.183
- **Magnitude:** 80.6 | **LOC:** 67 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.9839%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createServer` (Impact: 22.6)
  * `createServer` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 24`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `concurrency: 31`, `import: 5`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` express, vite, compression, path, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/config/config.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.303 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.966 IQR)
- **Top Global Matches:** file_cluster_4: 13.303, file_cluster_13: 13.49, file_cluster_11: 13.6
- **Magnitude:** 76.6 | **LOC:** 1198 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (46.4188%), Tech Debt (81.0848%)
**Top Internal Functions/Classes:**
  * `onChange` (Impact: 60.0)
  * `getStaticPaths` (Impact: 39.0)
  * `mergeReactRouterConfig` (Impact: 31.2)
    * *Intent:* /** * A function that is called after the full React Router build is complete.
  * `mergeRequired` (Impact: 26.1)
    * *Intent:* /**
  * `isEntryFileDependency` (Impact: 24.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 169`, `args: 60`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 259`, `planned_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 23`, `api: 25`, `concurrency: 136`, `import: 19`
* *Defense:* `safety: 81`, `doc: 31`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` express, omit, routes, express, vite, vite-node, cloneDeep, node:child_process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/helpers/create-fixture.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.619 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.207 IQR)
- **Top Global Matches:** file_cluster_4: 12.619, file_cluster_13: 13.163, file_cluster_11: 13.281
- **Magnitude:** 74.16 | **LOC:** 550 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (98.5309%), Tech Debt (99.9747%)
**Top Internal Functions/Classes:**
  * `createFixture` (Impact: 56.8)
  * `createAppFixture` (Impact: 42.1)
    * *Intent:* /** * @deprecated Use `integration/helpers/vite.ts`'s `test` instead * * This implementation sometim...
  * `reactRouterBuild` (Impact: 29.1)
  * `reject` (Impact: 20.3)
  * `reject` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 118`, `args: 50`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 194`, `duplicate_logic: 21`
* *Architecture:* `io: 34`, `api: 14`, `concurrency: 267`, `import: 17`
* *Defense:* `safety: 18`, `doc: 3`, `immutability_locks: 8`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` express, node:stream, strip-indent, get-port, express, type-fest, cross-spawn, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/route-chunks.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.961 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_17: 13.961, file_cluster_11: 14.424, file_cluster_0: 14.551
- **Magnitude:** 65.11 | **LOC:** 1007 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.0238%), Tech Debt (99.388%)
**Top Internal Functions/Classes:**
  * `hasChunkableExport` (Impact: 115.1)
  * `getExportDependencies` (Impact: 84.3)
  * `handleExport` (Impact: 43.7)
  * `invariant` (Impact: 34.9)
  * `walk` (Impact: 27.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 119`, `args: 73`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 144`, `dead_code: 14`, `duplicate_logic: 16`
* *Architecture:* `io: 49`, `api: 21`, `import: 4`
* *Defense:* `safety: 24`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001252
  * `Imports (Out-Degree: 3):` module, babel, generator, invariant, cache
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/create-react-router/prompts-text.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.324 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.238 IQR)
- **Top Global Matches:** file_cluster_4: 14.324, file_cluster_8: 14.537, file_cluster_13: 14.611
- **Magnitude:** 64.95 | **LOC:** 285 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6903%), Tech Debt (38.1338%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 18.2)
  * `clear` (Impact: 13.6)
  * `value` (Impact: 8.6)
  * `deleteForward` (Impact: 7.9)
  * `constructor` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 31`, `args: 28`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 491`, `duplicate_logic: 2`
* *Architecture:* `api: 14`, `concurrency: 25`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.463
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001669
  * `Imports (Out-Degree: 1):` prompts-prompt-base, utils, sisteransi
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-router-fs-routes/flatRoutes.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.421 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.154 IQR)
- **Top Global Matches:** file_cluster_8: 12.421, file_cluster_13: 12.506, file_cluster_17: 12.536
- **Magnitude:** 63.57 | **LOC:** 565 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.1741%), Tech Debt (40.0456%)
**Top Internal Functions/Classes:**
  * `flatRoutesUniversal` (Impact: 111.5)
  * `getRouteSegments` (Impact: 90.5)
  * `createRoutePath` (Impact: 23.9)
  * `flatRoutes` (Impact: 22.7)
  * `findRouteModuleForFolder` (Impact: 19.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 61`, `args: 27`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 269`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 34`, `api: 15`, `import: 6`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001252
  * `Imports (Out-Degree: 0):` manifest, minimatch, node:path, normalizeSlashes, node:fs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/create-react-router/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.544 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.294 IQR)
- **Top Global Matches:** file_cluster_4: 11.544, file_cluster_8: 11.935, file_cluster_13: 11.976
- **Magnitude:** 62.94 | **LOC:** 706 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.364%), Tech Debt (98.1762%)
**Top Internal Functions/Classes:**
  * `getContext` (Impact: 146.4)
  * `copyTempDirToAppDirStep` (Impact: 87.0)
  * `copyTemplateToTempDirStep` (Impact: 30.6)
  * `info` (Impact: 23.1)
  * `createReactRouter` (Impact: 15.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 57`, `args: 41`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 87`, `duplicate_logic: 11`
* *Architecture:* `io: 21`, `api: 3`, `concurrency: 130`, `import: 15`
* *Defense:* `safety: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` node:os, utils, sort-package-json, prompt, node:process, loading-indicator, copy-template, strip-ansi...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/version.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.94 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.92 IQR)
- **Top Global Matches:** file_cluster_4: 11.94, file_cluster_13: 12.265, file_cluster_17: 12.402
- **Magnitude:** 60.5 | **LOC:** 65 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.5398%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 14.4)
  * `invariant` (Impact: 4.2)
  * `invariant` (Impact: 2.5)
  * `execSync` (Impact: 2.5)
  * `run` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `args: 4`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 21`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `concurrency: 13`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` child_process, utils, picocolors, node:fs, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/helpers/playwright-fixture.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.365 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.063 IQR)
- **Top Global Matches:** file_cluster_4: 13.365, file_cluster_13: 14.095, file_cluster_11: 14.248
- **Magnitude:** 60.16 | **LOC:** 385 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (52.5%), Tech Debt (99.3497%)
**Top Internal Functions/Classes:**
  * `action` (Impact: 21.1)
    * *Intent:* /** * Keeps the fixture running for as many seconds as you want so you can go * poke around in the b...
  * `getPageContent` (Impact: 17.1)
  * `goto` (Impact: 13.2)
    * *Intent:* /**
  * `collectResponses` (Impact: 8.6)
    * *Intent:* /**
  * `onRequestDone` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 82`, `args: 44`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 154`, `duplicate_logic: 5`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 310`, `import: 6`
* *Defense:* `safety: 7`, `doc: 22`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, create-fixture.js, cheerio, node:child_process, prettier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 59.34 | **LOC:** 2967 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `scripts/docs.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.215 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.014 IQR)
- **Top Global Matches:** file_cluster_4: 12.215, file_cluster_17: 12.252, file_cluster_13: 12.496
- **Magnitude:** 52.56 | **LOC:** 769 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (62.4888%), Tech Debt (85.103%)
**Top Internal Functions/Classes:**
  * `generateMarkdownForComment` (Impact: 70.3)
  * `simplifyComment` (Impact: 55.5)
  * `getSignature` (Impact: 22.1)
  * `warn` (Impact: 21.4)
  * `generateMarkdownDocs` (Impact: 20.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 106`, `args: 55`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 150`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 22`, `api: 10`, `concurrency: 56`, `import: 8`
* *Defense:* `safety: 21`, `doc: 12`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dox, prettier, fast-glob, node:path, node:util, typescript, node:fs, typedoc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 50.84 | **LOC:** 2542 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `scripts/bench/passthrough-requests.bench.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.884 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.866 IQR)
- **Top Global Matches:** file_cluster_8: 7.884, file_cluster_7: 8.744, file_cluster_4: 8.766
- **Magnitude:** 46.36 | **LOC:** 140 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.7668%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `handleDataRequest` (Impact: 4.5)
  * `default` (Impact: 4.1)
  * `describe` (Impact: 2.4)
  * `describe` (Impact: 2.2)
  * `describe` (Impact: 2.2)
    * *Intent:* // --------------------------------------------------------------------------- // Benchmarks
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 23`, `args: 15`, `func_start: 17`
* *Risk/State:* `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `concurrency: 14`, `import: 2`
* *Defense:* `doc: 1`, `test: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.15
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `playground/split-route-modules-spa/react-router.config.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 1, safety: 1
- `playground/middleware/react-router.config.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 1, safety: 1
- `playground/split-route-modules-spa/app/routes.ts` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 4, func_start: 4, indent_spaces: 4
- `playground/split-route-modules/app/routes.ts` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 4, func_start: 4, indent_spaces: 4
- `packages/react-router-dev/vite/plugins/validate-plugin-order.ts` (TYPESCRIPT) | Magnitude: 4.72 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 13, structural_boundaries: 7, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/data-router/src/todos.ts` (TYPESCRIPT) | Magnitude: 3.51 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 13, args: 12, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/delete-nightly-tags.sh` (SHELL) | Magnitude: 3.87 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 24, debug_prints: 14, branch: 9, structural_boundaries: 9
- `scripts/delete-pre-tags.sh` (SHELL) | Magnitude: 2.09 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, io: 9, debug_prints: 9, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/react-router-dev/vite/rsc/plugin.ts` (TYPESCRIPT) | Magnitude: 43.29 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 548, branch: 129, structural_boundaries: 114, state_mutation: 93
- `playground/rsc-vite/src/routes/redirect.ts` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, branch: 1, args: 1
- `examples/ssr-data-router/src/lazy.tsx` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, concurrency: 5, args: 3
- `packages/react-router/__tests__/router/TestSequences/InitialLocationDefaultKey.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, branch: 2, args: 2, func_start: 2
- `packages/create-react-router/__tests__/msw-register.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, args: 1, closures: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/react-router/__tests__/router/utils/custom-matchers.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, generics: 7, branch: 6
- `packages/create-react-router/prompt.ts` (TYPESCRIPT) | Magnitude: 6.85 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 80, generics: 62, state_mutation: 34
- `packages/react-router-dev/vite/cache.ts` (TYPESCRIPT) | Magnitude: 2.22 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 12, structural_boundaries: 8, generics: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/react-router-dev/vite/remove-exports.ts` (TYPESCRIPT) | Magnitude: 38.31 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 170, branch: 65, state_mutation: 51, structural_boundaries: 45
- `scripts/find-release-from-changeset.js` (JAVASCRIPT) | Magnitude: 19.44 | Delta: **0.255 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 9, doc: 7, structural_boundaries: 6
- `packages/react-router-dev/vite/route-chunks.ts` (TYPESCRIPT) | Magnitude: 65.11 | Delta: **0.463 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 453, state_mutation: 144, structural_boundaries: 119, branch: 112

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/notes/src/main.jsx` (JAVASCRIPT) | Magnitude: 14.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, ui_framework: 3, import: 3, indent_spaces: 3
- `examples/multi-app/home/main.jsx` (JAVASCRIPT) | Magnitude: 15.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, ui_framework: 4, import: 4
- `examples/multi-app/inbox/main.jsx` (JAVASCRIPT) | Magnitude: 15.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, ui_framework: 4, import: 4
- `examples/modal/src/App.tsx` (TYPESCRIPT) | Magnitude: 13.28 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 267, state_mutation: 40, ui_framework: 33, branch: 28
- `integration/helpers/cloudflare-dev-proxy-template/app/root.tsx` (TYPESCRIPT) | Magnitude: 0.64 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, ui_framework: 5, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/react-router-dev/config/defaults/entry.server.node.tsx` (TYPESCRIPT) | Magnitude: 6.31 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, concurrency: 18, structural_boundaries: 15, args: 12
- `packages/react-router-dev/vite/plugins/prerender.ts` (TYPESCRIPT) | Magnitude: 33.29 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 276, structural_boundaries: 73, branch: 59, concurrency: 49
- `packages/react-router/__tests__/utils/waitForRedirect.tsx` (TYPESCRIPT) | Magnitude: 0.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, branch: 1
- `packages/create-react-router/__tests__/msw.ts` (TYPESCRIPT) | Magnitude: 3.17 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 18, io: 15, concurrency: 12
- `packages/react-router-node/server.ts` (TYPESCRIPT) | Magnitude: 2.46 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 18, concurrency: 14, generics: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `prettier.config.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `playground/rsc-vite-7-framework/app/routes/client-loader-hydrate/route.tsx` (TYPESCRIPT) | Magnitude: 0.83 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, import: 4, args: 3
- `examples/multi-app/home/App.jsx` (JAVASCRIPT) | Magnitude: 12.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, ui_framework: 12, structural_boundaries: 8, args: 4
- `playground/rsc-vite/src/routes/home/home.client.tsx` (TYPESCRIPT) | Magnitude: 1.55 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 20, api: 7, branch: 5
- `playground/split-route-modules/app/routes/splittable.tsx` (TYPESCRIPT) | Magnitude: 1.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, args: 4, func_start: 4
- `playground/rsc-vite-framework/app/routes/client-loader-hydrate/route.tsx` (TYPESCRIPT) | Magnitude: 0.83 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, import: 4, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-router-dev/vite/rsc/plugin.ts` -> Churn: **74.72%** | Cog Load: 83.2673% | Debt: 15.5998%
- `packages/react-router-dev/vite/plugin.ts` -> Churn: **73.03%** | Cog Load: 98.4282% | Debt: 98.661%
- `packages/react-router-dev/config/config.ts` -> Churn: **65.89%** | Cog Load: 46.4188% | Debt: 81.0848%
- `integration/helpers/vite.ts` -> Churn: **60.15%** | Cog Load: 100.0% | Debt: 99.9998%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/react-router-dev/vite/route-chunks.ts` -> **Matt Brophy** (100.0% isolated ownership) | Magnitude: 65.11
- `packages/react-router-fs-routes/flatRoutes.ts` -> **Fróði Karlsson** (100.0% isolated ownership) | Magnitude: 63.57
- `scripts/version.js` -> **Roli Bosch** (100.0% isolated ownership) | Magnitude: 60.5
- `integration/helpers/playwright-fixture.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 60.16

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react-router-dev/__tests__/utils/cli.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/create-react-router/prompts-prompt-base.ts` -> **Severity: 0.497** (Embedded: 0.005 * Error Risk: 99.2492%)
- `packages/create-react-router/prompts-select.ts` -> **Severity: 0.281** (Embedded: 0.0028 * Error Risk: 99.9517%)
- `packages/react-router-dev/vite/profiler.ts` -> **Severity: 0.242** (Embedded: 0.0033 * Error Risk: 72.3979%)
- `packages/react-router-dev/invariant.ts` -> **Severity: 0.237** (Embedded: 0.0078 * Error Risk: 30.2941%)
- `packages/react-router-dev/vite/remove-exports.ts` -> **Severity: 0.223** (Embedded: 0.0028 * Error Risk: 79.1936%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `integration/helpers/express.ts` -> **Severity: 550.105** (Blast Radius: 16.947 * Doc Risk: 32.4603%)
- `packages/react-router-dev/vite/node-adapter.ts` -> **Severity: 323.036** (Blast Radius: 3.719 * Doc Risk: 86.8611%)
- `playground/middleware/app/contexts.ts` -> **Severity: 212.033** (Blast Radius: 6.361 * Doc Risk: 33.3333%)
- `packages/react-router-dev/vite/babel.ts` -> **Severity: 174.056** (Blast Radius: 5.213 * Doc Risk: 33.3889%)
- `playground/rsc-vite/src/counter.tsx` -> **Severity: 157.913** (Blast Radius: 5.547 * Doc Risk: 28.4681%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
