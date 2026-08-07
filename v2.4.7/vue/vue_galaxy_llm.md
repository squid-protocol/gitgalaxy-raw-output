# ARCHITECTURAL_BRIEF: vue
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/vue` |
| **Timestamp** | `2026-08-07T05:40:34.926983+00:00` |
| **Scan Duration** | `0.83s` |
| **Git Branch** | `main` |
| **Git Commit** | `9e88707940088cb1f4cd7dd210c9168a50dc347c` |
| **Git Remote** | `https://github.com/vuejs/vue` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 248 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.119`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 154 | 51.7% |
| file_cluster_13 | 100 | 33.6% |
| file_cluster_16 | 18 | 6.0% |
| file_cluster_4 | 5 | 1.7% |
| file_cluster_17 | 5 | 1.7% |
| file_cluster_0 | 4 | 1.3% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 25.7 | 15.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 50.4 | 63.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.7 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.2 | 6.1 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 30.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 62.1 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.7 | 22.8 | 0.0 |
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

- `createPatchFunction` (@ `src/core/vdom/patch.ts`) -> Impact: **453.5** | LOC: 826
- `walkDeclaration` (@ `packages/compiler-sfc/src/compileScript.ts`) -> Impact: **339.6** | LOC: 431
  * *Intent:* // if withDefaults() is used, we need to remove the optional flags // on props that have default values
- `onIdentifier` (@ `packages/compiler-sfc/src/babelUtils.ts`) -> Impact: **324.1** | LOC: 358
- `defineReactive` (@ `src/core/observer/index.ts`) -> Impact: **114.7** | LOC: 87
- `_createElement` (@ `src/core/vdom/create-element.ts`) -> Impact: **110.1** | LOC: 95
- `isReferenced` (@ `packages/compiler-sfc/src/babelUtils.ts`) -> Impact: **104.4** | LOC: 168
- `patchVnode` (@ `src/core/vdom/patch.ts`) -> Impact: **104.3** | LOC: 76
- `hydrate` (@ `src/core/vdom/patch.ts`) -> Impact: **97.0** | LOC: 106
- `warn` (@ `src/platforms/web/runtime-with-compiler.ts`) -> Impact: **85.5** | LOC: 61
- `addHandler` (@ `src/compiler/helpers.ts`) -> Impact: **81.3** | LOC: 67

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/compiler/parser` | 5 | 3358.07 | 48.44% | 23.09% |
| `src/compiler` | 7 | 375.09 | 35.55% | 56.26% |
| `scripts` | 7 | 327.58 | 24.89% | 68.5% |
| `benchmarks/dbmon` | 3 | 238.32 | 28.04% | 33.18% |
| `src/core/vdom` | 5 | 234.0 | 31.05% | 59.29% |
| `packages/compiler-sfc/src` | 13 | 223.22 | 25.6% | 30.25% |
| `examples/composition` | 6 | 203.82 | 8.45% | 0.0% |
| `packages/server-renderer/src/optimizing-compiler` | 5 | 169.01 | 38.99% | 44.3% |
| `packages/server-renderer/src` | 10 | 158.95 | 31.88% | 30.79% |
| `benchmarks/uptime` | 1 | 141.98 | 67.73% | 99.82% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/server-renderer/src/create-renderer.ts` -> **100.0%** Exposure
- `packages/server-renderer/src/modules/dom-props.ts` -> **100.0%** Exposure
- `packages/server-renderer/src/render.ts` -> **100.0%** Exposure
- `src/compiler/directives/model.ts` -> **100.0%** Exposure
- `src/core/instance/render-helpers/render-static.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benchmarks/big-table/index.html` -> **100.0%** Exposure
- `benchmarks/dbmon/ENV.js` -> **100.0%** Exposure
- `packages/template-compiler/index.js` -> **100.0%** Exposure
- `packages/server-renderer/src/render-context.ts` -> **100.0%** Exposure
- `packages/server-renderer/src/render-stream.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/core/vdom/patch.ts` -> **0** Orphaned Functions | **52** Duplicates
- `packages/server-renderer/src/render.ts` -> **0** Orphaned Functions | **32** Duplicates
- `packages/compiler-sfc/src/compileScript.ts` -> **0** Orphaned Functions | **22** Duplicates
- `types/vue.d.ts` -> **3** Orphaned Functions | **9** Duplicates
- `src/core/vdom/modules/directives.ts` -> **0** Orphaned Functions | **9** Duplicates

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

### Hardcoded Payload Artifacts
- `examples/classic/firebase/app.js` -> **99.9399%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `489` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/core/util/next-tick.ts` (TYPESCRIPT) -> Cumulative Risk: **686.97**
- **Archetype:** `file_cluster_4` (Distance: 12.087 IQR)
- **Magnitude:** 10.79 | **LOC:** 118 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `nextTick` (Impact: 25.8), `handleError` (Impact: 6.2), `timerFunc` (Impact: 4.6)

### 2. `src/core/observer/dep.ts` (TYPESCRIPT) -> Cumulative Risk: **631.19**
- **Archetype:** `file_cluster_13` (Distance: 12.538 IQR)
- **Magnitude:** 12.86 | **LOC:** 109 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (94.2676%), Documentation (92.8801%)
- **Heaviest Functions:** `update` (Impact: 25.9), `notify` (Impact: 14.9), `depend` (Impact: 10.9)

### 3. `src/core/util/error.ts` (TYPESCRIPT) -> Cumulative Risk: **629.56**
- **Archetype:** `file_cluster_13` (Distance: 12.788 IQR)
- **Magnitude:** 10.6 | **LOC:** 82 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.0462%), Safety Score (80.0%)
- **Heaviest Functions:** `invokeWithErrorHandling` (Impact: 23.1), `handleError` (Impact: 21.3), `pushTarget` (Impact: 13.7)

### 4. `packages/server-renderer/src/template-renderer/index.ts` (TYPESCRIPT) -> Cumulative Risk: **604.3**
- **Archetype:** `file_cluster_4` (Distance: 12.347 IQR)
- **Magnitude:** 30.57 | **LOC:** 307 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.9902%), Safety Score (95.8056%)
- **Heaviest Functions:** `getPreloadType` (Impact: 22.7), `renderPreloadLinks` (Impact: 18.7), `constructor` (Impact: 15.6)

### 5. `src/compiler/helpers.ts` (TYPESCRIPT) -> Cumulative Risk: **603.54**
- **Archetype:** `file_cluster_8` (Distance: 10.552 IQR)
- **Magnitude:** 22.08 | **LOC:** 244 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.2204%), Tech Debt (94.9539%), Documentation (90.256%)
- **Heaviest Functions:** `addHandler` (Impact: 81.3), `addDirective` (Impact: 19.2), `addAttr` (Impact: 15.3)

### 6. `benchmarks/dbmon/ENV.js` (JAVASCRIPT) -> Cumulative Risk: **570.07**
- **Archetype:** `file_cluster_8` (Distance: 11.755 IQR)
- **Magnitude:** 216.34 | **LOC:** 212 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5358%), Safety Score (92.1849%)
- **Heaviest Functions:** `generateRow` (Impact: 32.4), `getData` (Impact: 24.5), `getElapsedClassName` (Impact: 9.3)

### 7. `src/core/vdom/helpers/resolve-async-component.ts` (TYPESCRIPT) -> Cumulative Risk: **560.46**
- **Archetype:** `file_cluster_13` (Distance: 10.521 IQR)
- **Magnitude:** 10.72 | **LOC:** 158 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9881%), State Flux (87.1007%), Verification (80.0%)
- **Heaviest Functions:** `forceRender` (Impact: 24.9), `forceRender` (Impact: 10.8), `ensureCtor` (Impact: 10.7)

### 8. `src/core/instance/events.ts` (TYPESCRIPT) -> Cumulative Risk: **558.95**
- **Archetype:** `file_cluster_8` (Distance: 10.758 IQR)
- **Magnitude:** 21.08 | **LOC:** 161 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.9943%), Verification (80.0%), Safety Score (76.4573%)
- **Heaviest Functions:** `eventsMixin` (Impact: 63.2), `tip` (Impact: 26.3), `off` (Impact: 22.7)

### 9. `src/core/components/keep-alive.ts` (TYPESCRIPT) -> Cumulative Risk: **556.58**
- **Archetype:** `file_cluster_8` (Distance: 10.911 IQR)
- **Magnitude:** 16.52 | **LOC:** 172 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9799%), Safety Score (82.9604%)
- **Heaviest Functions:** `remove` (Impact: 41.5), `render` (Impact: 24.7), `pruneCacheEntry` (Impact: 11.9)

### 10. `src/core/vdom/patch.ts` (TYPESCRIPT) -> Cumulative Risk: **555.3**
- **Archetype:** `file_cluster_8` (Distance: 11.41 IQR)
- **Magnitude:** 176.05 | **LOC:** 908 | **CtrlFlow:** 85.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (90.4322%), Verification (80.0%)
- **Heaviest Functions:** `createPatchFunction` (Impact: 453.5), `patchVnode` (Impact: 104.3), `hydrate` (Impact: 97.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/compiler/parser/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.74 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.895 IQR)
- **Top Global Matches:** file_cluster_8: 10.74, file_cluster_13: 11.268, file_cluster_7: 11.39
- **Magnitude:** 3337.18 | **LOC:** 1000 | **CtrlFlow:** 83.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.0358%), Tech Debt (15.4521%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 63`, `args: 100`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 108`, `dead_code: 1`, `fragile_debt: 5`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.946
  * `Choke Point (Betweenness):` 0.000154 | `Ripple Effect (Closeness):` 0.006734
  * `Imports (Out-Degree: 7):` util, model, he, compiler, html-parser, filter-parser, env, text-parser...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/compiler/error-detector.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.573 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.744 IQR)
- **Top Global Matches:** file_cluster_8: 10.573, file_cluster_4: 10.999, file_cluster_13: 11.005
- **Magnitude:** 309.44 | **LOC:** 159 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6405%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 19`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 12`
* *Architecture:* `api: 2`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 10`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.754
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006061
  * `Imports (Out-Degree: 1):` index, compiler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `benchmarks/dbmon/ENV.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.755 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.049 IQR)
- **Top Global Matches:** file_cluster_8: 11.755, file_cluster_17: 12.084, file_cluster_11: 12.155
- **Magnitude:** 216.34 | **LOC:** 212 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.7987%), Tech Debt (99.5358%)
**Top Internal Functions/Classes:**
  * `generateRow` (Impact: 32.4)
  * `getData` (Impact: 24.5)
  * `getElapsedClassName` (Impact: 9.3)
  * `countClassName` (Impact: 9.3)
  * `updateQuery` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 40`, `args: 12`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 99`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/vdom/patch.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.41 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.748 IQR)
- **Top Global Matches:** file_cluster_8: 11.41, file_cluster_13: 11.721, file_cluster_7: 11.889
- **Magnitude:** 176.05 | **LOC:** 908 | **CtrlFlow:** 85.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.968%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `createPatchFunction` (Impact: 453.5)
  * `patchVnode` (Impact: 104.3)
  * `hydrate` (Impact: 97.0)
  * `updateChildren` (Impact: 78.3)
    * *Intent:* // we have a recursively passed down rm callback // increase the listeners count
  * `createElm` (Impact: 68.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 43`, `args: 101`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 5`, `state_mutation: 104`, `dead_code: 4`, `fragile_debt: 1`, `duplicate_logic: 52`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 34`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.07
  * `Choke Point (Betweenness):` 0.000503 | `Ripple Effect (Closeness):` 0.010774
  * `Imports (Out-Degree: 5):` index, traverse, vnode, element, config, constants, template-ref, lifecycle
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scripts/release.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.185 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.618 IQR)
- **Top Global Matches:** file_cluster_4: 10.185, file_cluster_8: 10.384, file_cluster_13: 10.516
- **Magnitude:** 162.96 | **LOC:** 203 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.5752%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 40.9)
  * `publishPackage` (Impact: 38.8)
  * `step` (Impact: 4.3)
    * *Intent:* // build all packages with types
  * `step` (Impact: 4.0)
  * `step` (Impact: 3.2)
    * *Intent:* // run tests before release
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 28`, `args: 11`, `func_start: 19`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 7`
* *Architecture:* `io: 13`, `concurrency: 43`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, execa, package.json, enquirer, minimist, semver, chalk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benchmarks/uptime/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.142 IQR)
- **Top Global Matches:** file_cluster_8: 11.142, file_cluster_17: 11.354, file_cluster_4: 11.448
- **Magnitude:** 141.98 | **LOC:** 201 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.7281%), Tech Debt (99.8224%)
**Top Internal Functions/Classes:**
  * `maxStreak` (Impact: 11.0)
  * `generateServer` (Impact: 6.3)
  * `clearTimeout` (Impact: 6.1)
  * `toggle` (Impact: 5.6)
  * `render` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 31`, `args: 13`, `func_start: 15`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 69`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 6`
* *Defense:* `doc: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server-renderer/src/optimizing-compiler/modules.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.646 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.34 IQR)
- **Top Global Matches:** file_cluster_13: 9.646, file_cluster_8: 9.717, file_cluster_17: 9.813
- **Magnitude:** 116.41 | **LOC:** 119 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.4006%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 32`, `args: 10`, `func_start: 7`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.86
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.004489
  * `Imports (Out-Degree: 4):` util, index, compiler, codegen, attrs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `benchmarks/big-table/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.77 IQR)
- **Top Global Matches:** file_cluster_0: 11.77, file_cluster_8: 11.922, file_cluster_13: 11.967
- **Magnitude:** 115.08 | **LOC:** 164 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.9832%), Tech Debt (97.2785%)
**Top Internal Functions/Classes:**
  * `generateGrid` (Impact: 10.1)
  * `visibleCount` (Impact: 9.4)
  * `unmount` (Impact: 2.2)
  * `rerender` (Impact: 2.2)
  * `onhashchange` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 35`, `args: 16`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 70`, `duplicate_logic: 3`
* *Architecture:* `io: 5`, `api: 2`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` demo.css, style.css, vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-sfc/src/compileScript.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.653 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.121 IQR)
- **Top Global Matches:** file_cluster_17: 13.653, file_cluster_13: 13.68, file_cluster_0: 13.754
- **Magnitude:** 89.73 | **LOC:** 1917 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3656%), Tech Debt (99.9245%)
**Top Internal Functions/Classes:**
  * `walkDeclaration` (Impact: 339.6)
    * *Intent:* // if withDefaults() is used, we need to remove the optional flags // on props that have default val...
  * `inferRuntimeType` (Impact: 80.5)
  * `walkDeclaration` (Impact: 66.5)
  * `walkPattern` (Impact: 39.7)
  * `isCallOf` (Impact: 36.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 108`, `args: 33`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 52`, `dead_code: 21`, `planned_debt: 2`, `duplicate_logic: 22`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 22`
* *Defense:* `safety: 79`, `doc: 7`, `test: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.621
  * `Choke Point (Betweenness):` 0.003849 | `Ripple Effect (Closeness):` 0.039075
  * `Imports (Out-Degree: 11):` source-map, cssVars, warn, rewriteDefault, text-parser, magic-string, types, util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/classic/elastic-header/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.377 IQR)
- **Top Global Matches:** file_cluster_0: 11.377, file_cluster_8: 11.425, file_cluster_13: 11.728
- **Magnitude:** 78.3 | **LOC:** 106 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.1763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDrag` (Impact: 7.4)
  * `stopDrag` (Impact: 4.1)
  * `contentPosition` (Impact: 3.8)
  * `startDrag` (Impact: 3.8)
  * `data` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 18`, `args: 9`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 50`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 3`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js, style.css, dynamics.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/composition/todomvc.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 8.703 IQR)
- **Top Global Matches:** file_cluster_0: 8.703, file_cluster_8: 8.793, file_cluster_11: 8.965
- **Magnitude:** 76.44 | **LOC:** 242 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.1715%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 16.5)
  * `onHashChange` (Impact: 7.4)
  * `addTodo` (Impact: 5.8)
  * `doneEdit` (Impact: 5.7)
  * `pluralize` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 39`, `args: 30`, `func_start: 21`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 39`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.css, vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benchmarks/svg/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.483 IQR)
- **Top Global Matches:** file_cluster_8: 10.483, file_cluster_4: 10.693, file_cluster_0: 10.934
- **Magnitude:** 76.32 | **LOC:** 103 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createModel` (Impact: 13.3)
  * `move` (Impact: 10.3)
  * `render` (Impact: 4.5)
  * `created` (Impact: 4.2)
  * `toggleOptimization` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 13`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 7`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stats.min.js, vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/build.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.869 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.657 IQR)
- **Top Global Matches:** file_cluster_8: 9.869, file_cluster_13: 9.937, file_cluster_4: 10.034
- **Magnitude:** 70.18 | **LOC:** 98 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.9244%), Tech Debt (99.9955%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 15.2)
  * `buildEntry` (Impact: 9.2)
  * `build` (Impact: 6.7)
  * `next` (Impact: 5.6)
  * `report` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 21`, `args: 16`, `func_start: 15`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 4`
* *Architecture:* `io: 12`, `concurrency: 7`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003367
  * `Imports (Out-Degree: 0):` config, terser, path, rollup, zlib, fs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/classic/grid/grid.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.631 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.043 IQR)
- **Top Global Matches:** file_cluster_8: 11.631, file_cluster_17: 11.815, file_cluster_15: 12.091
- **Magnitude:** 59.52 | **LOC:** 70 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.7131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `filteredData` (Impact: 13.2)
  * `data` (Impact: 2.2)
  * `capitalize` (Impact: 1.9)
  * `sortBy` (Impact: 1.9)
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

### `packages/compiler-sfc/src/babelUtils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.864 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.638 IQR)
- **Top Global Matches:** file_cluster_8: 9.864, file_cluster_13: 10.348, file_cluster_0: 10.44
- **Magnitude:** 59.37 | **LOC:** 424 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.7367%), Tech Debt (99.3968%)
**Top Internal Functions/Classes:**
  * `onIdentifier` (Impact: 324.1)
  * `isReferenced` (Impact: 104.4)
  * `extractIdentifiers` (Impact: 35.1)
  * `onIdent` (Impact: 26.9)
  * `isInDestructureAssignment` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 90`, `args: 22`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`, `duplicate_logic: 8`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.309
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.032279
  * `Imports (Out-Degree: 1):` bar, foo, types, estree-walker
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.171 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.85 IQR)
- **Top Global Matches:** file_cluster_8: 9.171, file_cluster_13: 9.21, file_cluster_0: 9.452
- **Magnitude:** 58.3 | **LOC:** 306 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.0305%), Tech Debt (91.0097%)
**Top Internal Functions/Classes:**
  * `genConfig` (Impact: 19.1)
  * `resolve` (Impact: 5.6)
  * `onwarn` (Impact: 3.7)
  * `ts` (Impact: 3.6)
  * `warn` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 7`, `args: 5`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3`, `dead_code: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 7`, `api: 4`, `import: 16`
* *Defense:* `safety: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` plugin-alias, rollup-plugin-typescript2, package.json, feature-flags, plugin-commonjs, plugin-node-resolve, package.json, plugin-replace...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server-renderer/src/util.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.164 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.175 IQR)
- **Top Global Matches:** file_cluster_8: 8.164, file_cluster_4: 8.681, file_cluster_7: 9.011
- **Magnitude:** 56.25 | **LOC:** 115 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
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

### `examples/classic/tree/tree.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.945 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.129 IQR)
- **Top Global Matches:** file_cluster_8: 10.945, file_cluster_7: 11.559, file_cluster_15: 11.669
- **Magnitude:** 52.6 | **LOC:** 76 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.0947%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changeType` (Impact: 3.8)
  * `isFolder` (Impact: 3.7)
  * `toggle` (Impact: 3.7)
  * `data` (Impact: 2.0)
  * `addChild` (Impact: 2.0)
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

### `src/compiler/codegen/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.796 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.801 IQR)
- **Top Global Matches:** file_cluster_8: 10.796, file_cluster_13: 11.022, file_cluster_17: 11.18
- **Magnitude:** 51.99 | **LOC:** 669 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.1415%), Tech Debt (99.2009%)
**Top Internal Functions/Classes:**
  * `genElement` (Impact: 66.6)
  * `genChildren` (Impact: 40.8)
  * `genFor` (Impact: 39.8)
  * `genScopedSlot` (Impact: 35.8)
  * `genData` (Impact: 26.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 90`, `args: 37`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 75`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 1`, `api: 12`, `import: 7`
* *Defense:* `safety: 4`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.255
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.007576
  * `Imports (Out-Degree: 4):` util, compiler, events, index, types, helpers, index
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/server-renderer/src/render.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.063 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.097 IQR)
- **Top Global Matches:** file_cluster_8: 11.063, file_cluster_13: 11.151, file_cluster_4: 11.453
- **Magnitude:** 48.93 | **LOC:** 460 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.0458%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `renderAsyncComponent` (Impact: 45.2)
  * `renderComponent` (Impact: 45.1)
  * `renderNode` (Impact: 25.1)
  * `renderElement` (Impact: 21.6)
  * `resolve` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 41`, `args: 61`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 45`, `planned_debt: 1`, `duplicate_logic: 32`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 8`, `immutability_locks: 47`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` component, util, runtime-helpers, vnode, options, render-context, constants, debug...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/classic/todomvc/app.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.73%)
- **Global Archetype:** `file_cluster_11` (Drift: 11.277 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.33 IQR)
- **Top Global Matches:** file_cluster_11: 11.277, file_cluster_6: 11.413, file_cluster_17: 11.418
- **Magnitude:** 45.24 | **LOC:** 158 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.7123%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetch` (Impact: 3.9)
  * `pluralize` (Impact: 3.6)
  * `active` (Impact: 2.0)
  * `completed` (Impact: 2.0)
  * `set` (Impact: 2.0)
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

### `examples/composition/svg.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.666 IQR)
- **Top Global Matches:** file_cluster_8: 8.666, file_cluster_2: 9.136, file_cluster_0: 9.247
- **Magnitude:** 44.54 | **LOC:** 173 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.116%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 7.1)
  * `remove` (Impact: 5.5)
  * `add` (Impact: 3.9)
  * `valueToPoint` (Impact: 2.6)
    * *Intent:* // math helper...
  * `setup` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 21`, `args: 17`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 13`, `duplicate_logic: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 4`
* *Defense:* `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/observer/watcher.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.236 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.558 IQR)
- **Top Global Matches:** file_cluster_13: 14.236, file_cluster_11: 14.41, file_cluster_17: 14.586
- **Magnitude:** 39.86 | **LOC:** 279 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 32.5)
  * `run` (Impact: 12.8)
  * `get` (Impact: 12.5)
  * `recordEffectScope` (Impact: 11.0)
  * `teardown` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 20`, `args: 21`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 256`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 7`, `import: 8`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.922
  * `Choke Point (Betweenness):` 0.007034 | `Ripple Effect (Closeness):` 0.144416
  * `Imports (Out-Degree: 6):` component, index, dep, effectScope, debug, traverse, scheduler
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `examples/composition/grid.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.859 IQR)
- **Top Global Matches:** file_cluster_8: 7.859, file_cluster_7: 8.756, file_cluster_17: 8.849
- **Magnitude:** 36.44 | **LOC:** 174 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `capitalize` (Impact: 11.2)
  * `setup` (Impact: 9.1)
  * `data` (Impact: 2.2)
  * `sortBy` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 17`, `args: 13`, `func_start: 4`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vue.min.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/classic/firebase/app.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.221 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.58 IQR)
- **Top Global Matches:** file_cluster_8: 11.221, file_cluster_17: 11.702, file_cluster_7: 11.812
- **Magnitude:** 35.62 | **LOC:** 58 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.513%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addUser` (Impact: 3.8)
  * `validation` (Impact: 2.0)
  * `isValid` (Impact: 2.0)
  * `removeUser` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `io: 2`, `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/classic/elastic-header/index.html` (HTML) | Magnitude: 78.3 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 50, structural_boundaries: 18, args: 9
- `examples/composition/todomvc.html` (HTML) | Magnitude: 76.44 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 39, planned_debt: 39, args: 30
- `benchmarks/big-table/index.html` (HTML) | Magnitude: 115.08 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 70, structural_boundaries: 35, args: 16
- `examples/classic/todomvc/index.html` (HTML) | Magnitude: 17.34 | Delta: **0.4 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 60, decorators: 29, structural_boundaries: 20, planned_debt: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/classic/todomvc/app.js` (JAVASCRIPT) | Magnitude: 45.24 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 16, structural_boundaries: 15, args: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/core/observer/dep.ts` (TYPESCRIPT) | Magnitude: 12.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 38, branch: 17, structural_boundaries: 14
- `types/index.d.ts` (TYPESCRIPT) | Magnitude: 3.08 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, api: 14, import: 13
- `src/v3/sfc-helpers/useCssVars.ts` (TYPESCRIPT) | Magnitude: 2.28 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, branch: 7, immutability_locks: 5
- `src/v3/apiSetup.ts` (TYPESCRIPT) | Magnitude: 23.4 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 169, branch: 52, structural_boundaries: 44, args: 39
- `src/platforms/web/runtime/modules/class.ts` (TYPESCRIPT) | Magnitude: 2.58 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 9, branch: 8, immutability_locks: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `types/v3-setup-context.d.ts` (TYPESCRIPT) | Magnitude: 17.26 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 20, generics: 16, args: 8
- `types/jsx.d.ts` (TYPESCRIPT) | Magnitude: 2.08 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, branch: 17, doc: 17, structural_boundaries: 15
- `src/v3/reactivity/computed.ts` (TYPESCRIPT) | Magnitude: 4.42 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 30, generics: 22, branch: 11
- `types/vue.d.ts` (TYPESCRIPT) | Magnitude: 6.71 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 365, generics: 78, structural_boundaries: 60, args: 47
- `src/types/global-api.ts` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 15, args: 11, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/compiler-sfc/src/compileScript.ts` (TYPESCRIPT) | Magnitude: 89.73 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 778, branch: 314, structural_boundaries: 108, safety: 79
- `src/core/util/props.ts` (TYPESCRIPT) | Magnitude: 22.47 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 176, branch: 73, structural_boundaries: 58, args: 26
- `packages/server-renderer/src/webpack-plugin/client.ts` (TYPESCRIPT) | Magnitude: 5.25 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 19, args: 17, immutability_locks: 15
- `src/compiler/to-function.ts` (TYPESCRIPT) | Magnitude: 16.05 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, branch: 24, structural_boundaries: 22, args: 11
- `scripts/git-hooks/commit-msg` (SHELL) | Magnitude: 11.92 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, io: 13, indent_spaces: 7, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/server-renderer/src/template-renderer/index.ts` (TYPESCRIPT) | Magnitude: 30.57 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 240, state_mutation: 118, branch: 70, structural_boundaries: 66
- `scripts/release.js` (JAVASCRIPT) | Magnitude: 162.96 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, concurrency: 43, branch: 40, immutability_locks: 30
- `packages/server-renderer/src/template-renderer/create-async-file-mapper.ts` (TYPESCRIPT) | Magnitude: 5.46 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 13, structural_boundaries: 12, branch: 8
- `src/v3/apiAsyncComponent.ts` (TYPESCRIPT) | Magnitude: 16.42 | Delta: **0.256 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, branch: 31, structural_boundaries: 27, concurrency: 27
- `src/core/util/next-tick.ts` (TYPESCRIPT) | Magnitude: 10.79 | Delta: **0.346 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, concurrency: 26, branch: 23, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/core/instance/render-helpers/bind-dynamic-keys.ts` (TYPESCRIPT) | Magnitude: 2.75 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, branch: 9, structural_boundaries: 5, safety_bypasses: 4
- `src/core/vdom/create-element.ts` (TYPESCRIPT) | Magnitude: 19.71 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, branch: 55, structural_boundaries: 22, args: 14
- `packages/server-renderer/src/directives/index.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, indent_spaces: 2, branch: 1
- `src/platforms/web/runtime/components/index.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, indent_spaces: 2, branch: 1
- `src/platforms/web/runtime/directives/index.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 2, indent_spaces: 2, branch: 1

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
- `src/core/vdom/create-functional-component.ts` -> **Severity: 0.178** (Bridge: 0.0018 * Flux: 99.5236%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/shared/util.ts` -> **Severity: 21.377** (Embedded: 0.2348 * Error Risk: 91.0486%)
- `src/types/component.ts` -> **Severity: 20.002** (Embedded: 0.2117 * Error Risk: 94.5018%)
- `src/core/observer/watcher.ts` -> **Severity: 14.421** (Embedded: 0.1444 * Error Risk: 99.8552%)
- `src/v3/reactivity/effectScope.ts` -> **Severity: 13.839** (Embedded: 0.1419 * Error Risk: 97.5591%)
- `src/types/vnode.ts` -> **Severity: 11.809** (Embedded: 0.1476 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/shared/util.ts` -> **Severity: 4560.46** (Blast Radius: 47.254 * Doc Risk: 96.5095%)
- `src/types/compiler.ts` -> **Severity: 3703.543** (Blast Radius: 50.052 * Doc Risk: 73.9939%)
- `packages/compiler-sfc/src/types.ts` -> **Severity: 2153.561** (Blast Radius: 56.743 * Doc Risk: 37.9529%)
- `src/core/observer/dep.ts` -> **Severity: 1393.109** (Blast Radius: 14.999 * Doc Risk: 92.8801%)
- `src/v3/reactivity/ref.ts` -> **Severity: 997.19** (Blast Radius: 10.403 * Doc Risk: 95.856%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
