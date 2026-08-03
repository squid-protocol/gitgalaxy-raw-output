# ARCHITECTURAL_BRIEF: @livekit_rtc-node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@livekit_rtc-node` |
| **Timestamp** | `2026-08-03T21:08:13.161393+00:00` |
| **Scan Duration** | `0.28s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 36 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Cognitive Load Exposure | 0.0 | 100.0 | 32.5 | 15.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 45.6 | 61.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.9 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 32.4 | 2.6 | 80.0 |
| API Exposure | 0.9 | 16.3 | 6.6 | 6.3 | 3.7 |
| Concurrency Exposure | 0.0 | 100.0 | 32.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.1 | 53.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.8 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.7 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 100.0 | 52.0 | 44.7 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 35.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `processFfiEvent` (@ `package/src/room.ts`) -> Impact: **1334.8** | LOC: 297
  * *Intent:* /**
- `connect` (@ `package/src/room.ts`) -> Impact: **138.8** | LOC: 56
- `onEvent` (@ `package/src/audio_stream.ts`) -> Impact: **129.6** | LOC: 32
- `editChatMessage` (@ `package/src/participant.ts`) -> Impact: **90.3** | LOC: 42
- `constructor` (@ `package/src/audio_stream.ts`) -> Impact: **82.7** | LOC: 44
- `handleStreamHeader` (@ `package/src/room.ts`) -> Impact: **79.7** | LOC: 70
- `handleRpcMethodInvocation` (@ `package/src/participant.ts`) -> Impact: **75.8** | LOC: 46
  * *Intent:* /** * Establishes the participant as a receiver for calls of the specified RPC method. * Will overwrite any existing callback for the same method. * *...
- `sendChatMessage` (@ `package/src/participant.ts`) -> Impact: **75.5** | LOC: 34
- `publishTrack` (@ `package/src/participant.ts`) -> Impact: **67.8** | LOC: 36
- `onEvent` (@ `package/src/video_stream.ts`) -> Impact: **67.6** | LOC: 32

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `onEvent` (@ `package/src/audio_stream.ts`) -> **O(2^N) [Recursive]**
- `readAll` (@ `package/src/data_streams/stream_reader.ts`) -> **O(2^N) [Recursive]**
- `publishTranscription` (@ `package/src/participant.ts`) -> **O(2^N) [Recursive]**
- `processFfiEvent` (@ `package/src/room.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `connect` (@ `package/src/room.ts`) -> **O(2^N) [Recursive]**
- `ratchetSharedKey` (@ `package/src/e2ee.ts`) -> **O(2^N) [Recursive]**
- `ratchetKey` (@ `package/src/e2ee.ts`) -> **O(2^N) [Recursive]**
- `setSharedKey` (@ `package/src/e2ee.ts`) -> **O(2^N) [Recursive]**
- `setKey` (@ `package/src/e2ee.ts`) -> **O(2^N) [Recursive]**
- `frameCryptors` (@ `package/src/e2ee.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `processFfiEvent` (@ `package/src/room.ts`) -> DB Complexity: **78**
  * *Intent:* /**
- `getContribution` (@ `package/src/audio_mixer.ts`) -> DB Complexity: **19**
- `constructor` (@ `package/src/audio_stream.ts`) -> DB Complexity: **17**
- `captureFrame` (@ `package/src/audio_source.ts`) -> DB Complexity: **12**
- `connect` (@ `package/src/room.ts`) -> DB Complexity: **12**
- `protoInfo` (@ `package/src/video_frame.ts`) -> DB Complexity: **12**
  * *Intent:* /** @internal */
- `onEvent` (@ `package/src/audio_stream.ts`) -> DB Complexity: **10**
- `sendFile` (@ `package/src/participant.ts`) -> DB Complexity: **10**
- `onFfiEvent` (@ `package/src/room.ts`) -> DB Complexity: **10**
- `put` (@ `package/src/async_queue.ts`) -> DB Complexity: **9**
  * *Intent:* /** * AsyncQueue is a bounded queue with async support for both producers and consumers. * * This queue simplifies the AudioMixer implementation by ha...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src` | 25 | 621.5 | 37.23% | 33.12% |
| `package/src/proto` | 4 | 60.93 | 4.82% | 75.0% |
| `package/src/napi` | 3 | 48.45 | 13.19% | 33.02% |
| `package/src/data_streams` | 4 | 33.97 | 44.97% | 24.94% |
| `package` | 2 | 4.64 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/proto/participant_pb.ts` -> **100.0%** Exposure
- `package/src/proto/rpc_pb.ts` -> **100.0%** Exposure
- `package/src/proto/track_publication_pb.ts` -> **100.0%** Exposure
- `package/src/track.ts` -> **100.0%** Exposure
- `package/src/utils.ts` -> **99.8629%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/async_queue.ts` -> **100.0%** Exposure
- `package/src/audio_mixer.ts` -> **100.0%** Exposure
- `package/src/audio_source.ts` -> **100.0%** Exposure
- `package/src/audio_stream.ts` -> **100.0%** Exposure
- `package/src/data_streams/stream_reader.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/proto/rpc_pb.ts` -> **0** Orphaned Functions | **55** Duplicates
- `package/src/proto/track_publication_pb.ts` -> **0** Orphaned Functions | **30** Duplicates
- `package/src/proto/participant_pb.ts` -> **0** Orphaned Functions | **10** Duplicates
- `package/src/participant.ts` -> **0** Orphaned Functions | **9** Duplicates
- `package/src/track.ts` -> **0** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/napi/native.cjs`** -> AI Confidence: **99.48%**
2. **`package/src/audio_stream.ts`** -> AI Confidence: **99.31%**
3. **`package/src/participant.ts`** -> AI Confidence: **99.31%**
4. **`package/src/room.ts`** -> AI Confidence: **99.31%**
5. **`package/src/audio_mixer.ts`** -> AI Confidence: **99.2%**
6. **`package/src/nodejs.rs`** -> AI Confidence: **99.18%**
7. **`package/src/index.ts`** -> AI Confidence: **99.09%**
8. **`package/src/e2ee.ts`** -> AI Confidence: **99.06%**
9. **`package/src/types.ts`** -> AI Confidence: **99.06%**
10. **`package/src/utils.ts`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/src/audio_stream.ts` -> **100.0%** Exposure
- `package/src/participant.ts` -> **100.0%** Exposure
- `package/src/room.ts` -> **100.0%** Exposure
- `package/src/data_streams/stream_reader.ts` -> **99.9869%** Exposure
- `package/src/nodejs.rs` -> **0.0121%** Exposure
### Raw Memory Manipulation
- `package/src/nodejs.rs` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `package/src/audio_mixer.ts` -> **100.0%** Exposure
- `package/src/audio_source.ts` -> **100.0%** Exposure
- `package/src/audio_stream.ts` -> **100.0%** Exposure
- `package/src/data_streams/stream_reader.ts` -> **100.0%** Exposure
- `package/src/room.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `51` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/data_streams/stream_reader.ts` (TYPESCRIPT) -> Cumulative Risk: **968.81**
- **Archetype:** `file_cluster_4` (Distance: 13.569 IQR)
- **Magnitude:** 24.17 | **LOC:** 159 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `readAll` (Impact: 57.8), `next` (Impact: 20.9), `handleChunkReceived` (Impact: 10.7)

### 2. `package/src/participant.ts` (TYPESCRIPT) -> Cumulative Risk: **898.79**
- **Archetype:** `file_cluster_4` (Distance: 12.259 IQR)
- **Magnitude:** 102.37 | **LOC:** 873 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.4266%)
- **Heaviest Functions:** `editChatMessage` (Impact: 90.3), `handleRpcMethodInvocation` (Impact: 75.8), `sendChatMessage` (Impact: 75.5)

### 3. `package/src/audio_stream.ts` (TYPESCRIPT) -> Cumulative Risk: **885.1**
- **Archetype:** `file_cluster_13` (Distance: 12.834 IQR)
- **Magnitude:** 30.63 | **LOC:** 137 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `onEvent` (Impact: 129.6), `constructor` (Impact: 82.7), `constructor` (Impact: 7.1)

### 4. `package/src/room.ts` (TYPESCRIPT) -> Cumulative Risk: **851.16**
- **Archetype:** `file_cluster_13` (Distance: 14.453 IQR)
- **Magnitude:** 236.58 | **LOC:** 900 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `processFfiEvent` (Impact: 1334.8), `connect` (Impact: 138.8), `handleStreamHeader` (Impact: 79.7)

### 5. `package/src/video_stream.ts` (TYPESCRIPT) -> Cumulative Risk: **796.81**
- **Archetype:** `file_cluster_13` (Distance: 10.628 IQR)
- **Magnitude:** 10.64 | **LOC:** 87 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.95%), Tech Debt (98.8393%), Algorithmic Dos (98.8096%)
- **Heaviest Functions:** `onEvent` (Impact: 67.6), `constructor` (Impact: 6.0), `start` (Impact: 1.9)

### 6. `package/src/track.ts` (TYPESCRIPT) -> Cumulative Risk: **782.33**
- **Archetype:** `file_cluster_4` (Distance: 12.338 IQR)
- **Magnitude:** 17.34 | **LOC:** 128 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.988%)
- **Heaviest Functions:** `close` (Impact: 13.7), `close` (Impact: 13.7), `createAudioTrack` (Impact: 7.5)

### 7. `package/src/audio_mixer.ts` (TYPESCRIPT) -> Cumulative Risk: **742.6**
- **Archetype:** `file_cluster_4` (Distance: 13.529 IQR)
- **Magnitude:** 24.97 | **LOC:** 419 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getContribution` (Impact: 63.5)

### 8. `package/src/track_publication.ts` (TYPESCRIPT) -> Cumulative Risk: **721.9**
- **Archetype:** `file_cluster_4` (Distance: 13.914 IQR)
- **Magnitude:** 17.29 | **LOC:** 113 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.821%)
- **Heaviest Functions:** `setSubscribed` (Impact: 7.4), `sid` (Impact: 7.1), `name` (Impact: 7.1)

### 9. `package/src/e2ee.ts` (TYPESCRIPT) -> Cumulative Risk: **684.69**
- **Archetype:** `file_cluster_8` (Distance: 10.684 IQR)
- **Magnitude:** 22.45 | **LOC:** 316 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9999%), State Flux (99.8832%), Tech Debt (89.2117%)
- **Heaviest Functions:** `ratchetSharedKey` (Impact: 16.6), `ratchetKey` (Impact: 16.6), `setSharedKey` (Impact: 16.5)

### 10. `package/src/ffi_client.ts` (TYPESCRIPT) -> Cumulative Risk: **665.44**
- **Archetype:** `file_cluster_13` (Distance: 10.802 IQR)
- **Magnitude:** 5.71 | **LOC:** 83 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (95.4913%), Algorithmic Dos (89.7216%)
- **Heaviest Functions:** `waitFor` (Impact: 7.3), `ffi_event` (Impact: 4.3), `instance` (Impact: 4.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/room.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.453 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.627 IQR)
- **Top Global Matches:** file_cluster_13: 14.453, file_cluster_4: 14.56, file_cluster_11: 14.627
- **Magnitude:** 236.58 | **LOC:** 900 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 78
- **Risk Profile:** Cognitive Load (70.9477%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `processFfiEvent` (Impact: 1334.8 | O(2^N) | DB: 78)
    * *Intent:* /**
  * `connect` (Impact: 138.8 | O(2^N) | DB: 12)
  * `handleStreamHeader` (Impact: 79.7 | O(N^3) | DB: 8)
  * `disconnect` (Impact: 32.2 | O(2^N) | DB: 4)
  * `onFfiEvent` (Impact: 21.9 | O(N^2) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 142`, `args: 83`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 460`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `concurrency: 62`, `import: 23`
* *Defense:* `safety: 93`, `doc: 22`, `sync_locks: 4`, `immutability_locks: 67`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2ee_pb.js, log.js, events, track_publication.js, track_pb.js, participant.js, ffi_pb.js, utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/participant.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.259 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.341 IQR)
- **Top Global Matches:** file_cluster_4: 12.259, file_cluster_13: 12.442, file_cluster_2: 12.637
- **Magnitude:** 102.37 | **LOC:** 873 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (61.407%), Tech Debt (92.3123%)
**Top Internal Functions/Classes:**
  * `editChatMessage` (Impact: 90.3 | O(2^N) | DB: 1)
  * `handleRpcMethodInvocation` (Impact: 75.8 | O(N^3) | DB: 4)
    * *Intent:* /** * Establishes the participant as a receiver for calls of the specified RPC method. * Will overwr...
  * `sendChatMessage` (Impact: 75.5 | O(2^N) | DB: 1)
  * `publishTrack` (Impact: 67.8 | O(2^N) | DB: 4)
  * `unpublishTrack` (Impact: 58.7 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 155`, `args: 59`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 120`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 5`, `api: 11`, `concurrency: 179`, `import: 17`
* *Defense:* `safety: 41`, `doc: 23`, `sync_locks: 8`, `immutability_locks: 89`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, log.js, promises, track_publication.js, node:fs, utils.js, ffi_client.js, room_pb.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/nodejs.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.418 IQR)
- **Top Global Matches:** file_cluster_0: 12.418, file_cluster_13: 12.845, file_cluster_11: 12.923
- **Magnitude:** 68.28 | **LOC:** 135 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.5216%), Tech Debt (99.8414%)
**Top Internal Functions/Classes:**
  * `livekit_ffi_request` (Impact: 21.3 | O(N^4))
  * `dispose` (Impact: 9.7 | O(N^2) | DB: 1)
  * `livekit_initialize` (Impact: 9.2 | O(N^3))
  * `handle` (Impact: 3.7 | O(2^N))
  * `new` (Impact: 3.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 26`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` napi_derive::napi, threadsafe_function::
        ErrorStrategy, ThreadsafeFunction, prost::Message, std::sync::Arc, server, JsFunction, napi::
    bindgen_prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/proto/rpc_pb.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.214 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.067 IQR)
- **Top Global Matches:** file_cluster_16: 10.214, file_cluster_2: 10.224, file_cluster_8: 10.667
- **Magnitude:** 33.16 | **LOC:** 540 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.7533%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fromBinary` (Impact: 7.1 | O(2^N))
  * `fromJson` (Impact: 7.1 | O(2^N))
  * `fromJsonString` (Impact: 7.1 | O(2^N))
  * `fromBinary` (Impact: 7.1 | O(2^N))
    * *Intent:* /** * @generated from field: required string payload = 4; */
  * `fromJson` (Impact: 7.1 | O(2^N))
    * *Intent:* /** * @generated from field: optional uint32 response_timeout_ms = 5;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 91`, `args: 77`, `func_start: 66`, `class_start: 11`
* *Risk/State:* `duplicate_logic: 55`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 39`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/napi/native.cjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.101 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.171 IQR)
- **Top Global Matches:** file_cluster_13: 11.101, file_cluster_0: 11.28, file_cluster_8: 11.284
- **Magnitude:** 31.84 | **LOC:** 302 | **CtrlFlow:** 95.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (29.5755%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isMusl` (Impact: 11.1 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 3`, `api: 6`, `import: 39`
* *Defense:* `safety: 41`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rtc-node.android-arm64.node, rtc-node.win32-x64-msvc.node, rtc-node-linux-riscv64-musl, rtc-node.linux-riscv64-musl.node, rtc-node-linux-arm64-gnu, rtc-node.linux-x64-gnu.node, rtc-node.darwin-arm64.node, rtc-node.linux-s390x-gnu.node...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_stream.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.834 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.198 IQR)
- **Top Global Matches:** file_cluster_13: 12.834, file_cluster_11: 13.28, file_cluster_2: 13.34
- **Magnitude:** 30.63 | **LOC:** 137 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (73.7624%), Tech Debt (85.0342%)
**Top Internal Functions/Classes:**
  * `onEvent` (Impact: 129.6 | O(2^N) | DB: 10)
  * `constructor` (Impact: 82.7 | O(N^3) | DB: 17)
  * `constructor` (Impact: 7.1 | O(N^1))
  * `start` (Impact: 1.9 | O(N^1) | DB: 1)
  * `cancel` (Impact: 1.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 25`, `args: 10`, `func_start: 10`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 76`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` log.js, frame_processor.js, audio_frame_pb.js, ffi_client.js, track.js, audio_frame.js, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_mixer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.529 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.354 IQR)
- **Top Global Matches:** file_cluster_4: 13.529, file_cluster_13: 14.039, file_cluster_17: 14.051
- **Magnitude:** 24.97 | **LOC:** 419 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (99.9437%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getContribution` (Impact: 63.5 | O(N^2) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 13`, `args: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 129`
* *Architecture:* `api: 1`, `concurrency: 54`, `import: 4`
* *Defense:* `safety: 6`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` log.js, async_queue.js, audio_frame.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/data_streams/stream_reader.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.569 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.081 IQR)
- **Top Global Matches:** file_cluster_4: 13.569, file_cluster_13: 13.893, file_cluster_2: 14.037
- **Magnitude:** 24.17 | **LOC:** 159 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (66.0464%), Tech Debt (99.7464%)
**Top Internal Functions/Classes:**
  * `readAll` (Impact: 57.8 | O(2^N) | DB: 8)
  * `next` (Impact: 20.9 | O(N^3) | DB: 1)
  * `handleChunkReceived` (Impact: 10.7 | O(N^1) | DB: 7)
  * `constructor` (Impact: 4.9 | O(N^1) | DB: 1)
    * *Intent:* /** * A class to read chunks from a ReadableStream and provide them in a structured format. */
  * `constructor` (Impact: 4.3 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 37`, `args: 15`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 70`, `duplicate_logic: 4`
* *Architecture:* `api: 2`, `concurrency: 63`, `import: 4`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, types.js, log.js, room_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/e2ee.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.684 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.065 IQR)
- **Top Global Matches:** file_cluster_8: 10.684, file_cluster_13: 10.982, file_cluster_2: 11.158
- **Magnitude:** 22.45 | **LOC:** 316 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (37.9184%), Tech Debt (89.2117%)
**Top Internal Functions/Classes:**
  * `ratchetSharedKey` (Impact: 16.6 | O(2^N) | DB: 1)
  * `ratchetKey` (Impact: 16.6 | O(2^N) | DB: 1)
  * `setSharedKey` (Impact: 16.5 | O(2^N) | DB: 1)
  * `setKey` (Impact: 16.5 | O(2^N) | DB: 1)
  * `frameCryptors` (Impact: 14.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 22`, `args: 18`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 73`, `duplicate_logic: 5`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2ee_pb.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/video_frame.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.585 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.152 IQR)
- **Top Global Matches:** file_cluster_8: 10.585, file_cluster_13: 10.799, file_cluster_7: 11.025
- **Magnitude:** 18.32 | **LOC:** 232 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (38.9901%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPlaneInfos` (Impact: 38.1 | O(N^2))
  * `getPlaneLength` (Impact: 27.2 | O(N^1))
  * `protoInfo` (Impact: 22.5 | O(N^2) | DB: 12)
    * *Intent:* /** @internal */
  * `convert` (Impact: 19.2 | O(N^2) | DB: 1)
  * `fromOwnedInfo` (Impact: 3.8 | O(N^2))
    * *Intent:* /** @internal */
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

### `package/src/proto/track_publication_pb.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.868 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.177 IQR)
- **Top Global Matches:** file_cluster_16: 9.868, file_cluster_2: 9.892, file_cluster_8: 10.357
- **Magnitude:** 18.18 | **LOC:** 285 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.9197%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fromBinary` (Impact: 7.1 | O(2^N))
  * `fromJson` (Impact: 7.1 | O(2^N))
    * *Intent:* /** * @generated from field: required bool enabled = 2; */
  * `fromJsonString` (Impact: 7.1 | O(2^N))
  * `fromBinary` (Impact: 7.1 | O(2^N))
  * `fromJson` (Impact: 7.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 54`, `args: 42`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `duplicate_logic: 30`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 17`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/track.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.338 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.881 IQR)
- **Top Global Matches:** file_cluster_4: 12.338, file_cluster_13: 12.661, file_cluster_8: 13.087
- **Magnitude:** 17.34 | **LOC:** 128 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (79.1742%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `close` (Impact: 13.7 | O(2^N) | DB: 1)
  * `close` (Impact: 13.7 | O(2^N) | DB: 1)
  * `createAudioTrack` (Impact: 7.5 | O(2^N))
  * `createVideoTrack` (Impact: 7.5 | O(2^N))
  * `sid` (Impact: 7.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 41`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 30`, `duplicate_logic: 8`
* *Architecture:* `api: 10`, `concurrency: 42`, `import: 5`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 4`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, video_source.js, track_pb.js, audio_source.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/track_publication.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.914 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.607 IQR)
- **Top Global Matches:** file_cluster_4: 13.914, file_cluster_13: 14.109, file_cluster_11: 14.521
- **Magnitude:** 17.29 | **LOC:** 113 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (64.2248%), Tech Debt (99.821%)
**Top Internal Functions/Classes:**
  * `setSubscribed` (Impact: 7.4 | O(2^N) | DB: 1)
  * `sid` (Impact: 7.1 | O(2^N) | DB: 1)
  * `name` (Impact: 7.1 | O(2^N) | DB: 1)
  * `kind` (Impact: 7.1 | O(2^N) | DB: 1)
  * `source` (Impact: 7.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 32`, `args: 20`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 47`, `duplicate_logic: 3`
* *Architecture:* `api: 5`, `concurrency: 30`, `import: 7`
* *Defense:* `safety: 15`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2ee_pb.js, track_pb.js, native.js, ffi_client.js, room_pb.js, track.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_source.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.717 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.145 IQR)
- **Top Global Matches:** file_cluster_4: 12.717, file_cluster_13: 12.913, file_cluster_11: 13.292
- **Magnitude:** 16.22 | **LOC:** 152 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (49.9825%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `captureFrame` (Impact: 19.9 | O(N^1) | DB: 12)
  * `constructor` (Impact: 7.2 | O(N^2) | DB: 7)
  * `clearQueue` (Impact: 5.0 | O(N^2) | DB: 3)
  * `waitForPlayout` (Impact: 2.1 | O(N^1) | DB: 6)
  * `queuedDuration` (Impact: 2.0 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 20`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 68`
* *Architecture:* `api: 7`, `concurrency: 43`, `import: 5`
* *Defense:* `safety: 2`, `doc: 8`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, native.js, audio_frame_pb.js, audio_frame.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/napi/native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.771 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.967 IQR)
- **Top Global Matches:** file_cluster_8: 5.771, file_cluster_13: 6.612, file_cluster_7: 7.059
- **Magnitude:** 15.68 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

### `package/src/async_queue.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.451 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 7.441 IQR)
- **Top Global Matches:** file_cluster_4: 14.451, file_cluster_17: 15.087, file_cluster_13: 15.173
- **Magnitude:** 13.37 | **LOC:** 81 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (58.3324%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `put` (Impact: 15.9 | O(N^2) | DB: 9)
    * *Intent:* /** * AsyncQueue is a bounded queue with async support for both producers and consumers. * * This qu...
  * `waitForItem` (Impact: 5.5 | O(N^1) | DB: 3)
  * `length` (Impact: 3.6 | O(2^N) | DB: 1)
  * `get` (Impact: 3.2 | O(N^1) | DB: 4)
  * `constructor` (Impact: 2.5 | O(N^1))
    * *Intent:* /** * AsyncQueue is a bounded queue with async support for both producers and consumers. * * This qu...
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

### `package/src/video_stream.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.628 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.315 IQR)
- **Top Global Matches:** file_cluster_13: 10.628, file_cluster_2: 11.108, file_cluster_16: 11.209
- **Magnitude:** 10.64 | **LOC:** 87 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (78.5665%), Tech Debt (98.8393%)
**Top Internal Functions/Classes:**
  * `onEvent` (Impact: 67.6 | O(2^N) | DB: 5)
  * `constructor` (Impact: 6.0 | O(N^2) | DB: 2)
  * `start` (Impact: 1.9 | O(N^1) | DB: 1)
  * `constructor` (Impact: 1.9 | O(N^1))
  * `cancel` (Impact: 1.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 21`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 22`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, video_frame.js, track.js, video_frame_pb.js, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_resampler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.99 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.738 IQR)
- **Top Global Matches:** file_cluster_8: 7.99, file_cluster_7: 8.379, file_cluster_13: 8.421
- **Magnitude:** 7.25 | **LOC:** 182 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.7504%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 31.2 | O(N^2))
    * *Intent:* /** * AudioResampler provides functionality to resample audio data from an input sample rate to * an...
  * `push` (Impact: 12.0 | O(N^2) | DB: 1)
  * `flush` (Impact: 10.0 | O(N^2))
  * `inputRate` (Impact: 3.6 | O(2^N))
  * `outputRate` (Impact: 3.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 16`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `doc: 11`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, audio_frame_pb.js, audio_frame.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/proto/participant_pb.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.715 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_16: 9.715, file_cluster_2: 9.766, file_cluster_8: 9.873
- **Magnitude:** 6.48 | **LOC:** 352 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.753%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fromBinary` (Impact: 7.1 | O(2^N))
    * *Intent:* /** * SIP callee rejected the call (busy) * * @generated from enum value: USER_REJECTED = 12;
  * `fromJson` (Impact: 7.1 | O(2^N))
    * *Intent:* /**
  * `fromJsonString` (Impact: 7.1 | O(2^N))
    * *Intent:* /** * SIP protocol failure or unexpected response * * @generated from enum value: SIP_TRUNK_FAILURE ...
  * `fromBinary` (Impact: 7.1 | O(2^N))
  * `fromJson` (Impact: 7.1 | O(2^N))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 29`, `args: 14`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `duplicate_logic: 10`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `doc: 41`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` handle_pb.js, protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/data_streams/stream_writer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.82 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 7.061 IQR)
- **Top Global Matches:** file_cluster_4: 14.82, file_cluster_13: 15.268, file_cluster_16: 15.324
- **Magnitude:** 5.86 | **LOC:** 36 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (99.995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `close` (Impact: 7.2 | O(2^N) | DB: 3)
  * `constructor` (Impact: 4.3 | O(N^1) | DB: 4)
  * `write` (Impact: 3.6 | O(2^N) | DB: 1)
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

### `package/src/ffi_client.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.802 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.344 IQR)
- **Top Global Matches:** file_cluster_13: 10.802, file_cluster_4: 10.982, file_cluster_16: 11.211
- **Magnitude:** 5.71 | **LOC:** 83 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (73.3479%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `waitFor` (Impact: 7.3 | O(N^2) | DB: 2)
  * `ffi_event` (Impact: 4.3 | O(2^N))
  * `instance` (Impact: 4.3 | O(N^1))
    * *Intent:* /** @internal */
  * `constructor` (Impact: 2.8 | O(N^2) | DB: 2)
  * `request` (Impact: 2.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 31`, `args: 12`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 9`, `concurrency: 13`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, protobuf, ffi_pb.js, native.js, typed-emitter, version.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.598 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.801 IQR)
- **Top Global Matches:** file_cluster_16: 11.598, file_cluster_8: 11.892, file_cluster_7: 12.165
- **Magnitude:** 5.21 | **LOC:** 43 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (40.7652%), Tech Debt (99.8629%)
**Top Internal Functions/Classes:**
  * `splitUtf8` (Impact: 22.0 | O(N^2) | DB: 4)
  * `bigIntToNumber` (Impact: 7.2 | O(N^1))
    * *Intent:* // SPDX-FileCopyrightText: 2024 LiveKit, Inc. // // SPDX-License-Identifier: Apache-2.0 /** convert ...
  * `numberToBigInt` (Impact: 7.2 | O(N^1))
    * *Intent:* /** convert numbers to bigints preserving undefined values */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 12`, `args: 5`, `func_start: 3`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 3`
* *Architecture:* `api: 3`
* *Defense:* `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_frame.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.747 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.815 IQR)
- **Top Global Matches:** file_cluster_13: 10.747, file_cluster_8: 10.979, file_cluster_16: 11.161
- **Magnitude:** 4.86 | **LOC:** 108 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.7904%), Tech Debt (39.0501%)
**Top Internal Functions/Classes:**
  * `combineAudioFrames` (Impact: 17.3 | O(N^1) | DB: 1)
    * *Intent:* /**
  * `fromOwnedInfo` (Impact: 2.6 | O(N^1))
    * *Intent:* /** @internal */
  * `create` (Impact: 2.2 | O(N^1))
  * `userdata` (Impact: 1.9 | O(N^1) | DB: 1)
    * *Intent:* /** Returns the user data associated with the audio frame. */
  * `protoInfo` (Impact: 1.8 | O(N^1) | DB: 4)
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

### `package/src/video_source.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.027 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.424 IQR)
- **Top Global Matches:** file_cluster_13: 11.027, file_cluster_4: 11.309, file_cluster_8: 11.46
- **Magnitude:** 4.41 | **LOC:** 77 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (32.8882%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 8.9 | O(N^2) | DB: 4)
  * `captureFrame` (Impact: 6.1 | O(N^1) | DB: 2)
  * `close` (Impact: 1.9 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`
* *Architecture:* `api: 4`, `concurrency: 6`, `import: 4`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` video_frame.js, video_frame_pb.js, ffi_client.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.561 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.46 IQR)
- **Top Global Matches:** file_cluster_13: 7.561, file_cluster_8: 7.886, file_cluster_7: 8.793
- **Magnitude:** 4.31 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`
* *Risk/State:* None
* *Architecture:* `api: 27`, `import: 27`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, e2ee_pb.js, audio_source.js, video_frame_pb.js, e2ee.js, track_pb.js, audio_stream.js, ffi_client.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/src/nodejs.rs` (RUST) | Magnitude: 68.28 | Delta: **0.427 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 26, safety: 19, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/room.ts` (TYPESCRIPT) | Magnitude: 236.58 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 736, state_mutation: 460, branch: 277, structural_boundaries: 142
- `package/src/audio_filter.ts` (TYPESCRIPT) | Magnitude: 1.23 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, import: 3, branch: 2
- `package/src/napi/native.cjs` (JAVASCRIPT) | Magnitude: 31.84 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 267, branch: 133, safety: 41, import: 39
- `package/src/ffi_client.ts` (TYPESCRIPT) | Magnitude: 5.71 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 31, concurrency: 13, args: 12
- `package/src/log.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.207 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, immutability_locks: 3, api: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/src/proto/rpc_pb.ts` (TYPESCRIPT) | Magnitude: 33.16 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 276, generics: 121, structural_boundaries: 91, args: 77
- `package/src/proto/track_publication_pb.ts` (TYPESCRIPT) | Magnitude: 18.18 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 140, generics: 66, structural_boundaries: 54, args: 42
- `package/src/rpc.ts` (TYPESCRIPT) | Magnitude: 3.2 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, doc: 14, structural_boundaries: 12, state_mutation: 12
- `package/src/proto/participant_pb.ts` (TYPESCRIPT) | Magnitude: 6.48 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 112, doc: 41, structural_boundaries: 29, generics: 22
- `package/src/proto/handle_pb.ts` (TYPESCRIPT) | Magnitude: 3.11 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, generics: 11, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/participant.ts` (TYPESCRIPT) | Magnitude: 102.37 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 661, concurrency: 179, branch: 164, structural_boundaries: 155
- `package/src/track_publication.ts` (TYPESCRIPT) | Magnitude: 17.29 | Delta: **0.195 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 47, structural_boundaries: 32, concurrency: 30
- `package/src/audio_source.ts` (TYPESCRIPT) | Magnitude: 16.22 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 68, concurrency: 43, structural_boundaries: 20
- `package/src/track.ts` (TYPESCRIPT) | Magnitude: 17.34 | Delta: **0.323 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, concurrency: 42, structural_boundaries: 41, state_mutation: 30
- `package/src/data_streams/stream_reader.ts` (TYPESCRIPT) | Magnitude: 24.17 | Delta: **0.324 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, state_mutation: 70, concurrency: 63, structural_boundaries: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/data_streams/types.ts` (TYPESCRIPT) | Magnitude: 2.48 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 22, branch: 10, api: 9
- `package/src/video_frame.ts` (TYPESCRIPT) | Magnitude: 18.32 | Delta: **0.214 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 199, state_mutation: 56, structural_boundaries: 43, branch: 36
- `package/src/e2ee.ts` (TYPESCRIPT) | Magnitude: 22.45 | Delta: **0.298 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 249, state_mutation: 73, branch: 28, structural_boundaries: 22
- `package/src/audio_resampler.ts` (TYPESCRIPT) | Magnitude: 7.25 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 113, encapsulation: 19, structural_boundaries: 16, branch: 13
- `package/src/napi/native.d.ts` (TYPESCRIPT) | Magnitude: 0.93 | Delta: **0.465 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 14, func_start: 9, args: 8, api: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/index.ts` -> **Severity: 2631.6** (Blast Radius: 26.316 * Doc Risk: 100.0%)
- `package/src/frame_processor.ts` -> **Severity: 2628.045** (Blast Radius: 26.316 * Doc Risk: 99.8649%)
- `package/src/data_streams/types.ts` -> **Severity: 2625.908** (Blast Radius: 26.316 * Doc Risk: 99.7837%)
- `package/src/audio_stream.ts` -> **Severity: 2558.649** (Blast Radius: 26.316 * Doc Risk: 97.2279%)
- `package/src/ffi_client.ts` -> **Severity: 2512.949** (Blast Radius: 26.316 * Doc Risk: 95.4913%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
