# ARCHITECTURAL_BRIEF: next.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/vercel/next.js.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 24098 analyzed artifact(s), 1555168 LOC.
- **Load-bearing artifact:** `packages/next/link.js` -- 1142 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `turbopack/crates/turbopack-ecmascript/src/references/mod.rs` -- pulls in 216 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` at magnitude 23433.32 (structural weight, not risk).
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
| Total Artifacts | 28408 |
| Analyzed Artifacts (Scanned) | 24098 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4310 |
| Total LOC | 1555168 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 84.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.827 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2602 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 7.7095 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 827 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 9885 | 514334 | 41.0% |
| JAVASCRIPT | 9881 | 777379 | 41.0% |
| RUST | 960 | 220068 | 4.0% |
| PLAINTEXT | 878 | 35 | 3.6% |
| CSS | 841 | 27761 | 3.5% |
| MARKDOWN | 690 | 0 | 2.9% |
| JSON | 633 | 12504 | 2.6% |
| XML | 248 | 66 | 1.0% |
| YAML | 31 | 1702 | 0.1% |
| SHELL | 24 | 748 | 0.1% |
| HTML | 13 | 137 | 0.1% |
| DOCKERFILE | 9 | 303 | 0.0% |
| MAKEFILE | 1 | 27 | 0.0% |
| SQLITE | 1 | 14 | 0.0% |
| BATCH | 1 | 5 | 0.0% |
| PYTHON | 1 | 84 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.56`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.56; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 45%, Declarative / Non-Code 11%, Parameter Forwarders Files 7%, Callbacks & Closures Files 7%, Interface Declarations Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 22482 | 93.3% |
| Unknown | 35 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1533 | 6.4% |
| Static: Minified & Vendor Opaque Mass | 48 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4310*

**Composition by Extension & Reason:**
- `.js`: 458x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 117x Excluded (Saturation: Line 1 exceeds 500 chars), 23x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 532x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 29x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.mdx`: 422x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 9 exceeds 500 chars), 3x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.ts`: 291x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 4x Excluded (Machine-Generated Source Code Signature: 9 LOC)
- `.snapshot`: 285x Excluded (Unsupported Extension: '.snapshot')
- `.png`: 277x Excluded (Explicitly Denied Extension: '.png')
- `.map`: 216x Unresolved Ambiguity (No Retainable Structure), 32x Excluded (Saturation: Line 5 exceeds 500 chars), 10x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.json`: 262x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1294 LOC), 1x Excluded (Static Asset Blob without Intent: 1026 LOC)
- `.ico`: 157x Excluded (Explicitly Denied Extension: '.ico')
- `.tsx`: 23x Excluded (Machine-Generated Source Code Signature: 17 LOC), 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 21x Excluded (Machine-Generated Source Code Signature: 19 LOC)
- `.stderr`: 102x Excluded (Unsupported Extension: '.stderr')
- `.jpg`: 84x Excluded (Explicitly Denied Extension: '.jpg')
- `.example`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 69x Unsupported Format (.toml), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `.yml`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.6 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.1 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.0 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 99.0 | 2.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 13702 | 1770 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` |
| cleanup | 2473 | 586 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` |
| guards | 113050 | 4224 | 2 | `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` |
| danger | 37668 | 3378 | 1 | `packages/next/src/compiled/@vercel/og/index.node.js` |
| concurrency | 86204 | 6780 | 6 | `test/integration/file-serving/test/index.test.ts` |
| connectivity | 46137 | 17670 | 3 | `packages/next/src/compiled/@vercel/og/index.edge.js` |
| io | 17792 | 3033 | 1 | `test/e2e/app-dir/cache-components-errors/cache-components-errors.test.ts` |
| crypto | 55 | 35 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/load.js` |
| ipc | 369 | 196 | 0 | `turbopack/crates/turbopack-tests/tests/execution/turbopack/basic/worker-threads/input/index.js` |
| time | 2625 | 1163 | 0 | `test/e2e/app-dir/cache-components-errors/cache-components-errors.test.ts` |
| serialization | 3547 | 1258 | 0 | `test/integration/i18n-support/test/shared.ts` |
| regex | 3320 | 905 | 0 | `packages/next/src/compiled/@vercel/og/index.node.js` |
| events | 7683 | 1246 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/load.js` |
| tests | 42517 | 2414 | 1 | `test/integration/file-serving/test/index.test.ts` |
| docs | 16515 | 2319 | 0 | `turbopack/crates/turbo-tasks-macros/src/derive/task_storage_macro.rs` |
| debt | 10960 | 2493 | 1 | `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` |
| mutation | 303456 | 14635 | 12 | `packages/next/src/compiled/@vercel/og/index.node.js` |
| dead_code | 9057 | 4947 | 1 | `test/e2e/app-dir/monaco-editor/components/editor/monaco.ts` |
| credential | 144 | 71 | 0 | `packages/font/src/google/loader.test.ts` |
| threat | 8414 | 677 | 0 | `packages/next/src/compiled/@vercel/og/index.node.js` |
| ml_ai | 2389 | 455 | 0 | `test/e2e/app-dir/cache-components-errors/cache-components-errors.test.ts` |
| ui | 27819 | 6074 | 2 | `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/e2e/app-dir/cache-components-errors/cache-components-errors.test.ts` (Hits: 573)
- `test/e2e/app-dir/app-static/app-static.test.ts` (Hits: 395)
- `test/unit/image-optimizer/match-remote-pattern.test.ts` (Hits: 323)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **link.js** (`packages/next/link.js`) — 1142 inbound connections
2. **next-test-utils.ts** (`test/lib/next-test-utils.ts`) — 898 inbound connections
3. **server.js** (`packages/next/server.js`) — 686 inbound connections
4. **navigation.js** (`packages/next/navigation.js`) — 406 inbound connections
5. **headers.js** (`packages/next/headers.js`) — 405 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`turbopack/crates/turbopack-ecmascript/src/references/mod.rs`) — 216 outbound dependencies
2. **lib.rs** (`turbopack/crates/turbopack-ecmascript/src/lib.rs`) — 149 outbound dependencies
3. **app.rs** (`crates/next-api/src/app.rs`) — 139 outbound dependencies
4. **project.rs** (`crates/next-api/src/project.rs`) — 139 outbound dependencies
5. **mod.rs** (`turbopack/crates/turbo-tasks-backend/src/backend/mod.rs`) — 133 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `exports` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/@vercel/og/index.node.js`) -> Impact: **4884.2** | LOC: 13091
- `exports` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/@vercel/og/index.edge.js`) -> Impact: **4188.0** | LOC: 12087
- `Md` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/@vercel/og/index.edge.js`) -> Impact: **1748.6** | LOC: 1031
- `_l` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/@vercel/og/index.node.js`) -> Impact: **1748.6** | LOC: 1031
- `pushStartInstance` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.production.js`) -> Impact: **1287.5** | LOC: 1084
- `pushStartInstance` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.production.js`) -> Impact: **1287.5** | LOC: 1084
- `pushStartInstance` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.production.js`) -> Impact: **1286.7** | LOC: 1068
- `pushStartInstance` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.production.js`) -> Impact: **1286.7** | LOC: 1068
- `pushStartInstance` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.node.production.js`) -> Impact: **1286.5** | LOC: 1065
- `pushStartInstance` **(Many-Argument Workhorses)** (@ `packages/next/src/compiled/react-dom/cjs/react-dom-server-legacy.node.production.js`) -> Impact: **1286.5** | LOC: 1065

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/next/src/compiled/react-dom-experimental/cjs` | 18 | 140473.58 | 82.83% | 14.12% |
| `packages/next/src/compiled/react-dom/cjs` | 17 | 115994.12 | 82.9% | 14.67% |
| `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs` | 14 | 58206.26 | 95.13% | 14.15% |
| `packages/next/src/compiled/react-server-dom-webpack/cjs` | 14 | 57850.6 | 95.12% | 14.23% |
| `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs` | 12 | 57589.66 | 99.7% | 15.57% |
| `packages/next/src/compiled/react-server-dom-turbopack/cjs` | 12 | 57234.0 | 99.69% | 15.66% |
| `packages/next/src/compiled/@vercel/og` | 6 | 44789.5 | 35.5% | 21.53% |
| `test/development/acceptance-app` | 19 | 41580.4 | 25.42% | 0.0% |
| `test/development/acceptance` | 11 | 29659.18 | 20.93% | 0.0% |
| `turbopack/crates/turbopack-ecmascript/tests/benches` | 1 | 23433.32 | 92.98% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/next/src/compiled/@edge-runtime/cookies/index.d.ts` -> **100.0%** Exposure
- `packages/next/src/experimental/testing/server/config-testing-utils.test.ts` -> **100.0%** Exposure
- `packages/next/src/next-devtools/dev-overlay.shim.ts` -> **100.0%** Exposure
- `turbopack/crates/turbo-bincode/src/serde_self_describing/ser.rs` -> **100.0%** Exposure
- `turbopack/crates/turbo-tasks/src/task/task_input.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `apps/bundle-analyzer/components/import-chain.tsx` -> **100.0%** Exposure
- `apps/bundle-analyzer/components/treemap-visualizer.tsx` -> **100.0%** Exposure
- `examples/cms-payload/components/RichText/serialize.tsx` -> **100.0%** Exposure
- `examples/cms-sitecore-xmcloud/src/components/Container.tsx` -> **100.0%** Exposure
- `examples/cms-sitecore-xmcloud/src/components/Navigation.tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/next/src/compiled/@vercel/og/index.edge.js` -> **82** Orphaned Functions | **3** Duplicates
- `packages/next/src/compiled/@vercel/og/index.node.js` -> **80** Orphaned Functions | **3** Duplicates
- `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` -> **20** Orphaned Functions | **63** Duplicates
- `crates/next-core/src/next_config.rs` -> **40** Orphaned Functions | **6** Duplicates
- `turbopack/crates/turbo-bincode/src/serde_self_describing/ser.rs` -> **33** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `examples/with-supertokens/app/config/backend.ts` -> **99.999%** Exposure
- `examples/with-algolia-react-instantsearch/components/Search.tsx` -> **99.7922%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `33` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `37697` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 23433.32 | **LOC:** 25669 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.319; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (93.0%), Guard Balance (formerly Safety Score) (55.8%), Concurrency Surface (formerly Concurrency) (20.6%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setProp` **(Many-Argument Workhorses)** (Impact: 559.7)
  * `diffHydratedProperties` **(Many-Argument Workhorses)** (Impact: 504.0)
  * `updateClassComponent` **(Many-Argument Workhorses)** (Impact: 497.8)
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 487.9)
  * `completeWork` **(Many-Argument Workhorses)** (Impact: 484.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 24 instances
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 2012 instances
* *High Risk Execution (weighted view):* 11
* *Concurrency (weighted view):* 209
* *State Mutation (weighted view):* 6961
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6686`, `structural_boundaries: 2764`, `args: 1015`, `func_start: 938`
* *Risk/State:* `safety_bypasses: 414`, `high_risk_execution: 35`, `state_mutation: 2937`, `planned_debt: 1`, `fragile_debt: 87`, `duplicate_logic: 63`, `unreferenced_by_name: 20`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 64`, `import: 4`
* *Defense:* `safety: 3654`, `doc: 1`, `immutability_locks: 7`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.319
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006613
  * `Imports (Out-Degree: 0):` react, react-dom, scheduler
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/next/src/compiled/@vercel/og/index.node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 23042.14 | **LOC:** 21548 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.9718% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Many-Argument Workhorses)** (Impact: 4884.2)
  * `_l` **(Many-Argument Workhorses)** (Impact: 1748.6)
  * `ci` **(Defensive Guards)** (Impact: 266.4)
  * `tr` **(Defensive Guards)** (Impact: 152.8)
  * `exports` **(Defensive Guards)** (Impact: 150.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 2970 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 409
* *State Mutation (weighted view):* 9517
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6054`, `structural_boundaries: 7562`, `args: 2233`, `func_start: 1572`
* *Risk/State:* `safety_bypasses: 1036`, `high_risk_execution: 2`, `state_mutation: 3577`, `planned_debt: 22`, `duplicate_logic: 3`, `unreferenced_by_name: 80`
* *Architecture:* `io: 23`, `api: 1282`, `concurrency: 149`, `import: 4`
* *Defense:* `safety: 1926`, `doc: 35`, `test: 41`, `immutability_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fs, sharp, stream, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/@vercel/og/index.edge.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 21744.84 | **LOC:** 20508 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.8841% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Many-Argument Workhorses)** (Impact: 4188.0)
  * `Md` **(Many-Argument Workhorses)** (Impact: 1748.6)
  * `Ji` **(Defensive Guards)** (Impact: 266.4)
  * `zr` **(Defensive Guards)** (Impact: 152.8)
  * `exports` **(Defensive Guards)** (Impact: 150.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 52 instances
* *Amplified Cascading Flux:* 2798 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 385
* *State Mutation (weighted view):* 8979
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5674`, `structural_boundaries: 7181`, `args: 2027`, `func_start: 1470`
* *Risk/State:* `safety_bypasses: 958`, `high_risk_execution: 2`, `state_mutation: 3383`, `planned_debt: 21`, `duplicate_logic: 3`, `unreferenced_by_name: 82`
* *Architecture:* `io: 20`, `api: 1282`, `concurrency: 125`, `import: 2`
* *Defense:* `safety: 1801`, `doc: 35`, `test: 36`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` resvg.wasm?module, yoga.wasm?module
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-profiling.profiling.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 17753.44 | **LOC:** 22321 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%), Guard Balance (formerly Safety Score) (58.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 484.1)
  * `setProp` **(Many-Argument Workhorses)** (Impact: 432.0)
  * `updateProperties` **(Many-Argument Workhorses)** (Impact: 372.6)
  * `commitMutationEffectsOnFiber` **(Many-Argument Workhorses)** (Impact: 350.1)
  * `setInitialProperties` **(Many-Argument Workhorses)** (Impact: 281.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 2252 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 7383
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6330`, `structural_boundaries: 2593`, `args: 834`, `func_start: 789`
* *Risk/State:* `safety_bypasses: 375`, `high_risk_execution: 15`, `state_mutation: 2879`
* *Architecture:* `api: 24`, `concurrency: 57`, `import: 3`
* *Defense:* `safety: 3595`, `doc: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental, scheduler-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-unstable_testing.production.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16496.76 | **LOC:** 20540 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%), Guard Balance (formerly Safety Score) (59.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 484.1)
  * `setProp` **(Many-Argument Workhorses)** (Impact: 432.0)
  * `updateProperties` **(Many-Argument Workhorses)** (Impact: 372.6)
  * `commitMutationEffectsOnFiber` **(Many-Argument Workhorses)** (Impact: 303.2)
  * `setInitialProperties` **(Many-Argument Workhorses)** (Impact: 281.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 2128 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 189
* *State Mutation (weighted view):* 6953
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5859`, `structural_boundaries: 2550`, `args: 801`, `func_start: 748`
* *Risk/State:* `safety_bypasses: 350`, `high_risk_execution: 15`, `state_mutation: 2697`, `unreferenced_by_name: 20`
* *Architecture:* `api: 13`, `concurrency: 54`, `import: 3`
* *Defense:* `safety: 3323`, `doc: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental, scheduler-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-client.production.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15968.74 | **LOC:** 20073 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%), Guard Balance (formerly Safety Score) (59.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 484.1)
  * `setProp` **(Many-Argument Workhorses)** (Impact: 432.0)
  * `updateProperties` **(Many-Argument Workhorses)** (Impact: 372.6)
  * `commitMutationEffectsOnFiber` **(Many-Argument Workhorses)** (Impact: 303.2)
  * `setInitialProperties` **(Many-Argument Workhorses)** (Impact: 281.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 2058 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 189
* *State Mutation (weighted view):* 6729
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5709`, `structural_boundaries: 2471`, `args: 775`, `func_start: 726`
* *Risk/State:* `safety_bypasses: 346`, `high_risk_execution: 15`, `state_mutation: 2613`
* *Architecture:* `api: 12`, `concurrency: 54`, `import: 3`
* *Defense:* `safety: 3263`, `doc: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental, scheduler-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-profiling.profiling.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15724.38 | **LOC:** 20362 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%), Guard Balance (formerly Safety Score) (58.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 465.4)
  * `setProp` **(Many-Argument Workhorses)** (Impact: 418.2)
  * `updateProperties` **(Many-Argument Workhorses)** (Impact: 372.6)
  * `commitMutationEffectsOnFiber` **(Many-Argument Workhorses)** (Impact: 345.9)
  * `commitPassiveMountOnFiber` **(Many-Argument Workhorses)** (Impact: 254.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 12 instances
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 2022 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 158
* *State Mutation (weighted view):* 6623
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5780`, `structural_boundaries: 2397`, `args: 784`, `func_start: 742`
* *Risk/State:* `safety_bypasses: 334`, `high_risk_execution: 15`, `state_mutation: 2579`
* *Architecture:* `api: 24`, `concurrency: 53`, `import: 3`
* *Defense:* `safety: 3250`, `doc: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom, scheduler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-client.production.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 14068.74 | **LOC:** 18267 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%), Guard Balance (formerly Safety Score) (58.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 465.4)
  * `setProp` **(Many-Argument Workhorses)** (Impact: 418.2)
  * `updateProperties` **(Many-Argument Workhorses)** (Impact: 372.6)
  * `commitMutationEffectsOnFiber` **(Many-Argument Workhorses)** (Impact: 299.0)
  * `setInitialProperties` **(Many-Argument Workhorses)** (Impact: 221.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 12 instances
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 1842 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 176
* *State Mutation (weighted view):* 6015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5202`, `structural_boundaries: 2274`, `args: 726`, `func_start: 680`
* *Risk/State:* `safety_bypasses: 305`, `high_risk_execution: 15`, `state_mutation: 2331`
* *Architecture:* `api: 12`, `concurrency: 51`, `import: 3`
* *Defense:* `safety: 2936`, `doc: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom, scheduler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/acceptance-app/ReactRefreshLogBox.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 13257.79 | **LOC:** 1802 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (58.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.8%), Complexity Load (formerly Cognitive Load) (11.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *High Risk Execution (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 451`, `args: 95`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 26`, `state_mutation: 1`, `planned_debt: 10`, `fragile_debt: 4`
* *Architecture:* `io: 34`, `api: 45`, `concurrency: 209`, `import: 21`
* *Defense:* `safety: 9`, `test: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Child, FunctionDefault.js, actions, boom.css, index.module.css, module, styles1.css, styles2.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/acceptance/ReactRefreshLogBox.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 11385.61 | **LOC:** 1505 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (51.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.3%), Complexity Load (formerly Cognitive Load) (10.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 317`, `args: 67`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 1`, `planned_debt: 2`
* *Architecture:* `io: 40`, `api: 37`, `concurrency: 149`, `import: 17`
* *Defense:* `safety: 5`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Child, FunctionDefault.js, index.module.css, development-sandbox, e2e-utils, next-test-utils, outdent, path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10404.44 | **LOC:** 11520 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 99.697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1261.4)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 852.1)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 258.1)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 172.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 1055 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 178
* *State Mutation (weighted view):* 3702
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2836`, `structural_boundaries: 1125`, `args: 363`, `func_start: 313`
* *Risk/State:* `safety_bypasses: 318`, `high_risk_execution: 38`, `state_mutation: 1592`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 43`, `import: 7`
* *Defense:* `safety: 1453`, `doc: 1`, `immutability_locks: 4`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, react-dom-experimental, react-experimental, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.browser.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10397.42 | **LOC:** 10523 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1261.4)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 821.9)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 258.1)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 171.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 1179 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 3968
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2667`, `structural_boundaries: 1064`, `args: 276`, `func_start: 251`
* *Risk/State:* `safety_bypasses: 223`, `high_risk_execution: 38`, `state_mutation: 1610`, `planned_debt: 2`, `fragile_debt: 31`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 28`, `import: 3`
* *Defense:* `safety: 1395`, `doc: 1`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.node.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10397.42 | **LOC:** 10523 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1261.4)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 821.9)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 258.1)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 171.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 1179 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 3968
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2667`, `structural_boundaries: 1064`, `args: 276`, `func_start: 251`
* *Risk/State:* `safety_bypasses: 223`, `high_risk_execution: 38`, `state_mutation: 1610`, `planned_debt: 2`, `fragile_debt: 31`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 28`, `import: 3`
* *Defense:* `safety: 1395`, `doc: 1`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10289.54 | **LOC:** 11354 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1255.2)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 852.1)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 258.5)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 172.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 1043 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 191
* *State Mutation (weighted view):* 3662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2785`, `structural_boundaries: 1102`, `args: 330`, `func_start: 282`
* *Risk/State:* `safety_bypasses: 268`, `high_risk_execution: 38`, `state_mutation: 1576`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 46`, `import: 3`
* *Defense:* `safety: 1443`, `doc: 1`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.browser.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10275.84 | **LOC:** 11329 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1255.2)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 852.1)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 258.5)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 172.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 1041 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 194
* *State Mutation (weighted view):* 3660
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2781`, `structural_boundaries: 1098`, `args: 329`, `func_start: 282`
* *Risk/State:* `safety_bypasses: 270`, `high_risk_execution: 38`, `state_mutation: 1578`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 44`, `import: 3`
* *Defense:* `safety: 1437`, `doc: 1`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10038.62 | **LOC:** 11122 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 99.6855% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1261.4)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 859.0)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 249.7)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 138.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 1014 instances
* *High Risk Execution (weighted view):* 17
* *Concurrency (weighted view):* 159
* *State Mutation (weighted view):* 3560
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2735`, `structural_boundaries: 1097`, `args: 352`, `func_start: 306`
* *Risk/State:* `safety_bypasses: 309`, `high_risk_execution: 35`, `state_mutation: 1532`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 10`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 39`, `import: 7`
* *Defense:* `safety: 1407`, `doc: 1`, `immutability_locks: 4`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, react, react-dom, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server.edge.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9916.94 | **LOC:** 10942 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1255.2)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 859.0)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 250.1)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 138.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 1001 instances
* *High Risk Execution (weighted view):* 17
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 3517
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2682`, `structural_boundaries: 1074`, `args: 319`, `func_start: 275`
* *Risk/State:* `safety_bypasses: 259`, `high_risk_execution: 35`, `state_mutation: 1515`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 42`, `import: 3`
* *Defense:* `safety: 1393`, `doc: 1`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server.browser.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9906.86 | **LOC:** 10923 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1255.2)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 859.0)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 250.1)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 138.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 1000 instances
* *High Risk Execution (weighted view):* 17
* *Concurrency (weighted view):* 175
* *State Mutation (weighted view):* 3516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2681`, `structural_boundaries: 1069`, `args: 317`, `func_start: 274`
* *Risk/State:* `safety_bypasses: 261`, `high_risk_execution: 35`, `state_mutation: 1516`, `planned_debt: 2`, `fragile_debt: 32`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 40`, `import: 3`
* *Defense:* `safety: 1391`, `doc: 1`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server-legacy.browser.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9795.14 | **LOC:** 10147 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1261.4)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 798.4)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 249.7)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 133.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 1108 instances
* *High Risk Execution (weighted view):* 17
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 3748
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2564`, `structural_boundaries: 1027`, `args: 265`, `func_start: 244`
* *Risk/State:* `safety_bypasses: 215`, `high_risk_execution: 35`, `state_mutation: 1532`, `planned_debt: 2`, `fragile_debt: 31`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 1348`, `doc: 1`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server-legacy.node.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9795.14 | **LOC:** 10147 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1261.4)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 798.4)
  * `validateProperty` **(Many-Argument Workhorses)** (Impact: 327.4)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 249.7)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 133.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 1108 instances
* *High Risk Execution (weighted view):* 17
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 3748
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2564`, `structural_boundaries: 1027`, `args: 265`, `func_start: 244`
* *Risk/State:* `safety_bypasses: 215`, `high_risk_execution: 35`, `state_mutation: 1532`, `planned_debt: 2`, `fragile_debt: 31`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 1348`, `doc: 1`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/acceptance-app/error-recovery.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 9674.08 | **LOC:** 1166 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.0%), Complexity Load (formerly Cognitive Load) (15.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 154
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 311`, `args: 77`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 4`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 42`, `concurrency: 124`, `import: 26`
* *Defense:* `safety: 2`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Foo, child, development-sandbox, e2e-utils, next-test-utils, outdent, path, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.node.production.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8676.96 | **LOC:** 8249 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1286.7)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 505.7)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 240.9)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 137.0)
  * `retryNode` **(Many-Argument Workhorses)** (Impact: 115.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 16 instances
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 998 instances
* *High Risk Execution (weighted view):* 18
* *Concurrency (weighted view):* 164
* *State Mutation (weighted view):* 3362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2103`, `structural_boundaries: 960`, `args: 312`, `func_start: 266`
* *Risk/State:* `safety_bypasses: 245`, `high_risk_execution: 34`, `state_mutation: 1366`, `fragile_debt: 22`, `duplicate_logic: 30`
* *Architecture:* `api: 24`, `concurrency: 39`, `import: 6`
* *Defense:* `safety: 1062`, `doc: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, react-dom-experimental, react-experimental, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server.edge.production.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8486.7 | **LOC:** 8070 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1287.5)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 505.7)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 241.3)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 137.0)
  * `retryNode` **(Many-Argument Workhorses)** (Impact: 115.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 16 instances
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 986 instances
* *High Risk Execution (weighted view):* 18
* *Concurrency (weighted view):* 187
* *State Mutation (weighted view):* 3323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2052`, `structural_boundaries: 937`, `args: 279`, `func_start: 235`
* *Risk/State:* `safety_bypasses: 195`, `high_risk_execution: 34`, `state_mutation: 1351`, `fragile_debt: 22`, `duplicate_logic: 14`
* *Architecture:* `api: 20`, `concurrency: 42`, `import: 2`
* *Defense:* `safety: 1052`, `doc: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom/cjs/react-dom-server.node.production.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8318.06 | **LOC:** 7927 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1286.7)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 482.5)
  * `pushAttribute` **(Many-Argument Workhorses)** (Impact: 232.4)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 112.8)
  * `finishedTask` **(Defensive Guards)** (Impact: 102.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 15 instances
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 953 instances
* *High Risk Execution (weighted view):* 16
* *Concurrency (weighted view):* 145
* *State Mutation (weighted view):* 3217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2014`, `structural_boundaries: 930`, `args: 302`, `func_start: 260`
* *Risk/State:* `safety_bypasses: 236`, `high_risk_execution: 31`, `state_mutation: 1311`, `fragile_debt: 22`, `duplicate_logic: 30`
* *Architecture:* `api: 24`, `concurrency: 35`, `import: 6`
* *Defense:* `safety: 1023`, `doc: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_hooks, crypto, react, react-dom, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-server-legacy.node.production.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8183.36 | **LOC:** 7143 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 91.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.028; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushStartInstance` **(Many-Argument Workhorses)** (Impact: 1286.5)
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 445.1)
  * `flushCompletedBoundary` **(Defensive Guards)** (Impact: 202.6)
  * `flushCompletedQueues` **(Many-Argument Workhorses)** (Impact: 141.9)
  * `retryNode` **(Many-Argument Workhorses)** (Impact: 113.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 16 instances
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 1108 instances
* *High Risk Execution (weighted view):* 18
* *Concurrency (weighted view):* 137
* *State Mutation (weighted view):* 3612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1968`, `structural_boundaries: 887`, `args: 228`, `func_start: 206`
* *Risk/State:* `safety_bypasses: 151`, `high_risk_execution: 34`, `state_mutation: 1396`, `fragile_debt: 22`, `duplicate_logic: 2`
* *Architecture:* `api: 18`, `concurrency: 27`, `import: 2`
* *Defense:* `safety: 1022`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react-dom-experimental, react-experimental
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/next/src/compiled/react-server-dom-turbopack-experimental/cjs/react-server-dom-turbopack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 100.0% | Debt: 13.067%
- `packages/next/src/compiled/react-server-dom-turbopack/cjs/react-server-dom-turbopack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 100.0% | Debt: 13.067%
- `packages/next/src/compiled/react-server-dom-webpack-experimental/cjs/react-server-dom-webpack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 100.0% | Debt: 13.0475%
- `packages/next/src/compiled/react-server-dom-webpack/cjs/react-server-dom-webpack-client.browser.development.js` -> Churn: **68.3%** | Cog Load: 100.0% | Debt: 13.0475%
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-client.production.js` -> Churn: **67.76%** | Cog Load: 80.8146% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/next/src/compiled/@vercel/og/index.node.js` -> **Shu Ding** (100.0% isolated ownership) | Magnitude: 23042.14
- `packages/next/src/compiled/@vercel/og/index.edge.js` -> **Shu Ding** (100.0% isolated ownership) | Magnitude: 21744.84
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-profiling.profiling.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 17753.44
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-unstable_testing.production.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 16496.76
- `packages/next/src/compiled/react-dom-experimental/cjs/react-dom-client.production.js` -> **nextjs-bot** (91.2% isolated ownership) | Magnitude: 15968.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/next/src/server/route-modules/app-page/module.ts` -> **Severity: 0.063** (Bridge: 0.0006 * Flux: 96.4325%)
- `packages/next/src/shared/lib/router/router.ts` -> **Severity: 0.049** (Bridge: 0.0005 * Flux: 100.0%)
- `packages/next/src/server/base-server.ts` -> **Severity: 0.042** (Bridge: 0.0004 * Flux: 99.396%)
- `packages/next/src/server/after/after-context.ts` -> **Severity: 0.037** (Bridge: 0.0004 * Flux: 90.2745%)
- `packages/next/src/server/route-modules/route-module.ts` -> **Severity: 0.036** (Bridge: 0.0004 * Flux: 90.5956%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/next/link.js` -> **Severity: 2.986** (Embedded: 0.0463 * Error Risk: 64.5656%)
- `test/lib/next-test-utils.ts` -> **Severity: 2.231** (Embedded: 0.0371 * Error Risk: 60.161%)
- `packages/next/server.js` -> **Severity: 2.207** (Embedded: 0.0282 * Error Risk: 78.3421%)
- `test/lib/next-webdriver.ts` -> **Severity: 1.846** (Embedded: 0.0225 * Error Risk: 82.1607%)
- `turbopack/crates/turbo-tasks-fs/src/embed/fs.rs` -> **Severity: 1.306** (Embedded: 0.0269 * Error Risk: 48.4699%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/lib/next-test-utils.ts` -> **Severity: 2394.109** (Blast Radius: 26.003 * Doc Risk: 92.0705%)
- `turbopack/crates/turbo-tasks-fs/src/embed/fs.rs` -> **Severity: 1470.4** (Blast Radius: 14.704 * Doc Risk: 100.0%)
- `packages/next/src/server/request/draft-mode.ts` -> **Severity: 637.607** (Blast Radius: 7.357 * Doc Risk: 86.6667%)
- `packages/next/src/server/web/spec-extension/user-agent.ts` -> **Severity: 629.2** (Blast Radius: 6.292 * Doc Risk: 100.0%)
- `test/lib/next-webdriver.ts` -> **Severity: 465.471** (Blast Radius: 10.861 * Doc Risk: 42.8571%)

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
