# ARCHITECTURAL_BRIEF: cypress
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cypress-io/cypress.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 6959 |
| Analyzed Artifacts (Scanned) | 6120 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 839 |
| Total LOC | 426294 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7403 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.195 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9284 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 457 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2413 | 252724 | 39.4% |
| JAVASCRIPT | 1822 | 113619 | 29.8% |
| HTML | 665 | 37983 | 10.9% |
| JSON | 344 | 15569 | 5.6% |
| MARKDOWN | 286 | 0 | 4.7% |
| XML | 246 | 30 | 4.0% |
| PLAINTEXT | 216 | 5 | 3.5% |
| CSS | 108 | 4897 | 1.8% |
| SHELL | 10 | 296 | 0.2% |
| YAML | 6 | 1160 | 0.1% |
| CSV | 4 | 11 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.19; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 46%, Declarative / Non-Code 23%, Callbacks & Closures Files 13%, Large Core Modules 5%, Interface Declarations Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5606 | 91.6% |
| Unknown | 5 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 497 | 8.1% |
| Static: Minified & Vendor Opaque Mass | 12 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 839*

**Composition by Extension & Reason:**
- `.ansi`: 156x Excluded (Unsupported Extension: '.ansi')
- `.lock`: 121x Excluded (Unsupported Extension: '.lock')
- `no_extension`: 112x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.png`: 80x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Massive Static Asset Blob: 5877 LOC), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.vue`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Saturation: Line 25 exceeds 500 chars)
- `.patch`: 30x Excluded (Unsupported Extension: '.patch')
- `.yml`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2869 LOC), 1x Zero-Density Threshold (LOC: 99, Signals: 0)
- `.coffee`: 25x Excluded (Unsupported Extension: '.coffee')
- `.js`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 15 LOC), 1x Excluded (Saturation: Line 40 exceeds 500 chars)
- `.snap`: 24x Excluded (Unsupported Extension: '.snap')
- `.tsx`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 23 LOC), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.md`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 46 LOC), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `.ts`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 257 LOC)
- `.ico`: 12x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 25.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 17.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 50.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.1 | 1.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 53.4 | 2.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 36.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1668 | 532 | 0 | `cli/types/cypress.d.ts` |
| cleanup | 327 | 159 | 0 | `packages/server/lib/browsers/browser-cri-client.ts` |
| guards | 26768 | 1585 | 5 | `system-tests/__snapshots__/record_spec.js` |
| danger | 7960 | 1523 | 3 | `system-tests/__snapshots__/protocol_spec.js` |
| concurrency | 16307 | 1357 | 6 | `cli/types/cypress.d.ts` |
| connectivity | 8502 | 2500 | 4 | `packages/driver/cypress/fixtures/dom.html` |
| io | 15141 | 1322 | 4 | `system-tests/projects/e2e/elements.html` |
| crypto | 11 | 9 | 0 | `scripts/binary/binary-sources.js` |
| ipc | 167 | 103 | 0 | `packages/extension/test/integration/v3/content.spec.ts` |
| time | 818 | 326 | 0 | `packages/driver/cypress/e2e/cy/timers.cy.js` |
| serialization | 485 | 266 | 0 | `packages/driver/cypress/e2e/commands/net_stubbing.cy.ts` |
| regex | 1092 | 400 | 0 | `packages/server/test/integration/http_requests_spec.js` |
| events | 13065 | 1385 | 4 | `packages/driver/cypress/e2e/commands/navigation.cy.js` |
| tests | 50749 | 2074 | 15 | `system-tests/__snapshots__/protocol_spec.js` |
| docs | 2724 | 801 | 1 | `cli/types/cypress.d.ts` |
| debt | 6054 | 1015 | 2 | `system-tests/__snapshots__/record_spec.js` |
| mutation | 57897 | 3665 | 24 | `system-tests/projects/e2e/elements.html` |
| dead_code | 1917 | 795 | 1 | `packages/errors/test/visualSnapshotErrors.spec.ts` |
| credential | 98 | 22 | 0 | `packages/app/cypress/fixtures/debug-Passing/gql-Debug.json` |
| threat | 1416 | 346 | 0 | `packages/driver/cypress/fixtures/visibility/overflow.html` |
| ml_ai | 231 | 75 | 0 | `packages/server/test/support/fixtures/server/err_response.html` |
| ui | 4635 | 901 | 2 | `system-tests/projects/e2e/elements.html` |

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

1. **lodash.ts** (`packages/driver/src/config/lodash.ts`) — 409 inbound connections
2. **react.svg** (`packages/frontend-shared/src/assets/logos/react.svg`) — 313 inbound connections
3. **debug.js** (`scripts/debug.js`) — 292 inbound connections
4. **system-tests.ts** (`system-tests/lib/system-tests.ts`) — 181 inbound connections
5. **vue.svg** (`packages/frontend-shared/src/assets/logos/vue.svg`) — 140 inbound connections

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
  * *Intent:* /** * Add one or more custom commands that validate their prevSubject * @see https://on.cypress.io/api/commands#Validations */
- `startListening` **(Many-Argument Workhorses)** (@ `packages/server/lib/socket-base.ts`) -> Impact: **265.3** | LOC: 603
- `click` **(Tests & Verification)** (@ `packages/driver/cypress/e2e/commands/actions/click.cy.ts`) -> Impact: **220.0** | LOC: 2639
- `type` **(Many-Argument Workhorses)** (@ `packages/driver/src/cy/commands/actions/type.ts`) -> Impact: **206.8** | LOC: 575
- `expectValidationFails` **(Callbacks & Closures)** (@ `packages/server/test/unit/config_spec.js`) -> Impact: **201.4** | LOC: 804
- `action` **(Many-Argument Workhorses)** (@ `packages/driver/src/cypress.ts`) -> Impact: **174.2** | LOC: 366
- `collectLogs` **(Many-Argument Workhorses)** (@ `packages/driver/cypress/e2e/commands/querying/querying.cy.ts`) -> Impact: **169.2** | LOC: 1201
- `create` **(Compute Cores)** (@ `packages/driver/src/cy/chai/inspect.ts`) -> Impact: **159.0** | LOC: 437
  * *Intent:* // let config = require('../config')
- `res` **(Defensive Guards)** (@ `system-tests/test/record_spec.js`) -> Impact: **158.1** | LOC: 356
- `origin` **(Many-Argument Workhorses)** (@ `cli/types/cypress.d.ts`) -> Impact: **153.7** | LOC: 753
  * *Intent:* /** * Enables running Cypress commands in a secondary origin. * @see https://on.cypress.io/origin * @example * cy.origin('example.com', () => { * cy.g...

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Tests & Verification**: assertion-heavy test or verification function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cli/test/lib` | 6 | 7554.4 | 24.04% | 0.0% |
| `packages/driver/src/cypress` | 35 | 6025.24 | 37.86% | 7.4% |
| `packages/data-context/test/unit/sources` | 13 | 6000.29 | 49.55% | 0.0% |
| `packages/frontend-shared/src/components` | 56 | 5632.27 | 5.87% | 4.29% |
| `npm/webpack-preprocessor` | 12 | 5263.18 | 3.46% | 1.51% |
| `__monolith__` | 22 | 5230.44 | 0.2% | 0.0% |
| `cli` | 13 | 5157.94 | 1.31% | 0.0% |
| `npm/vue` | 12 | 5110.08 | 1.28% | 0.0% |
| `npm/svelte` | 9 | 5050.62 | 0.57% | 0.0% |
| `packages/driver/cypress/e2e/commands` | 26 | 4976.12 | 33.3% | 23.18% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `npm/vue/cypress/component/basic/slots/Card.cy.js` -> **100.0%** Exposure
- `packages/frontend-shared/cypress/fixtures/dummy-protocol.js` -> **100.0%** Exposure
- `system-tests/__snapshots__/before_all_after_all_throws_spec.ts.js` -> **100.0%** Exposure
- `system-tests/__snapshots__/cy_origin_retries_spec.ts.js` -> **100.0%** Exposure
- `system-tests/__snapshots__/fails_prior_to_top_change_retry_succeeds_spec.ts.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `__snapshots__/utils-spec.js` -> **100.0%** Exposure
- `npm/react/cypress/component/advanced/tutorial/tic-tac-toe.jsx` -> **100.0%** Exposure
- `npm/react/cypress/component/basic/react-tutorial/game.jsx` -> **100.0%** Exposure
- `packages/driver/cypress/e2e/util/limited_map.cy.js` -> **100.0%** Exposure
- `packages/extension/test/helpers/background.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/errors/test/visualSnapshotErrors.spec.ts` -> **134** Orphaned Functions | **0** Duplicates
- `packages/proxy/test/unit/http/response-middleware.spec.ts` -> **4** Orphaned Functions | **63** Duplicates
- `packages/driver/cypress/e2e/commands/assertions.cy.js` -> **3** Orphaned Functions | **27** Duplicates
- `packages/telemetry/test/span-exporters/cloud-span-exporter.spec.ts` -> **0** Orphaned Functions | **27** Duplicates
- `packages/proxy/test/unit/http/request-middleware.spec.ts` -> **2** Orphaned Functions | **23** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/https-proxy/test/unit/ca.spec.ts` -> **99.9999%** Exposure
- `packages/https-proxy/test/integration/proxy.spec.ts` -> **99.9809%** Exposure
- `packages/server/test/unit/cache_spec.ts` -> **85.9083%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6443` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/server/lib/project-base.ts` (TYPESCRIPT) -> Cumulative Risk: **764.06**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.00)
- **Magnitude:** 528.34 | **LOC:** 808 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9991%), State Flux (97.3315%)
- **Heaviest Functions:** `startWebsockets` (Defensive Guards, Impact: 72.9), `endTelemetry` (Defensive Guards, Impact: 26.3), `getConfig` (Defensive Guards, Impact: 21.4)

### 2. `packages/driver/src/cy/stability.ts` (TYPESCRIPT) -> Cumulative Risk: **742.98**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -1.04)
- **Magnitude:** 63.6 | **LOC:** 79 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.8274%)
- **Heaviest Functions:** `isStable` (Callbacks & Closures, Impact: 8.8), `create` (Callbacks & Closures, Impact: 5.6), `whenStable` (Callbacks & Closures, Impact: 3.7)

### 3. `packages/frontend-shared/cypress/e2e/e2ePluginSetup.ts` (TYPESCRIPT) -> Cumulative Risk: **738.54**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.88)
- **Magnitude:** 486.94 | **LOC:** 565 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.8482%), Documentation (90.9091%)
- **Heaviest Functions:** `makeE2ETasks` (Compute Cores, Impact: 78.8), `__internal__beforeEach` (Defensive Guards, Impact: 39.6), `__internal_withCtx` (Defensive Guards, Impact: 16.4)

### 4. `packages/server/lib/open_project.ts` (TYPESCRIPT) -> Cumulative Risk: **738.34**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.65)
- **Magnitude:** 278.3 | **LOC:** 376 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9995%), State Flux (98.7196%), Documentation (95.4545%)
- **Heaviest Functions:** `launch` (Many-Argument Workhorses, Impact: 57.0), `create` (Many-Argument Workhorses, Impact: 23.1), `onReloadBrowser` (I/O & Config Routines, Impact: 12.7)

### 5. `system-tests/lib/system-tests.ts` (TYPESCRIPT) -> Cumulative Risk: **730.06**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.71)
- **Magnitude:** 593.58 | **LOC:** 1066 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9988%), Documentation (95.0%), Concurrency (92.3555%)
- **Heaviest Functions:** `exec` (Many-Argument Workhorses, Impact: 83.2), `args` (Compute Cores, Impact: 42.1), `exit` (Compute Cores, Impact: 41.3)

### 6. `packages/server/lib/controllers/xhrs.ts` (TYPESCRIPT) -> Cumulative Risk: **720.04**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.70)
- **Magnitude:** 106.74 | **LOC:** 119 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.1242%)
- **Heaviest Functions:** `handle` (Many-Argument Workhorses, Impact: 25.5), `respond` (I/O & Config Routines, Impact: 10.7), `_get` (Compute Cores, Impact: 7.9)

### 7. `packages/driver/src/cy/retries.ts` (TYPESCRIPT) -> Cumulative Risk: **713.05**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.05)
- **Magnitude:** 101.22 | **LOC:** 174 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.6617%), Concurrency (93.7373%)
- **Heaviest Functions:** `retry` (Many-Argument Workhorses, Impact: 47.9), `ended` (I/O & Config Routines, Impact: 7.1), `create` (Parameter Forwarders, Impact: 5.3)

### 8. `packages/driver/src/cy/commands/actions/scroll.ts` (TYPESCRIPT) -> Cumulative Risk: **712.8**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.08)
- **Magnitude:** 330.6 | **LOC:** 422 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (94.9999%)
- **Heaviest Functions:** `scrollTo` (Many-Argument Workhorses, Impact: 113.1), `scrollIntoView` (Many-Argument Workhorses, Impact: 23.1), `ensureScrollability` (I/O & Config Routines, Impact: 12.7)

### 9. `packages/driver/src/cy/net-stubbing/events/before-request.ts` (TYPESCRIPT) -> Cumulative Risk: **710.22**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.04)
- **Magnitude:** 194.72 | **LOC:** 363 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8532%), State Flux (99.6732%)
- **Heaviest Functions:** `finish` (Defensive Guards, Impact: 21.3), `reply` (Many-Argument Workhorses, Impact: 19.8), `continue` (Compute Cores, Impact: 9.7)

### 10. `packages/server/lib/socket-base.ts` (TYPESCRIPT) -> Cumulative Risk: **709.2**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.43)
- **Magnitude:** 617.34 | **LOC:** 798 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Concurrency (99.9714%), Spec Match (98.5294%), Documentation (94.5205%), Cognitive Load (80.5741%)
- **Heaviest Functions:** `startListening` (Many-Argument Workhorses, Impact: 265.3), `backendRequest` (Defensive Guards, Impact: 52.1), `getFixture` (Defensive Guards, Impact: 31.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4983.17 | **LOC:** 723 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.8562%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 186`, `args: 110`, `func_start: 20`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`
* *Architecture:* `io: 4`, `concurrency: 52`, `import: 19`
* *Defense:* `safety: 22`, `test: 176`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` logger, util, assert, hasha, os, systeminformation, tty, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/test/unit/browsers/memory/memory_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3629.89 | **LOC:** 731 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5631%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 82`, `args: 31`, `func_start: 20`
* *Risk/State:* `state_mutation: 10`, `planned_debt: 93`
* *Architecture:* `io: 7`, `concurrency: 62`, `import: 11`
* *Defense:* `safety: 5`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` automation, browsers, memory, cgroup-v1, default, spec_helper, fs-extra, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/test/lib/tasks/state.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2698.31 | **LOC:** 459 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (19.8244%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 80`, `args: 62`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `io: 66`, `concurrency: 49`, `import: 13`
* *Defense:* `safety: 1`, `test: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` logger, state, util, debug, fs-extra, os, path, process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/data-context/test/unit/sources/VersionsDataSource.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2618.68 | **LOC:** 334 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.9652%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 55`, `args: 16`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `io: 2`, `concurrency: 28`, `import: 8`
* *Defense:* `safety: 3`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` src, sources, helper, globals, root, types, cross-fetch, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/test/unit/browsers/browser-cri-client_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2164.39 | **LOC:** 810 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (92.477%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 192
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 100`, `args: 56`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 44`, `planned_debt: 69`
* *Architecture:* `io: 32`, `concurrency: 77`, `import: 9`
* *Defense:* `safety: 20`, `test: 130`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` browser-cri-client, cri-client, protocol, spec_helper, errors, service-worker-manager, types, devtools-protocol...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/app/src/specs/RunStatusDots.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1944.22 | **LOC:** 240 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8429%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 47`, `args: 14`, `func_start: 3`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `import: 14`
* *Defense:* `safety: 13`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000163
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/launcher/test/unit/windows.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1752.45 | **LOC:** 526 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.8352%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 76`, `args: 46`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 16`
* *Architecture:* `io: 92`, `concurrency: 32`, `import: 10`
* *Defense:* `safety: 1`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` detect, known-browsers, windows, fixtures, types, fs-extra, lodash, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/frontend-shared/src/components/Alert.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1384.4 | **LOC:** 201 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.1788%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 22`, `args: 16`, `func_start: 2`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000163
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/test/integration/cypress_spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1285.12 | **LOC:** 2001 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.0665%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expectExitWithErr` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* // returns error object
  * `ensureDoesNotExist` **(State Mutators)** (Impact: 3.8)
  * `mockEE` **(Callbacks & Closures)** (Impact: 3.1)
  * `snapshotConsoleLogs` **(Callbacks & Closures)** (Impact: 2.2)
  * `expectExitWith` **(Callbacks & Closures)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 129 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 788
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 340`, `args: 273`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 3`, `state_mutation: 321`, `dead_code: 2`, `planned_debt: 96`, `unreferenced_by_name: 6`
* *Architecture:* `io: 29`, `api: 2`, `concurrency: 143`, `import: 46`
* *Defense:* `safety: 6`, `doc: 3`, `test: 253`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` commit-info, electron-app, print-run, spec_helper, config, extension, browsers, detect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/data-context/test/unit/codegen/spec-options.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1280.01 | **LOC:** 350 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.5165%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 65`, `args: 33`, `func_start: 13`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 2`
* *Architecture:* `io: 31`, `concurrency: 44`, `import: 8`
* *Defense:* `doc: 2`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` src, spec-options, helper, globals, config, scaffold-config, fs-extra, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/test/lib/exec/run.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1278.14 | **LOC:** 243 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (49.9999%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 209
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 89`, `args: 53`, `func_start: 20`
* *Risk/State:* `state_mutation: 72`
* *Architecture:* `io: 8`, `concurrency: 39`, `import: 6`
* *Defense:* `safety: 2`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` run, spawn, verify, util, os, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/src/cypress/runner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1241.52 | **LOC:** 2103 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.7605%), Tech Debt (9.8999%)
**Top Internal Functions/Classes:**
  * `onRunnableRun` **(Many-Argument Workhorses)** (Impact: 59.5)
  * `handleSuiteEnd` **(I/O & Config Routines)** (Impact: 37.3)
  * `case` **(Compute Cores)** (Impact: 36.6)
  * `maybeHandleRetryOnFailure` **(Compute Cores)** (Impact: 32.8)
  * `suiteHasOnlyId` **(Compute Cores)** (Impact: 30.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 147 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 472
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 343`, `args: 151`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 178`, `dead_code: 37`, `planned_debt: 7`
* *Architecture:* `api: 20`, `concurrency: 15`, `import: 11`
* *Defense:* `safety: 24`, `doc: 2`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000588
  * `Imports (Out-Degree: 7):` testConfigOverrides, error_utils, log, mocha, stack_utils, utils, types, bluebird...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cli/test/lib/cypress.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1138.45 | **LOC:** 301 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.1425%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Concurrency (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 64`, `args: 34`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `io: 9`, `concurrency: 55`, `import: 8`
* *Defense:* `safety: 3`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cypress, open, run, fs-extra, os, path, tmp, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/frontend-shared/src/gql-components/CloudViewerAndProject.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1106.79 | **LOC:** 189 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.5498%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 2`, `import: 4`
* *Defense:* `safety: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/test/unit/cy/commands/location.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1052.35 | **LOC:** 445 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.8918%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 69`, `args: 44`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 3`
* *Architecture:* `io: 38`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 5`, `doc: 1`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` location, location, cy, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/electron/test/open.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 985.33 | **LOC:** 419 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (48.426%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 139
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 115`, `args: 78`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 5`, `state_mutation: 39`
* *Architecture:* `io: 11`, `concurrency: 34`, `import: 10`
* *Defense:* `safety: 7`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` open, paths, stderr-filtering, child_process, debug, fs-extra, inspector, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/data-context/test/unit/sources/CloudDataSource.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 978.6 | **LOC:** 352 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.3727%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 58`, `args: 31`, `func_start: 10`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 4`, `concurrency: 34`, `import: 8`
* *Defense:* `safety: 9`, `test: 54`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DataContext, sources, helper, graphqlFixtures, globals, core, cross-fetch, graphql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/test/integration/http_requests_spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 978.16 | **LOC:** 4923 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (18.0939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `matches` **(Many-Argument Workhorses)** (Impact: 150.5)
  * `write` **(Tests & Verification)** (Impact: 86.2)
  * `onmessage` **(Tests & Verification)** (Impact: 21.8)
  * `use` **(Tests & Verification)** (Impact: 19.1)
  * `setup` **(Many-Argument Workhorses)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 484
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 716`, `args: 598`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 62`, `dead_code: 4`, `planned_debt: 6`, `unreferenced_by_name: 7`
* *Architecture:* `io: 24`, `concurrency: 314`, `import: 32`
* *Defense:* `safety: 16`, `doc: 4`, `test: 737`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` spec_helper, request, request-promise, config, csp-header, resolve-dist, system-tests, dep-installer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/vite-dev-server/test/getVite.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 967.77 | **LOC:** 267 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.3867%), Tech Debt (0.0%)
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

### `packages/app/cypress/e2e/subscriptions/specChange-subscription.cy.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 895.79 | **LOC:** 495 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.8476%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 68`, `args: 41`, `func_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 28`, `api: 4`, `concurrency: 40`, `import: 2`
* *Defense:* `safety: 1`, `doc: 7`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` paths, en-US.json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/app/src/runner/event-manager.ts` -> Churn: **53.42%** | Cog Load: 53.4201% | Debt: 14.4446%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cli/test/lib/util.spec.ts` -> **Bill Glesias** (100.0% isolated ownership) | Magnitude: 4983.17
- `packages/data-context/test/unit/sources/VersionsDataSource.spec.ts` -> **Bill Glesias** (100.0% isolated ownership) | Magnitude: 2618.68
- `packages/launcher/test/unit/windows.spec.ts` -> **Bill Glesias** (100.0% isolated ownership) | Magnitude: 1752.45
- `packages/data-context/test/unit/codegen/spec-options.spec.ts` -> **Bill Glesias** (100.0% isolated ownership) | Magnitude: 1280.01
- `packages/driver/src/cypress/runner.ts` -> **Ryan Manuel** (100.0% isolated ownership) | Magnitude: 1241.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/driver/src/cy/chai.ts` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 99.7679%)
- `packages/driver/src/cypress/cy.ts` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.702%)
- `packages/driver/src/cypress/error_utils.ts` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9248%)
- `packages/server/lib/project-base.ts` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 97.3315%)
- `system-tests/lib/system-tests.ts` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 99.9988%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scripts/debug.js` -> **Severity: 6.63** (Embedded: 0.0881 * Error Risk: 75.2927%)
- `packages/server/lib/util/child_process.js` -> **Severity: 4.338** (Embedded: 0.0672 * Error Risk: 64.5656%)
- `packages/server/lib/util/fs.ts` -> **Severity: 2.889** (Embedded: 0.0346 * Error Risk: 83.6037%)
- `system-tests/lib/system-tests.ts` -> **Severity: 2.498** (Embedded: 0.0291 * Error Risk: 85.9631%)
- `packages/driver/src/cypress/error_utils.ts` -> **Severity: 1.67** (Embedded: 0.0197 * Error Risk: 84.8329%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/debug.js` -> **Severity: 1396.7** (Blast Radius: 27.934 * Doc Risk: 50.0%)
- `system-tests/lib/system-tests.ts` -> **Severity: 1238.42** (Blast Radius: 13.036 * Doc Risk: 95.0%)
- `packages/server/lib/util/fs.ts` -> **Severity: 1090.0** (Blast Radius: 10.9 * Doc Risk: 100.0%)
- `packages/rewriter/lib/js.ts` -> **Severity: 701.1** (Blast Radius: 7.011 * Doc Risk: 100.0%)
- `packages/app/src/graphql.ts` -> **Severity: 420.4** (Blast Radius: 4.204 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
