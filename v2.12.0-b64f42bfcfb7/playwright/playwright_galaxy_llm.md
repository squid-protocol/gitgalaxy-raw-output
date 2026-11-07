# ARCHITECTURAL_BRIEF: playwright
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/playwright.git` |
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
- **Scope:** 2088 analyzed artifact(s), 393674 LOC.
- **Load-bearing artifact:** `tests/page/pageTest.ts` -- 126 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/playwright-core/src/utils.ts` -- pulls in 44 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/assets/client-certificates/client/localhost/localhost.key` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 3087 |
| Analyzed Artifacts (Scanned) | 2088 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 999 |
| Total LOC | 393674 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 67.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7419 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2487 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.6361 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 180 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1303 | 251064 | 62.4% |
| JAVASCRIPT | 208 | 113124 | 10.0% |
| HTML | 160 | 3445 | 7.7% |
| CSS | 81 | 6505 | 3.9% |
| PLAINTEXT | 67 | 7 | 3.2% |
| MARKDOWN | 66 | 0 | 3.2% |
| JSON | 57 | 8201 | 2.7% |
| YAML | 34 | 5999 | 1.6% |
| SHELL | 33 | 948 | 1.6% |
| XML | 30 | 4 | 1.4% |
| CPP | 21 | 2197 | 1.0% |
| OBJECTIVE-C | 7 | 1271 | 0.3% |
| POWERSHELL | 7 | 122 | 0.3% |
| GROOVY | 3 | 50 | 0.1% |
| BATCH | 2 | 72 | 0.1% |
| JAVA | 2 | 466 | 0.1% |
| PYTHON | 2 | 70 | 0.1% |
| DOCKERFILE | 2 | 65 | 0.1% |
| CSHARP | 2 | 53 | 0.1% |
| MAKEFILE | 1 | 11 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2080 |
| unknown | unknown | 7 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 28%, Declarative / Non-Code 28%, Large Core Modules (3) 11%, Callbacks & Closures Files 10%, Large Core Modules (2) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1951 | 93.4% |
| Unknown | 7 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 126 | 6.0% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 999*

**Composition by Extension & Reason:**
- `.png`: 389x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 197x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 172x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.list`: 51x Unsupported Format (.list)
- `no_extension`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.ts`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 23624 LOC), 1x Excluded (Saturation: Line 17 exceeds 500 chars)
- `.js`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.zip`: 10x Excluded (Explicitly Denied Extension: '.zip')
- `.pem`: 7x Excluded (Unsupported Extension: '.pem')
- `.css`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.jpg`: 6x Excluded (Explicitly Denied Extension: '.jpg')
- `.ico`: 5x Excluded (Explicitly Denied Extension: '.ico')
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 8410 LOC), 1x Excluded (Static Asset Blob without Intent: 1137 LOC)
- `.build`: 4x Excluded (Unsupported Extension: '.build')
- `.xcconfig`: 4x Excluded (Unsupported Extension: '.xcconfig')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 27.5 | 6.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 36.3 | 47.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.8 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 50.9 | 57.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 31.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.6 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.1 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.1 | 7.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 85.9 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1398 | 332 | 1 | `browser_patches/webkit/embedder/Playwright/mac/BrowserWindowController.m` |
| cleanup | 1748 | 381 | 2 | `tests/library/browsertype-connect.spec.ts` |
| guards | 21679 | 972 | 14 | `tests/assets/reading-list/react-dom_18.1.0.js` |
| danger | 8765 | 889 | 10 | `tests/assets/reading-list/react-dom_15.7.0.js` |
| concurrency | 51862 | 1104 | 73 | `tests/playwright-test/reporter-html.spec.ts` |
| connectivity | 14905 | 1032 | 10 | `packages/playwright-core/src/server/chromium/protocol.d.ts` |
| io | 7827 | 766 | 11 | `tests/playwright-test/reporter-blob.spec.ts` |
| crypto | 18 | 17 | 0 | `tests/library/client-certificates.spec.ts` |
| ipc | 345 | 129 | 0 | `packages/playwright-core/src/server/webkit/protocol.d.ts` |
| time | 1212 | 277 | 1 | `tests/library/unit/clock.spec.ts` |
| serialization | 751 | 280 | 1 | `tests/playwright-test/web-server.spec.ts` |
| regex | 1207 | 331 | 1 | `tests/assets/reading-list/vue_2.6.14.js` |
| events | 5580 | 638 | 6 | `tests/assets/reading-list/vue_3.1.5.js` |
| tests | 28456 | 681 | 34 | `tests/playwright-test/reporter-html.spec.ts` |
| docs | 13697 | 1331 | 1 | `packages/playwright-core/src/server/chromium/protocol.d.ts` |
| debt | 4034 | 495 | 3 | `tests/assets/reading-list/react-dom_18.1.0.js` |
| mutation | 87025 | 1563 | 77 | `tests/assets/reading-list/react-dom_18.1.0.js` |
| dead_code | 558 | 151 | 0 | `browser_patches/firefox/juggler/TargetRegistry.js` |
| credential | 297 | 19 | 0 | `packages/playwright/bundles/expect/package-lock.json` |
| threat | 31 | 16 | 0 | `tests/playwright-test/fit-to-width.spec.ts` |
| ml_ai | 341 | 109 | 0 | `packages/playwright-core/src/server/dom.ts` |
| ui | 3532 | 351 | 3 | `tests/assets/reading-list/react-dom_17.0.2.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/playwright-test/reporter-blob.spec.ts` (Hits: 174)
- `tests/library/download.spec.ts` (Hits: 134)
- `tests/library/browsercontext-har.spec.ts` (Hits: 115)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pageTest.ts** (`tests/page/pageTest.ts`) — 126 inbound connections
2. **browserTest.ts** (`tests/config/browserTest.ts`) — 112 inbound connections
3. **playwright-test-fixtures.ts** (`tests/playwright-test/playwright-test-fixtures.ts`) — 86 inbound connections
4. **utils.ts** (`tests/config/utils.ts`) — 76 inbound connections
5. **utils.ts** (`packages/playwright-core/src/utils.ts`) — 69 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **utils.ts** (`packages/playwright-core/src/utils.ts`) — 44 outbound dependencies
2. **loader.spec.ts** (`tests/playwright-test/loader.spec.ts`) — 40 outbound dependencies
3. **page.ts** (`packages/playwright-core/src/client/page.ts`) — 37 outbound dependencies
4. **browserContext.ts** (`packages/playwright-core/src/client/browserContext.ts`) — 33 outbound dependencies
5. **tracing.ts** (`packages/playwright-core/src/server/trace/recorder/tracing.ts`) — 33 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `baseCreateRenderer` **(Many-Argument Workhorses)** (@ `tests/assets/reading-list/vue_3.1.5.js`) -> Impact: **614.7** | LOC: 1175
  * *Intent:* // implementation
- `createPatchFunction` **(Compute Cores)** (@ `tests/assets/reading-list/vue_2.6.14.js`) -> Impact: **348.4** | LOC: 717
- `tokenize` **(Compute Cores)** (@ `packages/playwright-core/src/utils/isomorphic/cssTokenizer.ts`) -> Impact: **338.9** | LOC: 470
- `ChildReconciler` **(Defensive Guards)** (@ `tests/assets/reading-list/react-dom_18.1.0.js`) -> Impact: **329.5** | LOC: 933
  * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we can do it manually. Helpers that don't need this b...
- `ChildReconciler` **(Defensive Guards)** (@ `tests/assets/reading-list/react-dom_17.0.2.js`) -> Impact: **316.5** | LOC: 927
  * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we can do it manually. Helpers that don't need this b...
- `ChildReconciler` **(Defensive Guards)** (@ `tests/assets/reading-list/react-dom_16.14.0.js`) -> Impact: **313.5** | LOC: 924
  * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we can do it manually. Helpers that don't need this b...
- `parseAttribute` **(Many-Argument Workhorses)** (@ `tests/assets/reading-list/vue_3.1.5.js`) -> Impact: **311.4** | LOC: 1793
- `frameSnapshotStreamer` **(Stateful Encapsulated Methods)** (@ `packages/playwright-core/src/server/trace/recorder/snapshotterInjected.ts`) -> Impact: **297.9** | LOC: 624
- `completeWork` **(Many-Argument Workhorses)** (@ `tests/assets/reading-list/react-dom_18.1.0.js`) -> Impact: **282.1** | LOC: 643
- `diffHydratedProperties` **(Many-Argument Workhorses)** (@ `tests/assets/reading-list/react-dom_18.1.0.js`) -> Impact: **263.3** | LOC: 287

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/playwright-test` | 104 | 46942.47 | 12.82% | 0.0% |
| `tests/page` | 125 | 40874.46 | 24.72% | 0.0% |
| `tests/library` | 96 | 26993.6 | 31.51% | 0.0% |
| `tests/assets/client-certificates/client/trusted` | 3 | 15000.0 | 0.0% | 0.0% |
| `packages/playwright-core/src/server` | 49 | 13117.35 | 66.27% | 1.64% |
| `tests/mcp` | 84 | 12876.02 | 11.77% | 0.0% |
| `tests/assets/reading-list` | 17 | 9754.63 | 24.52% | 0.0% |
| `packages/playwright-core/src/client` | 50 | 8856.88 | 60.49% | 9.38% |
| `packages/injected/src` | 21 | 8104.32 | 61.47% | 10.91% |
| `tests/library/inspector` | 18 | 5596.89 | 33.49% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/playwright-core/src/remote/serverTransport.ts` -> **100.0%** Exposure
- `utils/generate_types/overrides-test.d.ts` -> **100.0%** Exposure
- `utils/generate_types/overrides.d.ts` -> **100.0%** Exposure
- `.github/ISSUE_TEMPLATE/bug.yml` -> **99.9998%** Exposure
- `browser_patches/firefox/juggler/components/Juggler.js` -> **99.9995%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/dashboard/src/transport.ts` -> **100.0%** Exposure
- `packages/injected/src/bindingsController.ts` -> **100.0%** Exposure
- `packages/injected/src/consoleApi.ts` -> **100.0%** Exposure
- `packages/injected/src/highlight.ts` -> **100.0%** Exposure
- `packages/injected/src/selectorGenerator.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/assets/reading-list/react-dom_18.1.0.js` -> **0** Orphaned Functions | **56** Duplicates
- `utils/generate_types/overrides.d.ts` -> **13** Orphaned Functions | **36** Duplicates
- `utils/generate_types/overrides-test.d.ts` -> **35** Orphaned Functions | **13** Duplicates
- `browser_patches/firefox/juggler/TargetRegistry.js` -> **46** Orphaned Functions | **0** Duplicates
- `tests/assets/reading-list/react-dom_16.14.0.js` -> **0** Orphaned Functions | **43** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/playwright-core/src/server/utils/crypto.ts` -> **85.9083%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2694` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/assets/client-certificates/client/localhost/localhost.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/client-certificates/client/self-signed/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/client-certificates/client/trusted/cert-legacy.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/client-certificates/client/trusted/cert.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/client-certificates/client/trusted/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/client-certificates/server/server_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/config/testserver/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/playwright-test/reporter-html.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.075)
- **Top Global Matches:** file_cluster_10: 8.075, file_cluster_15: 9.214, file_cluster_13: 9.422
- **Magnitude:** 3026.08 | **LOC:** 3550 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.9%), Complexity Load (formerly Cognitive Load) (49.8%), Guard Balance (formerly Safety Score) (35.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calculateTotalTestDuration` **(Compute Cores)** (Impact: 9.2)
  * `showReport` **(Defensive Guards)** (Impact: 8.5)
  * `execGit` **(Parameter Forwarders)** (Impact: 3.8)
  * `ghaPullRequestEnv` **(Parameter Forwarders)** (Impact: 2.2)
  * `initGitRepo` **(Annotated & Test Methods)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 275 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 2752
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 1697`, `args: 363`, `func_start: 279`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 116`
* *Architecture:* `io: 77`, `api: 58`, `concurrency: 1377`, `import: 136`
* *Defense:* `safety: 14`, `doc: 1`, `test: 1029`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` httpServer, utils, formatUtils, html, first, helper, inner, playwright-test-fixtures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/library/browsercontext-cookies.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.927)
- **Top Global Matches:** file_cluster_10: 4.927, file_cluster_2: 6.968, file_cluster_13: 7.526
- **Magnitude:** 2960.13 | **LOC:** 466 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.5%), Guard Balance (formerly Safety Score) (45.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 198
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 102`, `args: 37`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `fragile_debt: 1`
* *Architecture:* `io: 52`, `concurrency: 73`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` browserTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/library/chromium/chromium.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.206)
- **Top Global Matches:** file_cluster_10: 6.206, file_cluster_12: 8.383, file_cluster_2: 8.711
- **Magnitude:** 2261.65 | **LOC:** 749 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.1%), Guard Balance (formerly Safety Score) (46.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 445
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 284`, `args: 145`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 29`, `fragile_debt: 3`
* *Architecture:* `io: 39`, `concurrency: 205`, `import: 2`
* *Defense:* `safety: 15`, `doc: 1`, `test: 73`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` browserTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/playwright-test/golden.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.926)
- **Top Global Matches:** file_cluster_10: 4.926, file_cluster_2: 7.218, file_cluster_13: 7.541
- **Magnitude:** 2202.92 | **LOC:** 1195 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (33.8%), Complexity Load (formerly Cognitive Load) (23.0%), Connectivity (formerly Api Exposure) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 231
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 212`, `args: 125`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`
* *Architecture:* `io: 113`, `api: 16`, `concurrency: 116`, `import: 61`
* *Defense:* `safety: 54`, `doc: 1`, `test: 313`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` helper, helper, helper, playwright-test-fixtures, test, safe, fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/playwright-core/src/server/frames.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.156)
- **Top Global Matches:** file_cluster_12: 8.156, file_cluster_5: 8.528, file_cluster_7: 10.593
- **Magnitude:** 2086.66 | **LOC:** 1823 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 52.6%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **22**; blast radius 1.221; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Complexity Load (formerly Cognitive Load) (97.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `waitForSelector` **(Many-Argument Workhorses)** (Impact: 71.8)
  * `_expectInternal` **(Many-Argument Workhorses)** (Impact: 60.9)
  * `_retryWithProgressIfNotConnected` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `gotoImpl` **(Defensive Guards)** (Impact: 42.8)
  * `waitForFunctionExpression` **(Many-Argument Workhorses)** (Impact: 40.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 47 instances
* *Amplified Cascading Flux:* 90 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 552
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 535`, `args: 260`, `func_start: 161`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 3`, `state_mutation: 134`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 77`, `concurrency: 317`, `import: 26`
* *Defense:* `safety: 61`, `doc: 1`, `test: 6`, `immutability_locks: 10`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.221
  * `Choke Point (Betweenness):` 0.001918 | `Ripple Effect (Closeness):` 0.034734
  * `Imports (Out-Degree: 27):` utils, manualPromise, selectorParser, browserContext, callLog, console, dom, errors...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `tests/playwright-test/playwright.trace.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.254)
- **Top Global Matches:** file_cluster_10: 5.254, file_cluster_13: 7.263, file_cluster_2: 7.77
- **Magnitude:** 2065.52 | **LOC:** 1430 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.2%), Guard Balance (formerly Safety Score) (39.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 90 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 811
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 448`, `args: 165`, `func_start: 108`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 42`
* *Architecture:* `io: 30`, `api: 26`, `concurrency: 361`, `import: 50`
* *Defense:* `safety: 15`, `doc: 1`, `test: 288`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` utils, helper, playwright-test-fixtures, test, fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/page/page-network-response.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.912)
- **Top Global Matches:** file_cluster_10: 4.912, file_cluster_2: 7.642, file_cluster_13: 7.878
- **Magnitude:** 1963.83 | **LOC:** 429 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (71.2%), Complexity Load (formerly Cognitive Load) (48.4%), Guard Balance (formerly Safety Score) (42.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 227
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 158`, `args: 57`, `func_start: 26`
* *Risk/State:* `state_mutation: 17`, `dead_code: 1`
* *Architecture:* `io: 19`, `concurrency: 112`, `import: 3`
* *Defense:* `safety: 6`, `doc: 1`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pageTest, fs, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/reading-list/react-dom_18.1.0.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.645)
- **Top Global Matches:** file_cluster_4: 10.645, file_cluster_12: 13.707, file_cluster_15: 13.916
- **Magnitude:** 1935.4 | **LOC:** 29772 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.277; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.2%), Complexity Load (formerly Cognitive Load) (41.4%), Connectivity (formerly Api Exposure) (35.6%), Concurrency Surface (formerly Concurrency) (13.5%)
- **Documentation Coverage:** 93.4272% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ChildReconciler` **(Defensive Guards)** (Impact: 329.5)
    * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we ...
  * `completeWork` **(Many-Argument Workhorses)** (Impact: 282.1)
  * `diffHydratedProperties` **(Many-Argument Workhorses)** (Impact: 263.3)
  * `diffProperties` **(Many-Argument Workhorses)** (Impact: 194.9)
  * `commitLayoutEffectOnFiber` **(Many-Argument Workhorses)** (Impact: 162.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1847 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 6414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4950`, `structural_boundaries: 4722`, `args: 1191`, `func_start: 1168`
* *Risk/State:* `safety_bypasses: 139`, `high_risk_execution: 22`, `state_mutation: 2720`, `dead_code: 5`, `planned_debt: 217`, `fragile_debt: 82`, `duplicate_logic: 56`
* *Architecture:* `io: 1`, `api: 24`, `concurrency: 21`, `import: 4`
* *Defense:* `safety: 2762`, `doc: 109`, `test: 2`, `immutability_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.277
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000478
  * `Imports (Out-Degree: 0):` react, client
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/playwright-test/test-step.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.052)
- **Top Global Matches:** file_cluster_10: 5.052, file_cluster_13: 7.259, file_cluster_2: 7.626
- **Magnitude:** 1929.21 | **LOC:** 1845 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (40.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.9%), Connectivity (formerly Api Exposure) (9.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 76 instances
* *Concurrency (weighted view):* 804
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 557`, `args: 233`, `func_start: 180`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 41`
* *Architecture:* `io: 14`, `api: 41`, `concurrency: 424`, `import: 49`
* *Defense:* `safety: 55`, `doc: 1`, `test: 281`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` helper, playwright-test-fixtures, test, reporter, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/injected/src/injectedScript.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.511)
- **Top Global Matches:** file_cluster_4: 7.511, file_cluster_12: 10.951, file_cluster_6: 12.048
- **Magnitude:** 1780.08 | **LOC:** 1860 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 57.9%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **19**; blast radius 0.829; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.6%)
- **Documentation Coverage:** 96.175% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectSingleElement` **(Many-Argument Workhorses)** (Impact: 144.7)
  * `dispatchEvent` **(Defensive Guards)** (Impact: 77.3)
  * `expect` **(Defensive Guards)** (Impact: 56.2)
  * `elementState` **(Compute Cores)** (Impact: 49.7)
  * `createTextMatcher` **(Compute Cores)** (Impact: 48.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 143 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 485
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 524`, `structural_boundaries: 411`, `args: 161`, `func_start: 111`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 4`, `state_mutation: 199`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 28`, `concurrency: 19`, `import: 27`
* *Defense:* `safety: 48`, `doc: 1`, `test: 1`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.829
  * `Choke Point (Betweenness):` 0.00099 | `Ripple Effect (Closeness):` 0.025862
  * `Imports (Out-Degree: 14):` ariaSnapshot, consoleApi, domUtils, highlight, layoutSelectorUtils, roleSelectorEngine, roleUtils, selectorEngine...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/playwright-test/reporter-blob.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.723)
- **Top Global Matches:** file_cluster_10: 7.723, file_cluster_13: 9.122, file_cluster_15: 9.124
- **Magnitude:** 1752.74 | **LOC:** 2377 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.8%), Guard Balance (formerly Safety Score) (43.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patchPathSeparators` **(Compute Cores)** (Impact: 10.6)
  * `patchPathSeparatorsRecursive` **(Compute Cores)** (Impact: 7.5)
  * `showReport` **(Defensive Guards)** (Impact: 7.4)
  * `zipReport` **(Callbacks & Closures)** (Impact: 2.4)
  * `files` **(Annotated & Test Methods)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 175 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 1416
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 802`, `args: 268`, `func_start: 236`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 165`
* *Architecture:* `io: 174`, `api: 70`, `concurrency: 541`, `import: 101`
* *Defense:* `safety: 17`, `doc: 1`, `test: 448`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` yazl, extract-zip, httpServer, userAgent, reporter, html, playwright-test-fixtures, test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/reading-list/react-dom_17.0.2.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.398)
- **Top Global Matches:** file_cluster_4: 10.398, file_cluster_12: 13.592, file_cluster_15: 13.958
- **Magnitude:** 1722.74 | **LOC:** 26293 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.277; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.1%), Complexity Load (formerly Cognitive Load) (41.9%), Connectivity (formerly Api Exposure) (36.0%), Concurrency Surface (formerly Concurrency) (13.9%)
- **Documentation Coverage:** 92.5134% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ChildReconciler` **(Defensive Guards)** (Impact: 316.5)
    * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we ...
  * `completeWork` **(Many-Argument Workhorses)** (Impact: 231.4)
  * `diffHydratedProperties` **(Many-Argument Workhorses)** (Impact: 215.4)
  * `diffProperties` **(Many-Argument Workhorses)** (Impact: 207.7)
  * `beginWork` **(Many-Argument Workhorses)** (Impact: 155.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 18 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 1709 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 5927
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4298`, `structural_boundaries: 4209`, `args: 1057`, `func_start: 1007`
* *Risk/State:* `safety_bypasses: 143`, `high_risk_execution: 21`, `state_mutation: 2509`, `dead_code: 3`, `planned_debt: 171`, `fragile_debt: 62`, `duplicate_logic: 42`
* *Architecture:* `io: 1`, `api: 24`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 2425`, `doc: 109`, `test: 7`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.277
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000478
  * `Imports (Out-Degree: 0):` react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/library/inspector/cli-codegen-1.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.965)
- **Top Global Matches:** file_cluster_7: 6.965, file_cluster_14: 8.593, file_cluster_5: 10.156
- **Magnitude:** 1701.63 | **LOC:** 1117 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (49.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 97 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 859
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 419`, `args: 79`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 115`, `high_risk_execution: 1`, `state_mutation: 51`
* *Architecture:* `io: 5`, `concurrency: 374`, `import: 2`
* *Defense:* `safety: 4`, `doc: 1`, `test: 163`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` inspectorTest, playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/library/trace-viewer.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.87)
- **Top Global Matches:** file_cluster_10: 6.87, file_cluster_12: 9.181, file_cluster_11: 9.396
- **Magnitude:** 1674.16 | **LOC:** 2283 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.5%), Complexity Load (formerly Cognitive Load) (49.7%), Guard Balance (formerly Safety Score) (42.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `recordTrace` **(Callbacks & Closures)** (Impact: 4.4)
  * `runBeforeCloseBrowserContext` **(Callbacks & Closures)** (Impact: 1.3)
  * `doClick` **(Interface Declarations)** (Impact: 1.1)
  * `onload` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 97 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 1570
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 1283`, `args: 317`, `func_start: 116`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 43`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 52`, `concurrency: 1085`, `import: 10`
* *Defense:* `safety: 24`, `doc: 1`, `test: 372`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` extract-zip, browserTest, traceViewerFixtures, utils, test, fs, http, path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/reading-list/react-dom_16.14.0.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.516)
- **Top Global Matches:** file_cluster_4: 10.516, file_cluster_12: 13.349, file_cluster_15: 13.662
- **Magnitude:** 1661.9 | **LOC:** 25148 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.277; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.3%), Complexity Load (formerly Cognitive Load) (40.7%), Connectivity (formerly Api Exposure) (35.7%), Concurrency Surface (formerly Concurrency) (14.9%)
- **Documentation Coverage:** 88.1279% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ChildReconciler` **(Defensive Guards)** (Impact: 313.5)
    * *Intent:* // to be able to optimize each path individually by branching early. This needs // a compiler or we ...
  * `diffHydratedProperties` **(Many-Argument Workhorses)** (Impact: 212.3)
  * `completeWork` **(Many-Argument Workhorses)** (Impact: 211.4)
  * `diffProperties` **(Many-Argument Workhorses)** (Impact: 197.6)
  * `beginWork` **(Many-Argument Workhorses)** (Impact: 143.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 17 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 1625 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 5601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4168`, `structural_boundaries: 4024`, `args: 1034`, `func_start: 977`
* *Risk/State:* `safety_bypasses: 128`, `high_risk_execution: 21`, `state_mutation: 2351`, `dead_code: 6`, `planned_debt: 160`, `fragile_debt: 55`, `duplicate_logic: 43`
* *Architecture:* `io: 1`, `api: 23`, `concurrency: 15`, `import: 7`
* *Defense:* `safety: 2250`, `doc: 150`, `test: 7`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.277
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000478
  * `Imports (Out-Degree: 0):` MyComponent, react, test-utils, react-test-renderer, unstable_mock
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/page/workers.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.485)
- **Top Global Matches:** file_cluster_10: 7.485, file_cluster_12: 8.865, file_cluster_13: 9.76
- **Magnitude:** 1396.73 | **LOC:** 367 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 85.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.9%), Guard Balance (formerly Safety Score) (40.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Concurrency (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 165`, `args: 64`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4`, `fragile_debt: 5`
* *Architecture:* `io: 20`, `concurrency: 135`, `import: 6`
* *Defense:* `safety: 6`, `doc: 1`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` errors, utils, pageTest, test, fs, playwright-core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/page/page-event-pageerror.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.297)
- **Top Global Matches:** file_cluster_10: 7.297, file_cluster_12: 8.306, file_cluster_2: 9.559
- **Magnitude:** 1385.95 | **LOC:** 233 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.216; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.4%), Guard Balance (formerly Safety Score) (45.0%), Mutation Surface (formerly State Flux) (40.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Concurrency (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 63`, `args: 37`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`
* *Architecture:* `io: 2`, `concurrency: 57`, `import: 1`
* *Defense:* `doc: 1`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pageTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/assets/reading-list/vue_3.1.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.613)
- **Top Global Matches:** file_cluster_4: 11.613, file_cluster_12: 15.233, file_cluster_6: 15.454
- **Magnitude:** 1362.48 | **LOC:** 14998 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.308; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (59.3%), Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (39.0%), Concurrency Surface (formerly Concurrency) (20.1%)
- **Documentation Coverage:** 92.2395% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `baseCreateRenderer` **(Many-Argument Workhorses)** (Impact: 614.7)
    * *Intent:* // implementation
  * `parseAttribute` **(Many-Argument Workhorses)** (Impact: 311.4)
  * `buildProps` **(Many-Argument Workhorses)** (Impact: 179.7)
  * `createHydrationFunctions` **(Defensive Guards)** (Impact: 169.8)
    * *Intent:* // Note: hydration is DOM-specific // But we have to place it in core due to tight coupling with cor...
  * `patchKeyedChildren` **(Many-Argument Workhorses)** (Impact: 150.9)
    * *Intent:* // can be all-keyed or mixed
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 1013 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 103
* *State Mutation (weighted view):* 3425
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3272`, `structural_boundaries: 1832`, `args: 1044`, `func_start: 858`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 115`, `high_risk_execution: 6`, `state_mutation: 1399`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 8`, `duplicate_logic: 6`
* *Architecture:* `api: 148`, `concurrency: 38`, `import: 1`
* *Defense:* `safety: 767`, `doc: 68`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000478
  * `Imports (Out-Degree: 0):` vue
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/playwright-core/src/server/dispatchers/browserDispatcher.ts` (TYPESCRIPT) | Magnitude: 158.16 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 52, concurrency: 36, args: 18
- `packages/trace-viewer/src/ui/networkResourceDetails.tsx` (TYPESCRIPT) | Magnitude: 96.88 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 79, branch: 63, core_var_decl: 63
- `packages/playwright-core/src/server/dispatchers/playwrightDispatcher.ts` (TYPESCRIPT) | Magnitude: 76.42 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 47, import: 20, branch: 16
- `packages/playwright-core/src/server/protocolError.ts` (TYPESCRIPT) | Magnitude: 31.48 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 15, api: 6, branch: 5
- `packages/playwright-core/src/server/dispatchers/elementHandlerDispatcher.ts` (TYPESCRIPT) | Magnitude: 268.8 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 113, concurrency: 108, args: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/library/modernizr.spec.ts` (TYPESCRIPT) | Magnitude: 127.8 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 54, structural_boundaries: 18, branch: 14
- `packages/playwright-core/src/tools/backend/verify.ts` (TYPESCRIPT) | Magnitude: 0.08 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 42, safety: 20, concurrency: 19
- `utils/flakiness-dashboard/processing/utils.js` (JAVASCRIPT) | Magnitude: 72.44 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, core_var_decl: 21, structural_boundaries: 18, concurrency: 15
- `tests/assets/input/touches.html` (HTML) | Magnitude: 8.5 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 11, args: 8, core_var_decl: 8
- `tests/assets/player.html` (HTML) | Magnitude: 76.24 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, concurrency: 14, core_var_decl: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/playwright-core/src/server/playwright.ts` (TYPESCRIPT) | Magnitude: 34.22 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 30, import: 14, state_mutation: 12
- `tests/assets/reading-list/vue3.html` (HTML) | Magnitude: 23.18 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 10, func_start: 9, core_var_decl: 8
- `packages/playwright/src/runner/workerHost.ts` (TYPESCRIPT) | Magnitude: 68.26 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 26, args: 12, func_start: 12
- `browser_patches/firefox/juggler/components/Juggler.js` (JAVASCRIPT) | Magnitude: 64.04 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 23, core_var_decl: 19, args: 14
- `tests/assets/reading-list/vue2.html` (HTML) | Magnitude: 24.12 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 9, func_start: 9, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/playwright-core/src/server/dispatchers/browserContextDispatcher.ts` (TYPESCRIPT) | Magnitude: 496.76 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 318, structural_boundaries: 150, concurrency: 105, branch: 78
- `packages/playwright/src/runner/tasks.ts` (TYPESCRIPT) | Magnitude: 671.66 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 320, structural_boundaries: 155, branch: 91, args: 64
- `tests/library/video.spec.ts` (TYPESCRIPT) | Magnitude: 388.94 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 621, structural_boundaries: 247, concurrency: 202, core_var_decl: 173
- `tests/page/retarget.spec.ts` (TYPESCRIPT) | Magnitude: 258.52 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 286, structural_boundaries: 195, concurrency: 155, core_var_decl: 120
- `tests/library/web-socket.spec.ts` (TYPESCRIPT) | Magnitude: 1003.51 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 110, args: 69, concurrency: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/components/ct-vue-cli/public/index.html` (HTML) | Magnitude: 17.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, core_var_decl: 5, design_snake_case: 5, structural_boundaries: 4
- `packages/trace-viewer/src/ui/metadataView.tsx` (TYPESCRIPT) | Magnitude: 16.76 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: ui_framework: 37, indent_spaces: 31, core_var_decl: 22, design_camel_case: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `browser_patches/winldd/PrintDeps.cpp` (CPP) | Magnitude: 31.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 61, core_var_decl: 13, structural_boundaries: 9, branch: 7
- `packages/playwright-core/src/client/timeoutSettings.ts` (TYPESCRIPT) | Magnitude: 53.24 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 22, branch: 16, args: 8
- `packages/playwright-core/src/utils/isomorphic/trace/traceUtils.ts` (TYPESCRIPT) | Magnitude: 37.72 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 14, branch: 9, core_var_decl: 8
- `tests/assets/input/keyboard.html` (HTML) | Magnitude: 32.32 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 16, branch: 9, args: 7
- `.github/workflows/tests_bidi.yml` (YAML) | Magnitude: 23.82 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 82, branch: 15, args: 12, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/playwright-core/src/tools/backend/logFile.ts` (TYPESCRIPT) | Magnitude: 0.08 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 23, encapsulation: 13, core_var_decl: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/playwright-core/src/utils.ts` (TYPESCRIPT) | Magnitude: 59.88 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 44, api: 44, import: 44, doc: 1
- `packages/playwright-core/src/client/api.ts` (TYPESCRIPT) | Magnitude: 48.64 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 36, api: 32, import: 32, io: 1
- `packages/playwright-core/src/tools/exports.ts` (TYPESCRIPT) | Magnitude: 0.03 | Delta: **0.191** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, api: 18, import: 18, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/assets/modernizr/index.html` (HTML) | Magnitude: 19.18 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 7, structural_boundaries: 5, branch: 4
- `utils/generate_types/overrides-testReporter.d.ts` (TYPESCRIPT) | Magnitude: 0.9 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 29, branch: 12, api: 12
- `packages/playwright-ct-react/cli.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 1, decorators: 1, import: 1
- `packages/playwright-ct-react17/cli.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 1, decorators: 1, import: 1
- `packages/playwright-ct-vue/cli.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 1, decorators: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/playwright-core/src/server/utils/processLauncher.ts` (TYPESCRIPT) | Magnitude: 169.5 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 175, structural_boundaries: 65, args: 42, branch: 37
- `packages/playwright-ct-vue/registerSource.mjs` (JAVASCRIPT) | Magnitude: 208.2 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 143, branch: 59, structural_boundaries: 38, core_var_decl: 29
- `packages/playwright-core/src/server/utils/httpServer.ts` (TYPESCRIPT) | Magnitude: 208.28 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 167, structural_boundaries: 52, branch: 49, args: 29
- `utils/generate_channels.js` (JAVASCRIPT) | Magnitude: 281.58 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 198, branch: 99, core_var_decl: 68, structural_boundaries: 66
- `packages/playwright-core/src/server/har/harRecorder.ts` (TYPESCRIPT) | Magnitude: 155.88 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 40, branch: 31, core_var_decl: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/playwright-core/src/browserServerImpl.ts` (TYPESCRIPT) | Magnitude: 102.48 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 43, branch: 16, core_var_decl: 16
- `packages/playwright-core/src/server/firefox/ffConnection.ts` (TYPESCRIPT) | Magnitude: 125.86 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 39, state_mutation: 29, args: 20
- `packages/trace-viewer/src/sw/traceLoaderBackends.ts` (TYPESCRIPT) | Magnitude: 115.02 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 50, concurrency: 37, core_var_decl: 20
- `packages/playwright/src/mcp/test/testBackend.ts` (TYPESCRIPT) | Magnitude: 56.12 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 31, branch: 10, import: 10
- `tests/library/events/utils.ts` (TYPESCRIPT) | Magnitude: 30.84 | Delta: **0.161** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 13, args: 7, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `utils/doclint/api_parser.js` (JAVASCRIPT) | Magnitude: 453.3 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 327, branch: 133, core_var_decl: 88, structural_boundaries: 73
- `packages/playwright-core/src/utils/isomorphic/selectorParser.ts` (TYPESCRIPT) | Magnitude: 577.66 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 346, branch: 150, core_var_decl: 88, state_mutation: 67

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/playwright/src/reportActions.ts` (TYPESCRIPT) | Magnitude: 49.94 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 23, branch: 13, core_var_decl: 9
- `packages/playwright-core/src/cli/driver.ts` (TYPESCRIPT) | Magnitude: 48.32 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 30, branch: 15, core_var_decl: 14
- `packages/playwright-core/src/server/android/driver/app/src/androidTest/java/com/microsoft/playwright/androiddriver/InstrumentedTest.java` (JAVA) | Magnitude: 308.24 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 342, structural_boundaries: 118, branch: 84, core_var_decl: 84
- `browser_patches/roll_from_upstream.sh` (SHELL) | Magnitude: 21.26 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 16, branch: 4, io: 3
- `tests/playwright-test/ui-mode-test-network-tab.spec.ts` (TYPESCRIPT) | Magnitude: 319.58 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 324, structural_boundaries: 234, concurrency: 199, test: 102

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/playwright/src/index.ts` -> Churn: **86.89%** | Cog Load: 97.0352% | Debt: 8.0706%
- `packages/playwright-core/src/client/page.ts` -> Churn: **85.41%** | Cog Load: 98.4892% | Debt: 0.0%
- `packages/playwright-core/src/server/dispatchers/pageDispatcher.ts` -> Churn: **83.26%** | Cog Load: 100.0% | Debt: 8.4199%
- `packages/playwright-core/src/server/page.ts` -> Churn: **82.1%** | Cog Load: 98.8706% | Debt: 8.7682%
- `packages/playwright-core/src/server/webkit/wkPage.ts` -> Churn: **75.21%** | Cog Load: 100.0% | Debt: 9.735%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/library/chromium/chromium.spec.ts` -> **Dmitry Gozman** (100.0% isolated ownership) | Magnitude: 2261.65
- `tests/page/workers.spec.ts` -> **Dmitry Gozman** (85.7% isolated ownership) | Magnitude: 1396.73
- `tests/page/expect-boolean.spec.ts` -> **Dmitry Gozman** (100.0% isolated ownership) | Magnitude: 1101.03
- `packages/injected/src/roleUtils.ts` -> **Adam Gastineau** (100.0% isolated ownership) | Magnitude: 1032.76
- `tests/playwright-test/loader.spec.ts` -> **Simon Knott** (100.0% isolated ownership) | Magnitude: 1027.29

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/playwright-core/src/outofprocess.ts` -> **Severity: 1.211** (Bridge: 0.0145 * Flux: 83.2018%)
- `packages/playwright-core/src/server/playwright.ts` -> **Severity: 1.054** (Bridge: 0.0108 * Flux: 97.5191%)
- `packages/playwright-core/src/client/connection.ts` -> **Severity: 1.052** (Bridge: 0.0105 * Flux: 100.0%)
- `packages/playwright-core/src/androidServerImpl.ts` -> **Severity: 1.044** (Bridge: 0.0114 * Flux: 91.6827%)
- `tests/page/pageTest.ts` -> **Severity: 0.882** (Bridge: 0.0088 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/config/utils.ts` -> **Severity: 7.699** (Embedded: 0.1176 * Error Risk: 65.4753%)
- `packages/playwright-core/src/client/eventEmitter.ts` -> **Severity: 7.623** (Embedded: 0.1013 * Error Risk: 75.2746%)
- `packages/playwright-core/src/server/utils/zipFile.ts` -> **Severity: 7.458** (Embedded: 0.1078 * Error Risk: 69.2157%)
- `packages/playwright-core/src/utils/isomorphic/locatorGenerators.ts` -> **Severity: 6.51** (Embedded: 0.1027 * Error Risk: 63.3634%)
- `packages/playwright-core/src/utils/isomorphic/selectorParser.ts` -> **Severity: 6.088** (Embedded: 0.0841 * Error Risk: 72.3886%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/config/utils.ts` -> **Severity: 2601.5** (Blast Radius: 26.015 * Doc Risk: 100.0%)
- `tests/page/pageTest.ts` -> **Severity: 1943.0** (Blast Radius: 19.43 * Doc Risk: 100.0%)
- `tests/config/browserTest.ts` -> **Severity: 1803.7** (Blast Radius: 18.037 * Doc Risk: 100.0%)
- `tests/playwright-test/playwright-test-fixtures.ts` -> **Severity: 1239.2** (Blast Radius: 12.392 * Doc Risk: 100.0%)
- `tests/mcp/fixtures.ts` -> **Severity: 1154.9** (Blast Radius: 11.549 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1886 literal sites + 48 sites through wrappers = 1934
- **`panics_and_aborts`:** 2325 literal sites + 11 sites through wrappers = 2336

- `wrap` (function, debug_prints, primitive): 12 call sites in 1 files -- `packages/playwright/src/reporters/multiplexer.ts`
- `writeFile` (function, debug_prints, primitive): 11 call sites in 1 files -- `packages/playwright/src/agents/generateAgents.ts`
- `consoleTable` (function, debug_prints, primitive): 4 call sites in 1 files -- `tests/assets/reading-list/react-dom_15.7.0.js`
- `die` (function, debug_prints, primitive): 4 call sites in 1 files -- `utils/workspace.js`
- `die` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `utils/workspace.js`
- `initRepoDone` (function, debug_prints, primitive): 4 call sites in 1 files -- `packages/playwright/src/agents/generateAgents.ts`
- `print` (function, debug_prints, primitive): 4 call sites in 1 files -- `packages/playwright/src/plugins/gitCommitInfoPlugin.ts`
- `throwOnHydrationMismatch` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `tests/assets/reading-list/react-dom_18.1.0.js`
- `wrapAsync` (function, debug_prints, primitive): 3 call sites in 1 files -- `packages/playwright/src/reporters/multiplexer.ts`
- `throwElementIsNotAttached` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/playwright-core/src/server/dom.ts`
- `writeFiles` (function, debug_prints, primitive): 2 call sites in 1 files -- `packages/playwright/src/matchers/toMatchSnapshot.ts`
- `generateWebKitProtocol` (function, debug_prints, primitive): 1 call sites in 1 files -- `utils/protocol-types-generator/index.js`
*(+5 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 43193 call pairs -- scoped 44.5%, unique 0.0%, ambiguous 22.5%, external 33.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 24318 | 39.5% | 0.0% | 29.1% | 31.4% |
| javascript | 17141 | 54.8% | 0.0% | 15.1% | 30.1% |
| cpp | 647 | 15.5% | 0.9% | 7.7% | 75.9% |
| objective-c | 400 | 11.2% | 1.0% | 1.8% | 86.0% |
| html | 270 | 5.6% | 0.0% | 0.0% | 94.4% |
| java | 197 | 22.3% | 0.0% | 0.0% | 77.7% |
| shell | 192 | 6.2% | 0.0% | 0.0% | 93.8% |
| python | 28 | 7.1% | 0.0% | 0.0% | 92.9% |

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
