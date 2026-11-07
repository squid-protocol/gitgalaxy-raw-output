# ARCHITECTURAL_BRIEF: cypress
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cypress-io/cypress.git` |
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
- **Scope:** 6115 analyzed artifact(s), 428676 LOC.
- **Load-bearing artifact:** `system-tests/lib/system-tests.ts` -- 142 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `CONTRIBUTING.md` -- pulls in 64 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 6964 |
| Analyzed Artifacts (Scanned) | 6115 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 849 |
| Total LOC | 428676 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9057 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1588 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.4829 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 469 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2393 | 251793 | 39.1% |
| JAVASCRIPT | 1828 | 113717 | 29.9% |
| HTML | 663 | 37959 | 10.8% |
| JSON | 333 | 15128 | 5.4% |
| MARKDOWN | 288 | 0 | 4.7% |
| XML | 245 | 18 | 4.0% |
| PLAINTEXT | 218 | 5 | 3.6% |
| CSS | 108 | 4897 | 1.8% |
| YAML | 25 | 4852 | 0.4% |
| SHELL | 10 | 296 | 0.2% |
| CSV | 4 | 11 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 4 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 6106 |
| unknown | unknown | 5 |
| cp1252 | cp1252-fallback | 3 |
| latin-1 | latin-1-fallback | 1 |

> 2 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk / big5 / euc_kr: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `system-tests/projects/e2e/static/charsets/euc-kr.html`, `system-tests/projects/e2e/static/charsets/gb2312.html`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 46%, Declarative / Non-Code 23%, Callbacks & Closures Files 14%, Large Core Modules (2) 4%, Large Core Modules (3) 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5598 | 91.5% |
| Unknown | 5 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 501 | 8.2% |
| Static: Minified & Vendor Opaque Mass | 11 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 849*

**Composition by Extension & Reason:**
- `.ansi`: 156x Excluded (Unsupported Extension: '.ansi')
- `.lock`: 121x Excluded (Unsupported Extension: '.lock')
- `no_extension`: 112x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable)
- `.png`: 80x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Massive Static Asset Blob: 5877 LOC), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.vue`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Saturation: Line 25 exceeds 500 chars)
- `.ts`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.patch`: 30x Excluded (Unsupported Extension: '.patch')
- `.coffee`: 25x Excluded (Unsupported Extension: '.coffee')
- `.snap`: 24x Excluded (Unsupported Extension: '.snap')
- `.js`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 15 LOC), 1x Zero-Density Threshold (LOC: 65, Signals: 0)
- `.tsx`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 46 LOC), 1x Excluded (Machine-Generated Source Code Signature: 30 LOC)
- `.template`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 12x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.7 | 23.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 17.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.0 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 75.0 | 1.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 36.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.5 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1664 | 530 | 0 | `cli/types/cypress.d.ts` |
| cleanup | 335 | 160 | 0 | `packages/server/lib/browsers/browser-cri-client.ts` |
| guards | 26730 | 1582 | 5 | `system-tests/__snapshots__/record_spec.js` |
| danger | 7932 | 1526 | 3 | `system-tests/__snapshots__/protocol_spec.js` |
| concurrency | 16228 | 1353 | 6 | `cli/types/cypress.d.ts` |
| connectivity | 8462 | 2529 | 3 | `packages/driver/cypress/fixtures/dom.html` |
| io | 15109 | 1315 | 4 | `system-tests/projects/e2e/elements.html` |
| crypto | 35 | 33 | 0 | `scripts/binary/binary-sources.js` |
| ipc | 175 | 110 | 0 | `packages/extension/test/integration/v3/content.spec.ts` |
| time | 818 | 326 | 0 | `packages/driver/cypress/e2e/cy/timers.cy.js` |
| serialization | 483 | 264 | 0 | `packages/driver/cypress/e2e/commands/net_stubbing.cy.ts` |
| regex | 1093 | 398 | 0 | `packages/server/test/integration/http_requests_spec.js` |
| events | 13023 | 1384 | 4 | `packages/driver/cypress/e2e/commands/navigation.cy.js` |
| tests | 50725 | 2070 | 15 | `system-tests/__snapshots__/protocol_spec.js` |
| docs | 3023 | 814 | 1 | `cli/types/cypress.d.ts` |
| debt | 6520 | 1049 | 2 | `system-tests/__snapshots__/record_spec.js` |
| mutation | 57868 | 3673 | 24 | `system-tests/projects/e2e/elements.html` |
| dead_code | 841 | 361 | 0 | `packages/errors/test/visualSnapshotErrors.spec.ts` |
| credential | 106 | 26 | 0 | `packages/app/cypress/fixtures/debug-Passing/gql-Debug.json` |
| threat | 48 | 19 | 0 | `system-tests/test/issue_8280_spec.js` |
| ml_ai | 231 | 75 | 0 | `packages/server/test/support/fixtures/server/err_response.html` |
| ui | 4653 | 906 | 2 | `system-tests/projects/e2e/elements.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `system-tests/projects/e2e/elements.html` (Hits: 3500)
- `packages/driver/src/cypress/error_messages.ts` (Hits: 264)
- `packages/network-tools/test/unit/cors.spec.ts` (Hits: 183)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **system-tests.ts** (`system-tests/lib/system-tests.ts`) — 142 inbound connections
2. **spec_helper.js** (`packages/server/test/spec_helper.js`) — 94 inbound connections
3. **error_utils.ts** (`packages/driver/src/cypress/error_utils.ts`) — 80 inbound connections
4. **utils.ts** (`packages/driver/cypress/support/utils.ts`) — 66 inbound connections
5. **log.d.ts** (`packages/driver/types/cypress/log.d.ts`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 64 outbound dependencies
2. **server-base.ts** (`packages/server/lib/server-base.ts`) — 48 outbound dependencies
3. **cypress.ts** (`packages/driver/src/cypress.ts`) — 45 outbound dependencies
4. **node_builtins.cy.js** (`system-tests/projects/node-builtins/cypress/e2e/node_builtins.cy.js`) — 36 outbound dependencies
5. **index.ts** (`packages/data-context/graphql/schemaTypes/objectTypes/index.ts`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addAll` **(Many-Argument Workhorses)** (@ `cli/types/cypress.d.ts`) -> Impact: **356.0** | LOC: 1785
  * *Intent:* /** * Add one or more custom commands that validate their prevSubject */
- `startListening` **(Many-Argument Workhorses)** (@ `packages/server/lib/socket-base.ts`) -> Impact: **258.0** | LOC: 603
- `type` **(Many-Argument Workhorses)** (@ `packages/driver/src/cy/commands/actions/type.ts`) -> Impact: **206.8** | LOC: 575
- `action` **(Many-Argument Workhorses)** (@ `packages/driver/src/cypress.ts`) -> Impact: **174.2** | LOC: 366
- `create` **(Compute Cores)** (@ `packages/driver/src/cy/chai/inspect.ts`) -> Impact: **157.6** | LOC: 437
  * *Intent:* // let config = require('../config')
- `origin` **(Many-Argument Workhorses)** (@ `cli/types/cypress.d.ts`) -> Impact: **153.7** | LOC: 753
  * *Intent:* /** * Enables running Cypress commands in a secondary origin. * cy.origin('example.com', () => { * cy.get('h1').should('equal', 'Example Domain') * })...
- `visit` **(Many-Argument Workhorses)** (@ `packages/driver/src/cy/commands/navigation.ts`) -> Impact: **139.0** | LOC: 425
- `session` **(Many-Argument Workhorses)** (@ `packages/driver/src/cy/commands/sessions/index.ts`) -> Impact: **133.6** | LOC: 472
- `addToCypressConfigPlugin` **(Compute Cores)** (@ `packages/config/src/ast-utils/addToCypressConfigPlugin.ts`) -> Impact: **120.9** | LOC: 200
  * *Intent:* /** * Standardizes our approach to writing values into the existing * Cypress config file. Attempts to handle the pragmatic cases, * finding the typic...
- `onGitLogChange` **(Defensive Guards)** (@ `packages/data-context/src/sources/GitDataSource.ts`) -> Impact: **118.0** | LOC: 409

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cli/test/lib` | 6 | 5842.82 | 23.67% | 0.0% |
| `packages/driver/src/cypress` | 35 | 5601.64 | 36.57% | 7.05% |
| `packages/frontend-shared/src/components` | 56 | 5296.06 | 5.06% | 4.03% |
| `__monolith__` | 22 | 5230.44 | 0.19% | 0.0% |
| `npm/webpack-preprocessor` | 12 | 5229.98 | 3.24% | 1.4% |
| `cli` | 13 | 5157.04 | 1.31% | 0.0% |
| `npm/vue` | 12 | 5110.08 | 1.28% | 0.0% |
| `npm/svelte` | 9 | 5050.62 | 0.57% | 0.0% |
| `packages/data-context/test/unit/sources` | 13 | 4685.44 | 37.79% | 0.0% |
| `packages/server/lib` | 36 | 4389.36 | 40.17% | 8.92% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/frontend-shared/cypress/fixtures/dummy-protocol.js` -> **100.0%** Exposure
- `system-tests/__snapshots__/before_all_after_all_throws_spec.ts.js` -> **100.0%** Exposure
- `system-tests/__snapshots__/cy_origin_retries_spec.ts.js` -> **100.0%** Exposure
- `system-tests/__snapshots__/fails_prior_to_top_change_retry_succeeds_spec.ts.js` -> **100.0%** Exposure
- `system-tests/__snapshots__/retries_spec.ts.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `npm/react/cypress/component/advanced/tutorial/tic-tac-toe.jsx` -> **100.0%** Exposure
- `npm/react/cypress/component/basic/react-tutorial/game.jsx` -> **100.0%** Exposure
- `packages/driver/cypress/e2e/util/limited_map.cy.js` -> **100.0%** Exposure
- `packages/extension/test/helpers/background.js` -> **100.0%** Exposure
- `packages/server/__snapshots__/cypress_spec.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/errors/test/visualSnapshotErrors.spec.ts` -> **133** Orphaned Functions | **0** Duplicates
- `packages/proxy/test/unit/http/response-middleware.spec.ts` -> **3** Orphaned Functions | **88** Duplicates
- `packages/proxy/test/unit/http/request-middleware.spec.ts` -> **1** Orphaned Functions | **49** Duplicates
- `packages/telemetry/test/span-exporters/cloud-span-exporter.spec.ts` -> **0** Orphaned Functions | **40** Duplicates
- `packages/app/src/runner/SpecRunnerHeaderOpenMode.cy.tsx` -> **0** Orphaned Functions | **30** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/https-proxy/test/unit/ca.spec.ts` -> **99.5195%** Exposure
- `packages/https-proxy/test/integration/proxy.spec.ts` -> **94.1605%** Exposure
- `packages/server/test/unit/cache_spec.ts` -> **85.9083%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6354` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/vue/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/webpack-preprocessor/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/test/lib/util.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.464)
- **Top Global Matches:** file_cluster_10: 4.464, file_cluster_2: 7.599, file_cluster_13: 7.946
- **Magnitude:** 3609.53 | **LOC:** 723 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Guard Balance (formerly Safety Score) (32.6%), Complexity Load (formerly Cognitive Load) (8.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 186`, `args: 110`, `func_start: 20`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`
* *Architecture:* `io: 4`, `concurrency: 52`, `import: 19`
* *Defense:* `safety: 22`, `test: 176`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` logger, util, assert, hasha, os, systeminformation, tty, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/test/unit/browsers/memory/memory_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.531)
- **Top Global Matches:** file_cluster_10: 5.531, file_cluster_2: 6.543, file_cluster_13: 7.504
- **Magnitude:** 3064.2 | **LOC:** 731 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.2%), Complexity Load (formerly Cognitive Load) (32.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 82`, `args: 31`, `func_start: 20`
* *Risk/State:* `state_mutation: 10`, `planned_debt: 93`
* *Architecture:* `io: 7`, `concurrency: 62`, `import: 11`
* *Defense:* `safety: 5`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` automation, browsers, memory, cgroup-v1, default, spec_helper, fs-extra, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/data-context/test/unit/sources/VersionsDataSource.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.34)
- **Top Global Matches:** file_cluster_10: 5.34, file_cluster_13: 6.524, file_cluster_2: 7.012
- **Magnitude:** 2536.22 | **LOC:** 334 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (92.5%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 55`, `args: 16`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `io: 2`, `concurrency: 28`, `import: 8`
* *Defense:* `safety: 3`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` src, sources, helper, globals, root, types, cross-fetch, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/test/lib/tasks/state.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.735)
- **Top Global Matches:** file_cluster_10: 5.735, file_cluster_2: 8.364, file_cluster_13: 8.719
- **Magnitude:** 2140.7 | **LOC:** 459 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (85.0%), Guard Balance (formerly Safety Score) (39.9%), Complexity Load (formerly Cognitive Load) (18.3%), Mutation Surface (formerly State Flux) (7.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 80`, `args: 62`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `io: 66`, `concurrency: 49`, `import: 13`
* *Defense:* `safety: 1`, `test: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` logger, state, util, debug, fs-extra, os, path, process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/app/src/specs/RunStatusDots.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.684)
- **Top Global Matches:** file_cluster_13: 4.684, file_cluster_10: 4.849, file_cluster_2: 5.403
- **Magnitude:** 1789.3 | **LOC:** 240 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.153; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.7%), Complexity Load (formerly Cognitive Load) (6.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 47`, `args: 14`, `func_start: 3`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `import: 14`
* *Defense:* `safety: 13`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000163
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/frontend-shared/src/components/Alert.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.358)
- **Top Global Matches:** file_cluster_13: 5.358, file_cluster_10: 5.915, file_cluster_2: 6.515
- **Magnitude:** 1219.48 | **LOC:** 201 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.153; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (49.4%), Guard Balance (formerly Safety Score) (48.5%), Complexity Load (formerly Cognitive Load) (7.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 22`, `args: 16`, `func_start: 2`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000163
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/test/integration/cypress_spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.868)
- **Top Global Matches:** file_cluster_10: 6.868, file_cluster_12: 9.161, file_cluster_15: 9.971
- **Magnitude:** 1167.92 | **LOC:** 2001 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (53.7%), Complexity Load (formerly Cognitive Load) (49.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectExitWithErr` **(Compute Cores)** (Impact: 6.8)
    * *Intent:* // returns error object
  * `ensureDoesNotExist` **(State Mutators)** (Impact: 3.8)
  * `mockEE` **(Callbacks & Closures)** (Impact: 3.1)
  * `snapshotConsoleLogs` **(Callbacks & Closures)** (Impact: 2.2)
  * `expectExitWith` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 129 instances
* *Concurrency (weighted view):* 788
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 340`, `args: 273`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 3`, `state_mutation: 321`, `planned_debt: 96`, `unreferenced_by_name: 6`
* *Architecture:* `io: 29`, `api: 2`, `concurrency: 143`, `import: 46`
* *Defense:* `safety: 6`, `doc: 3`, `test: 253`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` commit-info, electron-app, print-run, spec_helper, config, extension, browsers, detect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/src/cypress/runner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.031)
- **Top Global Matches:** file_cluster_12: 7.031, file_cluster_10: 8.797, file_cluster_15: 9.423
- **Magnitude:** 1125.52 | **LOC:** 2103 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 0.839; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%), Guard Balance (formerly Safety Score) (68.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onRunnableRun` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `maybeHandleRetryOnFailure` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `normalizeAll` **(Many-Argument Workhorses)** (Impact: 27.5)
  * `filterOnly` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // this follows how mocha filters onlys. its runner#filterOnly // is pretty much the same minus the ...
  * `pruneEmptySuites` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* // When in open mode and a "testFilter" is active, tests/suites that do not match the test filter //...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 146 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 343`, `args: 151`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 178`, `dead_code: 2`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `concurrency: 15`, `import: 11`
* *Defense:* `safety: 24`, `doc: 2`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.839
  * `Choke Point (Betweenness):` 0.000276 | `Ripple Effect (Closeness):` 0.009446
  * `Imports (Out-Degree: 6):` testConfigOverrides, error_utils, log, mocha, stack_utils, utils, types, bluebird...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/launcher/test/unit/windows.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.709)
- **Top Global Matches:** file_cluster_10: 6.709, file_cluster_12: 7.338, file_cluster_2: 8.478
- **Magnitude:** 1062.88 | **LOC:** 526 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.6%), Complexity Load (formerly Cognitive Load) (27.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 76`, `args: 46`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 16`
* *Architecture:* `io: 92`, `concurrency: 32`, `import: 10`
* *Defense:* `safety: 1`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` detect, known-browsers, windows, fixtures, types, fs-extra, lodash, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/frontend-shared/src/gql-components/CloudViewerAndProject.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.443)
- **Top Global Matches:** file_cluster_2: 4.443, file_cluster_17: 5.899, file_cluster_13: 5.973
- **Magnitude:** 968.23 | **LOC:** 189 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (78.8%), Complexity Load (formerly Cognitive Load) (29.7%), Guard Balance (formerly Safety Score) (26.2%), Mutation Surface (formerly State Flux) (17.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 2`, `import: 4`
* *Defense:* `safety: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/vite-dev-server/test/getVite.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.747)
- **Top Global Matches:** file_cluster_10: 4.747, file_cluster_2: 7.241, file_cluster_13: 7.786
- **Magnitude:** 967.77 | **LOC:** 267 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.3%), Guard Balance (formerly Safety Score) (45.3%), Complexity Load (formerly Cognitive Load) (8.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 69`, `args: 34`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `concurrency: 22`, `import: 2`
* *Defense:* `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` getVite, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/test/lib/cypress.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.701)
- **Top Global Matches:** file_cluster_10: 5.701, file_cluster_12: 8.13, file_cluster_2: 8.219
- **Magnitude:** 901.81 | **LOC:** 301 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.1%), Guard Balance (formerly Safety Score) (43.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Concurrency (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 64`, `args: 34`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `io: 9`, `concurrency: 55`, `import: 8`
* *Defense:* `safety: 3`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cypress, open, run, fs-extra, os, path, tmp, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/electron/test/open.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.462)
- **Top Global Matches:** file_cluster_10: 6.462, file_cluster_12: 8.234, file_cluster_13: 9.121
- **Magnitude:** 892.45 | **LOC:** 419 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.3%), Guard Balance (formerly Safety Score) (48.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 139
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 115`, `args: 78`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 5`, `state_mutation: 39`
* *Architecture:* `io: 11`, `concurrency: 34`, `import: 10`
* *Defense:* `safety: 7`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` open, paths, stderr-filtering, child_process, debug, fs-extra, inspector, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/test/lib/cli.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.151)
- **Top Global Matches:** file_cluster_10: 6.151, file_cluster_12: 9.15, file_cluster_2: 9.961
- **Magnitude:** 860.14 | **LOC:** 812 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.3%), Guard Balance (formerly Safety Score) (45.1%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sanitizePlatform` **(Callbacks & Closures)** (Impact: 1.9)
  * `exec` **(Callbacks & Closures)** (Impact: 1.8)
  * `replacePlatform` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* /** * Replaces line "Platform: ..." with "Platform: xxx" */
  * `replaceCypressVersion` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* /** * Replaces line "Cypress Version: ..." with "Cypress Version: 1.2.3" */
  * `flushPromises` **(Callbacks & Closures)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 112 instances
* *Concurrency (weighted view):* 746
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 257`, `args: 115`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 94`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `concurrency: 186`, `import: 14`
* *Defense:* `doc: 2`, `test: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` cli, info, open, run, logger, cache, install, state...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/app/src/pages/Debug.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.166)
- **Top Global Matches:** file_cluster_10: 5.166, file_cluster_13: 5.827, file_cluster_2: 5.89
- **Magnitude:** 858.65 | **LOC:** 115 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (31.2%), Mutation Surface (formerly State Flux) (27.9%), Complexity Load (formerly Cognitive Load) (24.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 16`, `args: 5`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `import: 9`
* *Defense:* `safety: 23`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/test/lib/exec/run.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.225)
- **Top Global Matches:** file_cluster_10: 5.225, file_cluster_2: 8.554, file_cluster_13: 8.638
- **Magnitude:** 747.74 | **LOC:** 243 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (48.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Concurrency (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 89`, `args: 53`, `func_start: 20`
* *Risk/State:* `state_mutation: 72`
* *Architecture:* `io: 8`, `concurrency: 39`, `import: 6`
* *Defense:* `safety: 2`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` run, spawn, verify, util, os, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/src/cy/keyboard.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.736)
- **Top Global Matches:** file_cluster_4: 5.736, file_cluster_15: 10.71, file_cluster_10: 10.749
- **Magnitude:** 730.26 | **LOC:** 1428 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 0.39; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%), Guard Balance (formerly Safety Score) (62.8%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fireSimulatedEvent` **(Many-Argument Workhorses)** (Impact: 60.0)
  * `simulatedKeydown` **(Many-Argument Workhorses)** (Impact: 43.8)
  * `shouldUpdateValue` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `validateTyping` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `type` **(Compute Cores)** (Impact: 32.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 92 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 208`, `args: 65`, `func_start: 48`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 99`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `api: 4`, `concurrency: 5`, `import: 15`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.39
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.006029
  * `Imports (Out-Degree: 16):` UsKeyboardLayout, error_utils, log, state, utils, dom, document, elements...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/scaffold-config/test/detect.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.551)
- **Top Global Matches:** file_cluster_10: 5.551, file_cluster_13: 8.169, file_cluster_2: 8.328
- **Magnitude:** 717.4 | **LOC:** 312 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.12; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (32.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 99`, `args: 35`, `func_start: 23`
* *Risk/State:* None
* *Architecture:* `io: 27`, `concurrency: 63`, `import: 7`
* *Defense:* `safety: 10`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000163
  * `Imports (Out-Degree: 3):` src, fixtures, scaffolding, system-tests, fs-extra, path, vitest
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/lib/modes/run.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.908)
- **Top Global Matches:** file_cluster_4: 6.908, file_cluster_12: 10.792, file_cluster_6: 11.486
- **Magnitude:** 707.06 | **LOC:** 1243 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **32**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (86.9%), Mutation Surface (formerly State Flux) (79.9%), Guard Balance (formerly Safety Score) (51.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `waitForTestsToFinishRunning` **(Defensive Guards)** (Impact: 60.7)
  * `runSpecs` **(Defensive Guards)** (Impact: 48.9)
  * `ready` **(Compute Cores)** (Impact: 35.4)
  * `runEachSpec` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `waitForBrowserToConnect` **(Defensive Guards)** (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 155
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 212`, `args: 65`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `io: 19`, `api: 8`, `concurrency: 90`, `import: 36`
* *Defense:* `safety: 47`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.001042
  * `Imports (Out-Degree: 21):` browsers, types, errors, open_project, run_events, project-base, reporter, chrome_policy_check...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/server/test/integration/http_requests_spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.372)
- **Top Global Matches:** file_cluster_10: 5.372, file_cluster_2: 8.989, file_cluster_12: 9.169
- **Magnitude:** 687.46 | **LOC:** 4923 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.107; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (42.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.7%), Complexity Load (formerly Cognitive Load) (16.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `pollUntilEventsIpcLoaded` **(Callbacks & Closures)** (Impact: 4.0)
  * `rp` **(Callbacks & Closures)** (Impact: 3.8)
    * *Intent:* // use a custom request promise // to automatically backfill these // options including our proxy
  * `setupProject` **(Callbacks & Closures)** (Impact: 3.1)
  * `onRequest` **(Callbacks & Closures)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 479
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 716`, `args: 598`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 62`, `planned_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `io: 24`, `api: 1`, `concurrency: 314`, `import: 32`
* *Defense:* `safety: 16`, `doc: 4`, `test: 737`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` spec_helper, request, request-promise, config, csp-header, system-tests, dep-installer, bluebird...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/app/src/components/promo/PromoHeader.cy.tsx` (TYPESCRIPT) | Magnitude: 3.62 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, args: 5, closures: 5
- `packages/launchpad/cypress/e2e/scaffold-project.cy.ts` (TYPESCRIPT) | Magnitude: 33.14 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 28, args: 21, closures: 16
- `packages/app/src/runs/RunTagCount.cy.tsx` (TYPESCRIPT) | Magnitude: 7.56 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 10, args: 9, core_var_decl: 8
- `packages/frontend-shared/src/components/Input.cy.tsx` (TYPESCRIPT) | Magnitude: 15.68 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, args: 8, closures: 8
- `packages/reporter/src/test/test.tsx` (TYPESCRIPT) | Magnitude: 20.04 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 24, core_var_decl: 22, ui_framework: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `system-tests/test/issue_5016_spec.js` (JAVASCRIPT) | Magnitude: 15.36 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, events: 2, listeners: 2, branch: 1
- `packages/app/src/specs/generators/ExpandableFileChooser.cy.tsx` (TYPESCRIPT) | Magnitude: 22.22 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 54, args: 39, closures: 38
- `packages/driver/test/unit/cy/commands/helpers/location.spec.ts` (TYPESCRIPT) | Magnitude: 69.74 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 72, args: 50, closures: 42
- `packages/app/src/specs/generators/GeneratorSuccess.cy.tsx` (TYPESCRIPT) | Magnitude: 15.92 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, args: 12, closures: 11
- `npm/vue/cypress/component/basic/plugins/plugin.cy.js` (JAVASCRIPT) | Magnitude: 15.9 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 35, test: 13, structural_boundaries: 11, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `system-tests/project-fixtures/angular/src/app/components/component-provider.component.ts` (TYPESCRIPT) | Magnitude: 5.96 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, api: 3, decorators: 3
- `system-tests/projects/angular-21/src/app/components/legacy/providers/component-provider.component.ts` (TYPESCRIPT) | Magnitude: 5.96 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, api: 3, decorators: 3
- `packages/server/lib/gui/menu.ts` (TYPESCRIPT) | Magnitude: 66.18 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 27, args: 14, func_start: 14
- `packages/data-context/src/util/DocumentNodeBuilder.ts` (TYPESCRIPT) | Magnitude: 63.92 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 147, branch: 15, structural_boundaries: 14, args: 11
- `packages/server/lib/makeDataContext.ts` (TYPESCRIPT) | Magnitude: 186.26 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 187, structural_boundaries: 77, args: 52, func_start: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/driver/cypress/e2e/e2e/origin/commands/querying_shadow.cy.ts` (TYPESCRIPT) | Magnitude: 17.78 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 12, args: 10, test: 10
- `packages/scaffold-config/test/component-index-template.spec.ts` (TYPESCRIPT) | Magnitude: 17.22 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 55, core_var_decl: 14, design_snake_case: 14, structural_boundaries: 9
- `system-tests/project-fixtures/react/src/Unmount.cy.jsx` (JAVASCRIPT) | Magnitude: 2.88 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, test: 14, structural_boundaries: 10, args: 8
- `packages/driver/cypress/e2e/cypress/utils.cy.js` (JAVASCRIPT) | Magnitude: 21.74 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 252, test: 95, args: 56, closures: 56
- `packages/server/test/unit/cloud/api/transform_error_spec.ts` (TYPESCRIPT) | Magnitude: 34.04 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 95, test: 26, structural_boundaries: 22, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/frontend-shared/src/components/InlineCodeFragment.vue` (HTML) | Magnitude: 54.35 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, core_var_decl: 5, design_snake_case: 4, structural_boundaries: 3
- `packages/reporter/tailwind.config.js` (JAVASCRIPT) | Magnitude: 18.46 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 2, io: 2, state_mutation: 2
- `packages/frontend-shared/src/components/transitions/TransitionGroupQuickFade.vue` (HTML) | Magnitude: 16.24 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, decorators: 6, class_start: 1, api: 1
- `packages/frontend-shared/src/components/transitions/TransitionQuickFade.vue` (HTML) | Magnitude: 16.24 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, decorators: 6, class_start: 1, api: 1
- `packages/driver/cypress/fixtures/global_parent_definition.html` (HTML) | Magnitude: 0.02 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 3, core_var_decl: 2, design_snake_case: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/driver/src/util/escape.ts` (TYPESCRIPT) | Magnitude: 25.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, args: 2, func_start: 2
- `packages/app/src/studio/StudioPanel.cy.tsx` (TYPESCRIPT) | Magnitude: 15.7 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 20, core_var_decl: 16, design_camel_case: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/server/lib/session.ts` (TYPESCRIPT) | Magnitude: 32.48 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, branch: 5, args: 5
- `packages/proxy/lib/network-proxy.ts` (TYPESCRIPT) | Magnitude: 59.62 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 19, args: 18, io: 18
- `packages/proxy/lib/http/util/prerequests.ts` (TYPESCRIPT) | Magnitude: 201.42 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 256, structural_boundaries: 53, branch: 40, state_mutation: 39
- `packages/launchpad/cypress/component/support/attachFileWithPath.ts` (TYPESCRIPT) | Magnitude: 6.7 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 6, io: 4, state_mutation: 3
- `packages/https-proxy/lib/ca.ts` (TYPESCRIPT) | Magnitude: 131.0 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 250, structural_boundaries: 51, io: 33, concurrency: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/server/lib/cloud/studio/StudioElectron.ts` (TYPESCRIPT) | Magnitude: 11.58 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 6, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/net-stubbing/lib/server/index.ts` (TYPESCRIPT) | Magnitude: 21.16 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 7, import: 7
- `packages/scaffold-config/src/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/stderr-filtering/lib/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `tooling/v8-snapshot/src/v8-snapshot.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/data-context/graphql/schemaTypes/objectTypes/index.ts` (TYPESCRIPT) | Magnitude: 52.72 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 36, api: 36, import: 36, concurrency: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `system-tests/projects/node-builtins/cypress/e2e/node_builtins.cy.js` (JAVASCRIPT) | Magnitude: 15.76 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: test: 37, import: 36, indent_spaces: 36, io: 9
- `packages/data-context/graphql/schemaTypes/objectTypes/gql-WizardBundler.ts` (TYPESCRIPT) | Magnitude: 11.0 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, api: 3, args: 2
- `system-tests/projects/ts-proj-with-paths/cypress.config.ts` (TYPESCRIPT) | Magnitude: 19.2 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 2, branch: 1, api: 1
- `packages/driver/cypress/fixtures/auth/cookie-login.html` (HTML) | Magnitude: 0.2 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 43, core_var_decl: 18, args: 11, design_snake_case: 10
- `packages/reporter/src/lib/switch.scss` (CSS) | Magnitude: 0.83 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 81, class_start: 14, closures: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/v8-snapshot-require/src/snapshot-require.ts` (TYPESCRIPT) | Magnitude: 105.14 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 32, branch: 30, core_var_decl: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/frontend-shared/src/gql-components/topnav/TopNavList.vue` (HTML) | Magnitude: 129.02 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 42, decorators: 13, core_var_decl: 10, design_snake_case: 10
- `packages/server/test/unit/util/commit-info_spec.ts` (TYPESCRIPT) | Magnitude: 58.2 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 196, structural_boundaries: 56, args: 33, closures: 31
- `packages/data-context/src/sources/BrowserDataSource.ts` (TYPESCRIPT) | Magnitude: 113.78 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 43, args: 21, concurrency: 14
- `packages/server/test/support/fixtures/cloud/studio/test-studio.ts` (TYPESCRIPT) | Magnitude: 0.03 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 25, concurrency: 14, args: 12
- `packages/frontend-shared/cypress/support/tab-until.ts` (TYPESCRIPT) | Magnitude: 16.62 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, args: 5, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/net-stubbing/lib/server/intercepted-request.ts` (TYPESCRIPT) | Magnitude: 157.42 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 53, branch: 36, state_mutation: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `system-tests/test/browser_path_spec.js` (JAVASCRIPT) | Magnitude: 11.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 19, args: 11, closures: 11
- `scripts/cypress.js` (JAVASCRIPT) | Magnitude: 17.68 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 8, core_var_decl: 7, design_snake_case: 6, state_mutation: 4
- `packages/driver/test/unit/cy/stability.spec.ts` (TYPESCRIPT) | Magnitude: 56.22 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 36, args: 20, closures: 20
- `system-tests/projects/e2e/cypress/e2e/websockets.cy.js` (JAVASCRIPT) | Magnitude: 36.84 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 20, args: 12, closures: 12
- `packages/network/test/unit/connect.spec.ts` (TYPESCRIPT) | Magnitude: 7.2 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 24, closures: 12, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/stderr-filtering/lib/FilterPrefixedContent.ts` (TYPESCRIPT) | Magnitude: 102.46 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, branch: 23, structural_boundaries: 22, concurrency: 9
- `packages/data-context/graphql/schemaTypes/objectTypes/gql-DevState.ts` (TYPESCRIPT) | Magnitude: 28.78 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 13, branch: 5, args: 4
- `npm/grep/cypress.config.ts` (TYPESCRIPT) | Magnitude: 22.44 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 11, io: 7, branch: 6
- `packages/proxy/lib/http/request-middleware.ts` (TYPESCRIPT) | Magnitude: 233.84 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 367, branch: 101, core_var_decl: 58, safety: 50
- `tooling/v8-snapshot/src/sourcemap/process-sourcemap.ts` (TYPESCRIPT) | Magnitude: 30.84 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 55, core_var_decl: 13, structural_boundaries: 10, branch: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cli/test/lib/tasks/state.spec.ts` -> **Cacie Prins** (100.0% isolated ownership) | Magnitude: 2140.7
- `packages/driver/src/cypress/runner.ts` -> **Ryan Manuel** (100.0% isolated ownership) | Magnitude: 1125.52
- `cli/test/lib/cypress.spec.ts` -> **Cacie Prins** (100.0% isolated ownership) | Magnitude: 901.81
- `cli/test/lib/exec/run.spec.ts` -> **Cacie Prins** (100.0% isolated ownership) | Magnitude: 747.74
- `packages/driver/src/cy/keyboard.ts` -> **Jennifer Shehane** (100.0% isolated ownership) | Magnitude: 730.26

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/server/lib/project-base.ts` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 97.3315%)
- `packages/driver/src/cypress.ts` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 99.6943%)
- `packages/driver/src/cypress/log.ts` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.6915%)
- `packages/driver/src/cypress/error_utils.ts` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 99.8958%)
- `packages/driver/src/cypress/cy.ts` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 99.7307%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `system-tests/lib/system-tests.ts` -> **Severity: 1.48** (Embedded: 0.0231 * Error Risk: 64.1447%)
- `packages/driver/types/cypress/log.d.ts` -> **Severity: 1.222** (Embedded: 0.0153 * Error Risk: 80.0%)
- `packages/driver/src/cypress/error_utils.ts` -> **Severity: 0.92** (Embedded: 0.0147 * Error Risk: 62.5679%)
- `packages/server/test/spec_helper.js` -> **Severity: 0.89** (Embedded: 0.0154 * Error Risk: 57.916%)
- `system-tests/lib/spec_helper.js` -> **Severity: 0.742** (Embedded: 0.0122 * Error Risk: 60.8809%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `system-tests/lib/system-tests.ts` -> **Severity: 1112.562** (Blast Radius: 11.727 * Doc Risk: 94.8718%)
- `system-tests/lib/fixtures.ts` -> **Severity: 626.175** (Blast Radius: 6.831 * Doc Risk: 91.6667%)
- `packages/driver/cypress/support/utils.ts` -> **Severity: 612.7** (Blast Radius: 6.127 * Doc Risk: 100.0%)
- `packages/server/test/spec_helper.js` -> **Severity: 501.9** (Blast Radius: 5.019 * Doc Risk: 100.0%)
- `packages/driver/src/dom/jquery.ts` -> **Severity: 403.7** (Blast Radius: 4.037 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1046 literal sites + 104 sites through wrappers = 1150
- **`panics_and_aborts`:** 1770 literal sites + 30 sites through wrappers = 1800

- `logInfo` (function, debug_prints, primitive): 44 call sites in 17 files -- `scripts/gulp/gulpfile.ts`
- `log` (function, debug_prints, primitive): 23 call sites in 1 files -- `scripts/binary/build.ts`
- `log` (function, debug_prints, primitive): 16 call sites in 1 files -- `system-tests/lib/dep-installer/index.ts`
- `log` (function, debug_prints, primitive): 10 call sites in 1 files -- `system-tests/lib/docker.ts`
- `cannotAccess` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `tooling/v8-snapshot/src/blueprint/globals-strict.js`
- `killAndExit` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `scripts/gulp/tasks/gulpCypress.ts`
- `throwKnownError` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/server/lib/task.js`
- `_handleErrors` (function, debug_prints, primitive): 2 call sites in 1 files -- `scripts/semantic-commits/validate-changelog.js`
- `_handleErrors` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `scripts/semantic-commits/validate-changelog.js`
- `_logWriteErr` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/server/lib/util/settings.ts`
- `log` (function, debug_prints, primitive): 2 call sites in 1 files -- `scripts/binary/index.js`
- `throwCloudCannotProceed` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/server/lib/modes/record.ts`
*(+14 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 28638 call pairs -- scoped 22.9%, unique 0.1%, ambiguous 27.0%, external 50.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 23564 | 25.2% | 0.0% | 28.2% | 46.6% |
| javascript | 4318 | 11.4% | 0.0% | 25.2% | 63.3% |
| html | 710 | 15.6% | 1.8% | 1.0% | 81.5% |
| shell | 46 | 0.0% | 0.0% | 0.0% | 100.0% |

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
