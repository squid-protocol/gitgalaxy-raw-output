# ARCHITECTURAL_BRIEF: next.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/next.js` |
| **Timestamp** | `2026-08-03T19:55:33.833104+00:00` |
| **Scan Duration** | `36.42s` |
| **Git Branch** | `canary` |
| **Git Commit** | `cc79ef8cda9725008aacc9071aed423a584253d4` |
| **Git Remote** | `https://github.com/vercel/next.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 8179 malicious artifacts.

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
| Total Artifacts | 28412 |
| Analyzed Artifacts (Scanned) | 10600 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17812 |
| Total LOC | 974981 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 37.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2138 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 447 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 3926 | 577841 | 37.0% |
| TYPESCRIPT | 3265 | 180845 | 30.8% |
| RUST | 955 | 184472 | 9.0% |
| PLAINTEXT | 718 | 35 | 6.8% |
| MARKDOWN | 641 | 0 | 6.0% |
| JSON | 441 | 8733 | 4.2% |
| CSS | 418 | 20123 | 3.9% |
| XML | 162 | 48 | 1.5% |
| YAML | 29 | 1671 | 0.3% |
| SHELL | 20 | 674 | 0.2% |
| HTML | 12 | 132 | 0.1% |
| DOCKERFILE | 8 | 274 | 0.1% |
| MAKEFILE | 1 | 27 | 0.0% |
| SQLITE | 1 | 14 | 0.0% |
| BATCH | 1 | 7 | 0.0% |
| PYTHON | 1 | 84 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.697`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 5730 | 54.1% |
| file_cluster_13 | 2081 | 19.6% |
| file_cluster_4 | 424 | 4.0% |
| file_cluster_2 | 421 | 4.0% |
| file_cluster_0 | 210 | 2.0% |
| file_cluster_16 | 205 | 1.9% |
| file_cluster_17 | 69 | 0.7% |
| Unknown | 35 | 0.3% |
| file_cluster_11 | 24 | 0.2% |
| file_cluster_9 | 15 | 0.1% |
| file_cluster_6 | 10 | 0.1% |
| file_cluster_12 | 6 | 0.1% |
| file_cluster_7 | 4 | 0.0% |
| file_cluster_15 | 3 | 0.0% |
| file_cluster_1 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1324 | 12.5% |
| Static: Minified & Vendor Opaque Mass | 38 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17812*

**Composition by Extension & Reason:**
- `.js`: 6162x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 117x Excluded (Saturation: Line 1 exceeds 500 chars), 23x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.tsx`: 4257x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 13 exceeds 500 chars), 2x Excluded (Saturation: Line 17 exceeds 500 chars)
- `.ts`: 2723x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 4x Excluded (Machine-Generated Source Code Signature: 9 LOC)
- `no_extension`: 571x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 21x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.mdx`: 454x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 9 exceeds 500 chars), 3x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.json`: 447x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1294 LOC), 1x Excluded (Static Asset Blob without Intent: 2330 LOC)
- `.css`: 366x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 54 exceeds 500 chars)
- `.snapshot`: 275x Excluded (Unsupported Extension: '.snapshot'), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 274x Excluded (Explicitly Denied Extension: '.png')
- `.map`: 255x Excluded (Unsupported Extension: '.map'), 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jsx`: 221x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 168x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 157x Excluded (Explicitly Denied Extension: '.ico')
- `.mjs`: 129x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 101x Excluded (Unsupported Extension: '.stderr'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 14.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 13.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.7 | 4.7 | 5.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 66.5 | 80.0 | 100.0 |
| Instability Exposure | 0.0 | 8.0 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 99.0 | 3.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 11.7 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` (Hits: 110)
- `packages/next/src/compiled/@edge-runtime/primitives/load.js` (Hits: 110)
- `packages/next-codemod/transforms/middleware-to-proxy.ts` (Hits: 90)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **link.js** (`packages/next/link.js`) — 252 inbound connections
2. **fs.rs** (`turbopack/crates/turbo-tasks-fs/src/embed/fs.rs`) — 169 inbound connections
3. **server.js** (`packages/next/server.js`) — 122 inbound connections
4. **head.js** (`packages/next/head.js`) — 110 inbound connections
5. **router.js** (`packages/next/router.js`) — 103 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`turbopack/crates/turbopack-ecmascript/src/references/mod.rs`) — 216 outbound dependencies
2. **lib.rs** (`turbopack/crates/turbopack-ecmascript/src/lib.rs`) — 149 outbound dependencies
3. **app.rs** (`crates/next-api/src/app.rs`) — 139 outbound dependencies
4. **project.rs** (`crates/next-api/src/project.rs`) — 139 outbound dependencies
5. **mod.rs** (`turbopack/crates/turbo-tasks-backend/src/backend/mod.rs`) — 133 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `renderElement` (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.browser.development.js`) -> Impact: **6055.2** | LOC: 1093
- `renderElement` (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.development.js`) -> Impact: **6055.2** | LOC: 1093
- `renderElement` (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js`) -> Impact: **6055.2** | LOC: 1093
- `renderElement` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js`) -> Impact: **6037.7** | LOC: 1114
- `renderElement` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js`) -> Impact: **6037.7** | LOC: 1114
- `renderElement` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js`) -> Impact: **6037.7** | LOC: 1114
- `pushStartInstance` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js`) -> Impact: **4823.7** | LOC: 1069
- `pushStartInstance` (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js`) -> Impact: **4823.7** | LOC: 1069
- `pushStartInstance` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js`) -> Impact: **4790.6** | LOC: 1071
- `pushStartInstance` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js`) -> Impact: **4790.6** | LOC: 1071

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `assist` (@ `examples/cms-sanity/sanity/plugins/assist.ts`) -> **O(2^N) [Recursive]**
- `getFormattedLinkDiagnosticMessageText` (@ `packages/next/src/lib/typescript/diagnosticFormatter.ts`) -> **O(2^N) [Recursive]**
- `onError` (@ `packages/next/src/server/app-render/app-render.tsx`) -> **O(2^N) [Recursive]**
- `renderElement` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js`) -> **O(2^N) [Recursive]**
- `renderElement` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js`) -> **O(2^N) [Recursive]**
- `renderElement` (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js`) -> **O(2^N) [Recursive]**
- `renderElement` (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.browser.development.js`) -> **O(2^N) [Recursive]**
- `renderElement` (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.development.js`) -> **O(2^N) [Recursive]**
- `renderElement` (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js`) -> **O(2^N) [Recursive]**
- `mapIntoArray` (@ `packages/next/src/compiled/react-experimental/cjs/react.development.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `o0` (@ `packages/next/src/compiled/@vercel/og/index.edge.js`) -> DB Complexity: **348**
- `fE` (@ `packages/next/src/compiled/@vercel/og/index.node.js`) -> DB Complexity: **348**
- `async` (@ `packages/next/src/server/base-server.ts`) -> DB Complexity: **277**
  * *Intent:* /** * This is used to persist cache scopes across * prefetch -> full route requests for cache components
- `describe` (@ `packages/next-routing/src/__tests__/middleware.test.ts`) -> DB Complexity: **228**
- `describe` (@ `packages/next/src/server/lib/dedupe-fetch.test.ts`) -> DB Complexity: **206**
- `createMetadataElements` (@ `packages/next/src/lib/metadata/metadata.tsx`) -> DB Complexity: **185**
- `describe` (@ `packages/eslint-plugin-internal/src/eslint-typechecked-require.test.js`) -> DB Complexity: **180**
- `eval` (@ `turbopack/crates/turbopack-ecmascript/src/analyzer/graph.rs`) -> DB Complexity: **176**
- `describe` (@ `packages/next/src/lib/metadata/resolve-metadata.test.ts`) -> DB Complexity: **165**
- `import` (@ `packages/next/src/server/route-modules/route-module.ts`) -> DB Complexity: **149**
  * *Intent:* /** * RouteHandlerContext is the base context for a route handler. */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/next/src/compiled/react-dom-experimental/cjs` | 18 | 174566.94 | 53.66% | 25.06% |
| `packages/next/src/compiled/react-dom/cjs` | 17 | 142922.62 | 52.33% | 23.84% |
| `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs` | 14 | 116379.56 | 82.79% | 16.18% |
| `packages/next/src/compiled/react-server-dom-webpack/cjs` | 14 | 115743.2 | 82.83% | 16.25% |
| `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs` | 12 | 115485.66 | 83.64% | 14.77% |
| `packages/next/src/compiled/react-server-dom-turbopack/cjs` | 12 | 114849.3 | 83.69% | 14.85% |
| `packages/next/src/compiled/@edge-runtime/primitives` | 24 | 22665.26 | 17.75% | 27.44% |
| `packages/next/src/compiled/@vercel/og` | 6 | 21022.01 | 36.0% | 45.65% |
| `test/integration/env-config/app` | 4 | 15001.0 | 0.0% | 0.0% |
| `test/development/app-dir/typed-env` | 3 | 15000.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.conductor/scripts/setup.sh` -> **100.0%** Exposure
- `packages/next-codemod/scripts/test-upgrade-fixture.sh` -> **100.0%** Exposure
- `scripts/cargo/bench/get-workspace-crates.sh` -> **100.0%** Exposure
- `scripts/cargo/bench/list-crates-with-bench.sh` -> **100.0%** Exposure
- `scripts/check-examples.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/cargo/bench/list-crates-with-bench.sh` -> **100.0%** Exposure
- `scripts/deploy-examples.sh` -> **100.0%** Exposure
- `scripts/deploy-turbopack-docs.sh` -> **100.0%** Exposure
- `scripts/docker-native-build.sh` -> **100.0%** Exposure
- `crates/next-core/js/src/entry/page-loader.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` -> **0** Orphaned Functions | **127** Duplicates
- `packages/next/src/compiled/@edge-runtime/primitives/load.js` -> **0** Orphaned Functions | **127** Duplicates
- `turbopack/crates/turbopack-ecmascript/src/analyzer/mod.rs` -> **31** Orphaned Functions | **39** Duplicates
- `examples/cms-buttercms/css/main.css` -> **0** Orphaned Functions | **69** Duplicates
- `packages/next/src/compiled/@vercel/og/index.edge.js` -> **33** Orphaned Functions | **31** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/next/src/lib/metadata/metadata.tsx`** -> AI Confidence: **99.48%**
2. **`packages/next/src/server/render.tsx`** -> AI Confidence: **99.48%**
3. **`packages/next/src/bundles/webpack/packages/webpack.js`** -> AI Confidence: **99.48%**
4. **`packages/next/src/compiled/webpack/webpack.js`** -> AI Confidence: **99.48%**
5. **`packages/next/src/server/route-modules/app-page/module.compiled.js`** -> AI Confidence: **99.48%**
6. **`packages/next/src/server/route-modules/app-route/module.compiled.js`** -> AI Confidence: **99.48%**
7. **`scripts/trace-next-server.js`** -> AI Confidence: **99.48%**
8. **`packages/next-codemod/transforms/next-lint-to-eslint-cli.ts`** -> AI Confidence: **99.39%**
9. **`packages/next/src/client/legacy/image.tsx`** -> AI Confidence: **99.39%**
10. **`packages/next/src/server/config-shared.ts`** -> AI Confidence: **99.39%**
11. **`packages/next/src/server/config.ts`** -> AI Confidence: **99.39%**
12. **`packages/next/src/server/lib/patch-fetch.ts`** -> AI Confidence: **99.39%**
13. **`packages/next/src/client/app-dir/link.tsx`** -> AI Confidence: **99.35%**
14. **`packages/next/src/server/route-modules/pages-api/module.compiled.js`** -> AI Confidence: **99.34%**
15. **`packages/next/src/server/route-modules/pages/module.compiled.js`** -> AI Confidence: **99.34%**
16. **`packages/next/taskfile-swc.js`** -> AI Confidence: **99.34%**
17. **`scripts/docker-native-build.js`** -> AI Confidence: **99.34%**
18. **`evals/evals/agent-037-updatetag-cache/EVAL.ts`** -> AI Confidence: **99.32%**
19. **`evals/evals/agent-038-refresh-settings/EVAL.ts`** -> AI Confidence: **99.32%**
20. **`packages/next/src/server/dev/require-cache.ts`** -> AI Confidence: **99.32%**
21. **`packages/next/src/server/use-cache/cache-life.ts`** -> AI Confidence: **99.32%**
22. **`packages/next/src/shared/lib/router/utils/format-url.ts`** -> AI Confidence: **99.32%**
23. **`packages/next/src/shared/lib/router/utils/route-regex.test.ts`** -> AI Confidence: **99.32%**
24. **`scripts/sweep.cjs`** -> AI Confidence: **99.32%**
25. **`scripts/validate-externals-doc.js`** -> AI Confidence: **99.32%**
26. **`turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js`** -> AI Confidence: **99.32%**
27. **`examples/with-docker-compose/next-app/prod.Dockerfile`** -> AI Confidence: **99.32%**
28. **`examples/with-docker/Dockerfile`** -> AI Confidence: **99.32%**
29. **`.github/actions/validate-docs-links/src/index.ts`** -> AI Confidence: **99.31%**
30. **`apps/bundle-analyzer/components/sidebar.tsx`** -> AI Confidence: **99.31%**
31. **`bench/render-pipeline/benchmark.ts`** -> AI Confidence: **99.31%**
32. **`examples/with-cloudinary/components/SharedModal.tsx`** -> AI Confidence: **99.31%**
33. **`packages/create-next-app/create-app.ts`** -> AI Confidence: **99.31%**
34. **`packages/create-next-app/templates/index.ts`** -> AI Confidence: **99.31%**
35. **`packages/font/src/google/loader.ts`** -> AI Confidence: **99.31%**
36. **`packages/next-codemod/bin/agents-md.ts`** -> AI Confidence: **99.31%**
37. **`packages/next-codemod/bin/transform.ts`** -> AI Confidence: **99.31%**
38. **`packages/next-codemod/bin/upgrade.ts`** -> AI Confidence: **99.31%**
39. **`packages/next-codemod/transforms/cra-to-next.ts`** -> AI Confidence: **99.31%**
40. **`packages/next-codemod/transforms/next-image-experimental.ts`** -> AI Confidence: **99.31%**
41. **`packages/next/src/client/app-dir/form.tsx`** -> AI Confidence: **99.31%**
42. **`packages/next/src/client/components/navigation.ts`** -> AI Confidence: **99.31%**
43. **`packages/next/src/client/components/router-reducer/fetch-server-response.ts`** -> AI Confidence: **99.31%**
44. **`packages/next/src/client/components/router-reducer/ppr-navigations.ts`** -> AI Confidence: **99.31%**
45. **`packages/next/src/client/components/segment-cache/cache.ts`** -> AI Confidence: **99.31%**
46. **`packages/next/src/client/components/segment-cache/scheduler.ts`** -> AI Confidence: **99.31%**
47. **`packages/next/src/client/dev/hot-reloader/pages/hot-reloader-pages.ts`** -> AI Confidence: **99.31%**
48. **`packages/next/src/client/page-bootstrap.ts`** -> AI Confidence: **99.31%**
49. **`packages/next/src/client/react-client-callbacks/error-boundary-callbacks.ts`** -> AI Confidence: **99.31%**
50. **`packages/next/src/client/resolve-href.ts`** -> AI Confidence: **99.31%**
51. **`packages/next/src/export/helpers/create-incremental-cache.ts`** -> AI Confidence: **99.31%**
52. **`packages/next/src/export/index.ts`** -> AI Confidence: **99.31%**
53. **`packages/next/src/export/routes/pages.ts`** -> AI Confidence: **99.31%**
54. **`packages/next/src/lib/create-client-router-filter.ts`** -> AI Confidence: **99.31%**
55. **`packages/next/src/lib/load-custom-routes.ts`** -> AI Confidence: **99.31%**
56. **`packages/next/src/lib/metadata/resolve-metadata.ts`** -> AI Confidence: **99.31%**
57. **`packages/next/src/lib/mkcert.ts`** -> AI Confidence: **99.31%**
58. **`packages/next/src/lib/patch-incorrect-lockfile.ts`** -> AI Confidence: **99.31%**
59. **`packages/next/src/lib/typescript/getTypeScriptConfiguration.ts`** -> AI Confidence: **99.31%**
60. **`packages/next/src/lib/typescript/writeAppTypeDeclarations.ts`** -> AI Confidence: **99.31%**
61. **`packages/next/src/lib/typescript/writeConfigurationDefaults.ts`** -> AI Confidence: **99.31%**
62. **`packages/next/src/lib/verify-typescript-setup.ts`** -> AI Confidence: **99.31%**
63. **`packages/next/src/next-devtools/dev-overlay/components/devtools-indicator/next-logo.tsx`** -> AI Confidence: **99.31%**
64. **`packages/next/src/next-devtools/dev-overlay/components/terminal/terminal.tsx`** -> AI Confidence: **99.31%**
65. **`packages/next/src/next-devtools/dev-overlay/menu/dev-overlay-menu.tsx`** -> AI Confidence: **99.31%**
66. **`packages/next/src/next-devtools/dev-overlay/panel/dynamic-panel.tsx`** -> AI Confidence: **99.31%**
67. **`packages/next/src/next-devtools/server/launch-editor.ts`** -> AI Confidence: **99.31%**
68. **`packages/next/src/pages/_document.tsx`** -> AI Confidence: **99.31%**
69. **`packages/next/src/server/api-utils/node/api-resolver.ts`** -> AI Confidence: **99.31%**
70. **`packages/next/src/server/app-render/action-handler.ts`** -> AI Confidence: **99.31%**
71. **`packages/next/src/server/app-render/app-render.tsx`** -> AI Confidence: **99.31%**
72. **`packages/next/src/server/app-render/collect-segment-data.tsx`** -> AI Confidence: **99.31%**
73. **`packages/next/src/server/app-render/create-component-tree.tsx`** -> AI Confidence: **99.31%**
74. **`packages/next/src/server/app-render/dynamic-rendering.ts`** -> AI Confidence: **99.31%**
75. **`packages/next/src/server/app-render/encryption.ts`** -> AI Confidence: **99.31%**
76. **`packages/next/src/server/app-render/instant-validation/instant-samples.ts`** -> AI Confidence: **99.31%**
77. **`packages/next/src/server/app-render/instant-validation/instant-validation.tsx`** -> AI Confidence: **99.31%**
78. **`packages/next/src/server/app-render/walk-tree-with-flight-router-state.tsx`** -> AI Confidence: **99.31%**
79. **`packages/next/src/server/app-render/work-unit-async-storage.external.ts`** -> AI Confidence: **99.31%**
80. **`packages/next/src/server/base-server.ts`** -> AI Confidence: **99.31%**
81. **`packages/next/src/server/dev/browser-logs/receive-logs.ts`** -> AI Confidence: **99.31%**
82. **`packages/next/src/server/dev/hot-middleware.ts`** -> AI Confidence: **99.31%**
83. **`packages/next/src/server/dev/log-requests.ts`** -> AI Confidence: **99.31%**
84. **`packages/next/src/server/dev/middleware-turbopack.ts`** -> AI Confidence: **99.31%**
85. **`packages/next/src/server/dev/on-demand-entry-handler.ts`** -> AI Confidence: **99.31%**
86. **`packages/next/src/server/image-optimizer.ts`** -> AI Confidence: **99.31%**
87. **`packages/next/src/server/lib/incremental-cache/file-system-cache.ts`** -> AI Confidence: **99.31%**
88. **`packages/next/src/server/lib/incremental-cache/index.ts`** -> AI Confidence: **99.31%**
89. **`packages/next/src/server/lib/router-utils/cache-life-type-utils.ts`** -> AI Confidence: **99.31%**
90. **`packages/next/src/server/lib/router-utils/resolve-routes.ts`** -> AI Confidence: **99.31%**
91. **`packages/next/src/server/lib/router-utils/route-types-utils.ts`** -> AI Confidence: **99.31%**
92. **`packages/next/src/server/lib/router-utils/setup-dev-bundler.ts`** -> AI Confidence: **99.31%**
93. **`packages/next/src/server/lib/start-server.ts`** -> AI Confidence: **99.31%**
94. **`packages/next/src/server/patch-error-inspect.ts`** -> AI Confidence: **99.31%**
95. **`packages/next/src/server/pipe-readable.ts`** -> AI Confidence: **99.31%**
96. **`packages/next/src/server/request/connection.ts`** -> AI Confidence: **99.31%**
97. **`packages/next/src/server/request/cookies.ts`** -> AI Confidence: **99.31%**
98. **`packages/next/src/server/request/headers.ts`** -> AI Confidence: **99.31%**
99. **`packages/next/src/server/request/search-params.ts`** -> AI Confidence: **99.31%**
100. **`packages/next/src/server/response-cache/index.ts`** -> AI Confidence: **99.31%**
101. **`packages/next/src/server/route-modules/pages/pages-handler.ts`** -> AI Confidence: **99.31%**
102. **`packages/next/src/server/route-modules/route-module.ts`** -> AI Confidence: **99.31%**
103. **`packages/next/src/server/server-utils.ts`** -> AI Confidence: **99.31%**
104. **`packages/next/src/server/stream-utils/node-web-streams-helper.ts`** -> AI Confidence: **99.31%**
105. **`packages/next/src/server/typescript/index.ts`** -> AI Confidence: **99.31%**
106. **`packages/next/src/server/use-cache/use-cache-wrapper.ts`** -> AI Confidence: **99.31%**
107. **`packages/next/src/server/web/next-url.ts`** -> AI Confidence: **99.31%**
108. **`packages/next/src/server/web/spec-extension/revalidate.ts`** -> AI Confidence: **99.31%**
109. **`packages/next/src/shared/lib/i18n/get-locale-redirect.ts`** -> AI Confidence: **99.31%**
110. **`packages/next/src/shared/lib/router/router.ts`** -> AI Confidence: **99.31%**
111. **`packages/next/src/shared/lib/router/utils/get-dynamic-param.ts`** -> AI Confidence: **99.31%**
112. **`packages/next/src/shared/lib/router/utils/prepare-destination.ts`** -> AI Confidence: **99.31%**
113. **`packages/next/src/shared/lib/router/utils/resolve-rewrites.ts`** -> AI Confidence: **99.31%**
114. **`packages/next/src/trace/trace-uploader.ts`** -> AI Confidence: **99.31%**
115. **`turbopack/crates/turbopack-node/js/src/transforms/webpack-loaders.ts`** -> AI Confidence: **99.31%**
116. **`.github/actions/next-stats-action/src/add-comment.js`** -> AI Confidence: **99.31%**
117. **`.github/actions/next-stats-action/src/index.js`** -> AI Confidence: **99.31%**
118. **`.github/actions/next-stats-action/src/run/collect-diffs.js`** -> AI Confidence: **99.31%**
119. **`.github/actions/next-stats-action/src/run/index.js`** -> AI Confidence: **99.31%**
120. **`packages/next/src/compiled/@edge-runtime/primitives/fetch.js`** -> AI Confidence: **99.31%**
121. **`packages/next/src/compiled/@edge-runtime/primitives/load.js`** -> AI Confidence: **99.31%**
122. **`packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-plugin.js`** -> AI Confidence: **99.31%**
123. **`packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-plugin.js`** -> AI Confidence: **99.31%**
124. **`scripts/docker-image-cache.js`** -> AI Confidence: **99.31%**
125. **`scripts/get-changed-tests.mjs`** -> AI Confidence: **99.31%**
126. **`scripts/minimal-server.js`** -> AI Confidence: **99.31%**
127. **`scripts/publish-release.js`** -> AI Confidence: **99.31%**
128. **`scripts/sync-react.js`** -> AI Confidence: **99.31%**
129. **`turbopack/crates/turbopack-tests/tests/execution/webpack/chunks/__skipped__/named-chunks/input/index.js`** -> AI Confidence: **99.31%**
130. **`crates/next-code-frame/src/highlight.rs`** -> AI Confidence: **99.31%**
131. **`crates/next-core/src/next_app/mod.rs`** -> AI Confidence: **99.31%**
132. **`crates/next-core/src/next_font/google/options.rs`** -> AI Confidence: **99.31%**
133. **`crates/next-core/src/next_font/google/util.rs`** -> AI Confidence: **99.31%**
134. **`crates/next-core/src/next_font/local/font_fallback.rs`** -> AI Confidence: **99.31%**
135. **`crates/next-core/src/next_server/transforms.rs`** -> AI Confidence: **99.31%**
136. **`crates/next-custom-transforms/src/transforms/debug_instant_stack.rs`** -> AI Confidence: **99.31%**
137. **`crates/next-custom-transforms/src/transforms/optimize_barrel.rs`** -> AI Confidence: **99.31%**
138. **`crates/next-custom-transforms/src/transforms/page_config.rs`** -> AI Confidence: **99.31%**
139. **`crates/next-error-code-swc-plugin/src/lib.rs`** -> AI Confidence: **99.31%**
140. **`crates/next-napi-bindings/src/turbopack.rs`** -> AI Confidence: **99.31%**
141. **`rspack/crates/binding/src/handle_externals.rs`** -> AI Confidence: **99.31%**
142. **`turbopack/crates/turbo-persistence-tools/src/main.rs`** -> AI Confidence: **99.31%**
143. **`turbopack/crates/turbo-persistence/src/meta_file_builder.rs`** -> AI Confidence: **99.31%**
144. **`turbopack/crates/turbo-persistence/src/tests.rs`** -> AI Confidence: **99.31%**
145. **`turbopack/crates/turbo-rcstr/benches/mod.rs`** -> AI Confidence: **99.31%**
146. **`turbopack/crates/turbo-tasks-backend/src/error.rs`** -> AI Confidence: **99.31%**
147. **`turbopack/crates/turbo-tasks-backend/tests/debug.rs`** -> AI Confidence: **99.31%**
148. **`turbopack/crates/turbo-tasks-backend/tests/performance.rs`** -> AI Confidence: **99.31%**
149. **`turbopack/crates/turbo-tasks-fs/src/attach.rs`** -> AI Confidence: **99.31%**
150. **`turbopack/crates/turbo-tasks-fs/src/lib.rs`** -> AI Confidence: **99.31%**
151. **`turbopack/crates/turbo-tasks-macros/src/derive/task_storage_macro.rs`** -> AI Confidence: **99.31%**
152. **`turbopack/crates/turbo-tasks/src/keyed.rs`** -> AI Confidence: **99.31%**
153. **`turbopack/crates/turbopack-analyze/tests/split_chunk.rs`** -> AI Confidence: **99.31%**
154. **`turbopack/crates/turbopack-bench/src/bundlers/nextjs/mod.rs`** -> AI Confidence: **99.31%**
155. **`turbopack/crates/turbopack-bench/src/bundlers/parcel.rs`** -> AI Confidence: **99.31%**
156. **`turbopack/crates/turbopack-bench/src/bundlers/rspack/mod.rs`** -> AI Confidence: **99.31%**
157. **`turbopack/crates/turbopack-bench/src/bundlers/vite/mod.rs`** -> AI Confidence: **99.31%**
158. **`turbopack/crates/turbopack-bench/src/bundlers/webpack/mod.rs`** -> AI Confidence: **99.31%**
159. **`turbopack/crates/turbopack-cli/benches/bundler.rs`** -> AI Confidence: **99.31%**
160. **`turbopack/crates/turbopack-core/src/environment.rs`** -> AI Confidence: **99.31%**
161. **`turbopack/crates/turbopack-core/src/module_graph/side_effect_module_info.rs`** -> AI Confidence: **99.31%**
162. **`turbopack/crates/turbopack-core/src/module_graph/style_groups.rs`** -> AI Confidence: **99.31%**
163. **`turbopack/crates/turbopack-core/src/resolve/error.rs`** -> AI Confidence: **99.31%**
164. **`turbopack/crates/turbopack-core/src/resolve/pattern.rs`** -> AI Confidence: **99.31%**
165. **`turbopack/crates/turbopack-core/src/resolve/remap.rs`** -> AI Confidence: **99.31%**
166. **`turbopack/crates/turbopack-core/src/server_fs.rs`** -> AI Confidence: **99.31%**
167. **`turbopack/crates/turbopack-dev-server/src/source/resolve.rs`** -> AI Confidence: **99.31%**
168. **`turbopack/crates/turbopack-dev-server/src/source/route_tree.rs`** -> AI Confidence: **99.31%**
169. **`turbopack/crates/turbopack-ecmascript-runtime/src/browser_runtime.rs`** -> AI Confidence: **99.31%**
170. **`turbopack/crates/turbopack-ecmascript/src/analyzer/builtin.rs`** -> AI Confidence: **99.31%**
171. **`turbopack/crates/turbopack-ecmascript/src/analyzer/mod.rs`** -> AI Confidence: **99.31%**
172. **`turbopack/crates/turbopack-ecmascript/src/analyzer/side_effects.rs`** -> AI Confidence: **99.31%**
173. **`turbopack/crates/turbopack-ecmascript/src/analyzer/well_known.rs`** -> AI Confidence: **99.31%**
174. **`turbopack/crates/turbopack-ecmascript/src/references/external_module.rs`** -> AI Confidence: **99.31%**
175. **`turbopack/crates/turbopack-image/src/process/svg.rs`** -> AI Confidence: **99.31%**
176. **`turbopack/crates/turbopack-trace-server/src/span_graph_ref.rs`** -> AI Confidence: **99.31%**
177. **`turbopack/crates/turbopack-trace-server/src/viewer.rs`** -> AI Confidence: **99.31%**
178. **`turbopack/xtask/src/visualize_bundler_bench.rs`** -> AI Confidence: **99.31%**
179. **`.conductor/scripts/run.sh`** -> AI Confidence: **99.29%**
180. **`examples/cms-wordpress/src/utils/seoData.ts`** -> AI Confidence: **99.29%**
181. **`packages/next/src/client/lib/console.ts`** -> AI Confidence: **99.29%**
182. **`packages/next/src/lib/metadata/types/manifest-types.ts`** -> AI Confidence: **99.29%**
183. **`packages/next/src/next-devtools/shared/version-staleness.ts`** -> AI Confidence: **99.29%**
184. **`packages/next/src/server/lib/is-ipv6.ts`** -> AI Confidence: **99.29%**
185. **`packages/next/src/server/use-cache/cache-tag.ts`** -> AI Confidence: **99.29%**
186. **`packages/next/src/shared/lib/deployment-id.ts`** -> AI Confidence: **99.29%**
187. **`packages/next/src/shared/lib/router/utils/sorted-routes.ts`** -> AI Confidence: **99.29%**
188. **`packages/next/src/telemetry/events/version.ts`** -> AI Confidence: **99.29%**
189. **`turbopack/crates/turbopack-ecmascript-runtime/js/src/browser/runtime/dom/dev-backend-dom.ts`** -> AI Confidence: **99.29%**
190. **`turbopack/crates/turbopack-ecmascript-runtime/js/src/nodejs/runtime/runtime-base.ts`** -> AI Confidence: **99.29%**
191. **`crates/next-custom-transforms/tests/fixture/edge-assert/guarded-nodejs/input.js`** -> AI Confidence: **99.29%**
192. **`crates/next-custom-transforms/tests/fixture/edge-assert/guarded-nodejs/output.js`** -> AI Confidence: **99.29%**
193. **`crates/next-custom-transforms/tests/fixture/edge-assert/guarded-process/input.js`** -> AI Confidence: **99.29%**
194. **`crates/next-custom-transforms/tests/fixture/edge-assert/guarded-process/output.js`** -> AI Confidence: **99.29%**
195. **`crates/next-custom-transforms/tests/fixture/edge-assert/guarded-runtime-process/input.js`** -> AI Confidence: **99.29%**
196. **`crates/next-custom-transforms/tests/fixture/edge-assert/guarded-runtime-process/output.js`** -> AI Confidence: **99.29%**
197. **`crates/next-custom-transforms/tests/fixture/edge-assert/mixed-process-api/input.js`** -> AI Confidence: **99.29%**
198. **`crates/next-custom-transforms/tests/fixture/edge-assert/mixed-process-api/output.js`** -> AI Confidence: **99.29%**
199. **`crates/next-custom-transforms/tests/loader/issue-30389/input.js`** -> AI Confidence: **99.29%**
200. **`evals/evals/agent-030-app-router-migration-hard/pages/api/posts/[id].js`** -> AI Confidence: **99.29%**
201. **`examples/cache-handler-redis/next.config.js`** -> AI Confidence: **99.29%**
202. **`examples/mdx-pages/next.config.js`** -> AI Confidence: **99.29%**
203. **`jest.config.js`** -> AI Confidence: **99.29%**
204. **`packages/eslint-plugin-internal/src/eslint-no-ambiguous-jsx.js`** -> AI Confidence: **99.29%**
205. **`packages/next/root-params.js`** -> AI Confidence: **99.29%**
206. **`packages/next/src/bundles/cssnano-simple/index.js`** -> AI Confidence: **99.29%**
207. **`packages/next/src/compiled/@babel/runtime/helpers/AwaitValue.js`** -> AI Confidence: **99.29%**
208. **`packages/next/src/compiled/@babel/runtime/helpers/OverloadYield.js`** -> AI Confidence: **99.29%**
209. **`packages/next/src/compiled/@babel/runtime/helpers/assertClassBrand.js`** -> AI Confidence: **99.29%**
210. **`packages/next/src/compiled/@babel/runtime/helpers/checkPrivateRedeclaration.js`** -> AI Confidence: **99.29%**
211. **`packages/next/src/compiled/@babel/runtime/helpers/classApplyDescriptorSet.js`** -> AI Confidence: **99.29%**
212. **`packages/next/src/compiled/@babel/runtime/helpers/classCheckPrivateStaticFieldDescriptor.js`** -> AI Confidence: **99.29%**
213. **`packages/next/src/compiled/@babel/runtime/helpers/classNameTDZError.js`** -> AI Confidence: **99.29%**
214. **`packages/next/src/compiled/@babel/runtime/helpers/classPrivateMethodSet.js`** -> AI Confidence: **99.29%**
215. **`packages/next/src/compiled/@babel/runtime/helpers/classStaticPrivateMethodSet.js`** -> AI Confidence: **99.29%**
216. **`packages/next/src/compiled/@babel/runtime/helpers/esm/classApplyDescriptorSet.js`** -> AI Confidence: **99.29%**
217. **`packages/next/src/compiled/@babel/runtime/helpers/esm/jsx.js`** -> AI Confidence: **99.29%**
218. **`packages/next/src/compiled/@babel/runtime/helpers/inherits.js`** -> AI Confidence: **99.29%**
219. **`packages/next/src/compiled/@babel/runtime/helpers/initializerDefineProperty.js`** -> AI Confidence: **99.29%**
220. **`packages/next/src/compiled/@babel/runtime/helpers/instanceof.js`** -> AI Confidence: **99.29%**
221. **`packages/next/src/compiled/@babel/runtime/helpers/interopRequireDefault.js`** -> AI Confidence: **99.29%**
222. **`packages/next/src/compiled/@babel/runtime/helpers/iterableToArray.js`** -> AI Confidence: **99.29%**
223. **`packages/next/src/compiled/@babel/runtime/helpers/jsx.js`** -> AI Confidence: **99.29%**
224. **`packages/next/src/compiled/@babel/runtime/helpers/newArrowCheck.js`** -> AI Confidence: **99.29%**
225. **`packages/next/src/compiled/@babel/runtime/helpers/nonIterableRest.js`** -> AI Confidence: **99.29%**
226. **`packages/next/src/compiled/@babel/runtime/helpers/nonIterableSpread.js`** -> AI Confidence: **99.29%**
227. **`packages/next/src/compiled/@babel/runtime/helpers/nullishReceiverError.js`** -> AI Confidence: **99.29%**
228. **`packages/next/src/compiled/@babel/runtime/helpers/objectDestructuringEmpty.js`** -> AI Confidence: **99.29%**
229. **`packages/next/src/compiled/@babel/runtime/helpers/readOnlyError.js`** -> AI Confidence: **99.29%**
230. **`packages/next/src/compiled/@babel/runtime/helpers/tdz.js`** -> AI Confidence: **99.29%**
231. **`packages/next/src/compiled/@babel/runtime/helpers/temporalUndefined.js`** -> AI Confidence: **99.29%**
232. **`packages/next/src/compiled/@babel/runtime/helpers/tsRewriteRelativeImportExtensions.js`** -> AI Confidence: **99.29%**
233. **`packages/next/src/compiled/@babel/runtime/helpers/writeOnlyError.js`** -> AI Confidence: **99.29%**
234. **`packages/next/src/compiled/@babel/runtime/regenerator/index.js`** -> AI Confidence: **99.29%**
235. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.browser.development.js`** -> AI Confidence: **99.29%**
236. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.node.development.js`** -> AI Confidence: **99.29%**
237. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.node.production.js`** -> AI Confidence: **99.29%**
238. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom.development.js`** -> AI Confidence: **99.29%**
239. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom.react-server.development.js`** -> AI Confidence: **99.29%**
240. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom.react-server.production.js`** -> AI Confidence: **99.29%**
241. **`packages/next/src/compiled/react-dom-experimental/client.js`** -> AI Confidence: **99.29%**
242. **`packages/next/src/compiled/react-dom-experimental/index.js`** -> AI Confidence: **99.29%**
243. **`packages/next/src/compiled/react-dom-experimental/profiling.js`** -> AI Confidence: **99.29%**
244. **`packages/next/src/compiled/react-dom-experimental/react-dom.react-server.js`** -> AI Confidence: **99.29%**
245. **`packages/next/src/compiled/react-dom/cjs/react-dom-server-legacy.browser.development.js`** -> AI Confidence: **99.29%**
246. **`packages/next/src/compiled/react-dom/cjs/react-dom-server-legacy.node.development.js`** -> AI Confidence: **99.29%**
247. **`packages/next/src/compiled/react-dom/cjs/react-dom-server-legacy.node.production.js`** -> AI Confidence: **99.29%**
248. **`packages/next/src/compiled/react-dom/cjs/react-dom.development.js`** -> AI Confidence: **99.29%**
249. **`packages/next/src/compiled/react-dom/cjs/react-dom.react-server.development.js`** -> AI Confidence: **99.29%**
250. **`packages/next/src/compiled/react-dom/cjs/react-dom.react-server.production.js`** -> AI Confidence: **99.29%**
251. **`packages/next/src/compiled/react-dom/client.js`** -> AI Confidence: **99.29%**
252. **`packages/next/src/compiled/react-dom/index.js`** -> AI Confidence: **99.29%**
253. **`packages/next/src/compiled/react-dom/profiling.js`** -> AI Confidence: **99.29%**
254. **`packages/next/src/compiled/react-dom/react-dom.react-server.js`** -> AI Confidence: **99.29%**
255. **`packages/next/src/compiled/react-experimental/compiler-runtime.js`** -> AI Confidence: **99.29%**
256. **`packages/next/src/compiled/react-experimental/index.js`** -> AI Confidence: **99.29%**
257. **`packages/next/src/compiled/react-experimental/jsx-dev-runtime.js`** -> AI Confidence: **99.29%**
258. **`packages/next/src/compiled/react-experimental/jsx-dev-runtime.react-server.js`** -> AI Confidence: **99.29%**
259. **`packages/next/src/compiled/react-experimental/jsx-runtime.js`** -> AI Confidence: **99.29%**
260. **`packages/next/src/compiled/react-experimental/jsx-runtime.react-server.js`** -> AI Confidence: **99.29%**
261. **`packages/next/src/compiled/react-experimental/react.react-server.js`** -> AI Confidence: **99.29%**
262. **`packages/next/src/compiled/react-is/index.js`** -> AI Confidence: **99.29%**
263. **`packages/next/src/compiled/react-server-dom-turbopack-experimental/client.browser.js`** -> AI Confidence: **99.29%**
264. **`packages/next/src/compiled/react-server-dom-turbopack-experimental/client.edge.js`** -> AI Confidence: **99.29%**
265. **`packages/next/src/compiled/react-server-dom-turbopack-experimental/client.node.js`** -> AI Confidence: **99.29%**
266. **`packages/next/src/compiled/react-server-dom-turbopack/client.browser.js`** -> AI Confidence: **99.29%**
267. **`packages/next/src/compiled/react-server-dom-turbopack/client.edge.js`** -> AI Confidence: **99.29%**
268. **`packages/next/src/compiled/react-server-dom-turbopack/client.node.js`** -> AI Confidence: **99.29%**
269. **`packages/next/src/compiled/react-server-dom-webpack-experimental/client.browser.js`** -> AI Confidence: **99.29%**
270. **`packages/next/src/compiled/react-server-dom-webpack-experimental/client.edge.js`** -> AI Confidence: **99.29%**
271. **`packages/next/src/compiled/react-server-dom-webpack-experimental/client.node.js`** -> AI Confidence: **99.29%**
272. **`packages/next/src/compiled/react-server-dom-webpack/client.browser.js`** -> AI Confidence: **99.29%**
273. **`packages/next/src/compiled/react-server-dom-webpack/client.edge.js`** -> AI Confidence: **99.29%**
274. **`packages/next/src/compiled/react-server-dom-webpack/client.node.js`** -> AI Confidence: **99.29%**
275. **`packages/next/src/compiled/react/compiler-runtime.js`** -> AI Confidence: **99.29%**
276. **`packages/next/src/compiled/react/index.js`** -> AI Confidence: **99.29%**
277. **`packages/next/src/compiled/react/jsx-dev-runtime.js`** -> AI Confidence: **99.29%**
278. **`packages/next/src/compiled/react/jsx-dev-runtime.react-server.js`** -> AI Confidence: **99.29%**
279. **`packages/next/src/compiled/react/jsx-runtime.js`** -> AI Confidence: **99.29%**
280. **`packages/next/src/compiled/react/jsx-runtime.react-server.js`** -> AI Confidence: **99.29%**
281. **`packages/next/src/compiled/react/react.react-server.js`** -> AI Confidence: **99.29%**
282. **`packages/next/src/compiled/scheduler-experimental/index.js`** -> AI Confidence: **99.29%**
283. **`packages/next/src/compiled/scheduler-experimental/index.native.js`** -> AI Confidence: **99.29%**
284. **`packages/next/src/compiled/scheduler-experimental/unstable_mock.js`** -> AI Confidence: **99.29%**
285. **`packages/next/src/compiled/scheduler-experimental/unstable_post_task.js`** -> AI Confidence: **99.29%**
286. **`packages/next/src/compiled/scheduler/index.js`** -> AI Confidence: **99.29%**
287. **`packages/next/src/compiled/scheduler/index.native.js`** -> AI Confidence: **99.29%**
288. **`packages/next/src/compiled/scheduler/unstable_mock.js`** -> AI Confidence: **99.29%**
289. **`packages/next/src/compiled/scheduler/unstable_post_task.js`** -> AI Confidence: **99.29%**
290. **`packages/next/src/shared/lib/dset.js`** -> AI Confidence: **99.29%**
291. **`scripts/rust-fingerprint.js`** -> AI Confidence: **99.29%**
292. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/exports.default.default.cjs`** -> AI Confidence: **99.29%**
293. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/exports.default.server.cjs`** -> AI Confidence: **99.29%**
294. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/exports.next.default.cjs`** -> AI Confidence: **99.29%**
295. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/exports.next.server.cjs`** -> AI Confidence: **99.29%**
296. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/imports/imports.default.default.cjs`** -> AI Confidence: **99.29%**
297. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/imports/imports.default.server.cjs`** -> AI Confidence: **99.29%**
298. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/imports/imports.next.default.cjs`** -> AI Confidence: **99.29%**
299. **`test/e2e/app-dir/next-condition/packages/my-cjs-package/src/imports/imports.next.server.cjs`** -> AI Confidence: **99.29%**
300. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/exports.default.default.cjs`** -> AI Confidence: **99.29%**
301. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/exports.default.server.cjs`** -> AI Confidence: **99.29%**
302. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/exports.next.default.cjs`** -> AI Confidence: **99.29%**
303. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/exports.next.server.cjs`** -> AI Confidence: **99.29%**
304. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/imports/imports.default.default.cjs`** -> AI Confidence: **99.29%**
305. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/imports/imports.default.server.cjs`** -> AI Confidence: **99.29%**
306. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/imports/imports.next.default.cjs`** -> AI Confidence: **99.29%**
307. **`test/e2e/app-dir/next-condition/packages/my-external-cjs-package/src/imports/imports.next.server.cjs`** -> AI Confidence: **99.29%**
308. **`test/e2e/instrumentation-hook-src/src/instrumentation.js`** -> AI Confidence: **99.29%**
309. **`turbopack/crates/turbopack-ecmascript/tests/analyzer/graph/array/input.js`** -> AI Confidence: **99.29%**
310. **`turbopack/crates/turbopack-ecmascript/tests/analyzer/graph/mongoose-reduced/input.js`** -> AI Confidence: **99.29%**
311. **`turbopack/crates/turbopack-ecmascript/tests/analyzer/graph/pack-2521/input.js`** -> AI Confidence: **99.29%**
312. **`turbopack/crates/turbopack-tests/tests/execution/turbopack/evaluation-errors/basic/input/throws.js`** -> AI Confidence: **99.29%**
313. **`turbopack/crates/turbopack-tests/tests/execution/webpack/chunks/__skipped__/runtime/input/index.js`** -> AI Confidence: **99.29%**
314. **`turbopack/crates/turbopack-tests/tests/execution/webpack/chunks/import-context-exist-chunk/input/dir-initial-with-fake-map/initialModule2.js`** -> AI Confidence: **99.29%**
315. **`turbopack/crates/turbopack-tests/tests/execution/webpack/scope-hoisting/reexport-exposed-default-cjs/input/a.js`** -> AI Confidence: **99.29%**
316. **`turbopack/crates/turbopack-tests/tests/snapshot/basic-tree-shake/require-side-effect/output/1ece_tests_snapshot_basic-tree-shake_require-side-effect_input_index_1183joi.js`** -> AI Confidence: **99.29%**
317. **`turbopack/crates/turbopack-tests/tests/snapshot/basic/async_chunk/output/1i9t_crates_turbopack-tests_tests_snapshot_basic_async_chunk_input_index_0k4s9ge.js`** -> AI Confidence: **99.29%**
318. **`turbopack/crates/turbopack-tests/tests/snapshot/basic/chunk_loading_global/output/0rv8_turbopack-tests_tests_snapshot_basic_chunk_loading_global_input_index_176tecx.js`** -> AI Confidence: **99.29%**
319. **`turbopack/crates/turbopack-tests/tests/snapshot/basic/chunked/output/1i9t_crates_turbopack-tests_tests_snapshot_basic_chunked_input_index_14uir__.js`** -> AI Confidence: **99.29%**
320. **`turbopack/crates/turbopack-tests/tests/snapshot/basic/shebang/output/1i9t_crates_turbopack-tests_tests_snapshot_basic_shebang_input_index_0z_jazh.js`** -> AI Confidence: **99.29%**
321. **`turbopack/crates/turbopack-tests/tests/snapshot/basic/ts-parse-error/output/1i9t_crates_turbopack-tests_tests_snapshot_basic_ts-parse-error_input_index_1ujhpiq.js`** -> AI Confidence: **99.29%**
322. **`turbopack/crates/turbopack-tests/tests/snapshot/basic/use-strict/output/1i9t_crates_turbopack-tests_tests_snapshot_basic_use-strict_input_index_16lpo6o.js`** -> AI Confidence: **99.29%**
323. **`turbopack/crates/turbopack-tests/tests/snapshot/comptime/define/input/index.js`** -> AI Confidence: **99.29%**
324. **`turbopack/crates/turbopack-tests/tests/snapshot/comptime/define/output/1do3_crates_turbopack-tests_tests_snapshot_comptime_define_input_index_1etshin.js`** -> AI Confidence: **99.29%**
325. **`turbopack/crates/turbopack-tests/tests/snapshot/comptime/define/output/1i9t_crates_turbopack-tests_tests_snapshot_comptime_define_input_index_0ywijkh.js`** -> AI Confidence: **99.29%**
326. **`turbopack/crates/turbopack-tests/tests/snapshot/comptime/typeof/output/1i9t_crates_turbopack-tests_tests_snapshot_comptime_typeof_input_index_1b5f3gw.js`** -> AI Confidence: **99.29%**
327. **`turbopack/crates/turbopack-tests/tests/snapshot/css/chained-attributes/output/0rv8_turbopack-tests_tests_snapshot_css_chained-attributes_input_index_1fpqjba.js`** -> AI Confidence: **99.29%**
328. **`turbopack/crates/turbopack-tests/tests/snapshot/css/css-legacy-nesting/output/0rv8_turbopack-tests_tests_snapshot_css_css-legacy-nesting_input_index_1ygiwak.js`** -> AI Confidence: **99.29%**
329. **`turbopack/crates/turbopack-tests/tests/snapshot/css/css-modules/output/1i9t_crates_turbopack-tests_tests_snapshot_css_css-modules_input_index_1eiqfsb.js`** -> AI Confidence: **99.29%**
330. **`turbopack/crates/turbopack-tests/tests/snapshot/css/css-parse-error/output/1i9t_crates_turbopack-tests_tests_snapshot_css_css-parse-error_input_index_06xr3ir.js`** -> AI Confidence: **99.29%**
331. **`turbopack/crates/turbopack-tests/tests/snapshot/css/css/output/1i9t_crates_turbopack-tests_tests_snapshot_css_css_input_index_0p15brb.js`** -> AI Confidence: **99.29%**
332. **`turbopack/crates/turbopack-tests/tests/snapshot/css/cycle/output/1i9t_crates_turbopack-tests_tests_snapshot_css_cycle_input_index_0qzfn6v.js`** -> AI Confidence: **99.29%**
333. **`turbopack/crates/turbopack-tests/tests/snapshot/css/cycle2/output/1i9t_crates_turbopack-tests_tests_snapshot_css_cycle2_input_index_12qqqsy.js`** -> AI Confidence: **99.29%**
334. **`turbopack/crates/turbopack-tests/tests/snapshot/css/embed-url/output/1i9t_crates_turbopack-tests_tests_snapshot_css_embed-url_input_index_1t7t-i3.js`** -> AI Confidence: **99.29%**
335. **`turbopack/crates/turbopack-tests/tests/snapshot/css/minification/output/1i9t_crates_turbopack-tests_tests_snapshot_css_minification_input_index_1iii2hw.js`** -> AI Confidence: **99.29%**
336. **`turbopack/crates/turbopack-tests/tests/snapshot/css/split-shared/output/1i9t_crates_turbopack-tests_tests_snapshot_css_split-shared_input_index_083vk13.js`** -> AI Confidence: **99.29%**
337. **`turbopack/crates/turbopack-tests/tests/snapshot/css/url-in-supports-query/output/0rv8_turbopack-tests_tests_snapshot_css_url-in-supports-query_input_index_1tdhjpp.js`** -> AI Confidence: **99.29%**
338. **`turbopack/crates/turbopack-tests/tests/snapshot/cssmodules/composes/output/1i9t_crates_turbopack-tests_tests_snapshot_cssmodules_composes_input_index_0hzxlft.js`** -> AI Confidence: **99.29%**
339. **`turbopack/crates/turbopack-tests/tests/snapshot/debug-ids/browser/output/1do3_crates_turbopack-tests_tests_snapshot_debug-ids_browser_input_index_03ibyvs.js`** -> AI Confidence: **99.29%**
340. **`turbopack/crates/turbopack-tests/tests/snapshot/debug-ids/node/output/1do3_crates_turbopack-tests_tests_snapshot_debug-ids_node_input_index_1gqemi9.js`** -> AI Confidence: **99.29%**
341. **`turbopack/crates/turbopack-tests/tests/snapshot/dynamic-request/very-dynamic/output/0rv8_turbopack-tests_tests_snapshot_dynamic-request_very-dynamic_input_index_173nd8m.js`** -> AI Confidence: **99.29%**
342. **`turbopack/crates/turbopack-tests/tests/snapshot/emotion/emotion/output/1i9t_crates_turbopack-tests_tests_snapshot_emotion_emotion_input_index_0g4a66x.js`** -> AI Confidence: **99.29%**
343. **`turbopack/crates/turbopack-tests/tests/snapshot/evaluated_entrry/runtime_entry/output/1ece_tests_snapshot_evaluated_entrry_runtime_entry_input_index_1rizxil.js`** -> AI Confidence: **99.29%**
344. **`turbopack/crates/turbopack-tests/tests/snapshot/example/example/output/1i9t_crates_turbopack-tests_tests_snapshot_example_example_input_index_1i-hpj6.js`** -> AI Confidence: **99.29%**
345. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/duplicate-binding/output/0rv8_turbopack-tests_tests_snapshot_imports_duplicate-binding_input_index_1p9fqe6.js`** -> AI Confidence: **99.29%**
346. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/dynamic/output/1i9t_crates_turbopack-tests_tests_snapshot_imports_dynamic_input_index_17bvngz.js`** -> AI Confidence: **99.29%**
347. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/ignore-comments/output/0rv8_turbopack-tests_tests_snapshot_imports_ignore-comments_input_index_1aqs1qt.js`** -> AI Confidence: **99.29%**
348. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/ignore-comments/output/0rv8_turbopack-tests_tests_snapshot_imports_ignore-comments_input_vercel_cjs_02p77ng._.js`** -> AI Confidence: **99.29%**
349. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/json/output/1i9t_crates_turbopack-tests_tests_snapshot_imports_json_input_index_19kxr8d.js`** -> AI Confidence: **99.29%**
350. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/optional-comments/output/0rv8_turbopack-tests_tests_snapshot_imports_optional-comments_input_index_0v0vp97.js`** -> AI Confidence: **99.29%**
351. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/order/output/1i9t_crates_turbopack-tests_tests_snapshot_imports_order_input_index_1q7ppn1.js`** -> AI Confidence: **99.29%**
352. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/resolve_error_cjs/output/0rv8_turbopack-tests_tests_snapshot_imports_resolve_error_cjs_input_index_1f71ljk.js`** -> AI Confidence: **99.29%**
353. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/resolve_error_esm/output/0rv8_turbopack-tests_tests_snapshot_imports_resolve_error_esm_input_index_0sez0x_.js`** -> AI Confidence: **99.29%**
354. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/static-and-dynamic/output/0rv8_turbopack-tests_tests_snapshot_imports_static-and-dynamic_input_index_069ksn9.js`** -> AI Confidence: **99.29%**
355. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/static/output/1i9t_crates_turbopack-tests_tests_snapshot_imports_static_input_index_0lgmc8n.js`** -> AI Confidence: **99.29%**
356. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/subpath-imports-nested/output/1ece_tests_snapshot_imports_subpath-imports-nested_input_index_0cpull6.js`** -> AI Confidence: **99.29%**
357. **`turbopack/crates/turbopack-tests/tests/snapshot/imports/subpath-imports/output/0rv8_turbopack-tests_tests_snapshot_imports_subpath-imports_input_index_1jr1_4n.js`** -> AI Confidence: **99.29%**
358. **`turbopack/crates/turbopack-tests/tests/snapshot/intermediate-tree-shake/reexport-with-locals/output/1ece_tests_snapshot_intermediate-tree-shake_reexport-with-locals_input_index_1t49frh.js`** -> AI Confidence: **99.29%**
359. **`turbopack/crates/turbopack-tests/tests/snapshot/intermediate-tree-shake/rename-side-effect-free-facade/output/0nf9_intermediate-tree-shake_rename-side-effect-free-facade_input_index_1ll-jto.js`** -> AI Confidence: **99.29%**
360. **`turbopack/crates/turbopack-tests/tests/snapshot/minification/paren-remover/output/0rv8_turbopack-tests_tests_snapshot_minification_paren-remover_input_index_1w6w_zc.js`** -> AI Confidence: **99.29%**
361. **`turbopack/crates/turbopack-tests/tests/snapshot/node/bun_protocol_external/output/0rv8_turbopack-tests_tests_snapshot_node_bun_protocol_external_input_index_0-k7eno.js`** -> AI Confidence: **99.29%**
362. **`turbopack/crates/turbopack-tests/tests/snapshot/node/node_protocol_external/output/0rv8_turbopack-tests_tests_snapshot_node_node_protocol_external_input_index_0m3vfe8.js`** -> AI Confidence: **99.29%**
363. **`turbopack/crates/turbopack-tests/tests/snapshot/node/spawn_dynamic/output/1i9t_crates_turbopack-tests_tests_snapshot_node_spawn_dynamic_input_index_13kveuz.js`** -> AI Confidence: **99.29%**
364. **`turbopack/crates/turbopack-tests/tests/snapshot/node/spawn_node_eval/output/1i9t_crates_turbopack-tests_tests_snapshot_node_spawn_node_eval_input_index_0jbhsq3.js`** -> AI Confidence: **99.29%**
365. **`turbopack/crates/turbopack-tests/tests/snapshot/remove-unused-imports/exports/output/1ece_tests_snapshot_remove-unused-imports_exports_input_index_13-h7f-.js`** -> AI Confidence: **99.29%**
366. **`turbopack/crates/turbopack-tests/tests/snapshot/scope-hoisting/duplicate-imports/output/1ece_tests_snapshot_scope-hoisting_duplicate-imports_input_index_1gtmx6d.js`** -> AI Confidence: **99.29%**
367. **`turbopack/crates/turbopack-tests/tests/snapshot/scope-hoisting/split-shared/output/0rv8_turbopack-tests_tests_snapshot_scope-hoisting_split-shared_input_index_08id204.js`** -> AI Confidence: **99.29%**
368. **`turbopack/crates/turbopack-tests/tests/snapshot/source_maps/input-source-map-merged/output/1ece_tests_snapshot_source_maps_input-source-map-merged_input_index_0h3z820.js`** -> AI Confidence: **99.29%**
369. **`turbopack/crates/turbopack-tests/tests/snapshot/source_maps/input-source-map/output/0rv8_turbopack-tests_tests_snapshot_source_maps_input-source-map_input_index_15rjc21.js`** -> AI Confidence: **99.29%**
370. **`turbopack/crates/turbopack-tests/tests/snapshot/source_maps/invalid/output/1i9t_crates_turbopack-tests_tests_snapshot_source_maps_invalid_input_index_02k04hh.js`** -> AI Confidence: **99.29%**
371. **`turbopack/crates/turbopack-tests/tests/snapshot/source_maps/merged-unicode/input/index.js`** -> AI Confidence: **99.29%**
372. **`turbopack/crates/turbopack-tests/tests/snapshot/source_maps/merged-unicode/output/0rv8_turbopack-tests_tests_snapshot_source_maps_merged-unicode_input_index_1j3m-pr.js`** -> AI Confidence: **99.29%**
373. **`turbopack/crates/turbopack-tests/tests/snapshot/styled_components/styled_components/output/1ece_tests_snapshot_styled_components_styled_components_input_index_0f3bg15.js`** -> AI Confidence: **99.29%**
374. **`turbopack/crates/turbopack-tests/tests/snapshot/swc_transforms/mono_transforms/output/ad3e4_tests_snapshot_swc_transforms_mono_transforms_input_packages_app_index_1823fe7e.js`** -> AI Confidence: **99.29%**
375. **`turbopack/crates/turbopack-tests/tests/snapshot/swc_transforms/preset_env_modern/output/1ece_tests_snapshot_swc_transforms_preset_env_modern_input_index_1fs_im_.js`** -> AI Confidence: **99.29%**
376. **`turbopack/crates/turbopack-tests/tests/snapshot/tree-shaking/dce/output/1i9t_crates_turbopack-tests_tests_snapshot_tree-shaking_dce_input_index_0_i19wv.js`** -> AI Confidence: **99.29%**
377. **`turbopack/crates/turbopack-tests/tests/snapshot/typescript/jsconfig-baseurl/output/0rv8_turbopack-tests_tests_snapshot_typescript_jsconfig-baseurl_input_index_017mg0q.js`** -> AI Confidence: **99.29%**
378. **`turbopack/crates/turbopack-tests/tests/snapshot/typescript/tsconfig-baseurl/output/ad3e4_tests_snapshot_typescript_tsconfig-baseurl_input_index_ts_aac35728._.js`** -> AI Confidence: **99.29%**
379. **`turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/auth0.js`** -> AI Confidence: **99.29%**
380. **`turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/cosmosdb-query.js`** -> AI Confidence: **99.29%**
381. **`turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/cowsay.js`** -> AI Confidence: **99.29%**
382. **`turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/mongoose.js`** -> AI Confidence: **99.29%**
383. **`turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/playwright-core.js`** -> AI Confidence: **99.29%**
384. **`turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/twilio.js`** -> AI Confidence: **99.29%**
385. **`examples/with-docker-compose/next-app/dev.Dockerfile`** -> AI Confidence: **99.29%**
386. **`examples/with-docker-export-output/Dockerfile`** -> AI Confidence: **99.29%**
387. **`scripts/native-builder.Dockerfile`** -> AI Confidence: **99.29%**
388. **`crates/next-custom-transforms/src/transforms/optimize_server_react.rs`** -> AI Confidence: **99.25%**
389. **`turbopack/crates/turbopack-ecmascript/src/magic_identifier.rs`** -> AI Confidence: **99.25%**
390. **`apps/bundle-analyzer/app/page.tsx`** -> AI Confidence: **99.24%**
391. **`examples/cms-sanity/app/(blog)/page.tsx`** -> AI Confidence: **99.24%**
392. **`examples/cms-sanity/app/(blog)/posts/[slug]/page.tsx`** -> AI Confidence: **99.24%**
393. **`examples/cms-sitecore-xmcloud/src/pages/404.tsx`** -> AI Confidence: **99.24%**
394. **`packages/next/src/client/components/app-router.tsx`** -> AI Confidence: **99.24%**
395. **`packages/next/src/client/components/router-reducer/create-initial-router-state.ts`** -> AI Confidence: **99.24%**
396. **`packages/next/src/client/dev/hot-reloader/app/hot-reloader-app.tsx`** -> AI Confidence: **99.24%**
397. **`packages/next/src/client/image-component.tsx`** -> AI Confidence: **99.24%**
398. **`packages/next/src/client/index.tsx`** -> AI Confidence: **99.24%**
399. **`packages/next/src/experimental/testing/server/config-testing-utils.ts`** -> AI Confidence: **99.24%**
400. **`packages/next/src/export/worker.ts`** -> AI Confidence: **99.24%**
401. **`packages/next/src/lib/metadata/get-metadata-route.ts`** -> AI Confidence: **99.24%**
402. **`packages/next/src/lib/verify-partytown-setup.ts`** -> AI Confidence: **99.24%**
403. **`packages/next/src/next-devtools/dev-overlay/container/errors.tsx`** -> AI Confidence: **99.24%**
404. **`packages/next/src/next-devtools/userspace/pages/pages-dev-overlay-setup.tsx`** -> AI Confidence: **99.24%**
405. **`packages/next/src/server/app-render/create-error-handler.tsx`** -> AI Confidence: **99.24%**
406. **`packages/next/src/server/app-render/get-layer-assets.tsx`** -> AI Confidence: **99.24%**
407. **`packages/next/src/server/dev/hot-reloader-turbopack.ts`** -> AI Confidence: **99.24%**
408. **`packages/next/src/server/dev/hot-reloader-webpack.ts`** -> AI Confidence: **99.24%**
409. **`packages/next/src/server/lib/router-server.ts`** -> AI Confidence: **99.24%**
410. **`packages/next/src/server/lib/router-utils/filesystem.ts`** -> AI Confidence: **99.24%**
411. **`packages/next/src/server/lib/router-utils/typegen.ts`** -> AI Confidence: **99.24%**
412. **`packages/next/src/server/next-server.ts`** -> AI Confidence: **99.24%**
413. **`packages/next/src/server/next.ts`** -> AI Confidence: **99.24%**
414. **`packages/next/src/server/render-result.ts`** -> AI Confidence: **99.24%**
415. **`packages/next/src/server/request/root-params.ts`** -> AI Confidence: **99.24%**
416. **`packages/next/src/server/require.ts`** -> AI Confidence: **99.24%**
417. **`packages/next/src/server/route-matcher-managers/default-route-matcher-manager.ts`** -> AI Confidence: **99.24%**
418. **`packages/next/src/server/web/sandbox/sandbox.ts`** -> AI Confidence: **99.24%**
419. **`packages/next/src/server/web/spec-extension/adapters/next-request.ts`** -> AI Confidence: **99.24%**
420. **`turbopack/packages/devlow-bench/src/cli.ts`** -> AI Confidence: **99.24%**
421. **`.github/actions/next-stats-action/src/run/collect-stats.js`** -> AI Confidence: **99.24%**
422. **`examples/cms-takeshape/pages/posts/[slug].js`** -> AI Confidence: **99.24%**
423. **`run-tests.js`** -> AI Confidence: **99.24%**
424. **`crates/next-api/src/app.rs`** -> AI Confidence: **99.24%**
425. **`crates/next-api/src/dynamic_imports.rs`** -> AI Confidence: **99.24%**
426. **`crates/next-api/src/middleware.rs`** -> AI Confidence: **99.24%**
427. **`crates/next-api/src/next_server_nft.rs`** -> AI Confidence: **99.24%**
428. **`crates/next-api/src/nft_json.rs`** -> AI Confidence: **99.24%**
429. **`crates/next-api/src/pages.rs`** -> AI Confidence: **99.24%**
430. **`crates/next-build-test/src/lib.rs`** -> AI Confidence: **99.24%**
431. **`crates/next-core/src/app_page_loader_tree.rs`** -> AI Confidence: **99.24%**
432. **`crates/next-core/src/next_app/metadata/mod.rs`** -> AI Confidence: **99.24%**
433. **`crates/next-core/src/next_app/metadata/route.rs`** -> AI Confidence: **99.24%**
434. **`crates/next-core/src/next_client/context.rs`** -> AI Confidence: **99.24%**
435. **`crates/next-core/src/next_client_reference/ecmascript_client_reference/ecmascript_client_reference_module.rs`** -> AI Confidence: **99.24%**
436. **`crates/next-core/src/next_edge/context.rs`** -> AI Confidence: **99.24%**
437. **`crates/next-core/src/next_font/local/stylesheet.rs`** -> AI Confidence: **99.24%**
438. **`crates/next-core/src/next_root_params/mod.rs`** -> AI Confidence: **99.24%**
439. **`crates/next-core/src/next_server/context.rs`** -> AI Confidence: **99.24%**
440. **`crates/next-core/src/next_shared/webpack_rules/babel.rs`** -> AI Confidence: **99.24%**
441. **`crates/next-core/src/next_shared/webpack_rules/sass.rs`** -> AI Confidence: **99.24%**
442. **`crates/next-core/src/pages_structure.rs`** -> AI Confidence: **99.24%**
443. **`crates/next-core/src/raw_ecmascript_module.rs`** -> AI Confidence: **99.24%**
444. **`crates/next-core/src/segment_config.rs`** -> AI Confidence: **99.24%**
445. **`crates/next-core/src/transform_options.rs`** -> AI Confidence: **99.24%**
446. **`crates/next-core/src/util.rs`** -> AI Confidence: **99.24%**
447. **`crates/next-custom-transforms/src/transforms/dynamic.rs`** -> AI Confidence: **99.24%**
448. **`crates/next-custom-transforms/src/transforms/import_analyzer.rs`** -> AI Confidence: **99.24%**
449. **`crates/next-custom-transforms/src/transforms/next_ssg.rs`** -> AI Confidence: **99.24%**
450. **`crates/next-custom-transforms/src/transforms/react_server_components.rs`** -> AI Confidence: **99.24%**
451. **`crates/next-custom-transforms/src/transforms/warn_for_edge_runtime.rs`** -> AI Confidence: **99.24%**
452. **`crates/next-napi-bindings/src/lockfile.rs`** -> AI Confidence: **99.24%**
453. **`crates/next-taskless/src/lib.rs`** -> AI Confidence: **99.24%**
454. **`crates/wasm/src/lib.rs`** -> AI Confidence: **99.24%**
455. **`turbopack/crates/turbo-bincode/src/serde_self_describing/ser.rs`** -> AI Confidence: **99.24%**
456. **`turbopack/crates/turbo-persistence/src/bin/sst_inspect.rs`** -> AI Confidence: **99.24%**
457. **`turbopack/crates/turbo-persistence/src/static_sorted_file.rs`** -> AI Confidence: **99.24%**
458. **`turbopack/crates/turbo-rcstr/src/lib.rs`** -> AI Confidence: **99.24%**
459. **`turbopack/crates/turbo-tasks-backend/fuzz/src/graph.rs`** -> AI Confidence: **99.24%**
460. **`turbopack/crates/turbo-tasks-backend/src/backend/mod.rs`** -> AI Confidence: **99.24%**
461. **`turbopack/crates/turbo-tasks-backend/src/backend/operation/aggregation_update.rs`** -> AI Confidence: **99.24%**
462. **`turbopack/crates/turbo-tasks-backend/src/backend/operation/connect_child.rs`** -> AI Confidence: **99.24%**
463. **`turbopack/crates/turbo-tasks-backend/src/backend/operation/mod.rs`** -> AI Confidence: **99.24%**
464. **`turbopack/crates/turbo-tasks-backend/src/database/db_invalidation.rs`** -> AI Confidence: **99.24%**
465. **`turbopack/crates/turbo-tasks-backend/src/database/db_versioning.rs`** -> AI Confidence: **99.24%**
466. **`turbopack/crates/turbo-tasks-backend/src/database/turbo/mod.rs`** -> AI Confidence: **99.24%**
467. **`turbopack/crates/turbo-tasks-backend/src/kv_backing_storage.rs`** -> AI Confidence: **99.24%**
468. **`turbopack/crates/turbo-tasks-backend/tests/bug2.rs`** -> AI Confidence: **99.24%**
469. **`turbopack/crates/turbo-tasks-backend/tests/operation_vc.rs`** -> AI Confidence: **99.24%**
470. **`turbopack/crates/turbo-tasks-backend/tests/top_level_task_consistency.rs`** -> AI Confidence: **99.24%**
471. **`turbopack/crates/turbo-tasks-fuzz/src/fs_watcher.rs`** -> AI Confidence: **99.24%**
472. **`turbopack/crates/turbo-tasks-macros/src/expand.rs`** -> AI Confidence: **99.24%**
473. **`turbopack/crates/turbo-tasks-macros/src/turbofmt_macro.rs`** -> AI Confidence: **99.24%**
474. **`turbopack/crates/turbo-tasks/src/id.rs`** -> AI Confidence: **99.24%**
475. **`turbopack/crates/turbo-tasks/src/trace.rs`** -> AI Confidence: **99.24%**
476. **`turbopack/crates/turbo-tasks/src/vc/operation.rs`** -> AI Confidence: **99.24%**
477. **`turbopack/crates/turbopack-bench/src/util/npm.rs`** -> AI Confidence: **99.24%**
478. **`turbopack/crates/turbopack-bench/src/util/page_guard.rs`** -> AI Confidence: **99.24%**
479. **`turbopack/crates/turbopack-browser/src/ecmascript/content.rs`** -> AI Confidence: **99.24%**
480. **`turbopack/crates/turbopack-browser/src/ecmascript/worker.rs`** -> AI Confidence: **99.24%**
481. **`turbopack/crates/turbopack-cli-utils/src/issue.rs`** -> AI Confidence: **99.24%**
482. **`turbopack/crates/turbopack-cli/src/embed_js.rs`** -> AI Confidence: **99.24%**
483. **`turbopack/crates/turbopack-core/src/chunk/available_modules.rs`** -> AI Confidence: **99.24%**
484. **`turbopack/crates/turbopack-core/src/chunk/chunk_group.rs`** -> AI Confidence: **99.24%**
485. **`turbopack/crates/turbopack-core/src/chunk/chunking/dev.rs`** -> AI Confidence: **99.24%**
486. **`turbopack/crates/turbopack-core/src/introspect/utils.rs`** -> AI Confidence: **99.24%**
487. **`turbopack/crates/turbopack-core/src/module_graph/async_module_info.rs`** -> AI Confidence: **99.24%**
488. **`turbopack/crates/turbopack-core/src/module_graph/binding_usage_info.rs`** -> AI Confidence: **99.24%**
489. **`turbopack/crates/turbopack-core/src/module_graph/chunk_group_info.rs`** -> AI Confidence: **99.24%**
490. **`turbopack/crates/turbopack-core/src/module_graph/merged_modules.rs`** -> AI Confidence: **99.24%**
491. **`turbopack/crates/turbopack-core/src/module_graph/module_batches.rs`** -> AI Confidence: **99.24%**
492. **`turbopack/crates/turbopack-core/src/reference_type.rs`** -> AI Confidence: **99.24%**
493. **`turbopack/crates/turbopack-core/src/resolve/mod.rs`** -> AI Confidence: **99.24%**
494. **`turbopack/crates/turbopack-core/src/resolve/parse.rs`** -> AI Confidence: **99.24%**
495. **`turbopack/crates/turbopack-core/src/source_map/utils.rs`** -> AI Confidence: **99.24%**
496. **`turbopack/crates/turbopack-core/src/source_pos.rs`** -> AI Confidence: **99.24%**
497. **`turbopack/crates/turbopack-create-test-app/src/test_app_builder.rs`** -> AI Confidence: **99.24%**
498. **`turbopack/crates/turbopack-css/src/chunk/mod.rs`** -> AI Confidence: **99.24%**
499. **`turbopack/crates/turbopack-dev-server/src/source/asset_graph.rs`** -> AI Confidence: **99.24%**
500. **`turbopack/crates/turbopack-ecmascript/src/analyzer/imports.rs`** -> AI Confidence: **99.24%**
501. **`turbopack/crates/turbopack-ecmascript/src/analyzer/linker.rs`** -> AI Confidence: **99.24%**
502. **`turbopack/crates/turbopack-ecmascript/src/chunk/placeable.rs`** -> AI Confidence: **99.24%**
503. **`turbopack/crates/turbopack-ecmascript/src/references/esm/export.rs`** -> AI Confidence: **99.24%**
504. **`turbopack/crates/turbopack-ecmascript/src/references/mod.rs`** -> AI Confidence: **99.24%**
505. **`turbopack/crates/turbopack-ecmascript/src/references/worker.rs`** -> AI Confidence: **99.24%**
506. **`turbopack/crates/turbopack-ecmascript/src/rename/module.rs`** -> AI Confidence: **99.24%**
507. **`turbopack/crates/turbopack-ecmascript/src/source_map.rs`** -> AI Confidence: **99.24%**
508. **`turbopack/crates/turbopack-ecmascript/src/swc_comments.rs`** -> AI Confidence: **99.24%**
509. **`turbopack/crates/turbopack-ecmascript/src/tree_shake/mod.rs`** -> AI Confidence: **99.24%**
510. **`turbopack/crates/turbopack-ecmascript/src/tree_shake/side_effects/module.rs`** -> AI Confidence: **99.24%**
511. **`turbopack/crates/turbopack-ecmascript/src/worker_chunk/worker_type.rs`** -> AI Confidence: **99.24%**
512. **`turbopack/crates/turbopack-image/src/process/mod.rs`** -> AI Confidence: **99.24%**
513. **`turbopack/crates/turbopack-node/src/embed_js.rs`** -> AI Confidence: **99.24%**
514. **`turbopack/crates/turbopack-node/src/source_map/trace.rs`** -> AI Confidence: **99.24%**
515. **`turbopack/crates/turbopack-nodejs/src/ecmascript/node/content.rs`** -> AI Confidence: **99.24%**
516. **`turbopack/crates/turbopack-resolve/src/node_native_binding.rs`** -> AI Confidence: **99.24%**
517. **`turbopack/crates/turbopack-resolve/src/resolve.rs`** -> AI Confidence: **99.24%**
518. **`turbopack/crates/turbopack-test-utils/src/snapshot.rs`** -> AI Confidence: **99.24%**
519. **`turbopack/crates/turbopack-tests/tests/execution.rs`** -> AI Confidence: **99.24%**
520. **`turbopack/crates/turbopack-trace-server/src/reader/heaptrack.rs`** -> AI Confidence: **99.24%**
521. **`turbopack/crates/turbopack-trace-server/src/span_bottom_up_ref.rs`** -> AI Confidence: **99.24%**
522. **`turbopack/crates/turbopack-trace-server/src/span_ref.rs`** -> AI Confidence: **99.24%**
523. **`turbopack/crates/turbopack-wasm/src/loader.rs`** -> AI Confidence: **99.24%**
524. **`turbopack/crates/turbopack/src/module_options/mod.rs`** -> AI Confidence: **99.24%**
525. **`apps/bundle-analyzer/components/route-typeahead.tsx`** -> AI Confidence: **99.23%**
526. **`examples/cms-payload/components/Blocks/Content/index.tsx`** -> AI Confidence: **99.23%**
527. **`examples/cms-payload/components/Blocks/index.tsx`** -> AI Confidence: **99.23%**
528. **`examples/cms-sitecore-xmcloud/src/pages/500.tsx`** -> AI Confidence: **99.23%**
529. **`examples/with-stripe-typescript/app/components/ElementsForm.tsx`** -> AI Confidence: **99.23%**
530. **`packages/next-routing/src/resolve-routes.ts`** -> AI Confidence: **99.23%**
531. **`packages/next/src/client/dev/hot-reloader/app/web-socket.ts`** -> AI Confidence: **99.23%**
532. **`packages/next/src/client/route-params.ts`** -> AI Confidence: **99.23%**
533. **`packages/next/src/lib/typescript/runTypeCheck.ts`** -> AI Confidence: **99.23%**
534. **`packages/next/src/next-devtools/dev-overlay/components/overview/segment-explorer.tsx`** -> AI Confidence: **99.23%**
535. **`packages/next/src/next-devtools/shared/deepmerge.ts`** -> AI Confidence: **99.23%**
536. **`packages/next/src/server/app-render/use-flight-response.tsx`** -> AI Confidence: **99.23%**
537. **`packages/next/src/shared/lib/get-img-props.ts`** -> AI Confidence: **99.23%**
538. **`packages/next/src/shared/lib/router/utils/route-regex.ts`** -> AI Confidence: **99.23%**
539. **`.github/actions/next-stats-action/src/aggregate-results.js`** -> AI Confidence: **99.23%**
540. **`bench/vercel/bench.js`** -> AI Confidence: **99.23%**
541. **`turbopack/crates/turbopack-tests/tests/execution/webpack/async-modules/top-level-error/input/index.js`** -> AI Confidence: **99.23%**
542. **`crates/next-custom-transforms/src/transforms/fonts/font_imports_generator.rs`** -> AI Confidence: **99.23%**
543. **`turbopack/crates/turbo-static/src/visitor.rs`** -> AI Confidence: **99.23%**
544. **`turbopack/crates/turbo-tasks-macros/src/ident.rs`** -> AI Confidence: **99.23%**
545. **`turbopack/crates/turbo-tasks-macros/src/primitive_input.rs`** -> AI Confidence: **99.23%**
546. **`turbopack/crates/turbopack-browser/src/ecmascript/update.rs`** -> AI Confidence: **99.23%**
547. **`turbopack/crates/turbopack-ecmascript/src/tree_shake/optimizations.rs`** -> AI Confidence: **99.23%**
548. **`packages/next/src/server/app-render/instant-validation/instant-samples-client.ts`** -> AI Confidence: **99.22%**
549. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js`** -> AI Confidence: **99.22%**
550. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.production.js`** -> AI Confidence: **99.22%**
551. **`packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js`** -> AI Confidence: **99.22%**
552. **`packages/next/src/compiled/react-dom/cjs/react-dom-server.node.production.js`** -> AI Confidence: **99.22%**
553. **`turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/react.js`** -> AI Confidence: **99.22%**
554. **`packages/next/src/server/revalidation-utils.ts`** -> AI Confidence: **99.2%**
555. **`packages/next/src/server/typescript/rules/client-boundary.ts`** -> AI Confidence: **99.2%**
556. **`packages/next/src/shared/lib/format-webpack-messages.ts`** -> AI Confidence: **99.2%**
557. **`turbopack/packages/webpack-nmt/src/index.ts`** -> AI Confidence: **99.2%**
558. **`packages/next/src/compiled/@babel/runtime/helpers/applyDecs.js`** -> AI Confidence: **99.2%**
559. **`packages/next/src/compiled/@babel/runtime/helpers/applyDecs2203R.js`** -> AI Confidence: **99.2%**
560. **`packages/next/src/compiled/@babel/runtime/helpers/esm/applyDecs.js`** -> AI Confidence: **99.2%**
561. **`packages/next/src/compiled/@babel/runtime/helpers/esm/applyDecs2203R.js`** -> AI Confidence: **99.2%**
562. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-client.production.js`** -> AI Confidence: **99.2%**
563. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-profiling.profiling.js`** -> AI Confidence: **99.2%**
564. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-unstable_testing.production.js`** -> AI Confidence: **99.2%**
565. **`packages/next/src/compiled/react-dom/cjs/react-dom-client.production.js`** -> AI Confidence: **99.2%**
566. **`packages/next/src/compiled/react-dom/cjs/react-dom-profiling.profiling.js`** -> AI Confidence: **99.2%**
567. **`packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-client.node.development.js`** -> AI Confidence: **99.2%**
568. **`packages/next/src/compiled/react-server-dom-turbopack/cjs/react-server-dom-turbopack-client.node.development.js`** -> AI Confidence: **99.2%**
569. **`packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-client.node.development.js`** -> AI Confidence: **99.2%**
570. **`packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-client.node.development.js`** -> AI Confidence: **99.2%**
571. **`scripts/start-release.js`** -> AI Confidence: **99.2%**
572. **`turbopack/crates/turbopack-tests/tests/execution/turbopack/runtime/factory-group-existing-factory/input/index.js`** -> AI Confidence: **99.2%**
573. **`examples/blog-with-comment/pages/posts/[slug].tsx`** -> AI Confidence: **99.18%**
574. **`examples/cms-agilitycms/pages/[...slug].tsx`** -> AI Confidence: **99.18%**
575. **`examples/cms-enterspeed/pages/index.tsx`** -> AI Confidence: **99.18%**
576. **`examples/cms-enterspeed/pages/posts/[slug].tsx`** -> AI Confidence: **99.18%**
577. **`examples/cms-payload/payload/collections/Pages.ts`** -> AI Confidence: **99.18%**
578. **`examples/cms-prismic/components/post-header.tsx`** -> AI Confidence: **99.18%**
579. **`examples/cms-sanity/sanity.config.ts`** -> AI Confidence: **99.18%**
580. **`examples/cms-umbraco/pages/index.tsx`** -> AI Confidence: **99.18%**
581. **`examples/cms-umbraco/pages/posts/[slug].tsx`** -> AI Confidence: **99.18%**
582. **`examples/cms-webiny/pages/posts/[slug].tsx`** -> AI Confidence: **99.18%**
583. **`examples/with-fingerprintjs-pro/pages/_app.tsx`** -> AI Confidence: **99.18%**
584. **`examples/with-mongodb-mongoose/pages/[id]/index.tsx`** -> AI Confidence: **99.18%**
585. **`examples/with-supabase/app/page.tsx`** -> AI Confidence: **99.18%**
586. **`packages/next/src/client/app-index.tsx`** -> AI Confidence: **99.18%**
587. **`packages/next/src/client/components/client-page.tsx`** -> AI Confidence: **99.18%**
588. **`packages/next/src/client/components/error-boundary.tsx`** -> AI Confidence: **99.18%**
589. **`packages/next/src/export/routes/app-page.ts`** -> AI Confidence: **99.18%**
590. **`packages/next/src/lib/metadata/types/metadata-interface.ts`** -> AI Confidence: **99.18%**
591. **`packages/next/src/next-devtools/dev-overlay/components/code-frame/code-frame.tsx`** -> AI Confidence: **99.18%**
592. **`packages/next/src/next-devtools/dev-overlay/components/errors/dev-tools-indicator/dev-tools-info/user-preferences.tsx`** -> AI Confidence: **99.18%**
593. **`packages/next/src/next-devtools/dev-overlay/components/errors/error-overlay-layout/error-overlay-layout.tsx`** -> AI Confidence: **99.18%**
594. **`packages/next/src/next-devtools/dev-overlay/shared.ts`** -> AI Confidence: **99.18%**
595. **`packages/next/src/next-devtools/userspace/app/errors/use-error-handler.ts`** -> AI Confidence: **99.18%**
596. **`packages/next/src/server/mcp/tools/get-errors.ts`** -> AI Confidence: **99.18%**
597. **`packages/next/src/server/route-matcher-providers/app-page-route-matcher-provider.ts`** -> AI Confidence: **99.18%**
598. **`packages/next/src/server/route-matcher-providers/pages-api-route-matcher-provider.ts`** -> AI Confidence: **99.18%**
599. **`packages/next/src/server/route-modules/app-page/module.ts`** -> AI Confidence: **99.18%**
600. **`packages/next/src/server/route-modules/pages-api/module.ts`** -> AI Confidence: **99.18%**
601. **`packages/next/src/server/send-payload.ts`** -> AI Confidence: **99.18%**
602. **`packages/next/src/server/web/types.ts`** -> AI Confidence: **99.18%**
603. **`packages/next/src/shared/lib/turbopack/manifest-loader.ts`** -> AI Confidence: **99.18%**
604. **`packages/next/src/types.ts`** -> AI Confidence: **99.18%**
605. **`packages/next/types/$$compiled.internal.d.ts`** -> AI Confidence: **99.18%**
606. **`examples/cms-builder-io/pages/index.js`** -> AI Confidence: **99.18%**
607. **`examples/cms-buttercms/pages/blog/[slug].js`** -> AI Confidence: **99.18%**
608. **`examples/cms-datocms/pages/index.js`** -> AI Confidence: **99.18%**
609. **`examples/cms-drupal/pages/[...slug].js`** -> AI Confidence: **99.18%**
610. **`examples/cms-ghost/pages/index.js`** -> AI Confidence: **99.18%**
611. **`examples/cms-ghost/pages/posts/[slug].js`** -> AI Confidence: **99.18%**
612. **`examples/cms-graphcms/pages/index.js`** -> AI Confidence: **99.18%**
613. **`examples/cms-graphcms/pages/posts/[slug].js`** -> AI Confidence: **99.18%**
614. **`examples/cms-prepr/pages/index.js`** -> AI Confidence: **99.18%**
615. **`examples/cms-storyblok/pages/index.js`** -> AI Confidence: **99.18%**
616. **`examples/cms-tina/pages/posts/[slug].js`** -> AI Confidence: **99.18%**
617. **`examples/cms-umbraco-heartcore/pages/[...slug].js`** -> AI Confidence: **99.18%**
618. **`examples/cms-umbraco-heartcore/pages/index.js`** -> AI Confidence: **99.18%**
619. **`examples/with-neo4j/pages/actor/[name].js`** -> AI Confidence: **99.18%**
620. **`crates/next-api/src/loadable_manifest.rs`** -> AI Confidence: **99.18%**
621. **`crates/next-build-test/src/main.rs`** -> AI Confidence: **99.18%**
622. **`crates/next-core/src/middleware.rs`** -> AI Confidence: **99.18%**
623. **`crates/next-core/src/next_app/app_client_shared_chunks.rs`** -> AI Confidence: **99.18%**
624. **`crates/next-core/src/next_client/runtime_entry.rs`** -> AI Confidence: **99.18%**
625. **`crates/next-core/src/next_client_reference/css_client_reference/css_client_reference_module.rs`** -> AI Confidence: **99.18%**
626. **`crates/next-core/src/next_client_reference/css_client_reference/css_client_reference_transition.rs`** -> AI Confidence: **99.18%**
627. **`crates/next-core/src/next_dynamic/dynamic_module.rs`** -> AI Confidence: **99.18%**
628. **`crates/next-core/src/next_font/google/stylesheet.rs`** -> AI Confidence: **99.18%**
629. **`crates/next-core/src/next_manifests/mod.rs`** -> AI Confidence: **99.18%**
630. **`crates/next-core/src/next_server/resolve.rs`** -> AI Confidence: **99.18%**
631. **`crates/next-core/src/next_server_component/server_component_module.rs`** -> AI Confidence: **99.18%**
632. **`crates/next-core/src/next_server_component/server_component_transition.rs`** -> AI Confidence: **99.18%**
633. **`crates/next-core/src/next_server_utility/server_utility_module.rs`** -> AI Confidence: **99.18%**
634. **`crates/next-core/src/next_server_utility/server_utility_reference.rs`** -> AI Confidence: **99.18%**
635. **`crates/next-core/src/next_server_utility/server_utility_transition.rs`** -> AI Confidence: **99.18%**
636. **`crates/next-core/src/next_shared/transforms/emotion.rs`** -> AI Confidence: **99.18%**
637. **`crates/next-core/src/next_shared/transforms/react_remove_properties.rs`** -> AI Confidence: **99.18%**
638. **`crates/next-core/src/next_shared/transforms/remove_console.rs`** -> AI Confidence: **99.18%**
639. **`crates/next-core/src/next_shared/transforms/styled_components.rs`** -> AI Confidence: **99.18%**
640. **`crates/next-custom-transforms/src/react_compiler.rs`** -> AI Confidence: **99.18%**
641. **`crates/next-custom-transforms/src/transforms/pure.rs`** -> AI Confidence: **99.18%**
642. **`crates/next-custom-transforms/tests/full.rs`** -> AI Confidence: **99.18%**
643. **`crates/next-napi-bindings/src/minify.rs`** -> AI Confidence: **99.18%**
644. **`crates/next-napi-bindings/src/rspack.rs`** -> AI Confidence: **99.18%**
645. **`turbopack/crates/turbo-bincode/src/lib.rs`** -> AI Confidence: **99.18%**
646. **`turbopack/crates/turbo-bincode/src/macro_helpers.rs`** -> AI Confidence: **99.18%**
647. **`turbopack/crates/turbo-frozenmap/src/set.rs`** -> AI Confidence: **99.18%**
648. **`turbopack/crates/turbo-persistence/benches/mod.rs`** -> AI Confidence: **99.18%**
649. **`turbopack/crates/turbo-persistence/src/collector.rs`** -> AI Confidence: **99.18%**
650. **`turbopack/crates/turbo-persistence/src/compaction/interval_map.rs`** -> AI Confidence: **99.18%**
651. **`turbopack/crates/turbo-persistence/src/compaction/naive_interval_map.rs`** -> AI Confidence: **99.18%**
652. **`turbopack/crates/turbo-persistence/src/compression.rs`** -> AI Confidence: **99.18%**
653. **`turbopack/crates/turbo-prehash/src/lib.rs`** -> AI Confidence: **99.18%**
654. **`turbopack/crates/turbo-tasks-auto-hash-map/src/set.rs`** -> AI Confidence: **99.18%**
655. **`turbopack/crates/turbo-tasks-backend/benches/overhead.rs`** -> AI Confidence: **99.18%**
656. **`turbopack/crates/turbo-tasks-backend/benches/stress.rs`** -> AI Confidence: **99.18%**
657. **`turbopack/crates/turbo-tasks-backend/src/backend/counter_map.rs`** -> AI Confidence: **99.18%**
658. **`turbopack/crates/turbo-tasks-backend/src/backend/operation/cleanup_old_edges.rs`** -> AI Confidence: **99.18%**
659. **`turbopack/crates/turbo-tasks-backend/src/backend/operation/leaf_distance_update.rs`** -> AI Confidence: **99.18%**
660. **`turbopack/crates/turbo-tasks-backend/src/data.rs`** -> AI Confidence: **99.18%**
661. **`turbopack/crates/turbo-tasks-backend/src/lib.rs`** -> AI Confidence: **99.18%**
662. **`turbopack/crates/turbo-tasks-backend/src/utils/dash_map_multi.rs`** -> AI Confidence: **99.18%**
663. **`turbopack/crates/turbo-tasks-backend/tests/bug.rs`** -> AI Confidence: **99.18%**
664. **`turbopack/crates/turbo-tasks-backend/tests/collectibles.rs`** -> AI Confidence: **99.18%**
665. **`turbopack/crates/turbo-tasks-backend/tests/invalidation.rs`** -> AI Confidence: **99.18%**
666. **`turbopack/crates/turbo-tasks-backend/tests/random_change.rs`** -> AI Confidence: **99.18%**
667. **`turbopack/crates/turbo-tasks-backend/tests/resolved_vc.rs`** -> AI Confidence: **99.18%**
668. **`turbopack/crates/turbo-tasks-backend/tests/task_statistics.rs`** -> AI Confidence: **99.18%**
669. **`turbopack/crates/turbo-tasks-backend/tests/trait_ref_cell_mode.rs`** -> AI Confidence: **99.18%**
670. **`turbopack/crates/turbo-tasks-backend/tests/transient_vc.rs`** -> AI Confidence: **99.18%**
671. **`turbopack/crates/turbo-tasks-env/src/custom.rs`** -> AI Confidence: **99.18%**
672. **`turbopack/crates/turbo-tasks-fs/src/embed/file.rs`** -> AI Confidence: **99.18%**
673. **`turbopack/crates/turbo-tasks-fs/src/invalidator_map.rs`** -> AI Confidence: **99.18%**
674. **`turbopack/crates/turbo-tasks-fs/src/rope.rs`** -> AI Confidence: **99.18%**
675. **`turbopack/crates/turbo-tasks-fs/src/util.rs`** -> AI Confidence: **99.18%**
676. **`turbopack/crates/turbo-tasks-fuzz/src/symlink_stress.rs`** -> AI Confidence: **99.18%**
677. **`turbopack/crates/turbo-tasks-macros-tests/tests/value_debug.rs`** -> AI Confidence: **99.18%**
678. **`turbopack/crates/turbo-tasks-macros/src/derive/value_debug_format_macro.rs`** -> AI Confidence: **99.18%**
679. **`turbopack/crates/turbo-tasks-macros/src/value_impl_macro.rs`** -> AI Confidence: **99.18%**
680. **`turbopack/crates/turbo-tasks-malloc/src/lib.rs`** -> AI Confidence: **99.18%**
681. **`turbopack/crates/turbo-tasks-testing/src/lib.rs`** -> AI Confidence: **99.18%**
682. **`turbopack/crates/turbo-tasks/src/display.rs`** -> AI Confidence: **99.18%**
683. **`turbopack/crates/turbo-tasks/src/event.rs`** -> AI Confidence: **99.18%**
684. **`turbopack/crates/turbo-tasks/src/graph/graph_traversal.rs`** -> AI Confidence: **99.18%**
685. **`turbopack/crates/turbo-tasks/src/id_factory.rs`** -> AI Confidence: **99.18%**
686. **`turbopack/crates/turbo-tasks/src/join_iter_ext.rs`** -> AI Confidence: **99.18%**
687. **`turbopack/crates/turbo-tasks/src/mapped_read_ref.rs`** -> AI Confidence: **99.18%**
688. **`turbopack/crates/turbo-tasks/src/primitives.rs`** -> AI Confidence: **99.18%**
689. **`turbopack/crates/turbo-tasks/src/read_ref.rs`** -> AI Confidence: **99.18%**
690. **`turbopack/crates/turbo-tasks/src/state.rs`** -> AI Confidence: **99.18%**
691. **`turbopack/crates/turbo-tasks/src/task/function.rs`** -> AI Confidence: **99.18%**
692. **`turbopack/crates/turbo-tasks/src/task_statistics.rs`** -> AI Confidence: **99.18%**
693. **`turbopack/crates/turbo-tasks/src/vc/cast.rs`** -> AI Confidence: **99.18%**
694. **`turbopack/crates/turbo-tasks/src/vc/read.rs`** -> AI Confidence: **99.18%**
695. **`turbopack/crates/turbo-tasks/src/vc/traits.rs`** -> AI Confidence: **99.18%**
696. **`turbopack/crates/turbopack-bench/src/util/mod.rs`** -> AI Confidence: **99.18%**
697. **`turbopack/crates/turbopack-browser/src/ecmascript/list/asset.rs`** -> AI Confidence: **99.18%**
698. **`turbopack/crates/turbopack-browser/src/ecmascript/merged/content.rs`** -> AI Confidence: **99.18%**
699. **`turbopack/crates/turbopack-cli-utils/src/runtime_entry.rs`** -> AI Confidence: **99.18%**
700. **`turbopack/crates/turbopack-cli/benches/small_apps.rs`** -> AI Confidence: **99.18%**
701. **`turbopack/crates/turbopack-cli/src/contexts.rs`** -> AI Confidence: **99.18%**
702. **`turbopack/crates/turbopack-cli/src/main.rs`** -> AI Confidence: **99.18%**
703. **`turbopack/crates/turbopack-core/src/asset.rs`** -> AI Confidence: **99.18%**
704. **`turbopack/crates/turbopack-core/src/chunk/chunk_id_strategy.rs`** -> AI Confidence: **99.18%**
705. **`turbopack/crates/turbopack-core/src/chunk/chunking_context.rs`** -> AI Confidence: **99.18%**
706. **`turbopack/crates/turbopack-core/src/context.rs`** -> AI Confidence: **99.18%**
707. **`turbopack/crates/turbopack-core/src/generated_code_source.rs`** -> AI Confidence: **99.18%**
708. **`turbopack/crates/turbopack-core/src/issue/mod.rs`** -> AI Confidence: **99.18%**
709. **`turbopack/crates/turbopack-core/src/module_graph/traced_di_graph.rs`** -> AI Confidence: **99.18%**
710. **`turbopack/crates/turbopack-core/src/proxied_asset.rs`** -> AI Confidence: **99.18%**
711. **`turbopack/crates/turbopack-core/src/raw_module.rs`** -> AI Confidence: **99.18%**
712. **`turbopack/crates/turbopack-core/src/raw_output.rs`** -> AI Confidence: **99.18%**
713. **`turbopack/crates/turbopack-core/src/resolve/origin.rs`** -> AI Confidence: **99.18%**
714. **`turbopack/crates/turbopack-core/src/source_map/mod.rs`** -> AI Confidence: **99.18%**
715. **`turbopack/crates/turbopack-core/src/target.rs`** -> AI Confidence: **99.18%**
716. **`turbopack/crates/turbopack-core/src/virtual_output.rs`** -> AI Confidence: **99.18%**
717. **`turbopack/crates/turbopack-core/src/virtual_source.rs`** -> AI Confidence: **99.18%**
718. **`turbopack/crates/turbopack-dev-server/src/lib.rs`** -> AI Confidence: **99.18%**
719. **`turbopack/crates/turbopack-dev-server/src/source/combined.rs`** -> AI Confidence: **99.18%**
720. **`turbopack/crates/turbopack-dev-server/src/source/headers.rs`** -> AI Confidence: **99.18%**
721. **`turbopack/crates/turbopack-dev-server/src/source/lazy_instantiated.rs`** -> AI Confidence: **99.18%**
722. **`turbopack/crates/turbopack-ecmascript-plugins/src/transform/styled_components.rs`** -> AI Confidence: **99.18%**
723. **`turbopack/crates/turbopack-ecmascript-plugins/src/transform/swc_ecma_transform_plugins.rs`** -> AI Confidence: **99.18%**
724. **`turbopack/crates/turbopack-ecmascript/src/chunk/chunk_type.rs`** -> AI Confidence: **99.18%**
725. **`turbopack/crates/turbopack-ecmascript/src/chunk/content.rs`** -> AI Confidence: **99.18%**
726. **`turbopack/crates/turbopack-ecmascript/src/minify.rs`** -> AI Confidence: **99.18%**
727. **`turbopack/crates/turbopack-ecmascript/src/references/amd.rs`** -> AI Confidence: **99.18%**
728. **`turbopack/crates/turbopack-ecmascript/src/references/cjs.rs`** -> AI Confidence: **99.18%**
729. **`turbopack/crates/turbopack-ecmascript/src/references/esm/meta.rs`** -> AI Confidence: **99.18%**
730. **`turbopack/crates/turbopack-ecmascript/src/references/esm/module_id.rs`** -> AI Confidence: **99.18%**
731. **`turbopack/crates/turbopack-ecmascript/src/references/exports_info.rs`** -> AI Confidence: **99.18%**
732. **`turbopack/crates/turbopack-ecmascript/src/references/typescript.rs`** -> AI Confidence: **99.18%**
733. **`turbopack/crates/turbopack-ecmascript/src/references/unreachable.rs`** -> AI Confidence: **99.18%**
734. **`turbopack/crates/turbopack-ecmascript/src/runtime_functions.rs`** -> AI Confidence: **99.18%**
735. **`turbopack/crates/turbopack-ecmascript/src/single_file_ecmascript_output.rs`** -> AI Confidence: **99.18%**
736. **`turbopack/crates/turbopack-ecmascript/src/text/mod.rs`** -> AI Confidence: **99.18%**
737. **`turbopack/crates/turbopack-ecmascript/src/tree_shake/graph.rs`** -> AI Confidence: **99.18%**
738. **`turbopack/crates/turbopack-env/src/asset.rs`** -> AI Confidence: **99.18%**
739. **`turbopack/crates/turbopack-node/src/worker_pool/operation.rs`** -> AI Confidence: **99.18%**
740. **`turbopack/crates/turbopack-node/src/worker_pool/worker_thread.rs`** -> AI Confidence: **99.18%**
741. **`turbopack/crates/turbopack-nodejs/src/ecmascript/node/version.rs`** -> AI Confidence: **99.18%**
742. **`turbopack/crates/turbopack-resolve/src/resolve_options_context.rs`** -> AI Confidence: **99.18%**
743. **`turbopack/crates/turbopack-static/src/fixed.rs`** -> AI Confidence: **99.18%**
744. **`turbopack/crates/turbopack-static/src/output_asset.rs`** -> AI Confidence: **99.18%**
745. **`turbopack/crates/turbopack-swc-ast-explorer/src/main.rs`** -> AI Confidence: **99.18%**
746. **`turbopack/crates/turbopack-swc-utils/src/emitter.rs`** -> AI Confidence: **99.18%**
747. **`turbopack/crates/turbopack-trace-server/src/bottom_up.rs`** -> AI Confidence: **99.18%**
748. **`turbopack/crates/turbopack-trace-server/src/reader/turbopack.rs`** -> AI Confidence: **99.18%**
749. **`turbopack/crates/turbopack-trace-server/src/server.rs`** -> AI Confidence: **99.18%**
750. **`turbopack/crates/turbopack-trace-server/src/store.rs`** -> AI Confidence: **99.18%**
751. **`turbopack/crates/turbopack-tracing/benches/node_file_trace.rs`** -> AI Confidence: **99.18%**
752. **`turbopack/crates/turbopack-wasm/src/output_asset.rs`** -> AI Confidence: **99.18%**
753. **`turbopack/crates/turbopack/examples/turbopack.rs`** -> AI Confidence: **99.18%**
754. **`turbopack/crates/turbopack/src/global_module_ids.rs`** -> AI Confidence: **99.18%**
755. **`turbopack/crates/turbopack/src/module_options/module_rule.rs`** -> AI Confidence: **99.18%**
756. **`turbopack/crates/turbopack/src/transition/mod.rs`** -> AI Confidence: **99.18%**
757. **`turbopack/xtask/src/main.rs`** -> AI Confidence: **99.18%**
758. **`turbopack/xtask/src/nft_bench.rs`** -> AI Confidence: **99.18%**
759. **`.conductor/scripts/setup.sh`** -> AI Confidence: **99.17%**
760. **`scripts/deploy-examples.sh`** -> AI Confidence: **99.17%**
761. **`scripts/release-stats.sh`** -> AI Confidence: **99.17%**
762. **`scripts/setup-node.sh`** -> AI Confidence: **99.17%**
763. **`examples/cms-wordpress/src/utils/fetchGraphQL.ts`** -> AI Confidence: **99.17%**
764. **`examples/prisma-postgres/app/setup/page.tsx`** -> AI Confidence: **99.17%**
765. **`examples/with-docker/app/page.tsx`** -> AI Confidence: **99.17%**
766. **`examples/with-sitemap/app/page.tsx`** -> AI Confidence: **99.17%**
767. **`packages/create-next-app/templates/default-tw/ts/pages/index.tsx`** -> AI Confidence: **99.17%**
768. **`packages/font/src/google/find-font-files-in-css.ts`** -> AI Confidence: **99.17%**
769. **`packages/font/src/google/loader.test.ts`** -> AI Confidence: **99.17%**
770. **`packages/font/src/google/validate-google-font-function-call.ts`** -> AI Confidence: **99.17%**
771. **`packages/next-routing/src/middleware.ts`** -> AI Confidence: **99.17%**
772. **`packages/next/src/client/app-link-gc.ts`** -> AI Confidence: **99.17%**
773. **`packages/next/src/client/components/handle-isr-error.tsx`** -> AI Confidence: **99.17%**
774. **`packages/next/src/lib/fs/rename.ts`** -> AI Confidence: **99.17%**
775. **`packages/next/src/server/app-render/react-large-shell-error.ts`** -> AI Confidence: **99.17%**
776. **`packages/next/src/server/normalizers/request/segment-prefix-rsc.test.ts`** -> AI Confidence: **99.17%**
777. **`packages/next/src/shared/lib/fnv1a.ts`** -> AI Confidence: **99.17%**
778. **`packages/next/src/shared/lib/image-loader.ts`** -> AI Confidence: **99.17%**
779. **`packages/next/src/shared/lib/router/utils/get-next-pathname-info.ts`** -> AI Confidence: **99.17%**
780. **`packages/next/src/shared/lib/router/utils/parse-path.ts`** -> AI Confidence: **99.17%**
781. **`evals/evals/agent-030-app-router-migration-hard/pages/api/posts/index.js`** -> AI Confidence: **99.17%**
782. **`examples/with-facebook-pixel/public/scripts/pixel.js`** -> AI Confidence: **99.17%**
783. **`packages/create-next-app/templates/default-tw/js/pages/index.js`** -> AI Confidence: **99.17%**
784. **`packages/font/google/index.js`** -> AI Confidence: **99.17%**
785. **`packages/font/local/index.js`** -> AI Confidence: **99.17%**
786. **`packages/next/src/compiled/@babel/runtime/helpers/applyDecoratedDescriptor.js`** -> AI Confidence: **99.17%**
787. **`packages/next/src/compiled/@babel/runtime/helpers/applyDecs2203.js`** -> AI Confidence: **99.17%**
788. **`packages/next/src/compiled/@babel/runtime/helpers/applyDecs2311.js`** -> AI Confidence: **99.17%**
789. **`packages/next/src/compiled/@babel/runtime/helpers/esm/applyDecs2203.js`** -> AI Confidence: **99.17%**
790. **`packages/next/src/compiled/@babel/runtime/helpers/esm/inherits.js`** -> AI Confidence: **99.17%**
791. **`packages/next/src/compiled/@babel/runtime/helpers/esm/initializerDefineProperty.js`** -> AI Confidence: **99.17%**
792. **`packages/next/src/compiled/@babel/runtime/helpers/esm/iterableToArrayLimit.js`** -> AI Confidence: **99.17%**
793. **`packages/next/src/compiled/@babel/runtime/helpers/esm/tsRewriteRelativeImportExtensions.js`** -> AI Confidence: **99.17%**
794. **`packages/next/src/compiled/@babel/runtime/helpers/esm/unsupportedIterableToArray.js`** -> AI Confidence: **99.17%**
795. **`packages/next/src/compiled/@babel/runtime/helpers/esm/using.js`** -> AI Confidence: **99.17%**
796. **`packages/next/src/compiled/@babel/runtime/helpers/iterableToArrayLimit.js`** -> AI Confidence: **99.17%**
797. **`packages/next/src/compiled/@babel/runtime/helpers/setFunctionName.js`** -> AI Confidence: **99.17%**
798. **`packages/next/src/compiled/@babel/runtime/helpers/typeof.js`** -> AI Confidence: **99.17%**
799. **`packages/next/src/compiled/@babel/runtime/helpers/unsupportedIterableToArray.js`** -> AI Confidence: **99.17%**
800. **`packages/next/src/compiled/@babel/runtime/helpers/using.js`** -> AI Confidence: **99.17%**
801. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.browser.production.js`** -> AI Confidence: **99.17%**
802. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js`** -> AI Confidence: **99.17%**
803. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js`** -> AI Confidence: **99.17%**
804. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.production.js`** -> AI Confidence: **99.17%**
805. **`packages/next/src/compiled/react-dom-experimental/cjs/react-dom.production.js`** -> AI Confidence: **99.17%**
806. **`packages/next/src/compiled/react-dom/cjs/react-dom-server-legacy.browser.production.js`** -> AI Confidence: **99.17%**
807. **`packages/next/src/compiled/react-dom/cjs/react-dom-server.browser.development.js`** -> AI Confidence: **99.17%**
808. **`packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.development.js`** -> AI Confidence: **99.17%**
809. **`packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.production.js`** -> AI Confidence: **99.17%**
810. **`packages/next/src/compiled/react-dom/cjs/react-dom.production.js`** -> AI Confidence: **99.17%**
811. **`packages/next/src/compiled/react-experimental/cjs/react-jsx-dev-runtime.react-server.production.js`** -> AI Confidence: **99.17%**
812. **`packages/next/src/compiled/react-experimental/cjs/react-jsx-runtime.production.js`** -> AI Confidence: **99.17%**
813. **`packages/next/src/compiled/react-experimental/cjs/react-jsx-runtime.profiling.js`** -> AI Confidence: **99.17%**
814. **`packages/next/src/compiled/react-experimental/cjs/react-jsx-runtime.react-server.production.js`** -> AI Confidence: **99.17%**
815. **`packages/next/src/compiled/react-is/cjs/react-is.development.js`** -> AI Confidence: **99.17%**
816. **`packages/next/src/compiled/react-is/cjs/react-is.production.js`** -> AI Confidence: **99.17%**
817. **`packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-client.browser.development.js`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `packages/next/src/next-devtools/dev-overlay/storybook/errors.ts` -> **11.6566%** Exposure
- `scripts/profile-next-dev-boot.js` -> **0.0001%** Exposure
### Exploit Generation Surface
- `scripts/benchmark-boot-time.sh` -> **100.0%** Exposure
- `scripts/next-with-deps.sh` -> **100.0%** Exposure
- `scripts/test-stats-benchmark.sh` -> **100.0%** Exposure
- `bench/render-pipeline/analyze-profiles.ts` -> **100.0%** Exposure
- `bench/render-pipeline/benchmark.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bench/basic-app/benchmark.sh` -> **100.0%** Exposure
- `packages/next-codemod/scripts/test-upgrade-fixture.sh` -> **100.0%** Exposure
- `scripts/benchmark-boot-time.sh` -> **100.0%** Exposure
- `scripts/test-stats-benchmark.sh` -> **100.0%** Exposure
- `examples/api-routes-apollo-server-and-client/pages/index.tsx` -> **100.0%** Exposure
### Raw Memory Manipulation
- `turbopack/crates/turbo-tasks-malloc/src/lib.rs` -> **0.0038%** Exposure
- `turbopack/crates/turbo-frozenmap/src/map.rs` -> **0.0002%** Exposure
- `turbopack/crates/turbo-frozenmap/src/set.rs` -> **0.0001%** Exposure
- `turbopack/crates/turbo-rcstr/src/lib.rs` -> **0.0001%** Exposure
- `turbopack/crates/turbo-tasks-auto-hash-map/src/set.rs` -> **0.0001%** Exposure
### Hardcoded Payload Artifacts
- `examples/with-supertokens/app/config/backend.ts` -> **99.999%** Exposure
- `examples/with-algolia-react-instantsearch/components/Search.tsx` -> **99.7922%** Exposure
### Algorithmic DoS Exposure
- `scripts/benchmark-boot-time.sh` -> **100.0%** Exposure
- `.github/actions/next-integration-stat/src/index.ts` -> **100.0%** Exposure
- `.github/actions/validate-docs-links/src/index.ts` -> **100.0%** Exposure
- `bench/render-pipeline/benchmark.ts` -> **100.0%** Exposure
- `examples/cms-payload/components/Media/Image/index.tsx` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `36` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24350` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js` (JAVASCRIPT) -> Cumulative Risk: **970.39**
- **Archetype:** `file_cluster_8` (Distance: 14.715 IQR)
- **Magnitude:** 24419.62 | **LOC:** 11122 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `renderElement` (Impact: 6055.2), `pushStartInstance` (Impact: 4823.7), `validateProperty` (Impact: 964.7)

### 2. `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js` (JAVASCRIPT) -> Cumulative Risk: **969.49**
- **Archetype:** `file_cluster_8` (Distance: 14.724 IQR)
- **Magnitude:** 24931.04 | **LOC:** 11520 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `renderElement` (Impact: 6037.7), `pushStartInstance` (Impact: 4823.7), `validateProperty` (Impact: 964.7)

### 3. `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js` (JAVASCRIPT) -> Cumulative Risk: **943.47**
- **Archetype:** `file_cluster_8` (Distance: 14.641 IQR)
- **Magnitude:** 24804.44 | **LOC:** 11329 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `renderElement` (Impact: 6037.7), `pushStartInstance` (Impact: 4790.6), `validateProperty` (Impact: 964.7)

### 4. `packages/next/src/compiled/react-dom/cjs/react-dom-server.browser.development.js` (JAVASCRIPT) -> Cumulative Risk: **936.48**
- **Archetype:** `file_cluster_8` (Distance: 14.631 IQR)
- **Magnitude:** 24288.56 | **LOC:** 10923 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `renderElement` (Impact: 6055.2), `pushStartInstance` (Impact: 4790.6), `validateProperty` (Impact: 964.7)

### 5. `packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.development.js` (JAVASCRIPT) -> Cumulative Risk: **931.15**
- **Archetype:** `file_cluster_8` (Distance: 14.625 IQR)
- **Magnitude:** 24303.14 | **LOC:** 10942 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `renderElement` (Impact: 6055.2), `pushStartInstance` (Impact: 4790.6), `validateProperty` (Impact: 964.7)

### 6. `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js` (JAVASCRIPT) -> Cumulative Risk: **930.62**
- **Archetype:** `file_cluster_8` (Distance: 14.635 IQR)
- **Magnitude:** 24825.54 | **LOC:** 11354 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `renderElement` (Impact: 6037.7), `pushStartInstance` (Impact: 4790.6), `validateProperty` (Impact: 964.7)

### 7. `packages/next/src/compiled/react/cjs/react.react-server.production.js` (JAVASCRIPT) -> Cumulative Risk: **911.67**
- **Archetype:** `file_cluster_8` (Distance: 13.68 IQR)
- **Magnitude:** 1013.7 | **LOC:** 437 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `mapIntoArray` (Impact: 519.9), `cache` (Impact: 57.4), `resolveThenable` (Impact: 49.2)

### 8. `packages/next/src/compiled/react/cjs/react.development.js` (JAVASCRIPT) -> Cumulative Risk: **906.51**
- **Archetype:** `file_cluster_8` (Distance: 13.722 IQR)
- **Magnitude:** 3092.18 | **LOC:** 1331 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `mapIntoArray` (Impact: 795.1), `getComponentNameFromType` (Impact: 306.1), `act` (Impact: 272.3)

### 9. `packages/next/src/compiled/react/cjs/react.react-server.development.js` (JAVASCRIPT) -> Cumulative Risk: **905.94**
- **Archetype:** `file_cluster_8` (Distance: 13.312 IQR)
- **Magnitude:** 2206.34 | **LOC:** 879 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `mapIntoArray` (Impact: 795.1), `getComponentNameFromType` (Impact: 306.1), `forwardRef` (Impact: 132.0)

### 10. `packages/next/src/compiled/react/cjs/react.production.js` (JAVASCRIPT) -> Cumulative Risk: **898.58**
- **Archetype:** `file_cluster_8` (Distance: 13.809 IQR)
- **Magnitude:** 1119.08 | **LOC:** 566 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 91.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9941%)
- **Heaviest Functions:** `mapIntoArray` (Impact: 519.8), `resolveThenable` (Impact: 49.2), `cloneElement` (Impact: 49.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.724 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.897 IQR)
- **Top Global Matches:** file_cluster_8: 14.724, file_cluster_17: 14.893, file_cluster_11: 14.992
- **Magnitude:** 24931.04 | **LOC:** 11520 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 131
- **Risk Profile:** Cognitive Load (83.1204%), Tech Debt (17.8224%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 6037.7 | O(2^N) | DB: 128)
  * `pushStartInstance` (Impact: 4823.7 | O(N^6) | DB: 131)
  * `validateProperty` (Impact: 964.7 | O(N^5) | DB: 1)
  * `pushAttribute` (Impact: 757.1 | O(N^4) | DB: 10)
  * `finishedTask` (Impact: 594.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3059`, `structural_boundaries: 985`, `args: 363`, `func_start: 992`
* *Risk/State:* `safety_bypasses: 318`, `high_risk_execution: 38`, `state_mutation: 2268`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 10`
* *Architecture:* `io: 26`, `api: 14`, `concurrency: 128`, `import: 7`
* *Defense:* `safety: 1453`, `doc: 1`, `test: 4`, `immutability_locks: 9`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, util, react-dom-experimental, react-experimental, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.635 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.862 IQR)
- **Top Global Matches:** file_cluster_8: 14.635, file_cluster_17: 14.809, file_cluster_11: 14.925
- **Magnitude:** 24825.54 | **LOC:** 11354 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 130
- **Risk Profile:** Cognitive Load (83.2368%), Tech Debt (17.102%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 6037.7 | O(2^N) | DB: 128)
  * `pushStartInstance` (Impact: 4790.6 | O(N^6) | DB: 130)
  * `validateProperty` (Impact: 964.7 | O(N^5) | DB: 1)
  * `pushAttribute` (Impact: 757.5 | O(N^4) | DB: 10)
  * `finishedTask` (Impact: 594.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3009`, `structural_boundaries: 962`, `args: 330`, `func_start: 973`
* *Risk/State:* `safety_bypasses: 268`, `high_risk_execution: 37`, `state_mutation: 2243`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 8`
* *Architecture:* `io: 26`, `api: 10`, `concurrency: 121`, `import: 3`
* *Defense:* `safety: 1443`, `doc: 1`, `test: 4`, `immutability_locks: 9`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-experimental, react-dom-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.641 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.865 IQR)
- **Top Global Matches:** file_cluster_8: 14.641, file_cluster_17: 14.813, file_cluster_11: 14.929
- **Magnitude:** 24804.44 | **LOC:** 11329 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 130
- **Risk Profile:** Cognitive Load (84.0524%), Tech Debt (17.131%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 6037.7 | O(2^N) | DB: 128)
  * `pushStartInstance` (Impact: 4790.6 | O(N^6) | DB: 130)
  * `validateProperty` (Impact: 964.7 | O(N^5) | DB: 1)
  * `pushAttribute` (Impact: 757.5 | O(N^4) | DB: 10)
  * `finishedTask` (Impact: 594.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3005`, `structural_boundaries: 958`, `args: 329`, `func_start: 974`
* *Risk/State:* `safety_bypasses: 270`, `high_risk_execution: 37`, `state_mutation: 2248`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 8`
* *Architecture:* `io: 26`, `api: 11`, `concurrency: 139`, `import: 3`
* *Defense:* `safety: 1437`, `doc: 1`, `test: 4`, `immutability_locks: 9`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-experimental, react-dom-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-profiling.profiling.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.039 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.724 IQR)
- **Top Global Matches:** file_cluster_8: 15.039, file_cluster_17: 15.332, file_cluster_11: 15.388
- **Magnitude:** 24728.44 | **LOC:** 22321 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (71.351%), Tech Debt (8.1722%)
**Top Internal Functions/Classes:**
  * `setProp` (Impact: 2583.0 | O(2^N) | DB: 30)
  * `dispatchEventForPluginEventSystem` (Impact: 1647.6 | O(N^5) | DB: 19)
  * `completeRoot` (Impact: 1333.7 | O(2^N) | DB: 17)
  * `updateProperties` (Impact: 1028.9 | O(N^4) | DB: 11)
  * `startViewTransition` (Impact: 806.1 | O(2^N) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7007`, `structural_boundaries: 2123`, `args: 834`, `func_start: 2180`
* *Risk/State:* `safety_bypasses: 375`, `high_risk_execution: 3`, `state_mutation: 3532`, `duplicate_logic: 7`
* *Architecture:* `io: 24`, `api: 30`, `concurrency: 132`, `import: 3`
* *Defense:* `safety: 3595`, `doc: 1`, `cleanup: 69`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-experimental, scheduler-experimental, react-dom-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.715 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.901 IQR)
- **Top Global Matches:** file_cluster_8: 14.715, file_cluster_17: 14.882, file_cluster_11: 14.984
- **Magnitude:** 24419.62 | **LOC:** 11122 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 131
- **Risk Profile:** Cognitive Load (83.4611%), Tech Debt (18.3354%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 6055.2 | O(2^N) | DB: 123)
  * `pushStartInstance` (Impact: 4823.7 | O(N^6) | DB: 131)
  * `validateProperty` (Impact: 964.7 | O(N^5) | DB: 1)
  * `pushAttribute` (Impact: 731.6 | O(N^4) | DB: 10)
  * `finishedTask` (Impact: 594.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2950`, `structural_boundaries: 966`, `args: 352`, `func_start: 958`
* *Risk/State:* `safety_bypasses: 309`, `high_risk_execution: 36`, `state_mutation: 2211`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 10`
* *Architecture:* `io: 26`, `api: 14`, `concurrency: 124`, `import: 7`
* *Defense:* `safety: 1407`, `doc: 1`, `test: 3`, `immutability_locks: 9`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, util, react-dom, react, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.625 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.866 IQR)
- **Top Global Matches:** file_cluster_8: 14.625, file_cluster_17: 14.797, file_cluster_11: 14.917
- **Magnitude:** 24303.14 | **LOC:** 10942 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 130
- **Risk Profile:** Cognitive Load (83.6877%), Tech Debt (17.599%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 6055.2 | O(2^N) | DB: 123)
  * `pushStartInstance` (Impact: 4790.6 | O(N^6) | DB: 130)
  * `validateProperty` (Impact: 964.7 | O(N^5) | DB: 1)
  * `pushAttribute` (Impact: 732.0 | O(N^4) | DB: 10)
  * `finishedTask` (Impact: 594.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2898`, `structural_boundaries: 943`, `args: 319`, `func_start: 935`
* *Risk/State:* `safety_bypasses: 259`, `high_risk_execution: 35`, `state_mutation: 2188`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 8`
* *Architecture:* `io: 26`, `api: 10`, `concurrency: 117`, `import: 3`
* *Defense:* `safety: 1393`, `doc: 1`, `test: 3`, `immutability_locks: 9`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server.browser.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.631 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.867 IQR)
- **Top Global Matches:** file_cluster_8: 14.631, file_cluster_17: 14.802, file_cluster_11: 14.922
- **Magnitude:** 24288.56 | **LOC:** 10923 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 130
- **Risk Profile:** Cognitive Load (84.3488%), Tech Debt (17.6233%)
**Top Internal Functions/Classes:**
  * `renderElement` (Impact: 6055.2 | O(2^N) | DB: 123)
  * `pushStartInstance` (Impact: 4790.6 | O(N^6) | DB: 130)
  * `validateProperty` (Impact: 964.7 | O(N^5) | DB: 1)
  * `pushAttribute` (Impact: 732.0 | O(N^4) | DB: 10)
  * `finishedTask` (Impact: 594.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2897`, `structural_boundaries: 938`, `args: 317`, `func_start: 935`
* *Risk/State:* `safety_bypasses: 261`, `high_risk_execution: 35`, `state_mutation: 2192`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 8`
* *Architecture:* `io: 26`, `api: 11`, `concurrency: 130`, `import: 3`
* *Defense:* `safety: 1391`, `doc: 1`, `test: 3`, `immutability_locks: 9`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-unstable_testing.production.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.053 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.722 IQR)
- **Top Global Matches:** file_cluster_8: 15.053, file_cluster_17: 15.324, file_cluster_11: 15.387
- **Magnitude:** 23155.76 | **LOC:** 20540 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (49.1787%), Tech Debt (8.7556%)
**Top Internal Functions/Classes:**
  * `setProp` (Impact: 2583.0 | O(2^N) | DB: 30)
  * `dispatchEventForPluginEventSystem` (Impact: 1647.6 | O(N^5) | DB: 19)
  * `updateProperties` (Impact: 1028.9 | O(N^4) | DB: 11)
  * `completeRoot` (Impact: 995.3 | O(2^N) | DB: 18)
  * `setInitialProperties` (Impact: 798.8 | O(N^4) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6526`, `structural_boundaries: 2074`, `args: 801`, `func_start: 1980`
* *Risk/State:* `safety_bypasses: 350`, `high_risk_execution: 3`, `state_mutation: 3470`, `duplicate_logic: 7`, `orphaned_logic: 14`
* *Architecture:* `io: 24`, `api: 13`, `concurrency: 134`, `import: 3`
* *Defense:* `safety: 3323`, `doc: 1`, `cleanup: 70`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-experimental, scheduler-experimental, react-dom-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-client.production.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.035 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.719 IQR)
- **Top Global Matches:** file_cluster_8: 15.035, file_cluster_17: 15.309, file_cluster_11: 15.374
- **Magnitude:** 22705.64 | **LOC:** 20073 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (48.8355%), Tech Debt (8.2404%)
**Top Internal Functions/Classes:**
  * `setProp` (Impact: 2583.0 | O(2^N) | DB: 30)
  * `dispatchEventForPluginEventSystem` (Impact: 1647.6 | O(N^5) | DB: 19)
  * `updateProperties` (Impact: 1028.9 | O(N^4) | DB: 11)
  * `completeRoot` (Impact: 995.3 | O(2^N) | DB: 18)
  * `setInitialProperties` (Impact: 798.8 | O(N^4) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6363`, `structural_boundaries: 2008`, `args: 775`, `func_start: 1953`
* *Risk/State:* `safety_bypasses: 346`, `high_risk_execution: 3`, `state_mutation: 3360`, `duplicate_logic: 7`
* *Architecture:* `io: 24`, `api: 17`, `concurrency: 134`, `import: 3`
* *Defense:* `safety: 3263`, `doc: 1`, `cleanup: 69`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-experimental, scheduler-experimental, react-dom-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-profiling.profiling.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.954 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.708 IQR)
- **Top Global Matches:** file_cluster_8: 14.954, file_cluster_17: 15.249, file_cluster_11: 15.307
- **Magnitude:** 21697.18 | **LOC:** 20362 | **CtrlFlow:** 76.4% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (45.8524%), Tech Debt (8.2308%)
**Top Internal Functions/Classes:**
  * `setProp` (Impact: 2476.6 | O(2^N) | DB: 30)
  * `dispatchEventForPluginEventSystem` (Impact: 1565.2 | O(N^5) | DB: 18)
  * `startViewTransition` (Impact: 1132.4 | O(2^N) | DB: 16)
  * `updateProperties` (Impact: 1028.9 | O(N^4) | DB: 11)
  * `commitPassiveMountOnFiber` (Impact: 818.3 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6386`, `structural_boundaries: 1973`, `args: 784`, `func_start: 2015`
* *Risk/State:* `safety_bypasses: 334`, `high_risk_execution: 4`, `state_mutation: 3161`, `duplicate_logic: 7`
* *Architecture:* `io: 24`, `api: 35`, `concurrency: 133`, `import: 3`
* *Defense:* `safety: 3250`, `doc: 1`, `cleanup: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom, scheduler, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-client.production.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.942 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.703 IQR)
- **Top Global Matches:** file_cluster_8: 14.942, file_cluster_17: 15.219, file_cluster_11: 15.288
- **Magnitude:** 19438.74 | **LOC:** 18267 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 91.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (48.384%), Tech Debt (8.308%)
**Top Internal Functions/Classes:**
  * `setProp` (Impact: 2476.6 | O(2^N) | DB: 30)
  * `dispatchEventForPluginEventSystem` (Impact: 1565.2 | O(N^5) | DB: 18)
  * `updateProperties` (Impact: 1028.9 | O(N^4) | DB: 11)
  * `startViewTransition` (Impact: 995.7 | O(2^N) | DB: 16)
  * `setInitialProperties` (Impact: 646.5 | O(N^4) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5785`, `structural_boundaries: 1857`, `args: 726`, `func_start: 1800`
* *Risk/State:* `safety_bypasses: 305`, `high_risk_execution: 4`, `state_mutation: 2982`, `duplicate_logic: 7`
* *Architecture:* `io: 24`, `api: 17`, `concurrency: 136`, `import: 3`
* *Defense:* `safety: 2936`, `doc: 1`, `cleanup: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom, scheduler, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-server.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.55 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.069 IQR)
- **Top Global Matches:** file_cluster_8: 14.55, file_cluster_4: 14.682, file_cluster_17: 14.755
- **Magnitude:** 15458.38 | **LOC:** 6892 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 70.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (69.7031%), Tech Debt (18.4627%)
**Top Internal Functions/Classes:**
  * `renderModelDestructive` (Impact: 1971.9 | O(2^N) | DB: 9)
  * `visitAsyncNode` (Impact: 1105.2 | O(2^N) | DB: 13)
  * `renderDebugModel` (Impact: 892.3 | O(N^5) | DB: 24)
  * `renderElement` (Impact: 700.0 | O(2^N) | DB: 5)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1784`, `structural_boundaries: 843`, `args: 367`, `func_start: 626`
* *Risk/State:* `safety_bypasses: 209`, `state_mutation: 1450`, `fragile_debt: 9`, `duplicate_logic: 13`
* *Architecture:* `io: 6`, `api: 39`, `concurrency: 344`, `import: 7`
* *Defense:* `safety: 1122`, `doc: 1`, `test: 4`, `cleanup: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, util, react, react-dom, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-server.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.557 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.07 IQR)
- **Top Global Matches:** file_cluster_8: 14.557, file_cluster_4: 14.693, file_cluster_17: 14.763
- **Magnitude:** 15443.66 | **LOC:** 6890 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 72.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (69.3002%), Tech Debt (18.4649%)
**Top Internal Functions/Classes:**
  * `renderModelDestructive` (Impact: 1971.9 | O(2^N) | DB: 9)
  * `visitAsyncNode` (Impact: 1105.2 | O(2^N) | DB: 13)
  * `renderDebugModel` (Impact: 892.3 | O(N^5) | DB: 24)
  * `renderElement` (Impact: 700.0 | O(2^N) | DB: 5)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1783`, `structural_boundaries: 842`, `args: 367`, `func_start: 626`
* *Risk/State:* `safety_bypasses: 208`, `state_mutation: 1444`, `fragile_debt: 9`, `duplicate_logic: 13`
* *Architecture:* `io: 6`, `api: 39`, `concurrency: 339`, `import: 7`
* *Defense:* `safety: 1120`, `doc: 1`, `test: 4`, `cleanup: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, util, react, react-dom, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-server.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.543 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.069 IQR)
- **Top Global Matches:** file_cluster_8: 14.543, file_cluster_4: 14.675, file_cluster_17: 14.749
- **Magnitude:** 15345.84 | **LOC:** 6840 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 70.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (69.8244%), Tech Debt (18.5794%)
**Top Internal Functions/Classes:**
  * `renderModelDestructive` (Impact: 1912.6 | O(2^N) | DB: 9)
  * `visitAsyncNode` (Impact: 1105.2 | O(2^N) | DB: 13)
  * `renderDebugModel` (Impact: 892.3 | O(N^5) | DB: 24)
  * `renderElement` (Impact: 700.0 | O(2^N) | DB: 5)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1774`, `structural_boundaries: 838`, `args: 365`, `func_start: 621`
* *Risk/State:* `safety_bypasses: 202`, `state_mutation: 1436`, `fragile_debt: 9`, `duplicate_logic: 13`
* *Architecture:* `io: 6`, `api: 39`, `concurrency: 344`, `import: 7`
* *Defense:* `safety: 1114`, `doc: 1`, `test: 4`, `cleanup: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, util, react, react-dom, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-turbopack/cjs/react-server-dom-turbopack-server.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.55 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.07 IQR)
- **Top Global Matches:** file_cluster_8: 14.55, file_cluster_4: 14.685, file_cluster_17: 14.756
- **Magnitude:** 15331.12 | **LOC:** 6838 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 72.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (69.419%), Tech Debt (18.5817%)
**Top Internal Functions/Classes:**
  * `renderModelDestructive` (Impact: 1912.6 | O(2^N) | DB: 9)
  * `visitAsyncNode` (Impact: 1105.2 | O(2^N) | DB: 13)
  * `renderDebugModel` (Impact: 892.3 | O(N^5) | DB: 24)
  * `renderElement` (Impact: 700.0 | O(2^N) | DB: 5)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1773`, `structural_boundaries: 837`, `args: 365`, `func_start: 621`
* *Risk/State:* `safety_bypasses: 201`, `state_mutation: 1430`, `fragile_debt: 9`, `duplicate_logic: 13`
* *Architecture:* `io: 6`, `api: 39`, `concurrency: 339`, `import: 7`
* *Defense:* `safety: 1112`, `doc: 1`, `test: 4`, `cleanup: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, util, react, react-dom, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-client.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.034 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.95 IQR)
- **Top Global Matches:** file_cluster_8: 14.034, file_cluster_4: 14.252, file_cluster_11: 14.325
- **Magnitude:** 13391.4 | **LOC:** 5452 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (66.2086%), Tech Debt (12.6341%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1524`, `structural_boundaries: 590`, `args: 228`, `func_start: 373`
* *Risk/State:* `safety_bypasses: 141`, `state_mutation: 1037`, `fragile_debt: 10`, `duplicate_logic: 2`
* *Architecture:* `io: 24`, `api: 16`, `concurrency: 233`, `import: 3`
* *Defense:* `safety: 806`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, util, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-client.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.034 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.95 IQR)
- **Top Global Matches:** file_cluster_8: 14.034, file_cluster_4: 14.252, file_cluster_11: 14.325
- **Magnitude:** 13391.4 | **LOC:** 5452 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (66.2086%), Tech Debt (12.6341%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1524`, `structural_boundaries: 590`, `args: 228`, `func_start: 373`
* *Risk/State:* `safety_bypasses: 141`, `state_mutation: 1037`, `fragile_debt: 10`, `duplicate_logic: 2`
* *Architecture:* `io: 24`, `api: 16`, `concurrency: 233`, `import: 3`
* *Defense:* `safety: 806`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, util, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-client.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.024 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.951 IQR)
- **Top Global Matches:** file_cluster_8: 14.024, file_cluster_4: 14.247, file_cluster_11: 14.316
- **Magnitude:** 13376.68 | **LOC:** 5450 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (65.6816%), Tech Debt (12.6353%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1523`, `structural_boundaries: 589`, `args: 228`, `func_start: 373`
* *Risk/State:* `safety_bypasses: 140`, `state_mutation: 1031`, `fragile_debt: 10`, `duplicate_logic: 2`
* *Architecture:* `io: 24`, `api: 16`, `concurrency: 228`, `import: 3`
* *Defense:* `safety: 804`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, util, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-turbopack/cjs/react-server-dom-turbopack-client.node.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.024 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.951 IQR)
- **Top Global Matches:** file_cluster_8: 14.024, file_cluster_4: 14.247, file_cluster_11: 14.316
- **Magnitude:** 13376.68 | **LOC:** 5450 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (65.6816%), Tech Debt (12.6353%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1523`, `structural_boundaries: 589`, `args: 228`, `func_start: 373`
* *Risk/State:* `safety_bypasses: 140`, `state_mutation: 1031`, `fragile_debt: 10`, `duplicate_logic: 2`
* *Architecture:* `io: 24`, `api: 16`, `concurrency: 228`, `import: 3`
* *Defense:* `safety: 804`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, util, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-client.browser.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.275 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.92 IQR)
- **Top Global Matches:** file_cluster_8: 14.275, file_cluster_4: 14.482, file_cluster_11: 14.571
- **Magnitude:** 13286.48 | **LOC:** 5306 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 88.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (67.2509%), Tech Debt (11.4478%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1498`, `structural_boundaries: 579`, `args: 217`, `func_start: 361`
* *Risk/State:* `safety_bypasses: 133`, `state_mutation: 1029`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `io: 22`, `api: 13`, `concurrency: 233`, `import: 2`
* *Defense:* `safety: 798`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-client.browser.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.275 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.92 IQR)
- **Top Global Matches:** file_cluster_8: 14.275, file_cluster_4: 14.482, file_cluster_11: 14.571
- **Magnitude:** 13286.48 | **LOC:** 5306 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 88.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (67.2509%), Tech Debt (11.4478%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1498`, `structural_boundaries: 579`, `args: 217`, `func_start: 361`
* *Risk/State:* `safety_bypasses: 133`, `state_mutation: 1029`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `io: 22`, `api: 13`, `concurrency: 233`, `import: 2`
* *Defense:* `safety: 798`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-client.browser.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.261 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.924 IQR)
- **Top Global Matches:** file_cluster_8: 14.261, file_cluster_4: 14.473, file_cluster_11: 14.559
- **Magnitude:** 13260.48 | **LOC:** 5290 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 88.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (66.6745%), Tech Debt (11.4609%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1497`, `structural_boundaries: 574`, `args: 215`, `func_start: 359`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 1016`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `io: 22`, `api: 13`, `concurrency: 228`, `import: 2`
* *Defense:* `safety: 795`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-turbopack/cjs/react-server-dom-turbopack-client.browser.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.261 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.924 IQR)
- **Top Global Matches:** file_cluster_8: 14.261, file_cluster_4: 14.473, file_cluster_11: 14.559
- **Magnitude:** 13260.48 | **LOC:** 5290 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 88.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (66.6745%), Tech Debt (11.4609%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullStringRow` (Impact: 565.8 | O(N^5) | DB: 8)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1497`, `structural_boundaries: 574`, `args: 215`, `func_start: 359`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 1016`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `io: 22`, `api: 13`, `concurrency: 228`, `import: 2`
* *Defense:* `safety: 795`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-client.edge.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.99 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.95 IQR)
- **Top Global Matches:** file_cluster_8: 13.99, file_cluster_4: 14.207, file_cluster_11: 14.292
- **Magnitude:** 13085.64 | **LOC:** 5292 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (66.5637%), Tech Debt (11.0323%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullBinaryRow` (Impact: 745.2 | O(N^5) | DB: 7)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1458`, `structural_boundaries: 578`, `args: 219`, `func_start: 355`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 1014`, `fragile_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `io: 23`, `api: 12`, `concurrency: 233`, `import: 2`
* *Defense:* `safety: 780`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-client.edge.development.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.99 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 2.95 IQR)
- **Top Global Matches:** file_cluster_8: 13.99, file_cluster_4: 14.207, file_cluster_11: 14.292
- **Magnitude:** 13085.64 | **LOC:** 5292 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (66.5637%), Tech Debt (11.0323%)
**Top Internal Functions/Classes:**
  * `flushComponentPerformance` (Impact: 2032.9 | O(2^N) | DB: 38)
  * `processReply` (Impact: 1136.1 | O(N^6) | DB: 48)
  * `addValueToProperties` (Impact: 1124.3 | O(2^N) | DB: 13)
  * `processFullBinaryRow` (Impact: 745.2 | O(N^5) | DB: 7)
  * `describeObjectForErrorMessage` (Impact: 473.0 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1458`, `structural_boundaries: 578`, `args: 219`, `func_start: 355`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 1014`, `fragile_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `io: 23`, `api: 12`, `concurrency: 233`, `import: 2`
* *Defense:* `safety: 780`, `doc: 1`, `test: 2`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `test/e2e/instrumentation-client-hook/app-with-src/src/instrumentation-client.ts` (TYPESCRIPT) | **Drift Ratio: 1.63x**
  * **Global Archetype:** `file_cluster_8` (Drift: 4.648 IQR)
  * **Local Reality:** `Cluster 2: Type Definitions & Bypasses` (Drift: 7.559 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `turbopack/crates/turbo-tasks-fs/src/globset.rs` (RUST) | Magnitude: 1142.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 383, branch: 117, state_mutation: 74, structural_boundaries: 70
- `turbopack/crates/turbo-tasks-env/src/dotenv.rs` (RUST) | Magnitude: 93.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 22, safety: 17, branch: 14
- `packages/next/src/server/create-deduped-by-callsite-server-error-logger.ts` (TYPESCRIPT) | Magnitude: 4.78 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, branch: 8, structural_boundaries: 7, args: 6
- `turbopack/crates/turbo-tasks-backend/tests/trait_ref_cell_mode.rs` (RUST) | Magnitude: 82.82 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 29, concurrency: 24, generics: 17
- `turbopack/crates/turbopack-cli/src/embed_js.rs` (RUST) | Magnitude: 20.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, safety: 6, branch: 4, concurrency: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `examples/with-electron/main/preload.js` (JAVASCRIPT) | Magnitude: 24.16 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, events: 4, structural_boundaries: 3, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/next/src/compiled/@babel/runtime/helpers/applyDecs2305.js` (JAVASCRIPT) | Magnitude: 552.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 126, branch: 87, state_mutation: 84, structural_boundaries: 40
- `turbopack/crates/turbopack-tests/tests/snapshot/debug-ids/browser/output/1do3_crates_turbopack-tests_tests_snapshot_debug-ids_browser_input_index_03ibyvs.js` (JAVASCRIPT) | Magnitude: 19.12 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 9, safety: 6, state_mutation: 6, safety_bypasses: 4
- `packages/next/src/server/route-modules/app-route/helpers/auto-implement-methods.ts` (TYPESCRIPT) | Magnitude: 6.07 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 12, state_mutation: 12, branch: 10
- `packages/next/src/compiled/mini-css-extract-plugin/cjs.js` (JAVASCRIPT) | Magnitude: 36.42 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, structural_boundaries: 12, branch: 6, safety: 5
- `packages/next/src/server/web/spec-extension/fetch-event.ts` (TYPESCRIPT) | Magnitude: 4.7 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 11, args: 9, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/next/src/compiled/@babel/runtime/helpers/esm/isNativeReflectConstruct.js` (JAVASCRIPT) | Magnitude: 14.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, branch: 3, args: 3
- `packages/next/src/compiled/@babel/runtime/helpers/isNativeReflectConstruct.js` (JAVASCRIPT) | Magnitude: 25.48 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: api: 8, indent_spaces: 6, branch: 4, structural_boundaries: 3
- `scripts/benchmark-boot-time.sh` (SHELL) | Magnitude: 14.98 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 87, io: 74, safety_bypasses: 53, structural_boundaries: 51
- `packages/next/src/shared/lib/is-plain-object.ts` (TYPESCRIPT) | Magnitude: 1.44 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, reflection_metaprogramming: 8, structural_boundaries: 7, branch: 3
- `packages/next/src/compiled/@babel/runtime/helpers/esm/extends.js` (JAVASCRIPT) | Magnitude: 28.0 | Delta: **0.218 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 7, structural_boundaries: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `turbopack/crates/turbo-tasks-backend/src/utils/dash_map_multi.rs` (RUST) | Magnitude: 279.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 159, structural_boundaries: 60, state_mutation: 36, generics: 28
- `packages/next/src/server/api-utils/index.ts` (TYPESCRIPT) | Magnitude: 8.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 51, api: 22, immutability_locks: 19
- `packages/next/src/server/app-render/dynamic-rendering.ts` (TYPESCRIPT) | Magnitude: 70.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 411, branch: 136, structural_boundaries: 97, args: 34
- `examples/with-http2/server.js` (JAVASCRIPT) | Magnitude: 51.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 10, indent_spaces: 9, io: 4, import: 4
- `packages/next/src/server/app-render/create-component-styles-and-scripts.tsx` (TYPESCRIPT) | Magnitude: 3.65 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 11, concurrency: 9, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `turbopack/crates/turbopack-tracing/tests/node-file-trace/integration/webpack-target-node/webpack-api-runtime.js` (JAVASCRIPT) | Magnitude: 149.34 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 147, indent_spaces: 110, structural_boundaries: 38, state_mutation: 35
- `turbopack/crates/turbopack-tests/tests/snapshot/basic/ecmascript_minify/output/0_9x_turbopack-tests_tests_snapshot_basic_ecmascript_minify_input_index_103o_dh.js` (JAVASCRIPT) | Magnitude: 12.52 | Delta: **0.233 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, debug_prints: 2, args: 1, api: 1
- `turbopack/crates/turbopack-tests/tests/snapshot/css/css-parse-error/output/1do3_crates_turbopack-tests_tests_snapshot_css_css-parse-error_input_index_1njzmrl.js` (JAVASCRIPT) | Magnitude: 13.52 | Delta: **0.277 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 3, globals: 2, branch: 1, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `turbopack/crates/turbopack-core/src/resolve/plugin.rs` (RUST) | Magnitude: 149.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 77, generics: 26, structural_boundaries: 23, safety: 18
- `turbopack/crates/turbopack-ecmascript/src/code_gen.rs` (RUST) | Magnitude: 206.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 223, structural_boundaries: 59, concurrency: 59, generics: 33
- `turbopack/crates/turbo-bincode/src/lib.rs` (RUST) | Magnitude: 1068.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 473, structural_boundaries: 194, generics: 138, state_mutation: 112
- `turbopack/crates/turbopack-ecmascript/src/tree_shake/util.rs` (RUST) | Magnitude: 473.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 360, structural_boundaries: 95, state_mutation: 74, args: 48
- `turbopack/crates/turbopack-ecmascript/src/lib.rs` (RUST) | Magnitude: 1434.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1397, structural_boundaries: 260, safety: 201, generics: 151

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `test/e2e/switchable-runtime/utils/runtime.js` (JAVASCRIPT) | Magnitude: 18.82 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, branch: 4, structural_boundaries: 3, state_mutation: 3
- `turbopack/crates/turbopack-tests/tests/snapshot/swc_transforms/preset_env/output/0rv8_turbopack-tests_tests_snapshot_swc_transforms_preset_env_input_index_04jskxh.js` (JAVASCRIPT) | Magnitude: 2471.66 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 897, state_mutation: 407, branch: 322, structural_boundaries: 213
- `turbopack/crates/turbopack-trace-server/src/reader/mod.rs` (RUST) | Magnitude: 662.78 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 308, structural_boundaries: 116, state_mutation: 103, branch: 68
- `packages/next-codemod/transforms/next-experimental-turbo-to-turbopack.ts` (TYPESCRIPT) | Magnitude: 26.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 192, branch: 53, structural_boundaries: 44, state_mutation: 33
- `turbopack/crates/turbopack-cli/js/src/entry/websocket.ts` (TYPESCRIPT) | Magnitude: 5.53 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 16, args: 15, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `evals/evals/agent-037-updatetag-cache/EVAL.ts` (TYPESCRIPT) | Magnitude: 17.25 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, branch: 33, state_mutation: 21, immutability_locks: 16
- `examples/cms-buttercms/components/blog/search-widget.js` (JAVASCRIPT) | Magnitude: 5.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, ui_framework: 4, structural_boundaries: 2, branch: 1
- `examples/with-mobx-state-tree/components/SampleComponent.tsx` (TYPESCRIPT) | Magnitude: 0.33 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, ui_framework: 8, args: 6
- `packages/next/src/lib/metadata/types/extra-types.ts` (TYPESCRIPT) | Magnitude: 3.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, branch: 53, structural_boundaries: 41, api: 20
- `crates/next-custom-transforms/tests/fixture/optimize_server_react/1/output.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 14, args: 10, closures: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `.github/actions/next-stats-action/src/aggregate-results.js` (JAVASCRIPT) | Magnitude: 104.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, immutability_locks: 22, branch: 18, state_mutation: 12
- `turbopack/crates/turbopack-tests/tests/execution/webpack/chunks/__skipped__/named-chunks/input/index.js` (JAVASCRIPT) | Magnitude: 142.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 159, func_start: 44, args: 40, concurrency: 40
- `packages/next/types/global.d.ts` (TYPESCRIPT) | Magnitude: 1.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 22, branch: 8, immutability_locks: 8
- `examples/cms-sitecore-xmcloud/src/lib/middleware/index.ts` (TYPESCRIPT) | Magnitude: 2.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, concurrency: 14, structural_boundaries: 11, args: 6
- `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-server.node.production.js` (JAVASCRIPT) | Magnitude: 7314.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3552, branch: 987, state_mutation: 857, safety: 654

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/next/src/server/node-environment-extensions/process-error-handlers.ts` (TYPESCRIPT) | Magnitude: 1.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 5, branch: 3, state_mutation: 3
- `evals/evals/agent-021-avoid-fetch-in-effect/app/UserProfile.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, planned_debt: 2, branch: 1
- `examples/with-temporal/temporal/src/activities.ts` (TYPESCRIPT) | Magnitude: 0.82 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, api: 3, io: 2
- `packages/next/src/server/ReactDOMServerPages.js` (JAVASCRIPT) | Magnitude: 16.08 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 3, branch: 1, structural_boundaries: 1, safety: 1
- `examples/next-forms/app/actions.ts` (TYPESCRIPT) | Magnitude: 1.76 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, planned_debt: 14, structural_boundaries: 12, safety: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `turbopack/crates/turbopack-static/src/lib.rs` (RUST) | Magnitude: 17.64 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 4, api: 4, encapsulation: 4
- `examples/with-sitemap/next.config.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, api: 1
- `turbopack/crates/turbopack-ecmascript-runtime/js/src/browser/runtime/base/dummy.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, state_mutation: 1
- `turbopack/crates/turbo-persistence/src/constants.rs` (RUST) | Magnitude: 29.28 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 21, api: 14, immutability_locks: 14, encapsulation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/with-webassembly/app/api/edge/route.ts` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, immutability_locks: 6, indent_spaces: 5, api: 2
- `packages/next/src/next-devtools/dev-overlay/components/version-staleness-info/version-staleness-info.tsx` (TYPESCRIPT) | Magnitude: 2.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 30, state_mutation: 22, ui_framework: 8
- `packages/next/src/shared/lib/errors/usage-error.ts` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, args: 2, func_start: 2
- `test/e2e/instrumentation-client-hook/app-with-src/src/app/page.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, branch: 1, args: 1
- `bench/app-router-server/app/rsc/page.js` (JAVASCRIPT) | Magnitude: 3.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, branch: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/next/src/server/node-environment.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 11, dead_code: 1, scientific: 1
- `turbopack/crates/turbopack-tests/tests/snapshot/source_maps/merged-unicode/output/1do3_crates_turbopack-tests_tests_snapshot_source_maps_merged-unicode_input_0b1pxfd._.js` (JAVASCRIPT) | Magnitude: 22.82 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, state_mutation: 6, args: 5, dead_code: 5
- `examples/with-electron-typescript/renderer/interfaces/index.ts` (TYPESCRIPT) | Magnitude: 0.45 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, safety: 5, args: 3
- `packages/next/src/shared/lib/normalized-asset-prefix.ts` (TYPESCRIPT) | Magnitude: 1.78 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 9, branch: 5, structural_boundaries: 4, api: 2
- `turbopack/crates/turbopack-tests/tests/snapshot/source_maps/merged-unicode/input/reflect-utils.js` (JAVASCRIPT) | Magnitude: 6.68 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, args: 2, func_start: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 66.6745% | Debt: 11.4609%
- `packages/next/src/compiled/react-server-dom-turbopack/cjs/react-server-dom-turbopack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 66.6745% | Debt: 11.4609%
- `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 67.2509% | Debt: 11.4478%
- `packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 67.2509% | Debt: 11.4478%
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-profiling.profiling.js` -> Churn: **67.76%** | Cog Load: 71.351% | Debt: 8.1722%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 24931.04
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 24825.54
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 24804.44
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-profiling.profiling.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 24728.44
- `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 24419.62

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/next/src/shared/lib/image-loader.ts` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 100.0%)
- `packages/next/src/server/base-server.ts` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.9911%)
- `packages/next/src/client/components/app-router-instance.ts` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 95.7353%)
- `packages/next/src/server/route-modules/route-module.ts` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 94.4921%)
- `packages/next/src/server/after/after-context.ts` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `turbopack/crates/turbo-tasks-fs/src/embed/fs.rs` -> **Severity: 997.3** (Blast Radius: 9.973 * Doc Risk: 100.0%)
- `packages/next/src/shared/lib/image-external.tsx` -> **Severity: 407.382** (Blast Radius: 4.164 * Doc Risk: 97.8343%)
- `packages/next/src/shared/lib/invariant-error.ts` -> **Severity: 238.137** (Blast Radius: 3.973 * Doc Risk: 59.9389%)
- `packages/next/src/shared/lib/segment.ts` -> **Severity: 160.999** (Blast Radius: 1.613 * Doc Risk: 99.8131%)
- `packages/next/src/lib/picocolors.ts` -> **Severity: 151.2** (Blast Radius: 1.512 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
