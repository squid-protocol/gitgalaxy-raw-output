# ARCHITECTURAL_BRIEF: vue
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/vuejs/vue` |
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
- **Scope:** 496 analyzed artifact(s), 66706 LOC.
- **Load-bearing artifact:** `src/shared/util.ts` -- 93 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/compiler-sfc/src/compileScript.ts` -- pulls in 21 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/types/options.ts` at magnitude 1661.63 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 496 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12 |
| Total LOC | 66706 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5349 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2253 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 15.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3611 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 34 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 391 | 61993 | 78.8% |
| JAVASCRIPT | 35 | 1623 | 7.1% |
| HTML | 24 | 2027 | 4.8% |
| JSON | 12 | 222 | 2.4% |
| MARKDOWN | 11 | 0 | 2.2% |
| CSS | 10 | 717 | 2.0% |
| PLAINTEXT | 6 | 0 | 1.2% |
| YAML | 5 | 108 | 1.0% |
| SHELL | 2 | 16 | 0.4% |

## 4.1 SOURCE ENCODINGS
All 496 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 20%, Declarative / Non-Code 18%, Callbacks & Closures Files 13%, Compute Cores Files 13%, Large Core Modules (3) 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 479 | 96.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 3.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12*

**Composition by Extension & Reason:**
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 2x Excluded (Unsupported Extension: '.snap')
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 7018 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 20.4 | 6.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.9 | 42.5 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.6 | 2.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.6 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 31.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 64.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 174 | 67 | 1 | `types/test/v3/define-component-test.tsx` |
| cleanup | 34 | 21 | 0 | `test/unit/features/instance/methods-lifecycle.spec.ts` |
| guards | 473 | 126 | 3 | `test/unit/features/v3/reactivity/readonly.spec.ts` |
| danger | 1312 | 225 | 7 | `packages/compiler-sfc/src/compileScript.ts` |
| concurrency | 1240 | 106 | 4 | `test/e2e/todomvc.spec.ts` |
| connectivity | 1361 | 294 | 7 | `packages/compiler-sfc/test/rewriteDefault.spec.ts` |
| io | 447 | 70 | 2 | `test/e2e/commits.mock.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 1 | 0 | `benchmarks/dbmon/ENV.js` |
| time | 125 | 35 | 0 | `test/unit/features/component/component-async.spec.ts` |
| serialization | 59 | 34 | 0 | `test/unit/modules/compiler/compiler-options.spec.ts` |
| regex | 155 | 59 | 1 | `src/compiler/parser/index.ts` |
| events | 883 | 155 | 4 | `test/unit/features/v3/apiWatch.spec.ts` |
| tests | 7162 | 147 | 43 | `test/unit/modules/compiler/parser.spec.ts` |
| docs | 307 | 98 | 1 | `types/jsx.d.ts` |
| debt | 624 | 100 | 3 | `test/e2e/todomvc.spec.ts` |
| mutation | 12392 | 399 | 57 | `test/unit/features/v3/apiWatch.spec.ts` |
| dead_code | 241 | 87 | 1 | `types/test/options-test.ts` |
| credential | 3 | 2 | 0 | `test/e2e/commits.mock.ts` |
| threat | 1 | 1 | 0 | `packages/server-renderer/src/util.ts` |
| ml_ai | 20 | 10 | 0 | `test/unit/modules/vdom/patch/children.spec.ts` |
| ui | 321 | 54 | 1 | `types/test/v3/define-component-test.tsx` |

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

1. **util.ts** (`src/shared/util.ts`) — 93 inbound connections
2. **index.d.ts** (`types/index.d.ts`) — 89 inbound connections
3. **index.ts** (`src/core/util/index.ts`) — 68 inbound connections
4. **vnode.ts** (`src/core/vdom/vnode.ts`) — 49 inbound connections
5. **component.ts** (`src/types/component.ts`) — 44 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compileScript.ts** (`packages/compiler-sfc/src/compileScript.ts`) — 21 outbound dependencies
2. **index.ts** (`src/v3/index.ts`) — 18 outbound dependencies
3. **index.d.ts** (`types/index.d.ts`) — 17 outbound dependencies
4. **lifecycle.ts** (`src/core/instance/lifecycle.ts`) — 14 outbound dependencies
5. **config.js** (`scripts/config.js`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `compileScript` **(Many-Argument Workhorses)** (@ `packages/compiler-sfc/src/compileScript.ts`) -> Impact: **533.4** | LOC: 1176
  * *Intent:* /** * Compile `<script setup>` * It requires the whole SFC descriptor because we need to handle and merge * normal `<script>` + `<script setup>` if bo...
- `createPatchFunction` **(Compute Cores)** (@ `src/core/vdom/patch.ts`) -> Impact: **378.7** | LOC: 842
- `parseHTML` **(Many-Argument Workhorses)** (@ `src/compiler/parser/html-parser.ts`) -> Impact: **160.8** | LOC: 271
- `doWatch` **(Many-Argument Workhorses)** (@ `src/v3/apiWatch.ts`) -> Impact: **140.0** | LOC: 200
- `defineReactive` **(Many-Argument Workhorses)** (@ `src/core/observer/index.ts`) -> Impact: **114.7** | LOC: 87
  * *Intent:* /** * Define a reactive property on an Object. */
- `_createElement` **(Many-Argument Workhorses)** (@ `src/core/vdom/create-element.ts`) -> Impact: **107.6** | LOC: 95
- `addHandler` **(Many-Argument Workhorses)** (@ `src/compiler/helpers.ts`) -> Impact: **106.0** | LOC: 79
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
| `packages/compiler-sfc/src` | 13 | 2746.03 | 31.72% | 1.37% |
| `src/core/vdom` | 5 | 1964.6 | 74.36% | 1.82% |
| `src/types` | 8 | 1774.66 | 11.25% | 11.48% |
| `src/compiler/parser` | 5 | 1698.4 | 51.32% | 10.64% |
| `test/unit/features/v3` | 7 | 1578.6 | 38.07% | 0.0% |
| `src/core/instance` | 8 | 1334.96 | 62.58% | 1.42% |
| `src/compiler` | 7 | 1042.47 | 48.3% | 3.93% |
| `src/core/util` | 9 | 1029.44 | 49.95% | 0.0% |
| `test/unit/features/directives` | 21 | 924.28 | 2.29% | 0.0% |
| `src/core/observer` | 6 | 888.32 | 49.48% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `types/v3-manual-apis.d.ts` -> **99.593%** Exposure
- `packages/server-renderer/src/webpack-plugin/client.ts` -> **99.5664%** Exposure
- `packages/server-renderer/types/index.d.ts` -> **97.0688%** Exposure
- `packages/server-renderer/src/webpack-plugin/server.ts` -> **93.5379%** Exposure
- `packages/server-renderer/src/create-basic-renderer.ts` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/dbmon/ENV.js` -> **100.0%** Exposure
- `benchmarks/dbmon/lib/memory-stats.js` -> **100.0%** Exposure
- `benchmarks/dbmon/lib/monitor.js` -> **100.0%** Exposure
- `packages/server-renderer/src/render-context.ts` -> **100.0%** Exposure
- `packages/server-renderer/src/template-renderer/template-stream.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/features/options/errorCaptured.spec.ts` -> **0** Orphaned Functions | **43** Duplicates
- `test/unit/features/options/inject.spec.ts` -> **1** Orphaned Functions | **31** Duplicates
- `types/test/options-test.ts` -> **23** Orphaned Functions | **2** Duplicates
- `packages/server-renderer/test/ssr-string.spec.ts` -> **1** Orphaned Functions | **20** Duplicates
- `types/test/v3/define-component-test.tsx` -> **6** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `examples/classic/firebase/app.js` -> **99.9399%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `736` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/types/options.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.896)
- **Top Global Matches:** file_cluster_5: 6.896, file_cluster_7: 7.784, file_cluster_12: 9.694
- **Magnitude:** 1661.63 | **LOC:** 115 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 16.634; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.7%), Connectivity (formerly Api Exposure) (45.3%), Complexity Load (formerly Cognitive Load) (23.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 26`, `args: 6`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.634
  * `Choke Point (Betweenness):` 0.001527 | `Ripple Effect (Closeness):` 0.134516
  * `Imports (Out-Degree: 4):` component, vnode, apiSetup, debug
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/compiler-sfc/src/compileScript.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.937)
- **Top Global Matches:** file_cluster_6: 8.937, file_cluster_4: 10.303, file_cluster_12: 16.035
- **Magnitude:** 1574.66 | **LOC:** 1917 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 2.787; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Complexity Load (formerly Cognitive Load) (65.8%), Guard Balance (formerly Safety Score) (63.7%), Connectivity (formerly Api Exposure) (37.1%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileScript` **(Many-Argument Workhorses)** (Impact: 533.4)
    * *Intent:* /** * Compile `<script setup>` * It requires the whole SFC descriptor because we need to handle and ...
  * `inferRuntimeType` **(Compute Cores)** (Impact: 80.5)
  * `walkDeclaration` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `analyzeBindingsFromOptions` **(Compute Cores)** (Impact: 40.5)
  * `walkPattern` **(Many-Argument Workhorses)** (Impact: 39.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 96 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 317`, `args: 66`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 104`, `dead_code: 14`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 9`, `doc: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.787
  * `Choke Point (Betweenness):` 0.005817 | `Ripple Effect (Closeness):` 0.016783
  * `Imports (Out-Degree: 14):` $node.source.value, babelUtils, cssVars, parseComponent, rewriteDefault, types, warn, parser...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/core/vdom/patch.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.222)
- **Top Global Matches:** file_cluster_6: 6.222, file_cluster_8: 11.838, file_cluster_4: 13.359
- **Magnitude:** 1305.9 | **LOC:** 908 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 2.0; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPatchFunction` **(Compute Cores)** (Impact: 378.7)
  * `patchVnode` **(Many-Argument Workhorses)** (Impact: 104.3)
  * `hydrate` **(Many-Argument Workhorses)** (Impact: 92.5)
    * *Intent:* // Note: this is a browser-only function so we can assume elms are DOM nodes.
  * `updateChildren` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `patch` **(Many-Argument Workhorses)** (Impact: 65.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 46`, `args: 31`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 88`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.0
  * `Choke Point (Betweenness):` 0.001888 | `Ripple Effect (Closeness):` 0.019798
  * `Imports (Out-Degree: 9):` config, lifecycle, traverse, index, template-ref, vnode, constants, element
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/compiler/parser/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.299)
- **Top Global Matches:** file_cluster_2: 4.299, file_cluster_17: 5.679, file_cluster_12: 5.973
- **Magnitude:** 1119.08 | **LOC:** 1000 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 2.75; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Connectivity (formerly Api Exposure) (64.1%), Guard Balance (formerly Safety Score) (57.3%), Debt Markers (formerly Tech Debt) (15.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 68`, `args: 40`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 123`, `dead_code: 1`, `fragile_debt: 5`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.75
  * `Choke Point (Betweenness):` 0.000667 | `Ripple Effect (Closeness):` 0.026997
  * `Imports (Out-Degree: 8):` model, helpers, filter-parser, html-parser, text-parser, env, he, util...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `test/unit/features/v3/apiWatch.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.197)
- **Top Global Matches:** file_cluster_10: 7.197, file_cluster_12: 8.422, file_cluster_11: 9.099
- **Magnitude:** 761.36 | **LOC:** 1235 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.834; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (49.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Callbacks & Closures)** (Impact: 2.8)
  * `setup` **(Callbacks & Closures)** (Impact: 2.6)
  * `render` **(Interface Declarations)** (Impact: 2.1)
  * `render` **(Interface Declarations)** (Impact: 2.1)
  * `setup` **(Callbacks & Closures)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 88 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 546
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 232`, `args: 170`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 108`, `duplicate_logic: 7`
* *Architecture:* `concurrency: 106`, `import: 5`
* *Defense:* `safety: 5`, `test: 182`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` observer, util, component, v3, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/codegen/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.177)
- **Top Global Matches:** file_cluster_4: 6.177, file_cluster_6: 8.586, file_cluster_9: 12.475
- **Magnitude:** 657.72 | **LOC:** 669 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 1.448; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.4%), Guard Balance (formerly Safety Score) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genElement` **(Compute Cores)** (Impact: 63.2)
  * `genData` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `genScopedSlots` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `genChildren` **(Many-Argument Workhorses)** (Impact: 35.9)
  * `genFor` **(Many-Argument Workhorses)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 111`, `args: 40`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 69`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 11`, `import: 7`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.448
  * `Choke Point (Betweenness):` 0.000769 | `Ripple Effect (Closeness):` 0.008418
  * `Imports (Out-Degree: 6):` index, helpers, index, events, types, util, compiler
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/core/instance/lifecycle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.039)
- **Top Global Matches:** file_cluster_6: 6.039, file_cluster_4: 11.59, file_cluster_8: 14.076
- **Magnitude:** 444.14 | **LOC:** 422 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **14**; blast radius 2.334; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.9%), Guard Balance (formerly Safety Score) (73.4%), Connectivity (formerly Api Exposure) (66.3%)
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
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `import: 14`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.334
  * `Choke Point (Betweenness):` 0.003322 | `Ripple Effect (Closeness):` 0.099142
  * `Imports (Out-Degree: 16):` config, dep, index, watcher, index, perf, vnode, events...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/core/util/options.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.965)
- **Top Global Matches:** file_cluster_5: 7.965, file_cluster_7: 9.475, file_cluster_12: 9.517
- **Magnitude:** 409.28 | **LOC:** 490 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **9**; blast radius 4.59; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%), Connectivity (formerly Api Exposure) (62.0%)
- **Documentation Coverage:** 42.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `watch` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* /** * Watchers. * * Watchers hashes should not overwrite one * another, so we merge them as arrays. ...
  * `mergeOptions` **(Many-Argument Workhorses)** (Impact: 26.4)
    * *Intent:* /** * Merge two option objects into a new one. * Core utility used in both instantiation and inherit...
  * `mergeDataOrFn` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* /** * Data */
  * `normalizeProps` **(Compute Cores)** (Impact: 25.8)
    * *Intent:* /** * Ensure all props option syntax are normalized into the * Object-based format. */
  * `resolveAsset` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* /** * Resolve an asset. * This function is used because child instances need access * to assets defi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 63`, `args: 25`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 38`
* *Architecture:* `api: 12`, `import: 10`
* *Defense:* `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.59
  * `Choke Point (Betweenness):` 0.001852 | `Ripple Effect (Closeness):` 0.122555
  * `Imports (Out-Degree: 9):` config, index, debug, env, lang, constants, util, component...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/server-renderer/src/render.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.1)
- **Top Global Matches:** file_cluster_6: 7.1, file_cluster_4: 9.935, file_cluster_12: 16.369
- **Magnitude:** 383.54 | **LOC:** 460 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 1.156; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.3%), Complexity Load (formerly Cognitive Load) (60.2%), Concurrency Surface (formerly Concurrency) (56.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderComponent` **(Many-Argument Workhorses)** (Impact: 43.1)
  * `renderAsyncComponent` **(Many-Argument Workhorses)** (Impact: 37.2)
  * `renderStartingTag` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `renderNode` **(Compute Cores)** (Impact: 25.1)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 43`, `args: 26`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 38`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.156
  * `Choke Point (Betweenness):` 0.000896 | `Ripple Effect (Closeness):` 0.004545
  * `Imports (Out-Degree: 12):` compiler, runtime-helpers, render-context, util, debug, options, create-component, vnode...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/compiler-sfc/src/babelUtils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.831)
- **Top Global Matches:** file_cluster_6: 8.831, file_cluster_8: 9.623, file_cluster_4: 16.792
- **Magnitude:** 376.14 | **LOC:** 424 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 1.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%), Connectivity (formerly Api Exposure) (50.1%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isReferenced` **(Many-Argument Workhorses)** (Impact: 104.4)
    * *Intent:* /** * Copied from https://github.com/babel/babel/blob/main/packages/babel-types/src/validators/isRef...
  * `walkIdentifiers` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `enter` **(Compute Cores)** (Impact: 36.5)
    * *Intent:* ;(walk as any)(root, {
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015194
  * `Imports (Out-Degree: 0):` types, estree-walker
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/compiler/parser/html-parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.446)
- **Top Global Matches:** file_cluster_3: 11.446, file_cluster_8: 13.925, file_cluster_6: 26.389
- **Magnitude:** 367.26 | **LOC:** 342 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 2.053; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.6%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseHTML` **(Many-Argument Workhorses)** (Impact: 160.8)
  * `parseEndTag` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `handleStartTag` **(Compute Cores)** (Impact: 26.5)
  * `parseStartTag` **(I/O & Config Routines)** (Impact: 7.3)
  * `shouldIgnoreFirstNewline` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 30`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 35`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.053
  * `Choke Point (Betweenness):` 0.000218 | `Ripple Effect (Closeness):` 0.025411
  * `Imports (Out-Degree: 4):` lang, util, compiler, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/core/observer/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.573)
- **Top Global Matches:** file_cluster_8: 10.573, file_cluster_6: 19.0, file_cluster_3: 21.594
- **Magnitude:** 365.0 | **LOC:** 340 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **5**; blast radius 7.693; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Connectivity (formerly Api Exposure) (81.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.693
  * `Choke Point (Betweenness):` 0.008696 | `Ripple Effect (Closeness):` 0.124737
  * `Imports (Out-Degree: 9):` v3, index, vnode, array, dep
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/compiler/helpers.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.664)
- **Top Global Matches:** file_cluster_4: 7.664, file_cluster_12: 11.0, file_cluster_9: 11.776
- **Magnitude:** 324.36 | **LOC:** 244 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **3**; blast radius 3.936; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addHandler` **(Many-Argument Workhorses)** (Impact: 106.0)
  * `addDirective` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `addAttr` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `getBindingAttr` **(Compute Cores)** (Impact: 14.8)
  * `getAndRemoveAttr` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* // note: this only removes the attr from the Array (attrsList) so that it // doesn't get processed b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 27`, `args: 15`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 30`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.936
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.036167
  * `Imports (Out-Degree: 3):` filter-parser, util, compiler
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `packages/server-renderer/test/ssr-string.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.295)
- **Top Global Matches:** file_cluster_10: 6.295, file_cluster_11: 7.877, file_cluster_15: 8.03
- **Magnitude:** 323.04 | **LOC:** 2167 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.834; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.7%), Guard Balance (formerly Safety Score) (48.3%), Complexity Load (formerly Cognitive Load) (8.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nestedPrefetch` **(Callbacks & Closures)** (Impact: 2.4)
  * `testAsync` **(Callbacks & Closures)** (Impact: 2.2)
  * `Foo` **(Callbacks & Closures)** (Impact: 2.2)
  * `Bar` **(Callbacks & Closures)** (Impact: 2.2)
  * `testAsync` **(Callbacks & Closures)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 133
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 361`, `args: 280`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `duplicate_logic: 20`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `concurrency: 58`, `import: 4`
* *Defense:* `safety: 4`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utils, index, vm, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/v3/apiWatch.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.678)
- **Top Global Matches:** file_cluster_5: 8.678, file_cluster_12: 10.401, file_cluster_7: 11.857
- **Magnitude:** 317.66 | **LOC:** 354 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 1.324; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Complexity Load (formerly Cognitive Load) (69.9%), Guard Balance (formerly Safety Score) (64.1%), Connectivity (formerly Api Exposure) (53.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doWatch` **(Many-Argument Workhorses)** (Impact: 140.0)
  * `run` **(I/O & Config Routines)** (Impact: 11.7)
    * *Intent:* // overwrite default run
  * `watch` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* // implementation
  * `getter` **(Callbacks & Closures)** (Impact: 8.7)
  * `call` **(Callbacks & Closures)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 102`, `args: 34`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 24`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.324
  * `Choke Point (Betweenness):` 0.000322 | `Ripple Effect (Closeness):` 0.085094
  * `Imports (Out-Degree: 13):` scheduler, watcher, currentInstance, debug, computed, reactive, ref, traverse...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/core/instance/state.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.011)
- **Top Global Matches:** file_cluster_12: 8.011, file_cluster_4: 9.477, file_cluster_7: 10.14
- **Magnitude:** 298.08 | **LOC:** 394 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 1.141; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.7%), Complexity Load (formerly Cognitive Load) (58.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initComputed` **(Defensive Guards)** (Impact: 31.5)
  * `initData` **(Compute Cores)** (Impact: 23.2)
  * `initProps` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `defineComputed` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `initMethods` **(Compute Cores)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 34`, `args: 25`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 29`
* *Architecture:* `io: 1`, `api: 8`, `import: 9`
* *Defense:* `safety: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.000248 | `Ripple Effect (Closeness):` 0.069367
  * `Imports (Out-Degree: 15):` config, dep, index, watcher, index, lifecycle, component, v3...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/compiler/error-detector.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.348)
- **Top Global Matches:** file_cluster_12: 5.348, file_cluster_7: 5.856, file_cluster_5: 7.702
- **Magnitude:** 274.85 | **LOC:** 159 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.072; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.5%), Connectivity (formerly Api Exposure) (24.6%), Concurrency Surface (formerly Concurrency) (17.9%), Mutation Surface (formerly State Flux) (10.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 22`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 1`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.072
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.003636
  * `Imports (Out-Degree: 2):` index, compiler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/compiler-sfc/test/rewriteDefault.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.981)
- **Top Global Matches:** file_cluster_10: 4.981, file_cluster_13: 5.575, file_cluster_2: 6.956
- **Magnitude:** 259.64 | **LOC:** 312 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.834; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (91.9%), Guard Balance (formerly Safety Score) (43.1%), Connectivity (formerly Api Exposure) (13.7%), Dead Code Surface (formerly Dead Code) (8.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 127`, `args: 24`, `func_start: 18`, `class_start: 10`
* *Risk/State:* `state_mutation: 4`, `dead_code: 2`
* *Architecture:* `api: 58`, `concurrency: 12`, `import: 20`
* *Defense:* `safety: 2`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..., src, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benchmarks/dbmon/ENV.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.781)
- **Top Global Matches:** file_cluster_15: 6.781, file_cluster_10: 7.172, file_cluster_16: 7.699
- **Magnitude:** 257.64 | **LOC:** 212 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.976; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
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
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 59`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.976
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00202
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/shared/util.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 9.924)
- **Top Global Matches:** file_cluster_14: 9.924, file_cluster_5: 10.186, file_cluster_7: 10.556
- **Magnitude:** 250.94 | **LOC:** 379 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **93** in-repo importer(s); blast radius 50.01; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.256896
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 93):` (Excluded from Brief to save tokens)

### `src/platforms/web/runtime/modules/transition.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.5)
- **Top Global Matches:** file_cluster_8: 9.5, file_cluster_6: 10.928, file_cluster_4: 18.766
- **Magnitude:** 240.2 | **LOC:** 342 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 1.436; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (65.8%), Guard Balance (formerly Safety Score) (57.4%), Connectivity (formerly Api Exposure) (36.4%), Complexity Load (formerly Cognitive Load) (31.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.436
  * `Choke Point (Betweenness):` 0.000777 | `Ripple Effect (Closeness):` 0.013468
  * `Imports (Out-Degree: 8):` lifecycle, index, index, vnode, util, vnode, transition-util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/compiler-sfc/src/parseComponent.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.572)
- **Top Global Matches:** file_cluster_6: 7.572, file_cluster_4: 10.01, file_cluster_9: 16.362
- **Magnitude:** 233.18 | **LOC:** 221 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 4.451; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (58.2%), Connectivity (formerly Api Exposure) (54.5%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseComponent` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* /** * Parse a single-file component (*.vue) file into an SFC Descriptor Object. */
  * `start` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `end` **(Compute Cores)** (Impact: 20.3)
  * `checkAttrs` **(Compute Cores)** (Impact: 11.1)
  * `padContent` **(Compute Cores)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 38`, `args: 9`, `func_start: 7`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.451
  * `Choke Point (Betweenness):` 0.003054 | `Ripple Effect (Closeness):` 0.021818
  * `Imports (Out-Degree: 5):` compileScript, types, html-parser, de-indent, util, compiler
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/core/util/props.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.867)
- **Top Global Matches:** file_cluster_4: 7.867, file_cluster_6: 10.887, file_cluster_12: 11.48
- **Magnitude:** 213.26 | **LOC:** 255 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 3.597; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.3%), Complexity Load (formerly Cognitive Load) (48.2%), Connectivity (formerly Api Exposure) (15.2%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertProp` **(Many-Argument Workhorses)** (Impact: 43.8)
    * *Intent:* /** * Assert whether a prop is valid. */
  * `validateProp` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `getPropDefaultValue` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* /** * Get the default value of a prop. */
  * `assertType` **(Defensive Guards)** (Impact: 21.7)
  * `getInvalidTypeMessage` **(Many-Argument Workhorses)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 58`, `args: 15`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 17`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.597
  * `Choke Point (Betweenness):` 0.000635 | `Ripple Effect (Closeness):` 0.120448
  * `Imports (Out-Degree: 4):` index, debug, util, component
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `test/unit/features/v3/setupTemplateRef.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.76)
- **Top Global Matches:** file_cluster_12: 7.76, file_cluster_7: 9.071, file_cluster_10: 9.833
- **Magnitude:** 210.88 | **LOC:** 502 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.834; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (49.0%), Complexity Load (formerly Cognitive Load) (48.0%), Dead Code Surface (formerly Dead Code) (6.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Compute Cores)** (Impact: 4.5)
  * `render` **(Compute Cores)** (Impact: 3.2)
  * `render` **(Compute Cores)** (Impact: 3.0)
  * `render` **(Compute Cores)** (Impact: 3.0)
  * `render` **(Compute Cores)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 120
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 75`, `args: 62`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 16`, `dead_code: 2`, `duplicate_logic: 7`
* *Architecture:* `concurrency: 30`, `import: 2`
* *Defense:* `test: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` index, vue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/observer/watcher.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.049)
- **Top Global Matches:** file_cluster_4: 8.049, file_cluster_6: 9.492, file_cluster_12: 12.83
- **Magnitude:** 205.0 | **LOC:** 279 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **7**; blast radius 11.108; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.5%), Connectivity (formerly Api Exposure) (57.0%), Complexity Load (formerly Cognitive Load) (40.5%)
- **Documentation Coverage:** 11.7647% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `run` **(I/O & Config Routines)** (Impact: 8.4)
    * *Intent:* /** * Scheduler job interface. * Will be called by the scheduler. */
  * `teardown` **(I/O & Config Routines)** (Impact: 6.8)
    * *Intent:* /** * Remove self from all dependencies' subscriber list. */
  * `update` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* /** * Subscriber interface. * Will be called when a dependency changes. */
  * `get` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* /** * Evaluate the getter, and re-collect dependencies. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 22`, `args: 11`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 42`
* *Architecture:* `io: 1`, `api: 8`, `import: 8`
* *Defense:* `safety: 3`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.108
  * `Choke Point (Betweenness):` 0.007433 | `Ripple Effect (Closeness):` 0.120621
  * `Imports (Out-Degree: 10):` index, dep, scheduler, traverse, component, debug, effectScope
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/types/ssr.ts` (TYPESCRIPT) | Magnitude: 19.46 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, api: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/unit/features/options/comments.spec.ts` (TYPESCRIPT) | Magnitude: 9.56 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 8, structural_boundaries: 4, args: 3
- `test/unit/modules/compiler/compiler-options.spec.ts` (TYPESCRIPT) | Magnitude: 68.34 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 152, test: 29, structural_boundaries: 21, core_var_decl: 19
- `test/e2e/commits.spec.ts` (TYPESCRIPT) | Magnitude: 30.16 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 27, concurrency: 23, test: 17
- `test/unit/features/template-ref.spec.ts` (TYPESCRIPT) | Magnitude: 26.78 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 231, test: 40, structural_boundaries: 27, args: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/platforms/web/runtime/modules/events.ts` (TYPESCRIPT) | Magnitude: 83.82 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, branch: 23, listeners: 19, structural_boundaries: 13
- `src/v3/index.ts` (TYPESCRIPT) | Magnitude: 23.1 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 21, api: 20, import: 18
- `types/test/v3/define-component-test.tsx` (TYPESCRIPT) | Magnitude: 145.86 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 867, structural_boundaries: 141, args: 119, ui_framework: 113
- `test/unit/modules/observer/scheduler.spec.ts` (TYPESCRIPT) | Magnitude: 32.64 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 165, args: 31, structural_boundaries: 20, test: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/server-renderer/test/fixtures/cache-opt-out.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, args: 4, func_start: 3
- `src/core/observer/scheduler.ts` (TYPESCRIPT) | Magnitude: 132.02 | Delta: **0.161** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 94, branch: 35, core_var_decl: 25, state_mutation: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/compiler-sfc/src/index.ts` (TYPESCRIPT) | Magnitude: 29.44 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 14, api: 14, import: 14, indent_spaces: 6
- `src/core/util/index.ts` (TYPESCRIPT) | Magnitude: 23.68 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/core/vdom/helpers/index.ts` (TYPESCRIPT) | Magnitude: 22.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7, concurrency: 2
- `test/unit/modules/vdom/modules/directive.spec.ts` (TYPESCRIPT) | Magnitude: 16.16 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 6, test: 5, core_var_decl: 5
- `src/platforms/web/compiler/directives/html.ts` (TYPESCRIPT) | Magnitude: 4.84 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, branch: 2, import: 2
- `src/platforms/web/compiler/directives/text.ts` (TYPESCRIPT) | Magnitude: 4.84 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, branch: 2, import: 2
- `src/platforms/web/runtime/modules/index.ts` (TYPESCRIPT) | Magnitude: 14.64 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 8, import: 6, branch: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/server-renderer/src/optimizing-compiler/optimizer.ts` (TYPESCRIPT) | Magnitude: 117.04 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 94, branch: 32, structural_boundaries: 21, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/types/vnode.ts` (TYPESCRIPT) | Magnitude: 23.62 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 64, branch: 37, structural_boundaries: 23, safety_bypasses: 10
- `src/core/global-api/index.ts` (TYPESCRIPT) | Magnitude: 28.24 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 20, import: 11, state_mutation: 10
- `src/core/instance/render-helpers/resolve-scoped-slots.ts` (TYPESCRIPT) | Magnitude: 39.4 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 20, branch: 10, structural_boundaries: 5, state_mutation: 4
- `types/test/v3/reactivity-test.ts` (TYPESCRIPT) | Magnitude: 44.7 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 223, generics: 60, bitwise_ops: 42, core_var_decl: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/unit/features/options/props.spec.ts` (TYPESCRIPT) | Magnitude: 42.96 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 557, test: 130, structural_boundaries: 95, args: 76
- `src/core/vdom/helpers/merge-hook.ts` (TYPESCRIPT) | Magnitude: 41.7 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 24, branch: 7, state_mutation: 7, core_var_decl: 5
- `test/helpers/shim-done.ts` (TYPESCRIPT) | Magnitude: 33.42 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, closures: 6, branch: 5
- `src/core/util/env.ts` (TYPESCRIPT) | Magnitude: 55.76 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 27, branch: 24, core_var_decl: 22

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/core/vdom/create-component.ts` -> **Severity: 2.01** (Bridge: 0.0201 * Flux: 99.8515%)
- `src/core/util/debug.ts` -> **Severity: 1.981** (Bridge: 0.0198 * Flux: 100.0%)
- `src/core/vdom/create-functional-component.ts` -> **Severity: 0.938** (Bridge: 0.0094 * Flux: 100.0%)
- `src/core/observer/index.ts` -> **Severity: 0.864** (Bridge: 0.0087 * Flux: 99.3427%)
- `src/core/instance/render-helpers/index.ts` -> **Severity: 0.747** (Bridge: 0.0075 * Flux: 99.9986%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/shared/util.ts` -> **Severity: 20.552** (Embedded: 0.2569 * Error Risk: 80.0%)
- `src/types/component.ts` -> **Severity: 12.642** (Embedded: 0.158 * Error Risk: 80.0%)
- `src/core/vdom/vnode.ts` -> **Severity: 12.32** (Embedded: 0.1626 * Error Risk: 75.7587%)
- `src/types/vnode.ts` -> **Severity: 11.82** (Embedded: 0.1478 * Error Risk: 80.0%)
- `src/core/util/error.ts` -> **Severity: 10.676** (Embedded: 0.1334 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/types/component.ts` -> **Severity: 4319.0** (Blast Radius: 43.19 * Doc Risk: 100.0%)
- `benchmarks/ssr/common.js` -> **Severity: 3955.414** (Blast Radius: 48.225 * Doc Risk: 82.02%)
- `src/core/vdom/vnode.ts` -> **Severity: 3214.4** (Blast Radius: 32.144 * Doc Risk: 100.0%)
- `src/core/config.ts` -> **Severity: 1576.6** (Blast Radius: 15.766 * Doc Risk: 100.0%)
- `src/core/util/env.ts` -> **Severity: 1285.6** (Blast Radius: 12.856 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 102 literal sites + 14 sites through wrappers = 116

- `step` (function, debug_prints, primitive): 9 call sites in 1 files -- `scripts/release.js`
- `warn` (function, debug_prints, primitive): 3 call sites in 1 files -- `packages/server-renderer/src/webpack-plugin/util.ts`
- `tip` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/server-renderer/src/webpack-plugin/util.ts`
- `warn` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/compiler-sfc/src/warn.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4662 call pairs -- scoped 31.2%, unique 0.1%, ambiguous 13.6%, external 55.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 4286 | 33.1% | 0.0% | 14.3% | 52.6% |
| javascript | 213 | 12.2% | 0.0% | 9.4% | 78.4% |
| html | 159 | 6.3% | 1.9% | 0.0% | 91.8% |
| shell | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
