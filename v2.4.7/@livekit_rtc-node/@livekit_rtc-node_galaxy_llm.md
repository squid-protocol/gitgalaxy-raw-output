# ARCHITECTURAL_BRIEF: @livekit_rtc-node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@livekit_rtc-node` |
| **Timestamp** | `2026-08-07T05:11:19.934395+00:00` |
| **Scan Duration** | `0.23s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 36 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 38 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 4352 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.4% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 33 | 3947 | 86.8% |
| JAVASCRIPT | 2 | 296 | 5.3% |
| MARKDOWN | 1 | 0 | 2.6% |
| PLAINTEXT | 1 | 0 | 2.6% |
| RUST | 1 | 109 | 2.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.038`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 12 | 31.6% |
| file_cluster_8 | 9 | 23.7% |
| file_cluster_4 | 8 | 21.1% |
| file_cluster_16 | 6 | 15.8% |
| file_cluster_0 | 1 | 2.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 5.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `.ts`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2271 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2675 LOC)
- `.rs`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 31.9 | 15.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 46.9 | 61.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 38.1 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 19.5 | 2.5 | 80.0 |
| API Exposure | 0.9 | 16.3 | 6.6 | 6.5 | 3.7 |
| Concurrency Exposure | 0.0 | 100.0 | 32.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.1 | 53.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.8 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.7 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 3.2 | 100.0 | 35.8 | 29.7 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/participant.ts` (Hits: 5)
- `package/src/napi/native.cjs` (Hits: 3)
- `package/src/audio_filter.ts` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`package/README.md`) — 0 inbound connections
2. **package.json** (`package/package.json`) — 0 inbound connections
3. **async_queue.ts** (`package/src/async_queue.ts`) — 0 inbound connections
4. **audio_filter.ts** (`package/src/audio_filter.ts`) — 0 inbound connections
5. **audio_frame.ts** (`package/src/audio_frame.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **native.cjs** (`package/src/napi/native.cjs`) — 39 outbound dependencies
2. **index.ts** (`package/src/index.ts`) — 25 outbound dependencies
3. **room.ts** (`package/src/room.ts`) — 18 outbound dependencies
4. **participant.ts** (`package/src/participant.ts`) — 15 outbound dependencies
5. **nodejs.rs** (`package/src/nodejs.rs`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `processFfiEvent` (@ `package/src/room.ts`) -> Impact: **344.9** | LOC: 297
  * *Intent:* /**
- `getContribution` (@ `package/src/audio_mixer.ts`) -> Impact: **43.3** | LOC: 62
- `constructor` (@ `package/src/audio_stream.ts`) -> Impact: **42.4** | LOC: 44
- `handleStreamHeader` (@ `package/src/room.ts`) -> Impact: **41.6** | LOC: 70
- `handleRpcMethodInvocation` (@ `package/src/participant.ts`) -> Impact: **39.1** | LOC: 46
  * *Intent:* /** * Establishes the participant as a receiver for calls of the specified RPC method. * Will overwrite any existing callback for the same method. * *...
- `connect` (@ `package/src/room.ts`) -> Impact: **36.8** | LOC: 56
- `onEvent` (@ `package/src/audio_stream.ts`) -> Impact: **33.6** | LOC: 32
- `editChatMessage` (@ `package/src/participant.ts`) -> Impact: **31.5** | LOC: 42
- `getPlaneLength` (@ `package/src/video_frame.ts`) -> Impact: **27.2** | LOC: 24
- `getPlaneInfos` (@ `package/src/video_frame.ts`) -> Impact: **27.1** | LOC: 101

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src` | 25 | 401.43 | 36.44% | 34.9% |
| `package/src/napi` | 3 | 48.45 | 13.19% | 33.02% |
| `package/src/proto` | 4 | 39.33 | 4.82% | 75.0% |
| `package/src/data_streams` | 4 | 31.04 | 44.94% | 25.0% |
| `package` | 2 | 4.64 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/data_streams/stream_reader.ts` -> **100.0%** Exposure
- `package/src/proto/participant_pb.ts` -> **100.0%** Exposure
- `package/src/proto/rpc_pb.ts` -> **100.0%** Exposure
- `package/src/proto/track_publication_pb.ts` -> **100.0%** Exposure
- `package/src/track.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/async_queue.ts` -> **100.0%** Exposure
- `package/src/audio_mixer.ts` -> **100.0%** Exposure
- `package/src/audio_source.ts` -> **100.0%** Exposure
- `package/src/audio_stream.ts` -> **100.0%** Exposure
- `package/src/data_streams/stream_reader.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/proto/rpc_pb.ts` -> **0** Orphaned Functions | **64** Duplicates
- `package/src/proto/track_publication_pb.ts` -> **0** Orphaned Functions | **33** Duplicates
- `package/src/proto/participant_pb.ts` -> **0** Orphaned Functions | **12** Duplicates
- `package/src/data_streams/stream_reader.ts` -> **0** Orphaned Functions | **11** Duplicates
- `package/src/participant.ts` -> **0** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/napi/native.cjs`** -> AI Confidence: **99.48%**
2. **`package/src/audio_stream.ts`** -> AI Confidence: **99.31%**
3. **`package/src/participant.ts`** -> AI Confidence: **99.31%**
4. **`package/src/room.ts`** -> AI Confidence: **99.31%**
5. **`package/src/audio_mixer.ts`** -> AI Confidence: **99.2%**
6. **`package/src/index.ts`** -> AI Confidence: **99.09%**
7. **`package/src/nodejs.rs`** -> AI Confidence: **99.08%**
8. **`package/src/e2ee.ts`** -> AI Confidence: **99.06%**
9. **`package/src/types.ts`** -> AI Confidence: **99.06%**
10. **`package/src/utils.ts`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `51` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/track.ts` (TYPESCRIPT) -> Cumulative Risk: **772.32**
- **Archetype:** `file_cluster_4` (Distance: 12.336 IQR)
- **Magnitude:** 14.11 | **LOC:** 128 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.988%)
- **Heaviest Functions:** `close` (Impact: 7.0), `close` (Impact: 7.0), `createAudioTrack` (Impact: 4.1)

### 2. `package/src/room.ts` (TYPESCRIPT) -> Cumulative Risk: **683.43**
- **Archetype:** `file_cluster_13` (Distance: 14.438 IQR)
- **Magnitude:** 118.05 | **LOC:** 900 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.6555%), Concurrency (97.3039%)
- **Heaviest Functions:** `processFfiEvent` (Impact: 344.9), `handleStreamHeader` (Impact: 41.6), `connect` (Impact: 36.8)

### 3. `package/src/participant.ts` (TYPESCRIPT) -> Cumulative Risk: **653.18**
- **Archetype:** `file_cluster_4` (Distance: 12.258 IQR)
- **Magnitude:** 66.15 | **LOC:** 873 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (92.3123%), State Flux (87.6983%)
- **Heaviest Functions:** `handleRpcMethodInvocation` (Impact: 39.1), `editChatMessage` (Impact: 31.5), `sendChatMessage` (Impact: 26.3)

### 4. `package/src/track_publication.ts` (TYPESCRIPT) -> Cumulative Risk: **636.4**
- **Archetype:** `file_cluster_4` (Distance: 13.913 IQR)
- **Magnitude:** 13.61 | **LOC:** 113 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.821%)
- **Heaviest Functions:** `setSubscribed` (Impact: 4.0), `sid` (Impact: 3.6), `name` (Impact: 3.6)

### 5. `package/src/data_streams/stream_reader.ts` (TYPESCRIPT) -> Cumulative Risk: **624.57**
- **Archetype:** `file_cluster_4` (Distance: 13.576 IQR)
- **Magnitude:** 21.76 | **LOC:** 159 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `readAll` (Impact: 16.2), `next` (Impact: 10.8), `next` (Impact: 10.7)

### 6. `package/src/audio_stream.ts` (TYPESCRIPT) -> Cumulative Risk: **620.63**
- **Archetype:** `file_cluster_13` (Distance: 12.834 IQR)
- **Magnitude:** 17.0 | **LOC:** 137 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.2751%), Tech Debt (85.0342%)
- **Heaviest Functions:** `constructor` (Impact: 42.4), `onEvent` (Impact: 33.6), `constructor` (Impact: 7.1)

### 7. `package/src/data_streams/stream_writer.ts` (TYPESCRIPT) -> Cumulative Risk: **607.55**
- **Archetype:** `file_cluster_4` (Distance: 14.82 IQR)
- **Magnitude:** 5.34 | **LOC:** 36 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.995%)
- **Heaviest Functions:** `constructor` (Impact: 4.3), `close` (Impact: 3.7), `write` (Impact: 1.9)

### 8. `package/src/e2ee.ts` (TYPESCRIPT) -> Cumulative Risk: **582.54**
- **Archetype:** `file_cluster_8` (Distance: 10.645 IQR)
- **Magnitude:** 16.14 | **LOC:** 316 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8832%), Tech Debt (89.2117%), Safety Score (86.9073%)
- **Heaviest Functions:** `constructor` (Impact: 7.4), `exportSharedKey` (Impact: 6.2), `ratchetSharedKey` (Impact: 6.2)

### 9. `package/src/video_stream.ts` (TYPESCRIPT) -> Cumulative Risk: **568.07**
- **Archetype:** `file_cluster_13` (Distance: 10.628 IQR)
- **Magnitude:** 6.07 | **LOC:** 87 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.95%), Tech Debt (98.8393%), Safety Score (93.1419%)
- **Heaviest Functions:** `onEvent` (Impact: 23.6), `constructor` (Impact: 4.3), `start` (Impact: 1.9)

### 10. `package/src/audio_mixer.ts` (TYPESCRIPT) -> Cumulative Risk: **565.11**
- **Archetype:** `file_cluster_4` (Distance: 13.529 IQR)
- **Magnitude:** 22.95 | **LOC:** 419 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9437%)
- **Heaviest Functions:** `getContribution` (Impact: 43.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/room.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.438 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.61 IQR)
- **Top Global Matches:** file_cluster_13: 14.438, file_cluster_4: 14.543, file_cluster_11: 14.615
- **Magnitude:** 118.05 | **LOC:** 900 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.9752%), Tech Debt (68.6079%)
**Top Internal Functions/Classes:**
  * `processFfiEvent` (Impact: 344.9)
    * *Intent:* /**
  * `handleStreamHeader` (Impact: 41.6)
  * `connect` (Impact: 36.8)
  * `onFfiEvent` (Impact: 14.9)
  * `super` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 142`, `args: 83`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 458`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 15`, `concurrency: 62`, `import: 23`
* *Defense:* `safety: 93`, `doc: 22`, `sync_locks: 4`, `immutability_locks: 67`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2ee.js, ffi_client.js, log.js, participant_pb.js, ffi_pb.js, types.js, room_pb.js, utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/participant.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.258 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.341 IQR)
- **Top Global Matches:** file_cluster_4: 12.258, file_cluster_13: 12.441, file_cluster_2: 12.636
- **Magnitude:** 66.15 | **LOC:** 873 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.407%), Tech Debt (92.3123%)
**Top Internal Functions/Classes:**
  * `handleRpcMethodInvocation` (Impact: 39.1)
    * *Intent:* /** * Establishes the participant as a receiver for calls of the specified RPC method. * Will overwr...
  * `editChatMessage` (Impact: 31.5)
  * `sendChatMessage` (Impact: 26.3)
  * `publishTrack` (Impact: 23.8)
  * `unpublishTrack` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 155`, `args: 59`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 120`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 5`, `api: 11`, `concurrency: 179`, `import: 17`
* *Defense:* `safety: 41`, `doc: 23`, `sync_locks: 8`, `immutability_locks: 89`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs, ffi_client.js, log.js, participant_pb.js, types.js, promises, rpc_pb.js, room_pb.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/nodejs.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.395 IQR)
- **Top Global Matches:** file_cluster_0: 12.395, file_cluster_13: 12.824, file_cluster_11: 12.911
- **Magnitude:** 43.68 | **LOC:** 135 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.8669%), Tech Debt (99.8414%)
**Top Internal Functions/Classes:**
  * `livekit_ffi_request` (Impact: 7.3)
  * `dispose` (Impact: 6.7)
  * `livekit_initialize` (Impact: 5.2)
  * `new` (Impact: 2.4)
  * `livekit_retrieve_ptr` (Impact: 2.2)
    * *Intent:* // FfiHandle must be used instead //#[napi] //fn livekit_drop_handle(handle: BigInt) -> bool { // le...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 26`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` napi::
    bindgen_prelude::*, prost::Message, napi_derive::napi, ThreadsafeFunction, std::sync::Arc, Status, FFI_SERVER, server...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/napi/native.cjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.101 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.171 IQR)
- **Top Global Matches:** file_cluster_13: 11.101, file_cluster_0: 11.28, file_cluster_8: 11.284
- **Magnitude:** 31.84 | **LOC:** 302 | **CtrlFlow:** 95.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.5755%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isMusl` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 3`, `api: 6`, `import: 39`
* *Defense:* `safety: 41`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rtc-node.linux-x64-musl.node, rtc-node-win32-x64-msvc, rtc-node.linux-riscv64-musl.node, rtc-node-win32-ia32-msvc, rtc-node-linux-arm64-gnu, rtc-node.win32-x64-msvc.node, rtc-node.android-arm-eabi.node, fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_mixer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.529 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.354 IQR)
- **Top Global Matches:** file_cluster_4: 13.529, file_cluster_13: 14.039, file_cluster_17: 14.051
- **Magnitude:** 22.95 | **LOC:** 419 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9437%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getContribution` (Impact: 43.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 13`, `args: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 129`
* *Architecture:* `api: 1`, `concurrency: 54`, `import: 4`
* *Defense:* `safety: 6`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_frame.js, async_queue.js, log.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/data_streams/stream_reader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.576 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.097 IQR)
- **Top Global Matches:** file_cluster_4: 13.576, file_cluster_13: 13.861, file_cluster_2: 14.012
- **Magnitude:** 21.76 | **LOC:** 159 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.9489%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `readAll` (Impact: 16.2)
  * `next` (Impact: 10.8)
  * `next` (Impact: 10.7)
  * `handleChunkReceived` (Impact: 10.7)
  * `Symbol.asyncIterator` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 37`, `args: 15`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 70`, `duplicate_logic: 11`
* *Architecture:* `api: 2`, `concurrency: 53`, `import: 4`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` room_pb.js, log.js, utils.js, types.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/proto/rpc_pb.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.212 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.09 IQR)
- **Top Global Matches:** file_cluster_16: 10.212, file_cluster_2: 10.222, file_cluster_8: 10.666
- **Magnitude:** 21.36 | **LOC:** 540 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.7533%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 3.7)
    * *Intent:* /** * @generated from field: required string message = 2;
  * `constructor` (Impact: 3.7)
    * *Intent:* /** * @generated from field: required uint64 local_participant_handle = 1; */
  * `constructor` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 91`, `args: 77`, `func_start: 66`, `class_start: 11`
* *Risk/State:* `duplicate_logic: 64`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 39`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_stream.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.834 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.198 IQR)
- **Top Global Matches:** file_cluster_13: 12.834, file_cluster_11: 13.28, file_cluster_2: 13.34
- **Magnitude:** 17.0 | **LOC:** 137 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.7624%), Tech Debt (85.0342%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 42.4)
  * `onEvent` (Impact: 33.6)
  * `constructor` (Impact: 7.1)
  * `start` (Impact: 1.9)
  * `cancel` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 25`, `args: 10`, `func_start: 10`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 76`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_frame.js, ffi_client.js, log.js, frame_processor.js, web, audio_frame_pb.js, track.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/e2ee.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.645 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_8: 10.645, file_cluster_13: 10.944, file_cluster_2: 11.121
- **Magnitude:** 16.14 | **LOC:** 316 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.9184%), Tech Debt (89.2117%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 7.4)
  * `exportSharedKey` (Impact: 6.2)
  * `ratchetSharedKey` (Impact: 6.2)
  * `exportKey` (Impact: 6.2)
  * `ratchetKey` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 22`, `args: 14`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 73`, `duplicate_logic: 5`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, e2ee_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/video_frame.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.585 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.152 IQR)
- **Top Global Matches:** file_cluster_8: 10.585, file_cluster_13: 10.799, file_cluster_7: 11.025
- **Magnitude:** 15.81 | **LOC:** 232 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.9901%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPlaneLength` (Impact: 27.2)
  * `getPlaneInfos` (Impact: 27.1)
  * `protoInfo` (Impact: 15.4)
    * *Intent:* /** @internal */
  * `convert` (Impact: 13.2)
  * `getPlane` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 43`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 56`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 1`, `doc: 3`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` video_frame_pb.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/napi/native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.771 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.967 IQR)
- **Top Global Matches:** file_cluster_8: 5.771, file_cluster_13: 6.612, file_cluster_7: 7.059
- **Magnitude:** 15.68 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` native.cjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_source.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.537 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.112 IQR)
- **Top Global Matches:** file_cluster_4: 12.537, file_cluster_13: 12.731, file_cluster_11: 13.124
- **Magnitude:** 15.37 | **LOC:** 152 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.984%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `captureFrame` (Impact: 19.9)
  * `constructor` (Impact: 5.2)
  * `clearQueue` (Impact: 3.6)
  * `waitForPlayout` (Impact: 2.1)
  * `queuedDuration` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 20`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 60`
* *Architecture:* `api: 8`, `concurrency: 43`, `import: 5`
* *Defense:* `safety: 2`, `doc: 8`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_frame.js, audio_frame_pb.js, native.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/track.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.336 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.881 IQR)
- **Top Global Matches:** file_cluster_4: 12.336, file_cluster_13: 12.659, file_cluster_8: 13.084
- **Magnitude:** 14.11 | **LOC:** 128 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1742%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `close` (Impact: 7.0)
  * `close` (Impact: 7.0)
  * `createAudioTrack` (Impact: 4.1)
  * `createVideoTrack` (Impact: 4.1)
  * `constructor` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 41`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 30`, `duplicate_logic: 8`
* *Architecture:* `api: 10`, `concurrency: 42`, `import: 5`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 4`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` video_source.js, track_pb.js, audio_source.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/track_publication.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.913 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.607 IQR)
- **Top Global Matches:** file_cluster_4: 13.913, file_cluster_13: 14.107, file_cluster_11: 14.52
- **Magnitude:** 13.61 | **LOC:** 113 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.2248%), Tech Debt (99.821%)
**Top Internal Functions/Classes:**
  * `setSubscribed` (Impact: 4.0)
  * `sid` (Impact: 3.6)
  * `name` (Impact: 3.6)
  * `kind` (Impact: 3.6)
  * `source` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 32`, `args: 20`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 47`, `duplicate_logic: 3`
* *Architecture:* `api: 5`, `concurrency: 30`, `import: 7`
* *Defense:* `safety: 15`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, native.js, room_pb.js, e2ee_pb.js, track_pb.js, track.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/async_queue.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.451 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 7.441 IQR)
- **Top Global Matches:** file_cluster_4: 14.451, file_cluster_17: 15.087, file_cluster_13: 15.173
- **Magnitude:** 12.7 | **LOC:** 81 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.3324%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `put` (Impact: 10.9)
    * *Intent:* /** * AsyncQueue is a bounded queue with async support for both producers and consumers. * * This qu...
  * `waitForItem` (Impact: 5.5)
  * `get` (Impact: 3.2)
  * `constructor` (Impact: 2.5)
    * *Intent:* /** * AsyncQueue is a bounded queue with async support for both producers and consumers. * * This qu...
  * `close` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 15`, `args: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`
* *Architecture:* `api: 4`, `concurrency: 42`, `import: 1`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deque
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/proto/track_publication_pb.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.867 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_16: 9.867, file_cluster_2: 9.891, file_cluster_8: 10.356
- **Magnitude:** 11.4 | **LOC:** 285 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9197%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 54`, `args: 42`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `duplicate_logic: 33`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 17`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/video_stream.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.628 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.315 IQR)
- **Top Global Matches:** file_cluster_13: 10.628, file_cluster_2: 11.108, file_cluster_16: 11.209
- **Magnitude:** 6.07 | **LOC:** 87 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.5665%), Tech Debt (98.8393%)
**Top Internal Functions/Classes:**
  * `onEvent` (Impact: 23.6)
  * `constructor` (Impact: 4.3)
  * `start` (Impact: 1.9)
  * `constructor` (Impact: 1.9)
  * `cancel` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 21`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 22`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` video_frame_pb.js, ffi_client.js, video_frame.js, web, track.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/ffi_client.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.835 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.347 IQR)
- **Top Global Matches:** file_cluster_13: 10.835, file_cluster_4: 11.016, file_cluster_16: 11.244
- **Magnitude:** 5.83 | **LOC:** 83 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.3107%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `waitFor` (Impact: 5.0)
  * `instance` (Impact: 4.3)
    * *Intent:* /** @internal */
  * `listener` (Impact: 4.3)
  * `ffi_event` (Impact: 2.3)
  * `livekitInitialize` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 31`, `args: 13`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 9`, `concurrency: 13`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf, ffi_pb.js, native.js, version.js, typed-emitter, events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/data_streams/stream_writer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.82 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 7.061 IQR)
- **Top Global Matches:** file_cluster_4: 14.82, file_cluster_13: 15.268, file_cluster_16: 15.324
- **Magnitude:** 5.34 | **LOC:** 36 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 4.3)
  * `close` (Impact: 3.7)
  * `write` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `args: 4`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 3`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_resampler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.99 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.738 IQR)
- **Top Global Matches:** file_cluster_8: 7.99, file_cluster_7: 8.379, file_cluster_13: 8.421
- **Magnitude:** 5.13 | **LOC:** 182 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7504%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 21.4)
    * *Intent:* /** * AudioResampler provides functionality to resample audio data from an input sample rate to * an...
  * `push` (Impact: 8.5)
  * `flush` (Impact: 7.2)
  * `inputRate` (Impact: 1.9)
  * `outputRate` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 16`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `doc: 11`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_frame.js, audio_frame_pb.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_frame.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.747 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.815 IQR)
- **Top Global Matches:** file_cluster_13: 10.747, file_cluster_8: 10.979, file_cluster_16: 11.161
- **Magnitude:** 4.86 | **LOC:** 108 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.7904%), Tech Debt (39.0501%)
**Top Internal Functions/Classes:**
  * `combineAudioFrames` (Impact: 17.3)
    * *Intent:* /**
  * `fromOwnedInfo` (Impact: 2.6)
    * *Intent:* /** @internal */
  * `create` (Impact: 2.2)
  * `userdata` (Impact: 1.9)
    * *Intent:* /** Returns the user data associated with the audio frame. */
  * `protoInfo` (Impact: 1.8)
    * *Intent:* /** @internal */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 13`, `fragile_debt: 1`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 3`, `doc: 5`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_frame_pb.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.495 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.787 IQR)
- **Top Global Matches:** file_cluster_16: 11.495, file_cluster_8: 11.79, file_cluster_7: 12.066
- **Magnitude:** 4.52 | **LOC:** 43 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.7652%), Tech Debt (99.8629%)
**Top Internal Functions/Classes:**
  * `splitUtf8` (Impact: 15.1)
  * `bigIntToNumber` (Impact: 7.2)
    * *Intent:* // SPDX-FileCopyrightText: 2024 LiveKit, Inc. // // SPDX-License-Identifier: Apache-2.0 /** convert ...
  * `numberToBigInt` (Impact: 7.2)
    * *Intent:* /** convert numbers to bigints preserving undefined values */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 3`
* *Architecture:* `api: 3`
* *Defense:* `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/proto/participant_pb.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.711 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.815 IQR)
- **Top Global Matches:** file_cluster_16: 9.711, file_cluster_2: 9.762, file_cluster_8: 9.87
- **Magnitude:** 4.4 | **LOC:** 352 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.753%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 3.7)
  * `constructor` (Impact: 3.7)
  * `fromBinary` (Impact: 3.6)
    * *Intent:* /** * SIP callee rejected the call (busy) * * @generated from enum value: USER_REJECTED = 12;
  * `fromJson` (Impact: 3.6)
    * *Intent:* /**
  * `fromJsonString` (Impact: 3.6)
    * *Intent:* /** * SIP protocol failure or unexpected response * * @generated from enum value: SIP_TRUNK_FAILURE ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 29`, `args: 14`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `duplicate_logic: 12`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `doc: 41`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf, handle_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.561 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.46 IQR)
- **Top Global Matches:** file_cluster_13: 7.561, file_cluster_8: 7.886, file_cluster_7: 8.793
- **Magnitude:** 4.31 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`
* *Risk/State:* None
* *Architecture:* `api: 27`, `import: 27`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2ee.js, ffi_client.js, room_pb.js, e2ee_pb.js, transcription.js, audio_stream.js, audio_filter.js, video_frame_pb.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/video_source.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.027 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.424 IQR)
- **Top Global Matches:** file_cluster_13: 11.027, file_cluster_4: 11.309, file_cluster_8: 11.46
- **Magnitude:** 4.15 | **LOC:** 77 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8882%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 6.3)
  * `captureFrame` (Impact: 6.1)
  * `close` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`
* *Architecture:* `api: 4`, `concurrency: 6`, `import: 4`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` video_frame_pb.js, video_frame.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/src/nodejs.rs` (RUST) | Magnitude: 43.68 | Delta: **0.429 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 26, safety: 19, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/room.ts` (TYPESCRIPT) | Magnitude: 118.05 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 736, state_mutation: 458, branch: 277, structural_boundaries: 142
- `package/src/audio_filter.ts` (TYPESCRIPT) | Magnitude: 0.93 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, import: 3, branch: 2
- `package/src/napi/native.cjs` (JAVASCRIPT) | Magnitude: 31.84 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 267, branch: 133, safety: 41, import: 39
- `package/src/ffi_client.ts` (TYPESCRIPT) | Magnitude: 5.83 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 31, args: 13, concurrency: 13
- `package/src/log.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.207 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, immutability_locks: 3, api: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/src/proto/rpc_pb.ts` (TYPESCRIPT) | Magnitude: 21.36 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 276, generics: 121, structural_boundaries: 91, args: 77
- `package/src/proto/track_publication_pb.ts` (TYPESCRIPT) | Magnitude: 11.4 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 140, generics: 66, structural_boundaries: 54, args: 42
- `package/src/rpc.ts` (TYPESCRIPT) | Magnitude: 3.2 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, doc: 14, structural_boundaries: 12, state_mutation: 12
- `package/src/proto/participant_pb.ts` (TYPESCRIPT) | Magnitude: 4.4 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 112, doc: 41, structural_boundaries: 29, generics: 22
- `package/src/proto/handle_pb.ts` (TYPESCRIPT) | Magnitude: 2.17 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, generics: 11, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/participant.ts` (TYPESCRIPT) | Magnitude: 66.15 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 661, concurrency: 179, branch: 164, structural_boundaries: 155
- `package/src/audio_source.ts` (TYPESCRIPT) | Magnitude: 15.37 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 60, concurrency: 43, structural_boundaries: 20
- `package/src/track_publication.ts` (TYPESCRIPT) | Magnitude: 13.61 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 47, structural_boundaries: 32, concurrency: 30
- `package/src/data_streams/stream_reader.ts` (TYPESCRIPT) | Magnitude: 21.76 | Delta: **0.285 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, state_mutation: 70, concurrency: 53, structural_boundaries: 37
- `package/src/track.ts` (TYPESCRIPT) | Magnitude: 14.11 | Delta: **0.323 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, concurrency: 42, structural_boundaries: 41, state_mutation: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/data_streams/types.ts` (TYPESCRIPT) | Magnitude: 2.48 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 22, branch: 10, api: 9
- `package/src/video_frame.ts` (TYPESCRIPT) | Magnitude: 15.81 | Delta: **0.214 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 199, state_mutation: 56, structural_boundaries: 43, branch: 36
- `package/src/e2ee.ts` (TYPESCRIPT) | Magnitude: 16.14 | Delta: **0.299 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 249, state_mutation: 73, branch: 28, structural_boundaries: 22
- `package/src/audio_resampler.ts` (TYPESCRIPT) | Magnitude: 5.13 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 113, encapsulation: 19, structural_boundaries: 16, branch: 13
- `package/src/napi/native.d.ts` (TYPESCRIPT) | Magnitude: 0.93 | Delta: **0.465 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 14, func_start: 9, args: 8, api: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/index.ts` -> **Severity: 2631.592** (Blast Radius: 26.316 * Doc Risk: 99.9997%)
- `package/src/data_streams/types.ts` -> **Severity: 2551.968** (Blast Radius: 26.316 * Doc Risk: 96.974%)
- `package/src/napi/native.d.ts` -> **Severity: 2435.459** (Blast Radius: 26.316 * Doc Risk: 92.5467%)
- `package/src/frame_processor.ts` -> **Severity: 2367.274** (Blast Radius: 26.316 * Doc Risk: 89.9557%)
- `package/src/ffi_client.ts` -> **Severity: 2282.574** (Blast Radius: 26.316 * Doc Risk: 86.7371%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
