# ARCHITECTURAL_BRIEF: next.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/vercel/next.js.git` |
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
- **Scope:** 23499 analyzed artifact(s), 1030043 LOC.
- **Load-bearing artifact:** `packages/next/link.js` -- 1146 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `turbopack/crates/turbopack-ecmascript/src/references/mod.rs` -- pulls in 237 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` at magnitude 23099.52 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 23499 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4909 |
| Total LOC | 1030043 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 82.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7812 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2012 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 8.3372 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1534 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 9884 | 517703 | 42.1% |
| JAVASCRIPT | 9407 | 246802 | 40.0% |
| RUST | 960 | 220068 | 4.1% |
| PLAINTEXT | 782 | 30 | 3.3% |
| CSS | 755 | 25634 | 3.2% |
| MARKDOWN | 704 | 0 | 3.0% |
| JSON | 636 | 12621 | 2.7% |
| XML | 246 | 66 | 1.0% |
| YAML | 74 | 5798 | 0.3% |
| SHELL | 25 | 752 | 0.1% |
| HTML | 12 | 118 | 0.1% |
| DOCKERFILE | 10 | 321 | 0.0% |
| MAKEFILE | 1 | 27 | 0.0% |
| SQLITE | 1 | 14 | 0.0% |
| BATCH | 1 | 5 | 0.0% |
| PYTHON | 1 | 84 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 23468 |
| unknown | unknown | 30 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Declarative / Non-Code 11%, Parameter Forwarders Files 8%, Callbacks & Closures Files 8%, Interface Declarations Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 21966 | 93.5% |
| Unknown | 30 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1456 | 6.2% |
| Static: Minified & Vendor Opaque Mass | 47 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4909*

**Composition by Extension & Reason:**
- `.js`: 1053x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 59x Excluded (Saturation: Line 1 exceeds 500 chars), 23x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 531x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 30x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.mdx`: 422x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 374x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 4x Excluded (Machine-Generated Source Code Signature: 9 LOC)
- `.json`: 351x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1294 LOC), 1x Excluded (Static Asset Blob without Intent: 1026 LOC)
- `.snapshot`: 285x Excluded (Unsupported Extension: '.snapshot')
- `.png`: 277x Excluded (Explicitly Denied Extension: '.png')
- `.map`: 217x Unresolved Ambiguity (No Retainable Structure), 33x Excluded (Saturation: Line 5 exceeds 500 chars), 10x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.ico`: 157x Excluded (Explicitly Denied Extension: '.ico')
- `.stderr`: 102x Excluded (Unsupported Extension: '.stderr')
- `.scss`: 96x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Zero-Density Threshold (LOC: 131, Signals: 0)
- `.jpg`: 84x Excluded (Explicitly Denied Extension: '.jpg')
- `.example`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 69x Unsupported Format (.toml), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `.mjs`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.4 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.9 | 14.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.9 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.0 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 99.0 | 2.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3820 | 1092 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` |
| cleanup | 1605 | 515 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` |
| guards | 33083 | 3885 | 2 | `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` |
| danger | 18261 | 3079 | 1 | `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js` |
| concurrency | 81694 | 6658 | 6 | `test/integration/file-serving/test/index.test.ts` |
| connectivity | 41950 | 17220 | 3 | `crates/next-core/src/next_config.rs` |
| io | 18030 | 3035 | 1 | `test/e2e/app-dir/cache-components-errors/cache-components-errors.test.ts` |
| crypto | 175 | 72 | 0 | `test/e2e/app-dir/cache-components-errors/cache-components-errors.test.ts` |
| ipc | 315 | 176 | 0 | `turbopack/crates/turbopack-tests/tests/execution/turbopack/basic/worker-threads/input/index.js` |
| time | 2114 | 1075 | 0 | `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js` |
| serialization | 3012 | 1180 | 0 | `test/integration/i18n-support/test/shared.ts` |
| regex | 2460 | 810 | 0 | `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js` |
| events | 5330 | 1161 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/load.js` |
| tests | 42604 | 2421 | 1 | `test/integration/file-serving/test/index.test.ts` |
| docs | 16287 | 2165 | 0 | `turbopack/crates/turbo-tasks-macros/src/derive/task_storage_macro.rs` |
| debt | 7817 | 2401 | 1 | `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` |
| mutation | 155841 | 14264 | 11 | `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js` |
| dead_code | 5820 | 4058 | 1 | `test/e2e/app-dir/monaco-editor/components/editor/monaco.ts` |
| credential | 198 | 56 | 0 | `scripts/deploy-docs.sh` |
| threat | 70 | 39 | 0 | `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` |
| ml_ai | 2405 | 457 | 0 | `test/e2e/app-dir/cache-components-errors/cache-components-errors.test.ts` |
| ui | 22247 | 5976 | 2 | `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` |

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

1. **link.js** (`packages/next/link.js`) — 1146 inbound connections
2. **server.js** (`packages/next/server.js`) — 682 inbound connections
3. **mod.rs** (`turbopack/crates/turbo-tasks/src/vc/mod.rs`) — 456 inbound connections
4. **headers.js** (`packages/next/headers.js`) — 403 inbound connections
5. **navigation.js** (`packages/next/navigation.js`) — 399 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`turbopack/crates/turbopack-ecmascript/src/references/mod.rs`) — 237 outbound dependencies
2. **lib.rs** (`turbopack/crates/turbopack-ecmascript/src/lib.rs`) — 179 outbound dependencies
3. **lib.rs** (`turbopack/crates/turbo-tasks/src/lib.rs`) — 170 outbound dependencies
4. **app.rs** (`crates/next-api/src/app.rs`) — 139 outbound dependencies
5. **project.rs** (`crates/next-api/src/project.rs`) — 139 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `renderToHTMLImpl` **(Many-Argument Workhorses)** (@ `packages/next/src/server/render.tsx`) -> Impact: **741.7** | LOC: 1154
- `createHotReloaderTurbopack` **(Many-Argument Workhorses)** (@ `packages/next/src/server/dev/hot-reloader-turbopack.ts`) -> Impact: **681.5** | LOC: 1565
- `createPatchedFetcher` **(Many-Argument Workhorses)** (@ `packages/next/src/server/lib/patch-fetch.ts`) -> Impact: **649.7** | LOC: 1043
- `fetch` **(Many-Argument Workhorses)** (@ `packages/next/src/server/lib/patch-fetch.ts`) -> Impact: **648.7** | LOC: 1022
  * *Intent:* // Create the patched fetch function.
- `assignDefaultsAndValidate` **(Many-Argument Workhorses)** (@ `packages/next/src/server/config.ts`) -> Impact: **645.1** | LOC: 1186
  * *Intent:* /** * Assigns defaults to the user config and validates the config. * */
- `getResolveRoutes` **(Many-Argument Workhorses)** (@ `packages/next/src/server/lib/router-utils/resolve-routes.ts`) -> Impact: **623.4** | LOC: 879
- `prepare` **(Many-Argument Workhorses)** (@ `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js`) -> Impact: **592.5** | LOC: 729
- `cache` **(Many-Argument Workhorses)** (@ `packages/next/src/server/use-cache/use-cache-wrapper.ts`) -> Impact: **568.2** | LOC: 1028
- `createMetadataElements` **(Many-Argument Workhorses)** (@ `packages/next/src/lib/metadata/metadata.tsx`) -> Impact: **550.1** | LOC: 1555
  * *Intent:* // --------------------------------------------------------------------------- // Metadata tag rendering // ------------------------------------------...
- `setProp` **(Many-Argument Workhorses)** (@ `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js`) -> Impact: **528.0** | LOC: 453

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `turbopack/crates/turbopack-ecmascript/tests/benches` | 2 | 39075.5 | 84.51% | 0.0% |
| `test/development/acceptance-app` | 19 | 18148.62 | 16.6% | 0.0% |
| `test/production/standalone-mode/required-server-files` | 14 | 15969.62 | 9.49% | 0.0% |
| `test/development/app-dir/typed-env` | 6 | 15137.26 | 0.0% | 0.0% |
| `test/integration/env-config/app` | 5 | 15007.74 | 0.0% | 0.0% |
| `test/development/acceptance` | 11 | 14328.04 | 13.26% | 0.0% |
| `packages/next/src/compiled/@edge-runtime/primitives` | 24 | 10508.44 | 11.11% | 15.41% |
| `packages/next/src/server` | 56 | 10039.02 | 27.72% | 8.59% |
| `packages/next/src/server/app-render` | 67 | 9756.62 | 26.43% | 8.34% |
| `test/integration/css/test` | 7 | 8533.2 | 48.86% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/next/src/compiled/@edge-runtime/cookies/index.d.ts` -> **100.0%** Exposure
- `packages/next/src/experimental/testing/server/config-testing-utils.test.ts` -> **100.0%** Exposure
- `packages/next/src/next-devtools/dev-overlay.shim.ts` -> **100.0%** Exposure
- `turbopack/crates/turbo-tasks/src/task/task_input.rs` -> **100.0%** Exposure
- `turbopack/crates/turbo-tasks/src/trace.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `apps/bundle-analyzer/components/import-chain.tsx` -> **100.0%** Exposure
- `apps/bundle-analyzer/components/treemap-visualizer.tsx` -> **100.0%** Exposure
- `examples/cms-payload/components/RichText/serialize.tsx` -> **100.0%** Exposure
- `examples/i18n-routing-pages/pages/gsp/[slug].tsx` -> **100.0%** Exposure
- `examples/with-cloudinary/pages/p/[photoId].tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` -> **20** Orphaned Functions | **63** Duplicates
- `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js` -> **51** Orphaned Functions | **21** Duplicates
- `turbopack/crates/turbo-frozenmap/src/map.rs` -> **0** Orphaned Functions | **41** Duplicates
- `turbopack/crates/turbopack-tests/tests/snapshot/swc_transforms/preset_env/output/0rv8_turbopack-tests_tests_snapshot_swc_transforms_preset_env_input_index_04jskxh.js` -> **7** Orphaned Functions | **30** Duplicates
- `turbopack/crates/turbopack-core/src/resolve/mod.rs` -> **33** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `scripts/deploy-docs.sh` -> **100.0%** Exposure
- `examples/with-firebase/vercel.json` -> **99.9997%** Exposure
- `examples/with-supertokens/app/config/backend.ts` -> **99.999%** Exposure
- `examples/with-algolia-react-instantsearch/components/Search.tsx` -> **99.7922%** Exposure
- `test/lib/next-modes/next-start.ts` -> **94.6967%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `47` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36491` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.414)
- **Top Global Matches:** file_cluster_4: 8.414, file_cluster_6: 10.661, file_cluster_12: 13.653
- **Magnitude:** 23099.52 | **LOC:** 25669 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (92.7%), Guard Balance (formerly Safety Score) (51.9%), Concurrency Surface (formerly Concurrency) (20.6%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setProp` **(Many-Argument Workhorses)** (Impact: 528.0)
  * `diffHydratedProperties` **(Many-Argument Workhorses)** (Impact: 490.5)
  * `dispatchEventForPluginEventSystem` **(Many-Argument Workhorses)** (Impact: 487.9)
  * `completeWork` **(Many-Argument Workhorses)** (Impact: 474.6)
  * `updateClassComponent` **(Many-Argument Workhorses)** (Impact: 465.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 24 instances
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 2002 instances
* *High Risk Execution (weighted view):* 11
* *Concurrency (weighted view):* 209
* *State Mutation (weighted view):* 6941
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6522`, `structural_boundaries: 2764`, `args: 1015`, `func_start: 938`
* *Risk/State:* `safety_bypasses: 414`, `high_risk_execution: 35`, `state_mutation: 2937`, `planned_debt: 1`, `fragile_debt: 87`, `duplicate_logic: 63`, `unreferenced_by_name: 20`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 64`, `import: 4`
* *Defense:* `safety: 3654`, `doc: 1`, `immutability_locks: 7`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, react-dom, scheduler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 13.68)
- **Top Global Matches:** file_cluster_4: 13.68, file_cluster_12: 14.118, file_cluster_7: 15.411
- **Magnitude:** 15975.98 | **LOC:** 30073 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.039; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.5%), Complexity Load (formerly Cognitive Load) (76.3%), Guard Balance (formerly Safety Score) (59.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare` **(Many-Argument Workhorses)** (Impact: 592.5)
  * `n3` **(Many-Argument Workhorses)** (Impact: 356.2)
  * `n7` **(Many-Argument Workhorses)** (Impact: 255.9)
  * `rj` **(Many-Argument Workhorses)** (Impact: 224.2)
  * `handleRewrites` **(Many-Argument Workhorses)** (Impact: 206.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 16 instances
* *Amplified Race Conditions:* 281 instances
* *Amplified Cascading Flux:* 997 instances
* *High Risk Execution (weighted view):* 15
* *Concurrency (weighted view):* 1997
* *State Mutation (weighted view):* 4921
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3137`, `structural_boundaries: 5909`, `args: 2593`, `func_start: 1728`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 1754`, `high_risk_execution: 31`, `state_mutation: 2927`, `fragile_debt: 42`, `duplicate_logic: 21`, `unreferenced_by_name: 51`
* *Architecture:* `io: 52`, `api: 19`, `concurrency: 592`, `import: 30`
* *Defense:* `safety: 3129`, `sync_locks: 2`, `cleanup: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 4.2e-05
  * `Imports (Out-Degree: 0):` async_hooks, crypto, fs, jsonwebtoken, action-async-storage.external.js, after-task-async-storage.external.js, track-module-loading.external.js, work-async-storage.external.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/integration/css-modules/test/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.901)
- **Top Global Matches:** file_cluster_10: 4.901, file_cluster_2: 7.269, file_cluster_13: 7.843
- **Magnitude:** 7146.6 | **LOC:** 801 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (44.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 64 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 465
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 213`, `args: 90`, `func_start: 21`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 24`
* *Architecture:* `io: 2`, `concurrency: 145`, `import: 5`
* *Defense:* `safety: 3`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cheerio, fs-extra, next-test-utils, next-webdriver, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/acceptance/ReactRefreshLogBox.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.689)
- **Top Global Matches:** file_cluster_10: 5.689, file_cluster_2: 6.272, file_cluster_0: 6.473
- **Magnitude:** 6584.81 | **LOC:** 1505 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.3%), Connectivity (formerly Api Exposure) (9.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 317`, `args: 67`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 1`, `planned_debt: 2`
* *Architecture:* `io: 40`, `api: 37`, `concurrency: 149`, `import: 17`
* *Defense:* `safety: 5`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Child, FunctionDefault.js, index.module.css, development-sandbox, e2e-utils, next-test-utils, outdent, path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/acceptance-app/ReactRefreshLogBox.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.535)
- **Top Global Matches:** file_cluster_10: 5.535, file_cluster_2: 6.606, file_cluster_0: 6.818
- **Magnitude:** 6220.74 | **LOC:** 1802 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.8%), Complexity Load (formerly Cognitive Load) (10.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *High Risk Execution (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 451`, `args: 95`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 26`, `state_mutation: 1`, `planned_debt: 10`, `fragile_debt: 4`
* *Architecture:* `io: 34`, `api: 45`, `concurrency: 209`, `import: 21`
* *Defense:* `safety: 9`, `test: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Child, FunctionDefault.js, actions, boom.css, index.module.css, module, styles1.css, styles2.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/integration/css/test/css-compilation.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.277)
- **Top Global Matches:** file_cluster_10: 4.277, file_cluster_2: 6.3, file_cluster_13: 6.329
- **Magnitude:** 5460.8 | **LOC:** 619 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.5%), Complexity Load (formerly Cognitive Load) (49.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 290
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 117`, `args: 48`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 30`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 75`, `import: 11`
* *Defense:* `safety: 2`, `test: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` )
        const nextConfig = new File(join(appDir, next.config.js, cheerio, fs-extra, next-test-utils, next-webdriver, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/@edge-runtime/primitives/fetch.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.721)
- **Top Global Matches:** file_cluster_12: 8.721, file_cluster_4: 8.924, file_cluster_15: 10.583
- **Magnitude:** 5207.66 | **LOC:** 18583 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.1%), Concurrency Surface (formerly Concurrency) (90.6%), Connectivity (formerly Api Exposure) (56.8%), Complexity Load (formerly Cognitive Load) (51.2%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 150.5)
  * `processHeader` **(Defensive Guards)** (Impact: 89.3)
  * `parseURL` **(Defensive Guards)** (Impact: 43.3)
  * `buildConnector` **(Defensive Guards)** (Impact: 38.9)
  * `connect` **(Many-Argument Workhorses)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 133 instances
* *Amplified Cascading Flux:* 286 instances
* *Concurrency (weighted view):* 922
* *State Mutation (weighted view):* 2731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 540`, `structural_boundaries: 2965`, `args: 1205`, `func_start: 905`
* *Risk/State:* `safety_bypasses: 320`, `state_mutation: 2159`, `planned_debt: 9`
* *Architecture:* `io: 51`, `api: 60`, `concurrency: 257`, `import: 92`
* *Defense:* `safety: 1894`, `doc: 114`, `sync_locks: 3`, `immutability_locks: 4`, `cleanup: 138`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` client.js, proxy-agent, assert, async_hooks, buffer, console, crypto, diagnostics_channel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/next/src/compiled/@edge-runtime/primitives/load.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.592)
- **Top Global Matches:** file_cluster_4: 8.592, file_cluster_12: 8.844, file_cluster_15: 10.647
- **Magnitude:** 5194.12 | **LOC:** 18714 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **29**; blast radius 0.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Concurrency Surface (formerly Concurrency) (90.9%), Complexity Load (formerly Cognitive Load) (50.9%), Guard Balance (formerly Safety Score) (49.7%)
- **Documentation Coverage:** 89.5425% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 150.5)
  * `processHeader` **(Defensive Guards)** (Impact: 89.3)
  * `parseURL` **(Defensive Guards)** (Impact: 43.3)
  * `buildConnector` **(Defensive Guards)** (Impact: 38.9)
  * `connect` **(Many-Argument Workhorses)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 135 instances
* *Amplified Cascading Flux:* 280 instances
* *Concurrency (weighted view):* 936
* *State Mutation (weighted view):* 2726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 528`, `structural_boundaries: 2968`, `args: 1211`, `func_start: 910`
* *Risk/State:* `safety_bypasses: 320`, `high_risk_execution: 1`, `state_mutation: 2166`, `planned_debt: 9`
* *Architecture:* `io: 51`, `api: 62`, `concurrency: 261`, `import: 100`
* *Defense:* `safety: 1896`, `doc: 114`, `sync_locks: 3`, `immutability_locks: 4`, `cleanup: 138`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000152
  * `Imports (Out-Degree: 1):` client.js, proxy-agent, abort-controller.js.text.js, console.js.text.js, events.js.text.js, stream, timers.js.text.js, url.js.text.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/api-routes-apollo-server-and-client-auth/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/cms-payload/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/convex/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-docker-compose/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-docker-multi-env/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-msw/.env.production` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-passport-and-next-connect/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-passport/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-react-intl/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-realm-web/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-relay-modern/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-sitemap/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/with-zones/home/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/app-dir/typed-env/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/app-dir/typed-env/.env.local` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/development/app-dir/typed-env/.env.production` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/development/basic/define-class-fields/fixture/pages/index.tsx` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, core_var_decl: 5, args: 4
- `test/development/typescript-plugin/metadata/app/warn-no-type/generate-metadata/has-type/export-separate-from-next-async-arrow-function/page.tsx` (TYPESCRIPT) | Magnitude: 6.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, args: 2, func_start: 2
- `crates/next-core/src/bootstrap.rs` (RUST) | Magnitude: 138.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 34, branch: 25, test: 18
- `test/e2e/next-form/basepath/app/forms/button-formaction/page.tsx` (TYPESCRIPT) | Magnitude: 2.88 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, core_var_decl: 3, design_snake_case: 3
- `test/e2e/app-dir/external-redirect/components/link-accordion.tsx` (TYPESCRIPT) | Magnitude: 7.22 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 7, ui_framework: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/e2e/app-dir/segment-cache/staleness/components/link-accordion.tsx` (TYPESCRIPT) | Magnitude: 7.22 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 6, ui_framework: 4, core_var_decl: 4
- `test/e2e/app-dir/static-siblings/components/link-accordion.tsx` (TYPESCRIPT) | Magnitude: 7.22 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 6, ui_framework: 4, core_var_decl: 4
- `test/e2e/app-dir/use-offline/components/link-accordion.tsx` (TYPESCRIPT) | Magnitude: 7.22 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 6, ui_framework: 4, core_var_decl: 4
- `test/e2e/app-dir/concurrent-navigations/components/link-accordion.tsx` (TYPESCRIPT) | Magnitude: 10.14 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 7, core_var_decl: 5, branch: 4
- `test/e2e/app-dir/segment-cache/vary-params/components/link-accordion.tsx` (TYPESCRIPT) | Magnitude: 10.14 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 7, core_var_decl: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `turbopack/crates/turbopack-tests/tests/execution/turbopack/basic/async-lazy-init/input/index.js` (JAVASCRIPT) | Magnitude: 23.84 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 14, core_var_decl: 8, structural_boundaries: 5, design_camel_case: 5
- `test/e2e/app-dir/use-cache-dev/app/page.tsx` (TYPESCRIPT) | Magnitude: 13.68 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 11, core_var_decl: 8, design_snake_case: 8
- `packages/next/src/server/dev/browser-logs/file-logger.ts` (TYPESCRIPT) | Magnitude: 95.1 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 29, core_var_decl: 16, args: 15
- `evals/evals/agent-023-avoid-getserversideprops/app/page.tsx` (TYPESCRIPT) | Magnitude: 8.38 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, concurrency: 4, args: 2
- `test/e2e/app-dir/app-external/app/mixed/dynamic/page.js` (JAVASCRIPT) | Magnitude: 3.28 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 6, args: 3, indent_spaces: 3, ui_framework: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/integration/next-image-legacy/basic/pages/client-side.js` (JAVASCRIPT) | Magnitude: 5.42 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 90, core_var_decl: 58, design_snake_case: 57, ui_framework: 12
- `packages/next/src/server/config-shared.ts` (TYPESCRIPT) | Magnitude: 95.3 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 853, branch: 341, doc: 208, structural_boundaries: 110
- `examples/with-turso/app/todo-list.tsx` (TYPESCRIPT) | Magnitude: 18.84 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 13, branch: 8, concurrency: 6
- `examples/with-apivideo/components/Card/Card.module.css` (CSS) | Magnitude: 0.8 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 29, ui_framework: 9, class_start: 8, safety_bypasses: 1
- `crates/next-custom-transforms/src/react_compiler.rs` (RUST) | Magnitude: 111.54 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 41, args: 27, func_start: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/next-codemod/transforms/__testfixtures__/url-to-withrouter/destructuring-this-class.output.js` (JAVASCRIPT) | Magnitude: 2.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 1, args: 1
- `packages/next-codemod/transforms/__testfixtures__/url-to-withrouter/destructuring-this.output.js` (JAVASCRIPT) | Magnitude: 2.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 1, args: 1
- `packages/next-codemod/transforms/__testfixtures__/next-request-geo-ip/destructure-alias.output.ts` (TYPESCRIPT) | Magnitude: 3.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, import: 2, core_var_decl: 2
- `packages/next-codemod/transforms/__testfixtures__/next-request-geo-ip/destructure.output.ts` (TYPESCRIPT) | Magnitude: 3.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, import: 2, core_var_decl: 2
- `turbopack/crates/turbopack-tests/tests/execution/webpack/inner-graph/pure-in-removed/input/import-module.js` (JAVASCRIPT) | Magnitude: 2.5 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, test: 5, indent_spaces: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/next-codemod/transforms/__testfixtures__/next-async-request-api-dynamic-apis/generate-metadata-access-api-prop-03.input.tsx` (TYPESCRIPT) | Magnitude: 5.7 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, concurrency: 3, indent_spaces: 2, args: 1
- `packages/next-codemod/transforms/__testfixtures__/next-async-request-api-dynamic-apis/generate-metadata-access-api-prop-03.output.tsx` (TYPESCRIPT) | Magnitude: 6.7 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 5, concurrency: 4, indent_spaces: 2, args: 1
- `test/e2e/app-dir/next-font/app/navigation/page.js` (JAVASCRIPT) | Magnitude: 2.6 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, safety_bypasses: 2, branch: 1
- `turbopack/packages/devlow-bench/src/interfaces/compose.ts` (TYPESCRIPT) | Magnitude: 55.56 | Delta: **0.179** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 30, branch: 10, structural_boundaries: 8, safety_bypasses: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/lib/turbo.ts` (TYPESCRIPT) | Magnitude: 10.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, branch: 4, structural_boundaries: 3, globals: 3
- `test/production/chunk-load-failure/app/dynamic/async.ts` (TYPESCRIPT) | Magnitude: 3.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, args: 1, func_start: 1
- `packages/next-codemod/bin/agents-md.ts` (TYPESCRIPT) | Magnitude: 115.86 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 145, core_var_decl: 36, design_camel_case: 28, structural_boundaries: 25
- `test/e2e/app-dir/segment-cache/memory-pressure/segment-cache-memory-pressure.test.ts` (TYPESCRIPT) | Magnitude: 178.04 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 50, concurrency: 38, core_var_decl: 26
- `test/e2e/getserversideprops/app/pages/index.js` (JAVASCRIPT) | Magnitude: 19.5 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 84, core_var_decl: 17, design_snake_case: 16, ui_framework: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/next/src/server/normalizers/locale-route-normalizer.ts` (TYPESCRIPT) | Magnitude: 6.28 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 5, api: 3, args: 2
- `packages/next/src/server/normalizers/absolute-filename-normalizer.ts` (TYPESCRIPT) | Magnitude: 7.36 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, api: 3, import: 3
- `packages/next/src/server/route-matcher-providers/helpers/manifest-loaders/server-manifest-loader.ts` (TYPESCRIPT) | Magnitude: 6.24 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `turbopack/crates/turbo-tasks/src/task/mod.rs` (RUST) | Magnitude: 25.22 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, api: 10, import: 5, encapsulation: 4
- `packages/next/src/server/web/exports/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/next/src/server/web/http.ts` (TYPESCRIPT) | Magnitude: 4.86 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, api: 3, doc: 3
- `turbopack/crates/turbopack-ecmascript/src/references/esm/mod.rs` (RUST) | Magnitude: 24.34 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, encapsulation: 8, indent_spaces: 7
- `packages/next/src/server/node-environment.ts` (TYPESCRIPT) | Magnitude: 15.22 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, scientific: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/cms-cosmic/components/footer.tsx` (TYPESCRIPT) | Magnitude: 4.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, core_var_decl: 9, ui_framework: 7, design_camel_case: 6
- `packages/next-codemod/transforms/__testfixtures__/url-to-withrouter/variable-export.output.js` (JAVASCRIPT) | Magnitude: 2.24 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, core_var_decl: 2, branch: 1
- `test/e2e/app-dir/instant-validation/app/suspense-in-root/static/missing-suspense-in-parallel-route/@slot/default.tsx` (TYPESCRIPT) | Magnitude: 5.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, branch: 2, concurrency: 2
- `test/e2e/app-dir/actions/app/mutate-cookie/page-2/page.js` (JAVASCRIPT) | Magnitude: 5.74 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, branch: 2, concurrency: 2
- `test/development/dev-indicator/app/app/static-indicator/dynamic/page.tsx` (TYPESCRIPT) | Magnitude: 7.44 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, concurrency: 5, indent_spaces: 3, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/next-code-frame/src/highlight.rs` (RUST) | Magnitude: 487.14 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1028, structural_boundaries: 259, core_var_decl: 199, design_snake_case: 198
- `turbopack/crates/turbopack-trace-server/src/viewer.rs` (RUST) | Magnitude: 488.12 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1050, structural_boundaries: 161, branch: 150, core_var_decl: 80
- `packages/next/src/client/route-params.ts` (TYPESCRIPT) | Magnitude: 6.32 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 51, branch: 44, args: 11
- `turbopack/crates/turbopack-ecmascript/src/analyzer/side_effects.rs` (RUST) | Magnitude: 299.14 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1632, core_var_decl: 204, immutability_locks: 193, design_snake_case: 182
- `crates/next-core/src/next_font/google/mod.rs` (RUST) | Magnitude: 390.34 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 600, structural_boundaries: 168, branch: 107, core_var_decl: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `examples/with-gsap/pages/index.tsx` (TYPESCRIPT) | Magnitude: 9.32 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 46, core_var_decl: 9, structural_boundaries: 7, design_camel_case: 7
- `packages/next/src/next-devtools/dev-overlay/segment-explorer-trie.ts` (TYPESCRIPT) | Magnitude: 97.24 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 50, core_var_decl: 24, args: 20
- `examples/api-routes-apollo-server-and-client-auth/pages/signup.tsx` (TYPESCRIPT) | Magnitude: 17.04 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 51, core_var_decl: 15, structural_boundaries: 12, design_snake_case: 9
- `packages/next/src/next-devtools/userspace/app/forward-logs-utils.ts` (TYPESCRIPT) | Magnitude: 51.1 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 20, branch: 15, safety: 11
- `turbopack/crates/turbo-tasks/src/graph/with_future.rs` (RUST) | Magnitude: 15.8 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 14, generics: 11, concurrency: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `scripts/sync-react.js` (JAVASCRIPT) | Magnitude: 364.54 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 534, core_var_decl: 79, branch: 70, structural_boundaries: 62
- `packages/next/src/lib/metadata/resolvers/resolve-opengraph.ts` (TYPESCRIPT) | Magnitude: 154.24 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 46, branch: 42, core_var_decl: 20
- `packages/next-codemod/transforms/middleware-to-proxy.ts` (TYPESCRIPT) | Magnitude: 552.74 | Delta: **0.183** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 684, branch: 162, structural_boundaries: 123, core_var_decl: 96

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/e2e/streaming-ssr-edge/pages/err/index.js` (JAVASCRIPT) | Magnitude: 5.3 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, api: 2
- `test/integration/500-page/pages/err.js` (JAVASCRIPT) | Magnitude: 4.3 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, closures: 2
- `examples/with-unsplash/styles/global.css` (CSS) | Magnitude: 0.79 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 25, globals: 3, safety_bypasses: 1
- `examples/with-electron-typescript/electron-src/preload.ts` (TYPESCRIPT) | Magnitude: 4.4 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, args: 3, func_start: 3
- `test/e2e/next-font/with-proxy.test.ts` (TYPESCRIPT) | Magnitude: 147.13 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 17, concurrency: 9, test: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `apps/bundle-analyzer/components/file-search.tsx` (TYPESCRIPT) | Magnitude: 33.1 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 16, core_var_decl: 14, ui_framework: 12
- `evals/evals/agent-029-use-cache-directive/EVAL.ts` (TYPESCRIPT) | Magnitude: 23.32 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 22, test: 14, branch: 11
- `packages/next/src/server/lib/server-action-request-meta.ts` (TYPESCRIPT) | Magnitude: 37.38 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 13, branch: 12, core_var_decl: 8
- `scripts/pack-util.ts` (TYPESCRIPT) | Magnitude: 109.36 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 38, branch: 18, args: 17
- `packages/next/src/client/components/segment-cache/navigation.ts` (TYPESCRIPT) | Magnitude: 357.46 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 648, structural_boundaries: 76, core_var_decl: 62, branch: 55

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/next/src/server/app-render/app-render.tsx` -> Churn: **82.03%** | Cog Load: 53.2342% | Debt: 23.1775%
- `packages/next/src/server/dev/hot-reloader-turbopack.ts` -> Churn: **64.18%** | Cog Load: 97.9434% | Debt: 20.426%
- `crates/next-api/src/app.rs` -> Churn: **61.08%** | Cog Load: 87.4131% | Debt: 8.3269%
- `packages/next/src/server/base-server.ts` -> Churn: **58.38%** | Cog Load: 89.164% | Debt: 8.8918%
- `packages/next/src/client/components/router-reducer/fetch-server-response.ts` -> Churn: **58.02%** | Cog Load: 56.4643% | Debt: 17.3498%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `turbopack/crates/turbopack-ecmascript/tests/benches/app-page-turbo.runtime.prod.js` -> **Janka Uryga** (100.0% isolated ownership) | Magnitude: 15975.98
- `test/integration/css-modules/test/index.test.ts` -> **Niklas Mischkulnig** (100.0% isolated ownership) | Magnitude: 7146.6
- `test/e2e/app-dir/cache-components/cache-components.test.ts` -> **Zack Tanner** (100.0% isolated ownership) | Magnitude: 3069.12
- `test/production/adapter-config/adapter-config.test.ts` -> **JJ Kasper** (85.7% isolated ownership) | Magnitude: 2683.99
- `turbopack/crates/turbopack-tracing/tests/node-file-trace/test/unit/webpack-wrapper-strs-namespaces-large/input.js` -> **Niklas Mischkulnig** (100.0% isolated ownership) | Magnitude: 2183.92

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/next/src/server/route-modules/app-page/module.ts` -> **Severity: 0.239** (Bridge: 0.0025 * Flux: 96.4325%)
- `packages/next/src/shared/lib/router/router.ts` -> **Severity: 0.141** (Bridge: 0.0014 * Flux: 100.0%)
- `crates/next-api/src/project.rs` -> **Severity: 0.096** (Bridge: 0.0017 * Flux: 57.9163%)
- `packages/next/src/server/request/fallback-params.ts` -> **Severity: 0.078** (Bridge: 0.0023 * Flux: 33.7185%)
- `packages/next/src/shared/lib/router-context.shared-runtime.ts` -> **Severity: 0.068** (Bridge: 0.0012 * Flux: 57.5%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/next/link.js` -> **Severity: 2.488** (Embedded: 0.0491 * Error Risk: 50.7142%)
- `packages/next/src/server/web/spec-extension/adapters/reflect.ts` -> **Severity: 1.031** (Embedded: 0.0172 * Error Risk: 60.0%)
- `packages/next/src/lib/detached-promise.ts` -> **Severity: 1.0** (Embedded: 0.0125 * Error Risk: 80.0%)
- `packages/next/src/shared/lib/router/utils/format-url.ts` -> **Severity: 0.966** (Embedded: 0.0136 * Error Risk: 70.8139%)
- `turbopack/crates/turbo-tasks-fs/src/read_glob.rs` -> **Severity: 0.956** (Embedded: 0.0119 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/next/src/server/request/draft-mode.ts` -> **Severity: 597.914** (Blast Radius: 6.899 * Doc Risk: 86.6667%)
- `turbopack/crates/turbo-rcstr/src/lib.rs` -> **Severity: 335.5** (Blast Radius: 3.965 * Doc Risk: 84.6154%)
- `packages/next/src/server/web/spec-extension/response.ts` -> **Severity: 275.0** (Blast Radius: 2.75 * Doc Risk: 100.0%)
- `packages/next/cache.js` -> **Severity: 233.75** (Blast Radius: 4.675 * Doc Risk: 50.0%)
- `packages/next/src/shared/lib/invariant-error.ts` -> **Severity: 185.6** (Blast Radius: 1.856 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 4368 literal sites + 200 sites through wrappers = 4568
- **`panics_and_aborts`:** 5323 literal sites + 214 sites through wrappers = 5537

- `logger` (function, debug_prints, primitive): 62 call sites in 10 files -- `.github/actions/next-stats-action/src/util/logger.js`
- `warnInvalidHookAccess` (function, debug_prints, primitive): 60 call sites in 1 files -- `turbopack/crates/turbopack-ecmascript/tests/benches/react-dom-client.development.js`
- `ImageResponse` (function, panics_and_aborts, primitive): 44 call sites in 44 files -- `packages/next/src/server/web/spec-extension/image-response.ts`
- `nextFontError` (function, panics_and_aborts, primitive): 24 call sites in 6 files -- `packages/font/src/next-font-error.ts`
- `fatalMessage` (function, debug_prints, primitive): 12 call sites in 1 files -- `packages/next-codemod/transforms/cra-to-next.ts`
- `fatalMessage` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `packages/next-codemod/transforms/cra-to-next.ts`
- `trackMissingSampleErrorAndThrow` (function, panics_and_aborts, primitive): 9 call sites in 2 files -- `packages/next/src/server/app-render/instant-validation/instant-samples.ts`
- `invariant` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `turbopack/crates/turbopack-tests/tests/snapshot/debug-ids/browser/output/1i9t_crates_turbopack-tests_tests_snapshot_debug-ids_browser_input_index_19boa0e.js`
- `invariant` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `turbopack/crates/turbopack-tests/tests/snapshot/runtime/default_dev_runtime/output/0rv8_turbopack-tests_tests_snapshot_runtime_default_dev_runtime_input_index_17smy-b.js`
- `invariant` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `turbopack/crates/turbopack-tests/tests/snapshot/workers/basic/output/1i9t_crates_turbopack-tests_tests_snapshot_workers_basic_input_index_09-gc7x.js`
- `invariant` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `turbopack/crates/turbopack-tests/tests/snapshot/workers/basic/output/1i9t_crates_turbopack-tests_tests_snapshot_workers_basic_input_worker_0yr5fg0.js`
- `invariant` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `turbopack/crates/turbopack-tests/tests/snapshot/workers/shared/output/1i9t_crates_turbopack-tests_tests_snapshot_workers_shared_input_index_0arnewp.js`
*(+85 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 109039 call pairs -- scoped 22.0%, unique 0.0%, ambiguous 26.4%, external 51.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 54133 | 20.0% | 0.0% | 21.5% | 58.4% |
| typescript | 33766 | 23.9% | 0.0% | 32.2% | 43.9% |
| javascript | 20964 | 23.9% | 0.0% | 29.7% | 46.4% |
| shell | 161 | 8.7% | 0.0% | 0.0% | 91.3% |
| python | 15 | 33.3% | 0.0% | 0.0% | 66.7% |

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
