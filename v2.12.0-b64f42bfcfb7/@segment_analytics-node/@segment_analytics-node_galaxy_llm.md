# ARCHITECTURAL_BRIEF: @segment_analytics-node
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
- **Scope:** 29 analyzed artifact(s), 1326 LOC.
- **Load-bearing artifact:** `package/src/app/context.ts` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/app/analytics-node.ts` -- pulls in 11 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/src/lib/token-manager.ts` at magnitude 199.28 (structural weight, not risk).
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
| Total Artifacts | 30 |
| Analyzed Artifacts (Scanned) | 29 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 1326 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3169 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0947 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 51.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9674 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 27 | 1326 | 93.1% |
| MARKDOWN | 1 | 0 | 3.4% |
| PLAINTEXT | 1 | 0 | 3.4% |

## 4.1 SOURCE ENCODINGS
All 29 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 45%, Declarative / Non-Code 14%, Interface Declarations Files 10%, Large Core Modules (2) 10%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 27 | 93.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 6.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 73.6 | 11.0 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 58.3 | 14.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 37.8 | 3.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 11.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 3.5 | 82.1 | 30.4 | 31.8 | 20.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 1.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.5 | 20.8 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4 | 3 | 0 | `package/src/app/analytics-node.ts` |
| cleanup | 5 | 4 | 1 | `package/src/plugins/segmentio/publisher.ts` |
| guards | 107 | 10 | 4 | `package/src/lib/token-manager.ts` |
| danger | 11 | 4 | 1 | `package/src/lib/abort.ts` |
| concurrency | 62 | 8 | 5 | `package/src/lib/token-manager.ts` |
| connectivity | 101 | 27 | 9 | `package/src/app/analytics-node.ts` |
| io | 21 | 9 | 2 | `package/src/plugins/segmentio/publisher.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 18 | 5 | 1 | `package/src/lib/token-manager.ts` |
| serialization | 3 | 3 | 0 | `package/src/lib/token-manager.ts` |
| regex | 2 | 2 | 0 | `package/src/lib/create-url.ts` |
| events | 26 | 5 | 3 | `package/src/lib/abort.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 63 | 12 | 10 | `package/src/app/types/params.ts` |
| debt | 4 | 3 | 0 | `package/src/app/analytics-node.ts` |
| mutation | 190 | 20 | 12 | `package/src/lib/token-manager.ts` |
| dead_code | 3 | 3 | 0 | `package/src/index.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 4 | 3 | 0 | `package/src/lib/token-manager.ts` |
| ui | 7 | 1 | 0 | `package/src/lib/token-manager.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/plugins/segmentio/publisher.ts` (Hits: 5)
- `package/src/app/analytics-node.ts` (Hits: 3)
- `package/src/lib/fetch.ts` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **context.ts** (`package/src/app/context.ts`) — 9 inbound connections
2. **index.ts** (`package/src/app/types/index.ts`) — 9 inbound connections
3. **http-client.ts** (`package/src/lib/http-client.ts`) — 7 inbound connections
4. **emitter.ts** (`package/src/app/emitter.ts`) — 4 inbound connections
5. **settings.ts** (`package/src/app/settings.ts`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **analytics-node.ts** (`package/src/app/analytics-node.ts`) — 11 outbound dependencies
2. **publisher.ts** (`package/src/plugins/segmentio/publisher.ts`) — 9 outbound dependencies
3. **index.common.ts** (`package/src/index.common.ts`) — 6 outbound dependencies
4. **token-manager.ts** (`package/src/lib/token-manager.ts`) — 6 outbound dependencies
5. **index.ts** (`package/src/plugins/segmentio/index.ts`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `send` **(Compute Cores)** (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **41.3** | LOC: 119
- `enqueue` **(Defensive Guards)** (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **15.7** | LOC: 59
  * *Intent:* /** * Enqueues the context for future delivery. */
- `constructor` **(Defensive Guards)** (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **13.9** | LOC: 36
- `pollerLoop` **(I/O & Config Routines)** (@ `package/src/lib/token-manager.ts`) -> Impact: **13.1** | LOC: 61
- `detectRuntime` **(I/O & Config Routines)** (@ `package/src/lib/env.ts`) -> Impact: **12.8** | LOC: 36
- `dispatchAndEmit` **(Many-Argument Workhorses)** (@ `package/src/app/dispatch-emit.ts`) -> Impact: **12.6** | LOC: 28
  * *Intent:* /* Dispatch function, but swallow promise rejections and use event emitter instead */
- `constructor` **(Defensive Guards)** (@ `package/src/app/analytics-node.ts`) -> Impact: **11.7** | LOC: 37
- `flush` **(Callbacks & Closures)** (@ `package/src/app/analytics-node.ts`) -> Impact: **11.4** | LOC: 30
  * *Intent:* /** * Call this method to flush all existing events.. * This method also waits for any event method-specific callbacks to be triggered, * and any of t...
- `flush` **(Defensive Guards)** (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **9.9** | LOC: 29
- `handleRateLimited` **(Stateful Encapsulated Methods)** (@ `package/src/lib/token-manager.ts`) -> Impact: **9.3** | LOC: 26

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src/lib` | 10 | 314.65 | 14.22% | 6.44% |
| `package/src/plugins/segmentio` | 3 | 239.38 | 29.66% | 10.51% |
| `package/src/app` | 7 | 216.66 | 6.62% | 1.28% |
| `package/src/app/types` | 4 | 42.5 | 3.36% | 0.0% |
| `package/src` | 2 | 35.0 | 2.56% | 0.0% |
| `package/src/generated` | 1 | 11.52 | 0.0% | 0.0% |
| `package` | 2 | 2.32 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/lib/base-64-encode.ts` -> **37.7541%** Exposure
- `package/src/plugins/segmentio/index.ts` -> **31.5212%** Exposure
- `package/src/lib/abort.ts` -> **17.6759%** Exposure
- `package/src/lib/token-manager.ts` -> **8.996%** Exposure
- `package/src/app/analytics-node.ts` -> **8.9792%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/plugins/segmentio/publisher.ts` -> **99.9658%** Exposure
- `package/src/lib/token-manager.ts` -> **99.8165%** Exposure
- `package/src/lib/abort.ts` -> **96.6729%** Exposure
- `package/src/app/analytics-node.ts` -> **84.7826%** Exposure
- `package/src/lib/http-client.ts` -> **46.609%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/lib/base-64-encode.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/plugins/segmentio/index.ts` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `20` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/src/lib/token-manager.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.731)
- **Top Global Matches:** file_cluster_0: 7.731, file_cluster_16: 7.735, file_cluster_10: 8.632
- **Magnitude:** 199.28 | **LOC:** 328 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 31.593; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pollerLoop` **(I/O & Config Routines)** (Impact: 13.1)
  * `handleRateLimited` **(Stateful Encapsulated Methods)** (Impact: 9.3)
  * `isAccessToken` **(Defensive Guards)** (Impact: 9.0)
  * `convertHeaders` **(Generic / Templated Code)** (Impact: 7.9)
  * `isHeaders` **(Defensive Guards)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 50`, `args: 23`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 5`, `concurrency: 15`, `import: 6`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.593
  * `Choke Point (Betweenness):` 0.010582 | `Ripple Effect (Closeness):` 0.160401
  * `Imports (Out-Degree: 3):` http-client, types, uuid, analytics-core, analytics-generic-utils, jose
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/publisher.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.339)
- **Top Global Matches:** file_cluster_4: 7.339, file_cluster_6: 9.208, file_cluster_16: 13.399
- **Magnitude:** 196.64 | **LOC:** 332 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 14.47; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Compute Cores)** (Impact: 41.3)
  * `enqueue` **(Defensive Guards)** (Impact: 15.7)
    * *Intent:* /** * Enqueues the context for future delivery. */
  * `constructor` **(Defensive Guards)** (Impact: 13.9)
  * `flush` **(Defensive Guards)** (Impact: 9.9)
  * `createBatch` **(Stateful Encapsulated Methods)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 39`, `args: 14`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 14`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.47
  * `Choke Point (Betweenness):` 0.042989 | `Ripple Effect (Closeness):` 0.109422
  * `Imports (Out-Degree: 7):` context, emitter, create-url, http-client, token-manager, types, context-batch, analytics-core...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/analytics-node.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.595)
- **Top Global Matches:** file_cluster_15: 6.595, file_cluster_10: 7.254, file_cluster_16: 7.677
- **Magnitude:** 145.74 | **LOC:** 351 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 32.827; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Mutation Surface (formerly State Flux) (84.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.3%)
- **Documentation Coverage:** 20.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 11.7)
  * `flush` **(Callbacks & Closures)** (Impact: 11.4)
    * *Intent:* /** * Call this method to flush all existing events.. * This method also waits for any event method-...
  * `screen` **(Defensive Guards)** (Impact: 8.1)
    * *Intent:* /** * Records screen views on your app, along with optional extra information * about the screen vie...
  * `page` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * The page method lets you record page views on your website, along with optional extra informat...
  * `_dispatch` **(Stateful Encapsulated Methods)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 48`, `args: 25`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 13`, `import: 11`
* *Defense:* `safety: 13`, `doc: 10`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 32.827
  * `Choke Point (Betweenness):` 0.199735 | `Ripple Effect (Closeness):` 0.165899
  * `Imports (Out-Degree: 10):` version, http-client, segmentio, context, dispatch-emit, emitter, event-factory, event-queue...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/lib/abort.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.04)
- **Top Global Matches:** file_cluster_5: 7.04, file_cluster_12: 8.643, file_cluster_7: 9.941
- **Magnitude:** 36.14 | **LOC:** 78 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 60.217; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.7%), Guard Balance (formerly Safety Score) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (46.7%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `abortSignalAfterTimeout` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /** */
  * `dispatchEvent` **(Parameter Forwarders)** (Impact: 3.4)
  * `abort` **(Interface Declarations)** (Impact: 2.3)
  * `removeEventListener` **(Generic / Templated Code)** (Impact: 1.6)
  * `addEventListener` **(Generic / Templated Code)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 20`, `args: 10`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 2`, `doc: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.217
  * `Choke Point (Betweenness):` 0.012566 | `Ripple Effect (Closeness):` 0.222291
  * `Imports (Out-Degree: 1):` env, analytics-generic-utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/lib/http-client.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.479)
- **Top Global Matches:** file_cluster_5: 7.479, file_cluster_12: 9.659, file_cluster_7: 9.92
- **Magnitude:** 35.46 | **LOC:** 106 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 112.676; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (62.8%), Guard Balance (formerly Safety Score) (58.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeRequest` **(Stateful Encapsulated Methods)** (Impact: 5.7)
  * `constructor` **(Defensive Guards)** (Impact: 4.4)
  * `makeRequest` **(Callbacks & Closures)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 10
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 23`, `args: 8`, `func_start: 3`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 5`, `import: 2`
* *Defense:* `safety: 2`, `doc: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 112.676
  * `Choke Point (Betweenness):` 0.05754 | `Ripple Effect (Closeness):` 0.296703
  * `Imports (Out-Degree: 2):` abort, fetch
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/context-batch.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.849)
- **Top Global Matches:** file_cluster_11: 5.849, file_cluster_16: 7.032, file_cluster_15: 7.093
- **Magnitude:** 25.98 | **LOC:** 72 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 14.085; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (35.1%), Mutation Surface (formerly State Flux) (34.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tryAdd` **(Compute Cores)** (Impact: 7.1)
  * `constructor` **(State Mutators)** (Impact: 1.6)
  * `calculateSize` **(Encapsulated Accessors)** (Impact: 1.6)
  * `getEvents` **(Interface Declarations)** (Impact: 1.2)
  * `length` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 21`, `args: 11`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.085
  * `Choke Point (Betweenness):` 0.006173 | `Ripple Effect (Closeness):` 0.095238
  * `Imports (Out-Degree: 3):` context, types, uuid
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/dispatch-emit.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.875)
- **Top Global Matches:** file_cluster_10: 6.875, file_cluster_15: 8.474, file_cluster_13: 8.502
- **Magnitude:** 21.56 | **LOC:** 43 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 15.118; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (76.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (31.8%), Complexity Load (formerly Cognitive Load) (15.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchAndEmit` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* /* Dispatch function, but swallow promise rejections and use event emitter instead */
  * `normalizeDispatchCb` **(Callbacks & Closures)** (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 20`, `args: 4`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.128571
  * `Imports (Out-Degree: 4):` context, emitter, event-queue, types, analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.common.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.094)
- **Top Global Matches:** file_cluster_2: 6.094, file_cluster_17: 6.424, file_cluster_13: 6.929
- **Magnitude:** 21.44 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 22.807; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.807
  * `Choke Point (Betweenness):` 0.031746 | `Ripple Effect (Closeness):` 0.035714
  * `Imports (Out-Degree: 6):` analytics-node, context, settings, types, http-client, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/emitter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.44)
- **Top Global Matches:** file_cluster_0: 5.44, file_cluster_13: 7.901, file_cluster_2: 9.123
- **Magnitude:** 17.38 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 22.23; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (36.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.23
  * `Choke Point (Betweenness):` 0.017416 | `Ripple Effect (Closeness):` 0.171429
  * `Imports (Out-Degree: 3):` context, settings, types, analytics-core, analytics-generic-utils
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.987)
- **Top Global Matches:** file_cluster_0: 6.987, file_cluster_10: 7.825, file_cluster_13: 8.899
- **Magnitude:** 16.76 | **LOC:** 67 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 15.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (48.2%), Debt Markers (formerly Tech Debt) (31.5%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeEvent` **(State Mutators)** (Impact: 3.3)
  * `createNodePlugin` **(Callbacks & Closures)** (Impact: 2.4)
  * `createConfiguredNodePlugin` **(Callbacks & Closures)** (Impact: 2.2)
  * `action` **(Generic / Templated Code)** (Impact: 1.6)
  * `isLoaded` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 20`, `args: 6`, `func_start: 5`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.118
  * `Choke Point (Betweenness):` 0.058201 | `Ripple Effect (Closeness):` 0.128571
  * `Imports (Out-Degree: 6):` context, emitter, types, version, env, publisher
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/lib/env.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.414)
- **Top Global Matches:** file_cluster_9: 6.414, file_cluster_16: 12.396, file_cluster_15: 12.507
- **Magnitude:** 15.48 | **LOC:** 46 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 65.651; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (34.1%), Complexity Load (formerly Cognitive Load) (10.0%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `detectRuntime` **(I/O & Config Routines)** (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 12`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.210084
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/app/types/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.965)
- **Top Global Matches:** file_cluster_2: 4.965, file_cluster_17: 5.437, file_cluster_13: 5.927
- **Magnitude:** 14.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **3**; blast radius 99.896; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 99.896
  * `Choke Point (Betweenness):` 0.180556 | `Ripple Effect (Closeness):` 0.342857
  * `Imports (Out-Degree: 3):` params, plugin, segment-event
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `package/src/app/types/segment-event.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.875)
- **Top Global Matches:** file_cluster_0: 5.875, file_cluster_13: 7.959, file_cluster_2: 9.435
- **Magnitude:** 13.6 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 40.632; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.215561
  * `Imports (Out-Degree: 0):` analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.837)
- **Top Global Matches:** file_cluster_2: 5.837, file_cluster_17: 6.479, file_cluster_13: 6.922
- **Magnitude:** 13.56 | **LOC:** 6 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 12.328; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (30.8%), Connectivity (formerly Api Exposure) (5.6%), Complexity Load (formerly Cognitive Load) (5.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.328
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/types/plugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.018)
- **Top Global Matches:** file_cluster_0: 7.018, file_cluster_13: 10.006, file_cluster_2: 11.663
- **Magnitude:** 13.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 40.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.632
  * `Choke Point (Betweenness):` 0.160714 | `Ripple Effect (Closeness):` 0.205714
  * `Imports (Out-Degree: 2):` analytics-node, context, analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/event-factory.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.774)
- **Top Global Matches:** file_cluster_0: 6.774, file_cluster_10: 11.299, file_cluster_13: 11.722
- **Magnitude:** 13.02 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 15.118; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `screen` **(Generic / Templated Code)** (Impact: 2.1)
  * `onFinishedEvent` **(Callbacks & Closures)** (Impact: 1.6)
  * `page` **(Generic / Templated Code)** (Impact: 1.5)
  * `constructor` **(Callbacks & Closures)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 8`, `func_start: 4`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.118
  * `Choke Point (Betweenness):` 0.022487 | `Ripple Effect (Closeness):` 0.128571
  * `Imports (Out-Degree: 2):` get-message-id, types, analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/generated/version.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.176)
- **Top Global Matches:** file_cluster_2: 4.176, file_cluster_17: 5.367, file_cluster_13: 5.86
- **Magnitude:** 11.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 17.26; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (21.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.26
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.147213
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/lib/uuid.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.407)
- **Top Global Matches:** file_cluster_13: 5.407, file_cluster_2: 7.551, file_cluster_17: 8.202
- **Magnitude:** 11.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 41.21; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 41.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.196126
  * `Imports (Out-Degree: 0):` uuid
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/app/event-queue.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.855)
- **Top Global Matches:** file_cluster_0: 6.855, file_cluster_15: 9.421, file_cluster_13: 9.513
- **Magnitude:** 10.2 | **LOC:** 24 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 18.331; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.3%), Connectivity (formerly Api Exposure) (34.1%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getAttempts` **(Defensive Guards)** (Impact: 3.0)
    * *Intent:* // do not use an internal "seen" map
  * `updateAttempts` **(Parameter Forwarders)** (Impact: 1.6)
  * `constructor` **(I/O & Config Routines)** (Impact: 1.1)
  * `constructor` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 12`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.331
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.138996
  * `Imports (Out-Degree: 2):` types, context, analytics-core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/lib/create-url.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.93)
- **Top Global Matches:** file_cluster_10: 7.93, file_cluster_15: 9.853, file_cluster_11: 10.815
- **Magnitude:** 8.28 | **LOC:** 12 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 14.085; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Complexity Load (formerly Cognitive Load) (4.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tryCreateFormattedUrl` **(Callbacks & Closures)** (Impact: 5.3)
    * *Intent:* /** * */
  * `stripTrailingSlash` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.100595
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/settings.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.157)
- **Top Global Matches:** file_cluster_10: 7.157, file_cluster_13: 7.396, file_cluster_15: 7.909
- **Magnitude:** 5.52 | **LOC:** 60 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 35.126; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (35.3%), Complexity Load (formerly Cognitive Load) (3.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateSettings` **(Defensive Guards)** (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 2`, `import: 3`
* *Defense:* `safety: 1`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.126
  * `Choke Point (Betweenness):` 0.041005 | `Ripple Effect (Closeness):` 0.212121
  * `Imports (Out-Degree: 2):` http-client, types, analytics-core
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/app/context.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.608)
- **Top Global Matches:** file_cluster_0: 6.608, file_cluster_11: 9.249, file_cluster_13: 9.416
- **Magnitude:** 3.24 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **2**; blast radius 60.809; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (40.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `system` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.809
  * `Choke Point (Betweenness):` 0.006834 | `Ripple Effect (Closeness):` 0.321429
  * `Imports (Out-Degree: 1):` types, analytics-core
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `package/src/lib/base-64-encode.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.19)
- **Top Global Matches:** file_cluster_10: 5.19, file_cluster_13: 8.878, file_cluster_2: 8.95
- **Magnitude:** 2.68 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 12.328; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (37.8%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `b64encode` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* /** * Base64 encoder that works in browser, worker, node runtimes. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.328
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/lib/fetch.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.872)
- **Top Global Matches:** file_cluster_10: 6.872, file_cluster_13: 10.069, file_cluster_2: 10.131
- **Magnitude:** 2.68 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 60.217; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch` **(Callbacks & Closures)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.206633
  * `Imports (Out-Degree: 1):` http-client
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/lib/get-message-id.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.693)
- **Top Global Matches:** file_cluster_10: 5.693, file_cluster_2: 9.201, file_cluster_13: 9.25
- **Magnitude:** 2.18 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createMessageId` **(Callbacks & Closures)** (Impact: 1.1)
    * *Intent:* /** * get a unique messageId with a very low chance of collisions */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.753
  * `Choke Point (Betweenness):` 0.007937 | `Ripple Effect (Closeness):` 0.113881
  * `Imports (Out-Degree: 1):` uuid
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/src/lib/token-manager.ts` (TYPESCRIPT) | Magnitude: 199.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 248, structural_boundaries: 50, branch: 41, core_var_decl: 29

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/app/analytics-node.ts` -> **Severity: 16.934** (Bridge: 0.1997 * Flux: 84.7826%)
- `package/src/plugins/segmentio/publisher.ts` -> **Severity: 4.297** (Bridge: 0.043 * Flux: 99.9658%)
- `package/src/lib/http-client.ts` -> **Severity: 2.682** (Bridge: 0.0575 * Flux: 46.609%)
- `package/src/lib/abort.ts` -> **Severity: 1.215** (Bridge: 0.0126 * Flux: 96.6729%)
- `package/src/lib/token-manager.ts` -> **Severity: 1.056** (Bridge: 0.0106 * Flux: 99.8165%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/lib/http-client.ts` -> **Severity: 17.298** (Embedded: 0.2967 * Error Risk: 58.3019%)
- `package/src/lib/abort.ts` -> **Severity: 12.527** (Embedded: 0.2223 * Error Risk: 56.3543%)
- `package/src/lib/token-manager.ts` -> **Severity: 9.063** (Embedded: 0.1604 * Error Risk: 56.5028%)
- `package/src/app/analytics-node.ts` -> **Severity: 8.352** (Embedded: 0.1659 * Error Risk: 50.3425%)
- `package/src/app/event-queue.ts` -> **Severity: 6.851** (Embedded: 0.139 * Error Risk: 49.2858%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/lib/env.ts` -> **Severity: 6565.1** (Blast Radius: 65.651 * Doc Risk: 100.0%)
- `package/src/app/context.ts` -> **Severity: 6080.9** (Blast Radius: 60.809 * Doc Risk: 100.0%)
- `package/src/lib/fetch.ts` -> **Severity: 6021.7** (Blast Radius: 60.217 * Doc Risk: 100.0%)
- `package/src/lib/abort.ts` -> **Severity: 4516.275** (Blast Radius: 60.217 * Doc Risk: 75.0%)
- `package/src/lib/types.ts` -> **Severity: 4119.6** (Blast Radius: 41.196 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 179 call pairs -- scoped 37.4%, unique 0.0%, ambiguous 3.9%, external 58.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 179 | 37.4% | 0.0% | 3.9% | 58.7% |

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
