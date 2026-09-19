# ARCHITECTURAL_BRIEF: @mergeapi_merge-node-client
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 6208 analyzed artifact(s), 60638 LOC.
- **Load-bearing artifact:** `package/api/index.js` -- 1823 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/api/resources/accounting/types/index.d.ts` -- pulls in 601 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/core/pagination/Page.js` at magnitude 127.76 (structural weight, not risk).
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
| Total Artifacts | 10921 |
| Analyzed Artifacts (Scanned) | 6208 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4713 |
| Total LOC | 60638 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 56.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2608 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6328 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4964 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 28 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 5434 | 46525 | 87.5% |
| JAVASCRIPT | 771 | 14113 | 12.4% |
| MARKDOWN | 2 | 0 | 0.0% |
| PLAINTEXT | 1 | 0 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `5.148`
> **Composition Archetype:** `Mid Flat Project` (z +5.15; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 51%, Declarative / Non-Code 45%, Generic / Templated Code Files 2%, State Mutators Files 1%, Callbacks & Closures Files 0%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6205 | 100.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4713*

**Composition by Extension & Reason:**
- `.js`: 1727x Excluded (Machine-Generated Source Code Signature: 4 LOC), 641x Excluded (Machine-Generated Source Code Signature: 41 LOC), 295x Excluded (Machine-Generated Source Code Signature: 40 LOC)
- `.ts`: 11x Excluded (Saturation: Line 6 exceeds 500 chars), 6x Excluded (Saturation: Line 17 exceeds 500 chars), 6x Excluded (Saturation: Line 14 exceeds 500 chars)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 134 LOC), 1x Excluded (Monolithic Amalgamation: 38958 LOC exceeds safe regex boundaries)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.0 | 9.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.7 | 3.5 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3417 | 3411 | 1 | `package/index.d.ts` |
| cleanup | 4 | 4 | 0 | `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.d.ts` |
| guards | 6549 | 1306 | 3 | `package/api/resources/accounting/types/TransactionCurrencyEnum.d.ts` |
| danger | 166 | 81 | 0 | `package/core/schemas/builders/union/types.d.ts` |
| concurrency | 243 | 136 | 0 | `package/core/pagination/Page.js` |
| connectivity | 12915 | 5499 | 2 | `package/api/resources/accounting/types/index.d.ts` |
| io | 51 | 44 | 0 | `package/core/fetcher/getFetchFn.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `package/core/fetcher/signals.d.ts` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `package/core/fetcher/getErrorResponseBody.js` |
| events | 8 | 8 | 0 | `package/api/resources/ticketing/types/Permission.d.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 6321 | 1539 | 2 | `package/api/resources/ticketing/resources/tickets/client/requests/TicketsListRequest.d.ts` |
| debt | 161 | 145 | 0 | `package/core/logging/logger.d.ts` |
| mutation | 8769 | 3086 | 8 | `package/api/resources/filestorage/resources/index.js` |
| dead_code | 852 | 259 | 0 | `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 3129 | 771 | 4 | `package/index.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 1 | 1 | 0 | `package/core/schemas/builders/schema-utils/getSchemaUtils.d.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/core/fetcher/getFetchFn.js` (Hits: 5)
- `package/environments.d.ts` (Hits: 3)
- `package/BaseClient.d.ts` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`package/api/index.js`) — 1823 inbound connections
2. **index.js** (`package/core/schemas/builders/schema-utils/index.js`) — 16 inbound connections
3. **index.js** (`package/core/schemas/builders/object-like/index.js`) — 5 inbound connections
4. **chooseStreamWrapper.js** (`package/core/fetcher/stream-wrappers/chooseStreamWrapper.js`) — 4 inbound connections
5. **index.js** (`package/core/schemas/builders/object/index.js`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.d.ts** (`package/api/resources/accounting/types/index.d.ts`) — 601 outbound dependencies
2. **index.d.ts** (`package/serialization/resources/accounting/types/index.d.ts`) — 601 outbound dependencies
3. **index.d.ts** (`package/api/resources/crm/types/index.d.ts`) — 224 outbound dependencies
4. **index.d.ts** (`package/serialization/resources/crm/types/index.d.ts`) — 224 outbound dependencies
5. **index.d.ts** (`package/api/resources/ats/types/index.d.ts`) — 220 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getErrorResponseBody` **(Defensive Guards)** (@ `package/core/fetcher/getErrorResponseBody.js`) -> Impact: **32.7** | LOC: 31
- `chooseStreamWrapper` **(Defensive Guards)** (@ `package/core/fetcher/stream-wrappers/chooseStreamWrapper.js`) -> Impact: **12.0** | LOC: 13
- `getFetchFn` **(Defensive Guards)** (@ `package/core/fetcher/getFetchFn.js`) -> Impact: **8.9** | LOC: 19
  * *Intent:* /** * Returns a fetch function based on the runtime */
- `customObjectClassesCustomObjectsAssociationsUpdate` **(Generic / Templated Code)** (@ `package/api/resources/crm/resources/associations/client/Client.d.ts`) -> Impact: **8.5** | LOC: 1
  * *Intent:* * * await client.crm.associations.customObjectClassesCustomObjectsAssociationsUpdate("source_class_id", "source_object_id", "target_class_id", "target...
- `constructor` **(Compute Cores)** (@ `package/errors/MergeError.d.ts`) -> Impact: **7.4** | LOC: 6
- `verb` **(Compute Cores)** (@ `package/core/pagination/Page.js`) -> Impact: **7.0** | LOC: 1
- `_a` **(Defensive Guards)** (@ `package/core/pagination/Page.js`) -> Impact: **6.9** | LOC: 18
- `customObjectClassesAssociationTypesRetrieve` **(Generic / Templated Code)** (@ `package/api/resources/crm/resources/associationTypes/client/Client.d.ts`) -> Impact: **6.8** | LOC: 1
  * *Intent:* /** * Returns an `AssociationType` object with the given `id`. * * * await client.crm.associationTypes.customObjectClassesAssociationTypesRetrieve("cu...
- `customObjectClassesCustomObjectsAssociationsList` **(Generic / Templated Code)** (@ `package/api/resources/crm/resources/associations/client/Client.d.ts`) -> Impact: **6.8** | LOC: 1
  * *Intent:* * await client.crm.associations.customObjectClassesCustomObjectsAssociationsList("custom_object_class_id", "object_id", { * associationTypeId: "associ...
- `customObjectClassesCustomObjectsRetrieve` **(Generic / Templated Code)** (@ `package/api/resources/crm/resources/customObjects/client/Client.d.ts`) -> Impact: **6.8** | LOC: 1
  * *Intent:* * Returns a `CustomObject` object with the given `id`. * * * await client.crm.customObjects.customObjectClassesCustomObjectsRetrieve("custom_object_cl...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/serialization/resources/accounting/types` | 599 | 525.7 | 2.59% | 0.0% |
| `package/api/resources/accounting/types` | 602 | 432.21 | 1.66% | 10.21% |
| `package/serialization/resources/crm/types` | 223 | 197.66 | 3.11% | 0.0% |
| `package/core/fetcher` | 24 | 196.02 | 14.35% | 30.26% |
| `package/serialization/resources/ats/types` | 220 | 193.76 | 2.87% | 0.0% |
| `package/serialization/resources/hris/types` | 199 | 174.82 | 2.84% | 0.0% |
| `package/api/resources/crm/types` | 225 | 169.05 | 2.25% | 3.47% |
| `package/api/resources/ats/types` | 221 | 165.7 | 2.06% | 0.61% |
| `package/serialization/resources/ticketing/types` | 177 | 156.08 | 2.92% | 0.0% |
| `package/api/resources/hris/types` | 202 | 152.84 | 2.05% | 0.99% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/api/resources/accounting/resources/expenses/client/Client.d.ts` -> **100.0%** Exposure
- `package/api/resources/accounting/resources/invoices/client/Client.d.ts` -> **100.0%** Exposure
- `package/api/resources/accounting/resources/itemFulfillments/client/Client.d.ts` -> **100.0%** Exposure
- `package/api/resources/accounting/resources/payments/client/Client.d.ts` -> **100.0%** Exposure
- `package/api/resources/accounting/resources/salesOrders/client/Client.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/api/resources/filestorage/resources/index.js` -> **100.0%** Exposure
- `package/api/resources/index.js` -> **100.0%** Exposure
- `package/core/fetcher/getFetchFn.js` -> **100.0%** Exposure
- `package/core/fetcher/stream-wrappers/chooseStreamWrapper.js` -> **100.0%** Exposure
- `package/core/index.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/core/logging/logger.d.ts` -> **7** Orphaned Functions | **12** Duplicates
- `package/core/fetcher/stream-wrappers/Node18UniversalStreamWrapper.d.ts` -> **15** Orphaned Functions | **0** Duplicates
- `package/core/fetcher/stream-wrappers/NodePre18StreamWrapper.d.ts` -> **15** Orphaned Functions | **0** Duplicates
- `package/core/fetcher/stream-wrappers/UndiciStreamWrapper.d.ts` -> **15** Orphaned Functions | **0** Duplicates
- `package/core/fetcher/stream-wrappers/chooseStreamWrapper.d.ts` -> **15** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `106` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/core/pagination/Page.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 127.76 | **LOC:** 102 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.325; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (77.6%), Complexity Load (formerly Cognitive Load) (65.7%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verb` **(Compute Cores)** (Impact: 7.0)
  * `_a` **(Defensive Guards)** (Impact: 6.9)
  * `iterMessages` **(Interface Declarations)** (Impact: 4.7)
  * `iterMessages_1` **(Interface Declarations)** (Impact: 4.5)
  * `settle` **(Compute Cores)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 38`, `args: 34`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`
* *Architecture:* `api: 5`, `concurrency: 10`
* *Defense:* `safety: 18`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000457
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/api/resources/filestorage/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 98.76 | **LOC:** 84 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`
* *Architecture:* `api: 44`, `import: 44`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` accountDetails, accountToken, asyncPassthrough, types, auditTrail, requests, availableActions, deleteAccount...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ats/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 92.76 | **LOC:** 84 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`
* *Architecture:* `api: 40`, `import: 44`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` activities, requests, types, applications, requests, types, asyncPassthrough, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/hris/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 92.74 | **LOC:** 83 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`
* *Architecture:* `api: 40`, `import: 43`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncPassthrough, types, bankInfo, types, employeePayrollRuns, types, employees, requests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/crm/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 89.76 | **LOC:** 84 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 28`
* *Architecture:* `api: 38`, `import: 44`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` accounts, requests, associationTypes, requests, asyncPassthrough, types, contacts, requests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ticketing/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 83.6 | **LOC:** 76 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`
* *Architecture:* `api: 34`, `import: 36`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncPassthrough, types, attachments, requests, collections, types, comments, requests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/filestorage/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 71.44 | **LOC:** 68 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 22`
* *Architecture:* `api: 26`, `import: 28`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncPassthrough, types, fieldMapping, requests, files, requests, types, folders...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/fetcher/stream-wrappers/chooseStreamWrapper.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 64.08 | **LOC:** 60 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 0.482; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.7%), Concurrency Surface (formerly Concurrency) (99.6%), Guard Balance (formerly Safety Score) (83.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chooseStreamWrapper` **(Defensive Guards)** (Impact: 12.0)
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
  * `adopt` **(Defensive Guards)** (Impact: 2.9)
  * `step` **(Compute Cores)** (Impact: 2.9)
  * `fulfilled` **(Defensive Guards)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 28`, `args: 21`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 8`, `import: 4`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.482
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000726
  * `Imports (Out-Degree: 4):` runtime, Node18UniversalStreamWrapper, NodePre18StreamWrapper, UndiciStreamWrapper
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/core/fetcher/getFetchFn.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 59.0 | **LOC:** 69 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.135; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (97.5%), Complexity Load (formerly Cognitive Load) (82.9%), Guard Balance (formerly Safety Score) (82.6%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFetchFn` **(Defensive Guards)** (Impact: 8.9)
    * *Intent:* /** * Returns a fetch function based on the runtime */
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
  * `adopt` **(Defensive Guards)** (Impact: 2.9)
  * `step` **(Compute Cores)** (Impact: 2.9)
  * `fulfilled` **(Defensive Guards)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 27`, `args: 20`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 12`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000381
  * `Imports (Out-Degree: 1):` index, node-fetch
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/core/fetcher/getErrorResponseBody.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 51.36 | **LOC:** 46 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.135; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (94.4%), Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (80.0%), Concurrency Surface (formerly Concurrency) (53.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getErrorResponseBody` **(Defensive Guards)** (Impact: 32.7)
  * `adopt` **(Defensive Guards)** (Impact: 2.9)
  * `step` **(Compute Cores)** (Impact: 2.9)
  * `fulfilled` **(Defensive Guards)** (Impact: 1.5)
  * `rejected` **(Defensive Guards)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 13`, `args: 9`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 2`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000381
  * `Imports (Out-Degree: 2):` json, getResponseBody
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/api/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 49.94 | **LOC:** 43 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (96.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 9`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` accounting, ats, crm, filestorage, hris, ticketing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 49.94 | **LOC:** 43 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (96.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 9`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` accounting, ats, crm, filestorage, hris, ticketing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 48.32 | **LOC:** 63 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.9%), Guard Balance (formerly Safety Score) (90.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 36`, `args: 20`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 11`
* *Architecture:* `api: 14`, `import: 12`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Client, api, Client, Client, Client, Client, Client, Client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 41.06 | **LOC:** 49 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.2%), Connectivity (formerly Api Exposure) (99.0%), Guard Balance (formerly Safety Score) (94.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` auth, base64, fetcher, logging, pagination, runtime, schemas, url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/core/logging/exports.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 39.94 | **LOC:** 46 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.309; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.9%), Complexity Load (formerly Cognitive Load) (78.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 16`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 11`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000406
  * `Imports (Out-Degree: 1):` logger
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/serialization/resources/accounting/resources/webhookReceivers/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.92 | **LOC:** 42 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` list, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ats/resources/webhookReceivers/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.92 | **LOC:** 42 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` list, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/crm/resources/webhookReceivers/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.92 | **LOC:** 42 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` list, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/filestorage/resources/webhookReceivers/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.92 | **LOC:** 42 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` list, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/hris/resources/webhookReceivers/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.92 | **LOC:** 42 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` list, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ticketing/resources/webhookReceivers/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.92 | **LOC:** 42 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` list, requests
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/accounting/resources/forceResync/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.84 | **LOC:** 38 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 9`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` syncStatusResyncCreate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/ats/resources/forceResync/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.84 | **LOC:** 38 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 9`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` syncStatusResyncCreate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/crm/resources/forceResync/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.84 | **LOC:** 38 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 9`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` syncStatusResyncCreate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/serialization/resources/filestorage/resources/forceResync/client/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 34.84 | **LOC:** 38 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.12; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 9`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` syncStatusResyncCreate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/api/index.js` -> **Severity: 20.468** (Embedded: 0.2779 * Error Risk: 73.6639%)
- `package/core/schemas/builders/schema-utils/index.js` -> **Severity: 0.379** (Embedded: 0.0056 * Error Risk: 67.4492%)
- `package/core/schemas/builders/object-like/index.js` -> **Severity: 0.084** (Embedded: 0.0012 * Error Risk: 67.4492%)
- `package/core/fetcher/stream-wrappers/chooseStreamWrapper.js` -> **Severity: 0.06** (Embedded: 0.0007 * Error Risk: 83.131%)
- `package/core/schemas/builders/object/index.js` -> **Severity: 0.059** (Embedded: 0.0009 * Error Risk: 67.4492%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/core/fetcher/stream-wrappers/chooseStreamWrapper.js` -> **Severity: 48.2** (Blast Radius: 0.482 * Doc Risk: 100.0%)
- `package/core/base64.js` -> **Severity: 37.1** (Blast Radius: 0.371 * Doc Risk: 100.0%)
- `package/core/logging/exports.js` -> **Severity: 30.9** (Blast Radius: 0.309 * Doc Risk: 100.0%)
- `package/core/pagination/Page.js` -> **Severity: 23.021** (Blast Radius: 0.325 * Doc Risk: 70.8333%)
- `package/core/fetcher/Supplier.js` -> **Severity: 21.9** (Blast Radius: 0.219 * Doc Risk: 100.0%)

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
