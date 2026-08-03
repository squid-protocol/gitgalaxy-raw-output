# ARCHITECTURAL_BRIEF: workers-sdk
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/workers-sdk` |
| **Timestamp** | `2026-08-03T20:00:09.483199+00:00` |
| **Scan Duration** | `13.12s` |
| **Git Branch** | `main` |
| **Git Commit** | `f07100810d6d8c00e7d1977f0b760b369b52aed0` |
| **Git Remote** | `https://github.com/cloudflare/workers-sdk.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2423 malicious artifacts.

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
| Total Artifacts | 4632 |
| Analyzed Artifacts (Scanned) | 3428 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1204 |
| Total LOC | 277654 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 74.0% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7509 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1959 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.9235 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 173 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2226 | 263195 | 64.9% |
| JSON | 587 | 7673 | 17.1% |
| PLAINTEXT | 216 | 7 | 6.3% |
| JAVASCRIPT | 169 | 4742 | 4.9% |
| MARKDOWN | 111 | 0 | 3.2% |
| HTML | 52 | 1013 | 1.5% |
| XML | 24 | 9 | 0.7% |
| CSS | 14 | 622 | 0.4% |
| PYTHON | 9 | 58 | 0.3% |
| SQLITE | 5 | 16 | 0.1% |
| DOCKERFILE | 5 | 49 | 0.1% |
| BINARY_THREAT | 4 | 4 | 0.1% |
| PHP | 3 | 146 | 0.1% |
| MAKEFILE | 1 | 29 | 0.0% |
| SHELL | 1 | 28 | 0.0% |
| YAML | 1 | 63 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.383`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2142 | 62.5% |
| file_cluster_13 | 566 | 16.5% |
| file_cluster_4 | 240 | 7.0% |
| file_cluster_2 | 50 | 1.5% |
| file_cluster_16 | 42 | 1.2% |
| file_cluster_17 | 27 | 0.8% |
| Unknown | 11 | 0.3% |
| file_cluster_0 | 10 | 0.3% |
| file_cluster_6 | 4 | 0.1% |
| file_cluster_9 | 3 | 0.1% |
| file_cluster_11 | 2 | 0.1% |
| file_cluster_7 | 1 | 0.0% |
| file_cluster_1 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 320 | 9.3% |
| Static: Minified & Vendor Opaque Mass | 9 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1204*

**Composition by Extension & Reason:**
- `.ts`: 493x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 8 LOC), 3x Excluded (Machine-Generated Source Code Signature: 5 LOC)
- `no_extension`: 118x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Unsupported Format (.undeterminable), 7x Excluded (Unsupported Extension: '.ts"')
- `.json`: 108x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3161 LOC)
- `.mts`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 64 LOC), 1x Excluded (Machine-Generated Source Code Signature: 161 LOC)
- `.jsonc`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 55x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1765 LOC), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.mjs`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 12x Excluded (Unsupported Extension: '.patch'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wasm`: 6x Excluded (Unsupported Extension: '.wasm'), 4x Excluded (Binary Format Detected), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vars`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.6 | 5.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.0 | 14.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.7 | 0.8 | 0.0 |
| API Exposure | 0.0 | 19.9 | 4.3 | 5.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 76.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.5 | 1.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 91.6 | 8.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 39.1 | 30.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 1.1 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/wrangler/src/__tests__/pages/deploy.test.ts` (Hits: 222)
- `packages/wrangler/src/__tests__/type-generation.test.ts` (Hits: 177)
- `packages/vite-plugin-cloudflare/src/__tests__/resolve-plugin-config.spec.ts` (Hits: 136)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **logger.ts** (`packages/wrangler/src/logger.ts`) — 284 inbound connections
2. **create-command.ts** (`packages/wrangler/src/core/create-command.ts`) — 218 inbound connections
3. **run-wrangler.ts** (`packages/wrangler/src/__tests__/helpers/run-wrangler.ts`) — 131 inbound connections
4. **mock-account-id.ts** (`packages/wrangler/src/__tests__/helpers/mock-account-id.ts`) — 111 inbound connections
5. **vite-plugin.ts** (`packages/wrangler/src/autoconfig/frameworks/utils/vite-plugin.ts`) — 102 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/wrangler/src/index.ts`) — 224 outbound dependencies
2. **index.ts** (`packages/containers-shared/src/client/index.ts`) — 219 outbound dependencies
3. **deploy.ts** (`packages/wrangler/src/deploy/deploy.ts`) — 54 outbound dependencies
4. **templates.ts** (`packages/create-cloudflare/src/templates.ts`) — 48 outbound dependencies
5. **upload.ts** (`packages/wrangler/src/versions/upload.ts`) — 47 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `describe` (@ `packages/wrangler/src/__tests__/r2/bucket.test.ts`) -> Impact: **1432.8** | LOC: 1290
- `describe` (@ `packages/wrangler/src/__tests__/pipelines-setup.test.ts`) -> Impact: **1110.3** | LOC: 1421
- `mapWorkerMetadataBindings` (@ `packages/workers-utils/src/map-worker-metadata-bindings.ts`) -> Impact: **793.3** | LOC: 386
  * *Intent:* /**
- `describe` (@ `packages/wrangler/src/__tests__/dev.test.ts`) -> Impact: **792.0** | LOC: 1291
- `describe` (@ `packages/wrangler/src/__tests__/middleware.test.ts`) -> Impact: **730.9** | LOC: 1109
- `describe` (@ `packages/wrangler/src/__tests__/secret.test.ts`) -> Impact: **609.5** | LOC: 1383
- `describe` (@ `packages/wrangler/src/__tests__/kv/key.test.ts`) -> Impact: **597.8** | LOC: 1286
- `describe` (@ `packages/wrangler/src/__tests__/deploy/formats.test.ts`) -> Impact: **594.6** | LOC: 1222
- `describe` (@ `packages/wrangler/src/__tests__/deploy/build.test.ts`) -> Impact: **576.4** | LOC: 1308
- `describe` (@ `packages/wrangler/src/__tests__/pages/pages.test.ts`) -> Impact: **487.9** | LOC: 302

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `describe` (@ `packages/wrangler/src/__tests__/pages/pages.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/wrangler/src/__tests__/versions/deployments/deployments.list.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/wrangler/src/__tests__/versions/deployments/deployments.status.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/wrangler/src/__tests__/deploy/build.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/wrangler/src/__tests__/deploy/workflows.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/wrangler/src/__tests__/middleware.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/wrangler/src/__tests__/pipelines-setup.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/wrangler/src/__tests__/r2/bucket.test.ts`) -> **O(2^N) [Recursive]**
- `App` (@ `packages/create-cloudflare/templates/react/workers/js/src/App.jsx`) -> **O(2^N) [Recursive]**
- `App` (@ `packages/create-cloudflare/templates/react/workers/ts/src/App.tsx`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/vite-plugin-cloudflare/src/__tests__/resolve-plugin-config.spec.ts`) -> DB Complexity: **447**
- `describe` (@ `packages/wrangler/src/__tests__/deploy/formats.test.ts`) -> DB Complexity: **386**
- `describe` (@ `packages/wrangler/src/__tests__/type-generation.test.ts`) -> DB Complexity: **381**
- `describe` (@ `packages/wrangler/src/__tests__/deploy/build.test.ts`) -> DB Complexity: **379**
- `describe` (@ `packages/wrangler/src/__tests__/middleware.test.ts`) -> DB Complexity: **368**
- `describe` (@ `packages/wrangler/src/__tests__/pipelines.test.ts`) -> DB Complexity: **343**
- `describe` (@ `packages/wrangler/src/__tests__/deploy/bindings.test.ts`) -> DB Complexity: **335**
- `describe` (@ `packages/wrangler/src/__tests__/dev.test.ts`) -> DB Complexity: **313**
- `describe` (@ `packages/wrangler/src/__tests__/pages/deploy.test.ts`) -> DB Complexity: **265**
- `describe` (@ `packages/wrangler/src/__tests__/pages/deploy.test.ts`) -> DB Complexity: **246**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/workers-playground` | 12 | 5106.17 | 11.35% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/bindings` | 8 | 5071.28 | 4.03% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/dot-env` | 8 | 5055.73 | 3.75% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/sensitive-files` | 7 | 5054.27 | 3.72% | 0.0% |
| `fixtures/nodejs-hybrid-app` | 5 | 5000.05 | 4.78% | 0.0% |
| `fixtures/worker-app` | 4 | 5000.04 | 2.5% | 0.0% |
| `fixtures/pages-workerjs-app` | 3 | 5000.02 | 1.67% | 0.0% |
| `packages/wrangler/src/__tests__` | 74 | 1360.97 | 11.97% | 1.59% |
| `packages/format-errors/src` | 3 | 719.98 | 54.67% | 7.07% |
| `packages/wrangler/src/__tests__/deploy` | 21 | 613.27 | 16.07% | 4.76% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `fixtures/get-platform-proxy-remote-bindings/remote-worker.js` -> **100.0%** Exposure
- `fixtures/get-platform-proxy-remote-bindings/remote-worker.staging.js` -> **100.0%** Exposure
- `fixtures/isomorphic-random-example/src/default.js` -> **100.0%** Exposure
- `fixtures/miniflare-node-test/src/index-with-imports.js` -> **100.0%** Exposure
- `fixtures/pages-dev-proxy-with-script/_worker.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/create-cloudflare/templates/scheduled/js/src/index.js` -> **100.0%** Exposure
- `packages/format-errors/src/Youch.js` -> **100.0%** Exposure
- `packages/format-errors/src/impl/partition.js` -> **100.0%** Exposure
- `packages/vite-plugin-cloudflare/playground/module-resolution/packages/requires/ext.js` -> **100.0%** Exposure
- `packages/wrangler/scripts/node-options-for-tests.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/wrangler/src/__tests__/pages/deploy.test.ts` -> **1** Orphaned Functions | **65** Duplicates
- `packages/workers-shared/utils/tests/parseRedirects.valid.test.ts` -> **0** Orphaned Functions | **54** Duplicates
- `packages/quick-edit-extension/vscode.d.ts` -> **16** Orphaned Functions | **24** Duplicates
- `packages/miniflare/src/workers/browser-rendering/binding.worker.ts` -> **1** Orphaned Functions | **32** Duplicates
- `packages/wrangler/src/__tests__/type-generation.test.ts` -> **0** Orphaned Functions | **30** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/wrangler/src/__tests__/helpers/mock-upload-worker.ts`** -> AI Confidence: **99.39%**
2. **`packages/wrangler/src/api/dev.ts`** -> AI Confidence: **99.39%**
3. **`packages/wrangler/src/containers/config.ts`** -> AI Confidence: **99.39%**
4. **`packages/local-explorer-ui/src/components/workflows/StepRow.tsx`** -> AI Confidence: **99.34%**
5. **`packages/wrangler/src/complete.ts`** -> AI Confidence: **99.34%**
6. **`packages/wrangler/src/__tests__/test-old-node-version.js`** -> AI Confidence: **99.32%**
7. **`packages/workers-shared/utils/configuration/parseHeaders.ts`** -> AI Confidence: **99.32%**
8. **`packages/workers-utils/src/map-worker-metadata-bindings.ts`** -> AI Confidence: **99.32%**
9. **`tools/deployments/validate-catalog-usage.ts`** -> AI Confidence: **99.32%**
10. **`packages/cli/interactive.ts`** -> AI Confidence: **99.31%**
11. **`packages/create-cloudflare/src/help.ts`** -> AI Confidence: **99.31%**
12. **`packages/create-cloudflare/src/metrics.ts`** -> AI Confidence: **99.31%**
13. **`packages/local-explorer-ui/src/components/Sidebar.tsx`** -> AI Confidence: **99.31%**
14. **`packages/local-explorer-ui/src/components/studio/Table/Result/index.tsx`** -> AI Confidence: **99.31%**
15. **`packages/local-explorer-ui/src/routes/kv/$namespaceId.tsx`** -> AI Confidence: **99.31%**
16. **`packages/local-explorer-ui/src/routes/r2/$bucketName/index.tsx`** -> AI Confidence: **99.31%**
17. **`packages/local-explorer-ui/src/routes/r2/$bucketName/object.$.tsx`** -> AI Confidence: **99.31%**
18. **`packages/local-explorer-ui/src/routes/workflows/$workflowName/$instanceId.tsx`** -> AI Confidence: **99.31%**
19. **`packages/local-explorer-ui/src/routes/workflows/$workflowName/index.tsx`** -> AI Confidence: **99.31%**
20. **`packages/miniflare/src/http/fetch.ts`** -> AI Confidence: **99.31%**
21. **`packages/miniflare/src/index.ts`** -> AI Confidence: **99.31%**
22. **`packages/miniflare/src/plugins/core/errors/index.ts`** -> AI Confidence: **99.31%**
23. **`packages/miniflare/src/plugins/core/explorer.ts`** -> AI Confidence: **99.31%**
24. **`packages/miniflare/src/plugins/core/proxy/fetch-sync.ts`** -> AI Confidence: **99.31%**
25. **`packages/miniflare/src/shared/dev-registry.worker.ts`** -> AI Confidence: **99.31%**
26. **`packages/miniflare/src/workers/cache/cache.worker.ts`** -> AI Confidence: **99.31%**
27. **`packages/miniflare/src/workers/core/entry.worker.ts`** -> AI Confidence: **99.31%**
28. **`packages/miniflare/src/workers/email/send_email.worker.ts`** -> AI Confidence: **99.31%**
29. **`packages/miniflare/src/workers/r2/bucket.worker.ts`** -> AI Confidence: **99.31%**
30. **`packages/miniflare/src/workers/r2/validator.worker.ts`** -> AI Confidence: **99.31%**
31. **`packages/miniflare/src/workers/shared/object.worker.ts`** -> AI Confidence: **99.31%**
32. **`packages/playground-preview-worker/src/index.ts`** -> AI Confidence: **99.31%**
33. **`packages/vite-plugin-cloudflare/src/plugin-config.ts`** -> AI Confidence: **99.31%**
34. **`packages/vitest-pool-workers/src/pool/index.ts`** -> AI Confidence: **99.31%**
35. **`packages/workers-playground/src/QuickEditor/DevtoolsIframe.tsx`** -> AI Confidence: **99.31%**
36. **`packages/workers-playground/src/QuickEditor/PreviewTab/PreviewTab.tsx`** -> AI Confidence: **99.31%**
37. **`packages/workers-shared/asset-worker/src/worker.ts`** -> AI Confidence: **99.31%**
38. **`packages/workers-utils/src/config/config-helpers.ts`** -> AI Confidence: **99.31%**
39. **`packages/workers-utils/src/config/validation.ts`** -> AI Confidence: **99.31%**
40. **`packages/workers-utils/src/construct-wrangler-config.ts`** -> AI Confidence: **99.31%**
41. **`packages/wrangler/src/__tests__/pipelines-setup.test.ts`** -> AI Confidence: **99.31%**
42. **`packages/wrangler/src/__tests__/versions/versions.deploy.test.ts`** -> AI Confidence: **99.31%**
43. **`packages/wrangler/src/ai-search/create.ts`** -> AI Confidence: **99.31%**
44. **`packages/wrangler/src/api/pages/deploy.ts`** -> AI Confidence: **99.31%**
45. **`packages/wrangler/src/api/startDevWorker/BundlerController.ts`** -> AI Confidence: **99.31%**
46. **`packages/wrangler/src/api/startDevWorker/ConfigController.ts`** -> AI Confidence: **99.31%**
47. **`packages/wrangler/src/api/startDevWorker/LocalRuntimeController.ts`** -> AI Confidence: **99.31%**
48. **`packages/wrangler/src/api/startDevWorker/ProxyController.ts`** -> AI Confidence: **99.31%**
49. **`packages/wrangler/src/api/startDevWorker/types.ts`** -> AI Confidence: **99.31%**
50. **`packages/wrangler/src/autoconfig/frameworks/utils/vite-config.ts`** -> AI Confidence: **99.31%**
51. **`packages/wrangler/src/autoconfig/run.ts`** -> AI Confidence: **99.31%**
52. **`packages/wrangler/src/cfetch/index.ts`** -> AI Confidence: **99.31%**
53. **`packages/wrangler/src/cloudchamber/cli/deployments.ts`** -> AI Confidence: **99.31%**
54. **`packages/wrangler/src/config/index.ts`** -> AI Confidence: **99.31%**
55. **`packages/wrangler/src/containers/deploy.ts`** -> AI Confidence: **99.31%**
56. **`packages/wrangler/src/containers/instances.ts`** -> AI Confidence: **99.31%**
57. **`packages/wrangler/src/containers/list.ts`** -> AI Confidence: **99.31%**
58. **`packages/wrangler/src/containers/registries.ts`** -> AI Confidence: **99.31%**
59. **`packages/wrangler/src/core/handle-errors.ts`** -> AI Confidence: **99.31%**
60. **`packages/wrangler/src/core/register-yargs-command.ts`** -> AI Confidence: **99.31%**
61. **`packages/wrangler/src/d1/execute.ts`** -> AI Confidence: **99.31%**
62. **`packages/wrangler/src/d1/info.ts`** -> AI Confidence: **99.31%**
63. **`packages/wrangler/src/d1/migrations/apply.ts`** -> AI Confidence: **99.31%**
64. **`packages/wrangler/src/deployment-bundle/create-worker-upload-form.ts`** -> AI Confidence: **99.31%**
65. **`packages/wrangler/src/deployment-bundle/entry.ts`** -> AI Confidence: **99.31%**
66. **`packages/wrangler/src/deployment-bundle/run-custom-build.ts`** -> AI Confidence: **99.31%**
67. **`packages/wrangler/src/deployments.ts`** -> AI Confidence: **99.31%**
68. **`packages/wrangler/src/dev.ts`** -> AI Confidence: **99.31%**
69. **`packages/wrangler/src/dev/start-dev.ts`** -> AI Confidence: **99.31%**
70. **`packages/wrangler/src/pages/build.ts`** -> AI Confidence: **99.31%**
71. **`packages/wrangler/src/pages/deploy.ts`** -> AI Confidence: **99.31%**
72. **`packages/wrangler/src/pages/deployment-tails.ts`** -> AI Confidence: **99.31%**
73. **`packages/wrangler/src/pages/dev.ts`** -> AI Confidence: **99.31%**
74. **`packages/wrangler/src/pages/download-config.ts`** -> AI Confidence: **99.31%**
75. **`packages/wrangler/src/pages/functions/buildWorker.ts`** -> AI Confidence: **99.31%**
76. **`packages/wrangler/src/pages/functions/filepath-routing.ts`** -> AI Confidence: **99.31%**
77. **`packages/wrangler/src/pages/projects.ts`** -> AI Confidence: **99.31%**
78. **`packages/wrangler/src/pipelines/cli/create.ts`** -> AI Confidence: **99.31%**
79. **`packages/wrangler/src/pipelines/cli/sinks/create.ts`** -> AI Confidence: **99.31%**
80. **`packages/wrangler/src/pipelines/cli/streams/create.ts`** -> AI Confidence: **99.31%**
81. **`packages/wrangler/src/r2/catalog.ts`** -> AI Confidence: **99.31%**
82. **`packages/wrangler/src/r2/lifecycle.ts`** -> AI Confidence: **99.31%**
83. **`packages/wrangler/src/r2/lock.ts`** -> AI Confidence: **99.31%**
84. **`packages/wrangler/src/r2/sql.ts`** -> AI Confidence: **99.31%**
85. **`packages/wrangler/src/secret/index.ts`** -> AI Confidence: **99.31%**
86. **`packages/wrangler/src/sites.ts`** -> AI Confidence: **99.31%**
87. **`packages/wrangler/src/triggers/deploy.ts`** -> AI Confidence: **99.31%**
88. **`packages/wrangler/src/tunnel/cloudflared.ts`** -> AI Confidence: **99.31%**
89. **`packages/wrangler/src/type-generation/helpers.ts`** -> AI Confidence: **99.31%**
90. **`packages/wrangler/src/type-generation/index.ts`** -> AI Confidence: **99.31%**
91. **`packages/wrangler/src/user/user.ts`** -> AI Confidence: **99.31%**
92. **`packages/wrangler/src/utils/print-bindings.ts`** -> AI Confidence: **99.31%**
93. **`packages/wrangler/src/vectorize/insert.ts`** -> AI Confidence: **99.31%**
94. **`packages/wrangler/src/versions/deploy.ts`** -> AI Confidence: **99.31%**
95. **`packages/wrangler/src/versions/upload.ts`** -> AI Confidence: **99.31%**
96. **`packages/wrangler/src/workflows/commands/instances/describe.ts`** -> AI Confidence: **99.31%**
97. **`packages/wrangler/src/workflows/commands/instances/list.ts`** -> AI Confidence: **99.31%**
98. **`packages/vite-plugin-cloudflare/playground/module-resolution/packages/requires/hello.js`** -> AI Confidence: **99.29%**
99. **`packages/vite-plugin-cloudflare/playground/module-resolution/packages/requires/index.js`** -> AI Confidence: **99.29%**
100. **`packages/vite-plugin-cloudflare/playground/module-resolution/packages/requires/no-ext.js`** -> AI Confidence: **99.29%**
101. **`packages/vite-plugin-cloudflare/playground/module-resolution/packages/requires/world.cjs`** -> AI Confidence: **99.29%**
102. **`packages/wrangler/scripts/node-options-for-tests.js`** -> AI Confidence: **99.29%**
103. **`packages/wrangler/templates/checked-fetch.js`** -> AI Confidence: **99.29%**
104. **`packages/containers-shared/src/client/core/ApiRequestOptions.ts`** -> AI Confidence: **99.29%**
105. **`packages/create-cloudflare/src/event.ts`** -> AI Confidence: **99.29%**
106. **`packages/local-explorer-ui/src/components/studio/Table/index.tsx`** -> AI Confidence: **99.29%**
107. **`packages/miniflare/src/workers/node.d.ts`** -> AI Confidence: **99.29%**
108. **`packages/unenv-preset/src/runtime/polyfill/performance.ts`** -> AI Confidence: **99.29%**
109. **`packages/vitest-pool-workers/src/worker/node/console.ts`** -> AI Confidence: **99.29%**
110. **`packages/workers-shared/asset-worker/src/analytics.ts`** -> AI Confidence: **99.29%**
111. **`packages/workers-shared/asset-worker/src/configuration.ts`** -> AI Confidence: **99.29%**
112. **`packages/workers-shared/router-worker/src/analytics.ts`** -> AI Confidence: **99.29%**
113. **`packages/workers-shared/utils/configuration/parseRedirects.ts`** -> AI Confidence: **99.29%**
114. **`packages/wrangler/src/ai-search/types.ts`** -> AI Confidence: **99.29%**
115. **`packages/wrangler/templates/pages-dev-util.ts`** -> AI Confidence: **99.29%**
116. **`tools/deployments/alert-on-error.ts`** -> AI Confidence: **99.29%**
117. **`tools/deployments/validate-pr-description.ts`** -> AI Confidence: **99.29%**
118. **`packages/create-cloudflare/src/workers.ts`** -> AI Confidence: **99.25%**
119. **`packages/create-cloudflare/e2e/helpers/framework-helpers.ts`** -> AI Confidence: **99.24%**
120. **`packages/create-cloudflare/e2e/helpers/index.ts`** -> AI Confidence: **99.24%**
121. **`packages/create-cloudflare/src/deploy.ts`** -> AI Confidence: **99.24%**
122. **`packages/create-cloudflare/templates/vue/workers/c3.ts`** -> AI Confidence: **99.24%**
123. **`packages/local-explorer-ui/src/components/studio/Table/Result/EditableCell.tsx`** -> AI Confidence: **99.24%**
124. **`packages/local-explorer-ui/src/components/studio/Tabs/TableExplorer.tsx`** -> AI Confidence: **99.24%**
125. **`packages/local-explorer-ui/src/routeTree.gen.ts`** -> AI Confidence: **99.24%**
126. **`packages/miniflare/src/plugins/core/index.ts`** -> AI Confidence: **99.24%**
127. **`packages/miniflare/src/runtime/index.ts`** -> AI Confidence: **99.24%**
128. **`packages/miniflare/src/shared/external-service.ts`** -> AI Confidence: **99.24%**
129. **`packages/vite-plugin-cloudflare/e2e/helpers.ts`** -> AI Confidence: **99.24%**
130. **`packages/vite-plugin-cloudflare/src/plugins/dev.ts`** -> AI Confidence: **99.24%**
131. **`packages/vite-plugin-cloudflare/src/plugins/output-config.ts`** -> AI Confidence: **99.24%**
132. **`packages/vite-plugin-cloudflare/src/websockets.ts`** -> AI Confidence: **99.24%**
133. **`packages/vitest-pool-workers/src/worker/index.ts`** -> AI Confidence: **99.24%**
134. **`packages/workers-shared/router-worker/src/worker.ts`** -> AI Confidence: **99.24%**
135. **`packages/workflows-shared/src/context.ts`** -> AI Confidence: **99.24%**
136. **`packages/wrangler/e2e/helpers/command.ts`** -> AI Confidence: **99.24%**
137. **`packages/wrangler/src/__tests__/autoconfig/details/confirm-auto-config-details.test.ts`** -> AI Confidence: **99.24%**
138. **`packages/wrangler/src/__tests__/delete.test.ts`** -> AI Confidence: **99.24%**
139. **`packages/wrangler/src/__tests__/pages/pages-download-config.test.ts`** -> AI Confidence: **99.24%**
140. **`packages/wrangler/src/api/integrations/platform/index.ts`** -> AI Confidence: **99.24%**
141. **`packages/wrangler/src/api/startDevWorker/DevEnv.ts`** -> AI Confidence: **99.24%**
142. **`packages/wrangler/src/api/startDevWorker/MultiworkerRuntimeController.ts`** -> AI Confidence: **99.24%**
143. **`packages/wrangler/src/api/startDevWorker/RemoteRuntimeController.ts`** -> AI Confidence: **99.24%**
144. **`packages/wrangler/src/autoconfig/details/framework-detection.ts`** -> AI Confidence: **99.24%**
145. **`packages/wrangler/src/autoconfig/details/index.ts`** -> AI Confidence: **99.24%**
146. **`packages/wrangler/src/autoconfig/frameworks/astro.ts`** -> AI Confidence: **99.24%**
147. **`packages/wrangler/src/cloudchamber/common.ts`** -> AI Confidence: **99.24%**
148. **`packages/wrangler/src/cloudchamber/ssh/ssh.ts`** -> AI Confidence: **99.24%**
149. **`packages/wrangler/src/d1/create.ts`** -> AI Confidence: **99.24%**
150. **`packages/wrangler/src/d1/migrations/list.ts`** -> AI Confidence: **99.24%**
151. **`packages/wrangler/src/deploy/deploy.ts`** -> AI Confidence: **99.24%**
152. **`packages/wrangler/src/deploy/index.ts`** -> AI Confidence: **99.24%**
153. **`packages/wrangler/src/deployment-bundle/bindings.ts`** -> AI Confidence: **99.24%**
154. **`packages/wrangler/src/deployment-bundle/bundle.ts`** -> AI Confidence: **99.24%**
155. **`packages/wrangler/src/dev/miniflare/index.ts`** -> AI Confidence: **99.24%**
156. **`packages/wrangler/src/dev/use-esbuild.ts`** -> AI Confidence: **99.24%**
157. **`packages/wrangler/src/pages/secret/index.ts`** -> AI Confidence: **99.24%**
158. **`packages/wrangler/src/r2/helpers/object.ts`** -> AI Confidence: **99.24%**
159. **`packages/wrangler/src/r2/object.ts`** -> AI Confidence: **99.24%**
160. **`packages/wrangler/src/vectorize/create.ts`** -> AI Confidence: **99.24%**
161. **`packages/wrangler/src/vectorize/upsert.ts`** -> AI Confidence: **99.24%**
162. **`packages/wrangler/src/versions/rollback/index.ts`** -> AI Confidence: **99.24%**
163. **`packages/wrangler/src/versions/view.ts`** -> AI Confidence: **99.24%**
164. **`packages/create-cloudflare/src/helpers/args.ts`** -> AI Confidence: **99.23%**
165. **`packages/create-cloudflare/src/helpers/packageManagers.ts`** -> AI Confidence: **99.23%**
166. **`packages/create-cloudflare/src/pages.ts`** -> AI Confidence: **99.23%**
167. **`packages/local-explorer-ui/src/components/studio/Table/SchemaEditor/ConstraintListEditor.tsx`** -> AI Confidence: **99.23%**
168. **`packages/miniflare/src/shared/dev-registry.ts`** -> AI Confidence: **99.23%**
169. **`packages/vite-plugin-cloudflare/src/build.ts`** -> AI Confidence: **99.23%**
170. **`packages/vite-plugin-cloudflare/src/export-types.ts`** -> AI Confidence: **99.23%**
171. **`packages/vitest-pool-workers/src/pool/config.ts`** -> AI Confidence: **99.23%**
172. **`packages/workers-shared/asset-worker/src/handler.ts`** -> AI Confidence: **99.23%**
173. **`packages/wrangler/src/__tests__/update-config-file.test.ts`** -> AI Confidence: **99.23%**
174. **`packages/wrangler/src/autoconfig/frameworks/framework-class.ts`** -> AI Confidence: **99.23%**
175. **`packages/wrangler/src/logger.ts`** -> AI Confidence: **99.23%**
176. **`packages/wrangler/src/queues/cli/commands/create.ts`** -> AI Confidence: **99.23%**
177. **`packages/wrangler/src/r2/cors.ts`** -> AI Confidence: **99.23%**
178. **`packages/wrangler/src/type-generation/pipeline-schema.ts`** -> AI Confidence: **99.23%**
179. **`packages/wrangler/src/user/whoami.ts`** -> AI Confidence: **99.23%**
180. **`packages/wrangler/src/versions/list.ts`** -> AI Confidence: **99.23%**
181. **`packages/cli/packages.ts`** -> AI Confidence: **99.22%**
182. **`packages/wrangler/src/d1/insights.ts`** -> AI Confidence: **99.22%**
183. **`packages/local-explorer-ui/src/components/studio/Table/State/Helpers.tsx`** -> AI Confidence: **99.2%**
184. **`packages/miniflare/src/workers/kv/validator.worker.ts`** -> AI Confidence: **99.2%**
185. **`fixtures/no-bundle-import/src/index.js`** -> AI Confidence: **99.18%**
186. **`packages/containers-shared/src/client/models/Application.ts`** -> AI Confidence: **99.18%**
187. **`packages/containers-shared/src/client/models/CreateApplicationRequest.ts`** -> AI Confidence: **99.18%**
188. **`packages/containers-shared/src/client/models/DeploymentV2.ts`** -> AI Confidence: **99.18%**
189. **`packages/containers-shared/src/images.ts`** -> AI Confidence: **99.18%**
190. **`packages/create-cloudflare/e2e/helpers/workers-helpers.ts`** -> AI Confidence: **99.18%**
191. **`packages/create-cloudflare/templates/analog/c3.ts`** -> AI Confidence: **99.18%**
192. **`packages/create-cloudflare/templates/angular/pages/c3.ts`** -> AI Confidence: **99.18%**
193. **`packages/create-cloudflare/templates/astro/pages/c3.ts`** -> AI Confidence: **99.18%**
194. **`packages/create-cloudflare/templates/astro/workers/c3.ts`** -> AI Confidence: **99.18%**
195. **`packages/create-cloudflare/templates/nuxt/pages/c3.ts`** -> AI Confidence: **99.18%**
196. **`packages/create-cloudflare/templates/nuxt/workers/c3.ts`** -> AI Confidence: **99.18%**
197. **`packages/create-cloudflare/templates/pre-existing/c3.ts`** -> AI Confidence: **99.18%**
198. **`packages/create-cloudflare/templates/qwik/pages/c3.ts`** -> AI Confidence: **99.18%**
199. **`packages/create-cloudflare/templates/qwik/workers/c3.ts`** -> AI Confidence: **99.18%**
200. **`packages/create-cloudflare/templates/solid/c3.ts`** -> AI Confidence: **99.18%**
201. **`packages/create-cloudflare/templates/svelte/workers/c3.ts`** -> AI Confidence: **99.18%**
202. **`packages/local-explorer-ui/src/components/studio/SQLWhereEditor.tsx`** -> AI Confidence: **99.18%**
203. **`packages/local-explorer-ui/src/components/studio/Table/SchemaEditor/index.tsx`** -> AI Confidence: **99.18%**
204. **`packages/local-explorer-ui/src/routes/d1/$databaseId.tsx`** -> AI Confidence: **99.18%**
205. **`packages/miniflare/src/plugins/assets/index.ts`** -> AI Confidence: **99.18%**
206. **`packages/miniflare/src/plugins/browser-rendering/index.ts`** -> AI Confidence: **99.18%**
207. **`packages/miniflare/src/plugins/cache/index.ts`** -> AI Confidence: **99.18%**
208. **`packages/miniflare/src/plugins/hello-world/index.ts`** -> AI Confidence: **99.18%**
209. **`packages/miniflare/src/plugins/kv/sites.ts`** -> AI Confidence: **99.18%**
210. **`packages/miniflare/src/plugins/workflows/index.ts`** -> AI Confidence: **99.18%**
211. **`packages/vite-plugin-cloudflare/src/context.ts`** -> AI Confidence: **99.18%**
212. **`packages/workers-playground/src/QuickEditor/QuickEditor.tsx`** -> AI Confidence: **99.18%**
213. **`packages/workers-playground/src/QuickEditor/ToolsPane.tsx`** -> AI Confidence: **99.18%**
214. **`packages/workers-playground/src/QuickEditor/TopBar.tsx`** -> AI Confidence: **99.18%**
215. **`packages/workers-playground/src/main.tsx`** -> AI Confidence: **99.18%**
216. **`packages/wrangler/src/__tests__/autoconfig/details/framework-detection/pages-project-detection.test.ts`** -> AI Confidence: **99.18%**
217. **`packages/wrangler/src/__tests__/autoconfig/details/get-details-for-auto-config.test.ts`** -> AI Confidence: **99.18%**
218. **`packages/wrangler/src/__tests__/cloudchamber/list.test.ts`** -> AI Confidence: **99.18%**
219. **`packages/wrangler/src/__tests__/containers/instances.test.ts`** -> AI Confidence: **99.18%**
220. **`packages/wrangler/src/__tests__/containers/push.test.ts`** -> AI Confidence: **99.18%**
221. **`packages/wrangler/src/__tests__/containers/registries.test.ts`** -> AI Confidence: **99.18%**
222. **`packages/wrangler/src/__tests__/d1/create.test.ts`** -> AI Confidence: **99.18%**
223. **`packages/wrangler/src/__tests__/deploy/entry-points.test.ts`** -> AI Confidence: **99.18%**
224. **`packages/wrangler/src/__tests__/deploy/formats.test.ts`** -> AI Confidence: **99.18%**
225. **`packages/wrangler/src/__tests__/deploy/routes.test.ts`** -> AI Confidence: **99.18%**
226. **`packages/wrangler/src/__tests__/friendly-validator-errors.test.ts`** -> AI Confidence: **99.18%**
227. **`packages/wrangler/src/__tests__/helpers/msw/index.ts`** -> AI Confidence: **99.18%**
228. **`packages/wrangler/src/__tests__/hyperdrive.test.ts`** -> AI Confidence: **99.18%**
229. **`packages/wrangler/src/__tests__/kv/help.test.ts`** -> AI Confidence: **99.18%**
230. **`packages/wrangler/src/__tests__/kv/key.test.ts`** -> AI Confidence: **99.18%**
231. **`packages/wrangler/src/__tests__/match-tag.test.ts`** -> AI Confidence: **99.18%**
232. **`packages/wrangler/src/__tests__/navigator-user-agent.test.ts`** -> AI Confidence: **99.18%**
233. **`packages/wrangler/src/__tests__/pages/functions-build.test.ts`** -> AI Confidence: **99.18%**
234. **`packages/wrangler/src/__tests__/pages/project-validate.test.ts`** -> AI Confidence: **99.18%**
235. **`packages/wrangler/src/__tests__/provision.test.ts`** -> AI Confidence: **99.18%**
236. **`packages/wrangler/src/__tests__/queues/queues.test.ts`** -> AI Confidence: **99.18%**
237. **`packages/wrangler/src/__tests__/rollback.test.ts`** -> AI Confidence: **99.18%**
238. **`packages/wrangler/src/__tests__/versions/secrets/delete.test.ts`** -> AI Confidence: **99.18%**
239. **`packages/wrangler/src/__tests__/versions/secrets/put.test.ts`** -> AI Confidence: **99.18%**
240. **`packages/wrangler/src/api/remoteBindings/index.ts`** -> AI Confidence: **99.18%**
241. **`packages/wrangler/src/autoconfig/frameworks/angular.ts`** -> AI Confidence: **99.18%**
242. **`packages/wrangler/src/autoconfig/frameworks/qwik.ts`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `packages/wrangler/e2e/unenv-preset/worker/index.ts` -> **1.1178%** Exposure
- `packages/wrangler/src/__tests__/api/startDevWorker/LocalRuntimeController.test.ts` -> **0.0066%** Exposure
- `packages/create-cloudflare/e2e/helpers/constants.ts` -> **0.0004%** Exposure
### Exploit Generation Surface
- `packages/miniflare/src/index.ts` -> **100.0%** Exposure
- `packages/miniflare/src/plugins/core/proxy/client.ts` -> **100.0%** Exposure
- `packages/miniflare/src/shared/dev-registry.worker.ts` -> **100.0%** Exposure
- `packages/miniflare/src/shared/external-service.ts` -> **100.0%** Exposure
- `packages/miniflare/src/workers/browser-rendering/binding.worker.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `lint-turbo.mjs` -> **100.0%** Exposure
- `packages/wrangler/bin/wrangler.js` -> **100.0%** Exposure
- `packages/create-cloudflare/src/__tests__/check-node.test.ts` -> **100.0%** Exposure
- `packages/local-explorer-ui/src/types/studio.ts` -> **100.0%** Exposure
- `packages/miniflare/src/index.ts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `packages/vite-plugin-cloudflare/playground/node-compat/worker-crypto/index.ts` -> **99.9946%** Exposure
- `packages/miniflare/src/http/cert.ts` -> **99.9898%** Exposure
- `packages/wrangler/src/cloudchamber/ssh/validate.ts` -> **99.9257%** Exposure
- `packages/wrangler/src/__tests__/containers/deploy.test.ts` -> **97.5612%** Exposure
- `fixtures/nodejs-hybrid-app/src/index.ts` -> **96.9895%** Exposure
### Algorithmic DoS Exposure
- `packages/create-cloudflare/templates/react/workers/js/src/App.jsx` -> **100.0%** Exposure
- `packages/create-cloudflare/templates/react/workers/ts/src/App.tsx` -> **100.0%** Exposure
- `packages/devprod-status-bot/src/index.ts` -> **100.0%** Exposure
- `packages/miniflare/src/plugins/core/index.ts` -> **100.0%** Exposure
- `packages/miniflare/src/shared/external-service.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `37` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `27` endpoints documented but missing from code.
- **Known Shadow Routes:** `GET /test`, `GET /v8/artifacts/{var}`, `POST /api/d1/database/{var}/raw`, `GET /api/storage/kv/namespaces`, `POST /api/workers/durable_objects/namespaces/{var}/query`

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4397` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/miniflare/src/workers/browser-rendering/binding.worker.ts` (TYPESCRIPT) -> Cumulative Risk: **895.67**
- **Archetype:** `file_cluster_4` (Distance: 11.897 IQR)
- **Magnitude:** 61.57 | **LOC:** 579 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Spec Match (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `forwardClose` (Impact: 19.6), `sessionId` (Impact: 14.9), `scheduleStatusCheck` (Impact: 12.6)

### 2. `packages/workflows-shared/src/binding.ts` (TYPESCRIPT) -> Cumulative Risk: **795.16**
- **Archetype:** `file_cluster_4` (Distance: 13.407 IQR)
- **Magnitude:** 47.93 | **LOC:** 294 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `restart` (Impact: 16.7), `pause` (Impact: 16.5), `terminate` (Impact: 16.5)

### 3. `packages/miniflare/src/workers/kv/namespace.worker.ts` (TYPESCRIPT) -> Cumulative Risk: **783.24**
- **Archetype:** `file_cluster_4` (Distance: 11.934 IQR)
- **Magnitude:** 35.86 | **LOC:** 318 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.9997%), Cognitive Load (99.6176%)
- **Heaviest Functions:** `get` (Impact: 83.6), `put` (Impact: 75.9), `processKeyValue` (Impact: 31.9)

### 4. `packages/miniflare/src/workers/workflows/wrapped-binding.worker.ts` (TYPESCRIPT) -> Cumulative Risk: **762.93**
- **Archetype:** `file_cluster_4` (Distance: 12.608 IQR)
- **Magnitude:** 40.36 | **LOC:** 114 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9743%)
- **Heaviest Functions:** `create` (Impact: 10.2), `unsafeWaitForStepResult` (Impact: 8.3), `unsafeAbort` (Impact: 7.1)

### 5. `packages/miniflare/src/workers/core/entry.worker.ts` (TYPESCRIPT) -> Cumulative Risk: **760.96**
- **Archetype:** `file_cluster_13` (Distance: 11.727 IQR)
- **Magnitude:** 30.08 | **LOC:** 577 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.7892%), Logic Bomb (99.2228%), State Flux (95.6553%)
- **Heaviest Functions:** `fetch` (Impact: 192.4), `maybeLogRequest` (Impact: 16.5), `colourFromHTTPStatus` (Impact: 12.3)

### 6. `packages/vite-plugin-cloudflare/src/plugins/nodejs-compat.ts` (TYPESCRIPT) -> Cumulative Risk: **752.4**
- **Archetype:** `file_cluster_4` (Distance: 10.727 IQR)
- **Magnitude:** 11.97 | **LOC:** 225 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.927%), Verification (80.0%)
- **Heaviest Functions:** `exitCallback` (Impact: 32.0), `applyToEnvironment` (Impact: 20.5), `configEnvironment` (Impact: 9.8)

### 7. `packages/miniflare/src/plugins/core/inspector-proxy/inspector-proxy-controller.ts` (TYPESCRIPT) -> Cumulative Risk: **749.15**
- **Archetype:** `file_cluster_4` (Distance: 10.943 IQR)
- **Magnitude:** 17.86 | **LOC:** 350 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Cognitive Load (91.0512%)
- **Heaviest Functions:** `closeServer` (Impact: 31.6), `createServer` (Impact: 21.9), `getInspectorPort` (Impact: 4.5)

### 8. `packages/wrangler/src/api/startDevWorker/LocalRuntimeController.ts` (TYPESCRIPT) -> Cumulative Risk: **744.1**
- **Archetype:** `file_cluster_13` (Distance: 12.622 IQR)
- **Magnitude:** 44.21 | **LOC:** 488 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Cognitive Load (95.7736%)
- **Heaviest Functions:** `convertToConfigBundle` (Impact: 135.0), `onBundleComplete` (Impact: 119.6), `teardown` (Impact: 25.1)

### 9. `packages/wrangler/src/api/startDevWorker/ProxyController.ts` (TYPESCRIPT) -> Cumulative Risk: **720.12**
- **Archetype:** `file_cluster_4` (Distance: 13.812 IQR)
- **Magnitude:** 70.12 | **LOC:** 673 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `createProxyWorker` (Impact: 422.8), `logReady` (Impact: 7.1), `constructor` (Impact: 2.4)

### 10. `packages/miniflare/src/workers/queues/broker.worker.ts` (TYPESCRIPT) -> Cumulative Risk: **708.13**
- **Archetype:** `file_cluster_8` (Distance: 10.776 IQR)
- **Magnitude:** 14.68 | **LOC:** 421 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Tech Debt (89.9785%)
- **Heaviest Functions:** `formatQueueResponse` (Impact: 16.4), `validateBatchSize` (Impact: 15.0), `serialise` (Impact: 14.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `fixtures/nodejs-hybrid-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/pages-workerjs-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/worker-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/bindings/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/dot-env/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/sensitive-files/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workers-playground/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/no-bundle-import/src/data.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/miniflare/test/fixtures/modules/blobs/data.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/additional-modules/src/modules/bin-example.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workers-shared/asset-worker/fixtures/AssetManifest.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/format-errors/src/Stacktracey.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.584 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.617 IQR)
- **Top Global Matches:** file_cluster_4: 12.584, file_cluster_17: 12.818, file_cluster_8: 12.901
- **Magnitude:** 447.56 | **LOC:** 336 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (90.4343%), Tech Debt (10.719%)
**Top Internal Functions/Classes:**
  * `nixSlashes` (Impact: 306.3 | O(2^N) | DB: 44)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 51`, `args: 39`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 49`, `import: 1`
* *Defense:* `safety: 22`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.358
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` partition
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/lint-config-shared/rules/no-unsafe-command-execution.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.0 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.856 IQR)
- **Top Global Matches:** file_cluster_8: 12.0, file_cluster_17: 12.022, file_cluster_0: 12.246
- **Magnitude:** 321.74 | **LOC:** 269 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (23.7823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isUnsafeChildProcessCall` (Impact: 295.2 | O(2^N) | DB: 8)
    * *Intent:* /** * Check if a node is a binary expression (string concatenation)
  * `isTemplateLiteralWithExpressions` (Impact: 3.6 | O(N^1))
  * `isBinaryExpression` (Impact: 3.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 22`, `args: 9`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 32`, `doc: 6`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` child_process, node:child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/r2/bucket.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.996 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_8: 10.996, file_cluster_1: 11.536, file_cluster_7: 11.598
- **Magnitude:** 298.48 | **LOC:** 4129 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 79
- **Risk Profile:** Cognitive Load (33.6108%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 1432.8 | O(2^N) | DB: 79)
  * `describe` (Impact: 360.9 | O(2^N) | DB: 33)
  * `describe` (Impact: 235.9 | O(2^N) | DB: 68)
  * `describe` (Impact: 127.2 | O(2^N) | DB: 11)
  * `describe` (Impact: 79.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 584`, `args: 714`, `func_start: 696`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `fragile_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `io: 106`, `api: 10`, `concurrency: 399`, `import: 15`
* *Defense:* `safety: 53`, `test: 505`, `sync_locks: 71`, `immutability_locks: 217`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` notification, node:fs, test-helpers, msw, mock-dialogs, mock-account-id, vitest, mock-console...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/format-errors/src/Youch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.859 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.756 IQR)
- **Top Global Matches:** file_cluster_4: 13.859, file_cluster_17: 14.366, file_cluster_13: 14.449
- **Magnitude:** 264.48 | **LOC:** 315 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (49.9058%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_isNode` (Impact: 6.3 | O(N^1))
  * `addLink` (Impact: 6.1 | O(2^N) | DB: 2)
    * *Intent:* /**
  * `_serializeData` (Impact: 5.9 | O(N^1) | DB: 6)
    * *Intent:* /** * Serializes frame to a usable error object. * * @param {Object}
  * `_getDisplayClasses` (Impact: 5.8 | O(N^1) | DB: 2)
  * `toHTML` (Impact: 5.5 | O(N^1) | DB: 9)
    * *Intent:* /** * Serializes stack to Mustache friendly object to * be used within the view. Optionally can pass...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 41`, `args: 28`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 116`, `dead_code: 1`
* *Architecture:* `api: 5`, `concurrency: 79`, `import: 3`
* *Defense:* `safety: 8`, `doc: 40`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.23
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Stacktracey, error.compiled.mustache, mustache
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/lint-config-shared/rules/no-direct-recursive-rm.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.993 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.28 IQR)
- **Top Global Matches:** file_cluster_8: 10.993, file_cluster_7: 11.524, file_cluster_17: 11.559
- **Magnitude:** 176.44 | **LOC:** 236 | **CtrlFlow:** 72.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (17.0489%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkCall` (Impact: 116.5 | O(2^N))
  * `resolveImportSource` (Impact: 30.9 | O(N^1) | DB: 1)
  * `hasRecursiveOption` (Impact: 12.8 | O(N^1))
  * `getScope` (Impact: 10.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 21`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 4`
* *Defense:* `safety: 33`, `doc: 5`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/pages/deploy.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.716 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.146 IQR)
- **Top Global Matches:** file_cluster_8: 10.716, file_cluster_4: 11.216, file_cluster_7: 11.342
- **Magnitude:** 157.48 | **LOC:** 6277 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 265
- **Risk Profile:** Cognitive Load (43.8354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 258.6 | O(2^N) | DB: 265)
  * `describe` (Impact: 206.4 | O(N^3) | DB: 246)
  * `generatedWorkerBundleCheck` (Impact: 30.3 | O(2^N) | DB: 15)
  * `describe` (Impact: 15.4 | O(N^2) | DB: 36)
  * `describe` (Impact: 13.6 | O(N^2) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 622`, `args: 704`, `func_start: 706`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 59`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 65`, `orphaned_logic: 1`
* *Architecture:* `io: 222`, `api: 121`, `concurrency: 639`, `import: 37`
* *Defense:* `safety: 62`, `test: 407`, `immutability_locks: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` smol-toml, node:fs, msw, mock-dialogs, package.json, node:process, test-hello.wasm, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/middleware.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.336 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.605 IQR)
- **Top Global Matches:** file_cluster_4: 11.336, file_cluster_8: 11.817, file_cluster_13: 12.159
- **Magnitude:** 140.99 | **LOC:** 1150 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 368
- **Risk Profile:** Cognitive Load (49.386%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 730.9 | O(2^N) | DB: 368)
  * `seedFs` (Impact: 3.8 | O(N^1) | DB: 3)
    * *Intent:* /* * This file contains inline comments with the word "javascript"
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 334`, `args: 176`, `func_start: 172`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`, `planned_debt: 1`
* *Architecture:* `io: 115`, `api: 24`, `concurrency: 519`, `import: 9`
* *Defense:* `safety: 20`, `test: 69`, `immutability_locks: 134`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` node:fs, run-in-tmp, mock-console, vitest, ts-dedent, startDevWorker, node:path, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workers-utils/src/config/validation.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.269 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.522 IQR)
- **Top Global Matches:** file_cluster_8: 12.269, file_cluster_13: 12.694, file_cluster_7: 12.738
- **Magnitude:** 120.19 | **LOC:** 5390 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 22.7%
- **Algorithmic:** O(N^2) | **DB Complexity:** 181
- **Risk Profile:** Cognitive Load (23.4891%), Tech Debt (13.7076%)
**Top Internal Functions/Classes:**
  * `validateUnsafeSettings` (Impact: 359.5 | O(N^1) | DB: 181)
  * `validateDefines` (Impact: 66.8 | O(N^2) | DB: 9)
  * `applyPythonConfig` (Impact: 62.2 | O(N^1) | DB: 14)
  * `validateVars` (Impact: 56.0 | O(N^2) | DB: 6)
  * `normalizeAndValidateEnvironment` (Impact: 52.6 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 152`, `args: 145`, `func_start: 146`
* *Risk/State:* `state_mutation: 363`, `duplicate_logic: 6`
* *Architecture:* `io: 13`, `api: 5`, `import: 16`
* *Defense:* `safety: 41`, `doc: 18`, `test: 1`, `immutability_locks: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` node:fs, config, fs-helpers, validators, ts-dedent, diagnostics, misc-variables, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/pipelines-setup.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.297 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.875 IQR)
- **Top Global Matches:** file_cluster_8: 10.297, file_cluster_7: 11.011, file_cluster_1: 11.07
- **Magnitude:** 119.35 | **LOC:** 1444 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 101
- **Risk Profile:** Cognitive Load (5.8354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 1110.3 | O(2^N) | DB: 101)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 132`, `args: 331`, `func_start: 326`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 34`, `concurrency: 58`, `import: 12`
* *Defense:* `safety: 25`, `test: 93`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` node:fs, run-in-tmp, mock-console, run-wrangler, mock-account-id, mock-dialogs, msw, vitest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/dev.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.692 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.972 IQR)
- **Top Global Matches:** file_cluster_8: 10.692, file_cluster_4: 10.986, file_cluster_13: 11.211
- **Magnitude:** 107.96 | **LOC:** 2842 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 23.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 313
- **Risk Profile:** Cognitive Load (24.4125%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 792.0 | O(2^N) | DB: 313)
  * `it` (Impact: 4.7 | O(N^1) | DB: 3)
  * `it` (Impact: 4.1 | O(N^1) | DB: 3)
  * `it` (Impact: 3.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 253`, `args: 105`, `func_start: 249`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 13`, `duplicate_logic: 3`
* *Architecture:* `io: 112`, `api: 47`, `concurrency: 189`, `import: 25`
* *Defense:* `safety: 11`, `test: 188`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` node:fs, get-port, mock-console, ConfigController, logger, workers-utils, test-helpers, mock-account-id...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/create-cloudflare/templates/hello-world-workflows/js/src/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.336 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.555 IQR)
- **Top Global Matches:** file_cluster_4: 12.336, file_cluster_13: 13.235, file_cluster_8: 13.412
- **Magnitude:** 106.06 | **LOC:** 130 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (54.9991%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 11.4 | O(N^1) | DB: 7)
    * *Intent:* /** * Welcome to Cloudflare Workers! This is your first Workflows application. * * - Run `npm run de...
  * `fetch` (Impact: 6.7 | O(N^1) | DB: 7)
    * *Intent:* // Define a retry strategy
  * `constructor` (Impact: 1.6 | O(N^1) | DB: 1)
    * *Intent:* /** * Welcome to Cloudflare Workers! This is your first Workflows application. * * - Run `npm run de...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 29`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 66`, `import: 1`
* *Defense:* `doc: 16`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cloudflare:workers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/type-generation/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.826 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.081 IQR)
- **Top Global Matches:** file_cluster_8: 12.826, file_cluster_13: 12.898, file_cluster_17: 13.016
- **Magnitude:** 101.69 | **LOC:** 3520 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (41.5423%), Tech Debt (53.1037%)
**Top Internal Functions/Classes:**
  * `collectCoreBindingsPerEnvironment` (Impact: 299.3 | O(N^1) | DB: 30)
  * `handler` (Impact: 64.5 | O(N^1) | DB: 14)
  * `collectVarsPerEnvironment` (Impact: 41.9 | O(N^1) | DB: 7)
  * `trackBinding` (Impact: 20.4 | O(2^N) | DB: 1)
  * `trackBinding` (Impact: 20.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 468`, `structural_boundaries: 225`, `args: 97`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 298`, `dead_code: 2`, `duplicate_logic: 19`
* *Architecture:* `io: 17`, `api: 7`, `concurrency: 30`, `import: 28`
* *Defense:* `safety: 101`, `doc: 64`, `immutability_locks: 238`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` node:fs, chalk, config, find, logger, helpers, workers-utils, entry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/create-cloudflare/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 99.44 | **LOC:** 4972 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/miniflare/src/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.047 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.392 IQR)
- **Top Global Matches:** file_cluster_13: 12.047, file_cluster_8: 12.257, file_cluster_4: 12.295
- **Magnitude:** 98.47 | **LOC:** 3062 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 21.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (33.7123%), Tech Debt (8.6126%)
**Top Internal Functions/Classes:**
  * `handleLoopback` (Impact: 304.3 | O(2^N) | DB: 21)
    * *Intent:* // Unregister all workers from the dev registry. Note that dispose() // does synchronous cleanup (un...
  * `getRootPath` (Impact: 156.2 | O(2^N) | DB: 22)
  * `handleLoopbackWorkflowStorageDeleteReque` (Impact: 33.5 | O(N^1) | DB: 28)
  * `constructor` (Impact: 30.5 | O(N^1) | DB: 3)
  * `getQueueConsumers` (Impact: 29.3 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 174`, `args: 67`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 94`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 41`, `api: 16`, `concurrency: 84`, `import: 48`
* *Defense:* `safety: 72`, `doc: 13`, `test: 8`, `sync_locks: 3`, `immutability_locks: 143`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.162
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` node:fs, zod, zod-format, dev-registry-types, node:http, node:net, colors, shared...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/vite-plugin-cloudflare/src/workers/runner-worker/index.ts` (TYPESCRIPT) | Magnitude: 28.76 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 295, structural_boundaries: 108, branch: 57, concurrency: 52
- `packages/wrangler/src/utils/useServiceEnvironments.ts` (TYPESCRIPT) | Magnitude: 1.34 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 4, import: 2, branch: 1
- `packages/create-cloudflare/src/workers.ts` (TYPESCRIPT) | Magnitude: 12.29 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 127, branch: 39, structural_boundaries: 39, immutability_locks: 20
- `packages/create-cloudflare/templates/react-router/ts/react-router.config.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 1, safety: 1
- `tools/deployments/validate-fixtures.ts` (TYPESCRIPT) | Magnitude: 3.16 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 52, structural_boundaries: 13, state_mutation: 12, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/wrangler/src/utils/worker-not-found-error.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 8, doc: 6, structural_boundaries: 5, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/vitest-pool-workers/src/worker/durable-objects.ts` (TYPESCRIPT) | Magnitude: 12.39 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 95, branch: 43, structural_boundaries: 34, immutability_locks: 20
- `packages/miniflare/src/workers/shared/remote-bindings-utils.ts` (TYPESCRIPT) | Magnitude: 6.2 | Delta: **0.271 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 60, state_mutation: 18, structural_boundaries: 16, branch: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/miniflare/src/workers/r2/r2Object.worker.ts` (TYPESCRIPT) | Magnitude: 9.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 90, state_mutation: 51, structural_boundaries: 19, immutability_locks: 18
- `fixtures/shared/src/mock-postgres-server.ts` (TYPESCRIPT) | Magnitude: 11.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 118, immutability_locks: 31, structural_boundaries: 30, branch: 26
- `packages/pages-shared/environment-polyfills/miniflare.ts` (TYPESCRIPT) | Magnitude: 0.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 9, structural_boundaries: 7, concurrency: 3, import: 3
- `packages/wrangler/src/tunnel/run.ts` (TYPESCRIPT) | Magnitude: 6.89 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 120, structural_boundaries: 27, branch: 19, args: 16
- `packages/miniflare/src/workers/core/email.ts` (TYPESCRIPT) | Magnitude: 4.16 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 91, structural_boundaries: 29, concurrency: 15, io: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/create-cloudflare/templates/hello-world-durable-object-with-assets/ts/src/index.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 13, indent_tabs: 11, structural_boundaries: 9, concurrency: 5
- `packages/containers-shared/src/client/models/CreateApplicationBadRequest.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 2, branch: 1, safety_bypasses: 1
- `packages/containers-shared/src/client/models/CreateApplicationJobBadRequest.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 2, branch: 1, safety_bypasses: 1
- `packages/containers-shared/src/client/models/CreateDeploymentBadRequest.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 2, branch: 1, safety_bypasses: 1
- `packages/containers-shared/src/client/models/ImageRegistryAlreadyExistsError.ts` (TYPESCRIPT) | Magnitude: 1.77 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 5, doc: 4, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/workers-utils/src/construct-wrangler-config.ts` (TYPESCRIPT) | Magnitude: 9.73 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 118, branch: 34, structural_boundaries: 28, args: 11
- `packages/vite-plugin-cloudflare/playground/importable-env/src/index.ts` (TYPESCRIPT) | Magnitude: 1.2 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 7, args: 3, immutability_locks: 3
- `packages/quick-edit/setup.sh` (SHELL) | Magnitude: 13.76 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 11, safety_bypasses: 6, state_mutation: 6, globals: 4
- `packages/miniflare/src/workers/local-explorer/resources/d1.ts` (TYPESCRIPT) | Magnitude: 10.89 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 136, structural_boundaries: 50, branch: 26, immutability_locks: 26
- `packages/local-explorer-ui/src/drivers/sqlite/generate.ts` (TYPESCRIPT) | Magnitude: 18.66 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 168, branch: 67, state_mutation: 45, safety: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/local-explorer-ui/src/routes/kv/$namespaceId.tsx` (TYPESCRIPT) | Magnitude: 25.23 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 383, branch: 84, structural_boundaries: 76, args: 68
- `packages/local-explorer-ui/src/components/workflows/CopyButton.tsx` (TYPESCRIPT) | Magnitude: 0.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 6, args: 6, ui_framework: 6
- `packages/wrangler/src/core/create-command.ts` (TYPESCRIPT) | Magnitude: 1.51 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 13, api: 7, ui_framework: 6
- `fixtures/vitest-pool-workers-examples/workers-assets/src/index.ts` (TYPESCRIPT) | Magnitude: 2.79 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, branch: 6, structural_boundaries: 6, memory_alloc: 4
- `packages/create-cloudflare/templates/hello-world/ts/src/index.ts` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, api: 2, concurrency: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/wrangler/src/api/startDevWorker/LocalRuntimeController.ts` (TYPESCRIPT) | Magnitude: 44.21 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 304, branch: 98, structural_boundaries: 77, safety: 58
- `packages/wrangler/tsup.config.ts` (TYPESCRIPT) | Magnitude: 3.71 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 51, structural_boundaries: 22, branch: 12, io: 12
- `packages/vitest-pool-workers/src/pool/loopback.ts` (TYPESCRIPT) | Magnitude: 7.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 78, structural_boundaries: 29, branch: 22, concurrency: 16
- `packages/miniflare/src/workers/pipelines/pipeline.worker.ts` (TYPESCRIPT) | Magnitude: 0.51 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, concurrency: 2, branch: 1, args: 1
- `fixtures/vitest-pool-workers-examples/rpc/src/index.ts` (TYPESCRIPT) | Magnitude: 10.75 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 111, structural_boundaries: 40, args: 31, func_start: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/create-cloudflare/templates/hello-world-durable-object-with-assets/py/src/entry.py` (PYTHON) | Magnitude: 20.22 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, doc: 10, indent_spaces: 8, api: 5
- `packages/create-cloudflare/templates/hello-world-durable-object/py/src/entry.py` (PYTHON) | Magnitude: 20.22 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, doc: 10, indent_spaces: 8, api: 5
- `packages/create-cloudflare/templates/hello-world-durable-object-with-assets/js/src/index.js` (JAVASCRIPT) | Magnitude: 13.82 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 15, indent_tabs: 11, structural_boundaries: 9, planned_debt: 5
- `packages/create-cloudflare/templates/hello-world-durable-object/js/src/index.js` (JAVASCRIPT) | Magnitude: 13.82 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 15, indent_tabs: 11, structural_boundaries: 9, planned_debt: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/wrangler/src/utils/error-codes.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, immutability_locks: 2, structural_boundaries: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/wrangler/src/api/dev.ts` (TYPESCRIPT) | Magnitude: 2.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 90, branch: 62, structural_boundaries: 25, import: 11
- `packages/wrangler/src/deploy/open-next.ts` (TYPESCRIPT) | Magnitude: 3.33 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 52, structural_boundaries: 21, safety: 11, branch: 9
- `packages/wrangler/src/__tests__/api/startDevWorker/BundleController.test.ts` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: sec_io: 48, indent_tabs: 36, structural_boundaries: 14, import: 10
- `fixtures/wasm-app/worker/module/index_bg.js` (JAVASCRIPT) | Magnitude: 0.43 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 355, structural_boundaries: 204, state_mutation: 166, func_start: 93
- `fixtures/wasm-app/worker/service-worker-module/index_bg.js` (JAVASCRIPT) | Magnitude: 0.43 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 355, structural_boundaries: 204, state_mutation: 166, func_start: 93

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `fixtures/routing-app/functions/index.ts` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 10, safety: 3, structural_boundaries: 2, api: 2
- `packages/vite-plugin-cloudflare/e2e/fixtures/dynamic/src/dynamic.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: sec_high_risk_execution: 3, dead_code: 1
- `packages/wrangler/src/d1/trimmer.ts` (TYPESCRIPT) | Magnitude: 0.42 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, io: 2, api: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/wrangler/src/type-generation/index.ts` -> Churn: **57.81%** | Cog Load: 41.5423% | Debt: 53.1037%
- `packages/wrangler/src/dev/miniflare/index.ts` -> Churn: **56.47%** | Cog Load: 8.7556% | Debt: 94.422%
- `packages/wrangler/src/__tests__/autoconfig/details/get-details-for-auto-config.test.ts` -> Churn: **53.48%** | Cog Load: 58.5832% | Debt: 0.0%
- `packages/wrangler/src/user/user.ts` -> Churn: **53.48%** | Cog Load: 44.4255% | Debt: 62.5854%
- `packages/vite-plugin-cloudflare/src/plugin-config.ts` -> Churn: **51.81%** | Cog Load: 26.8888% | Debt: 57.8569%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/lint-config-shared/rules/no-unsafe-command-execution.mjs` -> **Somhairle MacLeòid** (100.0% isolated ownership) | Magnitude: 321.74
- `packages/lint-config-shared/rules/no-direct-recursive-rm.mjs` -> **Somhairle MacLeòid** (100.0% isolated ownership) | Magnitude: 176.44
- `packages/chrome-devtools-patches/Makefile` -> **Pete Bacon Darwin** (100.0% isolated ownership) | Magnitude: 86.08
- `packages/quick-edit-extension/src/cfs.ts` -> **Dario Piotrowicz** (100.0% isolated ownership) | Magnitude: 59.29

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/wrangler/src/logger.ts` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 99.8789%)
- `packages/wrangler/src/autoconfig/frameworks/astro.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 97.6901%)
- `packages/wrangler/src/autoconfig/frameworks/framework-class.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 96.1505%)
- `packages/cli/interactive.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 20.7734%)
- `packages/create-cloudflare/src/helpers/compatDate.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 97.4999%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/wrangler/src/logger.ts` -> **Severity: 3534.074** (Blast Radius: 58.832 * Doc Risk: 60.0706%)
- `packages/pages-shared/environment-polyfills/miniflare.ts` -> **Severity: 2767.147** (Blast Radius: 43.707 * Doc Risk: 63.3113%)
- `packages/wrangler/src/utils/format-message.ts` -> **Severity: 1936.308** (Blast Radius: 25.414 * Doc Risk: 76.1906%)
- `packages/wrangler/src/utils/log-file.ts` -> **Severity: 1548.222** (Blast Radius: 25.329 * Doc Risk: 61.1245%)
- `packages/wrangler/src/core/create-command.ts` -> **Severity: 1343.793** (Blast Radius: 13.443 * Doc Risk: 99.9623%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
