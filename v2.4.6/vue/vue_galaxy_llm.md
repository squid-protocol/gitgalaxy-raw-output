# ARCHITECTURAL_BRIEF: vue
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/vue` |
| **Timestamp** | `2026-08-03T21:40:15.240933+00:00` |
| **Scan Duration** | `0.91s` |
| **Git Branch** | `main` |
| **Git Commit** | `9e88707940088cb1f4cd7dd210c9168a50dc347c` |
| **Git Remote** | `https://github.com/vuejs/vue` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 248 malicious artifacts.

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
| Total Artifacts | 508 |
| Analyzed Artifacts (Scanned) | 298 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 210 |
| Total LOC | 21971 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 58.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5295 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2374 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1486 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 223 | 18290 | 74.8% |
| JAVASCRIPT | 23 | 1254 | 7.7% |
| HTML | 22 | 1974 | 7.4% |
| JSON | 9 | 201 | 3.0% |
| CSS | 7 | 234 | 2.3% |
| PLAINTEXT | 6 | 0 | 2.0% |
| MARKDOWN | 5 | 0 | 1.7% |
| SHELL | 2 | 16 | 0.7% |
| YAML | 1 | 2 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.141`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 156 | 52.3% |
| file_cluster_13 | 98 | 32.9% |
| file_cluster_16 | 18 | 6.0% |
| file_cluster_4 | 7 | 2.3% |
| file_cluster_17 | 4 | 1.3% |
| file_cluster_0 | 3 | 1.0% |
| file_cluster_11 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 210*

**Composition by Extension & Reason:**
- `.ts`: 165x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 9 LOC), 1x Excluded (Machine-Generated Source Code Signature: 163 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 7018 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 25.9 | 15.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 44.5 | 57.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.7 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.2 | 5.9 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 62.1 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 47.7 | 46.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.9 | 0.3 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/release.js` (Hits: 13)
- `scripts/git-hooks/commit-msg` (Hits: 13)
- `examples/classic/todomvc/index.html` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.ts** (`src/shared/util.ts`) — 59 inbound connections
2. **component.ts** (`src/types/component.ts`) — 42 inbound connections
3. **compiler.ts** (`src/types/compiler.ts`) — 30 inbound connections
4. **vnode.ts** (`src/types/vnode.ts`) — 30 inbound connections
5. **vnode.ts** (`src/core/vdom/vnode.ts`) — 23 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compileScript.ts** (`packages/compiler-sfc/src/compileScript.ts`) — 22 outbound dependencies
2. **index.ts** (`src/v3/index.ts`) — 18 outbound dependencies
3. **index.d.ts** (`types/index.d.ts`) — 17 outbound dependencies
4. **lifecycle.ts** (`src/core/instance/lifecycle.ts`) — 14 outbound dependencies
5. **config.js** (`scripts/config.js`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createPatchFunction` (@ `src/core/vdom/patch.ts`) -> Impact: **1071.9** | LOC: 826
- `onIdentifier` (@ `packages/compiler-sfc/src/babelUtils.ts`) -> Impact: **936.5** | LOC: 358
- `walkDeclaration` (@ `packages/compiler-sfc/src/compileScript.ts`) -> Impact: **800.5** | LOC: 431
  * *Intent:* // if withDefaults() is used, we need to remove the optional flags // on props that have default values
- `createRenderer` (@ `packages/server-renderer/src/bundle-renderer/create-bundle-renderer.ts`) -> Impact: **306.4** | LOC: 127
- `defineReactive` (@ `src/core/observer/index.ts`) -> Impact: **225.0** | LOC: 87
- `source` (@ `src/v3/apiAsyncComponent.ts`) -> Impact: **194.8** | LOC: 86
  * *Intent:* /** * v3-compatible async component API.
- `mount` (@ `src/platforms/web/runtime-with-compiler.ts`) -> Impact: **183.7** | LOC: 72
- `updateDOMProps` (@ `src/platforms/web/runtime/modules/dom-props.ts`) -> Impact: **170.5** | LOC: 84
- `_createElement` (@ `src/core/vdom/create-element.ts`) -> Impact: **162.7** | LOC: 95
- `looseEqual` (@ `src/shared/util.ts`) -> Impact: **147.5** | LOC: 40

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `createRenderer` (@ `packages/server-renderer/src/bundle-renderer/create-bundle-renderer.ts`) -> **O(2^N) [Recursive]**
- `source` (@ `src/v3/apiAsyncComponent.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * v3-compatible async component API.
- `unmount` (@ `benchmarks/big-table/index.html`) -> **O(2^N) [Recursive]**
- `rerender` (@ `benchmarks/big-table/index.html`) -> **O(2^N) [Recursive]**
- `upDays` (@ `benchmarks/uptime/index.html`) -> **O(2^N) [Recursive]**
- `shuffle` (@ `examples/classic/move-animations/index.html`) -> **O(2^N) [Recursive]**
- `capitalize` (@ `examples/composition/grid.html`) -> **O(2^N) [Recursive]**
- `start` (@ `packages/compiler-sfc/src/parseComponent.ts`) -> **O(2^N) [Recursive]**
- `next` (@ `packages/server-renderer/src/render-context.ts`) -> **O(2^N) [Recursive]**
- `apply` (@ `packages/server-renderer/src/webpack-plugin/client.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `createPatchFunction` (@ `src/core/vdom/patch.ts`) -> DB Complexity: **38**
- `constructor` (@ `src/core/observer/watcher.ts`) -> DB Complexity: **33**
- `start` (@ `packages/server-renderer/src/template-renderer/template-stream.ts`) -> DB Complexity: **22**
- `write` (@ `scripts/build.js`) -> DB Complexity: **18**
- `stop` (@ `src/v3/reactivity/effectScope.ts`) -> DB Complexity: **18**
- `createRenderer` (@ `packages/server-renderer/src/bundle-renderer/create-bundle-renderer.ts`) -> DB Complexity: **17**
- `next` (@ `packages/server-renderer/src/render-context.ts`) -> DB Complexity: **17**
- `constructor` (@ `packages/server-renderer/src/render-stream.ts`) -> DB Complexity: **16**
- `cleanupDeps` (@ `src/core/observer/watcher.ts`) -> DB Complexity: **15**
- `constructor` (@ `packages/server-renderer/src/render-context.ts`) -> DB Complexity: **14**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/compiler/parser` | 5 | 3381.79 | 48.53% | 23.09% |
| `src/compiler` | 7 | 377.74 | 35.55% | 3.93% |
| `scripts` | 7 | 356.08 | 27.69% | 21.42% |
| `packages/compiler-sfc/src` | 13 | 303.38 | 23.99% | 9.78% |
| `benchmarks/dbmon` | 3 | 264.82 | 29.28% | 0.0% |
| `examples/composition` | 6 | 184.82 | 8.98% | 0.0% |
| `packages/server-renderer/src/optimizing-compiler` | 5 | 178.23 | 39.3% | 0.0% |
| `src/core/vdom` | 5 | 177.87 | 27.9% | 1.82% |
| `benchmarks/uptime` | 1 | 175.78 | 69.89% | 0.0% |
| `packages/server-renderer/src` | 10 | 158.4 | 31.16% | 21.26% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/core/instance/render-helpers/resolve-scoped-slots.ts` -> **100.0%** Exposure
- `scripts/git-hooks/commit-msg` -> **100.0%** Exposure
- `scripts/git-hooks/pre-commit` -> **100.0%** Exposure
- `src/core/util/env.ts` -> **99.9995%** Exposure
- `types/v3-manual-apis.d.ts` -> **99.9992%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benchmarks/big-table/index.html` -> **100.0%** Exposure
- `benchmarks/dbmon/ENV.js` -> **100.0%** Exposure
- `packages/template-compiler/index.js` -> **100.0%** Exposure
- `packages/server-renderer/src/render-context.ts` -> **100.0%** Exposure
- `packages/server-renderer/src/render-stream.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `types/vue.d.ts` -> **3** Orphaned Functions | **9** Duplicates
- `types/v3-define-component.d.ts` -> **0** Orphaned Functions | **5** Duplicates
- `src/core/util/env.ts` -> **0** Orphaned Functions | **4** Duplicates
- `src/core/util/next-tick.ts` -> **0** Orphaned Functions | **4** Duplicates
- `examples/composition/svg.html` -> **0** Orphaned Functions | **3** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/compiler/parser/index.ts`** -> AI Confidence: **99.48%**
2. **`src/core/vdom/patch.ts`** -> AI Confidence: **99.48%**
3. **`packages/compiler-sfc/src/compileScript.ts`** -> AI Confidence: **99.39%**
4. **`packages/server-renderer/src/render.ts`** -> AI Confidence: **99.39%**
5. **`src/core/observer/watcher.ts`** -> AI Confidence: **99.39%**
6. **`src/core/vdom/create-element.ts`** -> AI Confidence: **99.39%**
7. **`scripts/config.js`** -> AI Confidence: **99.31%**
8. **`scripts/release.js`** -> AI Confidence: **99.31%**
9. **`packages/compiler-sfc/src/compileTemplate.ts`** -> AI Confidence: **99.31%**
10. **`packages/compiler-sfc/src/parse.ts`** -> AI Confidence: **99.31%**
11. **`packages/compiler-sfc/src/parseComponent.ts`** -> AI Confidence: **99.31%**
12. **`packages/server-renderer/src/bundle-renderer/create-bundle-renderer.ts`** -> AI Confidence: **99.31%**
13. **`packages/server-renderer/src/create-renderer.ts`** -> AI Confidence: **99.31%**
14. **`packages/server-renderer/src/optimizing-compiler/runtime-helpers.ts`** -> AI Confidence: **99.31%**
15. **`src/compiler/codegen/index.ts`** -> AI Confidence: **99.31%**
16. **`src/core/instance/init.ts`** -> AI Confidence: **99.31%**
17. **`src/core/instance/lifecycle.ts`** -> AI Confidence: **99.31%**
18. **`src/core/instance/render.ts`** -> AI Confidence: **99.31%**
19. **`src/core/instance/state.ts`** -> AI Confidence: **99.31%**
20. **`src/core/util/options.ts`** -> AI Confidence: **99.31%**
21. **`src/core/vdom/create-component.ts`** -> AI Confidence: **99.31%**
22. **`src/core/vdom/create-functional-component.ts`** -> AI Confidence: **99.31%**
23. **`src/core/vdom/helpers/normalize-scoped-slots.ts`** -> AI Confidence: **99.31%**
24. **`src/platforms/web/runtime-with-compiler.ts`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `benchmarks/big-table/index.html` -> **100.0%** Exposure
- `benchmarks/uptime/index.html` -> **100.0%** Exposure
- `examples/classic/elastic-header/index.html` -> **100.0%** Exposure
- `examples/classic/move-animations/index.html` -> **100.0%** Exposure
- `examples/composition/svg.html` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/config.js` -> **100.0%** Exposure
- `src/platforms/web/util/index.ts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `examples/classic/firebase/app.js` -> **99.9399%** Exposure
### Algorithmic DoS Exposure
- `benchmarks/big-table/index.html` -> **100.0%** Exposure
- `benchmarks/uptime/index.html` -> **100.0%** Exposure
- `examples/classic/elastic-header/index.html` -> **100.0%** Exposure
- `examples/classic/move-animations/index.html` -> **100.0%** Exposure
- `examples/classic/select2/index.html` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `489` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/server-renderer/src/template-renderer/index.ts` (TYPESCRIPT) -> Cumulative Risk: **857.06**
- **Archetype:** `file_cluster_4` (Distance: 12.381 IQR)
- **Magnitude:** 39.49 | **LOC:** 307 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `render` (Impact: 43.8), `renderPreloadLinks` (Impact: 36.0), `renderPrefetchLinks` (Impact: 25.3)

### 2. `src/core/observer/dep.ts` (TYPESCRIPT) -> Cumulative Risk: **844.56**
- **Archetype:** `file_cluster_4` (Distance: 12.795 IQR)
- **Magnitude:** 16.62 | **LOC:** 109 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `update` (Impact: 93.8), `pushTarget` (Impact: 5.1), `cleanupDeps` (Impact: 3.9)

### 3. `src/compiler/codeframe.ts` (TYPESCRIPT) -> Cumulative Risk: **754.32**
- **Archetype:** `file_cluster_8` (Distance: 10.94 IQR)
- **Magnitude:** 9.68 | **LOC:** 53 | **CtrlFlow:** 86.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `generateCodeFrame` (Impact: 61.8), `repeat` (Impact: 11.1)

### 4. `src/core/util/next-tick.ts` (TYPESCRIPT) -> Cumulative Risk: **752.05**
- **Archetype:** `file_cluster_4` (Distance: 12.099 IQR)
- **Magnitude:** 13.99 | **LOC:** 118 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9984%)
- **Heaviest Functions:** `nextTick` (Impact: 75.0), `flushCallbacks` (Impact: 3.9), `timerFunc` (Impact: 3.8)

### 5. `src/core/util/debug.ts` (TYPESCRIPT) -> Cumulative Risk: **741.71**
- **Archetype:** `file_cluster_13` (Distance: 10.824 IQR)
- **Magnitude:** 19.3 | **LOC:** 106 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9999%)
- **Heaviest Functions:** `generateComponentTrace` (Impact: 90.1), `formatComponentName` (Impact: 32.3), `warn` (Impact: 21.2)

### 6. `src/platforms/web/runtime/components/transition-group.ts` (TYPESCRIPT) -> Cumulative Risk: **741.69**
- **Archetype:** `file_cluster_13` (Distance: 11.682 IQR)
- **Magnitude:** 19.5 | **LOC:** 205 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `render` (Impact: 68.1), `updated` (Impact: 30.3), `hasMove` (Impact: 11.7)

### 7. `packages/server-renderer/src/render-context.ts` (TYPESCRIPT) -> Cumulative Risk: **736.71**
- **Archetype:** `file_cluster_13` (Distance: 12.796 IQR)
- **Magnitude:** 19.91 | **LOC:** 135 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `next` (Impact: 93.1), `constructor` (Impact: 11.5), `normalizeAsync` (Impact: 9.2)

### 8. `src/core/components/keep-alive.ts` (TYPESCRIPT) -> Cumulative Risk: **706.81**
- **Archetype:** `file_cluster_8` (Distance: 10.9 IQR)
- **Magnitude:** 14.33 | **LOC:** 172 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9998%)
- **Heaviest Functions:** `render` (Impact: 47.3), `pruneCacheEntry` (Impact: 11.9), `matches` (Impact: 11.1)

### 9. `src/core/vdom/helpers/resolve-async-component.ts` (TYPESCRIPT) -> Cumulative Risk: **697.45**
- **Archetype:** `file_cluster_13` (Distance: 10.538 IQR)
- **Magnitude:** 9.6 | **LOC:** 158 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.5132%), Tech Debt (96.3358%), State Flux (87.1007%)
- **Heaviest Functions:** `warn` (Impact: 17.4), `forceRender` (Impact: 15.8), `forceRender` (Impact: 14.9)

### 10. `src/core/observer/watcher.ts` (TYPESCRIPT) -> Cumulative Risk: **692.38**
- **Archetype:** `file_cluster_13` (Distance: 14.226 IQR)
- **Magnitude:** 41.57 | **LOC:** 279 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 62.0), `run` (Impact: 24.1), `get` (Impact: 18.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/compiler/parser/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.742 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.896 IQR)
- **Top Global Matches:** file_cluster_8: 10.742, file_cluster_13: 11.27, file_cluster_7: 11.392
- **Magnitude:** 3353.36 | **LOC:** 1000 | **CtrlFlow:** 83.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (33.5071%), Tech Debt (15.4521%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 63`, `args: 101`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 108`, `dead_code: 1`, `fragile_debt: 5`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.946
  * `Choke Point (Betweenness):` 0.000154 | `Ripple Effect (Closeness):` 0.006734
  * `Imports (Out-Degree: 7):` html-parser, env, text-parser, compiler, he, model, filter-parser, util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/compiler/error-detector.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.573 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.744 IQR)
- **Top Global Matches:** file_cluster_8: 10.573, file_cluster_4: 10.999, file_cluster_13: 11.005
- **Magnitude:** 309.44 | **LOC:** 159 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.6405%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 19`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 12`
* *Architecture:* `api: 2`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 10`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.754
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006061
  * `Imports (Out-Degree: 1):` compiler, index
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `benchmarks/dbmon/ENV.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.773 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.448 IQR)
- **Top Global Matches:** file_cluster_8: 11.773, file_cluster_17: 12.134, file_cluster_11: 12.205
- **Magnitude:** 241.14 | **LOC:** 212 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (77.5317%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generateRow` (Impact: 47.4 | O(N^2) | DB: 10)
  * `getData` (Impact: 35.7 | O(N^2) | DB: 9)
  * `countClassName` (Impact: 18.0 | O(2^N) | DB: 1)
  * `getElapsedClassName` (Impact: 9.3 | O(N^1) | DB: 1)
  * `cleanQuery` (Impact: 8.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 40`, `args: 12`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 99`, `dead_code: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.252 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.174 IQR)
- **Top Global Matches:** file_cluster_4: 10.252, file_cluster_8: 10.41, file_cluster_13: 10.562
- **Magnitude:** 179.36 | **LOC:** 203 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (83.7923%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 58.9 | O(N^2) | DB: 3)
  * `publishPackage` (Impact: 56.8 | O(N^2) | DB: 9)
  * `updatePackage` (Impact: 2.0 | O(N^1) | DB: 13)
  * `run` (Impact: 1.1 | O(N^1))
  * `execa` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 28`, `args: 11`, `func_start: 19`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 13`, `concurrency: 43`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` minimist, enquirer, execa, fs, package.json, semver, chalk, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benchmarks/uptime/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.156 IQR)
- **Top Global Matches:** file_cluster_8: 11.156, file_cluster_17: 11.4, file_cluster_4: 11.508
- **Magnitude:** 175.78 | **LOC:** 201 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (69.8868%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `maxStreak` (Impact: 26.6 | O(N^4) | DB: 2)
  * `upDays` (Impact: 14.1 | O(2^N) | DB: 1)
  * `update` (Impact: 12.4 | O(2^N) | DB: 2)
  * `toggle` (Impact: 10.8 | O(N^3) | DB: 3)
  * `render` (Impact: 10.7 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 31`, `args: 13`, `func_start: 15`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 69`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 6`
* *Defense:* `doc: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benchmarks/big-table/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.906 IQR)
- **Top Global Matches:** file_cluster_4: 11.906, file_cluster_0: 11.96, file_cluster_8: 12.095
- **Magnitude:** 155.78 | **LOC:** 164 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (92.2562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visibleCount` (Impact: 22.4 | O(N^4) | DB: 10)
  * `generateGrid` (Impact: 18.8 | O(N^3) | DB: 8)
  * `unmount` (Impact: 7.4 | O(2^N) | DB: 2)
  * `rerender` (Impact: 7.4 | O(2^N) | DB: 3)
  * `matches` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 35`, `args: 16`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 70`
* *Architecture:* `io: 5`, `api: 2`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` demo.css, vue.min.js, style.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/vdom/patch.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.403 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.656 IQR)
- **Top Global Matches:** file_cluster_8: 11.403, file_cluster_13: 11.744, file_cluster_7: 11.889
- **Magnitude:** 123.1 | **LOC:** 908 | **CtrlFlow:** 85.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (40.6315%), Tech Debt (9.1145%)
**Top Internal Functions/Classes:**
  * `createPatchFunction` (Impact: 1071.9 | O(N^4) | DB: 38)
  * `sameVnode` (Impact: 14.4 | O(N^1))
  * `sameInputType` (Impact: 14.2 | O(N^1) | DB: 1)
  * `createKeyToOldIdx` (Impact: 6.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 43`, `args: 102`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 5`, `state_mutation: 106`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 34`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.07
  * `Choke Point (Betweenness):` 0.000503 | `Ripple Effect (Closeness):` 0.010774
  * `Imports (Out-Degree: 5):` index, element, vnode, lifecycle, constants, template-ref, config, traverse
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/server-renderer/src/optimizing-compiler/modules.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.646 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.34 IQR)
- **Top Global Matches:** file_cluster_13: 9.646, file_cluster_8: 9.717, file_cluster_17: 9.813
- **Magnitude:** 116.41 | **LOC:** 119 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (24.4006%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 32`, `args: 10`, `func_start: 7`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.86
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.004489
  * `Imports (Out-Degree: 4):` index, compiler, attrs, codegen, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/compiler-sfc/src/babelUtils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.924 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.624 IQR)
- **Top Global Matches:** file_cluster_8: 9.924, file_cluster_13: 10.437, file_cluster_7: 10.533
- **Magnitude:** 97.08 | **LOC:** 424 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (36.8789%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onIdentifier` (Impact: 936.5 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 90`, `args: 22`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.309
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.032279
  * `Imports (Out-Degree: 1):` estree-walker, foo, types, bar
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/classic/elastic-header/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.377 IQR)
- **Top Global Matches:** file_cluster_0: 11.377, file_cluster_8: 11.425, file_cluster_13: 11.728
- **Magnitude:** 96.5 | **LOC:** 106 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (57.1763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDrag` (Impact: 14.4 | O(N^3) | DB: 7)
  * `stopDrag` (Impact: 7.6 | O(N^3) | DB: 3)
  * `contentPosition` (Impact: 7.3 | O(N^3) | DB: 3)
  * `startDrag` (Impact: 5.5 | O(N^2) | DB: 3)
  * `headerPath` (Impact: 3.7 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 18`, `args: 9`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 50`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 3`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` style.css, vue.min.js, dynamics.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-sfc/src/compileScript.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.675 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.114 IQR)
- **Top Global Matches:** file_cluster_17: 13.675, file_cluster_13: 13.701, file_cluster_0: 13.78
- **Magnitude:** 95.01 | **LOC:** 1917 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (40.28%), Tech Debt (18.8171%)
**Top Internal Functions/Classes:**
  * `walkDeclaration` (Impact: 800.5 | O(N^3) | DB: 7)
    * *Intent:* // if withDefaults() is used, we need to remove the optional flags // on props that have default val...
  * `registerUserImport` (Impact: 42.2 | O(N^4) | DB: 1)
  * `walkDeclaration` (Impact: 21.6 | O(2^N))
  * `checkInvalidScopeReference` (Impact: 4.8 | O(N^1))
  * `registerBinding` (Impact: 2.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 108`, `args: 34`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 52`, `dead_code: 21`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 22`
* *Defense:* `safety: 79`, `doc: 7`, `test: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.621
  * `Choke Point (Betweenness):` 0.003849 | `Ripple Effect (Closeness):` 0.039075
  * `Imports (Out-Degree: 11):` $node.source.value, lru-cache, codeframe, warn, types, x, text-parser, html-parser...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scripts/build.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.02 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.172 IQR)
- **Top Global Matches:** file_cluster_8: 10.02, file_cluster_4: 10.04, file_cluster_13: 10.108
- **Magnitude:** 74.98 | **LOC:** 98 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (51.1903%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 22.1 | O(N^2) | DB: 18)
  * `buildEntry` (Impact: 17.2 | O(N^3))
  * `build` (Impact: 9.7 | O(N^2) | DB: 1)
  * `getSize` (Impact: 2.1 | O(N^1))
  * `logError` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 21`, `args: 16`, `func_start: 15`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 12`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003367
  * `Imports (Out-Degree: 0):` zlib, fs, config, terser, rollup, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/compiler/codegen/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.817 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.805 IQR)
- **Top Global Matches:** file_cluster_8: 10.817, file_cluster_13: 11.055, file_cluster_17: 11.221
- **Magnitude:** 74.98 | **LOC:** 669 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (52.1415%), Tech Debt (8.4637%)
**Top Internal Functions/Classes:**
  * `genScopedSlot` (Impact: 105.1 | O(2^N))
  * `genElement` (Impact: 98.7 | O(N^2) | DB: 4)
  * `maybeComponent` (Impact: 67.2 | O(2^N) | DB: 2)
  * `genChildren` (Impact: 60.4 | O(N^2))
  * `genFor` (Impact: 58.8 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 90`, `args: 38`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 75`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `import: 7`
* *Defense:* `safety: 4`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.255
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.007576
  * `Imports (Out-Degree: 4):` events, index, compiler, index, types, util, helpers
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/classic/grid/grid.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.631 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.043 IQR)
- **Top Global Matches:** file_cluster_8: 11.631, file_cluster_17: 11.815, file_cluster_15: 12.091
- **Magnitude:** 71.62 | **LOC:** 70 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (85.7131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `filteredData` (Impact: 25.3 | O(N^3) | DB: 10)
  * `data` (Impact: 2.2 | O(N^1) | DB: 2)
  * `capitalize` (Impact: 1.9 | O(N^1))
  * `sortBy` (Impact: 1.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 8`, `func_start: 4`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003367
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `benchmarks/svg/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.594 IQR)
- **Top Global Matches:** file_cluster_8: 10.594, file_cluster_4: 10.628, file_cluster_0: 11.039
- **Magnitude:** 65.62 | **LOC:** 103 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (70.0429%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createModel` (Impact: 13.3 | O(N^1) | DB: 3)
  * `created` (Impact: 5.9 | O(N^2) | DB: 1)
  * `toggleOptimization` (Impact: 5.5 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 13`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 12`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js, stats.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.037 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.756 IQR)
- **Top Global Matches:** file_cluster_8: 9.037, file_cluster_13: 9.169, file_cluster_0: 9.416
- **Magnitude:** 65.5 | **LOC:** 306 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (5.6121%), Tech Debt (61.3717%)
**Top Internal Functions/Classes:**
  * `genConfig` (Impact: 34.7 | O(N^3) | DB: 9)
  * `resolve` (Impact: 10.8 | O(2^N) | DB: 6)
  * `require` (Impact: 3.5 | O(2^N))
  * `require` (Impact: 2.5 | O(2^N))
  * `cjs` (Impact: 2.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 7`, `args: 5`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 7`, `api: 3`, `import: 16`
* *Defense:* `safety: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` feature-flags, plugin-node-resolve, plugin-replace, plugin-commonjs, package.json, package.json, alias, rollup-plugin-typescript2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/classic/tree/tree.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.945 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.129 IQR)
- **Top Global Matches:** file_cluster_8: 10.945, file_cluster_7: 11.559, file_cluster_15: 11.669
- **Magnitude:** 58.5 | **LOC:** 76 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (57.0947%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changeType` (Impact: 5.5 | O(N^2) | DB: 5)
  * `isFolder` (Impact: 5.4 | O(N^2) | DB: 2)
  * `toggle` (Impact: 5.4 | O(N^2) | DB: 3)
  * `addChild` (Impact: 2.8 | O(N^2) | DB: 2)
  * `data` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003367
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/composition/todomvc.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 8.683 IQR)
- **Top Global Matches:** file_cluster_0: 8.683, file_cluster_8: 8.771, file_cluster_11: 8.946
- **Magnitude:** 56.54 | **LOC:** 242 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (8.1084%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 27.8 | O(N^3) | DB: 5)
  * `fetch` (Impact: 4.6 | O(N^2) | DB: 8)
  * `completed` (Impact: 4.5 | O(2^N))
  * `pluralize` (Impact: 3.6 | O(N^1))
  * `active` (Impact: 2.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 39`, `args: 30`, `func_start: 21`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 39`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js, index.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server-renderer/src/util.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.164 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.175 IQR)
- **Top Global Matches:** file_cluster_8: 8.164, file_cluster_4: 8.681, file_cluster_7: 9.011
- **Magnitude:** 56.25 | **LOC:** 115 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.135%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 24`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 13`, `import: 1`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/composition/grid.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.858 IQR)
- **Top Global Matches:** file_cluster_8: 7.858, file_cluster_7: 8.756, file_cluster_17: 8.85
- **Magnitude:** 51.34 | **LOC:** 174 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (9.1999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `capitalize` (Impact: 37.1 | O(2^N) | DB: 2)
  * `data` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 17`, `args: 13`, `func_start: 4`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/classic/todomvc/app.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.73%)
- **Global Archetype:** `file_cluster_11` (Drift: 11.277 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.33 IQR)
- **Top Global Matches:** file_cluster_11: 11.277, file_cluster_6: 11.413, file_cluster_17: 11.418
- **Magnitude:** 49.34 | **LOC:** 158 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (50.7123%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetch` (Impact: 3.9 | O(N^1) | DB: 9)
  * `completed` (Impact: 3.7 | O(2^N))
  * `pluralize` (Impact: 3.6 | O(N^1))
  * `set` (Impact: 2.8 | O(N^2) | DB: 1)
  * `handler` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 15`, `args: 15`, `func_start: 11`
* *Risk/State:* `state_mutation: 16`, `planned_debt: 9`
* *Architecture:* `io: 4`, `api: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/classic/move-animations/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.102 IQR)
- **Top Global Matches:** file_cluster_8: 10.102, file_cluster_2: 10.41, file_cluster_0: 10.462
- **Magnitude:** 43.6 | **LOC:** 94 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (47.9626%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 6.0 | O(N^3) | DB: 4)
  * `shuffle` (Impact: 5.8 | O(2^N) | DB: 2)
  * `insert` (Impact: 3.0 | O(N^3) | DB: 4)
  * `reset` (Impact: 3.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `args: 6`, `func_start: 4`, `class_start: 9`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 2`
* *Defense:* `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lodash.min.js, vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/observer/watcher.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.226 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.558 IQR)
- **Top Global Matches:** file_cluster_13: 14.226, file_cluster_11: 14.401, file_cluster_17: 14.576
- **Magnitude:** 41.57 | **LOC:** 279 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (41.3707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 62.0 | O(N^3) | DB: 33)
  * `run` (Impact: 24.1 | O(N^3) | DB: 13)
  * `get` (Impact: 18.1 | O(N^2) | DB: 7)
  * `teardown` (Impact: 13.5 | O(N^2) | DB: 10)
  * `addDep` (Impact: 8.3 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 20`, `args: 21`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 256`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 7`, `import: 8`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.922
  * `Choke Point (Betweenness):` 0.007034 | `Ripple Effect (Closeness):` 0.144416
  * `Imports (Out-Degree: 6):` debug, index, effectScope, scheduler, component, dep, traverse
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `packages/server-renderer/src/render.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.054 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.003 IQR)
- **Top Global Matches:** file_cluster_8: 11.054, file_cluster_13: 11.18, file_cluster_4: 11.506
- **Magnitude:** 39.78 | **LOC:** 460 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (38.0458%), Tech Debt (8.6096%)
**Top Internal Functions/Classes:**
  * `renderComponent` (Impact: 87.2 | O(N^3))
  * `renderAsyncComponent` (Impact: 66.2 | O(N^2) | DB: 2)
  * `waitForServerPrefetch` (Impact: 28.0 | O(N^2) | DB: 3)
  * `renderNode` (Impact: 25.1 | O(N^1))
  * `renderStartingTag` (Impact: 23.5 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 41`, `args: 61`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 45`, `planned_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 8`, `immutability_locks: 47`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` debug, util, vnode, compiler, runtime-helpers, constants, render-context, vnode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server-renderer/src/template-renderer/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.381 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.535 IQR)
- **Top Global Matches:** file_cluster_4: 12.381, file_cluster_17: 12.46, file_cluster_13: 12.667
- **Magnitude:** 39.49 | **LOC:** 307 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (95.5931%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 43.8 | O(2^N) | DB: 6)
    * *Intent:* // render synchronously given rendered app content and render context
  * `renderPreloadLinks` (Impact: 36.0 | O(N^3) | DB: 4)
  * `renderPrefetchLinks` (Impact: 25.3 | O(N^3) | DB: 5)
  * `getPreloadType` (Impact: 22.7 | O(N^1))
  * `renderStyles` (Impact: 22.6 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 66`, `args: 32`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 118`, `dead_code: 2`
* *Architecture:* `io: 3`, `api: 4`, `concurrency: 40`, `import: 8`
* *Defense:* `safety: 1`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` parse-template, template-stream, serialize-javascript, util, create-async-file-mapper, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/classic/elastic-header/index.html` (HTML) | Magnitude: 96.5 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 50, structural_boundaries: 18, args: 9
- `examples/composition/todomvc.html` (HTML) | Magnitude: 56.54 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 39, planned_debt: 39, args: 30
- `examples/classic/todomvc/index.html` (HTML) | Magnitude: 17.34 | Delta: **0.4 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 60, decorators: 29, structural_boundaries: 20, planned_debt: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/classic/todomvc/app.js` (JAVASCRIPT) | Magnitude: 49.34 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 16, structural_boundaries: 15, args: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/server-renderer/src/bundle-renderer/create-bundle-renderer.ts` (TYPESCRIPT) | Magnitude: 31.91 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 118, branch: 31, structural_boundaries: 24, args: 19
- `src/platforms/web/util/style.ts` (TYPESCRIPT) | Magnitude: 7.38 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, branch: 12, state_mutation: 9, structural_boundaries: 8
- `types/index.d.ts` (TYPESCRIPT) | Magnitude: 3.08 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, api: 14, import: 13
- `src/platforms/web/runtime/modules/class.ts` (TYPESCRIPT) | Magnitude: 1.98 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 9, branch: 8, immutability_locks: 4
- `packages/server-renderer/src/modules/attrs.ts` (TYPESCRIPT) | Magnitude: 7.57 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, branch: 22, structural_boundaries: 14, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `types/v3-setup-context.d.ts` (TYPESCRIPT) | Magnitude: 17.26 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 20, generics: 16, args: 8
- `types/jsx.d.ts` (TYPESCRIPT) | Magnitude: 2.08 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, branch: 17, doc: 17, structural_boundaries: 15
- `src/v3/reactivity/computed.ts` (TYPESCRIPT) | Magnitude: 8.5 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 30, generics: 22, branch: 11
- `types/vue.d.ts` (TYPESCRIPT) | Magnitude: 6.8 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 365, generics: 78, structural_boundaries: 60, safety_bypasses: 43
- `src/types/global-api.ts` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 15, args: 11, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/core/util/props.ts` (TYPESCRIPT) | Magnitude: 24.29 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 176, branch: 73, structural_boundaries: 58, args: 26
- `packages/compiler-sfc/src/compileScript.ts` (TYPESCRIPT) | Magnitude: 95.01 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 778, branch: 314, structural_boundaries: 108, safety: 79
- `packages/server-renderer/src/webpack-plugin/client.ts` (TYPESCRIPT) | Magnitude: 5.4 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 19, args: 17, immutability_locks: 15
- `scripts/git-hooks/commit-msg` (SHELL) | Magnitude: 11.92 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, io: 13, indent_spaces: 7, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/core/observer/dep.ts` (TYPESCRIPT) | Magnitude: 16.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 46, branch: 17, structural_boundaries: 14
- `benchmarks/big-table/index.html` (HTML) | Magnitude: 155.78 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 70, structural_boundaries: 35, args: 16
- `packages/server-renderer/src/template-renderer/index.ts` (TYPESCRIPT) | Magnitude: 39.49 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 240, state_mutation: 118, branch: 70, structural_boundaries: 66
- `scripts/release.js` (JAVASCRIPT) | Magnitude: 179.36 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, concurrency: 43, branch: 40, immutability_locks: 30
- `packages/server-renderer/src/template-renderer/create-async-file-mapper.ts` (TYPESCRIPT) | Magnitude: 5.42 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 13, structural_boundaries: 12, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/core/instance/render-helpers/bind-dynamic-keys.ts` (TYPESCRIPT) | Magnitude: 3.89 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, branch: 9, structural_boundaries: 5, safety_bypasses: 4
- `packages/server-renderer/src/directives/index.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, indent_spaces: 2, branch: 1
- `src/platforms/web/runtime/components/index.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, indent_spaces: 2, branch: 1
- `src/platforms/web/runtime/directives/index.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, indent_spaces: 2, branch: 1
- `src/v3/apiSetup.ts` (TYPESCRIPT) | Magnitude: 22.64 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 169, branch: 52, structural_boundaries: 44, args: 39

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/core/observer/watcher.ts` -> **Severity: 0.703** (Bridge: 0.007 * Flux: 100.0%)
- `packages/compiler-sfc/src/parseComponent.ts` -> **Severity: 0.511** (Bridge: 0.0054 * Flux: 95.0279%)
- `src/core/observer/scheduler.ts` -> **Severity: 0.324** (Bridge: 0.0032 * Flux: 99.7405%)
- `src/core/instance/lifecycle.ts` -> **Severity: 0.261** (Bridge: 0.0043 * Flux: 61.2336%)
- `src/core/vdom/create-functional-component.ts` -> **Severity: 0.178** (Bridge: 0.0018 * Flux: 99.7151%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/shared/util.ts` -> **Severity: 21.377** (Embedded: 0.2348 * Error Risk: 91.0486%)
- `src/types/component.ts` -> **Severity: 20.002** (Embedded: 0.2117 * Error Risk: 94.5018%)
- `src/core/observer/watcher.ts` -> **Severity: 14.421** (Embedded: 0.1444 * Error Risk: 99.8552%)
- `src/v3/reactivity/effectScope.ts` -> **Severity: 13.839** (Embedded: 0.1419 * Error Risk: 97.5591%)
- `src/core/observer/dep.ts` -> **Severity: 11.97** (Embedded: 0.1283 * Error Risk: 93.2602%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/shared/util.ts` -> **Severity: 4697.827** (Blast Radius: 47.254 * Doc Risk: 99.4165%)
- `src/types/compiler.ts` -> **Severity: 4028.58** (Blast Radius: 50.052 * Doc Risk: 80.4879%)
- `packages/compiler-sfc/src/types.ts` -> **Severity: 2978.888** (Blast Radius: 56.743 * Doc Risk: 52.4979%)
- `src/v3/reactivity/effectScope.ts` -> **Severity: 1705.731** (Blast Radius: 18.445 * Doc Risk: 92.4766%)
- `packages/compiler-sfc/src/parseComponent.ts` -> **Severity: 1678.236** (Blast Radius: 27.508 * Doc Risk: 61.009%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
