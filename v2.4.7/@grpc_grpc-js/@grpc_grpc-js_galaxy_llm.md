# ARCHITECTURAL_BRIEF: @grpc_grpc-js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@grpc_grpc-js` |
| **Timestamp** | `2026-08-07T05:11:06.316053+00:00` |
| **Scan Duration** | `0.4s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 69 malicious artifacts.

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
| Total Artifacts | 74 |
| Analyzed Artifacts (Scanned) | 70 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 14874 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2508 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2584 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 45.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.021 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 66 | 14720 | 94.3% |
| PROTO | 3 | 154 | 4.3% |
| PLAINTEXT | 1 | 0 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.134`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 33 | 47.1% |
| file_cluster_8 | 26 | 37.1% |
| file_cluster_4 | 7 | 10.0% |
| file_cluster_16 | 2 | 2.9% |
| file_cluster_2 | 1 | 1.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 85 LOC)
- `.ts`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 39.6 | 41.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 61.5 | 71.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 49.2 | 58.2 | 0.0 |
| Testing Exposure | 0.3 | 80.0 | 41.7 | 80.0 | 80.0 |
| API Exposure | 0.0 | 13.4 | 5.4 | 4.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 63.2 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 8.0 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 94.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 99.9 | 33.1 | 22.0 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/server.ts` (Hits: 18)
- `package/src/http_proxy.ts` (Hits: 12)
- `package/src/server-call.ts` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **constants.ts** (`package/src/constants.ts`) — 37 inbound connections
2. **call-interface.ts** (`package/src/call-interface.ts`) — 32 inbound connections
3. **metadata.ts** (`package/src/metadata.ts`) — 26 inbound connections
4. **channel-options.ts** (`package/src/channel-options.ts`) — 25 inbound connections
5. **logging.ts** (`package/src/logging.ts`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **channelz.ts** (`package/src/channelz.ts`) — 38 outbound dependencies
2. **index.ts** (`package/src/index.ts`) — 32 outbound dependencies
3. **internal-channel.ts** (`package/src/internal-channel.ts`) — 27 outbound dependencies
4. **experimental.ts** (`package/src/experimental.ts`) — 20 outbound dependencies
5. **server.ts** (`package/src/server.ts`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `constructor` (@ `package/src/server.ts`) -> Impact: **292.6** | LOC: 863
- `destroy` (@ `package/src/server.ts`) -> Impact: **249.1** | LOC: 910
  * *Intent:* /** * If there is a pending bindAsync operation, this is a promise that resolves * with the port number when that operation succeeds. If there is no s...
- `shutdown` (@ `package/src/transport.ts`) -> Impact: **134.3** | LOC: 509
- `onReceiveStatus` (@ `package/src/load-balancing-call.ts`) -> Impact: **115.5** | LOC: 335
- `constructor` (@ `package/src/internal-channel.ts`) -> Impact: **98.9** | LOC: 218
  * *Intent:* /** * This timer does not do anything on its own. Its purpose is to hold the * event loop open while there are any pending calls for the channel that ...
- `_sessionHandler` (@ `package/src/server.ts`) -> Impact: **93.8** | LOC: 179
- `createSession` (@ `package/src/transport.ts`) -> Impact: **66.8** | LOC: 97
- `shutdown` (@ `package/src/transport.ts`) -> Impact: **65.2** | LOC: 172
- `getAuthContext` (@ `package/src/client-interceptors.ts`) -> Impact: **62.9** | LOC: 127
- `validateMethodConfig` (@ `package/src/service-config.ts`) -> Impact: **57.5** | LOC: 71

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src` | 66 | 1730.12 | 40.96% | 51.42% |
| `package/proto` | 1 | 17.4 | 0.0% | 0.0% |
| `package/proto/xds/xds/data/orca/v3` | 1 | 15.38 | 13.73% | 0.0% |
| `package/proto/xds/xds/service/orca/v3` | 1 | 15.3 | 17.48% | 0.0% |
| `package` | 1 | 1.8 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/call-credentials.ts` -> **100.0%** Exposure
- `package/src/call.ts` -> **100.0%** Exposure
- `package/src/channel-credentials.ts` -> **100.0%** Exposure
- `package/src/client-interceptors.ts` -> **100.0%** Exposure
- `package/src/compression-filter.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/call-interface.ts` -> **100.0%** Exposure
- `package/src/certificate-provider.ts` -> **100.0%** Exposure
- `package/src/filter-stack.ts` -> **100.0%** Exposure
- `package/src/internal-channel.ts` -> **100.0%** Exposure
- `package/src/load-balancer-child-handler.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/server-interceptors.ts` -> **0** Orphaned Functions | **52** Duplicates
- `package/src/server-call.ts` -> **0** Orphaned Functions | **47** Duplicates
- `package/src/server.ts` -> **0** Orphaned Functions | **45** Duplicates
- `package/src/channel-credentials.ts` -> **0** Orphaned Functions | **41** Duplicates
- `package/src/client-interceptors.ts` -> **0** Orphaned Functions | **40** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/service-config.ts`** -> AI Confidence: **99.32%**
2. **`package/src/channel-credentials.ts`** -> AI Confidence: **99.31%**
3. **`package/src/client.ts`** -> AI Confidence: **99.31%**
4. **`package/src/internal-channel.ts`** -> AI Confidence: **99.31%**
5. **`package/src/load-balancer-child-handler.ts`** -> AI Confidence: **99.31%**
6. **`package/src/load-balancer-outlier-detection.ts`** -> AI Confidence: **99.31%**
7. **`package/src/load-balancer-weighted-round-robin.ts`** -> AI Confidence: **99.31%**
8. **`package/src/load-balancing-call.ts`** -> AI Confidence: **99.31%**
9. **`package/src/resolver-dns.ts`** -> AI Confidence: **99.31%**
10. **`package/src/resolving-call.ts`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `43` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/certificate-provider.ts` (TYPESCRIPT) -> Cumulative Risk: **768.14**
- **Archetype:** `file_cluster_4` (Distance: 14.037 IQR)
- **Magnitude:** 26.32 | **LOC:** 177 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9998%), Tech Debt (99.0935%)
- **Heaviest Functions:** `updateCertificates` (Impact: 24.5), `constructor` (Impact: 10.3), `maybeStartWatchingFiles` (Impact: 9.5)

### 2. `package/src/transport.ts` (TYPESCRIPT) -> Cumulative Risk: **725.12**
- **Archetype:** `file_cluster_13` (Distance: 14.011 IQR)
- **Magnitude:** 110.72 | **LOC:** 826 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.8725%), Tech Debt (99.4252%)
- **Heaviest Functions:** `shutdown` (Impact: 134.3), `createSession` (Impact: 66.8), `shutdown` (Impact: 65.2)

### 3. `package/src/resolver-dns.ts` (TYPESCRIPT) -> Cumulative Risk: **722.75**
- **Archetype:** `file_cluster_4` (Distance: 13.514 IQR)
- **Magnitude:** 55.9 | **LOC:** 450 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.973%), Tech Debt (98.0358%)
- **Heaviest Functions:** `startResolution` (Impact: 54.6), `constructor` (Impact: 37.2), `lookup` (Impact: 15.0)

### 4. `package/src/single-subchannel-channel.ts` (TYPESCRIPT) -> Cumulative Risk: **702.98**
- **Archetype:** `file_cluster_4` (Distance: 13.802 IQR)
- **Magnitude:** 43.62 | **LOC:** 249 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.7293%)
- **Heaviest Functions:** `start` (Impact: 25.9), `constructor` (Impact: 20.7), `sendMessageWithContext` (Impact: 7.6)

### 5. `package/src/compression-filter.ts` (TYPESCRIPT) -> Cumulative Risk: **696.6**
- **Archetype:** `file_cluster_4` (Distance: 12.282 IQR)
- **Magnitude:** 41.56 | **LOC:** 359 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.99%)
- **Heaviest Functions:** `constructor` (Impact: 22.6), `super` (Impact: 18.5), `sendMessage` (Impact: 15.2)

### 6. `package/src/filter-stack.ts` (TYPESCRIPT) -> Cumulative Risk: **690.36**
- **Archetype:** `file_cluster_4` (Distance: 13.622 IQR)
- **Magnitude:** 16.1 | **LOC:** 101 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `sendMetadata` (Impact: 3.9), `receiveMetadata` (Impact: 3.9), `sendMessage` (Impact: 3.9)

### 7. `package/src/orca.ts` (TYPESCRIPT) -> Cumulative Risk: **688.44**
- **Archetype:** `file_cluster_13` (Distance: 13.268 IQR)
- **Magnitude:** 31.38 | **LOC:** 350 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.9108%), Tech Debt (92.6921%)
- **Heaviest Functions:** `updateMetricsSubscription` (Impact: 17.0), `createMetricsReader` (Impact: 9.6), `removeDataWatcher` (Impact: 7.5)

### 8. `package/src/server.ts` (TYPESCRIPT) -> Cumulative Risk: **687.9**
- **Archetype:** `file_cluster_13` (Distance: 13.309 IQR)
- **Magnitude:** 162.52 | **LOC:** 2213 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9991%), Safety Score (87.4578%)
- **Heaviest Functions:** `constructor` (Impact: 292.6), `destroy` (Impact: 249.1), `_sessionHandler` (Impact: 93.8)

### 9. `package/src/load-balancing-call.ts` (TYPESCRIPT) -> Cumulative Risk: **681.31**
- **Archetype:** `file_cluster_13` (Distance: 13.351 IQR)
- **Magnitude:** 54.34 | **LOC:** 388 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.2937%), Cognitive Load (93.2883%)
- **Heaviest Functions:** `onReceiveStatus` (Impact: 115.5), `doPick` (Impact: 52.0), `constructor` (Impact: 15.1)

### 10. `package/src/server-interceptors.ts` (TYPESCRIPT) -> Cumulative Risk: **675.76**
- **Archetype:** `file_cluster_13` (Distance: 14.154 IQR)
- **Magnitude:** 122.04 | **LOC:** 1072 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (95.7525%)
- **Heaviest Functions:** `getMetricsRecorder` (Impact: 54.0), `constructor` (Impact: 46.4), `trace` (Impact: 30.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/server.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.309 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.2 IQR)
- **Top Global Matches:** file_cluster_13: 13.309, file_cluster_11: 13.434, file_cluster_4: 13.492
- **Magnitude:** 162.52 | **LOC:** 2213 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.6579%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 292.6)
  * `destroy` (Impact: 249.1)
    * *Intent:* /** * If there is a pending bindAsync operation, this is a promise that resolves * with the port num...
  * `_sessionHandler` (Impact: 93.8)
  * `_channelzHandler` (Impact: 32.1)
  * `handleUnary` (Impact: 28.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 119`, `args: 107`, `func_start: 88`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 367`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 45`
* *Architecture:* `io: 18`, `api: 16`, `concurrency: 38`, `import: 20`
* *Defense:* `safety: 57`, `doc: 20`, `immutability_locks: 49`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.244
  * `Choke Point (Betweenness):` 0.029039 | `Ripple Effect (Closeness):` 0.176539
  * `Imports (Out-Degree: 14):` channelz, util, net, call, logging, call-interface, channel-options, server-credentials...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/server-interceptors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.154 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.279 IQR)
- **Top Global Matches:** file_cluster_13: 14.154, file_cluster_8: 14.259, file_cluster_11: 14.28
- **Magnitude:** 122.04 | **LOC:** 1072 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.7026%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getMetricsRecorder` (Impact: 54.0)
  * `constructor` (Impact: 46.4)
    * *Intent:* // TODO(cjihrig): Remove these encoding headers from the default response // once compression is int...
  * `trace` (Impact: 30.0)
  * `sendStatus` (Impact: 28.9)
  * `constructor` (Impact: 24.8)
    * *Intent:* /** * End the call by sending this status. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 174`, `args: 125`, `func_start: 98`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 587`, `planned_debt: 1`, `duplicate_logic: 52`
* *Architecture:* `io: 9`, `api: 32`, `concurrency: 21`, `import: 16`
* *Defense:* `safety: 88`, `doc: 19`, `immutability_locks: 46`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.336
  * `Choke Point (Betweenness):` 0.025314 | `Ripple Effect (Closeness):` 0.217521
  * `Imports (Out-Degree: 12):` logging, zlib, tls, constants, error, server-call, metadata, call-interface...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/retrying-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.826 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.876 IQR)
- **Top Global Matches:** file_cluster_8: 13.826, file_cluster_13: 13.876, file_cluster_17: 14.006
- **Magnitude:** 119.18 | **LOC:** 924 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.4332%), Tech Debt (87.2048%)
**Top Internal Functions/Classes:**
  * `handleProcessedStatus` (Impact: 51.3)
  * `constructor` (Impact: 33.6)
    * *Intent:* /** * Entry in the buffer of messages to send to the remote end.
  * `handleChildStatus` (Impact: 32.3)
  * `callback` (Impact: 27.8)
  * `sendNextChildMessage` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 79`, `args: 61`, `func_start: 57`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 678`, `duplicate_logic: 14`
* *Architecture:* `api: 7`, `concurrency: 18`, `import: 10`
* *Defense:* `safety: 33`, `doc: 9`, `immutability_locks: 52`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.948
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.128901
  * `Imports (Out-Degree: 10):` logging, internal-channel, constants, load-balancing-call, call-credentials, metadata, resolver, call-interface...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/transport.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.011 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.262 IQR)
- **Top Global Matches:** file_cluster_13: 14.011, file_cluster_4: 14.04, file_cluster_11: 14.222
- **Magnitude:** 110.72 | **LOC:** 826 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.1206%), Tech Debt (99.4252%)
**Top Internal Functions/Classes:**
  * `shutdown` (Impact: 134.3)
  * `createSession` (Impact: 66.8)
  * `shutdown` (Impact: 65.2)
  * `constructor` (Impact: 50.7)
    * *Intent:* /** * Indicates that the keepalive timer ran out while there were no active
  * `createCall` (Impact: 41.3)
    * *Intent:* /** * Starts the keepalive ping timer if appropriate. If the timer already ran * out while there wer...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 87`, `args: 82`, `func_start: 65`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 420`, `duplicate_logic: 21`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 77`, `import: 19`
* *Defense:* `safety: 53`, `doc: 12`, `immutability_locks: 35`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.894
  * `Choke Point (Betweenness):` 0.033367 | `Ripple Effect (Closeness):` 0.203019
  * `Imports (Out-Degree: 13):` subchannel-call, logging, package.json, tls, constants, call-number, metadata, call-interface...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/src/internal-channel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.535 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.106 IQR)
- **Top Global Matches:** file_cluster_13: 13.535, file_cluster_8: 13.647, file_cluster_11: 13.86
- **Magnitude:** 94.15 | **LOC:** 879 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.9244%), Tech Debt (75.8117%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 98.9)
    * *Intent:* /** * This timer does not do anything on its own. Its purpose is to hold the * event loop open while...
  * `callback` (Impact: 15.6)
  * `createResolvingCall` (Impact: 14.1)
  * `updateState` (Impact: 13.8)
  * `createCall` (Impact: 13.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 85`, `args: 64`, `func_start: 55`, `class_start: 8`
* *Risk/State:* `state_mutation: 546`, `duplicate_logic: 11`
* *Architecture:* `api: 10`, `concurrency: 18`, `import: 27`
* *Defense:* `safety: 24`, `doc: 7`, `immutability_locks: 56`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.252
  * `Choke Point (Betweenness):` 0.125404 | `Ripple Effect (Closeness):` 0.163505
  * `Imports (Out-Degree: 26):` retrying-call, channelz, channel-credentials, logging, control-plane-status, call-number, call-credentials, call-interface...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-outlier-detection.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.34 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.689 IQR)
- **Top Global Matches:** file_cluster_8: 12.34, file_cluster_13: 12.495, file_cluster_11: 12.767
- **Magnitude:** 87.6 | **LOC:** 841 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.1514%), Tech Debt (99.9146%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 35.3)
  * `runSuccessRateCheck` (Impact: 34.8)
  * `createFromJson` (Impact: 34.5)
  * `updateAddressList` (Impact: 29.7)
  * `runFailurePercentageCheck` (Impact: 29.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 74`, `args: 89`, `func_start: 88`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 270`, `duplicate_logic: 29`
* *Architecture:* `api: 9`, `concurrency: 12`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 70`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.125
  * `Choke Point (Betweenness):` 0.000667 | `Ripple Effect (Closeness):` 0.028986
  * `Imports (Out-Degree: 13):` service-config, logging, constants, connectivity-state, call-interface, picker, load-balancer, channel-options...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/channel-credentials.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.388 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.401 IQR)
- **Top Global Matches:** file_cluster_4: 13.388, file_cluster_13: 13.485, file_cluster_8: 13.706
- **Magnitude:** 60.23 | **LOC:** 524 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7262%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `createSsl` (Impact: 43.8)
  * `destroy` (Impact: 35.5)
  * `getConnectionOptions` (Impact: 31.2)
  * `connect` (Impact: 15.7)
  * `getLatestSecureContext` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 93`, `args: 83`, `func_start: 76`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 155`, `duplicate_logic: 41`
* *Architecture:* `api: 10`, `concurrency: 66`, `import: 10`
* *Defense:* `safety: 33`, `doc: 21`, `immutability_locks: 20`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.281
  * `Choke Point (Betweenness):` 0.025039 | `Ripple Effect (Closeness):` 0.241211
  * `Imports (Out-Degree: 8):` logging, tls, constants, call-credentials, resolver, uri-parser, certificate-provider, tls-helpers...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `package/src/resolver-dns.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.514 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_4: 13.514, file_cluster_13: 13.571, file_cluster_17: 13.788
- **Magnitude:** 55.9 | **LOC:** 450 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.411%), Tech Debt (98.0358%)
**Top Internal Functions/Classes:**
  * `startResolution` (Impact: 54.6)
  * `constructor` (Impact: 37.2)
  * `lookup` (Impact: 15.0)
    * *Intent:* /* If TXT lookup fails we should do nothing, which means that we * continue to use the result of the...
  * `trace` (Impact: 13.4)
  * `updateResolution` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 51`, `args: 46`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 281`, `duplicate_logic: 10`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 53`, `import: 14`
* *Defense:* `safety: 17`, `doc: 10`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.885
  * `Choke Point (Betweenness):` 0.018211 | `Ripple Effect (Closeness):` 0.141641
  * `Imports (Out-Degree: 10):` service-config, logging, constants, metadata, call-interface, resolver, uri-parser, environment...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/resolving-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.763 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.369 IQR)
- **Top Global Matches:** file_cluster_13: 13.763, file_cluster_4: 13.819, file_cluster_8: 13.826
- **Magnitude:** 55.81 | **LOC:** 380 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.3681%), Tech Debt (26.3198%)
**Top Internal Functions/Classes:**
  * `getConfig` (Impact: 31.0)
  * `runDeadlineTimer` (Impact: 26.3)
  * `clearTimeout` (Impact: 21.7)
  * `handleDeadline` (Impact: 20.4)
  * `constructor` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 41`, `args: 34`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 338`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `concurrency: 19`, `import: 10`
* *Defense:* `safety: 16`, `doc: 1`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.948
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.128901
  * `Imports (Out-Degree: 10):` logging, internal-channel, constants, control-plane-status, call-credentials, metadata, call-interface, auth-context...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/load-balancing-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.351 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.513 IQR)
- **Top Global Matches:** file_cluster_13: 13.351, file_cluster_8: 13.518, file_cluster_4: 13.597
- **Magnitude:** 54.34 | **LOC:** 388 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.2883%), Tech Debt (58.2455%)
**Top Internal Functions/Classes:**
  * `onReceiveStatus` (Impact: 115.5)
  * `doPick` (Impact: 52.0)
  * `constructor` (Impact: 15.1)
  * `getDeadlineInfo` (Impact: 13.7)
  * `outputStatus` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 44`, `args: 23`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 257`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 22`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.538
  * `Choke Point (Betweenness):` 0.002394 | `Ripple Effect (Closeness):` 0.129587
  * `Imports (Out-Degree: 14):` subchannel-call, logging, internal-channel, constants, control-plane-status, call-credentials, connectivity-state, metadata...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/client-interceptors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.603 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.001 IQR)
- **Top Global Matches:** file_cluster_13: 13.603, file_cluster_11: 13.709, file_cluster_17: 13.725
- **Magnitude:** 52.99 | **LOC:** 586 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.0724%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getAuthContext` (Impact: 62.9)
  * `start` (Impact: 40.1)
    * *Intent:* /** * Indicates that a status was received but could not be propagated because * a message was still...
  * `start` (Impact: 25.9)
  * `start` (Impact: 23.5)
  * `constructor` (Impact: 21.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 104`, `args: 86`, `func_start: 70`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 141`, `duplicate_logic: 40`
* *Architecture:* `io: 3`, `api: 25`, `import: 8`
* *Defense:* `safety: 65`, `doc: 25`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.479
  * `Choke Point (Betweenness):` 0.010119 | `Ripple Effect (Closeness):` 0.139213
  * `Imports (Out-Degree: 8):` constants, error, channel, metadata, call-interface, auth-context, make-client, client
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-weighted-round-robin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.752 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.217 IQR)
- **Top Global Matches:** file_cluster_13: 12.752, file_cluster_8: 12.83, file_cluster_17: 13.062
- **Magnitude:** 43.82 | **LOC:** 495 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.4727%), Tech Debt (88.6682%)
**Top Internal Functions/Classes:**
  * `calculateAndUpdateState` (Impact: 36.1)
  * `constructor` (Impact: 35.1)
  * `parseDurationField` (Impact: 20.1)
  * `updateWeight` (Impact: 16.4)
  * `trace` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 61`, `args: 43`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 194`, `duplicate_logic: 7`
* *Architecture:* `api: 9`, `concurrency: 6`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 36`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.8
  * `Choke Point (Betweenness):` 0.000375 | `Ripple Effect (Closeness):` 0.014493
  * `Imports (Out-Degree: 11):` logging, OrcaLoadReport, constants, connectivity-state, call-interface, orca, load-balancer, channel-options...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/single-subchannel-channel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.802 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.605 IQR)
- **Top Global Matches:** file_cluster_4: 13.802, file_cluster_13: 14.117, file_cluster_8: 14.454
- **Magnitude:** 43.62 | **LOC:** 249 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.7293%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 25.9)
  * `constructor` (Impact: 20.7)
  * `sendMessageWithContext` (Impact: 7.6)
  * `halfClose` (Impact: 6.0)
  * `cancelWithStatus` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 46`, `args: 23`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 211`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 96`, `import: 18`
* *Defense:* `safety: 15`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.31
  * `Choke Point (Betweenness):` 0.006377 | `Ripple Effect (Closeness):` 0.105465
  * `Imports (Out-Degree: 17):` subchannel-call, subchannel, constants, control-plane-status, call-number, channel, call-credentials, connectivity-state...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/channelz.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.045 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.454 IQR)
- **Top Global Matches:** file_cluster_13: 11.045, file_cluster_8: 11.186, file_cluster_16: 11.429
- **Magnitude:** 43.16 | **LOC:** 910 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4893%), Tech Debt (99.9899%)
**Top Internal Functions/Classes:**
  * `GetSocket` (Impact: 36.4)
  * `connectivityStateToMessage` (Impact: 21.1)
  * `ipAddressStringToBuffer` (Impact: 19.4)
  * `addTrace` (Impact: 14.9)
  * `subchannelAddressToAddressMessage` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 171`, `args: 73`, `func_start: 65`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 70`, `duplicate_logic: 36`
* *Architecture:* `io: 1`, `api: 33`, `import: 39`
* *Defense:* `safety: 22`, `doc: 14`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.612
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` GetServerSocketsResponse, GetServerResponse, GetSubchannelResponse, Socket, channelz, Server, net, Timestamp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/compression-filter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.282 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.994 IQR)
- **Top Global Matches:** file_cluster_4: 12.282, file_cluster_13: 12.561, file_cluster_2: 12.68
- **Magnitude:** 41.56 | **LOC:** 359 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.0361%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 22.6)
  * `super` (Impact: 18.5)
  * `sendMessage` (Impact: 15.2)
  * `getCompressionHandler` (Impact: 11.0)
  * `resolve` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 65`, `args: 46`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `state_mutation: 86`, `duplicate_logic: 21`
* *Architecture:* `api: 6`, `concurrency: 158`, `import: 9`
* *Defense:* `safety: 5`, `doc: 8`, `immutability_locks: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.313
  * `Choke Point (Betweenness):` 0.001553 | `Ripple Effect (Closeness):` 0.132404
  * `Imports (Out-Degree: 8):` logging, zlib, compression-algorithms, constants, channel, metadata, call-interface, channel-options...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/server-credentials.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.718 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.573 IQR)
- **Top Global Matches:** file_cluster_8: 12.718, file_cluster_13: 12.736, file_cluster_11: 13.032
- **Magnitude:** 37.11 | **LOC:** 353 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.5843%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_equals` (Impact: 57.2)
  * `createSsl` (Impact: 30.4)
  * `_equals` (Impact: 11.2)
  * `_equals` (Impact: 9.3)
  * `calculateSecureContextOptions` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 61`, `args: 40`, `func_start: 40`, `class_start: 7`
* *Risk/State:* `state_mutation: 162`, `duplicate_logic: 26`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 11`, `doc: 3`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.99
  * `Choke Point (Betweenness):` 0.00103 | `Ripple Effect (Closeness):` 0.146087
  * `Imports (Out-Degree: 2):` tls, certificate-provider, http2, , tls-helpers
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/service-config.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.259 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.691 IQR)
- **Top Global Matches:** file_cluster_8: 9.259, file_cluster_7: 9.812, file_cluster_13: 9.966
- **Magnitude:** 36.47 | **LOC:** 565 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.9916%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateMethodConfig` (Impact: 57.5)
  * `validateRetryPolicy` (Impact: 49.8)
  * `validateCanaryConfig` (Impact: 45.3)
  * `validateHedgingPolicy` (Impact: 38.5)
  * `validateServiceConfig` (Impact: 36.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 39`, `args: 10`, `func_start: 10`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 22`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 5`, `doc: 7`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.245
  * `Choke Point (Betweenness):` 0.007939 | `Ripple Effect (Closeness):` 0.22039
  * `Imports (Out-Degree: 2):` constants, duration, os
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/src/resolving-load-balancer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.213 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.656 IQR)
- **Top Global Matches:** file_cluster_13: 12.213, file_cluster_8: 12.429, file_cluster_11: 12.663
- **Magnitude:** 31.95 | **LOC:** 408 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.1863%), Tech Debt (67.1601%)
**Top Internal Functions/Classes:**
  * `hasMatchingName` (Impact: 32.6)
  * `getDefaultConfigSelector` (Impact: 27.5)
  * `constructor` (Impact: 20.4)
  * `invoke` (Impact: 17.2)
  * `exitIdle` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 39`, `args: 22`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 151`, `duplicate_logic: 4`
* *Architecture:* `api: 6`, `import: 15`
* *Defense:* `safety: 10`, `doc: 4`, `immutability_locks: 19`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.948
  * `Choke Point (Betweenness):` 0.008566 | `Ripple Effect (Closeness):` 0.13098
  * `Imports (Out-Degree: 13):` service-config, logging, constants, connectivity-state, metadata, resolver, call-interface, uri-parser...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/orca.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.268 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.495 IQR)
- **Top Global Matches:** file_cluster_13: 13.268, file_cluster_11: 13.753, file_cluster_8: 13.758
- **Magnitude:** 31.38 | **LOC:** 350 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.6092%), Tech Debt (92.6921%)
**Top Internal Functions/Classes:**
  * `updateMetricsSubscription` (Impact: 17.0)
  * `createMetricsReader` (Impact: 9.6)
  * `removeDataWatcher` (Impact: 7.5)
  * `previousOnCallEnded` (Impact: 5.2)
  * `listener` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 56`, `args: 53`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 144`, `duplicate_logic: 5`
* *Architecture:* `api: 32`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 10`, `doc: 24`, `immutability_locks: 18`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.612
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` subchannel, OrcaLoadReport, constants, proto-loader, channel, connectivity-state, OpenRcaService, picker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/subchannel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.564 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.947 IQR)
- **Top Global Matches:** file_cluster_13: 12.564, file_cluster_8: 12.899, file_cluster_7: 13.133
- **Magnitude:** 27.28 | **LOC:** 560 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.1451%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `startConnectingInternal` (Impact: 27.7)
  * `constructor` (Impact: 14.5)
    * *Intent:* /** * Indicates that the subchannel should transition from TRANSIENT_FAILURE to * CONNECTING instead...
  * `handleBackoffTimer` (Impact: 5.8)
  * `getOrCreateDataProducer` (Impact: 3.9)
  * `throttleKeepalive` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 36`, `args: 29`, `func_start: 24`
* *Risk/State:* `state_mutation: 156`
* *Architecture:* `api: 18`, `import: 17`
* *Defense:* `safety: 8`, `doc: 16`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.493
  * `Choke Point (Betweenness):` 0.033624 | `Ripple Effect (Closeness):` 0.127551
  * `Imports (Out-Degree: 14):` subchannel-call, logging, constants, single-subchannel-channel, connectivity-state, call-credentials, metadata, transport...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-pick-first.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.949 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.746 IQR)
- **Top Global Matches:** file_cluster_13: 11.949, file_cluster_8: 12.046, file_cluster_7: 12.286
- **Magnitude:** 26.33 | **LOC:** 663 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.2138%), Tech Debt (99.4685%)
**Top Internal Functions/Classes:**
  * `interleaveAddressFamilies` (Impact: 30.9)
  * `updateAddressList` (Impact: 19.9)
  * `isTcpSubchannelAddress` (Impact: 8.9)
    * *Intent:* /** * Return a new array with the elements of the input array in a random order
  * `createFromJson` (Impact: 8.6)
  * `trace` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 47`, `args: 33`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 114`, `duplicate_logic: 9`
* *Architecture:* `api: 14`, `import: 11`
* *Defense:* `safety: 2`, `doc: 22`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.292
  * `Choke Point (Betweenness):` 0.003921 | `Ripple Effect (Closeness):` 0.060386
  * `Imports (Out-Degree: 9):` logging, constants, connectivity-state, call-interface, load-balancer, channel-options, picker, subchannel-interface...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/certificate-provider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.037 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.899 IQR)
- **Top Global Matches:** file_cluster_4: 14.037, file_cluster_13: 14.233, file_cluster_17: 14.424
- **Magnitude:** 26.32 | **LOC:** 177 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.9328%), Tech Debt (99.0935%)
**Top Internal Functions/Classes:**
  * `updateCertificates` (Impact: 24.5)
  * `constructor` (Impact: 10.3)
  * `maybeStartWatchingFiles` (Impact: 9.5)
  * `removeIdentityCertificateListener` (Impact: 7.4)
  * `maybeStopWatchingFiles` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 23`, `args: 22`, `func_start: 20`, `class_start: 7`
* *Risk/State:* `state_mutation: 141`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 31`, `import: 4`
* *Defense:* `safety: 10`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.063
  * `Choke Point (Betweenness):` 0.000448 | `Ripple Effect (Closeness):` 0.19005
  * `Imports (Out-Degree: 2):` constants, util, logging, fs
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/server-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.043 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.292 IQR)
- **Top Global Matches:** file_cluster_13: 12.043, file_cluster_2: 12.111, file_cluster_16: 12.183
- **Magnitude:** 23.96 | **LOC:** 421 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.8556%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `serverErrorToStatus` (Impact: 21.9)
  * `end` (Impact: 6.2)
  * `_final` (Impact: 5.5)
  * `end` (Impact: 5.5)
  * `_final` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 114`, `args: 63`, `func_start: 57`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 74`, `duplicate_logic: 47`
* *Architecture:* `io: 12`, `api: 30`, `import: 11`
* *Defense:* `safety: 20`, `doc: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.699
  * `Choke Point (Betweenness):` 0.13676 | `Ripple Effect (Closeness):` 0.316394
  * `Imports (Out-Degree: 9):` constants, server-interceptors, stream, metadata, call-interface, auth-context, orca, events...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-child-handler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.346 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.859 IQR)
- **Top Global Matches:** file_cluster_13: 13.346, file_cluster_8: 13.621, file_cluster_17: 13.862
- **Magnitude:** 21.67 | **LOC:** 174 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.9555%), Tech Debt (74.9721%)
**Top Internal Functions/Classes:**
  * `updateAddressList` (Impact: 24.1)
  * `updateState` (Impact: 12.7)
  * `requestReresolution` (Impact: 6.0)
  * `destroy` (Impact: 4.8)
  * `exitIdle` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 22`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 134`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 7`, `doc: 4`, `immutability_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.857
  * `Choke Point (Betweenness):` 0.001499 | `Ripple Effect (Closeness):` 0.112789
  * `Imports (Out-Degree: 7):` connectivity-state, call-interface, load-balancer, channel-options, channelz, picker, subchannel-interface, subchannel-address
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/subchannel-address.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.2 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.964 IQR)
- **Top Global Matches:** file_cluster_8: 11.2, file_cluster_13: 11.31, file_cluster_17: 11.384
- **Magnitude:** 21.56 | **LOC:** 253 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5437%), Tech Debt (50.3141%)
**Top Internal Functions/Classes:**
  * `subchannelAddressEqual` (Impact: 21.8)
  * `endpointEqualUnordered` (Impact: 13.2)
  * `stringToSubchannelAddress` (Impact: 11.1)
  * `subchannelAddressToString` (Impact: 10.6)
  * `deleteMissing` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 48`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `state_mutation: 59`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 20`, `import: 1`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.782
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.311771
  * `Imports (Out-Degree: 0):` net
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/client.ts` (TYPESCRIPT) | Magnitude: 21.25 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 399, branch: 80, structural_boundaries: 60, func_start: 46
- `package/src/transport.ts` (TYPESCRIPT) | Magnitude: 110.72 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 645, state_mutation: 420, branch: 115, structural_boundaries: 87
- `package/src/resolving-call.ts` (TYPESCRIPT) | Magnitude: 55.81 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 338, indent_spaces: 325, branch: 54, structural_boundaries: 41
- `package/src/server-call.ts` (TYPESCRIPT) | Magnitude: 23.96 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 114, state_mutation: 74, args: 63
- `package/src/load-balancer-weighted-round-robin.ts` (TYPESCRIPT) | Magnitude: 43.82 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 341, state_mutation: 194, branch: 81, structural_boundaries: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/src/make-client.ts` (TYPESCRIPT) | Magnitude: 2.33 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 36, generics: 19, branch: 12
- `package/src/object-stream.ts` (TYPESCRIPT) | Magnitude: 5.85 | Delta: **0.321 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, generics: 27, structural_boundaries: 22, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/src/filter.ts` (TYPESCRIPT) | Magnitude: 3.16 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, concurrency: 15, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/resolver-dns.ts` (TYPESCRIPT) | Magnitude: 55.9 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 360, state_mutation: 281, branch: 65, concurrency: 53
- `package/src/channel-credentials.ts` (TYPESCRIPT) | Magnitude: 60.23 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 372, state_mutation: 155, branch: 99, structural_boundaries: 93
- `package/src/certificate-provider.ts` (TYPESCRIPT) | Magnitude: 26.32 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 141, indent_spaces: 117, concurrency: 31, branch: 27
- `package/src/compression-filter.ts` (TYPESCRIPT) | Magnitude: 41.56 | Delta: **0.279 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 235, concurrency: 158, state_mutation: 86, structural_boundaries: 65
- `package/src/single-subchannel-channel.ts` (TYPESCRIPT) | Magnitude: 43.62 | Delta: **0.315 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 211, indent_spaces: 198, concurrency: 96, structural_boundaries: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/events.ts` (TYPESCRIPT) | Magnitude: 3.4 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, args: 7, func_start: 7, indent_spaces: 7
- `package/src/server-credentials.ts` (TYPESCRIPT) | Magnitude: 37.11 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 270, state_mutation: 162, branch: 64, structural_boundaries: 61
- `package/src/http_proxy.ts` (TYPESCRIPT) | Magnitude: 13.73 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 159, structural_boundaries: 42, branch: 36, immutability_locks: 22
- `package/src/retrying-call.ts` (TYPESCRIPT) | Magnitude: 119.18 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 764, state_mutation: 678, branch: 163, structural_boundaries: 79
- `package/src/subchannel-address.ts` (TYPESCRIPT) | Magnitude: 21.56 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, state_mutation: 59, branch: 48, structural_boundaries: 48

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/server-call.ts` -> **Severity: 13.657** (Bridge: 0.1368 * Flux: 99.8582%)
- `package/src/call-interface.ts` -> **Severity: 12.767** (Bridge: 0.1277 * Flux: 100.0%)
- `package/src/internal-channel.ts` -> **Severity: 12.54** (Bridge: 0.1254 * Flux: 100.0%)
- `package/src/channel.ts` -> **Severity: 11.265** (Bridge: 0.1179 * Flux: 95.5794%)
- `package/src/subchannel-interface.ts` -> **Severity: 4.441** (Bridge: 0.0451 * Flux: 98.4593%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/call-interface.ts` -> **Severity: 39.06** (Embedded: 0.4872 * Error Risk: 80.1645%)
- `package/src/metadata.ts` -> **Severity: 32.924** (Embedded: 0.4466 * Error Risk: 73.7178%)
- `package/src/logging.ts` -> **Severity: 31.87** (Embedded: 0.4381 * Error Risk: 72.7469%)
- `package/src/subchannel-address.ts` -> **Severity: 25.445** (Embedded: 0.3118 * Error Risk: 81.614%)
- `package/src/channel-options.ts` -> **Severity: 24.78** (Embedded: 0.3816 * Error Risk: 64.9425%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/constants.ts` -> **Severity: 5380.314** (Blast Radius: 109.398 * Doc Risk: 49.1811%)
- `package/src/call-interface.ts` -> **Severity: 3916.634** (Blast Radius: 40.18 * Doc Risk: 97.4772%)
- `package/src/logging.ts` -> **Severity: 2878.516** (Blast Radius: 43.402 * Doc Risk: 66.3222%)
- `package/src/error.ts` -> **Severity: 1644.497** (Blast Radius: 24.223 * Doc Risk: 67.8899%)
- `package/src/subchannel-address.ts` -> **Severity: 1644.033** (Blast Radius: 21.782 * Doc Risk: 75.4767%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
