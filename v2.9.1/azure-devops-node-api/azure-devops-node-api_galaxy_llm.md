# ARCHITECTURAL_BRIEF: azure-devops-node-api
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
- **Scope:** 90 analyzed artifact(s), 23983 LOC.
- **Load-bearing artifact:** `package/interfaces/common/VsoBaseInterfaces.js` -- 37 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/WebApi.js` -- pulls in 41 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/WebApi.js` at magnitude 558.44 (structural weight, not risk).
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
| Total Artifacts | 164 |
| Analyzed Artifacts (Scanned) | 90 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 74 |
| Total LOC | 23983 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 54.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2258 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6696 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4154 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 74 | 22505 | 82.2% |
| JAVASCRIPT | 12 | 1478 | 13.3% |
| PLAINTEXT | 3 | 0 | 3.3% |
| MARKDOWN | 1 | 0 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `2.912`
> **Composition Archetype:** `Small Flat Repo (2)` (z +2.91; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 40%, Generic / Templated Code Files 30%, Data / Markup / Trivial 10%, Compute Cores Files 8%, Parameter Forwarders Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 86 | 95.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 4.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 74*

**Composition by Extension & Reason:**
- `.js`: 8x Excluded (Saturation: Line 12 exceeds 500 chars), 2x Excluded (Machine-Generated Source Code Signature: 122 LOC), 2x Excluded (Machine-Generated Source Code Signature: 76 LOC)
- `.ts`: 1x Excluded (Saturation: Line 23 exceeds 500 chars), 1x Excluded (Saturation: Line 26 exceeds 500 chars), 1x Excluded (Saturation: Line 63 exceeds 500 chars)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.2 | 23.7 | 13.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 45.3 | 58.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 44.7 | 8.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 30.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 78.6 | 11.3 | 8.2 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 40.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.6 | 14.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 23.9 | 25.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2 | 1 | 0 | `package/interfaces/common/VSSInterfaces.d.ts` |
| cleanup | 0 | 0 | 0 | - |
| guards | 100 | 27 | 1 | `package/Serialization.js` |
| danger | 1292 | 60 | 40 | `package/interfaces/TestInterfaces.d.ts` |
| concurrency | 2314 | 39 | 66 | `package/TaskAgentApiBase.d.ts` |
| connectivity | 2404 | 85 | 72 | `package/interfaces/TestInterfaces.d.ts` |
| io | 95 | 21 | 3 | `package/GitApi.d.ts` |
| crypto | 2 | 2 | 0 | `package/WebApi.js` |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 1 | 0 | `package/Serialization.js` |
| serialization | 2 | 1 | 0 | `package/WebApi.js` |
| regex | 10 | 5 | 0 | `package/Serialization.js` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 8784 | 73 | 259 | `package/interfaces/TestInterfaces.d.ts` |
| debt | 2237 | 37 | 66 | `package/TaskAgentApiBase.d.ts` |
| mutation | 3238 | 83 | 117 | `package/interfaces/ReleaseInterfaces.d.ts` |
| dead_code | 137 | 41 | 1 | `package/WebApi.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 22 | 13 | 1 | `package/CoreApi.d.ts` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/GitApi.d.ts` (Hits: 16)
- `package/interfaces/GitInterfaces.d.ts` (Hits: 11)
- `package/TfvcApi.d.ts` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **VsoBaseInterfaces.js** (`package/interfaces/common/VsoBaseInterfaces.js`) — 37 inbound connections
2. **ClientApiBases.js** (`package/ClientApiBases.js`) — 27 inbound connections
3. **VsoClient.js** (`package/VsoClient.js`) — 4 inbound connections
4. **TaskAgentApi.js** (`package/TaskAgentApi.js`) — 2 inbound connections
5. **Serialization.js** (`package/Serialization.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **WebApi.js** (`package/WebApi.js`) — 41 outbound dependencies
2. **WebApi.d.ts** (`package/WebApi.d.ts`) — 34 outbound dependencies
3. **WikiApi.d.ts** (`package/WikiApi.d.ts`) — 6 outbound dependencies
4. **CoreApi.d.ts** (`package/CoreApi.d.ts`) — 5 outbound dependencies
5. **GitApi.d.ts** (`package/GitApi.d.ts`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_getTranslatedField` **(Many-Argument Workhorses)** (@ `package/Serialization.js`) -> Impact: **91.5** | LOC: 86
- `queryTestRuns` **(Compute Cores)** (@ `package/TestResultsApi.d.ts`) -> Impact: **63.7** | LOC: 1
- `queryTestRuns` **(Compute Cores)** (@ `package/TestResultsApi.d.ts`) -> Impact: **63.7** | LOC: 1
  * *Intent:* */
- `constructor` **(Many-Argument Workhorses)** (@ `package/WebApi.js`) -> Impact: **53.2** | LOC: 81
  * *Intent:* /* * Factory to return client apis and handlers */
- `readReportingRevisionsGet` **(Compute Cores)** (@ `package/WorkItemTrackingApi.d.ts`) -> Impact: **46.9** | LOC: 1
- `readReportingRevisionsGet` **(Compute Cores)** (@ `package/WorkItemTrackingApi.d.ts`) -> Impact: **46.9** | LOC: 1
  * *Intent:* * */
- `replaceRouteValues` **(Compute Cores)** (@ `package/VsoClient.js`) -> Impact: **44.7** | LOC: 63
  * *Intent:* // helper method copied directly from VSS\WebAPI\restclient.ts
- `getItems` **(Compute Cores)** (@ `package/FileContainerApiBase.d.ts`) -> Impact: **43.3** | LOC: 1
- `getItems` **(Compute Cores)** (@ `package/FileContainerApiBase.d.ts`) -> Impact: **43.3** | LOC: 1
  * *Intent:* * */
- `getHfsItem` **(Compute Cores)** (@ `package/GitApi.d.ts`) -> Impact: **39.7** | LOC: 1

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package` | 42 | 2103.62 | 36.75% | 83.05% |
| `package/opensource/node-http-ntlm` | 2 | 222.14 | 27.71% | 0.0% |
| `package/interfaces` | 31 | 205.14 | 11.43% | 1.91% |
| `package/interfaces/common` | 7 | 56.88 | 9.65% | 14.29% |
| `package/handlers` | 8 | 30.22 | 2.22% | 25.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/AlertApi.d.ts` -> **100.0%** Exposure
- `package/CIXApi.d.ts` -> **100.0%** Exposure
- `package/CoreApi.d.ts` -> **100.0%** Exposure
- `package/DashboardApi.d.ts` -> **100.0%** Exposure
- `package/ExtensionManagementApi.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/ClientApiBases.js` -> **100.0%** Exposure
- `package/Serialization.js` -> **100.0%** Exposure
- `package/VsoClient.js` -> **100.0%** Exposure
- `package/WebApi.js` -> **100.0%** Exposure
- `package/interfaces/common/System.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/TaskAgentApiBase.d.ts` -> **1** Orphaned Functions | **312** Duplicates
- `package/GitApi.d.ts` -> **1** Orphaned Functions | **304** Duplicates
- `package/TestResultsApi.d.ts` -> **1** Orphaned Functions | **242** Duplicates
- `package/WorkItemTrackingApi.d.ts` -> **1** Orphaned Functions | **180** Duplicates
- `package/GalleryApi.d.ts` -> **1** Orphaned Functions | **168** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `29` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/WebApi.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 558.44 | **LOC:** 497 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 42.5532% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 53.2)
    * *Intent:* /* * Factory to return client apis and handlers */
  * `_getResourceAreaUrl` **(Defensive Guards)** (Impact: 16.9)
  * `getHandlerFromToken` **(Defensive Guards)** (Impact: 7.3)
  * `_readTaskLibSecrets` **(Compute Cores)** (Impact: 6.6)
  * `getLocationsApi` **(Compute Cores)** (Impact: 5.7)
    * *Intent:* // TODO: Don't call resource area here? Will cause infinite loop?
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 132`, `args: 85`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 88`, `dead_code: 1`, `planned_debt: 24`, `unreferenced_by_name: 32`
* *Architecture:* `io: 7`, `api: 12`, `concurrency: 3`, `import: 41`
* *Defense:* `safety: 15`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` AlertApi, BuildApi, CIXApi, CoreApi, DashboardApi, ExtensionManagementApi, FeatureManagementApi, FileContainerApi...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/Serialization.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 334.42 | **LOC:** 273 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 47.116; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getTranslatedField` **(Many-Argument Workhorses)** (Impact: 91.5)
  * `_getTranslatedEnumValue` **(Defensive Guards)** (Impact: 32.0)
  * `_getTranslatedArray` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `_getTranslatedObject` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `deserialize` **(Defensive Guards)** (Impact: 16.5)
    * *Intent:* /** * Process a pure JSON object (e.g. that came from a REST call) and transform it into a JS object...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 58`, `args: 10`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`
* *Architecture:* `api: 3`
* *Defense:* `safety: 19`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.160163
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/VsoClient.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 308.42 | **LOC:** 266 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 53.471; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Concurrency Surface (formerly Concurrency) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replaceRouteValues` **(Compute Cores)** (Impact: 44.7)
    * *Intent:* // helper method copied directly from VSS\WebAPI\restclient.ts
  * `autoNegotiateApiVersion` **(Compute Cores)** (Impact: 38.9)
  * `queryParamsToStringHelper` **(Defensive Guards)** (Impact: 24.1)
  * `getRequestUrl` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `getVersioningData` **(Many-Argument Workhorses)** (Impact: 8.1)
    * *Intent:* /** * Gets the route template for a resource based on its location ID and negotiates the api version...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 42`, `args: 17`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 52`
* *Architecture:* `io: 3`, `api: 6`, `concurrency: 5`, `import: 2`
* *Defense:* `safety: 8`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.186168
  * `Imports (Out-Degree: 0):` path, url
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/opensource/node-http-ntlm/ntlm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 221.14 | **LOC:** 391 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 7.476; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createType3Message` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `parseType2Message` **(Compute Cores)** (Impact: 12.0)
  * `createType1Message` **(Compute Cores)** (Impact: 6.3)
  * `binaryArray2bytes` **(Compute Cores)** (Impact: 6.1)
  * `insertZerosEvery7Bits` **(Defensive Guards)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 84`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/GitApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 144.09 | **LOC:** 1605 | **CtrlFlow:** 210.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.082% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getHfsItem` **(Compute Cores)** (Impact: 39.7)
  * `getHfsItemContent` **(Compute Cores)** (Impact: 39.7)
  * `getHfsItemText` **(Compute Cores)** (Impact: 39.7)
  * `getHfsItemZip` **(Compute Cores)** (Impact: 39.7)
  * `getItem` **(Compute Cores)** (Impact: 39.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 664`, `structural_boundaries: 51`, `args: 305`, `func_start: 305`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `duplicate_logic: 304`, `unreferenced_by_name: 1`
* *Architecture:* `io: 16`, `api: 2`, `concurrency: 304`, `import: 5`
* *Defense:* `doc: 152`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, CoreInterfaces, GitInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/TaskAgentApi.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 141.1 | **LOC:** 204 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 10.654; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.0%), Mutation Surface (formerly State Flux) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%)
- **Documentation Coverage:** 22.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getAccountUrl` **(Defensive Guards)** (Impact: 22.6)
  * `getTaskContentZip` **(Many-Argument Workhorses)** (Impact: 14.5)
    * *Intent:* /** */
  * `getTaskDefinition` **(Many-Argument Workhorses)** (Impact: 14.5)
    * *Intent:* /** */
  * `getTaskDefinitions` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* /** */
  * `deleteTaskDefinition` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 55`, `args: 22`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`, `dead_code: 1`
* *Architecture:* `api: 8`, `concurrency: 7`, `import: 2`
* *Defense:* `safety: 16`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.654
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022472
  * `Imports (Out-Degree: 0):` TaskAgentApiBase, url
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/TaskAgentApiBase.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 81.89 | **LOC:** 1235 | **CtrlFlow:** 89.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.0799% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDeploymentTargets` **(Compute Cores)** (Impact: 39.7)
  * `getDeploymentTargets` **(Compute Cores)** (Impact: 39.7)
    * *Intent:* * */
  * `getTaskGroups` **(Compute Cores)** (Impact: 24.1)
  * `getTaskGroups` **(Compute Cores)** (Impact: 24.1)
    * *Intent:* /** * List task groups. * */
  * `getAgents` **(Compute Cores)** (Impact: 19.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 66`, `args: 313`, `func_start: 313`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `duplicate_logic: 312`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 312`, `import: 4`
* *Defense:* `doc: 156`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, TaskAgentInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/TestResultsApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 80.68 | **LOC:** 1111 | **CtrlFlow:** 108.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.1029% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `queryTestRuns` **(Compute Cores)** (Impact: 63.7)
  * `queryTestRuns` **(Compute Cores)** (Impact: 63.7)
    * *Intent:* */
  * `getTestRuns` **(Compute Cores)** (Impact: 28.5)
  * `getTestRuns` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* /** */
  * `getTestResultsByPipeline` **(Compute Cores)** (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 56`, `args: 243`, `func_start: 243`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `duplicate_logic: 242`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 242`, `import: 4`
* *Defense:* `doc: 121`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, TestInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ClientApiBases.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 63.56 | **LOC:** 61 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **4**; blast radius 93.27; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Complexity Load (formerly Cognitive Load) (92.2%), Connectivity (formerly Api Exposure) (78.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extractRateLimitHeaders` **(Compute Cores)** (Impact: 16.8)
  * `createAcceptHeader` **(Parameter Forwarders)** (Impact: 3.6)
  * `constructor` **(State Mutators)** (Impact: 2.6)
  * `formatResponse` **(Parameter Forwarders)** (Impact: 2.4)
  * `createRequestOptions` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 8`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 93.27
  * `Choke Point (Betweenness):` 0.006895 | `Ripple Effect (Closeness):` 0.303371
  * `Imports (Out-Degree: 2):` Serialization, VsoClient, HttpClient, RestClient
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `package/WorkItemTrackingApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 60.36 | **LOC:** 830 | **CtrlFlow:** 133.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.1381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readReportingRevisionsGet` **(Compute Cores)** (Impact: 46.9)
  * `readReportingRevisionsGet` **(Compute Cores)** (Impact: 46.9)
    * *Intent:* * */
  * `updateWorkItem` **(Compute Cores)** (Impact: 18.1)
  * `updateWorkItem` **(Compute Cores)** (Impact: 18.1)
    * *Intent:* /** * Updates a single work item. * */
  * `getComments` **(Compute Cores)** (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 43`, `args: 181`, `func_start: 181`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `duplicate_logic: 180`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 2`, `concurrency: 180`, `import: 5`
* *Defense:* `doc: 90`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, CoreInterfaces, WorkItemTrackingInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/GalleryApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 48.38 | **LOC:** 697 | **CtrlFlow:** 91.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.1479% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCategoryTree` **(Compute Cores)** (Impact: 21.1)
  * `getCategoryTree` **(Compute Cores)** (Impact: 21.1)
    * *Intent:* /** */
  * `getRootCategories` **(Compute Cores)** (Impact: 15.9)
  * `getAssetWithToken` **(Compute Cores)** (Impact: 15.9)
  * `getRootCategories` **(Compute Cores)** (Impact: 15.9)
    * *Intent:* /** */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 57`, `args: 169`, `func_start: 169`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `duplicate_logic: 168`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 168`, `import: 3`
* *Defense:* `doc: 84`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GalleryCompatHttpClientBase, GalleryInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/common/System.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 35.52 | **LOC:** 48 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 13.831; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.6%), Connectivity (formerly Api Exposure) (51.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `api: 5`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011236
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/TfvcApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 29.59 | **LOC:** 255 | **CtrlFlow:** 282.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.5102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getChangeset` **(Compute Cores)** (Impact: 38.2)
  * `getChangeset` **(Compute Cores)** (Impact: 38.2)
    * *Intent:* * Retrieve a Tfvc Changeset * */
  * `getItem` **(Compute Cores)** (Impact: 24.1)
  * `getItemContent` **(Compute Cores)** (Impact: 24.1)
  * `getItemText` **(Compute Cores)** (Impact: 24.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 12`, `args: 49`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `duplicate_logic: 48`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `api: 2`, `concurrency: 48`, `import: 4`
* *Defense:* `doc: 24`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, TfvcInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/TestPlanApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 27.71 | **LOC:** 452 | **CtrlFlow:** 91.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.2632% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getTestCaseList` **(Compute Cores)** (Impact: 31.2)
  * `getTestCaseList` **(Compute Cores)** (Impact: 31.2)
    * *Intent:* * Get Test Case List return those test cases which have all the configuration Ids as mentioned in th...
  * `getPointsList` **(Compute Cores)** (Impact: 22.2)
  * `getPointsList` **(Compute Cores)** (Impact: 22.2)
    * *Intent:* /** * Get all the points inside a suite based on some filters * */
  * `getTestEntityCountByPlanId` **(Compute Cores)** (Impact: 21.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 30`, `args: 95`, `func_start: 95`, `class_start: 2`
* *Risk/State:* `duplicate_logic: 94`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 94`, `import: 4`
* *Defense:* `doc: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, TestPlanInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/TaskAgentInterfaces.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 23.85 | **LOC:** 4223 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.476; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.2%), Mutation Surface (formerly State Flux) (54.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 971`, `structural_boundaries: 660`, `class_start: 268`
* *Risk/State:* `safety_bypasses: 117`, `state_mutation: 51`
* *Architecture:* `io: 1`, `api: 269`, `import: 3`
* *Defense:* `safety: 1`, `doc: 642`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DistributedTaskCommonInterfaces, FormInputInterfaces, VSSInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/TestInterfaces.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 23.33 | **LOC:** 6096 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.476; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (24.0%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1459`, `structural_boundaries: 664`, `class_start: 298`
* *Risk/State:* `safety_bypasses: 151`, `state_mutation: 39`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 299`, `import: 3`
* *Defense:* `doc: 1037`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CoreInterfaces, SystemDataInterfaces, VSSInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WorkApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 19.96 | **LOC:** 504 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.2101% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDeliveryTimelineData` **(Compute Cores)** (Impact: 9.8)
  * `getDeliveryTimelineData` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* /** * Get Delivery View Data * */
  * `getBoardBadge` **(Generic / Templated Code)** (Impact: 6.8)
  * `getBoardBadgeData` **(Compute Cores)** (Impact: 6.8)
  * `getPredefinedQueryResults` **(Generic / Templated Code)** (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 24`, `args: 119`, `func_start: 119`, `class_start: 2`
* *Risk/State:* `duplicate_logic: 118`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 118`, `import: 4`
* *Defense:* `doc: 59`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, CoreInterfaces, WorkInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/ReleaseInterfaces.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 19.6 | **LOC:** 4544 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.476; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (49.6%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 814`, `structural_boundaries: 540`, `class_start: 217`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 43`
* *Architecture:* `io: 2`, `api: 218`, `import: 3`
* *Defense:* `doc: 849`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DistributedTaskCommonInterfaces, FormInputInterfaces, VSSInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/GitInterfaces.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 19.36 | **LOC:** 4349 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.476; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (41.0%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 784`, `structural_boundaries: 583`, `class_start: 232`
* *Risk/State:* `safety_bypasses: 142`, `state_mutation: 38`, `planned_debt: 1`
* *Architecture:* `io: 11`, `api: 233`, `import: 3`
* *Defense:* `doc: 795`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CoreInterfaces, PolicyInterfaces, VSSInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WorkItemTrackingProcessApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 19.22 | **LOC:** 522 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 6.8)
  * `moveControlToGroup` **(Generic / Templated Code)** (Impact: 5.3)
  * `moveControlToGroup` **(Generic / Templated Code)** (Impact: 5.3)
    * *Intent:* /** * Moves a control to a specified group. * */
  * `getWorkItemTypeField` **(Generic / Templated Code)** (Impact: 4.5)
  * `getWorkItemTypeField` **(Generic / Templated Code)** (Impact: 4.5)
    * *Intent:* /** * Returns a field in a work item type. * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 33`, `args: 115`, `func_start: 115`, `class_start: 2`
* *Risk/State:* `duplicate_logic: 114`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 114`, `import: 3`
* *Defense:* `doc: 57`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, WorkItemTrackingProcessInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/CoreApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 15.9 | **LOC:** 260 | **CtrlFlow:** 77.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.3425% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getProjects` **(Compute Cores)** (Impact: 14.7)
  * `getProjects` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* /** * Get all projects in the organization that the authenticated user has access to. * */
  * `getTeams` **(Compute Cores)** (Impact: 12.3)
  * `getTeams` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* /** * Get a list of teams. * */
  * `getAllTeams` **(Compute Cores)** (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 29`, `args: 67`, `func_start: 67`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `duplicate_logic: 66`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 66`, `import: 5`
* *Defense:* `doc: 33`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, CoreInterfaces, OperationsInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WikiApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 15.53 | **LOC:** 244 | **CtrlFlow:** 110.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listComments` **(Compute Cores)** (Impact: 22.2)
  * `listComments` **(Compute Cores)** (Impact: 22.2)
    * *Intent:* /** * Returns a pageable list of comments. * */
  * `getPageText` **(Compute Cores)** (Impact: 13.3)
  * `getPageZip` **(Compute Cores)** (Impact: 13.3)
  * `getPageText` **(Compute Cores)** (Impact: 13.3)
    * *Intent:* /** * Gets metadata or content of the wiki page for the provided path. Content negotiation is done b...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 22`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 44`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 44`, `import: 6`
* *Defense:* `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, CommentsInterfaces, GitInterfaces, WikiInterfaces, VSSInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/interfaces/BuildInterfaces.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 15.23 | **LOC:** 3621 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 7.476; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (46.1%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 644`, `structural_boundaries: 446`, `class_start: 172`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 34`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 173`, `import: 5`
* *Defense:* `doc: 696`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CoreInterfaces, DistributedTaskCommonInterfaces, TestInterfaces, TfvcInterfaces, VSSInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/WorkItemTrackingProcessDefinitionsApi.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 15.02 | **LOC:** 425 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.2688% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 6.8)
  * `setControlInGroup` **(Generic / Templated Code)** (Impact: 5.3)
  * `setControlInGroup` **(Generic / Templated Code)** (Impact: 5.3)
    * *Intent:* /** * Moves a control to a new group * */
  * `getWorkItemType` **(Generic / Templated Code)** (Impact: 4.0)
  * `getWorkItemType` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* /** * Returns a work item type of the process. * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 29`, `args: 93`, `func_start: 93`, `class_start: 2`
* *Risk/State:* `duplicate_logic: 92`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 92`, `import: 3`
* *Defense:* `doc: 46`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ClientApiBases, WorkItemTrackingProcessDefinitionsInterfaces, VsoBaseInterfaces
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ThirdPartyNotice.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 13.74 | **LOC:** 687 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/ClientApiBases.js` -> **Severity: 0.69** (Bridge: 0.0069 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/ClientApiBases.js` -> **Severity: 28.789** (Embedded: 0.3034 * Error Risk: 94.8975%)
- `package/VsoClient.js` -> **Severity: 18.129** (Embedded: 0.1862 * Error Risk: 97.3787%)
- `package/Serialization.js` -> **Severity: 14.07** (Embedded: 0.1602 * Error Risk: 87.8481%)
- `package/TaskAgentApi.js` -> **Severity: 1.32** (Embedded: 0.0225 * Error Risk: 58.7331%)
- `package/interfaces/common/System.js` -> **Severity: 0.939** (Embedded: 0.0112 * Error Risk: 83.5974%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/ClientApiBases.js` -> **Severity: 4663.5** (Blast Radius: 93.27 * Doc Risk: 50.0%)
- `package/Serialization.js` -> **Severity: 1884.64** (Blast Radius: 47.116 * Doc Risk: 40.0%)
- `package/VsoClient.js` -> **Severity: 1527.741** (Blast Radius: 53.471 * Doc Risk: 28.5714%)
- `package/handlers/basiccreds.js` -> **Severity: 853.6** (Blast Radius: 8.536 * Doc Risk: 100.0%)
- `package/handlers/bearertoken.js` -> **Severity: 853.6** (Blast Radius: 8.536 * Doc Risk: 100.0%)

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
