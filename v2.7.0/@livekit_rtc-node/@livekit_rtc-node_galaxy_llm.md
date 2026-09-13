# ARCHITECTURAL_BRIEF: @livekit_rtc-node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 38 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 4497 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.4% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 33 | 4092 | 86.8% |
| JAVASCRIPT | 2 | 296 | 5.3% |
| MARKDOWN | 1 | 0 | 2.6% |
| PLAINTEXT | 1 | 0 | 2.6% |
| RUST | 1 | 109 | 2.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 36 | 94.7% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 74.5 | 21.2 | 11.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.2 | 47.3 | 61.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 19.7 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 3.5 | 86.5 | 31.2 | 29.3 | 7.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 29.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 46.7 | 41.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 21.8 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 86.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 59.7 | 73.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 42 | 9 | 2 | `package/src/room.ts` |
| cleanup | 27 | 11 | 3 | `package/src/track.ts` |
| guards | 321 | 20 | 31 | `package/src/room.ts` |
| danger | 242 | 20 | 9 | `package/src/room.ts` |
| concurrency | 173 | 13 | 10 | `package/src/participant.ts` |
| connectivity | 267 | 36 | 15 | `package/src/index.ts` |
| io | 10 | 3 | 0 | `package/src/participant.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `package/src/napi/native.cjs` |
| time | 10 | 4 | 0 | `package/src/audio_source.ts` |
| serialization | 1 | 1 | 0 | `package/src/audio_stream.ts` |
| regex | 0 | 0 | 0 | - |
| events | 65 | 6 | 4 | `package/src/room.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 190 | 24 | 13 | `package/src/proto/participant_pb.ts` |
| debt | 19 | 6 | 2 | `package/src/participant.ts` |
| mutation | 863 | 30 | 40 | `package/src/napi/native.cjs` |
| dead_code | 18 | 3 | 0 | `package/src/nodejs.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 9 | 4 | 0 | `package/src/video_frame.ts` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1394**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/participant.ts` (Hits: 5)
- `package/src/napi/native.cjs` (Hits: 3)
- `package/src/audio_filter.ts` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **native.js** (`package/src/napi/native.js`) — 3 inbound connections
2. **native.cjs** (`package/src/napi/native.cjs`) — 1 inbound connections
3. **README.md** (`package/README.md`) — 0 inbound connections
4. **package.json** (`package/package.json`) — 0 inbound connections
5. **async_queue.ts** (`package/src/async_queue.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **native.cjs** (`package/src/napi/native.cjs`) — 39 outbound dependencies
2. **index.ts** (`package/src/index.ts`) — 25 outbound dependencies
3. **room.ts** (`package/src/room.ts`) — 18 outbound dependencies
4. **participant.ts** (`package/src/participant.ts`) — 15 outbound dependencies
5. **nodejs.rs** (`package/src/nodejs.rs`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `processFfiEvent` (@ `package/src/room.ts`) -> Impact: **212.9** | LOC: 298
- `streamBytes` (@ `package/src/participant.ts`) -> Impact: **41.7** | LOC: 99
- `handleStreamHeader` (@ `package/src/room.ts`) -> Impact: **41.6** | LOC: 70
- `constructor` (@ `package/src/audio_stream.ts`) -> Impact: **38.2** | LOC: 44
- `connect` (@ `package/src/room.ts`) -> Impact: **34.8** | LOC: 56
  * *Intent:* /** * Connects to a LiveKit room using the provided URL and access token. * @param url - The WebSocket URL of the LiveKit server * @param token - A va...
- `streamText` (@ `package/src/participant.ts`) -> Impact: **32.6** | LOC: 87
  * *Intent:* /** * Returns a `StreamWriter` instance that allows to write individual chunks of text to a stream. * Well suited for TTS and/or streaming LLM output....
- `handleRpcMethodInvocation` (@ `package/src/participant.ts`) -> Impact: **31.4** | LOC: 46
  * *Intent:* /** @internal */
- `editChatMessage` (@ `package/src/participant.ts`) -> Impact: **28.9** | LOC: 42
  * *Intent:* /** * @experimental */
- `getPlaneLength` (@ `package/src/video_frame.ts`) -> Impact: **27.3** | LOC: 26
- `getPlaneInfos` (@ `package/src/video_frame.ts`) -> Impact: **25.2** | LOC: 101

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src` | 25 | 2440.53 | 21.97% | 16.04% |
| `package/src/proto` | 4 | 355.3 | 4.64% | 0.0% |
| `package/src/napi` | 3 | 252.07 | 24.84% | 33.33% |
| `package/src/data_streams` | 4 | 166.92 | 29.89% | 0.0% |
| `package` | 2 | 4.64 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/napi/native.d.ts` -> **99.9994%** Exposure
- `package/src/track.ts` -> **99.9651%** Exposure
- `package/src/nodejs.rs` -> **99.8414%** Exposure
- `package/src/utils.ts` -> **98.2014%** Exposure
- `package/src/audio_frame.ts` -> **47.4338%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/audio_mixer.ts` -> **100.0%** Exposure
- `package/src/napi/native.cjs` -> **100.0%** Exposure
- `package/src/audio_source.ts` -> **99.9978%** Exposure
- `package/src/video_source.ts` -> **99.9411%** Exposure
- `package/src/async_queue.ts` -> **99.9254%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/napi/native.d.ts` -> **7** Orphaned Functions | **0** Duplicates
- `package/src/nodejs.rs` -> **6** Orphaned Functions | **0** Duplicates
- `package/src/participant.ts` -> **0** Orphaned Functions | **4** Duplicates
- `package/src/track.ts` -> **0** Orphaned Functions | **4** Duplicates
- `package/src/utils.ts` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `51` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/track.ts` (TYPESCRIPT) -> Cumulative Risk: **670.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 72.96 | **LOC:** 128 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9651%), Documentation (95.6522%), Concurrency (92.7764%)
- **Heaviest Functions:** `close` (Impact: 4.5), `close` (Impact: 4.5), `createAudioTrack` (Impact: 4.1)

### 2. `package/src/room.ts` (TYPESCRIPT) -> Cumulative Risk: **637.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 608.34 | **LOC:** 900 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.3131%), Safety Score (93.2505%), Verification (80.0%)
- **Heaviest Functions:** `processFfiEvent` (Impact: 212.9), `handleStreamHeader` (Impact: 41.6), `connect` (Impact: 34.8)

### 3. `package/src/audio_source.ts` (TYPESCRIPT) -> Cumulative Risk: **629.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 115.62 | **LOC:** 152 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9978%), Safety Score (90.8633%)
- **Heaviest Functions:** `captureFrame` (Impact: 14.7), `constructor` (Impact: 5.2), `clearQueue` (Impact: 2.8)

### 4. `package/src/audio_mixer.ts` (TYPESCRIPT) -> Cumulative Risk: **626.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 293.66 | **LOC:** 419 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Safety Score (90.457%)
- **Heaviest Functions:** `getContribution` (Impact: 25.1), `mixAudio` (Impact: 21.5), `mixer` (Impact: 20.4)

### 5. `package/src/participant.ts` (TYPESCRIPT) -> Cumulative Risk: **619.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 494.74 | **LOC:** 873 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.7609%), Verification (80.0%), Documentation (70.9091%)
- **Heaviest Functions:** `streamBytes` (Impact: 41.7), `streamText` (Impact: 32.6), `handleRpcMethodInvocation` (Impact: 31.4)

### 6. `package/src/video_source.ts` (TYPESCRIPT) -> Cumulative Risk: **610.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 40.72 | **LOC:** 77 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9411%), Concurrency (97.2917%)
- **Heaviest Functions:** `captureFrame` (Impact: 7.0), `constructor` (Impact: 6.3), `close` (Impact: 1.2)

### 7. `package/src/audio_stream.ts` (TYPESCRIPT) -> Cumulative Risk: **602.01**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 108.36 | **LOC:** 137 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9169%), Safety Score (82.3757%)
- **Heaviest Functions:** `constructor` (Impact: 38.2), `onEvent` (Impact: 18.6), `constructor` (Impact: 6.3)

### 8. `package/src/async_queue.ts` (TYPESCRIPT) -> Cumulative Risk: **587.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 42.86 | **LOC:** 81 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9254%), Concurrency (99.5792%), Safety Score (84.2905%)
- **Heaviest Functions:** `put` (Impact: 8.0), `waitForItem` (Impact: 3.3), `get` (Impact: 2.4)

### 9. `package/src/data_streams/stream_writer.ts` (TYPESCRIPT) -> Cumulative Risk: **583.34**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 28.56 | **LOC:** 36 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8887%), Concurrency (76.8525%)
- **Heaviest Functions:** `constructor` (Impact: 4.3), `close` (Impact: 2.2), `write` (Impact: 1.6)

### 10. `package/src/data_streams/stream_reader.ts` (TYPESCRIPT) -> Cumulative Risk: **577.9**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 122.56 | **LOC:** 159 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.8833%), Safety Score (82.2067%)
- **Heaviest Functions:** `handleChunkReceived` (Impact: 7.7), `handleChunkReceived` (Impact: 4.6), `[Symbol.asyncIterator]` (Impact: 4.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/room.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 608.34 | **LOC:** 900 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.6805%), Tech Debt (9.8818%)
**Top Internal Functions/Classes:**
  * `processFfiEvent` (Impact: 212.9)
  * `handleStreamHeader` (Impact: 41.6)
  * `connect` (Impact: 34.8)
    * *Intent:* /** * Connects to a LiveKit room using the provided URL and access token. * @param url - The WebSock...
  * `start` (Impact: 20.1)
  * `requireParticipantByIdentity` (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 191`, `args: 75`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 44`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 22`, `concurrency: 12`, `import: 23`
* *Defense:* `safety: 48`, `doc: 11`, `sync_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stream_reader.js, types.js, e2ee.js, ffi_client.js, log.js, participant.js, e2ee_pb.js, ffi_pb.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/participant.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 494.74 | **LOC:** 873 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.1246%), Tech Debt (45.7652%)
**Top Internal Functions/Classes:**
  * `streamBytes` (Impact: 41.7)
  * `streamText` (Impact: 32.6)
    * *Intent:* /** * Returns a `StreamWriter` instance that allows to write individual chunks of text to a stream. ...
  * `handleRpcMethodInvocation` (Impact: 31.4)
    * *Intent:* /** @internal */
  * `editChatMessage` (Impact: 28.9)
    * *Intent:* /** * @experimental */
  * `sendChatMessage` (Impact: 23.7)
    * *Intent:* /** * Sends a chat message to participants in the room * * @param text - The text content of the cha...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 156`, `args: 54`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 17`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 22`, `concurrency: 64`, `import: 17`
* *Defense:* `safety: 40`, `doc: 13`, `sync_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, ffi_client.js, log.js, participant_pb.js, room_pb.js, rpc_pb.js, rpc.js, track.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_mixer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 293.66 | **LOC:** 419 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getContribution` (Impact: 25.1)
  * `mixAudio` (Impact: 21.5)
  * `mixer` (Impact: 20.4)
  * `constructor` (Impact: 14.8)
    * *Intent:* /** * Initialize the AudioMixer. * * @param sampleRate - The audio sample rate in Hz. * @param numCh...
  * `getNextFrame` (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 56`, `args: 23`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `api: 7`, `concurrency: 29`, `import: 4`
* *Defense:* `safety: 11`, `doc: 10`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` async_queue.js, audio_frame.js, log.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/napi/native.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 235.44 | **LOC:** 302 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5199%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isMusl` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 71 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 24`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 77`
* *Architecture:* `io: 3`, `api: 6`, `import: 39`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 92.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.061776
  * `Imports (Out-Degree: 0):` rtc-node.android-arm-eabi.node, rtc-node.android-arm64.node, rtc-node.darwin-arm64.node, rtc-node.darwin-universal.node, rtc-node.darwin-x64.node, rtc-node.freebsd-x64.node, rtc-node.linux-arm-gnueabihf.node, rtc-node.linux-arm-musleabihf.node...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/proto/rpc_pb.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 189.7 | **LOC:** 540 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.7533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fromBinary` (Impact: 3.6)
  * `fromJson` (Impact: 3.6)
  * `fromJsonString` (Impact: 3.6)
  * `fromBinary` (Impact: 3.6)
  * `fromJson` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 91`, `args: 66`, `func_start: 55`, `class_start: 11`
* *Risk/State:* None
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 39`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/data_streams/stream_reader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 122.56 | **LOC:** 159 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.5766%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleChunkReceived` (Impact: 7.7)
  * `handleChunkReceived` (Impact: 4.6)
  * `[Symbol.asyncIterator]` (Impact: 4.5)
    * *Intent:* /** * Async iterator implementation to allow usage of `for await...of` syntax. * Yields structured c...
  * `constructor` (Impact: 4.4)
    * *Intent:* /** * A TextStreamReader instance can be used as an AsyncIterator that returns the entire string * t...
  * `constructor` (Impact: 4.3)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` log.js, room_pb.js, utils.js, types.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/e2ee.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 117.32 | **LOC:** 316 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.8626%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 7.4)
  * `exportKey` (Impact: 6.2)
  * `ratchetKey` (Impact: 6.2)
  * `setSharedKey` (Impact: 6.1)
  * `setKey` (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 22`, `args: 14`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, e2ee_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_source.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 115.62 | **LOC:** 152 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `captureFrame` (Impact: 14.7)
  * `constructor` (Impact: 5.2)
  * `clearQueue` (Impact: 2.8)
  * `release` (Impact: 2.5)
    * *Intent:* /** @internal */
  * `waitForPlayout` (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 21`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 20`
* *Architecture:* `api: 7`, `concurrency: 8`, `import: 5`
* *Defense:* `safety: 1`, `doc: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` audio_frame.js, ffi_client.js, native.js, audio_frame_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_stream.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 108.36 | **LOC:** 137 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.7893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 38.2)
  * `onEvent` (Impact: 18.6)
  * `constructor` (Impact: 6.3)
  * `constructor` (Impact: 2.0)
  * `constructor` (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 28`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 7`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_frame.js, ffi_client.js, frame_processor.js, log.js, audio_frame_pb.js, track.js, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/video_frame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 108.2 | **LOC:** 232 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.7672%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPlaneLength` (Impact: 27.3)
  * `getPlaneInfos` (Impact: 25.2)
  * `convert` (Impact: 13.2)
  * `protoInfo` (Impact: 9.3)
    * *Intent:* /** @internal */
  * `getPlane` (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 46`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 8`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, video_frame_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/proto/track_publication_pb.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 104.36 | **LOC:** 285 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fromBinary` (Impact: 3.6)
  * `fromJson` (Impact: 3.6)
  * `fromJsonString` (Impact: 3.6)
  * `fromBinary` (Impact: 3.6)
  * `fromJson` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 54`, `args: 36`, `func_start: 30`, `class_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `doc: 17`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/track.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 72.96 | **LOC:** 128 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.0545%), Tech Debt (99.9651%)
**Top Internal Functions/Classes:**
  * `close` (Impact: 4.5)
  * `close` (Impact: 4.5)
  * `createAudioTrack` (Impact: 4.1)
  * `createVideoTrack` (Impact: 4.1)
  * `constructor` (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 41`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `concurrency: 7`, `import: 5`
* *Defense:* `safety: 7`, `doc: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_source.js, ffi_client.js, track_pb.js, video_source.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/track_publication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 67.3 | **LOC:** 113 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.0023%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setSubscribed` (Impact: 3.3)
  * `resolveFirstSubscription` (Impact: 2.3)
    * *Intent:* /** @internal */
  * `sid` (Impact: 2.1)
  * `name` (Impact: 2.1)
  * `kind` (Impact: 2.1)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ffi_client.js, native.js, e2ee_pb.js, room_pb.js, track_pb.js, track.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 43.06 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 43`
* *Risk/State:* None
* *Architecture:* `api: 27`, `import: 27`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_filter.js, audio_frame.js, audio_mixer.js, audio_resampler.js, audio_source.js, audio_stream.js, index.js, e2ee.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/async_queue.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 42.86 | **LOC:** 81 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.68%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `put` (Impact: 8.0)
  * `waitForItem` (Impact: 3.3)
    * *Intent:* /** * Wait until an item is available or the queue is closed. * Returns immediately if items are alr...
  * `get` (Impact: 2.4)
  * `close` (Impact: 1.6)
  * `constructor` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 21`, `args: 13`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `api: 5`, `concurrency: 7`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deque
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_resampler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 41.06 | **LOC:** 182 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 17.5)
    * *Intent:* #inputRate: number; #outputRate: number; #channels: number; #ffiHandle: FfiHandle; /** * Initializes...
  * `push` (Impact: 7.3)
    * *Intent:* /** * Push audio data into the resampler and retrieve any available resampled data. * * This method ...
  * `flush` (Impact: 5.5)
    * *Intent:* /** * Flush any remaining audio data through the resampler and retrieve the resampled data. * * @rem...
  * `inputRate` (Impact: 1.1)
  * `outputRate` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio_frame.js, ffi_client.js, audio_frame_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 40.76 | **LOC:** 43 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.2022%), Tech Debt (98.2014%)
**Top Internal Functions/Classes:**
  * `splitUtf8` (Impact: 13.3)
  * `bigIntToNumber` (Impact: 5.9)
    * *Intent:* // SPDX-FileCopyrightText: 2024 LiveKit, Inc. // // SPDX-License-Identifier: Apache-2.0 /** convert ...
  * `numberToBigInt` (Impact: 5.9)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/video_source.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 40.72 | **LOC:** 77 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.3386%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `captureFrame` (Impact: 7.0)
  * `constructor` (Impact: 6.3)
  * `close` (Impact: 1.2)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, video_frame_pb.js, video_frame.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/proto/participant_pb.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 39.02 | **LOC:** 352 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.753%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fromBinary` (Impact: 3.6)
  * `fromJson` (Impact: 3.6)
  * `fromJsonString` (Impact: 3.6)
  * `fromBinary` (Impact: 3.6)
  * `fromJson` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 29`, `args: 12`, `func_start: 10`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `doc: 41`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` handle_pb.js, protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/audio_frame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 38.16 | **LOC:** 108 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.4103%), Tech Debt (47.4338%)
**Top Internal Functions/Classes:**
  * `combineAudioFrames` (Impact: 9.9)
    * *Intent:* /** * Combines one or more `rtc.AudioFrame` objects into a single `rtc.AudioFrame`. * * This functio...
  * `constructor` (Impact: 3.1)
    * *Intent:* // note: if converting from Uint8Array to Int16Array, *do not* use buffer.slice! // it is marked uns...
  * `create` (Impact: 2.2)
  * `fromOwnedInfo` (Impact: 2.0)
    * *Intent:* /** @internal */
  * `protoInfo` (Impact: 1.4)
    * *Intent:* /** @internal */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 17`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 7`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 1`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, audio_frame_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/nodejs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 37.88 | **LOC:** 135 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.8669%), Tech Debt (99.8414%)
**Top Internal Functions/Classes:**
  * `livekit_ffi_request` (Impact: 5.5)
  * `livekit_initialize` (Impact: 5.2)
  * `dispose` (Impact: 4.9)
  * `livekit_copy_buffer` (Impact: 2.0)
  * `finalize` (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 26`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FFI_SERVER, JsFunction, Status, ThreadSafeCallContext, ThreadsafeFunction, ThreadsafeFunctionCallMode, livekit_ffi::proto, napi::
    bindgen_prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/ffi_client.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34.12 | **LOC:** 83 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.3873%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `waitFor` (Impact: 3.4)
  * `listener` (Impact: 3.3)
  * `instance` (Impact: 2.3)
    * *Intent:* /** @internal */
  * `copyBuffer` (Impact: 1.9)
  * `request` (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 32`, `args: 11`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 11`, `concurrency: 3`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` native.js, ffi_pb.js, version.js, protobuf, typed-emitter, events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/video_stream.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 31.74 | **LOC:** 87 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4899%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onEvent` (Impact: 14.3)
  * `constructor` (Impact: 3.6)
  * `start` (Impact: 1.6)
  * `constructor` (Impact: 1.6)
  * `cancel` (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ffi_client.js, video_frame_pb.js, track.js, video_frame.js, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/data_streams/stream_writer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.56 | **LOC:** 36 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.0036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 4.3)
  * `close` (Impact: 2.2)
  * `write` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 17`, `args: 4`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/rpc.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.1 | **LOC:** 122 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.8753%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 4.3)
    * *Intent:* /** * Creates an error object with the given code and message, plus an optional data payload. * * If...
  * `builtIn` (Impact: 3.6)
    * *Intent:* /** * Creates an error object from the code, with an auto-populated message. * * @internal */
  * `fromProto` (Impact: 1.6)
  * `toProto` (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 4`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `doc: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rpc_pb.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/napi/native.cjs` -> **Severity: 5.822** (Embedded: 0.0618 * Error Risk: 94.2394%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/napi/native.cjs` -> **Severity: 9221.1** (Blast Radius: 92.211 * Doc Risk: 100.0%)
- `package/src/audio_filter.ts` -> **Severity: 2295.3** (Blast Radius: 22.953 * Doc Risk: 100.0%)
- `package/src/audio_stream.ts` -> **Severity: 2295.3** (Blast Radius: 22.953 * Doc Risk: 100.0%)
- `package/src/data_streams/stream_writer.ts` -> **Severity: 2295.3** (Blast Radius: 22.953 * Doc Risk: 100.0%)
- `package/src/napi/native.d.ts` -> **Severity: 2295.3** (Blast Radius: 22.953 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
