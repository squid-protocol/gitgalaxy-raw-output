# ARCHITECTURAL_BRIEF: @segment_analytics-node
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
| Total Artifacts | 19 |
| Analyzed Artifacts (Scanned) | 18 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 874 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3246 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2254 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4265 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 16 | 874 | 88.9% |
| MARKDOWN | 1 | 0 | 5.6% |
| PLAINTEXT | 1 | 0 | 5.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 16 | 88.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 11.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 71.0 | 9.9 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 74.7 | 15.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 41.5 | 3.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 12.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 5.6 | 56.4 | 30.1 | 33.0 | 56.4 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.5 | 20.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 5.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 81.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 44.0 | 10.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2 | 1 | 0 | `package/src/app/analytics-node.ts` |
| cleanup | 2 | 1 | 0 | `package/src/plugins/segmentio/publisher.ts` |
| guards | 63 | 6 | 4 | `package/src/plugins/segmentio/publisher.ts` |
| danger | 1 | 1 | 0 | `package/src/app/settings.ts` |
| concurrency | 34 | 4 | 3 | `package/src/plugins/segmentio/publisher.ts` |
| connectivity | 65 | 16 | 7 | `package/src/app/analytics-node.ts` |
| io | 11 | 4 | 2 | `package/src/plugins/segmentio/publisher.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 7 | 1 | 0 | `package/src/plugins/segmentio/publisher.ts` |
| serialization | 2 | 2 | 0 | `package/src/plugins/segmentio/context-batch.ts` |
| regex | 1 | 1 | 0 | `package/src/plugins/segmentio/context-batch.ts` |
| events | 10 | 3 | 1 | `package/src/app/analytics-node.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 36 | 5 | 10 | `package/src/app/types/params.ts` |
| debt | 2 | 1 | 0 | `package/src/app/analytics-node.ts` |
| mutation | 114 | 10 | 9 | `package/src/plugins/segmentio/publisher.ts` |
| dead_code | 6 | 5 | 1 | `package/src/plugins/segmentio/publisher.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 2 | 2 | 0 | `package/src/plugins/segmentio/context-batch.ts` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/plugins/segmentio/publisher.ts` (Hits: 5)
- `package/src/app/analytics-node.ts` (Hits: 3)
- `package/src/app/settings.ts` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **context.ts** (`package/src/app/context.ts`) — 9 inbound connections
2. **emitter.ts** (`package/src/app/emitter.ts`) — 4 inbound connections
3. **settings.ts** (`package/src/app/settings.ts`) — 4 inbound connections
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

- `send` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **41.3** | LOC: 119
- `constructor` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **22.6** | LOC: 36
- `constructor` (@ `package/src/app/analytics-node.ts`) -> Impact: **18.8** | LOC: 37
- `enqueue` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **17.1** | LOC: 59
  * *Intent:* /** * Enqueues the context for future delivery. * @param ctx - Context containing a Segment event. * @returns a promise that resolves with the context...
- `flush` (@ `package/src/app/analytics-node.ts`) -> Impact: **12.8** | LOC: 30
  * *Intent:* /** * Call this method to flush all existing events.. * This method also waits for any event method-specific callbacks to be triggered, * and any of t...
- `dispatchAndEmit` (@ `package/src/app/dispatch-emit.ts`) -> Impact: **12.6** | LOC: 28
  * *Intent:* /* Dispatch function, but swallow promise rejections and use event emitter instead */
- `page` (@ `package/src/app/analytics-node.ts`) -> Impact: **11.5** | LOC: 22
  * *Intent:* /** * The page method lets you record page views on your website, along with optional extra information about the page being viewed. * @link https://s...
- `screen` (@ `package/src/app/analytics-node.ts`) -> Impact: **11.5** | LOC: 23
  * *Intent:* /** * Records screen views on your app, along with optional extra information * about the screen viewed by the user. * * TODO: This is not documented ...
- `flush` (@ `package/src/plugins/segmentio/publisher.ts`) -> Impact: **9.9** | LOC: 29
- `_dispatch` (@ `package/src/app/analytics-node.ts`) -> Impact: **7.8** | LOC: 18

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src/plugins/segmentio` | 3 | 249.98 | 30.17% | 13.82% |
| `package/src/app` | 7 | 233.56 | 7.02% | 1.39% |
| `package/src/app/types` | 4 | 42.5 | 3.36% | 0.0% |
| `package/src` | 2 | 35.0 | 2.56% | 0.0% |
| `package` | 2 | 2.32 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/plugins/segmentio/index.ts` -> **41.4637%** Exposure
- `package/src/app/analytics-node.ts` -> **9.7593%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/plugins/segmentio/publisher.ts` -> **99.9658%** Exposure
- `package/src/app/analytics-node.ts` -> **84.7826%** Exposure
- `package/src/plugins/segmentio/context-batch.ts` -> **34.8061%** Exposure
- `package/src/app/event-queue.ts` -> **16.7982%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
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
- **Unknown Dependencies:** `14` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/plugins/segmentio/publisher.ts` (TYPESCRIPT) -> Cumulative Risk: **678.06**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 206.74 | **LOC:** 332 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9658%), Concurrency (99.4766%), Documentation (83.3333%)
- **Heaviest Functions:** `send` (Impact: 41.3), `constructor` (Impact: 22.6), `enqueue` (Impact: 17.1)

### 2. `package/src/app/analytics-node.ts` (TYPESCRIPT) -> Cumulative Risk: **564.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 161.14 | **LOC:** 351 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.5157%), State Flux (84.7826%), Verification (80.0%)
- **Heaviest Functions:** `constructor` (Impact: 18.8), `flush` (Impact: 12.8), `page` (Impact: 11.5)

### 3. `package/src/plugins/segmentio/context-batch.ts` (TYPESCRIPT) -> Cumulative Risk: **392.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 25.98 | **LOC:** 72 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (59.3812%), Stability (50.0%)
- **Heaviest Functions:** `tryAdd` (Impact: 7.1), `constructor` (Impact: 1.6), `calculateSize` (Impact: 1.6)

### 4. `package/src/app/dispatch-emit.ts` (TYPESCRIPT) -> Cumulative Risk: **376.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 21.56 | **LOC:** 43 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (76.8525%), Stability (50.0%)
- **Heaviest Functions:** `dispatchAndEmit` (Impact: 12.6), `normalizeDispatchCb` (Impact: 3.2)

### 5. `package/src/app/event-queue.ts` (TYPESCRIPT) -> Cumulative Risk: **364.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 11.6 | **LOC:** 24 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (53.5652%), Stability (50.0%)
- **Heaviest Functions:** `getAttempts` (Impact: 4.4), `updateAttempts` (Impact: 1.6), `constructor` (Impact: 1.1)

### 6. `package/src/plugins/segmentio/index.ts` (TYPESCRIPT) -> Cumulative Risk: **357.56**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 17.26 | **LOC:** 67 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Concurrency (48.1936%)
- **Heaviest Functions:** `normalizeEvent` (Impact: 3.3), `createNodePlugin` (Impact: 2.4), `createConfiguredNodePlugin` (Impact: 2.2)

### 7. `package/src/app/event-factory.ts` (TYPESCRIPT) -> Cumulative Risk: **339.57**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 13.12 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Api Exposure (56.3522%), Stability (50.0%)
- **Heaviest Functions:** `screen` (Impact: 2.1), `onFinishedEvent` (Impact: 1.7), `page` (Impact: 1.5)

### 8. `package/src/app/context.ts` (TYPESCRIPT) -> Cumulative Risk: **293.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3.24 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Api Exposure (40.8091%)
- **Heaviest Functions:** `system` (Impact: 1.1)

### 9. `package/src/app/types/params.ts` (TYPESCRIPT) -> Cumulative Risk: **220.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1.26 | **LOC:** 122 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Api Exposure (54.4824%), Stability (50.0%), Cognitive Load (13.4471%)

### 10. `package/src/app/settings.ts` (TYPESCRIPT) -> Cumulative Risk: **191.43**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 5.52 | **LOC:** 60 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Api Exposure (35.3268%), Cognitive Load (3.7509%)
- **Heaviest Functions:** `validateSettings` (Impact: 3.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/plugins/segmentio/publisher.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 206.74 | **LOC:** 332 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.9608%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 41.3)
  * `constructor` (Impact: 22.6)
  * `enqueue` (Impact: 17.1)
    * *Intent:* /** * Enqueues the context for future delivery. * @param ctx - Context containing a Segment event. *...
  * `flush` (Impact: 9.9)
  * `createBatch` (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 39`, `args: 14`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 14`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.435
  * `Choke Point (Betweenness):` 0.003676 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 3):` context, emitter, create-url, http-client, token-manager, types, context-batch, analytics-core...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/analytics-node.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 161.14 | **LOC:** 351 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.0062%), Tech Debt (9.7593%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 18.8)
  * `flush` (Impact: 12.8)
    * *Intent:* /** * Call this method to flush all existing events.. * This method also waits for any event method-...
  * `page` (Impact: 11.5)
    * *Intent:* /** * The page method lets you record page views on your website, along with optional extra informat...
  * `screen` (Impact: 11.5)
    * *Intent:* /** * Records screen views on your app, along with optional extra information * about the screen vie...
  * `_dispatch` (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 48`, `args: 25`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 13`, `import: 11`
* *Defense:* `safety: 13`, `doc: 10`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 63.596
  * `Choke Point (Betweenness):` 0.066176 | `Ripple Effect (Closeness):` 0.156863
  * `Imports (Out-Degree: 6):` version, http-client, segmentio, context, dispatch-emit, emitter, event-factory, event-queue...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/context-batch.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 25.98 | **LOC:** 72 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.6374%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tryAdd` (Impact: 7.1)
  * `constructor` (Impact: 1.6)
  * `calculateSize` (Impact: 1.6)
  * `getEvents` (Impact: 1.2)
  * `length` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 21`, `args: 11`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.902
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.078431
  * `Imports (Out-Degree: 1):` context, types, uuid
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/dispatch-emit.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21.56 | **LOC:** 43 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1871%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dispatchAndEmit` (Impact: 12.6)
    * *Intent:* /* Dispatch function, but swallow promise rejections and use event emitter instead */
  * `normalizeDispatchCb` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 20`, `args: 4`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.738
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.13369
  * `Imports (Out-Degree: 3):` context, emitter, event-queue, types, analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.common.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21.44 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.848
  * `Choke Point (Betweenness):` 0.025735 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 3):` analytics-node, context, settings, types, http-client, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/emitter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.38 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 70.877
  * `Choke Point (Betweenness):` 0.011029 | `Ripple Effect (Closeness):` 0.268908
  * `Imports (Out-Degree: 2):` context, settings, types, analytics-core, analytics-generic-utils
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/plugins/segmentio/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.26 | **LOC:** 67 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.9144%), Tech Debt (41.4637%)
**Top Internal Functions/Classes:**
  * `normalizeEvent` (Impact: 3.3)
  * `createNodePlugin` (Impact: 2.4)
  * `createConfiguredNodePlugin` (Impact: 2.2)
  * `action` (Impact: 1.6)
  * `isLoaded` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 20`, `args: 6`, `func_start: 5`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 30.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` context, emitter, types, version, env, publisher
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/types/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 30.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` params, plugin, segment-event
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/types/segment-event.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.6 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.435
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.56 | **LOC:** 6 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1174%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 30.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/event-factory.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.12 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `screen` (Impact: 2.1)
  * `onFinishedEvent` (Impact: 1.7)
  * `page` (Impact: 1.5)
  * `constructor` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 8`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.738
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.13369
  * `Imports (Out-Degree: 0):` get-message-id, types, analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/types/plugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.435
  * `Choke Point (Betweenness):` 0.025735 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 2):` analytics-node, context, analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/app/event-queue.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 11.6 | **LOC:** 24 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1758%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getAttempts` (Impact: 4.4)
    * *Intent:* // do not use an internal "seen" map
  * `updateAttempts` (Impact: 1.6)
  * `constructor` (Impact: 1.1)
  * `constructor` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 50.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.176471
  * `Imports (Out-Degree: 1):` types, context, analytics-core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/app/settings.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.52 | **LOC:** 60 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7509%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateSettings` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 2`, `import: 3`
* *Defense:* `safety: 1`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 112.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.346021
  * `Imports (Out-Degree: 0):` http-client, types, analytics-core
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/app/context.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3.24 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `system` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 212.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.547511
  * `Imports (Out-Degree: 0):` types, analytics-core
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.28 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 30.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` settings.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/app/types/params.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1.26 | **LOC:** 122 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4471%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 22`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.435
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` analytics-core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.04 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/app/analytics-node.ts` -> **Severity: 5.611** (Bridge: 0.0662 * Flux: 84.7826%)
- `package/src/plugins/segmentio/publisher.ts` -> **Severity: 0.367** (Bridge: 0.0037 * Flux: 99.9658%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/app/event-queue.ts` -> **Severity: 9.453** (Embedded: 0.1765 * Error Risk: 53.5652%)
- `package/src/app/analytics-node.ts` -> **Severity: 8.858** (Embedded: 0.1569 * Error Risk: 56.4699%)
- `package/src/plugins/segmentio/context-batch.ts` -> **Severity: 4.657** (Embedded: 0.0784 * Error Risk: 59.3812%)
- `package/src/plugins/segmentio/publisher.ts` -> **Severity: 4.395** (Embedded: 0.0588 * Error Risk: 74.7188%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/app/context.ts` -> **Severity: 21283.1** (Blast Radius: 212.831 * Doc Risk: 100.0%)
- `package/src/app/event-queue.ts` -> **Severity: 5099.7** (Blast Radius: 50.997 * Doc Risk: 100.0%)
- `package/src/plugins/segmentio/context-batch.ts` -> **Severity: 4190.2** (Blast Radius: 41.902 * Doc Risk: 100.0%)
- `package/src/app/dispatch-emit.ts` -> **Severity: 3973.8** (Blast Radius: 39.738 * Doc Risk: 100.0%)
- `package/src/app/event-factory.ts` -> **Severity: 3973.8** (Blast Radius: 39.738 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
