# ARCHITECTURAL_BRIEF: @rudderstack_rudder-sdk-node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 14 analyzed artifact(s), 1682 LOC.
- **Load-bearing artifact:** `package/package.json` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/cjs/index.js` -- pulls in 15 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/esm/index.js` at magnitude 732.48 (structural weight, not risk).
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
| Total Artifacts | 23 |
| Analyzed Artifacts (Scanned) | 14 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 1682 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3194 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 6 | 1430 | 42.9% |
| TYPESCRIPT | 4 | 252 | 28.6% |
| MARKDOWN | 3 | 0 | 21.4% |
| PLAINTEXT | 1 | 0 | 7.1% |

## 4.1 SOURCE ENCODINGS
All 14 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Callbacks & Closures Files 21%, Compute Cores Files 14%, State Mutators Files 14%, Large Core Modules (2) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 10 | 71.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 28.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `.map`: 7x Excluded (Saturation: Line 1 exceeds 500 chars), 2x Unresolved Ambiguity (No Retainable Structure)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 81.1 | 32.9 | 13.6 | 60.1 |
| Guard Balance (formerly Error & Exception Exposure) | 49.1 | 80.0 | 64.7 | 67.0 | 75.4 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 33.5 | 9.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 25.8 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 2.1 | 19.7 | 6.5 | 3.2 | 19.7 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 23.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 58.4 | 67.2 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 80.0 | 35.0 | 34.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 4 | 2 | 2 | `package/cjs/index.js` |
| guards | 108 | 6 | 37 | `package/esm/index.js` |
| danger | 72 | 8 | 20 | `package/esm/index.js` |
| concurrency | 76 | 4 | 36 | `package/esm/index.js` |
| connectivity | 12 | 10 | 2 | `package/index.d.ts` |
| io | 10 | 4 | 4 | `package/cjs/index.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 24 | 4 | 11 | `package/cjs/index.js` |
| serialization | 18 | 4 | 8 | `package/cjs/index.js` |
| regex | 0 | 0 | 0 | - |
| events | 86 | 2 | 43 | `package/cjs/index.js` |
| tests | 0 | 0 | 0 | - |
| docs | 72 | 10 | 11 | `package/index.d.ts` |
| debt | 0 | 0 | 0 | - |
| mutation | 509 | 9 | 177 | `package/esm/index.js` |
| dead_code | 40 | 5 | 9 | `package/types/index.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 6 | 2 | 3 | `package/cjs/index.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cjs/index.js` (Hits: 4)
- `package/esm/index.js` (Hits: 4)
- `package/index.d.ts` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **package.json** (`package/package.json`) — 2 inbound connections
2. **Logger.js** (`package/cjs/Logger.js`) — 1 inbound connections
3. **index.js** (`package/cjs/loosely-validate-event/index.js`) — 1 inbound connections
4. **Logger.js** (`package/esm/Logger.js`) — 1 inbound connections
5. **index.js** (`package/esm/loosely-validate-event/index.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/cjs/index.js`) — 15 outbound dependencies
2. **index.js** (`package/esm/index.js`) — 14 outbound dependencies
3. **index.js** (`package/cjs/loosely-validate-event/index.js`) — 3 outbound dependencies
4. **index.js** (`package/esm/loosely-validate-event/index.js`) — 3 outbound dependencies
5. **index.d.ts** (`package/types/index.d.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `flush` **(Defensive Guards)** (@ `package/cjs/index.js`) -> Impact: **60.8** | LOC: 169
  * *Intent:* /** * Flush the current queue * */ // eslint-disable-next-line consistent-return, sonarjs/cognitive-complexity
- `flush` **(Defensive Guards)** (@ `package/esm/index.js`) -> Impact: **60.8** | LOC: 169
  * *Intent:* /** * Flush the current queue * */ // eslint-disable-next-line consistent-return, sonarjs/cognitive-complexity
- `step` **(Defensive Guards)** (@ `package/esm/index.js`) -> Impact: **50.6** | LOC: 22
- `enqueue` **(Many-Argument Workhorses)** (@ `package/cjs/index.js`) -> Impact: **34.9** | LOC: 58
  * *Intent:* /** * Add a `message` of type `type` to the queue and * check whether it should be flushed. * */
- `enqueue` **(Many-Argument Workhorses)** (@ `package/esm/index.js`) -> Impact: **34.9** | LOC: 58
  * *Intent:* /** * Add a `message` of type `type` to the queue and * check whether it should be flushed. * */
- `Analytics` **(Defensive Guards)** (@ `package/cjs/index.js`) -> Impact: **30.1** | LOC: 47
  * *Intent:* */
- `Analytics` **(Defensive Guards)** (@ `package/esm/index.js`) -> Impact: **30.1** | LOC: 47
  * *Intent:* */
- `createPersistenceQueue` **(Many-Argument Workhorses)** (@ `package/cjs/index.js`) -> Impact: **28.9** | LOC: 93
  * *Intent:* * port?: number = 6379; * host?: string = localhost; * db?: number = 0; * password?: string; * }, * jobOpts: { * maxAttempts: number = 10 * } * } * Al...
- `createPersistenceQueue` **(Many-Argument Workhorses)** (@ `package/esm/index.js`) -> Impact: **28.9** | LOC: 93
  * *Intent:* * port?: number = 6379; * host?: string = localhost; * db?: number = 0; * password?: string; * }, * jobOpts: { * maxAttempts: number = 10 * } * } * Al...
- `addPersistentQueueProcessor` **(Callbacks & Closures)** (@ `package/cjs/index.js`) -> Impact: **21.9** | LOC: 118

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/esm` | 2 | 827.52 | 70.64% | 9.33% |
| `package/cjs` | 2 | 692.7 | 69.81% | 10.01% |
| `package/cjs/loosely-validate-event` | 1 | 50.04 | 9.17% | 0.0% |
| `package/esm/loosely-validate-event` | 1 | 50.04 | 9.17% | 0.0% |
| `package` | 5 | 19.27 | 2.57% | 19.86% |
| `package/types` | 2 | 6.69 | 8.54% | 98.53% |
| `package/types/loosely-validate-event` | 1 | 0.19 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/types/index.d.ts` -> **99.9995%** Exposure
- `package/index.d.ts` -> **99.2882%** Exposure
- `package/types/Logger.d.ts` -> **97.0688%** Exposure
- `package/cjs/index.js` -> **20.0246%** Exposure
- `package/esm/index.js` -> **18.6547%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/cjs/Logger.js` -> **100.0%** Exposure
- `package/cjs/index.js` -> **100.0%** Exposure
- `package/esm/Logger.js` -> **100.0%** Exposure
- `package/esm/index.js` -> **100.0%** Exposure
- `package/cjs/loosely-validate-event/index.js` -> **67.192%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/types/index.d.ts` -> **16** Orphaned Functions | **0** Duplicates
- `package/index.d.ts` -> **9** Orphaned Functions | **0** Duplicates
- `package/cjs/index.js` -> **6** Orphaned Functions | **0** Duplicates
- `package/esm/index.js` -> **6** Orphaned Functions | **0** Duplicates
- `package/types/Logger.d.ts` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `30` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/esm/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.612)
- **Top Global Matches:** file_cluster_6: 8.612, file_cluster_8: 13.385, file_cluster_4: 14.417
- **Magnitude:** 732.48 | **LOC:** 797 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 56.497; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 58.8235% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flush` **(Defensive Guards)** (Impact: 60.8)
    * *Intent:* /** * Flush the current queue * */ // eslint-disable-next-line consistent-return, sonarjs/cognitive-...
  * `step` **(Defensive Guards)** (Impact: 50.6)
  * `enqueue` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* /** * Add a `message` of type `type` to the queue and * check whether it should be flushed. * */
  * `Analytics` **(Defensive Guards)** (Impact: 30.1)
    * *Intent:* */
  * `createPersistenceQueue` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* * port?: number = 6379; * host?: string = localhost; * db?: number = 0; * password?: string; * }, * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 92 instances
* *Concurrency (weighted view):* 124
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 127`, `args: 65`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 131`, `unreferenced_by_name: 6`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 34`, `import: 15`
* *Defense:* `safety: 53`, `doc: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` package.json, Logger, loosely-validate-event, assert, axios, axios-retry, bull, lodash.clonedeep...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.989)
- **Top Global Matches:** file_cluster_6: 8.989, file_cluster_8: 12.512, file_cluster_4: 15.309
- **Magnitude:** 597.66 | **LOC:** 751 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 56.497; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%)
- **Documentation Coverage:** 44.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flush` **(Defensive Guards)** (Impact: 60.8)
    * *Intent:* /** * Flush the current queue * */ // eslint-disable-next-line consistent-return, sonarjs/cognitive-...
  * `enqueue` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* /** * Add a `message` of type `type` to the queue and * check whether it should be flushed. * */
  * `Analytics` **(Defensive Guards)** (Impact: 30.1)
    * *Intent:* */
  * `createPersistenceQueue` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* * port?: number = 6379; * host?: string = localhost; * db?: number = 0; * password?: string; * }, * ...
  * `addPersistentQueueProcessor` **(Callbacks & Closures)** (Impact: 21.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 122
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 99`, `args: 50`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 108`, `unreferenced_by_name: 6`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 32`, `import: 16`
* *Defense:* `safety: 37`, `doc: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` package.json, Logger, loosely-validate-event, assert, axios, axios-retry, bull, lodash.clonedeep...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Logger.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.052)
- **Top Global Matches:** file_cluster_10: 7.052, file_cluster_12: 7.75, file_cluster_15: 9.372
- **Magnitude:** 95.04 | **LOC:** 89 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 72.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (60.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatLogData` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* /** * Formats the console message */ // eslint-disable-next-line class-methods-use-this
  * `outputLog` **(Callbacks & Closures)** (Impact: 3.8)
  * `Logger` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* /** * Service to log messages/data to output provider, default is console */
  * `log` **(Callbacks & Closures)** (Impact: 2.4)
  * `info` **(Callbacks & Closures)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 21`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`
* *Architecture:* `api: 1`
* *Defense:* `safety: 6`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/esm/Logger.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.052)
- **Top Global Matches:** file_cluster_10: 7.052, file_cluster_12: 7.75, file_cluster_15: 9.372
- **Magnitude:** 95.04 | **LOC:** 89 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 72.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (60.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatLogData` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* /** * Formats the console message */ // eslint-disable-next-line class-methods-use-this
  * `outputLog` **(Callbacks & Closures)** (Impact: 3.8)
  * `Logger` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* /** * Service to log messages/data to output provider, default is console */
  * `log` **(Callbacks & Closures)** (Impact: 2.4)
  * `info` **(Callbacks & Closures)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 21`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`
* *Architecture:* `api: 1`
* *Defense:* `safety: 6`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/cjs/loosely-validate-event/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.134)
- **Top Global Matches:** file_cluster_15: 6.134, file_cluster_10: 7.23, file_cluster_2: 7.307
- **Magnitude:** 50.04 | **LOC:** 107 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 72.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (67.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (9.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `looselyValidateEvent` **(Compute Cores)** (Impact: 18.4)
    * *Intent:* /** * Validate an event. */
  * `validateGenericEvent` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* /** * Validate an event object. */
  * `validateTrackEvent` **(State Mutators)** (Impact: 3.0)
    * *Intent:* /** * Validate a "track" event. */
  * `validateGroupEvent` **(State Mutators)** (Impact: 3.0)
    * *Intent:* /** * Validate a "group" event. */
  * `validateIdentifyEvent` **(State Mutators)** (Impact: 3.0)
    * *Intent:* /** * Validate a "identify" event. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 17`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 3`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` assert, component-type, join-component
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/esm/loosely-validate-event/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.134)
- **Top Global Matches:** file_cluster_15: 6.134, file_cluster_10: 7.23, file_cluster_2: 7.307
- **Magnitude:** 50.04 | **LOC:** 107 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 72.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (67.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (9.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `looselyValidateEvent` **(Compute Cores)** (Impact: 18.4)
    * *Intent:* /** * Validate an event. */
  * `validateGenericEvent` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* /** * Validate an event object. */
  * `validateTrackEvent` **(State Mutators)** (Impact: 3.0)
    * *Intent:* /** * Validate a "track" event. */
  * `validateGroupEvent` **(State Mutators)** (Impact: 3.0)
    * *Intent:* /** * Validate a "group" event. */
  * `validateIdentifyEvent` **(State Mutators)** (Impact: 3.0)
    * *Intent:* /** * Validate a "identify" event. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 17`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 3`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` assert, component-type, join-component
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 10.34 | **LOC:** 517 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 8.947)
- **Top Global Matches:** file_cluster_14: 8.947, file_cluster_7: 9.11, file_cluster_12: 11.616
- **Magnitude:** 5.87 | **LOC:** 254 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 56.497; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPersistenceQueue` **(Compute Cores)** (Impact: 16.2)
    * *Intent:* * port?: number = 6379; * host?: string = localhost; * db?: number = 0; * password?: string; * }, * ...
  * `identify` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* /** * Send an identify `message`. * */
  * `group` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* /** * Send a group `message`. * */
  * `track` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* /** * Send a track `message`. * */
  * `page` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* /** * Send a page `message`. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 13`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 2`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Logger, bull
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 2.9 | **LOC:** 145 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 88.512; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 88.512
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.586)
- **Top Global Matches:** file_cluster_12: 6.586, file_cluster_7: 6.917, file_cluster_5: 9.087
- **Magnitude:** 2.69 | **LOC:** 304 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.4%), Concurrency Surface (formerly Concurrency) (19.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPersistenceQueue` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* * port?: number = 6379; * host?: string = localhost; * db?: number = 0; * password?: string; * }, * ...
  * `constructor` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* */
  * `identify` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Send an identify `message`. * */
  * `group` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Send a group `message`. * */
  * `track` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Send a track `message`. * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 28`, `args: 12`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 1`
* *Defense:* `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 2.34 | **LOC:** 117 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/LICENSE.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 32 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/Logger.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_14: 6.997, file_cluster_7: 11.431, file_cluster_5: 14.454
- **Magnitude:** 0.82 | **LOC:** 27 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (5.6%)
- **Documentation Coverage:** 62.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 2.9)
  * `outputLog` **(Parameter Forwarders)** (Impact: 1.8)
  * `formatLogData` **(State Mutators)** (Impact: 1.8)
    * *Intent:* /** * Formats the console message */
  * `log` **(Parameter Forwarders)** (Impact: 1.5)
  * `info` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 10`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `unreferenced_by_name: 3`
* *Architecture:* `api: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/loosely-validate-event/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 7.933)
- **Top Global Matches:** file_cluster_14: 7.933, file_cluster_7: 14.292, file_cluster_5: 17.406
- **Magnitude:** 0.19 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `looselyValidateEvent` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* /** * Validate an event. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `package/types/index.d.ts` (TYPESCRIPT) | Magnitude: 5.87 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 104, branch: 55, safety_bypasses: 20, args: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/cjs/Logger.js` -> **Severity: 5.029** (Embedded: 0.0667 * Error Risk: 75.4295%)
- `package/esm/Logger.js` -> **Severity: 5.029** (Embedded: 0.0667 * Error Risk: 75.4295%)
- `package/cjs/loosely-validate-event/index.js` -> **Severity: 3.272** (Embedded: 0.0667 * Error Risk: 49.0723%)
- `package/esm/loosely-validate-event/index.js` -> **Severity: 3.272** (Embedded: 0.0667 * Error Risk: 49.0723%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/cjs/Logger.js` -> **Severity: 5800.4** (Blast Radius: 72.505 * Doc Risk: 80.0%)
- `package/esm/Logger.js` -> **Severity: 5800.4** (Blast Radius: 72.505 * Doc Risk: 80.0%)
- `package/types/Logger.d.ts` -> **Severity: 3531.062** (Blast Radius: 56.497 * Doc Risk: 62.5%)
- `package/esm/index.js` -> **Severity: 3323.351** (Blast Radius: 56.497 * Doc Risk: 58.8235%)
- `package/cjs/index.js` -> **Severity: 2485.868** (Blast Radius: 56.497 * Doc Risk: 44.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 345 call pairs -- scoped 6.4%, unique 0.0%, ambiguous 0.0%, external 93.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 345 | 6.4% | 0.0% | 0.0% | 93.6% |

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
