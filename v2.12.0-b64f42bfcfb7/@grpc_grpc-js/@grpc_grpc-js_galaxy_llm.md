# ARCHITECTURAL_BRIEF: @grpc_grpc-js
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
- **Scope:** 174 analyzed artifact(s), 19853 LOC.
- **Load-bearing artifact:** `package/src/constants.ts` -- 38 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/generated/orca.ts` -- pulls in 53 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/src/server.ts` at magnitude 1190.5 (structural weight, not risk).
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
| Total Artifacts | 177 |
| Analyzed Artifacts (Scanned) | 174 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 19853 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5119 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3467 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 28.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7065 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 168 | 19309 | 96.6% |
| PROTO | 4 | 544 | 2.3% |
| MARKDOWN | 1 | 0 | 0.6% |
| PLAINTEXT | 1 | 0 | 0.6% |

## 4.1 SOURCE ENCODINGS
All 174 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 49%, Large Core Modules (3) 23%, Data / Markup / Trivial 15%, Compute Cores Files 4%, State Mutators Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 172 | 98.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.7 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 20.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 17.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 96.6 | 36.9 | 34.1 | 35.7 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.4 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 27.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 79 | 25 | 1 | `package/src/channelz.ts` |
| cleanup | 90 | 24 | 1 | `package/src/server.ts` |
| guards | 1311 | 62 | 27 | `package/src/server.ts` |
| danger | 391 | 43 | 7 | `package/src/server.ts` |
| concurrency | 249 | 25 | 4 | `package/src/server.ts` |
| connectivity | 1011 | 168 | 15 | `package/src/call-interface.ts` |
| io | 124 | 23 | 1 | `package/src/server.ts` |
| crypto | 6 | 6 | 0 | `package/src/auth-context.ts` |
| ipc | 0 | 0 | 0 | - |
| time | 122 | 19 | 1 | `package/src/server.ts` |
| serialization | 11 | 9 | 0 | `package/src/server.ts` |
| regex | 20 | 15 | 0 | `package/src/http_proxy.ts` |
| events | 113 | 15 | 0 | `package/src/server.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 1006 | 113 | 16 | `package/src/generated/validate/StringRules.ts` |
| debt | 105 | 14 | 0 | `package/src/server-call.ts` |
| mutation | 3052 | 77 | 59 | `package/src/server.ts` |
| dead_code | 3 | 2 | 0 | `package/src/metadata.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 43 | 14 | 0 | `package/src/load-balancer-outlier-detection.ts` |
| ui | 24 | 4 | 0 | `package/src/retrying-call.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/server.ts` (Hits: 27)
- `package/src/http_proxy.ts` (Hits: 15)
- `package/src/server-call.ts` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **constants.ts** (`package/src/constants.ts`) — 38 inbound connections
2. **call-interface.ts** (`package/src/call-interface.ts`) — 32 inbound connections
3. **metadata.ts** (`package/src/metadata.ts`) — 26 inbound connections
4. **channel-options.ts** (`package/src/channel-options.ts`) — 25 inbound connections
5. **logging.ts** (`package/src/logging.ts`) — 25 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **orca.ts** (`package/src/generated/orca.ts`) — 53 outbound dependencies
2. **channelz.ts** (`package/src/generated/channelz.ts`) — 49 outbound dependencies
3. **channelz.ts** (`package/src/channelz.ts`) — 38 outbound dependencies
4. **index.ts** (`package/src/index.ts`) — 32 outbound dependencies
5. **internal-channel.ts** (`package/src/internal-channel.ts`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `constructor` **(Many-Argument Workhorses)** (@ `package/src/subchannel-call.ts`) -> Impact: **88.3** | LOC: 199
- `constructor` **(Many-Argument Workhorses)** (@ `package/src/internal-channel.ts`) -> Impact: **83.0** | LOC: 221
- `updateAddressList` **(Many-Argument Workhorses)** (@ `package/src/load-balancer-weighted-round-robin.ts`) -> Impact: **53.9** | LOC: 95
- `constructor` **(Many-Argument Workhorses)** (@ `package/src/transport.ts`) -> Impact: **51.0** | LOC: 125
- `createSession` **(Defensive Guards)** (@ `package/src/transport.ts`) -> Impact: **48.9** | LOC: 97
- `_equals` **(Compute Cores)** (@ `package/src/server-credentials.ts`) -> Impact: **47.4** | LOC: 71
  * *Intent:* /** * Checks equality by checking the options that are actually set by * createSsl. */
- `_channelzSessionHandler` **(Defensive Guards)** (@ `package/src/server.ts`) -> Impact: **47.0** | LOC: 204
- `_sessionHandler` **(Defensive Guards)** (@ `package/src/server.ts`) -> Impact: **43.5** | LOC: 162
- `transitionToState` **(Many-Argument Workhorses)** (@ `package/src/subchannel.ts`) -> Impact: **43.5** | LOC: 70
  * *Intent:* /** * Initiate a state transition from any element of oldStates to the new * state. If the current connectivityState is not in oldStates, do nothing. ...
- `handleProcessedStatus` **(Many-Argument Workhorses)** (@ `package/src/retrying-call.ts`) -> Impact: **43.3** | LOC: 66

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src` | 67 | 11100.9 | 30.02% | 9.3% |
| `package/src/generated/google/protobuf` | 37 | 706.14 | 6.86% | 0.0% |
| `package/src/generated/grpc/channelz/v1` | 35 | 697.06 | 4.06% | 0.0% |
| `package/src/generated/validate` | 24 | 416.16 | 4.62% | 0.0% |
| `package/src/generated` | 2 | 36.86 | 0.0% | 0.0% |
| `package/src/generated/xds/service/orca/v3` | 2 | 35.0 | 3.64% | 0.0% |
| `package/proto` | 1 | 20.14 | 0.0% | 0.0% |
| `package/proto/protoc-gen-validate/validate` | 1 | 20.06 | 0.0% | 0.0% |
| `package/src/generated/xds/data/orca/v3` | 1 | 17.46 | 5.1% | 0.0% |
| `package/proto/xds/xds/data/orca/v3` | 1 | 15.38 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/call.ts` -> **100.0%** Exposure
- `package/src/object-stream.ts` -> **100.0%** Exposure
- `package/src/server-call.ts` -> **100.0%** Exposure
- `package/src/channel-credentials.ts` -> **85.554%** Exposure
- `package/src/client.ts` -> **64.2543%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/filter-stack.ts` -> **100.0%** Exposure
- `package/src/stream-decoder.ts` -> **100.0%** Exposure
- `package/src/subchannel-call.ts` -> **99.9993%** Exposure
- `package/src/backoff-timeout.ts` -> **99.9975%** Exposure
- `package/src/logging.ts` -> **99.9965%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/server-call.ts` -> **0** Orphaned Functions | **36** Duplicates
- `package/src/call.ts` -> **0** Orphaned Functions | **18** Duplicates
- `package/src/server.ts` -> **0** Orphaned Functions | **15** Duplicates
- `package/src/client.ts` -> **0** Orphaned Functions | **8** Duplicates
- `package/src/channel-credentials.ts` -> **0** Orphaned Functions | **7** Duplicates

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
- **Unknown Dependencies:** `78` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/src/server.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.087)
- **Top Global Matches:** file_cluster_12: 7.087, file_cluster_4: 8.839, file_cluster_5: 9.171
- **Magnitude:** 1190.5 | **LOC:** 2213 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **20**; blast radius 6.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.1%), Concurrency Surface (formerly Concurrency) (82.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (63.6%)
- **Documentation Coverage:** 90.5172% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_channelzSessionHandler` **(Defensive Guards)** (Impact: 47.0)
  * `_sessionHandler` **(Defensive Guards)** (Impact: 43.5)
  * `addService` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `_channelzHandler` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `bindAsync` **(Many-Argument Workhorses)** (Impact: 30.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 300
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 250`, `args: 161`, `func_start: 99`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 122`, `planned_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `io: 27`, `api: 18`, `concurrency: 34`, `import: 20`
* *Defense:* `safety: 68`, `doc: 20`, `immutability_locks: 7`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.494
  * `Choke Point (Betweenness):` 0.017714 | `Ripple Effect (Closeness):` 0.085439
  * `Imports (Out-Degree: 15):` call, call-interface, channel-options, channelz, constants, logging, make-client, metadata...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/server-interceptors.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.815)
- **Top Global Matches:** file_cluster_12: 5.815, file_cluster_5: 8.568, file_cluster_7: 9.009
- **Magnitude:** 546.64 | **LOC:** 1072 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 4.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 82.0225% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `sendStatus` **(Defensive Guards)** (Impact: 22.7)
  * `decompressMessage` **(Stateful Encapsulated Methods)** (Impact: 19.4)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 17.9)
  * `start` **(Defensive Guards)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 216`, `args: 107`, `func_start: 79`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 66`, `planned_debt: 1`
* *Architecture:* `io: 9`, `api: 30`, `concurrency: 6`, `import: 16`
* *Defense:* `safety: 41`, `doc: 17`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.302
  * `Choke Point (Betweenness):` 0.009261 | `Ripple Effect (Closeness):` 0.097543
  * `Imports (Out-Degree: 13):` auth-context, call-interface, channel-options, constants, deadline, error, logging, make-client...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/retrying-call.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_12: 6.526, file_cluster_16: 7.976, file_cluster_4: 8.498
- **Magnitude:** 540.04 | **LOC:** 924 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 3.233; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleProcessedStatus` **(Many-Argument Workhorses)** (Impact: 43.3)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 30.4)
  * `handleChildStatus` **(Many-Argument Workhorses)** (Impact: 25.4)
  * `maybeRetryCall` **(Stateful Encapsulated Methods)** (Impact: 22.7)
  * `sendMessageWithContext` **(Compute Cores)** (Impact: 20.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 100`, `args: 54`, `func_start: 47`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 67`
* *Architecture:* `api: 11`, `concurrency: 3`, `import: 10`
* *Defense:* `safety: 24`, `doc: 9`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.233
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.061606
  * `Imports (Out-Degree: 10):` auth-context, call-credentials, call-interface, constants, deadline, internal-channel, load-balancing-call, logging...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/transport.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.06)
- **Top Global Matches:** file_cluster_12: 8.06, file_cluster_4: 8.234, file_cluster_16: 8.61
- **Magnitude:** 492.56 | **LOC:** 826 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **18**; blast radius 4.949; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Concurrency Surface (formerly Concurrency) (96.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.7%)
- **Documentation Coverage:** 92.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `createSession` **(Defensive Guards)** (Impact: 48.9)
  * `createCall` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `getChannelzInfo` **(I/O & Config Routines)** (Impact: 16.8)
  * `maybeSendPing` **(Defensive Guards)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 101`, `args: 72`, `func_start: 53`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 17`, `import: 19`
* *Defense:* `safety: 38`, `doc: 10`, `immutability_locks: 4`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.949
  * `Choke Point (Betweenness):` 0.013088 | `Ripple Effect (Closeness):` 0.089353
  * `Imports (Out-Degree: 15):` package.json, auth-context, call-interface, call-number, channel-credentials, channel-options, channelz, constants...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/src/internal-channel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.068)
- **Top Global Matches:** file_cluster_16: 7.068, file_cluster_15: 7.807, file_cluster_4: 8.226
- **Magnitude:** 439.2 | **LOC:** 879 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **27**; blast radius 4.643; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 90.7407% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 83.0)
  * `watchConnectivityState` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `createCall` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `getConfig` **(Compute Cores)** (Impact: 11.5)
  * `updateState` **(Stateful Encapsulated Methods)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 92`, `args: 51`, `func_start: 40`, `class_start: 8`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 15`, `concurrency: 3`, `import: 27`
* *Defense:* `safety: 17`, `doc: 6`, `immutability_locks: 17`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.643
  * `Choke Point (Betweenness):` 0.02618 | `Ripple Effect (Closeness):` 0.080173
  * `Imports (Out-Degree: 27):` call-credentials, call-interface, call-number, channel-credentials, channel-options, channelz, compression-filter, connectivity-state...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/src/client.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.634)
- **Top Global Matches:** file_cluster_5: 6.634, file_cluster_12: 8.304, file_cluster_0: 9.845
- **Magnitude:** 417.46 | **LOC:** 717 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 5.177; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (64.3%), Guard Balance (formerly Safety Score) (58.6%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeUnaryRequest` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `makeClientStreamRequest` **(Many-Argument Workhorses)** (Impact: 36.9)
  * `checkOptionalUnaryResponseArguments` **(Stateful Encapsulated Methods)** (Impact: 25.5)
  * `makeServerStreamRequest` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `makeBidiStreamRequest` **(Many-Argument Workhorses)** (Impact: 23.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 85`, `args: 38`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 36`, `duplicate_logic: 8`
* *Architecture:* `io: 4`, `api: 10`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 17`, `doc: 7`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.177
  * `Choke Point (Betweenness):` 0.003405 | `Ripple Effect (Closeness):` 0.083609
  * `Imports (Out-Degree: 13):` call, call-credentials, call-interface, channel, channel-credentials, channel-options, client-interceptors, connectivity-state...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-outlier-detection.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.83)
- **Top Global Matches:** file_cluster_16: 6.83, file_cluster_12: 6.946, file_cluster_15: 7.014
- **Magnitude:** 416.56 | **LOC:** 841 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 3.348; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateAddressList` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `createFromJson` **(I/O & Config Routines)** (Impact: 24.3)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `runSuccessRateCheck` **(Compute Cores)** (Impact: 21.8)
  * `validatePositiveDuration` **(Many-Argument Workhorses)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 82`, `args: 52`, `func_start: 49`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`
* *Architecture:* `api: 16`, `concurrency: 2`, `import: 13`
* *Defense:* `safety: 12`, `immutability_locks: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.348
  * `Choke Point (Betweenness):` 0.000571 | `Ripple Effect (Closeness):` 0.058235
  * `Imports (Out-Degree: 13):` call-interface, channel-options, connectivity-state, constants, duration, experimental, load-balancer, load-balancer-child-handler...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/subchannel-call.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.639)
- **Top Global Matches:** file_cluster_12: 6.639, file_cluster_4: 7.947, file_cluster_16: 8.986
- **Magnitude:** 397.0 | **LOC:** 623 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 4.007; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.0%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 88.3)
  * `mapHttpStatusCode` **(Compute Cores)** (Impact: 17.2)
  * `handleTrailers` **(Stateful Encapsulated Methods)** (Impact: 12.4)
  * `sendMessageWithContext` **(Defensive Guards)** (Impact: 12.0)
  * `cb` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 74`, `args: 42`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 60`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 15`, `doc: 4`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.007
  * `Choke Point (Betweenness):` 0.000514 | `Ripple Effect (Closeness):` 0.076505
  * `Imports (Out-Degree: 7):` auth-context, call-interface, constants, logging, metadata, stream-decoder, transport, http2...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-weighted-round-robin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.917)
- **Top Global Matches:** file_cluster_4: 5.917, file_cluster_12: 8.41, file_cluster_16: 10.201
- **Magnitude:** 350.5 | **LOC:** 495 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 3.203; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.7%), Guard Balance (formerly Safety Score) (61.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateAddressList` **(Many-Argument Workhorses)** (Impact: 53.9)
  * `parseDurationField` **(Compute Cores)** (Impact: 20.1)
  * `constructor` **(Defensive Guards)** (Impact: 19.3)
  * `calculateAndUpdateState` **(I/O & Config Routines)** (Impact: 19.1)
  * `updateWeight` **(Defensive Guards)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 72`, `args: 37`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 37`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 10`, `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.203
  * `Choke Point (Betweenness):` 0.001686 | `Ripple Effect (Closeness):` 0.056821
  * `Imports (Out-Degree: 13):` call-interface, channel-options, connectivity-state, constants, duration, OrcaLoadReport, load-balancer, load-balancer-pick-first...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/client-interceptors.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.257)
- **Top Global Matches:** file_cluster_5: 7.257, file_cluster_12: 7.324, file_cluster_7: 9.072
- **Magnitude:** 324.0 | **LOC:** 586 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 4.046; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.5%), Guard Balance (formerly Safety Score) (55.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (36.9%)
- **Documentation Coverage:** 61.7647% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Defensive Guards)** (Impact: 29.7)
  * `start` **(Defensive Guards)** (Impact: 22.5)
  * `start` **(Defensive Guards)** (Impact: 21.8)
  * `getInterceptingCall` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 128`, `args: 74`, `func_start: 55`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 27`
* *Architecture:* `io: 3`, `api: 24`, `import: 8`
* *Defense:* `safety: 41`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.046
  * `Choke Point (Betweenness):` 0.003164 | `Ripple Effect (Closeness):` 0.067271
  * `Imports (Out-Degree: 8):` auth-context, call-interface, channel, client, constants, error, make-client, metadata
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/service-config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.973)
- **Top Global Matches:** file_cluster_3: 6.973, file_cluster_8: 20.868, file_cluster_6: 33.677
- **Magnitude:** 319.24 | **LOC:** 565 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 5.145; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.6%), Connectivity (formerly Api Exposure) (54.5%)
- **Documentation Coverage:** 76.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateMethodConfig` **(Compute Cores)** (Impact: 40.3)
  * `validateRetryPolicy` **(Compute Cores)** (Impact: 36.3)
  * `validateCanaryConfig` **(Compute Cores)** (Impact: 33.0)
  * `validateHedgingPolicy` **(Compute Cores)** (Impact: 28.0)
  * `validateServiceConfig` **(Compute Cores)** (Impact: 26.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 41`, `args: 10`, `func_start: 10`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 22`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.145
  * `Choke Point (Betweenness):` 0.000723 | `Ripple Effect (Closeness):` 0.099441
  * `Imports (Out-Degree: 2):` constants, duration, os
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/src/channel-credentials.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.243)
- **Top Global Matches:** file_cluster_12: 7.243, file_cluster_16: 7.879, file_cluster_15: 8.138
- **Magnitude:** 313.18 | **LOC:** 524 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **10**; blast radius 7.283; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.2%), Debt Markers (formerly Tech Debt) (85.6%), Mutation Surface (formerly State Flux) (83.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 81.9672% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createSsl` **(Stateful Encapsulated Methods)** (Impact: 32.7)
    * *Intent:* /** * Return a new ChannelCredentials instance with a given set of credentials. * The resulting inst...
  * `getConnectionOptions` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `_equals` **(Defensive Guards)** (Impact: 11.9)
  * `connect` **(Callbacks & Closures)** (Impact: 10.3)
  * `_equals` **(Compute Cores)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 102`, `args: 65`, `func_start: 57`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 15`, `duplicate_logic: 7`
* *Architecture:* `api: 9`, `concurrency: 16`, `import: 10`
* *Defense:* `safety: 24`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.283
  * `Choke Point (Betweenness):` 0.003976 | `Ripple Effect (Closeness):` 0.109394
  * `Imports (Out-Degree: 8):` call-credentials, certificate-provider, channel-options, constants, logging, resolver, tls-helpers, uri-parser...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `package/src/channelz.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.639)
- **Top Global Matches:** file_cluster_0: 6.639, file_cluster_15: 7.19, file_cluster_11: 8.222
- **Magnitude:** 301.18 | **LOC:** 910 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **38**; blast radius 7.067; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.3%), Connectivity (formerly Api Exposure) (66.6%), Guard Balance (formerly Safety Score) (53.7%)
- **Documentation Coverage:** 92.4528% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetSocket` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `addTrace` **(Defensive Guards)** (Impact: 14.9)
  * `ipAddressStringToBuffer` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* /** * Converts an IPv4 or IPv6 address from string representation to binary * representation */
  * `connectivityStateToMessage` **(Compute Cores)** (Impact: 12.8)
  * `GetServerSockets` **(Many-Argument Workhorses)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 185`, `args: 56`, `func_start: 47`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 31`, `import: 39`
* *Defense:* `safety: 8`, `doc: 6`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.067
  * `Choke Point (Betweenness):` 0.088615 | `Ripple Effect (Closeness):` 0.103586
  * `Imports (Out-Degree: 35):` admin, connectivity-state, constants, channelz, Timestamp, Address, Channel, ChannelConnectivityState...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-pick-first.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.028)
- **Top Global Matches:** file_cluster_16: 6.028, file_cluster_15: 6.912, file_cluster_11: 7.291
- **Magnitude:** 286.4 | **LOC:** 663 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 3.86; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 70.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onSubchannelStateUpdate` **(Stateful Encapsulated Methods)** (Impact: 26.2)
  * `updateAddressList` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `interleaveAddressFamilies` **(Compute Cores)** (Impact: 18.5)
    * *Intent:* /** * Interleave addresses in addressList by family in accordance with RFC-8304 section 4 */
  * `calculateAndReportNewState` **(I/O & Config Routines)** (Impact: 15.2)
  * `connectToAddressList` **(Stateful Encapsulated Methods)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 63`, `args: 50`, `func_start: 41`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`
* *Architecture:* `api: 13`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 5`, `doc: 18`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.86
  * `Choke Point (Betweenness):` 0.000405 | `Ripple Effect (Closeness):` 0.061284
  * `Imports (Out-Degree: 9):` call-interface, channel-options, connectivity-state, constants, load-balancer, logging, picker, subchannel-address...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/compression-filter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.955)
- **Top Global Matches:** file_cluster_0: 6.955, file_cluster_16: 9.001, file_cluster_10: 9.254
- **Magnitude:** 253.74 | **LOC:** 359 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 3.392; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (82.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 17.7)
  * `getCompressionHandler` **(Compute Cores)** (Impact: 11.0)
  * `sendMessage` **(Defensive Guards)** (Impact: 9.8)
  * `receiveMetadata` **(Compute Cores)** (Impact: 8.6)
  * `writeMessage` **(Generic / Templated Code)** (Impact: 5.7)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 78
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 66`, `args: 35`, `func_start: 25`, `class_start: 7`
* *Risk/State:* `state_mutation: 19`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 33`, `import: 9`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.392
  * `Choke Point (Betweenness):` 0.000237 | `Ripple Effect (Closeness):` 0.063271
  * `Imports (Out-Degree: 8):` call-interface, channel, channel-options, compression-algorithms, constants, filter, logging, metadata...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/subchannel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.302)
- **Top Global Matches:** file_cluster_16: 7.302, file_cluster_15: 7.573, file_cluster_11: 7.824
- **Magnitude:** 247.38 | **LOC:** 560 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **16**; blast radius 5.044; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 72.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transitionToState` **(Many-Argument Workhorses)** (Impact: 43.5)
    * *Intent:* /** * Initiate a state transition from any element of oldStates to the new * state. If the current c...
  * `createCall` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 12.0)
    * *Intent:* /** * A class representing a connection to a single backend. * will connect to * for this subchannel...
  * `startConnectingInternal` **(I/O & Config Routines)** (Impact: 9.8)
  * `onCallEnd` **(Callbacks & Closures)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 66`, `args: 43`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 23`, `import: 17`
* *Defense:* `safety: 3`, `doc: 14`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.044
  * `Choke Point (Betweenness):` 0.011515 | `Ripple Effect (Closeness):` 0.087352
  * `Imports (Out-Degree: 16):` backoff-timeout, call-credentials, channel, channel-credentials, channel-options, channelz, connectivity-state, constants...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/single-subchannel-channel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.038)
- **Top Global Matches:** file_cluster_15: 7.038, file_cluster_11: 7.682, file_cluster_16: 8.031
- **Magnitude:** 230.2 | **LOC:** 249 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 3.355; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.4%), Complexity Load (formerly Cognitive Load) (96.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Compute Cores)** (Impact: 22.4)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 18.4)
  * `sendMessageWithContext` **(Compute Cores)** (Impact: 7.6)
  * `cancelWithStatus` **(Compute Cores)** (Impact: 5.8)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 55`, `args: 22`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 16`, `import: 18`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.355
  * `Choke Point (Betweenness):` 0.001646 | `Ripple Effect (Closeness):` 0.06576
  * `Imports (Out-Degree: 18):` auth-context, call-credentials, call-interface, call-number, channel, channel-options, channelz, compression-filter...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/resolving-call.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.703)
- **Top Global Matches:** file_cluster_12: 7.703, file_cluster_4: 7.806, file_cluster_16: 9.389
- **Magnitude:** 223.9 | **LOC:** 380 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 3.233; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Concurrency Surface (formerly Concurrency) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.1%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfig` **(I/O & Config Routines)** (Impact: 23.6)
  * `runDeadlineTimer` **(I/O & Config Routines)** (Impact: 14.1)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `handleDeadline` **(I/O & Config Routines)** (Impact: 10.3)
  * `outputStatus` **(Stateful Encapsulated Methods)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 52`, `args: 32`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 31`
* *Architecture:* `api: 9`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.233
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.061606
  * `Imports (Out-Degree: 10):` auth-context, call-credentials, call-interface, constants, control-plane-status, deadline, filter-stack, internal-channel...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/resolver-dns.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.515)
- **Top Global Matches:** file_cluster_16: 6.515, file_cluster_12: 7.441, file_cluster_15: 7.817
- **Magnitude:** 219.02 | **LOC:** 450 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 3.7; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (95.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 27.2)
  * `startResolution` **(I/O & Config Routines)** (Impact: 21.8)
    * *Intent:* /** * If the target is an IP address, just provide that address as a result. * Otherwise, initiate A...
  * `updateResolution` **(I/O & Config Routines)** (Impact: 8.2)
  * `lookup` **(Stateful Encapsulated Methods)** (Impact: 7.3)
  * `handleHealthStatus` **(Stateful Encapsulated Methods)** (Impact: 4.6)
    * *Intent:* /** * The ResolverListener returns a boolean indicating whether the LB policy * accepted the resolut...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 51`, `args: 28`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 39`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 13`, `import: 14`
* *Defense:* `safety: 6`, `doc: 8`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.7
  * `Choke Point (Betweenness):` 0.007035 | `Ripple Effect (Closeness):` 0.068451
  * `Imports (Out-Degree: 11):` backoff-timeout, call-interface, channel-options, constants, environment, logging, metadata, resolver...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/resolving-load-balancer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.807)
- **Top Global Matches:** file_cluster_12: 6.807, file_cluster_16: 7.873, file_cluster_15: 7.892
- **Magnitude:** 215.52 | **LOC:** 408 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 3.233; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 79.3103% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleResolverResult` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `hasMatchingName` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 20.6)
    * *Intent:* /** * Wrapper class that behaves like a `LoadBalancer` and also handles name * resolution internally...
  * `invoke` **(Many-Argument Workhorses)** (Impact: 14.0)
  * `getDefaultConfigSelector` **(Defensive Guards)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 46`, `args: 20`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`
* *Architecture:* `api: 10`, `import: 15`
* *Defense:* `safety: 5`, `doc: 7`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.233
  * `Choke Point (Betweenness):` 0.000898 | `Ripple Effect (Closeness):` 0.062595
  * `Imports (Out-Degree: 14):` backoff-timeout, call-interface, channel-options, connectivity-state, constants, load-balancer, load-balancer-child-handler, logging...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/server-credentials.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.029)
- **Top Global Matches:** file_cluster_16: 7.029, file_cluster_15: 7.125, file_cluster_11: 7.709
- **Magnitude:** 195.78 | **LOC:** 353 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 3.716; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_equals` **(Compute Cores)** (Impact: 47.4)
    * *Intent:* /** * Checks equality by checking the options that are actually set by * createSsl. */
  * `createSsl` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `_equals` **(Compute Cores)** (Impact: 9.3)
  * `_equals` **(Compute Cores)** (Impact: 7.7)
  * `calculateSecureContextOptions` **(Stateful Encapsulated Methods)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 66`, `args: 35`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.716
  * `Choke Point (Betweenness):` 0.000274 | `Ripple Effect (Closeness):` 0.070294
  * `Imports (Out-Degree: 2):` , certificate-provider, tls-helpers, http2, tls
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/orca.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.221)
- **Top Global Matches:** file_cluster_15: 7.221, file_cluster_12: 7.573, file_cluster_10: 7.609
- **Magnitude:** 187.26 | **LOC:** 350 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **16**; blast radius 4.424; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.0%), Connectivity (formerly Api Exposure) (53.7%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateMetricsSubscription` **(Callbacks & Closures)** (Impact: 10.4)
  * `createMetricsReader` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** * Create an onCallEnded callback for use in a picker. * to, if applicable. */
  * `removeDataWatcher` **(Defensive Guards)** (Impact: 6.3)
  * `recordRequestCostMetric` **(State Mutators)** (Impact: 3.8)
    * *Intent:* /** * Records a request cost metric measurement for the call. */
  * `recordUtilizationMetric` **(State Mutators)** (Impact: 3.8)
    * *Intent:* /** * Records a request cost metric measurement for the call. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 62`, `args: 48`, `func_start: 38`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`
* *Architecture:* `api: 32`, `concurrency: 1`, `import: 17`
* *Defense:* `safety: 4`, `doc: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.424
  * `Choke Point (Betweenness):` 0.110319 | `Ripple Effect (Closeness):` 0.097543
  * `Imports (Out-Degree: 15):` backoff-timeout, call, channel, channel-credentials, connectivity-state, constants, duration, orca...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/load-balancing-call.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.961)
- **Top Global Matches:** file_cluster_12: 7.961, file_cluster_4: 9.165, file_cluster_5: 9.449
- **Magnitude:** 170.68 | **LOC:** 388 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 3.508; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doPick` **(I/O & Config Routines)** (Impact: 33.5)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 12.5)
  * `getDeadlineInfo` **(Defensive Guards)** (Impact: 8.9)
  * `outputStatus` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `sendMessageWithContext` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 55`, `args: 22`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 18`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 14`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.508
  * `Choke Point (Betweenness):` 0.000372 | `Ripple Effect (Closeness):` 0.061932
  * `Imports (Out-Degree: 14):` auth-context, call-credentials, call-interface, connectivity-state, constants, control-plane-status, deadline, internal-channel...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/metadata.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.463)
- **Top Global Matches:** file_cluster_15: 5.463, file_cluster_11: 6.989, file_cluster_10: 7.108
- **Magnitude:** 159.58 | **LOC:** 324 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **4**; blast radius 25.684; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 38.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromHttp2Headers` **(Defensive Guards)** (Impact: 20.6)
    * *Intent:* /** * Returns a new Metadata object based fields in a given IncomingHttpHeaders * object. */
  * `validate` **(Compute Cores)** (Impact: 18.5)
  * `add` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* /** * Adds the given value for the given key by appending to a list of previous * values associated ...
  * `clone` **(Callbacks & Closures)** (Impact: 4.9)
    * *Intent:* /** * Clones the metadata object. */
  * `merge` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* /** * Merges all key-value pairs from a given Metadata object into this one. * If both this object a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 42`, `args: 26`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 21`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 16`, `import: 4`
* *Defense:* `safety: 2`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.684
  * `Choke Point (Betweenness):` 0.002053 | `Ripple Effect (Closeness):` 0.187776
  * `Imports (Out-Degree: 3):` constants, error, logging, http2
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `package/src/subchannel-address.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.183)
- **Top Global Matches:** file_cluster_15: 6.183, file_cluster_0: 7.036, file_cluster_11: 7.625
- **Magnitude:** 157.58 | **LOC:** 253 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **1**; blast radius 9.514; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Connectivity (formerly Api Exposure) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.7%)
- **Documentation Coverage:** 88.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `subchannelAddressEqual` **(Compute Cores)** (Impact: 21.8)
  * `endpointEqualUnordered` **(Compute Cores)** (Impact: 11.4)
  * `stringToSubchannelAddress` **(Defensive Guards)** (Impact: 9.4)
  * `deleteMissing` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* /** * Delete any entries in this map with keys that are not in endpoints */
  * `subchannelAddressToString` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 49`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 5`, `api: 21`, `import: 1`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.514
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130119
  * `Imports (Out-Degree: 0):` net
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/src/generated/grpc/channelz/v1/Channelz.ts` (TYPESCRIPT) | Magnitude: 110.06 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, args: 52, func_start: 52, structural_boundaries: 41
- `package/src/generated/google/protobuf/MethodOptions.ts` (TYPESCRIPT) | Magnitude: 20.54 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, api: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `package/src/resolving-call.ts` (TYPESCRIPT) | Magnitude: 223.9 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 325, structural_boundaries: 52, branch: 51, args: 32
- `package/src/make-client.ts` (TYPESCRIPT) | Magnitude: 102.12 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 44, branch: 23, generics: 19
- `package/src/generated/orca.ts` (TYPESCRIPT) | Magnitude: 18.64 | Delta: **0.259** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 111, indent_spaces: 75, import: 53, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/src/channel.ts` (TYPESCRIPT) | Magnitude: 51.1 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 26, args: 13, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/src/server-credentials.ts` (TYPESCRIPT) | Magnitude: 195.78 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 66, branch: 61, args: 35
- `package/src/stream-decoder.ts` (TYPESCRIPT) | Magnitude: 90.26 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 79, state_mutation: 22, branch: 12, core_var_decl: 12
- `package/src/load-balancer-outlier-detection.ts` (TYPESCRIPT) | Magnitude: 416.56 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 698, branch: 112, structural_boundaries: 82, core_var_decl: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/src/generated/grpc/channelz/v1/ChannelTraceEvent.ts` (TYPESCRIPT) | Magnitude: 20.7 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, doc: 13, branch: 9
- `package/src/generated/google/protobuf/FileDescriptorProto.ts` (TYPESCRIPT) | Magnitude: 17.78 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 18, branch: 14, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `package/src/generated/channelz.ts` (TYPESCRIPT) | Magnitude: 18.22 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 103, indent_spaces: 58, import: 49, safety_bypasses: 2
- `package/src/index.ts` (TYPESCRIPT) | Magnitude: 54.36 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 79, import: 35, api: 31
- `package/src/client-interceptors.ts` (TYPESCRIPT) | Magnitude: 324.0 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 402, structural_boundaries: 128, args: 74, branch: 64

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/orca.ts` -> **Severity: 11.017** (Bridge: 0.1103 * Flux: 99.8685%)
- `package/src/call-interface.ts` -> **Severity: 7.199** (Bridge: 0.0743 * Flux: 96.9524%)
- `package/src/channelz.ts` -> **Severity: 6.58** (Bridge: 0.0886 * Flux: 74.2507%)
- `package/src/server-call.ts` -> **Severity: 5.238** (Bridge: 0.1052 * Flux: 49.816%)
- `package/src/internal-channel.ts` -> **Severity: 2.575** (Bridge: 0.0262 * Flux: 98.3537%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/logging.ts` -> **Severity: 12.886** (Embedded: 0.1903 * Error Risk: 67.7104%)
- `package/src/constants.ts` -> **Severity: 12.177** (Embedded: 0.2408 * Error Risk: 50.5714%)
- `package/src/call-interface.ts` -> **Severity: 11.962** (Embedded: 0.2018 * Error Risk: 59.2701%)
- `package/src/metadata.ts` -> **Severity: 11.268** (Embedded: 0.1878 * Error Risk: 60.0066%)
- `package/src/channel-options.ts` -> **Severity: 8.989** (Embedded: 0.1631 * Error Risk: 55.1196%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/logging.ts` -> **Severity: 1743.544** (Blast Radius: 21.459 * Doc Risk: 81.25%)
- `package/src/call-interface.ts` -> **Severity: 1520.333** (Blast Radius: 18.244 * Doc Risk: 83.3333%)
- `package/src/channel-options.ts` -> **Severity: 1341.7** (Blast Radius: 13.417 * Doc Risk: 100.0%)
- `package/src/error.ts` -> **Severity: 1107.5** (Blast Radius: 11.075 * Doc Risk: 100.0%)
- `package/src/metadata.ts` -> **Severity: 982.035** (Blast Radius: 25.684 * Doc Risk: 38.2353%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2450 call pairs -- scoped 45.3%, unique 0.0%, ambiguous 19.2%, external 35.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 2450 | 45.3% | 0.0% | 19.2% | 35.5% |

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
