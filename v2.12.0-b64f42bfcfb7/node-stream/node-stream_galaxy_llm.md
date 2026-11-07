# ARCHITECTURAL_BRIEF: node-stream
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
- **Scope:** 31 analyzed artifact(s), 656 LOC.
- **Load-bearing artifact:** `package/lib/modifiers/map.js` -- 8 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/index.js` -- pulls in 27 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/modifiers/batch.js` at magnitude 107.94 (structural weight, not risk).
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
| Total Artifacts | 32 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 656 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2897 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5651 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3472 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 29 | 656 | 93.5% |
| MARKDOWN | 1 | 0 | 3.2% |
| PLAINTEXT | 1 | 0 | 3.2% |

## 4.1 SOURCE ENCODINGS
All 31 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Callbacks & Closures Files 45%, Large Core Modules (2) 23%, State Mutators Files 13%, Data / Markup / Trivial 6%, Parameter Forwarders Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 29 | 93.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 6.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 47.1 | 11.4 | 7.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 45.6 | 67.1 | 52.6 | 52.0 | 50.6 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.1 | 6.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 5.1 | 2.4 | 2.4 |
| Connectivity (formerly API Exposure) | 3.3 | 36.3 | 20.9 | 20.1 | 20.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 13.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 16.8 | 100.0 | 64.2 | 69.0 | 16.8 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 80.0 | 14.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 2 | 1 | 0 | `package/lib/modifiers/batch.js` |
| guards | 25 | 11 | 2 | `package/lib/creators/fromPromise.js` |
| danger | 3 | 3 | 0 | `package/lib/creators/fromArray.js` |
| concurrency | 5 | 4 | 1 | `package/lib/modifiers/batch.js` |
| connectivity | 65 | 29 | 3 | `package/lib/index.js` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 1 | 0 | `package/lib/modifiers/batch.js` |
| serialization | 4 | 4 | 1 | `package/lib/_utils/parse.js` |
| regex | 0 | 0 | 0 | - |
| events | 20 | 5 | 1 | `package/lib/consumers/v1/forEach.js` |
| tests | 0 | 0 | 0 | - |
| docs | 48 | 29 | 4 | `package/lib/modifiers/batch.js` |
| debt | 0 | 0 | 0 | - |
| mutation | 220 | 29 | 9 | `package/lib/index.js` |
| dead_code | 5 | 3 | 0 | `package/lib/creators/fromPromise.js` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/README.md` (Hits: 0)
- `package/lib/_utils/getArgs.js` (Hits: 0)
- `package/lib/_utils/makeAsync.js` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **map.js** (`package/lib/modifiers/map.js`) — 8 inbound connections
2. **pipeline.js** (`package/lib/modifiers/pipeline.js`) — 5 inbound connections
3. **makeAsync.js** (`package/lib/_utils/makeAsync.js`) — 3 inbound connections
4. **filter.js** (`package/lib/modifiers/filter.js`) — 3 inbound connections
5. **take.js** (`package/lib/modifiers/take.js`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/lib/index.js`) — 27 outbound dependencies
2. **sort.js** (`package/lib/modifiers/sort.js`) — 5 outbound dependencies
3. **wait.js** (`package/lib/consumers/v2/wait.js`) — 3 outbound dependencies
4. **find.js** (`package/lib/modifiers/find.js`) — 3 outbound dependencies
5. **findWhere.js** (`package/lib/modifiers/findWhere.js`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `batch` **(Compute Cores)** (@ `package/lib/modifiers/batch.js`) -> Impact: **25.8** | LOC: 121
  * *Intent:* * * const input = nodeStream.through.obj(); * * input.pipe(nodeStream.batch({ count: 2 })); * * input.write(1); * input.write(2); * input.write(3); * ...
- `writeIfPossible` **(Defensive Guards)** (@ `package/lib/modifiers/batch.js`) -> Impact: **10.7** | LOC: 16
  * *Intent:* /** * Flushes the cache if it is appropriate to do so. * */
- `fromPromise` **(Defensive Guards)** (@ `package/lib/creators/fromPromise.js`) -> Impact: **9.2** | LOC: 42
  * *Intent:* * resolves, each argument becomes a discrete item in the stream. * If the promise rejects, the stream will emit an "error" event. * * * * // Create a ...
- `validateOptions` **(Compute Cores)** (@ `package/lib/modifiers/batch.js`) -> Impact: **8.0** | LOC: 19
  * *Intent:* /** * * */
- `sort` **(Callbacks & Closures)** (@ `package/lib/modifiers/sort.js`) -> Impact: **7.8** | LOC: 43
  * *Intent:* * * to Array.sort for item comparison. * * * // sort a stream of numbers * objStream // => [10, 3, 9, 2, 4, 1] * .pipe(nodeStream.sort()) * // => [1, ...
- `fromCallback` **(Defensive Guards)** (@ `package/lib/creators/fromCallback.js`) -> Impact: **7.7** | LOC: 40
  * *Intent:* * callback as the last argument. When that callback * is called, this stream will emit all arguments * as a single array. * * * * // Create a stream f...
- `isOptionalIntAbove` **(Compute Cores)** (@ `package/lib/modifiers/batch.js`) -> Impact: **7.5** | LOC: 12
  * *Intent:* /** * * */
- `Transform` **(Many-Argument Workhorses)** (@ `package/lib/modifiers/batch.js`) -> Impact: **7.0** | LOC: 21
- `fromArray` **(Defensive Guards)** (@ `package/lib/creators/fromArray.js`) -> Impact: **6.8** | LOC: 22
  * *Intent:* * in the array is `null` the stream will end early. Every * other data type is allowed and valid. * * * * // Create a stream from an array which is th...
- `Transform` **(State Mutators)** (@ `package/lib/modifiers/intersperse.js`) -> Impact: **6.6** | LOC: 12

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **State Mutators**: general-purpose function that reassigns or mutates state

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib/modifiers` | 17 | 278.2 | 8.21% | 0.0% |
| `package/lib/creators` | 3 | 75.72 | 26.22% | 57.53% |
| `package/lib/consumers/v1` | 3 | 71.98 | 10.05% | 0.0% |
| `package/lib` | 1 | 70.08 | 0.0% | 0.0% |
| `package/lib/_utils` | 3 | 30.28 | 20.34% | 0.0% |
| `package/lib/consumers/v2` | 1 | 22.46 | 7.38% | 0.0% |
| `package/lib/consumers` | 1 | 8.3 | 13.0% | 0.0% |
| `package` | 2 | 2.26 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/creators/fromPromise.js` -> **97.0688%** Exposure
- `package/lib/creators/fromArray.js` -> **37.7541%** Exposure
- `package/lib/creators/fromCallback.js` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/index.js` -> **100.0%** Exposure
- `package/lib/creators/fromArray.js` -> **99.9932%** Exposure
- `package/lib/modifiers/batch.js` -> **99.9676%** Exposure
- `package/lib/consumers/v1/first.js` -> **99.9254%** Exposure
- `package/lib/consumers/v1/wait.js` -> **99.9254%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/creators/fromPromise.js` -> **3** Orphaned Functions | **0** Duplicates
- `package/lib/creators/fromArray.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/lib/creators/fromCallback.js` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `26` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/modifiers/batch.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.0)
- **Top Global Matches:** file_cluster_15: 7.0, file_cluster_10: 7.968, file_cluster_16: 8.264
- **Magnitude:** 107.94 | **LOC:** 233 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `batch` **(Compute Cores)** (Impact: 25.8)
    * *Intent:* * * const input = nodeStream.through.obj(); * * input.pipe(nodeStream.batch({ count: 2 })); * * inpu...
  * `writeIfPossible` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* /** * Flushes the cache if it is appropriate to do so. * */
  * `validateOptions` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* /** * * */
  * `isOptionalIntAbove` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* /** * * */
  * `Transform` **(Many-Argument Workhorses)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 25`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 2`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` lodash, through2
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 17.78)
- **Top Global Matches:** file_cluster_17: 17.78, file_cluster_13: 17.903, file_cluster_15: 17.942
- **Magnitude:** 70.08 | **LOC:** 125 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 17.774; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (13.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 27`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 27`, `import: 27`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` selectVersion.js, first.js, forEach.js, wait.js, wait.js, fromArray.js, fromCallback.js, fromPromise.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/modifiers/sort.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.345)
- **Top Global Matches:** file_cluster_10: 5.345, file_cluster_15: 6.689, file_cluster_11: 8.018
- **Magnitude:** 31.12 | **LOC:** 76 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 18.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.8%), Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (53.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sort` **(Callbacks & Closures)** (Impact: 7.8)
    * *Intent:* * * to Array.sort for item comparison. * * * // sort a stream of numbers * objStream // => [10, 3, 9...
  * `Transform` **(Parameter Forwarders)** (Impact: 5.1)
    * *Intent:* // expand the array so all input items are re-emitted
  * `emitNextItem` **(Callbacks & Closures)** (Impact: 3.6)
    * *Intent:* // recursively add array items to the stream asynchronously
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 5`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 3):` wait.js, map.js, pipeline.js, lodash, through2
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/consumers/v1/wait.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.152)
- **Top Global Matches:** file_cluster_10: 6.152, file_cluster_15: 7.423, file_cluster_2: 8.862
- **Magnitude:** 29.72 | **LOC:** 98 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (57.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (17.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `waitObj` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* /** * Wait for the contents of an object stream. * * */
  * `wait` **(Callbacks & Closures)** (Impact: 4.1)
    * *Intent:* /** * Wait for the contents of a stream. * * */
  * `waitJson` **(Callbacks & Closures)** (Impact: 4.0)
    * *Intent:* /** * Wait for the stream contents, then parse for JSON. * * */
  * `end` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* /** * Send the correct data to the onEnd callback. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 8`, `func_start: 4`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.000575 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 1):` parse.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/consumers/v1/first.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.979)
- **Top Global Matches:** file_cluster_10: 5.979, file_cluster_15: 7.042, file_cluster_2: 8.518
- **Magnitude:** 29.58 | **LOC:** 96 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (57.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (17.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `firstObj` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* /** * Get the first item in a stream. * * */
  * `first` **(Callbacks & Closures)** (Impact: 4.0)
    * *Intent:* /** * Get the first item in a stream and convert to a buffer. * * */
  * `firstJson` **(Callbacks & Closures)** (Impact: 4.0)
    * *Intent:* /** * Get the first item in a stream and parse it for JSON. * * */
  * `end` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* /** * Send the correct data to the onEnd callback. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.000575 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 1):` parse.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/creators/fromPromise.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.06)
- **Top Global Matches:** file_cluster_10: 6.06, file_cluster_15: 8.102, file_cluster_2: 8.492
- **Magnitude:** 29.46 | **LOC:** 69 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.8%), Debt Markers (formerly Tech Debt) (97.1%), Mutation Surface (formerly State Flux) (91.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromPromise` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* * resolves, each argument becomes a discrete item in the stream. * If the promise rejects, the strea...
  * `read` **(Callbacks & Closures)** (Impact: 3.3)
  * `onReject` **(Callbacks & Closures)** (Impact: 1.7)
  * `onResolve` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 5`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` readable
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/creators/fromArray.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.621)
- **Top Global Matches:** file_cluster_10: 5.621, file_cluster_15: 7.563, file_cluster_2: 7.726
- **Magnitude:** 26.58 | **LOC:** 49 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromArray` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* * in the array is `null` the stream will end early. Every * other data type is allowed and valid. * ...
  * `read` **(Callbacks & Closures)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` readable
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/intersperse.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.007)
- **Top Global Matches:** file_cluster_15: 6.007, file_cluster_2: 6.692, file_cluster_13: 7.15
- **Magnitude:** 22.86 | **LOC:** 40 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (56.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (31.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Transform` **(State Mutators)** (Impact: 6.6)
  * `intersperse` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* * * * * // Log some values to the console with new lines interspersed * shoppingList // => ['banana'...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 3`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` through2
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/consumers/v2/wait.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.695)
- **Top Global Matches:** file_cluster_10: 5.695, file_cluster_15: 6.714, file_cluster_13: 7.963
- **Magnitude:** 22.46 | **LOC:** 141 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 23.585; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (53.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (34.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `throughWithCallback` **(Callbacks & Closures)** (Impact: 3.4)
    * *Intent:* /** * Create a through stream that simply calls a callback with the contents. * Make sure to also pa...
  * `waitObj` **(Parameter Forwarders)** (Impact: 2.4)
    * *Intent:* * * of the stream. This is a convenience to * avoid listening to the data/end events of * the stream...
  * `transform` **(State Mutators)** (Impact: 2.2)
  * `wait` **(Callbacks & Closures)** (Impact: 2.0)
    * *Intent:* * * of the stream. This is a convenience to * avoid listening to the data/end events of * the stream...
  * `waitJson` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* * * of the stream. This is a convenience to * avoid listening to the data/end events of * the stream...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.585
  * `Choke Point (Betweenness):` 0.001149 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 2):` parse.js, pipeline.js, through2
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/creators/fromCallback.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.523)
- **Top Global Matches:** file_cluster_10: 5.523, file_cluster_15: 8.13, file_cluster_2: 8.313
- **Magnitude:** 19.68 | **LOC:** 70 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.9%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromCallback` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* * callback as the last argument. When that callback * is called, this stream will emit all arguments...
  * `read` **(Callbacks & Closures)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` lodash, readable
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/_utils/makeAsync.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.042)
- **Top Global Matches:** file_cluster_10: 5.042, file_cluster_2: 8.415, file_cluster_17: 8.744
- **Magnitude:** 15.78 | **LOC:** 36 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 184.962; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.8%), Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeAsync` **(Callbacks & Closures)** (Impact: 4.5)
    * *Intent:* /** * Create a function that will allow end users to ignore callbacks. * * * accepts. */...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 184.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.258621
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/flatten.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.417)
- **Top Global Matches:** file_cluster_10: 4.417, file_cluster_2: 7.242, file_cluster_15: 7.659
- **Magnitude:** 13.8 | **LOC:** 64 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (30.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Transform` **(Callbacks & Closures)** (Impact: 4.7)
  * `flatten` **(Callbacks & Closures)** (Impact: 2.8)
    * *Intent:* * .pipe(nodeStream.batch({ count: 2 })) * // perform a transform action on the batches * .pipe(trans...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` lodash, through2
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/reduce.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.113)
- **Top Global Matches:** file_cluster_10: 5.113, file_cluster_2: 7.183, file_cluster_13: 7.277
- **Magnitude:** 12.98 | **LOC:** 88 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (35.2%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reduce` **(Callbacks & Closures)** (Impact: 2.6)
    * *Intent:* * // This tweet is the most recent so far, save it for later * if (new Date(data.statuses.created_at...
  * `transform` **(State Mutators)** (Impact: 2.4)
  * `Flush` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.000383 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 1):` makeAsync.js, through2
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/consumers/v1/forEach.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.432)
- **Top Global Matches:** file_cluster_10: 7.432, file_cluster_2: 8.573, file_cluster_15: 8.766
- **Magnitude:** 12.68 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.6%), Connectivity (formerly Api Exposure) (18.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forEachJson` **(Defensive Guards)** (Impact: 2.7)
    * *Intent:* /** * Read the items in a stream and parse each item for JSON. * * */
  * `forEach` **(State Mutators)** (Impact: 2.3)
    * *Intent:* /** * Read the items in a stream and convert to buffers. * * */
  * `forEachObj` **(State Mutators)** (Impact: 2.2)
    * *Intent:* /** * Read the items in a stream. * * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 5`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/drop.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.04)
- **Top Global Matches:** file_cluster_10: 4.04, file_cluster_2: 6.903, file_cluster_15: 7.248
- **Magnitude:** 12.52 | **LOC:** 44 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drop` **(Callbacks & Closures)** (Impact: 5.2)
    * *Intent:* * * * * // drop the first 3 items from a stream * inStream // => ['b', 'a', 'n', 'a', 'n', 'a'] * .p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 1):` map.js, lodash
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/take.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.04)
- **Top Global Matches:** file_cluster_10: 4.04, file_cluster_2: 6.903, file_cluster_15: 7.248
- **Magnitude:** 12.52 | **LOC:** 44 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 28.792; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `take` **(Callbacks & Closures)** (Impact: 5.2)
    * *Intent:* * * * * // take the first 3 items from a stream * inStream // => ['b', 'a', 'n', 'a', 'n', 'a'] * .p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.792
  * `Choke Point (Betweenness):` 0.002874 | `Ripple Effect (Closeness):` 0.1
  * `Imports (Out-Degree: 1):` map.js, lodash
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/parse.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.195)
- **Top Global Matches:** file_cluster_10: 6.195, file_cluster_15: 7.071, file_cluster_2: 7.086
- **Magnitude:** 11.3 | **LOC:** 58 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 28.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.9%), Connectivity (formerly Api Exposure) (20.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* * * // parse a newline-separated JSON file * fs.createReadStream('example.log') * .pipe(nodeStream.s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.402
  * `Choke Point (Betweenness):` 0.002299 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 1):` map.js, lodash
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/filter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.942)
- **Top Global Matches:** file_cluster_10: 3.942, file_cluster_2: 7.456, file_cluster_15: 7.742
- **Magnitude:** 9.54 | **LOC:** 89 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 43.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (19.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter` **(Callbacks & Closures)** (Impact: 5.2)
    * *Intent:* * * // Error the stream since this file is not valid * if (err) { * return next(err); * } * * next(n...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.632
  * `Choke Point (Betweenness):` 0.003257 | `Ripple Effect (Closeness):` 0.106667
  * `Imports (Out-Degree: 1):` makeAsync.js, through2
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/_utils/getArgs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.13)
- **Top Global Matches:** file_cluster_15: 7.13, file_cluster_2: 7.152, file_cluster_17: 7.425
- **Magnitude:** 9.0 | **LOC:** 26 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 55.193; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getArgs` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* /** * Get an array of arguments out of a function whose signature is {...Arg|Arg[]}. * * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 55.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.109091
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/pipeline.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.507)
- **Top Global Matches:** file_cluster_10: 4.507, file_cluster_2: 7.598, file_cluster_17: 7.887
- **Magnitude:** 8.38 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **3**; blast radius 44.023; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipeline` **(Callbacks & Closures)** (Impact: 1.5)
    * *Intent:* * return nodeStream.pipeline( * nodeStream.split(), * nodeStream.sort((a, b) => { * return a.length ...
  * `pipelineObj` **(Callbacks & Closures)** (Impact: 1.5)
    * *Intent:* * * // read the contents of a file and parse json * function readJson() { * return nodeStream.pipeli...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.023
  * `Choke Point (Betweenness):` 0.005747 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 1):` getArgs.js, stream-combiner2, through2
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/consumers/selectVersion.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.534)
- **Top Global Matches:** file_cluster_10: 6.534, file_cluster_15: 7.929, file_cluster_2: 8.101
- **Magnitude:** 8.3 | **LOC:** 28 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.378; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectVersion` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* /** * Determines which version of the API should be used for the given input. If * a stream is provi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` stream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/pluck.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.225)
- **Top Global Matches:** file_cluster_10: 4.225, file_cluster_2: 7.371, file_cluster_15: 7.553
- **Magnitude:** 7.04 | **LOC:** 38 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pluck` **(Callbacks & Closures)** (Impact: 4.8)
    * *Intent:* * * each item in the source stream. * * * // get the value of the "age" property for every item in t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 1):` map.js, lodash
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/where.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.945)
- **Top Global Matches:** file_cluster_10: 3.945, file_cluster_2: 7.152, file_cluster_15: 7.507
- **Magnitude:** 5.64 | **LOC:** 39 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 23.585; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (21.5%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `where` **(Callbacks & Closures)** (Impact: 3.4)
    * *Intent:* * * the source stream. * * * // Get all users from a given zip code * users // => [{ name: 'Bill', z...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.585
  * `Choke Point (Betweenness):` 0.001724 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 1):` filter.js, lodash
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/modifiers/pick.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.838)
- **Top Global Matches:** file_cluster_10: 5.838, file_cluster_15: 7.245, file_cluster_2: 7.435
- **Magnitude:** 5.62 | **LOC:** 37 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.378; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%), Connectivity (formerly Api Exposure) (20.1%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pick` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* * * be picked from the source object. * * * // get some properties from each item in the stream * //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 1):` map.js, lodash
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/_utils/parse.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.637)
- **Top Global Matches:** file_cluster_2: 6.637, file_cluster_15: 7.054, file_cluster_17: 7.359
- **Magnitude:** 5.5 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 49.017; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.4%), Mutation Surface (formerly State Flux) (31.0%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* /** * Parse the contents of a string as JSON. * * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 49.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/lib/_utils/getArgs.js` (JAVASCRIPT) | Magnitude: 9.0 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, branch: 2, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/lib/index.js` (JAVASCRIPT) | Magnitude: 70.08 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 27, api: 27, state_mutation: 27, import: 27

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/modifiers/pipeline.js` -> **Severity: 0.397** (Bridge: 0.0057 * Flux: 68.9974%)
- `package/lib/modifiers/take.js` -> **Severity: 0.263** (Bridge: 0.0029 * Flux: 91.6827%)
- `package/lib/modifiers/parse.js` -> **Severity: 0.211** (Bridge: 0.0023 * Flux: 91.6827%)
- `package/lib/modifiers/map.js` -> **Severity: 0.171** (Bridge: 0.0102 * Flux: 16.7982%)
- `package/lib/modifiers/filter.js` -> **Severity: 0.163** (Bridge: 0.0033 * Flux: 50.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/modifiers/map.js` -> **Severity: 14.569** (Embedded: 0.2881 * Error Risk: 50.5714%)
- `package/lib/_utils/makeAsync.js` -> **Severity: 13.632** (Embedded: 0.2586 * Error Risk: 52.7116%)
- `package/lib/modifiers/pipeline.js` -> **Severity: 8.762** (Embedded: 0.1667 * Error Risk: 52.5692%)
- `package/lib/modifiers/filter.js` -> **Severity: 5.547** (Embedded: 0.1067 * Error Risk: 51.9989%)
- `package/lib/modifiers/take.js` -> **Severity: 5.413** (Embedded: 0.1 * Error Risk: 54.1334%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/modifiers/reduce.js` -> **Severity: 1470.24** (Blast Radius: 18.378 * Doc Risk: 80.0%)
- `package/lib/modifiers/sort.js` -> **Severity: 1470.24** (Blast Radius: 18.378 * Doc Risk: 80.0%)
- `package/lib/creators/fromPromise.js` -> **Severity: 1378.35** (Blast Radius: 18.378 * Doc Risk: 75.0%)
- `package/lib/consumers/v2/wait.js` -> **Severity: 1179.25** (Blast Radius: 23.585 * Doc Risk: 50.0%)
- `package/lib/creators/fromArray.js` -> **Severity: 918.9** (Blast Radius: 18.378 * Doc Risk: 50.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 179 call pairs -- scoped 21.2%, unique 0.0%, ambiguous 0.0%, external 78.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 179 | 21.2% | 0.0% | 0.0% | 78.8% |

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
