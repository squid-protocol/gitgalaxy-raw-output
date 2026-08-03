# ARCHITECTURAL_BRIEF: @grpc_grpc-js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@grpc_grpc-js` |
| **Timestamp** | `2026-08-03T21:07:57.162671+00:00` |
| **Scan Duration** | `0.48s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 69 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 39.2 | 39.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 61.6 | 72.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.6 | 0.0 | 0.0 |
| Testing Exposure | 0.3 | 80.0 | 48.4 | 80.0 | 80.0 |
| API Exposure | 0.0 | 13.4 | 5.3 | 4.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 28.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 63.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 8.0 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 94.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 100.0 | 47.7 | 44.2 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 53.9 | 99.5 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 38.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `destroy` (@ `package/src/server.ts`) -> Impact: **1267.4** | LOC: 910
  * *Intent:* /** * If there is a pending bindAsync operation, this is a promise that resolves * with the port number when that operation succeeds. If there is no s...
- `onReceiveStatus` (@ `package/src/load-balancing-call.ts`) -> Impact: **707.8** | LOC: 335
- `shutdown` (@ `package/src/transport.ts`) -> Impact: **461.0** | LOC: 509
- `shutdown` (@ `package/src/transport.ts`) -> Impact: **234.9** | LOC: 172
- `getAuthContext` (@ `package/src/client-interceptors.ts`) -> Impact: **232.6** | LOC: 127
- `constructor` (@ `package/src/internal-channel.ts`) -> Impact: **186.9** | LOC: 218
  * *Intent:* /** * This timer does not do anything on its own. Its purpose is to hold the * event loop open while there are any pending calls for the channel that ...
- `calculateAndUpdateState` (@ `package/src/load-balancer-weighted-round-robin.ts`) -> Impact: **167.7** | LOC: 64
- `getMetricsRecorder` (@ `package/src/server-interceptors.ts`) -> Impact: **150.2** | LOC: 119
- `deserialize` (@ `package/src/client.ts`) -> Impact: **144.8** | LOC: 97
- `getConfig` (@ `package/src/resolving-call.ts`) -> Impact: **132.8** | LOC: 111

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `onReceiveStatus` (@ `package/src/load-balancing-call.ts`) -> **O(2^N) [Recursive]**
- `destroy` (@ `package/src/server.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * If there is a pending bindAsync operation, this is a promise that resolves * with the port number when that operation succeeds. If there is no s...
- `deserialize` (@ `package/src/client.ts`) -> **O(2^N) [Recursive]**
- `calculateAndUpdateState` (@ `package/src/load-balancer-weighted-round-robin.ts`) -> **O(2^N) [Recursive]**
- `createSubchannel` (@ `package/src/load-balancer-weighted-round-robin.ts`) -> **O(2^N) [Recursive]**
- `getConfig` (@ `package/src/resolving-call.ts`) -> **O(2^N) [Recursive]**
- `sendMessageWithContext` (@ `package/src/retrying-call.ts`) -> **O(2^N) [Recursive]**
- `getAuthContext` (@ `package/src/client-interceptors.ts`) -> **O(2^N) [Recursive]**
- `start` (@ `package/src/client-interceptors.ts`) -> **O(2^N) [Recursive]**
- `startIdleTimeout` (@ `package/src/internal-channel.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `destroy` (@ `package/src/server.ts`) -> DB Complexity: **189**
  * *Intent:* /** * If there is a pending bindAsync operation, this is a promise that resolves * with the port number when that operation succeeds. If there is no s...
- `shutdown` (@ `package/src/transport.ts`) -> DB Complexity: **149**
- `onReceiveStatus` (@ `package/src/load-balancing-call.ts`) -> DB Complexity: **100**
- `constructor` (@ `package/src/internal-channel.ts`) -> DB Complexity: **71**
  * *Intent:* /** * This timer does not do anything on its own. Its purpose is to hold the * event loop open while there are any pending calls for the channel that ...
- `getConfig` (@ `package/src/resolving-call.ts`) -> DB Complexity: **58**
- `startResolution` (@ `package/src/resolver-dns.ts`) -> DB Complexity: **52**
- `getMetricsRecorder` (@ `package/src/server-interceptors.ts`) -> DB Complexity: **41**
- `write` (@ `package/src/stream-decoder.ts`) -> DB Complexity: **41**
- `startConnectingInternal` (@ `package/src/subchannel.ts`) -> DB Complexity: **40**
- `right` (@ `package/src/priority-queue.ts`) -> DB Complexity: **38**
  * *Intent:* /* * Copyright 2025 gRPC authors. * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compliance...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src` | 66 | 2035.13 | 40.49% | 27.85% |
| `package/proto` | 1 | 17.4 | 0.0% | 0.0% |
| `package/proto/xds/xds/data/orca/v3` | 1 | 15.38 | 13.73% | 0.0% |
| `package/proto/xds/xds/service/orca/v3` | 1 | 15.3 | 17.48% | 0.0% |
| `package` | 1 | 1.8 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/call.ts` -> **100.0%** Exposure
- `package/src/channel-credentials.ts` -> **100.0%** Exposure
- `package/src/server-call.ts` -> **100.0%** Exposure
- `package/src/server-credentials.ts` -> **100.0%** Exposure
- `package/src/filter-stack.ts` -> **99.9999%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/call-interface.ts` -> **100.0%** Exposure
- `package/src/certificate-provider.ts` -> **100.0%** Exposure
- `package/src/filter-stack.ts` -> **100.0%** Exposure
- `package/src/internal-channel.ts` -> **100.0%** Exposure
- `package/src/load-balancer-child-handler.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/server-call.ts` -> **0** Orphaned Functions | **42** Duplicates
- `package/src/channel-credentials.ts` -> **0** Orphaned Functions | **29** Duplicates
- `package/src/call.ts` -> **0** Orphaned Functions | **23** Duplicates
- `package/src/server-credentials.ts` -> **0** Orphaned Functions | **23** Duplicates
- `package/src/server-interceptors.ts` -> **0** Orphaned Functions | **22** Duplicates

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

### Exploit Generation Surface
- `package/src/channel-credentials.ts` -> **100.0%** Exposure
- `package/src/client-interceptors.ts` -> **100.0%** Exposure
- `package/src/client.ts` -> **100.0%** Exposure
- `package/src/compression-filter.ts` -> **100.0%** Exposure
- `package/src/internal-channel.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/src/certificate-provider.ts` -> **100.0%** Exposure
- `package/src/channel-credentials.ts` -> **100.0%** Exposure
- `package/src/client-interceptors.ts` -> **100.0%** Exposure
- `package/src/client.ts` -> **100.0%** Exposure
- `package/src/compression-filter.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `43` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/server-interceptors.ts` (TYPESCRIPT) -> Cumulative Risk: **942.76**
- **Archetype:** `file_cluster_13` (Distance: 14.151 IQR)
- **Magnitude:** 130.77 | **LOC:** 1072 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getMetricsRecorder` (Impact: 150.2), `constructor` (Impact: 72.3), `sendStatus` (Impact: 54.9)

### 2. `package/src/compression-filter.ts` (TYPESCRIPT) -> Cumulative Risk: **934.01**
- **Archetype:** `file_cluster_4` (Distance: 12.303 IQR)
- **Magnitude:** 42.54 | **LOC:** 359 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 43.4), `sendMessage` (Impact: 22.2), `sendMetadata` (Impact: 13.3)

### 3. `package/src/load-balancer-outlier-detection.ts` (TYPESCRIPT) -> Cumulative Risk: **914.36**
- **Archetype:** `file_cluster_8` (Distance: 12.301 IQR)
- **Magnitude:** 96.51 | **LOC:** 841 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9955%)
- **Heaviest Functions:** `updateAddressList` (Impact: 110.2), `runSuccessRateCheck` (Impact: 64.8), `pick` (Impact: 64.0)

### 4. `package/src/channel-credentials.ts` (TYPESCRIPT) -> Cumulative Risk: **877.42**
- **Archetype:** `file_cluster_4` (Distance: 13.398 IQR)
- **Magnitude:** 58.72 | **LOC:** 524 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `destroy` (Impact: 51.8), `getConnectionOptions` (Impact: 31.2), `connect` (Impact: 29.6)

### 5. `package/src/resolving-call.ts` (TYPESCRIPT) -> Cumulative Risk: **867.27**
- **Archetype:** `file_cluster_13` (Distance: 13.783 IQR)
- **Magnitude:** 67.2 | **LOC:** 380 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getConfig` (Impact: 132.8), `runDeadlineTimer` (Impact: 50.5), `constructor` (Impact: 21.0)

### 6. `package/src/resolver-dns.ts` (TYPESCRIPT) -> Cumulative Risk: **859.95**
- **Archetype:** `file_cluster_4` (Distance: 13.576 IQR)
- **Magnitude:** 69.18 | **LOC:** 450 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `startResolution` (Impact: 124.7), `constructor` (Impact: 88.2), `lookup` (Impact: 55.3)

### 7. `package/src/load-balancer-weighted-round-robin.ts` (TYPESCRIPT) -> Cumulative Risk: **856.45**
- **Archetype:** `file_cluster_13` (Distance: 12.748 IQR)
- **Magnitude:** 62.52 | **LOC:** 495 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `calculateAndUpdateState` (Impact: 167.7), `constructor` (Impact: 35.1), `createSubchannel` (Impact: 35.0)

### 8. `package/src/internal-channel.ts` (TYPESCRIPT) -> Cumulative Risk: **856.05**
- **Archetype:** `file_cluster_13` (Distance: 13.542 IQR)
- **Magnitude:** 113.14 | **LOC:** 879 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 186.9), `callback` (Impact: 43.5), `startIdleTimeout` (Impact: 41.2)

### 9. `package/src/load-balancer-round-robin.ts` (TYPESCRIPT) -> Cumulative Risk: **856.03**
- **Archetype:** `file_cluster_13` (Distance: 11.373 IQR)
- **Magnitude:** 15.76 | **LOC:** 288 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.999%), Logic Bomb (99.9891%)
- **Heaviest Functions:** `calculateAndUpdateState` (Impact: 37.0), `constructor` (Impact: 22.1), `trace` (Impact: 4.2)

### 10. `package/src/server-credentials.ts` (TYPESCRIPT) -> Cumulative Risk: **854.96**
- **Archetype:** `file_cluster_8` (Distance: 12.726 IQR)
- **Magnitude:** 47.49 | **LOC:** 353 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_equals` (Impact: 110.9), `createSsl` (Impact: 44.4), `_equals` (Impact: 32.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/server.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.385 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.143 IQR)
- **Top Global Matches:** file_cluster_13: 13.385, file_cluster_11: 13.501, file_cluster_4: 13.582
- **Magnitude:** 174.22 | **LOC:** 2213 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 189
- **Risk Profile:** Cognitive Load (75.2847%), Tech Debt (7.9509%)
**Top Internal Functions/Classes:**
  * `destroy` (Impact: 1267.4 | O(2^N) | DB: 189)
    * *Intent:* /** * If there is a pending bindAsync operation, this is a promise that resolves * with the port num...
  * `getDefaultHandler` (Impact: 19.7 | O(N^2))
  * `deprecate` (Impact: 4.5 | O(2^N))
  * `onClose` (Impact: 4.3 | O(N^1))
    * *Intent:* /** * The key used to refer to this object in the boundPorts map.
  * `getUnimplementedStatusResponse` (Impact: 2.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 119`, `args: 108`, `func_start: 88`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 375`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 18`, `api: 7`, `concurrency: 38`, `import: 20`
* *Defense:* `safety: 57`, `doc: 20`, `immutability_locks: 49`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.244
  * `Choke Point (Betweenness):` 0.029039 | `Ripple Effect (Closeness):` 0.176539
  * `Imports (Out-Degree: 14):` channelz, http2, resolver, constants, subchannel-address, util, server-interceptors, logging...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/retrying-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.848 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.877 IQR)
- **Top Global Matches:** file_cluster_8: 13.848, file_cluster_13: 13.907, file_cluster_17: 14.039
- **Magnitude:** 150.17 | **LOC:** 924 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (66.4332%), Tech Debt (17.4649%)
**Top Internal Functions/Classes:**
  * `handleProcessedStatus` (Impact: 99.3 | O(N^3) | DB: 24)
  * `sendMessageWithContext` (Impact: 89.4 | O(2^N) | DB: 14)
  * `callback` (Impact: 79.8 | O(2^N) | DB: 13)
  * `sendNextChildMessage` (Impact: 62.1 | O(N^4) | DB: 6)
  * `constructor` (Impact: 49.4 | O(N^2) | DB: 11)
    * *Intent:* /** * Entry in the buffer of messages to send to the remote end.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 79`, `args: 62`, `func_start: 57`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 684`, `duplicate_logic: 3`
* *Architecture:* `api: 6`, `concurrency: 18`, `import: 10`
* *Defense:* `safety: 33`, `doc: 9`, `immutability_locks: 52`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.948
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.128901
  * `Imports (Out-Degree: 10):` constants, call-interface, metadata, load-balancing-call, logging, auth-context, resolver, call-credentials...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/server-interceptors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.151 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.233 IQR)
- **Top Global Matches:** file_cluster_13: 14.151, file_cluster_8: 14.248, file_cluster_11: 14.273
- **Magnitude:** 130.77 | **LOC:** 1072 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (72.9189%), Tech Debt (99.8484%)
**Top Internal Functions/Classes:**
  * `getMetricsRecorder` (Impact: 150.2 | O(2^N) | DB: 41)
  * `constructor` (Impact: 72.3 | O(N^2) | DB: 34)
    * *Intent:* // TODO(cjihrig): Remove these encoding headers from the default response // once compression is int...
  * `sendStatus` (Impact: 54.9 | O(N^3) | DB: 28)
  * `decompressMessage` (Impact: 36.7 | O(N^3) | DB: 6)
  * `onReceiveMessage` (Impact: 26.9 | O(2^N) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 174`, `args: 126`, `func_start: 98`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 593`, `planned_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 9`, `api: 32`, `concurrency: 21`, `import: 16`
* *Defense:* `safety: 88`, `doc: 19`, `immutability_locks: 46`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.336
  * `Choke Point (Betweenness):` 0.025314 | `Ripple Effect (Closeness):` 0.217521
  * `Imports (Out-Degree: 12):` channel-options, call-interface, constants, stream-decoder, metadata, transport, logging, http2...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/transport.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.05 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.224 IQR)
- **Top Global Matches:** file_cluster_13: 14.05, file_cluster_4: 14.069, file_cluster_8: 14.245
- **Magnitude:** 122.66 | **LOC:** 826 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 149
- **Risk Profile:** Cognitive Load (73.5457%), Tech Debt (14.5401%)
**Top Internal Functions/Classes:**
  * `shutdown` (Impact: 461.0 | O(2^N) | DB: 149)
  * `shutdown` (Impact: 234.9 | O(2^N) | DB: 31)
  * `onStreamEnd` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 87`, `args: 83`, `func_start: 65`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 428`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 5`, `concurrency: 82`, `import: 19`
* *Defense:* `safety: 53`, `doc: 12`, `immutability_locks: 35`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.894
  * `Choke Point (Betweenness):` 0.033367 | `Ripple Effect (Closeness):` 0.203019
  * `Imports (Out-Degree: 13):` http_proxy, channel-options, call-interface, constants, metadata, call-number, subchannel-address, logging...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/src/internal-channel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.542 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.119 IQR)
- **Top Global Matches:** file_cluster_13: 13.542, file_cluster_8: 13.641, file_cluster_11: 13.865
- **Magnitude:** 113.14 | **LOC:** 879 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (82.2243%), Tech Debt (30.0615%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 186.9 | O(N^3) | DB: 71)
    * *Intent:* /** * This timer does not do anything on its own. Its purpose is to hold the * event loop open while...
  * `callback` (Impact: 43.5 | O(2^N) | DB: 5)
  * `startIdleTimeout` (Impact: 41.2 | O(2^N) | DB: 12)
  * `createResolvingCall` (Impact: 38.6 | O(2^N) | DB: 5)
  * `createCall` (Impact: 38.0 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 85`, `args: 64`, `func_start: 55`, `class_start: 8`
* *Risk/State:* `state_mutation: 546`, `duplicate_logic: 5`
* *Architecture:* `api: 7`, `concurrency: 18`, `import: 27`
* *Defense:* `safety: 24`, `doc: 7`, `immutability_locks: 56`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.252
  * `Choke Point (Betweenness):` 0.125404 | `Ripple Effect (Closeness):` 0.163505
  * `Imports (Out-Degree: 26):` subchannel-pool, resolving-load-balancer, load-balancing-call, channelz, resolver, call-credentials, filter-stack, constants...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/src/load-balancing-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.417 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.54 IQR)
- **Top Global Matches:** file_cluster_13: 13.417, file_cluster_8: 13.568, file_cluster_4: 13.669
- **Magnitude:** 99.59 | **LOC:** 388 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 100
- **Risk Profile:** Cognitive Load (73.9331%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onReceiveStatus` (Impact: 707.8 | O(2^N) | DB: 100)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 44`, `args: 23`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 265`
* *Architecture:* `io: 1`, `api: 4`, `concurrency: 12`, `import: 15`
* *Defense:* `safety: 22`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.538
  * `Choke Point (Betweenness):` 0.002394 | `Ripple Effect (Closeness):` 0.129587
  * `Imports (Out-Degree: 14):` constants, call-interface, connectivity-state, metadata, picker, control-plane-status, logging, auth-context...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-outlier-detection.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.301 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.628 IQR)
- **Top Global Matches:** file_cluster_8: 12.301, file_cluster_13: 12.471, file_cluster_11: 12.74
- **Magnitude:** 96.51 | **LOC:** 841 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (89.0782%), Tech Debt (53.4575%)
**Top Internal Functions/Classes:**
  * `updateAddressList` (Impact: 110.2 | O(2^N) | DB: 19)
  * `runSuccessRateCheck` (Impact: 64.8 | O(N^3) | DB: 11)
  * `pick` (Impact: 64.0 | O(2^N) | DB: 3)
  * `runFailurePercentageCheck` (Impact: 55.1 | O(N^3) | DB: 8)
  * `constructor` (Impact: 52.3 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 74`, `args: 91`, `func_start: 88`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 270`, `duplicate_logic: 8`
* *Architecture:* `api: 9`, `concurrency: 12`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 70`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.125
  * `Choke Point (Betweenness):` 0.000667 | `Ripple Effect (Closeness):` 0.028986
  * `Imports (Out-Degree: 13):` duration, channel-options, constants, connectivity-state, call-interface, picker, load-balancer-child-handler, experimental...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/client-interceptors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.706 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.016 IQR)
- **Top Global Matches:** file_cluster_13: 13.706, file_cluster_11: 13.802, file_cluster_17: 13.831
- **Magnitude:** 71.39 | **LOC:** 586 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (45.0925%), Tech Debt (99.4283%)
**Top Internal Functions/Classes:**
  * `getAuthContext` (Impact: 232.6 | O(2^N) | DB: 36)
  * `start` (Impact: 98.7 | O(2^N) | DB: 5)
  * `start` (Impact: 68.5 | O(2^N) | DB: 2)
  * `getInterceptingCall` (Impact: 32.6 | O(N^2) | DB: 1)
  * `sendMessageWithContext` (Impact: 16.2 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 104`, `args: 86`, `func_start: 70`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 153`, `duplicate_logic: 14`
* *Architecture:* `io: 3`, `api: 25`, `import: 8`
* *Defense:* `safety: 65`, `doc: 25`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.479
  * `Choke Point (Betweenness):` 0.010119 | `Ripple Effect (Closeness):` 0.139213
  * `Imports (Out-Degree: 8):` constants, call-interface, metadata, make-client, auth-context, client, channel, error
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/resolver-dns.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.576 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_4: 13.576, file_cluster_13: 13.624, file_cluster_8: 13.84
- **Magnitude:** 69.18 | **LOC:** 450 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (73.2884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `startResolution` (Impact: 124.7 | O(N^4) | DB: 52)
  * `constructor` (Impact: 88.2 | O(N^4) | DB: 24)
  * `lookup` (Impact: 55.3 | O(2^N) | DB: 4)
    * *Intent:* /* If TXT lookup fails we should do nothing, which means that we * continue to use the result of the...
  * `updateResolution` (Impact: 23.8 | O(N^3) | DB: 8)
  * `resolveTxt` (Impact: 9.3 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 51`, `args: 46`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 291`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 53`, `import: 14`
* *Defense:* `safety: 17`, `doc: 10`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.885
  * `Choke Point (Betweenness):` 0.018211 | `Ripple Effect (Closeness):` 0.141641
  * `Imports (Out-Degree: 10):` constants, call-interface, channel-options, dns, metadata, subchannel-address, service-config, environment...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/resolving-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.783 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.361 IQR)
- **Top Global Matches:** file_cluster_13: 13.783, file_cluster_8: 13.84, file_cluster_4: 13.843
- **Magnitude:** 67.2 | **LOC:** 380 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (76.3681%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getConfig` (Impact: 132.8 | O(2^N) | DB: 58)
  * `runDeadlineTimer` (Impact: 50.5 | O(N^3) | DB: 29)
  * `constructor` (Impact: 21.0 | O(N^3) | DB: 8)
  * `outputStatus` (Impact: 13.1 | O(N^2) | DB: 10)
  * `halfClose` (Impact: 11.7 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 41`, `args: 34`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 340`
* *Architecture:* `api: 5`, `concurrency: 19`, `import: 10`
* *Defense:* `safety: 16`, `doc: 1`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.948
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.128901
  * `Imports (Out-Degree: 10):` constants, call-interface, metadata, control-plane-status, logging, auth-context, call-credentials, internal-channel...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-weighted-round-robin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.748 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.209 IQR)
- **Top Global Matches:** file_cluster_13: 12.748, file_cluster_8: 12.819, file_cluster_17: 13.06
- **Magnitude:** 62.52 | **LOC:** 495 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (92.5907%), Tech Debt (36.659%)
**Top Internal Functions/Classes:**
  * `calculateAndUpdateState` (Impact: 167.7 | O(2^N) | DB: 21)
  * `constructor` (Impact: 35.1 | O(N^1) | DB: 6)
  * `createSubchannel` (Impact: 35.0 | O(2^N) | DB: 2)
  * `parseDurationField` (Impact: 29.6 | O(N^2) | DB: 1)
  * `pick` (Impact: 27.2 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 61`, `args: 43`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 194`, `duplicate_logic: 3`
* *Architecture:* `api: 9`, `concurrency: 6`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 36`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.8
  * `Choke Point (Betweenness):` 0.000375 | `Ripple Effect (Closeness):` 0.014493
  * `Imports (Out-Degree: 11):` duration, channel-options, call-interface, connectivity-state, constants, priority-queue, picker, load-balancer-pick-first...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/channel-credentials.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.398 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_4: 13.398, file_cluster_13: 13.491, file_cluster_8: 13.692
- **Magnitude:** 58.72 | **LOC:** 524 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (49.7001%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `destroy` (Impact: 51.8 | O(N^2))
  * `getConnectionOptions` (Impact: 31.2 | O(N^1) | DB: 1)
  * `connect` (Impact: 29.6 | O(N^3) | DB: 5)
  * `_equals` (Impact: 26.6 | O(2^N) | DB: 2)
  * `getLatestSecureContext` (Impact: 21.7 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 93`, `args: 85`, `func_start: 76`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 155`, `duplicate_logic: 29`
* *Architecture:* `api: 7`, `concurrency: 66`, `import: 10`
* *Defense:* `safety: 33`, `doc: 21`, `immutability_locks: 20`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.281
  * `Choke Point (Betweenness):` 0.025039 | `Ripple Effect (Closeness):` 0.241211
  * `Imports (Out-Degree: 8):` channel-options, constants, certificate-provider, logging, tls-helpers, resolver, tls, uri-parser...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `package/src/service-config.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.259 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.691 IQR)
- **Top Global Matches:** file_cluster_8: 9.259, file_cluster_7: 9.812, file_cluster_13: 9.966
- **Magnitude:** 55.33 | **LOC:** 565 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.9916%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateCanaryConfig` (Impact: 87.3 | O(N^3) | DB: 2)
  * `validateMethodConfig` (Impact: 84.5 | O(N^2) | DB: 1)
  * `validateHedgingPolicy` (Impact: 74.5 | O(N^3))
  * `validateRetryPolicy` (Impact: 72.8 | O(N^2))
  * `validateServiceConfig` (Impact: 70.5 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 39`, `args: 10`, `func_start: 10`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 22`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 5`, `doc: 7`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.245
  * `Choke Point (Betweenness):` 0.007939 | `Ripple Effect (Closeness):` 0.22039
  * `Imports (Out-Degree: 2):` duration, constants, os
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/src/single-subchannel-channel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.801 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.607 IQR)
- **Top Global Matches:** file_cluster_4: 13.801, file_cluster_13: 14.116, file_cluster_8: 14.448
- **Magnitude:** 48.72 | **LOC:** 249 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (99.7293%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 37.1 | O(N^2) | DB: 30)
  * `constructor` (Impact: 30.5 | O(N^2) | DB: 10)
  * `sendMessageWithContext` (Impact: 21.4 | O(2^N) | DB: 8)
  * `cancelWithStatus` (Impact: 16.2 | O(2^N) | DB: 3)
  * `halfClose` (Impact: 11.7 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 46`, `args: 23`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `state_mutation: 211`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 96`, `import: 18`
* *Defense:* `safety: 15`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.31
  * `Choke Point (Betweenness):` 0.006377 | `Ripple Effect (Closeness):` 0.105465
  * `Imports (Out-Degree: 17):` channel-options, call-interface, connectivity-state, constants, metadata, call-number, control-plane-status, auth-context...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/server-credentials.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.726 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_8: 12.726, file_cluster_13: 12.744, file_cluster_11: 13.04
- **Magnitude:** 47.49 | **LOC:** 353 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (84.4867%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_equals` (Impact: 110.9 | O(N^3) | DB: 16)
  * `createSsl` (Impact: 44.4 | O(N^2) | DB: 3)
  * `_equals` (Impact: 32.0 | O(2^N) | DB: 5)
  * `_addWatcher` (Impact: 10.7 | O(2^N) | DB: 5)
    * *Intent:* /* ciphers is derived from a value that is constant for the process, so no
  * `_removeWatcher` (Impact: 10.7 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 61`, `args: 41`, `func_start: 40`, `class_start: 7`
* *Risk/State:* `state_mutation: 162`, `duplicate_logic: 23`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `safety: 11`, `doc: 3`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.99
  * `Choke Point (Betweenness):` 0.00103 | `Ripple Effect (Closeness):` 0.146087
  * `Imports (Out-Degree: 2):` , certificate-provider, tls-helpers, http2, tls
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/channelz.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.093 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.412 IQR)
- **Top Global Matches:** file_cluster_13: 11.093, file_cluster_8: 11.23, file_cluster_16: 11.47
- **Magnitude:** 46.13 | **LOC:** 910 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (16.9229%), Tech Debt (93.7119%)
**Top Internal Functions/Classes:**
  * `GetSocket` (Impact: 79.5 | O(N^3))
  * `connectivityStateToMessage` (Impact: 30.9 | O(N^2))
  * `ipAddressStringToBuffer` (Impact: 19.4 | O(N^1) | DB: 2)
  * `subchannelAddressToAddressMessage` (Impact: 19.4 | O(N^2) | DB: 3)
  * `addTrace` (Impact: 14.9 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 171`, `args: 73`, `func_start: 65`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 72`, `duplicate_logic: 16`
* *Architecture:* `io: 1`, `api: 33`, `import: 39`
* *Defense:* `safety: 22`, `doc: 14`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.612
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` GetTopChannelsResponse, Security, Subchannel, admin, Channelz, GetSocketResponse, SocketRef, ChannelTrace...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/compression-filter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.303 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.967 IQR)
- **Top Global Matches:** file_cluster_4: 12.303, file_cluster_13: 12.578, file_cluster_2: 12.695
- **Magnitude:** 42.54 | **LOC:** 359 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (69.9876%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 43.4 | O(N^3) | DB: 5)
  * `sendMessage` (Impact: 22.2 | O(N^2) | DB: 6)
  * `sendMetadata` (Impact: 13.3 | O(N^2) | DB: 6)
  * `decompressMessage` (Impact: 11.5 | O(N^3) | DB: 5)
  * `decompressMessage` (Impact: 11.5 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 65`, `args: 47`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `state_mutation: 86`, `duplicate_logic: 15`
* *Architecture:* `api: 6`, `concurrency: 158`, `import: 9`
* *Defense:* `safety: 5`, `doc: 8`, `immutability_locks: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.313
  * `Choke Point (Betweenness):` 0.001553 | `Ripple Effect (Closeness):` 0.132404
  * `Imports (Out-Degree: 8):` channel-options, call-interface, constants, filter, metadata, logging, compression-algorithms, zlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/resolving-load-balancer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.204 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.667 IQR)
- **Top Global Matches:** file_cluster_13: 12.204, file_cluster_8: 12.402, file_cluster_11: 12.651
- **Magnitude:** 38.06 | **LOC:** 408 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (62.1863%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDefaultConfigSelector` (Impact: 52.9 | O(N^3))
  * `hasMatchingName` (Impact: 48.3 | O(N^2))
  * `constructor` (Impact: 46.2 | O(N^4) | DB: 25)
  * `exitIdle` (Impact: 21.9 | O(2^N) | DB: 6)
  * `updateState` (Impact: 12.8 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 39`, `args: 22`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 149`
* *Architecture:* `api: 5`, `import: 15`
* *Defense:* `safety: 10`, `doc: 4`, `immutability_locks: 19`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.948
  * `Choke Point (Betweenness):` 0.008566 | `Ripple Effect (Closeness):` 0.13098
  * `Imports (Out-Degree: 13):` constants, call-interface, connectivity-state, channel-options, metadata, picker, subchannel-address, service-config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/load-balancer-child-handler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.346 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.859 IQR)
- **Top Global Matches:** file_cluster_13: 13.346, file_cluster_8: 13.621, file_cluster_17: 13.862
- **Magnitude:** 32.56 | **LOC:** 174 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (62.9555%), Tech Debt (74.9721%)
**Top Internal Functions/Classes:**
  * `updateAddressList` (Impact: 68.8 | O(2^N) | DB: 17)
  * `updateState` (Impact: 36.6 | O(2^N) | DB: 7)
  * `requestReresolution` (Impact: 17.3 | O(2^N) | DB: 4)
  * `exitIdle` (Impact: 13.1 | O(2^N) | DB: 4)
  * `resetBackoff` (Impact: 13.1 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 22`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 134`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 7`, `doc: 4`, `immutability_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.857
  * `Choke Point (Betweenness):` 0.001499 | `Ripple Effect (Closeness):` 0.112789
  * `Imports (Out-Degree: 7):` channel-options, call-interface, connectivity-state, picker, subchannel-address, load-balancer, channelz, subchannel-interface
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/client.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.657 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.17 IQR)
- **Top Global Matches:** file_cluster_13: 10.657, file_cluster_2: 10.659, file_cluster_8: 10.759
- **Magnitude:** 31.71 | **LOC:** 717 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (13.9209%), Tech Debt (44.8577%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 144.8 | O(2^N) | DB: 8)
  * `deserialize` (Impact: 63.5 | O(2^N) | DB: 9)
  * `waitForReady` (Impact: 36.1 | O(N^3) | DB: 1)
  * `getErrorStackString` (Impact: 6.2 | O(N^1))
  * `checkMetadataAndOptions` (Impact: 5.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 60`, `args: 38`, `func_start: 46`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 28`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 17`, `doc: 5`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.208
  * `Choke Point (Betweenness):` 0.077299 | `Ripple Effect (Closeness):` 0.174017
  * `Imports (Out-Degree: 13):` channel-options, call-interface, connectivity-state, constants, client-interceptors, metadata, deadline, call-credentials...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/orca.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.272 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.486 IQR)
- **Top Global Matches:** file_cluster_13: 13.272, file_cluster_11: 13.756, file_cluster_8: 13.758
- **Magnitude:** 31.42 | **LOC:** 350 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (44.9024%), Tech Debt (62.8128%)
**Top Internal Functions/Classes:**
  * `updateMetricsSubscription` (Impact: 24.8 | O(N^2) | DB: 14)
  * `createMetricsReader` (Impact: 13.9 | O(N^2) | DB: 1)
  * `removeDataWatcher` (Impact: 7.5 | O(N^1) | DB: 10)
  * `StreamCoreMetrics` (Impact: 5.7 | O(N^2) | DB: 1)
  * `loadOrcaProto` (Impact: 4.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 56`, `args: 53`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 144`, `duplicate_logic: 3`
* *Architecture:* `api: 32`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 10`, `doc: 24`, `immutability_locks: 18`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.612
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` proto-loader, duration, subchannel-interface, call, constants, connectivity-state, server, picker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/load-balancer-pick-first.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.947 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.761 IQR)
- **Top Global Matches:** file_cluster_13: 11.947, file_cluster_8: 12.046, file_cluster_7: 12.284
- **Magnitude:** 29.18 | **LOC:** 663 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (43.416%), Tech Debt (97.1076%)
**Top Internal Functions/Classes:**
  * `updateAddressList` (Impact: 55.7 | O(2^N) | DB: 10)
  * `interleaveAddressFamilies` (Impact: 30.9 | O(N^1) | DB: 5)
  * `createFromJson` (Impact: 12.6 | O(N^2))
  * `exitIdle` (Impact: 4.6 | O(N^1) | DB: 5)
  * `shuffled` (Impact: 4.5 | O(N^1) | DB: 1)
    * *Intent:* /** * Picker for a `PickFirstLoadBalancer` in the READY state. Always returns the * picked subchanne...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 47`, `args: 33`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 114`, `duplicate_logic: 7`
* *Architecture:* `api: 14`, `import: 11`
* *Defense:* `safety: 2`, `doc: 22`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.292
  * `Choke Point (Betweenness):` 0.003921 | `Ripple Effect (Closeness):` 0.060386
  * `Imports (Out-Degree: 9):` constants, channel-options, connectivity-state, call-interface, picker, subchannel-address, logging, load-balancer...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/subchannel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.583 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.923 IQR)
- **Top Global Matches:** file_cluster_13: 12.583, file_cluster_8: 12.864, file_cluster_7: 13.13
- **Magnitude:** 28.28 | **LOC:** 560 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (40.7924%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `startConnectingInternal` (Impact: 69.3 | O(N^5) | DB: 40)
  * `constructor` (Impact: 20.6 | O(N^2) | DB: 23)
    * *Intent:* /** * Indicates that the subchannel should transition from TRANSIENT_FAILURE to * CONNECTING instead...
  * `handleBackoffTimer` (Impact: 8.4 | O(N^2) | DB: 3)
  * `trace` (Impact: 6.6 | O(2^N) | DB: 2)
  * `refTrace` (Impact: 3.6 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 36`, `args: 29`, `func_start: 24`
* *Risk/State:* `state_mutation: 158`
* *Architecture:* `api: 5`, `import: 17`
* *Defense:* `safety: 8`, `doc: 16`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.493
  * `Choke Point (Betweenness):` 0.033624 | `Ripple Effect (Closeness):` 0.127551
  * `Imports (Out-Degree: 14):` channel-options, constants, connectivity-state, single-subchannel-channel, metadata, subchannel-address, logging, channelz...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/server-call.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.046 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 12.046, file_cluster_2: 12.113, file_cluster_16: 12.185
- **Magnitude:** 28.25 | **LOC:** 421 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (45.4214%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `serverErrorToStatus` (Impact: 21.9 | O(N^1))
  * `end` (Impact: 12.2 | O(2^N))
  * `end` (Impact: 10.7 | O(2^N) | DB: 1)
  * `end` (Impact: 10.7 | O(2^N) | DB: 1)
  * `_final` (Impact: 5.5 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 114`, `args: 63`, `func_start: 57`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 74`, `duplicate_logic: 42`
* *Architecture:* `io: 12`, `api: 30`, `import: 11`
* *Defense:* `safety: 20`, `doc: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.699
  * `Choke Point (Betweenness):` 0.13676 | `Ripple Effect (Closeness):` 0.316394
  * `Imports (Out-Degree: 9):` constants, call-interface, metadata, events, stream, server-interceptors, orca, make-client...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `package/src/certificate-provider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.05 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.901 IQR)
- **Top Global Matches:** file_cluster_4: 14.05, file_cluster_13: 14.242, file_cluster_11: 14.434
- **Magnitude:** 27.65 | **LOC:** 177 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (96.9328%), Tech Debt (74.9721%)
**Top Internal Functions/Classes:**
  * `updateCertificates` (Impact: 35.8 | O(N^2) | DB: 20)
  * `maybeStartWatchingFiles` (Impact: 13.8 | O(N^2) | DB: 11)
  * `maybeStopWatchingFiles` (Impact: 10.8 | O(N^2) | DB: 6)
  * `constructor` (Impact: 10.3 | O(N^1) | DB: 2)
  * `removeIdentityCertificateListener` (Impact: 7.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 23`, `args: 22`, `func_start: 20`, `class_start: 7`
* *Risk/State:* `state_mutation: 141`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 31`, `import: 4`
* *Defense:* `safety: 10`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.063
  * `Choke Point (Betweenness):` 0.000448 | `Ripple Effect (Closeness):` 0.19005
  * `Imports (Out-Degree: 2):` logging, util, constants, fs
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/client.ts` (TYPESCRIPT) | Magnitude: 31.71 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 399, branch: 80, structural_boundaries: 60, func_start: 46
- `package/src/transport.ts` (TYPESCRIPT) | Magnitude: 122.66 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 645, state_mutation: 428, branch: 115, structural_boundaries: 87
- `package/src/resolving-call.ts` (TYPESCRIPT) | Magnitude: 67.2 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 340, indent_spaces: 325, branch: 54, structural_boundaries: 41
- `package/src/server-call.ts` (TYPESCRIPT) | Magnitude: 28.25 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 114, state_mutation: 74, args: 63
- `package/src/load-balancer-weighted-round-robin.ts` (TYPESCRIPT) | Magnitude: 62.52 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 341, state_mutation: 194, branch: 81, structural_boundaries: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/src/make-client.ts` (TYPESCRIPT) | Magnitude: 2.33 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 36, generics: 19, branch: 12
- `package/src/object-stream.ts` (TYPESCRIPT) | Magnitude: 6.96 | Delta: **0.34 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, generics: 27, structural_boundaries: 22, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/src/filter.ts` (TYPESCRIPT) | Magnitude: 2.33 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, concurrency: 15, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/resolver-dns.ts` (TYPESCRIPT) | Magnitude: 69.18 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 360, state_mutation: 291, branch: 65, concurrency: 53
- `package/src/channel-credentials.ts` (TYPESCRIPT) | Magnitude: 58.72 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 372, state_mutation: 155, branch: 99, structural_boundaries: 93
- `package/src/certificate-provider.ts` (TYPESCRIPT) | Magnitude: 27.65 | Delta: **0.192 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 141, indent_spaces: 117, concurrency: 31, branch: 27
- `package/src/compression-filter.ts` (TYPESCRIPT) | Magnitude: 42.54 | Delta: **0.275 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 235, concurrency: 158, state_mutation: 86, structural_boundaries: 65
- `package/src/single-subchannel-channel.ts` (TYPESCRIPT) | Magnitude: 48.72 | Delta: **0.315 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 211, indent_spaces: 198, concurrency: 96, structural_boundaries: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/events.ts` (TYPESCRIPT) | Magnitude: 3.4 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, args: 7, func_start: 7, indent_spaces: 7
- `package/src/server-credentials.ts` (TYPESCRIPT) | Magnitude: 47.49 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 270, state_mutation: 162, branch: 64, structural_boundaries: 61
- `package/src/http_proxy.ts` (TYPESCRIPT) | Magnitude: 13.37 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 159, structural_boundaries: 42, branch: 36, immutability_locks: 22
- `package/src/retrying-call.ts` (TYPESCRIPT) | Magnitude: 150.17 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 764, state_mutation: 684, branch: 163, structural_boundaries: 79
- `package/src/admin.ts` (TYPESCRIPT) | Magnitude: 1.17 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, api: 4, args: 2

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

- `package/src/constants.ts` -> **Severity: 8003.295** (Blast Radius: 109.398 * Doc Risk: 73.1576%)
- `package/src/call-interface.ts` -> **Severity: 3968.024** (Blast Radius: 40.18 * Doc Risk: 98.7562%)
- `package/src/logging.ts` -> **Severity: 3341.655** (Blast Radius: 43.402 * Doc Risk: 76.9931%)
- `package/src/error.ts` -> **Severity: 2360.464** (Blast Radius: 24.223 * Doc Risk: 97.4472%)
- `package/src/uri-parser.ts` -> **Severity: 1837.407** (Blast Radius: 18.766 * Doc Risk: 97.9115%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
