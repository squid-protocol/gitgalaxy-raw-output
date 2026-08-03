# ARCHITECTURAL_BRIEF: @segment_analytics-node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@segment_analytics-node` |
| **Timestamp** | `2026-08-03T21:10:06.214138+00:00` |
| **Scan Duration** | `0.16s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Total Artifacts | 19 |
| Analyzed Artifacts (Scanned) | 18 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 766 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2812 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3201 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2476 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 16 | 766 | 88.9% |
| MARKDOWN | 1 | 0 | 5.6% |
| PLAINTEXT | 1 | 0 | 5.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.703`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 11 | 61.1% |
| file_cluster_8 | 3 | 16.7% |
| file_cluster_4 | 2 | 11.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 11.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.4 | 80.1 | 18.9 | 6.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 86.0 | 18.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 80.0 | 11.6 | 2.3 | 2.3 |
| API Exposure | 2.3 | 11.9 | 6.7 | 6.7 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 21.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 23.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 5.1 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 77.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 47.0 | 38.6 | 20.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 19.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/plugins/segmentio/publisher.ts` (Hits: 5)
- `package/src/app/analytics-node.ts` (Hits: 3)
- `package/src/app/settings.ts` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **context.ts** (`package/src/app/context.ts`) — 9 inbound connections
2. **emitter.ts** (`package/src/app/emitter.ts`) — 4 inbound connections
3. **settings.ts** (`package/src/app/settings.ts`) — 3 inbound connections
4. **analytics-node.ts** (`package/src/app/analytics-node.ts`) — 2 inbound connections
5. **event-queue.ts** (`package/src/app/event-queue.ts`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **analytics-node.ts** (`package/src/app/analytics-node.ts`) — 11 outbound dependencies
2. **publisher.ts** (`package/src/plugins/segmentio/publisher.ts`) — 9 outbound dependencies
3. **index.common.ts** (`package/src/index.common.ts`) — 6 outbound dependencies
4. **index.ts** (`package/src/plugins/segmentio/index.ts`) — 6 outbound dependencies
5. **dispatch-emit.ts** (`package/src/app/dispatch-emit.ts`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `constructor` (@ `package/src/app/analytics-node.ts`) -> Impact: **43.4** | LOC: 37
- `resolver` (@ `package/src/plugins/segmentio/context-batch.ts`) -> Impact: **27.1** | LOC: 63
- `dispatchAndEmit` (@ `package/src/app/dispatch-emit.ts`) -> Impact: **24.9** | LOC: 28
  * *Intent:* /* Dispatch function, but swallow promise rejections and use event emitter instead */
- `deregister` (@ `package/src/app/analytics-node.ts`) -> Impact: **18.8** | LOC: 15
- `_dispatch` (@ `package/src/app/analytics-node.ts`) -> Impact: **16.5** | LOC: 18
- `createBatch` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **13.7** | LOC: 15
- `resolver` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **12.8** | LOC: 16
- `flush` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **11.3** | LOC: 18
- `resolve` (@ `package/src/app/analytics-node.ts`) -> Impact: **8.8** | LOC: 6
- `resolveFailedBatch` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **7.6** | LOC: 13

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `deregister` (@ `package/src/app/analytics-node.ts`) -> **O(2^N) [Recursive]**
- `resolve` (@ `package/src/app/analytics-node.ts`) -> **O(2^N) [Recursive]**
- `register` (@ `package/src/app/analytics-node.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Records actions your users perform.
- `screen` (@ `package/src/app/event-factory.ts`) -> **O(2^N) [Recursive]**
- `resolver` (@ `package/src/plugins/segmentio/context-batch.ts`) -> **O(2^N) [Recursive]**
- `system` (@ `package/src/app/context.ts`) -> **O(2^N) [Recursive]**
- `constructor` (@ `package/src/app/analytics-node.ts`) -> **O(N^3)**
- `flush` (@ `package/src/plugins/segmentio/publisher.ts`) -> **O(N^3)**
- `resolveFailedBatch` (@ `package/src/plugins/segmentio/publisher.ts`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `resolver` (@ `package/src/plugins/segmentio/context-batch.ts`) -> DB Complexity: **15**
- `constructor` (@ `package/src/app/analytics-node.ts`) -> DB Complexity: **13**
- `createBatch` (@ `package/src/plugins/segmentio/publisher.ts`) -> DB Complexity: **10**
- `_dispatch` (@ `package/src/app/analytics-node.ts`) -> DB Complexity: **7**
- `deregister` (@ `package/src/app/analytics-node.ts`) -> DB Complexity: **3**
- `register` (@ `package/src/app/analytics-node.ts`) -> DB Complexity: **3**
  * *Intent:* /** * Records actions your users perform.
- `resolver` (@ `package/src/plugins/segmentio/publisher.ts`) -> DB Complexity: **3**
- `flush` (@ `package/src/plugins/segmentio/publisher.ts`) -> DB Complexity: **3**
- `clearBatch` (@ `package/src/plugins/segmentio/publisher.ts`) -> DB Complexity: **3**
- `constructor` (@ `package/src/plugins/segmentio/publisher.ts`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src/app` | 7 | 38.12 | 17.38% | 15.57% |
| `package/src/plugins/segmentio` | 3 | 22.16 | 47.56% | 33.59% |
| `package/src/app/types` | 4 | 6.65 | 7.11% | 0.0% |
| `package/src` | 2 | 3.5 | 4.87% | 0.0% |
| `package` | 2 | 2.32 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/app/event-queue.ts` -> **100.0%** Exposure
- `package/src/plugins/segmentio/publisher.ts` -> **69.2378%** Exposure
- `package/src/plugins/segmentio/index.ts` -> **31.5212%** Exposure
- `package/src/app/analytics-node.ts` -> **8.9792%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/plugins/segmentio/publisher.ts` -> **100.0%** Exposure
- `package/src/app/analytics-node.ts` -> **99.9993%** Exposure
- `package/src/plugins/segmentio/context-batch.ts` -> **84.9994%** Exposure
- `package/src/app/event-queue.ts` -> **83.2018%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/app/event-queue.ts` -> **0** Orphaned Functions | **2** Duplicates
- `package/src/plugins/segmentio/publisher.ts` -> **0** Orphaned Functions | **2** Duplicates
- `package/src/plugins/segmentio/index.ts` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/app/analytics-node.ts`** -> AI Confidence: **99.31%**
2. **`package/src/plugins/segmentio/publisher.ts`** -> AI Confidence: **99.31%**
3. **`package/src/app/settings.ts`** -> AI Confidence: **99.09%**
4. **`package/src/app/types/params.ts`** -> AI Confidence: **99.06%**
5. **`package/src/app/dispatch-emit.ts`** -> AI Confidence: **98.93%**
6. **`package/src/index.ts`** -> AI Confidence: **98.89%**
7. **`package/src/app/event-factory.ts`** -> AI Confidence: **98.88%**
8. **`package/src/app/types/index.ts`** -> AI Confidence: **98.88%**
9. **`package/src/app/types/plugin.ts`** -> AI Confidence: **98.88%**
10. **`package/src/app/event-queue.ts`** -> AI Confidence: **98.87%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/src/app/analytics-node.ts` -> **100.0%** Exposure
- `package/src/plugins/segmentio/publisher.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/src/app/analytics-node.ts` -> **100.0%** Exposure
- `package/src/plugins/segmentio/context-batch.ts` -> **100.0%** Exposure
- `package/src/plugins/segmentio/publisher.ts` -> **99.9999%** Exposure
- `package/src/app/event-factory.ts` -> **4.3252%** Exposure
- `package/src/app/dispatch-emit.ts` -> **1.5055%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/plugins/segmentio/publisher.ts` (TYPESCRIPT) -> Cumulative Risk: **903.34**
- **Archetype:** `file_cluster_4` (Distance: 13.453 IQR)
- **Magnitude:** 15.14 | **LOC:** 332 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `createBatch` (Impact: 13.7), `resolver` (Impact: 12.8), `flush` (Impact: 11.3)

### 2. `package/src/app/analytics-node.ts` (TYPESCRIPT) -> Cumulative Risk: **802.45**
- **Archetype:** `file_cluster_4` (Distance: 13.027 IQR)
- **Magnitude:** 29.19 | **LOC:** 351 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 43.4), `deregister` (Impact: 18.8), `_dispatch` (Impact: 16.5)

### 3. `package/src/plugins/segmentio/context-batch.ts` (TYPESCRIPT) -> Cumulative Risk: **527.13**
- **Archetype:** `file_cluster_13` (Distance: 11.462 IQR)
- **Magnitude:** 5.43 | **LOC:** 72 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (84.9994%), Safety Score (80.8925%)
- **Heaviest Functions:** `resolver` (Impact: 27.1)

### 4. `package/src/app/event-queue.ts` (TYPESCRIPT) -> Cumulative Risk: **499.43**
- **Archetype:** `file_cluster_13` (Distance: 10.697 IQR)
- **Magnitude:** 1.48 | **LOC:** 24 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (86.2356%), State Flux (83.2018%)
- **Heaviest Functions:** `getAttempts` (Impact: 5.3), `updateAttempts` (Impact: 1.9), `constructor` (Impact: 1.6)

### 5. `package/src/app/dispatch-emit.ts` (TYPESCRIPT) -> Cumulative Risk: **360.53**
- **Archetype:** `file_cluster_13` (Distance: 10.267 IQR)
- **Magnitude:** 3.59 | **LOC:** 43 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.6385%), Documentation (74.4797%), Stability (50.0%)
- **Heaviest Functions:** `dispatchAndEmit` (Impact: 24.9), `normalizeDispatchCb` (Impact: 4.2)

### 6. `package/src/plugins/segmentio/index.ts` (TYPESCRIPT) -> Cumulative Risk: **296.45**
- **Archetype:** `file_cluster_8` (Distance: 8.258 IQR)
- **Magnitude:** 1.59 | **LOC:** 67 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (50.3017%), Stability (50.0%), Concurrency (48.1936%)
- **Heaviest Functions:** `normalizeEvent` (Impact: 4.5), `createNodePlugin` (Impact: 3.0), `createConfiguredNodePlugin` (Impact: 2.2)

### 7. `package/src/app/event-factory.ts` (TYPESCRIPT) -> Cumulative Risk: **280.7**
- **Archetype:** `file_cluster_13` (Distance: 14.747 IQR)
- **Magnitude:** 0.82 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (81.6863%), Stability (50.0%), Dead Code (30.8169%)
- **Heaviest Functions:** `screen` (Impact: 5.8)

### 8. `package/src/index.common.ts` (TYPESCRIPT) -> Cumulative Risk: **268.97**
- **Archetype:** `file_cluster_8` (Distance: 6.784 IQR)
- **Magnitude:** 2.14 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9865%), Stability (50.0%), Api Exposure (11.9451%)

### 9. `package/src/app/emitter.ts` (TYPESCRIPT) -> Cumulative Risk: **237.6**
- **Archetype:** `file_cluster_13` (Distance: 8.138 IQR)
- **Magnitude:** 1.74 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (76.1906%), Stability (50.0%), Api Exposure (6.7439%)

### 10. `package/src/app/types/params.ts` (TYPESCRIPT) -> Cumulative Risk: **206.21**
- **Archetype:** `file_cluster_8` (Distance: 7.949 IQR)
- **Magnitude:** 2.52 | **LOC:** 122 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (30.8957%), Cognitive Load (13.4471%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/app/analytics-node.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.027 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.065 IQR)
- **Top Global Matches:** file_cluster_4: 13.027, file_cluster_13: 13.249, file_cluster_17: 13.487
- **Magnitude:** 29.19 | **LOC:** 351 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (55.7869%), Tech Debt (8.9792%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 43.4 | O(N^3) | DB: 13)
  * `deregister` (Impact: 18.8 | O(2^N) | DB: 3)
  * `_dispatch` (Impact: 16.5 | O(N^2) | DB: 7)
  * `resolve` (Impact: 8.8 | O(2^N) | DB: 1)
  * `register` (Impact: 5.9 | O(2^N) | DB: 3)
    * *Intent:* /** * Records actions your users perform.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 36`, `args: 30`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 106`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 6`, `concurrency: 68`, `import: 11`
* *Defense:* `safety: 25`, `doc: 12`, `immutability_locks: 18`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 61.342
  * `Choke Point (Betweenness):` 0.051471 | `Ripple Effect (Closeness):` 0.132353
  * `Imports (Out-Degree: 6):` types, analytics-core, http-client, emitter, context, event-factory, dispatch-emit, version...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/publisher.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.453 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.419 IQR)
- **Top Global Matches:** file_cluster_4: 13.453, file_cluster_13: 13.469, file_cluster_0: 13.621
- **Magnitude:** 15.14 | **LOC:** 332 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (80.1468%), Tech Debt (69.2378%)
**Top Internal Functions/Classes:**
  * `createBatch` (Impact: 13.7 | O(N^2) | DB: 10)
  * `resolver` (Impact: 12.8 | O(N^1) | DB: 3)
  * `flush` (Impact: 11.3 | O(N^3) | DB: 3)
  * `resolveFailedBatch` (Impact: 7.6 | O(N^3))
  * `clearBatch` (Impact: 3.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 25`, `args: 13`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `state_mutation: 74`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 7`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.047
  * `Choke Point (Betweenness):` 0.003676 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 3):` create-url, http-client, analytics-core, analytics-generic-utils, emitter, token-manager, types, context...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/context-batch.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.462 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.028 IQR)
- **Top Global Matches:** file_cluster_13: 11.462, file_cluster_8: 11.47, file_cluster_17: 11.531
- **Magnitude:** 5.43 | **LOC:** 72 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (55.0673%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolver` (Impact: 27.1 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 19`, `args: 11`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 45.74
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.078431
  * `Imports (Out-Degree: 1):` context, types, uuid
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/dispatch-emit.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.267 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.297 IQR)
- **Top Global Matches:** file_cluster_13: 10.267, file_cluster_8: 10.4, file_cluster_0: 10.715
- **Magnitude:** 3.59 | **LOC:** 43 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (24.8755%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dispatchAndEmit` (Impact: 24.9 | O(N^2))
    * *Intent:* /* Dispatch function, but swallow promise rejections and use event emitter instead */
  * `normalizeDispatchCb` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 16`, `args: 4`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.117647
  * `Imports (Out-Degree: 3):` types, analytics-core, emitter, context, event-queue
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/types/params.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.949 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.616 IQR)
- **Top Global Matches:** file_cluster_8: 7.949, file_cluster_7: 8.406, file_cluster_1: 8.67
- **Magnitude:** 2.52 | **LOC:** 122 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.4471%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 22`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `doc: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.common.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.784 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.004 IQR)
- **Top Global Matches:** file_cluster_8: 6.784, file_cluster_13: 6.867, file_cluster_7: 7.859
- **Magnitude:** 2.14 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.7426%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 33.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` settings, analytics-node, context, types, types, http-client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/emitter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.138 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.119 IQR)
- **Top Global Matches:** file_cluster_13: 8.138, file_cluster_16: 8.509, file_cluster_8: 8.675
- **Magnitude:** 1.74 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.3713%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 75.9
  * `Choke Point (Betweenness):` 0.011029 | `Ripple Effect (Closeness):` 0.262032
  * `Imports (Out-Degree: 2):` types, analytics-core, analytics-generic-utils, context, settings
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.258 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.61 IQR)
- **Top Global Matches:** file_cluster_8: 8.258, file_cluster_13: 8.386, file_cluster_2: 8.821
- **Magnitude:** 1.59 | **LOC:** 67 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.4658%), Tech Debt (31.5212%)
**Top Internal Functions/Classes:**
  * `normalizeEvent` (Impact: 4.5 | O(N^1))
  * `createNodePlugin` (Impact: 3.0 | O(N^1))
  * `createConfiguredNodePlugin` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 20`, `args: 7`, `func_start: 13`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 6`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 33.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` emitter, types, env, version, context, publisher
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/event-queue.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.697 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.564 IQR)
- **Top Global Matches:** file_cluster_13: 10.697, file_cluster_16: 11.194, file_cluster_0: 11.205
- **Magnitude:** 1.48 | **LOC:** 24 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (20.587%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getAttempts` (Impact: 5.3 | O(N^1))
    * *Intent:* // do not use an internal "seen" map
  * `updateAttempts` (Impact: 1.9 | O(N^1) | DB: 2)
  * `constructor` (Impact: 1.6 | O(N^1))
  * `constructor` (Impact: 1.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 54.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163399
  * `Imports (Out-Degree: 1):` context, types, analytics-core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/app/types/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.189 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.03 IQR)
- **Top Global Matches:** file_cluster_13: 7.189, file_cluster_8: 7.895, file_cluster_7: 8.783
- **Magnitude:** 1.46 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 33.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` plugin, params, segment-event
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/types/segment-event.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.291 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.448 IQR)
- **Top Global Matches:** file_cluster_13: 8.291, file_cluster_8: 8.41, file_cluster_16: 8.417
- **Magnitude:** 1.36 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 23.313 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.732 IQR)
- **Top Global Matches:** file_cluster_13: 23.313, file_cluster_9: 23.591, file_cluster_0: 23.637
- **Magnitude:** 1.36 | **LOC:** 6 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/types/plugin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.109 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 7.009 IQR)
- **Top Global Matches:** file_cluster_13: 9.109, file_cluster_16: 9.706, file_cluster_0: 9.953
- **Magnitude:** 1.31 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.047
  * `Choke Point (Betweenness):` 0.025735 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 2):` context, analytics-core, analytics-node
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.28 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.04 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/event-factory.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.747 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.217 IQR)
- **Top Global Matches:** file_cluster_13: 14.747, file_cluster_16: 14.944, file_cluster_0: 14.99
- **Magnitude:** 0.82 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.7426%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `screen` (Impact: 5.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 9`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.117647
  * `Imports (Out-Degree: 0):` get-message-id, types, analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/settings.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.158 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.236 IQR)
- **Top Global Matches:** file_cluster_13: 10.158, file_cluster_8: 10.416, file_cluster_7: 10.607
- **Magnitude:** 0.77 | **LOC:** 60 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateSettings` (Impact: 4.2 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 3`, `import: 3`
* *Defense:* `safety: 1`, `doc: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.995
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.268908
  * `Imports (Out-Degree: 0):` types, analytics-core, http-client
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/app/context.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.186 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.726 IQR)
- **Top Global Matches:** file_cluster_13: 9.186, file_cluster_16: 9.55, file_cluster_8: 9.706
- **Magnitude:** 0.53 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `system` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 220.905
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.534759
  * `Imports (Out-Degree: 0):` types, analytics-core
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/plugins/segmentio/context-batch.ts` (TYPESCRIPT) | Magnitude: 5.43 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 23, structural_boundaries: 19, args: 11
- `package/src/app/types/segment-event.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, class_start: 1, api: 1, decorators: 1
- `package/src/app/dispatch-emit.ts` (TYPESCRIPT) | Magnitude: 3.59 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 16, branch: 9, safety: 6
- `package/src/app/event-factory.ts` (TYPESCRIPT) | Magnitude: 0.82 | Delta: **0.197 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, generics: 13, func_start: 10, structural_boundaries: 9
- `package/src/app/settings.ts` (TYPESCRIPT) | Magnitude: 0.77 | Delta: **0.258 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, doc: 12, branch: 11, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/plugins/segmentio/publisher.ts` (TYPESCRIPT) | Magnitude: 15.14 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 74, branch: 35, structural_boundaries: 25
- `package/src/app/analytics-node.ts` (TYPESCRIPT) | Magnitude: 29.19 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 258, state_mutation: 106, concurrency: 68, branch: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/index.common.ts` (TYPESCRIPT) | Magnitude: 2.14 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, api: 6, import: 6
- `package/src/plugins/segmentio/index.ts` (TYPESCRIPT) | Magnitude: 1.59 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 20, func_start: 13, args: 7
- `package/src/app/types/params.ts` (TYPESCRIPT) | Magnitude: 2.52 | Delta: **0.457 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 41, branch: 31, structural_boundaries: 22, doc: 12

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/app/analytics-node.ts` -> **Severity: 5.147** (Bridge: 0.0515 * Flux: 99.9993%)
- `package/src/plugins/segmentio/publisher.ts` -> **Severity: 0.368** (Bridge: 0.0037 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/app/analytics-node.ts` -> **Severity: 9.933** (Embedded: 0.1324 * Error Risk: 75.0517%)
- `package/src/app/event-queue.ts` -> **Severity: 8.17** (Embedded: 0.1634 * Error Risk: 50.0%)
- `package/src/plugins/segmentio/context-batch.ts` -> **Severity: 6.344** (Embedded: 0.0784 * Error Risk: 80.8925%)
- `package/src/plugins/segmentio/publisher.ts` -> **Severity: 5.06** (Embedded: 0.0588 * Error Risk: 86.0271%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/app/context.ts` -> **Severity: 9701.838** (Blast Radius: 220.905 * Doc Risk: 43.9186%)
- `package/src/app/emitter.ts` -> **Severity: 5782.867** (Blast Radius: 75.9 * Doc Risk: 76.1906%)
- `package/src/app/event-queue.ts` -> **Severity: 4673.97** (Blast Radius: 54.2 * Doc Risk: 86.2356%)
- `package/src/app/event-factory.ts` -> **Severity: 3449.939** (Blast Radius: 42.234 * Doc Risk: 81.6863%)
- `package/src/index.common.ts` -> **Severity: 3353.847** (Blast Radius: 33.543 * Doc Risk: 99.9865%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
