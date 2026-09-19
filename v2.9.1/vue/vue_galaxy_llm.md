# ARCHITECTURAL_BRIEF: vue
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/vuejs/vue` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 484 analyzed artifact(s), 66104 LOC.
- **Load-bearing artifact:** `src/shared/util.ts` -- 64 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/compiler-sfc/src/compileScript.ts` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/compiler/parser/index.ts` at magnitude 21670.39 (structural weight, not risk).
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
| Total Artifacts | 508 |
| Analyzed Artifacts (Scanned) | 484 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24 |
| Total LOC | 66104 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 95.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5692 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1594 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6566 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 45 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 390 | 61959 | 80.6% |
| JAVASCRIPT | 35 | 1623 | 7.2% |
| HTML | 24 | 2027 | 5.0% |
| JSON | 12 | 222 | 2.5% |
| CSS | 9 | 255 | 1.9% |
| PLAINTEXT | 6 | 0 | 1.2% |
| MARKDOWN | 5 | 0 | 1.0% |
| SHELL | 2 | 16 | 0.4% |
| YAML | 1 | 2 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.055`
> **Composition Archetype:** `Hub-Coupled App` (z +2.06; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 18%, Declarative / Non-Code 17%, Callbacks & Closures Files 14%, Compute Cores Files 13%, Large Core Modules (3) 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 473 | 97.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 2.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24*

**Composition by Extension & Reason:**
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 9 LOC), 1x Excluded (Machine-Generated Source Code Signature: 163 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 2x Excluded (Unsupported Extension: '.snap')
- `.css`: 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 7018 LOC)
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 207 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 22.1 | 8.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 48.9 | 56.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 3.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.0 | 8.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 73.9 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 174 | 67 | 1 | `types/test/v3/define-component-test.tsx` |
| cleanup | 34 | 21 | 0 | `test/unit/features/instance/methods-lifecycle.spec.ts` |
| guards | 461 | 124 | 3 | `test/unit/features/v3/reactivity/readonly.spec.ts` |
| danger | 1309 | 224 | 7 | `packages/compiler-sfc/src/compileScript.ts` |
| concurrency | 1240 | 106 | 4 | `test/e2e/todomvc.spec.ts` |
| connectivity | 1375 | 293 | 7 | `packages/compiler-sfc/test/rewriteDefault.spec.ts` |
| io | 447 | 70 | 2 | `test/e2e/commits.mock.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 1 | 0 | `benchmarks/dbmon/ENV.js` |
| time | 125 | 35 | 0 | `test/unit/features/component/component-async.spec.ts` |
| serialization | 59 | 34 | 0 | `test/unit/modules/compiler/compiler-options.spec.ts` |
| regex | 155 | 59 | 1 | `src/compiler/parser/index.ts` |
| events | 881 | 154 | 4 | `test/unit/features/v3/apiWatch.spec.ts` |
| tests | 7147 | 146 | 46 | `test/unit/modules/compiler/parser.spec.ts` |
| docs | 304 | 96 | 1 | `types/jsx.d.ts` |
| debt | 561 | 97 | 2 | `test/e2e/todomvc.spec.ts` |
| mutation | 12383 | 397 | 59 | `test/unit/features/v3/apiWatch.spec.ts` |
| dead_code | 347 | 121 | 2 | `packages/compiler-sfc/src/compileScript.ts` |
| credential | 3 | 2 | 0 | `test/e2e/commits.mock.ts` |
| threat | 220 | 75 | 1 | `test/unit/modules/compiler/codegen.spec.ts` |
| ml_ai | 20 | 10 | 0 | `test/unit/modules/vdom/patch/children.spec.ts` |
| ui | 313 | 52 | 1 | `types/test/v3/define-component-test.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/e2e/commits.mock.ts` (Hits: 186)
- `examples/classic/todomvc/index.html` (Hits: 14)
- `scripts/git-hooks/commit-msg` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.ts** (`src/shared/util.ts`) — 64 inbound connections
2. **component.ts** (`src/types/component.ts`) — 44 inbound connections
3. **vnode.ts** (`src/core/vdom/vnode.ts`) — 41 inbound connections
4. **compiler.ts** (`src/types/compiler.ts`) — 31 inbound connections
5. **vnode.ts** (`src/types/vnode.ts`) — 30 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compileScript.ts** (`packages/compiler-sfc/src/compileScript.ts`) — 22 outbound dependencies
2. **index.ts** (`src/v3/index.ts`) — 18 outbound dependencies
3. **index.d.ts** (`types/index.d.ts`) — 17 outbound dependencies
4. **compileScript.spec.ts** (`packages/compiler-sfc/test/compileScript.spec.ts`) — 16 outbound dependencies
5. **lifecycle.ts** (`src/core/instance/lifecycle.ts`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `compileScript` **(Many-Argument Workhorses)** (@ `packages/compiler-sfc/src/compileScript.ts`) -> Impact: **575.0** | LOC: 1176
  * *Intent:* /** * Compile `<script setup>` * It requires the whole SFC descriptor because we need to handle and merge * normal `<script>` + `<script setup>` if bo...
- `createPatchFunction` **(Compute Cores)** (@ `src/core/vdom/patch.ts`) -> Impact: **381.5** | LOC: 842
- `parseHTML` **(Many-Argument Workhorses)** (@ `src/compiler/parser/html-parser.ts`) -> Impact: **162.5** | LOC: 271
- `doWatch` **(Many-Argument Workhorses)** (@ `src/v3/apiWatch.ts`) -> Impact: **144.0** | LOC: 200
- `addHandler` **(Many-Argument Workhorses)** (@ `src/compiler/helpers.ts`) -> Impact: **115.0** | LOC: 79
- `defineReactive` **(Many-Argument Workhorses)** (@ `src/core/observer/index.ts`) -> Impact: **114.7** | LOC: 87
  * *Intent:* /** * Define a reactive property on an Object. */
- `_createElement` **(Many-Argument Workhorses)** (@ `src/core/vdom/create-element.ts`) -> Impact: **110.1** | LOC: 95
- `isReferenced` **(Many-Argument Workhorses)** (@ `packages/compiler-sfc/src/babelUtils.ts`) -> Impact: **104.4** | LOC: 168
  * *Intent:* /** * Copied from https://github.com/babel/babel/blob/main/packages/babel-types/src/validators/isReferenced.ts * This file should not change very ofte...
- `patchVnode` **(Many-Argument Workhorses)** (@ `src/core/vdom/patch.ts`) -> Impact: **104.3** | LOC: 76
- `enter` **(Many-Argument Workhorses)** (@ `src/platforms/web/runtime/modules/transition.ts`) -> Impact: **100.7** | LOC: 143

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/compiler/parser` | 5 | 22253.21 | 65.71% | 13.16% |
| `packages/compiler-sfc/test` | 10 | 4502.54 | 2.91% | 0.0% |
| `packages/compiler-sfc/src` | 13 | 2912.43 | 32.49% | 1.48% |
| `src/compiler` | 7 | 2267.21 | 50.34% | 4.7% |
| `src/core/vdom` | 5 | 1981.3 | 74.32% | 1.87% |
| `src/types` | 8 | 1776.86 | 11.25% | 12.46% |
| `packages/server-renderer/src/optimizing-compiler` | 5 | 1636.88 | 49.04% | 0.0% |
| `test/unit/features/v3` | 7 | 1597.3 | 38.14% | 0.0% |
| `src/core/instance` | 8 | 1366.66 | 63.15% | 1.52% |
| `packages/server-renderer/src` | 10 | 1254.0 | 38.7% | 13.29% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `types/v3-manual-apis.d.ts` -> **99.7527%** Exposure
- `packages/server-renderer/src/webpack-plugin/client.ts` -> **99.708%** Exposure
- `packages/server-renderer/src/create-basic-renderer.ts` -> **98.2014%** Exposure
- `packages/server-renderer/types/index.d.ts` -> **98.2014%** Exposure
- `packages/server-renderer/src/webpack-plugin/server.ts` -> **95.7035%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/dbmon/ENV.js` -> **100.0%** Exposure
- `benchmarks/dbmon/lib/memory-stats.js` -> **100.0%** Exposure
- `benchmarks/dbmon/lib/monitor.js` -> **100.0%** Exposure
- `packages/server-renderer/src/render-context.ts` -> **100.0%** Exposure
- `packages/server-renderer/src/template-renderer/template-stream.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/features/options/errorCaptured.spec.ts` -> **0** Orphaned Functions | **33** Duplicates
- `test/unit/features/options/inject.spec.ts` -> **1** Orphaned Functions | **27** Duplicates
- `types/test/options-test.ts` -> **23** Orphaned Functions | **0** Duplicates
- `test/unit/features/error-handling.spec.ts` -> **6** Orphaned Functions | **14** Duplicates
- `types/test/v3/define-component-test.tsx` -> **6** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `examples/classic/firebase/app.js` -> **99.9399%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `734` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/compiler/parser/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 21670.39 | **LOC:** 1000 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **9**; blast radius 2.844; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.3%), Complexity Load (formerly Cognitive Load) (79.1%), Connectivity (formerly Api Exposure) (64.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 68`, `args: 40`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 123`, `dead_code: 1`, `fragile_debt: 5`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.844
  * `Choke Point (Betweenness):` 0.000329 | `Ripple Effect (Closeness):` 0.017894
  * `Imports (Out-Degree: 6):` model, helpers, filter-parser, html-parser, text-parser, env, he, util...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `packages/compiler-sfc/test/rewriteDefault.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3581.64 | **LOC:** 312 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.856; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (91.9%), Dead Code Surface (formerly Dead Code) (73.9%), Guard Balance (formerly Safety Score) (33.7%), Connectivity (formerly Api Exposure) (13.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 127`, `args: 24`, `func_start: 18`, `class_start: 10`
* *Risk/State:* `state_mutation: 4`, `dead_code: 14`
* *Architecture:* `api: 58`, `concurrency: 12`, `import: 20`
* *Defense:* `safety: 2`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..., src, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-sfc/src/compileScript.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1717.66 | **LOC:** 1917 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 4.241; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (84.6%), Complexity Load (formerly Cognitive Load) (68.2%), Connectivity (formerly Api Exposure) (40.5%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileScript` **(Many-Argument Workhorses)** (Impact: 575.0)
    * *Intent:* /** * Compile `<script setup>` * It requires the whole SFC descriptor because we need to handle and ...
  * `inferRuntimeType` **(Compute Cores)** (Impact: 80.5)
  * `removeSpecifier` **(Compute Cores)** (Impact: 71.6)
  * `walkDeclaration` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `analyzeBindingsFromOptions` **(Compute Cores)** (Impact: 40.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 97 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 528`, `structural_boundaries: 317`, `args: 66`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 104`, `dead_code: 28`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 9`, `doc: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.241
  * `Choke Point (Betweenness):` 0.00172 | `Ripple Effect (Closeness):` 0.030099
  * `Imports (Out-Degree: 11):` $node.source.value, babelUtils, cssVars, parseComponent, rewriteDefault, types, warn, x...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/types/options.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1661.63 | **LOC:** 115 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 16.736; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.9%), Connectivity (formerly Api Exposure) (45.3%), Complexity Load (formerly Cognitive Load) (23.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 26`, `args: 6`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.736
  * `Choke Point (Betweenness):` 0.001006 | `Ripple Effect (Closeness):` 0.110425
  * `Imports (Out-Degree: 4):` component, vnode, apiSetup, debug
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/compiler/error-detector.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1466.29 | **LOC:** 159 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.115; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.1%), Connectivity (formerly Api Exposure) (24.6%), Complexity Load (formerly Cognitive Load) (19.7%), Concurrency Surface (formerly Concurrency) (17.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 22`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 1`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.115
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.003727
  * `Imports (Out-Degree: 2):` index, compiler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/core/vdom/patch.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1313.7 | **LOC:** 908 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 2.21; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Guard Balance (formerly Safety Score) (90.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPatchFunction` **(Compute Cores)** (Impact: 381.5)
  * `patchVnode` **(Many-Argument Workhorses)** (Impact: 104.3)
  * `hydrate` **(Many-Argument Workhorses)** (Impact: 92.5)
    * *Intent:* // Note: this is a browser-only function so we can assume elms are DOM nodes.
  * `updateChildren` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `createElm` **(Many-Argument Workhorses)** (Impact: 68.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 46`, `args: 31`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 88`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.21
  * `Choke Point (Betweenness):` 0.000633 | `Ripple Effect (Closeness):` 0.016908
  * `Imports (Out-Degree: 5):` config, lifecycle, traverse, index, template-ref, vnode, constants, element
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/server-renderer/src/optimizing-compiler/modules.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1139.96 | **LOC:** 119 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 1.26; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (72.0%), Connectivity (formerly Api Exposure) (42.6%), Complexity Load (formerly Cognitive Load) (37.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 33`, `args: 10`, `func_start: 6`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.26
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.003727
  * `Imports (Out-Degree: 4):` util, codegen, index, compiler, attrs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/unit/features/v3/apiWatch.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 763.56 | **LOC:** 1235 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.856; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (49.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Callbacks & Closures)** (Impact: 2.8)
  * `setup` **(Callbacks & Closures)** (Impact: 2.6)
  * `render` **(Interface Declarations)** (Impact: 2.1)
  * `render` **(Interface Declarations)** (Impact: 2.1)
  * `setup` **(Callbacks & Closures)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 88 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 546
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 232`, `args: 170`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 108`, `duplicate_logic: 7`
* *Architecture:* `concurrency: 106`, `import: 5`
* *Defense:* `safety: 5`, `test: 182`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` observer, util, component, v3, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/codegen/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 729.82 | **LOC:** 669 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 1.709; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.5%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genElement` **(Compute Cores)** (Impact: 66.6)
  * `genScopedSlots` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `genChildren` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `genData` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `genFor` **(Many-Argument Workhorses)** (Impact: 39.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 111`, `args: 40`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 69`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `import: 7`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.709
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.007394
  * `Imports (Out-Degree: 4):` index, helpers, index, events, types, util, compiler
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/compiler-sfc/test/cssVars.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 557.62 | **LOC:** 248 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.856; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (35.7%), Connectivity (formerly Api Exposure) (7.5%), Dead Code Surface (formerly Dead Code) (6.7%), Complexity Load (formerly Cognitive Load) (2.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 40`, `args: 22`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` src, util, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server-renderer/src/util.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 523.28 | **LOC:** 115 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.856; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Connectivity (formerly Api Exposure) (72.9%), Guard Balance (formerly Safety Score) (63.1%), Mutation Surface (formerly State Flux) (43.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 24`, `args: 9`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 3`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/instance/lifecycle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 451.24 | **LOC:** 422 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **14**; blast radius 4.26; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (77.9%), Connectivity (formerly Api Exposure) (66.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateChildComponent` **(Many-Argument Workhorses)** (Impact: 71.4)
  * `mountComponent` **(Many-Argument Workhorses)** (Impact: 42.9)
  * `lifecycleMixin` **(Compute Cores)** (Impact: 29.7)
  * `callHook` **(Many-Argument Workhorses)** (Impact: 21.5)
  * `_update` **(Many-Argument Workhorses)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 40`, `args: 18`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `import: 14`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.26
  * `Choke Point (Betweenness):` 0.002591 | `Ripple Effect (Closeness):` 0.08295
  * `Imports (Out-Degree: 11):` config, dep, index, watcher, index, perf, vnode, events...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/core/util/options.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 416.68 | **LOC:** 490 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.928; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.0%)
- **Documentation Coverage:** 42.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `watch` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* /** * Watchers. * * Watchers hashes should not overwrite one * another, so we merge them as arrays. ...
  * `normalizeProps` **(Compute Cores)** (Impact: 27.5)
    * *Intent:* /** * Ensure all props option syntax are normalized into the * Object-based format. */
  * `mergeOptions` **(Many-Argument Workhorses)** (Impact: 26.4)
    * *Intent:* /** * Merge two option objects into a new one. * Core utility used in both instantiation and inherit...
  * `mergeDataOrFn` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* /** * Data */
  * `resolveAsset` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* /** * Resolve an asset. * This function is used because child instances need access * to assets defi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 63`, `args: 25`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 38`
* *Architecture:* `api: 12`, `import: 10`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.928
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.00207
  * `Imports (Out-Degree: 7):` config, index, debug, env, lang, constants, util, component...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server-renderer/src/render.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 398.74 | **LOC:** 460 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.856; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.1%), Complexity Load (formerly Cognitive Load) (60.9%), Concurrency Surface (formerly Concurrency) (56.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderComponent` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `renderAsyncComponent` **(Many-Argument Workhorses)** (Impact: 37.2)
  * `renderStartingTag` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `resolve` **(Defensive Guards)** (Impact: 27.1)
  * `renderNode` **(Compute Cores)** (Impact: 25.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 43`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 38`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` compiler, runtime-helpers, render-context, util, debug, options, create-component, vnode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-sfc/src/babelUtils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 376.24 | **LOC:** 424 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.667; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Connectivity (formerly Api Exposure) (50.1%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isReferenced` **(Many-Argument Workhorses)** (Impact: 104.4)
    * *Intent:* /** * Copied from https://github.com/babel/babel/blob/main/packages/babel-types/src/validators/isRef...
  * `walkIdentifiers` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `enter` **(Compute Cores)** (Impact: 36.5)
  * `extractIdentifiers` **(Compute Cores)** (Impact: 24.7)
  * `walkBlockDeclarations` **(Compute Cores)** (Impact: 20.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 110`, `args: 16`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 10`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.024882
  * `Imports (Out-Degree: 1):` types, bar, estree-walker, foo
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/compiler/parser/html-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 368.96 | **LOC:** 342 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 4.535; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseHTML` **(Many-Argument Workhorses)** (Impact: 162.5)
  * `parseEndTag` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `handleStartTag` **(Compute Cores)** (Impact: 26.5)
  * `parseStartTag` **(I/O & Config Routines)** (Impact: 7.3)
  * `shouldIgnoreFirstNewline` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 30`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 35`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.535
  * `Choke Point (Betweenness):` 0.000431 | `Ripple Effect (Closeness):` 0.034136
  * `Imports (Out-Degree: 4):` lang, util, compiler, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/core/observer/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 365.0 | **LOC:** 340 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **5**; blast radius 8.604; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Guard Balance (formerly Safety Score) (88.3%), Connectivity (formerly Api Exposure) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 21.875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defineReactive` **(Many-Argument Workhorses)** (Impact: 114.7)
    * *Intent:* /** * Define a reactive property on an Object. */
  * `set` **(Many-Argument Workhorses)** (Impact: 42.7)
  * `observe` **(Compute Cores)** (Impact: 31.0)
    * *Intent:* // helpers /** * Attempt to create an observer instance for a value, * returns the new observer if s...
  * `del` **(Compute Cores)** (Impact: 29.8)
  * `reactiveSetter` **(Compute Cores)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 44`, `args: 14`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 18`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `safety: 2`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.604
  * `Choke Point (Betweenness):` 0.001664 | `Ripple Effect (Closeness):` 0.100271
  * `Imports (Out-Degree: 3):` v3, index, vnode, array, dep
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/v3/apiWatch.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 360.96 | **LOC:** 354 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.998; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (87.3%), Complexity Load (formerly Cognitive Load) (75.3%), Connectivity (formerly Api Exposure) (53.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doWatch` **(Many-Argument Workhorses)** (Impact: 144.0)
  * `update` **(Callbacks & Closures)** (Impact: 16.6)
    * *Intent:* // pre
  * `run` **(I/O & Config Routines)** (Impact: 14.9)
    * *Intent:* // overwrite default run
  * `watch` **(Generic / Templated Code)** (Impact: 14.7)
    * *Intent:* // implementation
  * `call` **(Callbacks & Closures)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 102`, `args: 34`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 24`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.998
  * `Choke Point (Betweenness):` 8.3e-05 | `Ripple Effect (Closeness):` 0.004732
  * `Imports (Out-Degree: 7):` scheduler, watcher, currentInstance, debug, computed, reactive, ref, traverse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server-renderer/test/ssr-string.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 352.54 | **LOC:** 2167 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.856; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.7%), Guard Balance (formerly Safety Score) (45.1%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Callbacks & Closures)** (Impact: 9.9)
  * `render` **(Callbacks & Closures)** (Impact: 8.7)
  * `rendered` **(Callbacks & Closures)** (Impact: 6.1)
  * `render` **(Callbacks & Closures)** (Impact: 5.8)
  * `render` **(Callbacks & Closures)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 133
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 361`, `args: 280`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `duplicate_logic: 14`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `concurrency: 58`, `import: 4`
* *Defense:* `safety: 4`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utils, index, vm, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/helpers.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 333.36 | **LOC:** 244 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **3**; blast radius 3.558; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.1%), Complexity Load (formerly Cognitive Load) (81.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addHandler` **(Many-Argument Workhorses)** (Impact: 115.0)
  * `addDirective` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `addAttr` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `getBindingAttr` **(Compute Cores)** (Impact: 14.8)
  * `getAndRemoveAttr` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* // note: this only removes the attr from the Array (attrsList) so that it // doesn't get processed b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 27`, `args: 15`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 30`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.558
  * `Choke Point (Betweenness):` 0.000122 | `Ripple Effect (Closeness):` 0.015246
  * `Imports (Out-Degree: 3):` filter-parser, util, compiler
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/core/instance/state.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 306.38 | **LOC:** 394 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 1.406; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.9%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initComputed` **(Defensive Guards)** (Impact: 33.3)
  * `initData` **(Compute Cores)** (Impact: 24.6)
  * `initProps` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `defineComputed` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `initMethods` **(Compute Cores)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 34`, `args: 25`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 29`
* *Architecture:* `io: 1`, `api: 8`, `import: 9`
* *Defense:* `safety: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.406
  * `Choke Point (Betweenness):` 0.00011 | `Ripple Effect (Closeness):` 0.020944
  * `Imports (Out-Degree: 6):` config, dep, index, watcher, index, lifecycle, component, v3...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `test/e2e/async-edge-cases.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 281.65 | **LOC:** 45 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.856; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 24`, `args: 2`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 3`, `concurrency: 22`, `import: 2`
* *Defense:* `safety: 3`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` e2eUtils, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benchmarks/dbmon/ENV.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 257.64 | **LOC:** 212 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.037; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateRow` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `getData` **(Compute Cores)** (Impact: 20.3)
  * `getElapsedClassName` **(Compute Cores)** (Impact: 7.7)
  * `countClassName` **(Compute Cores)** (Impact: 7.7)
  * `updateQuery` **(Compute Cores)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 40`, `args: 12`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 59`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00207
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/shared/util.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 250.94 | **LOC:** 379 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **64** in-repo importer(s); blast radius 39.062; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 22.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `looseEqual` **(Defensive Guards)** (Impact: 34.9)
    * *Intent:* /** * Check if two values are loosely equal - that is, * if they are plain objects, do they have the...
  * `hasChanged` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is#polyfi...
  * `no` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* /** * Always return false. */
  * `makeMap` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Make a map and return a function for checking if a key * is in that map. */
  * `noop` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /* eslint-disable no-unused-vars */ /** * Perform no operation. * Stubbing args to make Flow happy w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 106`, `args: 47`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 11`
* *Architecture:* `api: 38`, `concurrency: 1`
* *Defense:* `safety: 8`, `doc: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.195144
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 64):` (Excluded from Brief to save tokens)

### `src/platforms/web/runtime/modules/transition.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 240.2 | **LOC:** 342 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.7%), Mutation Surface (formerly State Flux) (65.8%), Connectivity (formerly Api Exposure) (36.4%), Complexity Load (formerly Cognitive Load) (31.2%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enter` **(Many-Argument Workhorses)** (Impact: 100.7)
  * `leave` **(Compute Cores)** (Impact: 60.8)
  * `performLeave` **(I/O & Config Routines)** (Impact: 15.8)
  * `getHookArgumentsLength` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** * Normalize a transition hook's argument length. The hook may be: * - a merged hook (invoker) wi...
  * `checkDuration` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* // only used in dev mode
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 32`, `args: 13`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 7`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.000199 | `Ripple Effect (Closeness):` 0.00207
  * `Imports (Out-Degree: 7):` lifecycle, index, index, vnode, util, vnode, transition-util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/core/observer/watcher.ts` -> **Severity: 0.387** (Bridge: 0.0039 * Flux: 100.0%)
- `src/core/vdom/vnode.ts` -> **Severity: 0.348** (Bridge: 0.0035 * Flux: 100.0%)
- `src/v3/apiSetup.ts` -> **Severity: 0.342** (Bridge: 0.0035 * Flux: 96.8484%)
- `src/core/vdom/create-component.ts` -> **Severity: 0.328** (Bridge: 0.0033 * Flux: 99.7795%)
- `src/core/instance/lifecycle.ts` -> **Severity: 0.259** (Bridge: 0.0026 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/shared/util.ts` -> **Severity: 19.036** (Embedded: 0.1951 * Error Risk: 97.546%)
- `src/types/component.ts` -> **Severity: 16.147** (Embedded: 0.1667 * Error Risk: 96.8658%)
- `src/core/vdom/vnode.ts` -> **Severity: 15.04** (Embedded: 0.1549 * Error Risk: 97.1233%)
- `src/core/observer/watcher.ts` -> **Severity: 11.441** (Embedded: 0.1203 * Error Risk: 95.0814%)
- `src/v3/reactivity/effectScope.ts` -> **Severity: 10.803** (Embedded: 0.1176 * Error Risk: 91.8491%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/types/component.ts` -> **Severity: 6387.2** (Blast Radius: 63.872 * Doc Risk: 100.0%)
- `src/core/vdom/vnode.ts` -> **Severity: 4780.6** (Blast Radius: 47.806 * Doc Risk: 100.0%)
- `packages/compiler-sfc/src/types.ts` -> **Severity: 4195.0** (Blast Radius: 41.95 * Doc Risk: 100.0%)
- `packages/compiler-sfc/src/parseComponent.ts` -> **Severity: 1577.775** (Blast Radius: 21.037 * Doc Risk: 75.0%)
- `src/types/global-api.ts` -> **Severity: 1451.9** (Blast Radius: 14.519 * Doc Risk: 100.0%)

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
