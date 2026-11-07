# ARCHITECTURAL_BRIEF: @livekit_rtc-node
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
- **Scope:** 44 analyzed artifact(s), 5255 LOC.
- **Load-bearing artifact:** `package/src/ffi_client.ts` -- 14 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/napi/native.cjs` -- pulls in 39 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/src/room.ts` at magnitude 558.94 (structural weight, not risk).
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
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 44 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 5255 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3203 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2892 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7634 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 37 | 4843 | 84.1% |
| RUST | 3 | 116 | 6.8% |
| JAVASCRIPT | 2 | 296 | 4.5% |
| MARKDOWN | 1 | 0 | 2.3% |
| PLAINTEXT | 1 | 0 | 2.3% |

## 4.1 SOURCE ENCODINGS
All 44 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 25%, Data / Markup / Trivial 16%, Declarative / Non-Code 16%, Generic / Templated Code Files 14%, Large Core Modules (2) 14%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 42 | 95.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 4.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 2271 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2675 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1232 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 74.5 | 21.4 | 11.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 36.5 | 51.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.9 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 83.4 | 28.0 | 24.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 32.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.1 | 35.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 21.8 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.4 | 76.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 34 | 9 | 2 | `package/src/room.ts` |
| cleanup | 33 | 13 | 3 | `package/src/track.ts` |
| guards | 336 | 23 | 31 | `package/src/room.ts` |
| danger | 306 | 22 | 12 | `package/src/room.ts` |
| concurrency | 349 | 16 | 23 | `package/src/tests/e2e.test.ts` |
| connectivity | 272 | 37 | 15 | `package/src/index.ts` |
| io | 14 | 4 | 0 | `package/src/participant.ts` |
| crypto | 1 | 1 | 0 | `package/src/tests/e2e.test.ts` |
| ipc | 1 | 1 | 0 | `package/src/napi/native.cjs` |
| time | 23 | 7 | 2 | `package/src/tests/e2e.test.ts` |
| serialization | 1 | 1 | 0 | `package/src/audio_stream.ts` |
| regex | 0 | 0 | 0 | - |
| events | 70 | 7 | 4 | `package/src/room.ts` |
| tests | 112 | 4 | 0 | `package/src/async_queue.test.ts` |
| docs | 190 | 24 | 13 | `package/src/proto/participant_pb.ts` |
| debt | 19 | 6 | 2 | `package/src/participant.ts` |
| mutation | 1066 | 33 | 86 | `package/src/napi/native.cjs` |
| dead_code | 13 | 4 | 0 | `package/src/napi/native.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 23 | 5 | 1 | `package/src/tests/e2e.test.ts` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1394**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/participant.ts` (Hits: 5)
- `package/src/tests/e2e.test.ts` (Hits: 4)
- `package/src/napi/native.cjs` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ffi_client.ts** (`package/src/ffi_client.ts`) — 14 inbound connections
2. **audio_frame.ts** (`package/src/audio_frame.ts`) — 7 inbound connections
3. **track.ts** (`package/src/track.ts`) — 6 inbound connections
4. **log.ts** (`package/src/log.ts`) — 5 inbound connections
5. **types.ts** (`package/src/data_streams/types.ts`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **native.cjs** (`package/src/napi/native.cjs`) — 39 outbound dependencies
2. **index.ts** (`package/src/index.ts`) — 25 outbound dependencies
3. **room.ts** (`package/src/room.ts`) — 18 outbound dependencies
4. **participant.ts** (`package/src/participant.ts`) — 15 outbound dependencies
5. **nodejs.rs** (`package/src/nodejs.rs`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `processFfiEvent` **(Defensive Guards)** (@ `package/src/room.ts`) -> Impact: **211.5** | LOC: 298
- `streamBytes` **(Defensive Guards)** (@ `package/src/participant.ts`) -> Impact: **36.1** | LOC: 99
- `connect` **(Many-Argument Workhorses)** (@ `package/src/room.ts`) -> Impact: **34.8** | LOC: 56
  * *Intent:* /** * Connects to a LiveKit room using the provided URL and access token. */
- `constructor` **(Many-Argument Workhorses)** (@ `package/src/audio_stream.ts`) -> Impact: **30.2** | LOC: 44
- `handleStreamHeader` **(Defensive Guards)** (@ `package/src/room.ts`) -> Impact: **29.5** | LOC: 70
- `editChatMessage` **(Many-Argument Workhorses)** (@ `package/src/participant.ts`) -> Impact: **28.9** | LOC: 42
  * *Intent:* /** */
- `streamText` **(Defensive Guards)** (@ `package/src/participant.ts`) -> Impact: **28.4** | LOC: 87
  * *Intent:* /** * Returns a `StreamWriter` instance that allows to write individual chunks of text to a stream. * Well suited for TTS and/or streaming LLM output....
- `getPlaneLength` **(Compute Cores)** (@ `package/src/video_frame.ts`) -> Impact: **27.2** | LOC: 24
- `handleRpcMethodInvocation` **(Many-Argument Workhorses)** (@ `package/src/participant.ts`) -> Impact: **26.1** | LOC: 46
- `getPlaneInfos` **(Many-Argument Workhorses)** (@ `package/src/video_frame.ts`) -> Impact: **25.2** | LOC: 101

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src` | 29 | 2993.3 | 22.12% | 10.4% |
| `package/src/proto` | 4 | 355.3 | 4.64% | 0.0% |
| `package/src/tests` | 1 | 269.36 | 45.48% | 0.0% |
| `package/src/napi` | 3 | 252.07 | 24.84% | 33.33% |
| `package/src/data_streams` | 4 | 166.92 | 29.89% | 0.0% |
| `package` | 3 | 5.82 | 0.0% | 12.58% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/napi/native.d.ts` -> **99.999%** Exposure
- `package/src/track.ts` -> **99.9549%** Exposure
- `package/src/utils.ts` -> **97.0688%** Exposure
- `package/src/participant.ts` -> **44.4236%** Exposure
- `package/src/audio_frame.ts` -> **39.0501%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/audio_mixer.ts` -> **100.0%** Exposure
- `package/src/napi/native.cjs` -> **100.0%** Exposure
- `package/src/audio_source.ts` -> **99.9955%** Exposure
- `package/src/video_source.ts` -> **99.9411%** Exposure
- `package/src/async_queue.ts` -> **99.9254%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/napi/native.d.ts` -> **7** Orphaned Functions | **0** Duplicates
- `package/src/participant.ts` -> **0** Orphaned Functions | **4** Duplicates
- `package/src/track.ts` -> **0** Orphaned Functions | **4** Duplicates
- `package/src/utils.ts` -> **3** Orphaned Functions | **0** Duplicates
- `package/build.rs` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `60` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/src/room.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 11.071)
- **Top Global Matches:** file_cluster_5: 11.071, file_cluster_7: 11.33, file_cluster_12: 11.96
- **Magnitude:** 558.94 | **LOC:** 900 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 15.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.5%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.5%)
- **Documentation Coverage:** 65.9574% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processFfiEvent` **(Defensive Guards)** (Impact: 211.5)
  * `connect` **(Many-Argument Workhorses)** (Impact: 34.8)
    * *Intent:* /** * Connects to a LiveKit room using the provided URL and access token. */
  * `handleStreamHeader` **(Defensive Guards)** (Impact: 29.5)
  * `requireParticipantByIdentity` **(Stateful Encapsulated Methods)** (Impact: 8.9)
  * `onFfiEvent` **(Defensive Guards)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 191`, `args: 75`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 44`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 21`, `concurrency: 12`, `import: 23`
* *Defense:* `safety: 48`, `doc: 11`, `sync_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.359
  * `Choke Point (Betweenness):` 0.006488 | `Ripple Effect (Closeness):` 0.046512
  * `Imports (Out-Degree: 11):` stream_reader.js, types.js, e2ee.js, ffi_client.js, log.js, participant.js, e2ee_pb.js, ffi_pb.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/async_queue.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.463)
- **Top Global Matches:** file_cluster_10: 5.463, file_cluster_2: 7.965, file_cluster_13: 8.266
- **Magnitude:** 497.91 | **LOC:** 251 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (75.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 153
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 62`, `args: 25`, `func_start: 12`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `concurrency: 58`, `import: 2`
* *Defense:* `safety: 2`, `test: 46`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` async_queue.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/participant.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.844)
- **Top Global Matches:** file_cluster_4: 8.844, file_cluster_12: 9.357, file_cluster_5: 9.423
- **Magnitude:** 471.94 | **LOC:** 873 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 12.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%)
- **Documentation Coverage:** 70.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `streamBytes` **(Defensive Guards)** (Impact: 36.1)
  * `editChatMessage` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /** */
  * `streamText` **(Defensive Guards)** (Impact: 28.4)
    * *Intent:* /** * Returns a `StreamWriter` instance that allows to write individual chunks of text to a stream. ...
  * `handleRpcMethodInvocation` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `sendChatMessage` **(Many-Argument Workhorses)** (Impact: 23.7)
    * *Intent:* /** * Sends a chat message to participants in the room * * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 156`, `args: 54`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 17`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 22`, `concurrency: 64`, `import: 17`
* *Defense:* `safety: 40`, `doc: 13`, `sync_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.144
  * `Choke Point (Betweenness):` 0.004476 | `Ripple Effect (Closeness):` 0.052326
  * `Imports (Out-Degree: 12):` index.js, ffi_client.js, log.js, participant_pb.js, room_pb.js, rpc_pb.js, rpc.js, track.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/audio_mixer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.523)
- **Top Global Matches:** file_cluster_4: 7.523, file_cluster_16: 10.013, file_cluster_0: 10.304
- **Magnitude:** 285.26 | **LOC:** 419 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 15.359; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (66.4%), Complexity Load (formerly Cognitive Load) (60.3%)
- **Documentation Coverage:** 35.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getContribution` **(Compute Cores)** (Impact: 23.6)
  * `mixer` **(I/O & Config Routines)** (Impact: 20.4)
  * `mixAudio` **(Stateful Encapsulated Methods)** (Impact: 18.7)
  * `constructor` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* /** * Initialize the AudioMixer. * */
  * `getNextFrame` **(Stateful Encapsulated Methods)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 56`, `args: 23`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 7`, `concurrency: 29`, `import: 4`
* *Defense:* `safety: 11`, `doc: 10`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.359
  * `Choke Point (Betweenness):` 0.002353 | `Ripple Effect (Closeness):` 0.052326
  * `Imports (Out-Degree: 3):` async_queue.js, audio_frame.js, log.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/tests/e2e.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.434)
- **Top Global Matches:** file_cluster_7: 9.434, file_cluster_5: 9.662, file_cluster_14: 10.468
- **Magnitude:** 269.36 | **LOC:** 515 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `estimateFreqHz` **(Compute Cores)** (Impact: 15.7)
  * `waitFor` **(Defensive Guards)** (Impact: 11.0)
  * `normalizeLiveKitUrl` **(Compute Cores)** (Impact: 4.5)
  * `channelSamples` **(Compute Cores)** (Impact: 3.9)
  * `concatUint8` **(Parameter Forwarders)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 131
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 109`, `args: 44`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 30`
* *Architecture:* `io: 4`, `concurrency: 86`, `import: 5`
* *Defense:* `safety: 11`, `test: 34`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` index.js, livekit-server-sdk, node:crypto, promises, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/napi/native.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.05)
- **Top Global Matches:** file_cluster_2: 7.05, file_cluster_13: 7.185, file_cluster_15: 7.495
- **Magnitude:** 235.44 | **LOC:** 302 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **39**; blast radius 69.041; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (74.5%), Guard Balance (formerly Safety Score) (70.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isMusl` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 71 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 24`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 77`
* *Architecture:* `io: 3`, `api: 6`, `import: 39`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.157667
  * `Imports (Out-Degree: 0):` rtc-node.android-arm-eabi.node, rtc-node.android-arm64.node, rtc-node.darwin-arm64.node, rtc-node.darwin-universal.node, rtc-node.darwin-x64.node, rtc-node.freebsd-x64.node, rtc-node.linux-arm-gnueabihf.node, rtc-node.linux-arm-musleabihf.node...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/proto/rpc_pb.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.911)
- **Top Global Matches:** file_cluster_0: 5.911, file_cluster_10: 11.107, file_cluster_13: 11.272
- **Magnitude:** 189.7 | **LOC:** 540 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 21.264; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.9%), Complexity Load (formerly Cognitive Load) (5.8%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromBinary` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJson` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJsonString` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromBinary` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJson` **(Generic / Templated Code)** (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 91`, `args: 66`, `func_start: 55`, `class_start: 11`
* *Risk/State:* None
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 39`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.064599
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/data_streams/stream_reader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.835)
- **Top Global Matches:** file_cluster_5: 5.835, file_cluster_12: 8.731, file_cluster_7: 10.048
- **Magnitude:** 122.56 | **LOC:** 159 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 50.159; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (64.6%), Guard Balance (formerly Safety Score) (60.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleChunkReceived` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `handleChunkReceived` **(Stateful Encapsulated Methods)** (Impact: 4.6)
  * `[Symbol.asyncIterator]` **(Defensive Guards)** (Impact: 4.5)
    * *Intent:* /** * Async iterator implementation to allow usage of `for await...of` syntax. * Yields structured c...
  * `constructor` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* /** * A TextStreamReader instance can be used as an AsyncIterator that returns the entire string * t...
  * `constructor` **(Generic / Templated Code)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 43`, `args: 14`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`
* *Architecture:* `api: 2`, `concurrency: 13`, `import: 4`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 50.159
  * `Choke Point (Betweenness):` 0.003322 | `Ripple Effect (Closeness):` 0.103594
  * `Imports (Out-Degree: 3):` log.js, room_pb.js, utils.js, types.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/e2ee.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.419)
- **Top Global Matches:** file_cluster_12: 6.419, file_cluster_7: 8.208, file_cluster_5: 8.218
- **Magnitude:** 115.62 | **LOC:** 316 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 12.144; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exportKey` **(Type Conversions)** (Impact: 6.2)
  * `ratchetKey` **(Type Conversions)** (Impact: 6.2)
  * `setSharedKey` **(State Mutators)** (Impact: 6.1)
  * `setKey` **(State Mutators)** (Impact: 6.1)
  * `constructor` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 22`, `args: 14`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052326
  * `Imports (Out-Degree: 1):` ffi_client.js, e2ee_pb.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/audio_mixer.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.415)
- **Top Global Matches:** file_cluster_12: 7.415, file_cluster_5: 8.029, file_cluster_7: 8.517
- **Magnitude:** 115.46 | **LOC:** 168 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (54.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createMockAudioStream` **(Generic / Templated Code)** (Impact: 5.1)
    * *Intent:* // Helper to create a mock audio stream that yields frames
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 23`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`
* *Architecture:* `concurrency: 19`, `import: 3`
* *Defense:* `safety: 1`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` audio_frame.js, audio_mixer.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_source.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.767)
- **Top Global Matches:** file_cluster_12: 7.767, file_cluster_5: 7.917, file_cluster_7: 9.03
- **Magnitude:** 112.22 | **LOC:** 152 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 17.092; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.8%), Connectivity (formerly Api Exposure) (50.4%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `captureFrame` **(Compute Cores)** (Impact: 14.7)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 5.2)
  * `clearQueue` **(I/O & Config Routines)** (Impact: 2.8)
  * `waitForPlayout` **(Callbacks & Closures)** (Impact: 1.4)
  * `queuedDuration` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 21`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 20`
* *Architecture:* `api: 7`, `concurrency: 8`, `import: 5`
* *Defense:* `safety: 1`, `doc: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.092
  * `Choke Point (Betweenness):` 0.003913 | `Ripple Effect (Closeness):` 0.106312
  * `Imports (Out-Degree: 3):` audio_frame.js, ffi_client.js, native.js, audio_frame_pb.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/video_frame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.935)
- **Top Global Matches:** file_cluster_7: 8.935, file_cluster_12: 10.047, file_cluster_14: 10.332
- **Magnitude:** 108.1 | **LOC:** 232 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 26.773; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (65.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 72.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPlaneLength` **(Compute Cores)** (Impact: 27.2)
  * `getPlaneInfos` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `convert` **(Compute Cores)** (Impact: 13.2)
  * `protoInfo` **(I/O & Config Routines)** (Impact: 9.3)
  * `getPlane` **(Parameter Forwarders)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 46`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 8`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.773
  * `Choke Point (Betweenness):` 0.001107 | `Ripple Effect (Closeness):` 0.122399
  * `Imports (Out-Degree: 1):` ffi_client.js, video_frame_pb.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/proto/track_publication_pb.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.86)
- **Top Global Matches:** file_cluster_0: 5.86, file_cluster_10: 11.15, file_cluster_13: 11.197
- **Magnitude:** 104.36 | **LOC:** 285 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 10.359; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.4%), Complexity Load (formerly Cognitive Load) (4.9%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromBinary` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJson` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJsonString` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromBinary` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJson` **(Generic / Templated Code)** (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 54`, `args: 36`, `func_start: 30`, `class_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 17`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_stream.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.676)
- **Top Global Matches:** file_cluster_5: 6.676, file_cluster_12: 8.352, file_cluster_7: 9.726
- **Magnitude:** 100.36 | **LOC:** 137 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 10.957; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.5%), Guard Balance (formerly Safety Score) (60.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `onEvent` **(Defensive Guards)** (Impact: 18.6)
  * `constructor` **(State Mutators)** (Impact: 6.3)
  * `constructor` **(State Mutators)** (Impact: 2.0)
  * `constructor` **(State Mutators)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 28`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 7`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.957
  * `Choke Point (Betweenness):` 0.000138 | `Ripple Effect (Closeness):` 0.031008
  * `Imports (Out-Degree: 5):` audio_frame.js, ffi_client.js, frame_processor.js, log.js, audio_frame_pb.js, track.js, web
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/track.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.715)
- **Top Global Matches:** file_cluster_5: 6.715, file_cluster_12: 8.245, file_cluster_7: 9.117
- **Magnitude:** 72.96 | **LOC:** 128 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 21.655; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (92.8%), Mutation Surface (formerly State Flux) (70.4%), Connectivity (formerly Api Exposure) (69.9%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `close` **(Defensive Guards)** (Impact: 4.5)
  * `close` **(Defensive Guards)** (Impact: 4.5)
  * `createAudioTrack` **(Generic / Templated Code)** (Impact: 4.1)
  * `createVideoTrack` **(Generic / Templated Code)** (Impact: 4.1)
  * `constructor` **(State Mutators)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 41`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 7`, `doc: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.655
  * `Choke Point (Betweenness):` 0.009413 | `Ripple Effect (Closeness):` 0.142442
  * `Imports (Out-Degree: 3):` audio_source.js, ffi_client.js, track_pb.js, video_source.js
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/src/track_publication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.917)
- **Top Global Matches:** file_cluster_12: 6.917, file_cluster_5: 7.803, file_cluster_7: 9.219
- **Magnitude:** 67.3 | **LOC:** 113 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 13.004; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Mutation Surface (formerly State Flux) (71.0%), Connectivity (formerly Api Exposure) (67.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 89.6552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setSubscribed` **(State Mutators)** (Impact: 3.3)
  * `resolveFirstSubscription` **(Interface Declarations)** (Impact: 2.3)
  * `sid` **(Defensive Guards)** (Impact: 2.1)
  * `name` **(Defensive Guards)** (Impact: 2.1)
  * `kind` **(Defensive Guards)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 10
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 37`, `args: 18`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `api: 16`, `concurrency: 5`, `import: 7`
* *Defense:* `safety: 10`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.004
  * `Choke Point (Betweenness):` 0.00192 | `Ripple Effect (Closeness):` 0.074419
  * `Imports (Out-Degree: 3):` ffi_client.js, native.js, e2ee_pb.js, room_pb.js, track_pb.js, track.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/nodejs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.849)
- **Top Global Matches:** file_cluster_12: 7.849, file_cluster_13: 8.045, file_cluster_15: 8.266
- **Magnitude:** 43.88 | **LOC:** 135 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 19.165; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.2%), Connectivity (formerly Api Exposure) (55.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (30.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `livekit_ffi_request` **(Compute Cores)** (Impact: 5.5)
  * `livekit_initialize` **(Callbacks & Closures)** (Impact: 5.2)
  * `dispose` **(Compute Cores)** (Impact: 4.9)
  * `livekit_copy_buffer` **(Type Conversions)** (Impact: 2.0)
  * `finalize` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 26`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 10`, `concurrency: 2`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 0):` livekit_ffi::FFI_SERVER, livekit_ffi::proto, livekit_ffi::server, napi::JsFunction, napi::Status, napi::bindgen_prelude::*, napi::threadsafe_function::ErrorStrategy, napi::threadsafe_function::ThreadSafeCallContext...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 15.597)
- **Top Global Matches:** file_cluster_17: 15.597, file_cluster_13: 15.771, file_cluster_15: 15.877
- **Magnitude:** 43.06 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 14.762; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (16.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`
* *Risk/State:* None
* *Architecture:* `api: 27`, `import: 27`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.762
  * `Choke Point (Betweenness):` 0.011646 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 21):` audio_filter.js, audio_frame.js, audio_mixer.js, audio_resampler.js, audio_source.js, audio_stream.js, index.js, e2ee.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/async_queue.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.067)
- **Top Global Matches:** file_cluster_12: 8.067, file_cluster_5: 8.308, file_cluster_7: 8.801
- **Magnitude:** 42.86 | **LOC:** 81 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 23.516; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (99.6%), Guard Balance (formerly Safety Score) (62.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `put` **(Compute Cores)** (Impact: 8.0)
  * `waitForItem` **(Interface Declarations)** (Impact: 3.3)
    * *Intent:* /** * Wait until an item is available or the queue is closed. * Returns immediately if items are alr...
  * `get` **(Interface Declarations)** (Impact: 2.4)
  * `close` **(Interface Declarations)** (Impact: 1.6)
  * `constructor` **(Encapsulated Accessors)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 21`, `args: 13`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `api: 5`, `concurrency: 7`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.516
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.064599
  * `Imports (Out-Degree: 0):` deque
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/audio_resampler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.296)
- **Top Global Matches:** file_cluster_12: 6.296, file_cluster_5: 7.925, file_cluster_7: 8.17
- **Magnitude:** 41.06 | **LOC:** 182 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.957; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (39.2%), Complexity Load (formerly Cognitive Load) (4.1%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 17.5)
    * *Intent:* #inputRate: number; #outputRate: number; #channels: number; #ffiHandle: FfiHandle; /** * Initializes...
  * `push` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* /** * Push audio data into the resampler and retrieve any available resampled data. * * This method ...
  * `flush` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* /** * Flush any remaining audio data through the resampler and retrieve the resampled data. * * This...
  * `inputRate` **(Interface Declarations)** (Impact: 1.1)
  * `outputRate` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.957
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.031008
  * `Imports (Out-Degree: 2):` audio_frame.js, ffi_client.js, audio_frame_pb.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.223)
- **Top Global Matches:** file_cluster_0: 7.223, file_cluster_9: 10.259, file_cluster_15: 10.284
- **Magnitude:** 40.76 | **LOC:** 43 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 35.423; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (58.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `splitUtf8` **(Compute Cores)** (Impact: 13.3)
  * `bigIntToNumber` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* // SPDX-FileCopyrightText: 2024 LiveKit, Inc. // // SPDX-License-Identifier: Apache-2.0 /** convert ...
  * `numberToBigInt` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* /** convert numbers to bigints preserving undefined values */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 35.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.125581
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/video_source.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.209)
- **Top Global Matches:** file_cluster_5: 7.209, file_cluster_12: 7.302, file_cluster_7: 7.66
- **Magnitude:** 40.72 | **LOC:** 77 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 17.092; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (97.3%), Guard Balance (formerly Safety Score) (61.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `captureFrame` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `constructor` **(Defensive Guards)** (Impact: 6.3)
  * `close` **(State Mutators)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 2`, `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.092
  * `Choke Point (Betweenness):` 0.002215 | `Ripple Effect (Closeness):` 0.106312
  * `Imports (Out-Degree: 2):` ffi_client.js, video_frame_pb.js, video_frame.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/proto/participant_pb.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 4.008)
- **Top Global Matches:** file_cluster_0: 4.008, file_cluster_13: 8.987, file_cluster_10: 9.363
- **Magnitude:** 39.02 | **LOC:** 352 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 13.004; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.1%), Complexity Load (formerly Cognitive Load) (3.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromBinary` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJson` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJsonString` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromBinary` **(Generic / Templated Code)** (Impact: 3.6)
  * `fromJson` **(Generic / Templated Code)** (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 29`, `args: 12`, `func_start: 10`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `doc: 41`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.004
  * `Choke Point (Betweenness):` 0.002215 | `Ripple Effect (Closeness):` 0.074419
  * `Imports (Out-Degree: 1):` handle_pb.js, protobuf
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/audio_frame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.671)
- **Top Global Matches:** file_cluster_5: 7.671, file_cluster_7: 7.953, file_cluster_12: 9.509
- **Magnitude:** 38.16 | **LOC:** 108 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 36.521; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `combineAudioFrames` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /** * Combines one or more `rtc.AudioFrame` objects into a single `rtc.AudioFrame`. * * This functio...
  * `constructor` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* // note: if converting from Uint8Array to Int16Array, *do not* use buffer.slice! // it is marked uns...
  * `create` **(Parameter Forwarders)** (Impact: 2.2)
  * `fromOwnedInfo` **(Parameter Forwarders)** (Impact: 2.0)
  * `protoInfo` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 17`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 7`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 1`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.521
  * `Choke Point (Betweenness):` 0.005537 | `Ripple Effect (Closeness):` 0.17088
  * `Imports (Out-Degree: 1):` ffi_client.js, audio_frame_pb.js
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `package/src/ffi_client.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.862)
- **Top Global Matches:** file_cluster_0: 6.862, file_cluster_10: 8.809, file_cluster_11: 9.689
- **Magnitude:** 32.92 | **LOC:** 83 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **6**; blast radius 117.989; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.4%), Concurrency Surface (formerly Concurrency) (65.4%), Guard Balance (formerly Safety Score) (51.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `waitFor` **(Generic / Templated Code)** (Impact: 3.4)
  * `listener` **(Callbacks & Closures)** (Impact: 3.1)
  * `instance` **(Interface Declarations)** (Impact: 2.3)
  * `copyBuffer` **(Parameter Forwarders)** (Impact: 1.9)
  * `request` **(Generic / Templated Code)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 32`, `args: 11`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 10`, `concurrency: 3`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 117.989
  * `Choke Point (Betweenness):` 0.024622 | `Ripple Effect (Closeness):` 0.342495
  * `Imports (Out-Degree: 2):` native.js, ffi_pb.js, version.js, protobuf, typed-emitter, events
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `package/src/audio_source.ts` (TYPESCRIPT) | Magnitude: 112.22 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 21, state_mutation: 20, core_var_decl: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/src/index.ts` (TYPESCRIPT) | Magnitude: 43.06 | Delta: **0.174** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 43, api: 27, import: 27, indent_spaces: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/src/napi/native.cjs` (JAVASCRIPT) | Magnitude: 235.44 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 267, branch: 77, state_mutation: 77, core_var_decl: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `package/src/video_source.ts` (TYPESCRIPT) | Magnitude: 40.72 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 9, state_mutation: 7, core_var_decl: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/ffi_client.ts` -> **Severity: 0.883** (Bridge: 0.0246 * Flux: 35.8514%)
- `package/src/track.ts` -> **Severity: 0.662** (Bridge: 0.0094 * Flux: 70.3768%)
- `package/src/room.ts` -> **Severity: 0.62** (Bridge: 0.0065 * Flux: 95.5079%)
- `package/src/audio_frame.ts` -> **Severity: 0.539** (Bridge: 0.0055 * Flux: 97.4103%)
- `package/src/audio_source.ts` -> **Severity: 0.391** (Bridge: 0.0039 * Flux: 99.9955%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/ffi_client.ts` -> **Severity: 17.682** (Embedded: 0.3425 * Error Risk: 51.6273%)
- `package/src/audio_frame.ts` -> **Severity: 13.67** (Embedded: 0.1709 * Error Risk: 80.0%)
- `package/src/napi/native.cjs` -> **Severity: 11.185** (Embedded: 0.1577 * Error Risk: 70.9407%)
- `package/src/video_frame.ts` -> **Severity: 9.792** (Embedded: 0.1224 * Error Risk: 80.0%)
- `package/src/log.ts` -> **Severity: 8.129** (Embedded: 0.1563 * Error Risk: 51.9989%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/ffi_client.ts` -> **Severity: 9983.686** (Blast Radius: 117.989 * Doc Risk: 84.6154%)
- `package/src/napi/native.cjs` -> **Severity: 6904.1** (Blast Radius: 69.041 * Doc Risk: 100.0%)
- `package/src/data_streams/stream_reader.ts` -> **Severity: 4012.72** (Blast Radius: 50.159 * Doc Risk: 80.0%)
- `package/src/track.ts` -> **Severity: 2062.381** (Blast Radius: 21.655 * Doc Risk: 95.2381%)
- `package/src/video_frame.ts` -> **Severity: 1947.128** (Blast Radius: 26.773 * Doc Risk: 72.7273%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 669 call pairs -- scoped 34.4%, unique 0.0%, ambiguous 6.3%, external 59.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 627 | 36.5% | 0.0% | 6.7% | 56.8% |
| rust | 36 | 2.8% | 0.0% | 0.0% | 97.2% |
| javascript | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
