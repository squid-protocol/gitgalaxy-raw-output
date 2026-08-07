# ARCHITECTURAL_BRIEF: @types_node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@types_node` |
| **Timestamp** | `2026-08-07T05:13:34.351191+00:00` |
| **Scan Duration** | `0.54s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 78 malicious artifacts.

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
| Total Artifacts | 88 |
| Analyzed Artifacts (Scanned) | 80 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 7196 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.9% |
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
| TYPESCRIPT | 78 | 7196 | 97.5% |
| MARKDOWN | 1 | 0 | 1.2% |
| PLAINTEXT | 1 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.332`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 30 | 37.5% |
| file_cluster_16 | 25 | 31.2% |
| file_cluster_13 | 14 | 17.5% |
| file_cluster_2 | 6 | 7.5% |
| file_cluster_6 | 1 | 1.2% |
| file_cluster_1 | 1 | 1.2% |
| file_cluster_0 | 1 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `.ts`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4066 LOC), 1x Excluded (Machine-Generated Source Code Signature: 151 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 76.8 | 16.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 22.3 | 12.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 48.0 | 46.9 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 4.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 9.6 | 3.2 | 2.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 47.5 | 13.2 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 91.7 | 1.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `node/https.d.ts` (Hits: 47)
- `node/process.d.ts` (Hits: 35)
- `node/cluster.d.ts` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`node/README.md`) — 0 inbound connections
2. **assert.d.ts** (`node/assert.d.ts`) — 0 inbound connections
3. **strict.d.ts** (`node/assert/strict.d.ts`) — 0 inbound connections
4. **async_hooks.d.ts** (`node/async_hooks.d.ts`) — 0 inbound connections
5. **buffer.buffer.d.ts** (`node/buffer.buffer.d.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **process.d.ts** (`node/process.d.ts`) — 111 outbound dependencies
2. **worker_threads.d.ts** (`node/worker_threads.d.ts`) — 13 outbound dependencies
3. **child_process.d.ts** (`node/child_process.d.ts`) — 10 outbound dependencies
4. **stream.d.ts** (`node/stream.d.ts`) — 10 outbound dependencies
5. **promises.d.ts** (`node/fs/promises.d.ts`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `oncreate` (@ `node/http.d.ts`) -> Impact: **75.8** | LOC: 131
- `assert` (@ `node/assert.d.ts`) -> Impact: **65.2** | LOC: 127
  * *Intent:* /** * The `node:assert` module provides a set of assertion functions for verifying * invariants. * @see [source](https://github.com/nodejs/node/blob/v...
- `removeListener` (@ `node/http2.d.ts`) -> Impact: **40.8** | LOC: 124
- `isWritable` (@ `node/stream.d.ts`) -> Impact: **38.4** | LOC: 34
  * *Intent:* * } * } * * const wordsStream = Readable.from(['text passed through', 'composed stream']).compose(splitToWords); * const words = await wordsStream.toA...
- `callback` (@ `node/tls.d.ts`) -> Impact: **30.0** | LOC: 45
  * *Intent:* /** * The name property is available only when type is 'ECDH'.
- `callback` (@ `node/readline.d.ts`) -> Impact: **25.7** | LOC: 29
- `removeListener` (@ `node/http2.d.ts`) -> Impact: **18.7** | LOC: 62
  * *Intent:* /** * Sends an additional informational `HEADERS` frame to the connected HTTP/2 peer. * @since v8.4.0
- `removeListener` (@ `node/net.d.ts`) -> Impact: **18.1** | LOC: 15
  * *Intent:* /** * Pauses the reading of data. That is, `'data'` events will not be emitted. * Useful to throttle back an upload. * @return The socket itself. */
- `removeEventListener` (@ `node/web-globals/events.d.ts`) -> Impact: **17.5** | LOC: 37
- `waitForDebugger` (@ `node/inspector.d.ts`) -> Impact: **16.9** | LOC: 27

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `node/ts5.7/compatibility` | 1 | 166.4 | 23.02% | 0.0% |
| `node` | 45 | 165.09 | 7.42% | 57.43% |
| `node/ts5.6/compatibility` | 1 | 157.8 | 23.5% | 0.0% |
| `node/web-globals` | 16 | 54.17 | 46.63% | 24.79% |
| `node/stream` | 3 | 15.79 | 26.91% | 71.69% |
| `node/ts5.6` | 3 | 6.12 | 3.01% | 0.0% |
| `node/fs` | 1 | 5.92 | 8.89% | 100.0% |
| `node/dns` | 1 | 3.29 | 8.41% | 54.16% |
| `node/path` | 2 | 3.24 | 5.0% | 0.0% |
| `node/timers` | 1 | 2.36 | 5.0% | 100.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `node/web-globals/timers.d.ts` -> **99.9999%** Exposure
- `node/timers/promises.d.ts` -> **99.9992%** Exposure
- `node/fs/promises.d.ts` -> **99.9965%** Exposure
- `node/async_hooks.d.ts` -> **99.9908%** Exposure
- `node/console.d.ts` -> **99.9447%** Exposure
### Highest State Flux (Mutation/Volatility)
- `node/web-globals/encoding.d.ts` -> **100.0%** Exposure
- `node/web-globals/fetch.d.ts` -> **100.0%** Exposure
- `node/web-globals/messaging.d.ts` -> **100.0%** Exposure
- `node/web-globals/performance.d.ts` -> **100.0%** Exposure
- `node/web-globals/storage.d.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `node/stream.d.ts` -> **6** Orphaned Functions | **6** Duplicates
- `node/stream/web.d.ts` -> **5** Orphaned Functions | **5** Duplicates
- `node/http.d.ts` -> **4** Orphaned Functions | **4** Duplicates
- `node/module.d.ts` -> **8** Orphaned Functions | **0** Duplicates
- `node/fs/promises.d.ts` -> **1** Orphaned Functions | **6** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`node/child_process.d.ts`** -> AI Confidence: **99.31%**
2. **`node/fs/promises.d.ts`** -> AI Confidence: **99.31%**
3. **`node/http.d.ts`** -> AI Confidence: **99.31%**
4. **`node/cluster.d.ts`** -> AI Confidence: **99.23%**
5. **`node/vm.d.ts`** -> AI Confidence: **99.23%**
6. **`node/http2.d.ts`** -> AI Confidence: **99.18%**
7. **`node/stream.d.ts`** -> AI Confidence: **99.18%**
8. **`node/v8.d.ts`** -> AI Confidence: **99.18%**
9. **`node/worker_threads.d.ts`** -> AI Confidence: **99.16%**
10. **`node/dgram.d.ts`** -> AI Confidence: **99.13%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `node/tls.d.ts` -> **91.7239%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `344` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `node/web-globals/messaging.d.ts` (TYPESCRIPT) -> Cumulative Risk: **533.23**
- **Archetype:** `file_cluster_16` (Distance: 12.515 IQR)
- **Magnitude:** 1.39 | **LOC:** 24 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.7148%), Safety Score (80.0%)
- **Heaviest Functions:** `structuredClone` (Impact: 3.6)

### 2. `node/stream/web.d.ts` (TYPESCRIPT) -> Cumulative Risk: **499.65**
- **Archetype:** `file_cluster_16` (Distance: 12.658 IQR)
- **Magnitude:** 13.13 | **LOC:** 297 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (96.8082%), Cognitive Load (70.0012%)
- **Heaviest Functions:** `values` (Impact: 12.7), `cancel` (Impact: 5.4), `getWriter` (Impact: 4.5)

### 3. `node/web-globals/fetch.d.ts` (TYPESCRIPT) -> Cumulative Risk: **497.73**
- **Archetype:** `file_cluster_16` (Distance: 11.867 IQR)
- **Magnitude:** 3.43 | **LOC:** 70 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (80.0%), Cognitive Load (76.8217%)
- **Heaviest Functions:** `fetch` (Impact: 4.3)

### 4. `node/web-globals/storage.d.ts` (TYPESCRIPT) -> Cumulative Risk: **474.3**
- **Archetype:** `file_cluster_16` (Distance: 13.492 IQR)
- **Magnitude:** 1.46 | **LOC:** 25 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (92.4142%), Cognitive Load (68.1856%)
- **Heaviest Functions:** `setItem` (Impact: 4.2)

### 5. `node/buffer.d.ts` (TYPESCRIPT) -> Cumulative Risk: **453.6**
- **Archetype:** `file_cluster_16` (Distance: 13.304 IQR)
- **Magnitude:** 3.95 | **LOC:** 1811 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.3012%), State Flux (88.8708%), Stability (50.0%)
- **Heaviest Functions:** `includes` (Impact: 5.7), `text` (Impact: 4.5)

### 6. `node/web-globals/timers.d.ts` (TYPESCRIPT) -> Cumulative Risk: **448.43**
- **Archetype:** `file_cluster_2` (Distance: 12.735 IQR)
- **Magnitude:** 1.74 | **LOC:** 45 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Concurrency (99.9665%), Stability (50.0%)
- **Heaviest Functions:** `callback` (Impact: 4.4), `callback` (Impact: 2.4)

### 7. `node/module.d.ts` (TYPESCRIPT) -> Cumulative Risk: **437.01**
- **Archetype:** `file_cluster_16` (Distance: 11.241 IQR)
- **Magnitude:** 8.66 | **LOC:** 758 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.4164%), Verification (80.0%), Stability (50.0%)
- **Heaviest Functions:** `wrap` (Impact: 9.6), `isBuiltin` (Impact: 8.4), `registerHooks` (Impact: 8.4)

### 8. `node/web-globals/blob.d.ts` (TYPESCRIPT) -> Cumulative Risk: **435.23**
- **Archetype:** `file_cluster_16` (Distance: 11.371 IQR)
- **Magnitude:** 13.66 | **LOC:** 24 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Safety Score (80.0%), Cognitive Load (69.4938%)

### 9. `node/web-globals/crypto.d.ts` (TYPESCRIPT) -> Cumulative Risk: **435.03**
- **Archetype:** `file_cluster_16` (Distance: 10.844 IQR)
- **Magnitude:** 1.43 | **LOC:** 40 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.994%), Safety Score (80.0%), Cognitive Load (76.6133%)
- **Heaviest Functions:** `supports` (Impact: 2.6)

### 10. `node/web-globals/performance.d.ts` (TYPESCRIPT) -> Cumulative Risk: **429.81**
- **Archetype:** `file_cluster_16` (Distance: 11.754 IQR)
- **Magnitude:** 4.07 | **LOC:** 46 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (80.0%), Cognitive Load (72.0283%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `node/ts5.7/compatibility/float16array.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.063 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.796 IQR)
- **Top Global Matches:** file_cluster_2: 12.063, file_cluster_8: 12.131, file_cluster_16: 12.154
- **Magnitude:** 166.4 | **LOC:** 73 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.0191%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 21`, `args: 38`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/ts5.6/compatibility/float16array.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.747 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.515 IQR)
- **Top Global Matches:** file_cluster_8: 11.747, file_cluster_16: 11.976, file_cluster_17: 12.16
- **Magnitude:** 157.8 | **LOC:** 72 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.4984%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 21`, `args: 34`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/http.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.084 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.184 IQR)
- **Top Global Matches:** file_cluster_16: 13.084, file_cluster_2: 13.23, file_cluster_8: 13.233
- **Magnitude:** 14.16 | **LOC:** 2189 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2031%), Tech Debt (46.232%)
**Top Internal Functions/Classes:**
  * `oncreate` (Impact: 75.8)
  * `removeListener` (Impact: 13.5)
  * `removeListener` (Impact: 12.7)
    * *Intent:* /** * Reference to the underlying socket. Usually, users will not want to access * this property. * ...
  * `setGlobalProxyFromEnv` (Impact: 4.8)
    * *Intent:* /** * Returns an array containing the unique names of the current outgoing headers. * All names are ...
  * `writeProcessing` (Impact: 4.0)
    * *Intent:* /** * The maximum number of requests socket can handle * before closing keep alive connection. * * A...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 200`, `args: 161`, `func_start: 172`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 3`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 9`, `api: 4`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 115`, `doc: 140`, `immutability_locks: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, node:buffer, node:stream, node:net, node:events, node:url, node:dns, undici-types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/stream.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.602 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.484 IQR)
- **Top Global Matches:** file_cluster_16: 12.602, file_cluster_2: 13.043, file_cluster_13: 13.098
- **Magnitude:** 14.04 | **LOC:** 1794 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0756%), Tech Debt (99.0674%)
**Top Internal Functions/Classes:**
  * `isWritable` (Impact: 38.4)
    * *Intent:* * } * } * * const wordsStream = Readable.from(['text passed through', 'composed stream']).compose(sp...
  * `Symbol.asyncIterator` (Impact: 14.6)
    * *Intent:* /** * This method allows mapping over the stream. The *fn* function will be called for every chunk i...
  * `removeListener` (Impact: 12.7)
    * *Intent:* /** * Is `true` after `'close'` has been emitted. * @since v18.0.0
  * `duplexPair` (Impact: 12.4)
    * *Intent:* /** * The `readable.setEncoding()` method sets the character encoding for * data read from the `Read...
  * `setDefaultHighWaterMark` (Impact: 7.2)
    * *Intent:* /** * The `readable.pause()` method will cause a stream in flowing mode to stop
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 253`, `args: 144`, `func_start: 130`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 3`, `planned_debt: 3`, `duplicate_logic: 6`, `orphaned_logic: 6`
* *Architecture:* `api: 5`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 92`, `doc: 86`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:http, node:buffer, node:fs, old-api-module.js, node:events, web, node:string_decoder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/web-globals/blob.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.371 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.27 IQR)
- **Top Global Matches:** file_cluster_16: 11.371, file_cluster_13: 11.762, file_cluster_8: 11.998
- **Magnitude:** 13.66 | **LOC:** 24 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4938%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 23`, `args: 2`, `func_start: 2`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/stream/web.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.658 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.777 IQR)
- **Top Global Matches:** file_cluster_16: 12.658, file_cluster_4: 12.798, file_cluster_8: 12.958
- **Magnitude:** 13.13 | **LOC:** 297 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.0012%), Tech Debt (96.8082%)
**Top Internal Functions/Classes:**
  * `values` (Impact: 12.7)
  * `cancel` (Impact: 5.4)
  * `getWriter` (Impact: 4.5)
  * `error` (Impact: 3.8)
  * `error` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 92`, `args: 39`, `func_start: 35`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 31`, `duplicate_logic: 5`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `concurrency: 43`, `import: 2`
* *Defense:* `safety: 45`, `immutability_locks: 28`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:util, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/http2.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.473 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.696 IQR)
- **Top Global Matches:** file_cluster_16: 12.473, file_cluster_8: 12.501, file_cluster_13: 12.605
- **Magnitude:** 9.71 | **LOC:** 2481 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4839%), Tech Debt (22.9464%)
**Top Internal Functions/Classes:**
  * `removeListener` (Impact: 40.8)
  * `removeListener` (Impact: 18.7)
    * *Intent:* /** * Sends an additional informational `HEADERS` frame to the connected HTTP/2 peer. * @since v8.4....
  * `connect` (Impact: 8.9)
  * `callback` (Impact: 4.2)
    * *Intent:* * * Initiates a response. When the `options.waitForTrailers` option is set, the `'wantTrailers'` eve...
  * `removeListener` (Impact: 3.9)
    * *Intent:* /** * Provides miscellaneous information about the current state of the `Http2Stream`. * * A current...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 172`, `args: 130`, `func_start: 138`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 3`, `duplicate_logic: 3`
* *Architecture:* `io: 7`, `api: 2`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 104`, `doc: 103`, `immutability_locks: 253`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, node:buffer, node:fs, node:net, node:tls, node:http2, node:events, node:url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/util.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.034 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.805 IQR)
- **Top Global Matches:** file_cluster_16: 11.034, file_cluster_8: 11.422, file_cluster_13: 11.487
- **Magnitude:** 9.54 | **LOC:** 1688 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.659%), Tech Debt (81.9409%)
**Top Internal Functions/Classes:**
  * `parseArgs` (Impact: 15.3)
    * *Intent:* /** * If `true`, `Proxy` inspection includes the target and handler objects. * @default false
  * `decode` (Impact: 9.0)
    * *Intent:* /** * The `util.format()` method returns a formatted string using the first argument * as a `printf`...
  * `styleText` (Impact: 4.9)
    * *Intent:* /** * If `true`, the output is styled with ANSI color codes. Colors are customizable.
  * `inspect` (Impact: 3.9)
  * `Symbol.iterator` (Impact: 3.1)
    * *Intent:* * // Comparing arrays * const actualArray = ['1', '2', '3']; * const expectedArray = ['1', '3', '4']...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 121`, `args: 16`, `func_start: 14`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `planned_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 17`, `doc: 34`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, node:fs, node:util, node:events, node:assert, node:process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/assert.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.74 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_8: 14.74, file_cluster_16: 14.763, file_cluster_4: 14.773
- **Magnitude:** 8.95 | **LOC:** 956 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.3222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert` (Impact: 65.2)
    * *Intent:* /** * The `node:assert` module provides a set of assertion functions for verifying * invariants. * @...
  * `partialDeepStrictEqual` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 32`, `args: 26`, `func_start: 27`, `class_start: 5`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 62`, `doc: 39`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, node:assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/module.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.241 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.046 IQR)
- **Top Global Matches:** file_cluster_16: 11.241, file_cluster_2: 11.261, file_cluster_8: 11.32
- **Magnitude:** 8.66 | **LOC:** 758 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6983%), Tech Debt (97.4164%)
**Top Internal Functions/Classes:**
  * `wrap` (Impact: 9.6)
    * *Intent:* /** * If you want to resolve `specifier` relative to a
  * `isBuiltin` (Impact: 8.4)
    * *Intent:* /** * @since v12.2.0 * @param path Filename to be used to construct the require * function. Must be ...
  * `registerHooks` (Impact: 8.4)
    * *Intent:* /** * Node.js fails to enable the compile cache. This can be caused by the lack of * permission to u...
  * `register` (Impact: 7.3)
    * *Intent:* /**
  * `findSourceMap` (Impact: 6.3)
    * *Intent:* /** * ```text * /path/to/project * ├ packages/ * ├ bar/ * ├ bar.js
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 83`, `args: 28`, `func_start: 23`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 4`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 8`, `doc: 82`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:url, node:module, node:assert, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/web-globals/streams.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.496 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.523 IQR)
- **Top Global Matches:** file_cluster_16: 11.496, file_cluster_8: 12.168, file_cluster_11: 12.328
- **Magnitude:** 6.89 | **LOC:** 116 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.1574%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 109`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 51`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/net.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.911 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.969 IQR)
- **Top Global Matches:** file_cluster_8: 13.911, file_cluster_16: 13.924, file_cluster_13: 13.952
- **Magnitude:** 6.4 | **LOC:** 953 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.8724%), Tech Debt (78.8108%)
**Top Internal Functions/Classes:**
  * `removeListener` (Impact: 18.1)
    * *Intent:* /** * Pauses the reading of data. That is, `'data'` events will not be emitted. * Useful to throttle...
  * `callback` (Impact: 16.3)
  * `isIPv6` (Impact: 10.6)
  * `callback` (Impact: 4.3)
    * *Intent:* /** * > Stability: 2 - Stable * * The `node:net` module provides an asynchronous network API for cre...
  * `toJSON` (Impact: 3.1)
    * *Intent:* /** * Opposite of `unref()`, calling `ref()` on a previously `unref`ed socket will _not_ let the pro...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 109`, `args: 91`, `func_start: 89`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 13`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 66`, `doc: 107`, `immutability_locks: 23`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:stream, node:net, node:events, node:dns
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/fs/promises.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.479 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.473 IQR)
- **Top Global Matches:** file_cluster_8: 10.479, file_cluster_13: 10.69, file_cluster_16: 10.699
- **Magnitude:** 5.92 | **LOC:** 1330 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.89%), Tech Debt (99.9965%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 10.2)
  * `opendir` (Impact: 7.2)
    * *Intent:* * const stream = fd.createReadStream(); * setTimeout(() => { * stream.close(); // This may not close...
  * `write` (Impact: 7.1)
    * *Intent:* /** * Modifies the permissions on the file. See [`chmod(2)`](http://man7.org/linux/man-pages/man2/ch...
  * `write` (Impact: 5.2)
    * *Intent:* /** * Changes the ownership of the file. A wrapper for [`chown(2)`](http://man7.org/linux/man-pages/...
  * `readFile` (Impact: 4.3)
    * *Intent:* /** * Unlike the 16 KiB default `highWaterMark` for a `stream.Readable`, the stream * returned by th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 31`, `args: 22`, `func_start: 22`, `class_start: 11`
* *Risk/State:* `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 8`, `api: 1`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 5`, `doc: 43`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:os, node:fs, node:readline, node:path, node:events, web, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/tls.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.684 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.681 IQR)
- **Top Global Matches:** file_cluster_13: 12.684, file_cluster_8: 12.704, file_cluster_16: 12.8
- **Magnitude:** 5.83 | **LOC:** 1204 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.6088%), Tech Debt (69.7059%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 30.0)
    * *Intent:* /** * The name property is available only when type is 'ECDH'.
  * `disableRenegotiation` (Impact: 12.1)
    * *Intent:* /** * The issuer certificate object. * For self-signed certificates, this may be a circular referenc...
  * `constructor` (Impact: 5.3)
    * *Intent:* /**
  * `setDefaultCACertificates` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 46`, `args: 30`, `func_start: 25`, `class_start: 13`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 15`, `doc: 86`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:fs, node:net, node:tls, node:crypto, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/url.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.127 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.808 IQR)
- **Top Global Matches:** file_cluster_8: 11.127, file_cluster_13: 11.266, file_cluster_16: 11.398
- **Magnitude:** 5.28 | **LOC:** 542 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0114%), Tech Debt (84.4986%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 10.7)
    * *Intent:* /** * The `url.format()` method returns a formatted URL string derived from `urlObject`. *
  * `revokeObjectURL` (Impact: 9.4)
    * *Intent:* * function getURL(req) { * return new URL(req.url || '/', 'https://example.com'); * } * ``` * @since...
  * `toJSON` (Impact: 6.2)
    * *Intent:* * } * ``` * * The example above assumes well-formed headers are forwarded from a reverse * proxy to ...
  * `format` (Impact: 5.7)
  * `values` (Impact: 3.1)
    * *Intent:* * query: { * page: 1, * format: 'json', * }, * }); * * // => 'https://example.com/some/path?page=1&#...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 30`, `args: 21`, `func_start: 21`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 1`, `import: 4`
* *Defense:* `safety: 8`, `doc: 9`, `test: 1`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:url, node:http, node:querystring, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/worker_threads.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.367 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.202 IQR)
- **Top Global Matches:** file_cluster_13: 13.367, file_cluster_2: 13.591, file_cluster_16: 13.592
- **Magnitude:** 5.12 | **LOC:** 718 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2001%), Tech Debt (18.1115%)
**Top Internal Functions/Classes:**
  * `postMessageToThread` (Impact: 5.8)
  * `removeEventListener` (Impact: 5.0)
    * *Intent:* * * The `import { isMainThread } from 'node:worker_threads'` variable is set to `false`. * * The `im...
  * `removeListener` (Impact: 3.8)
    * *Intent:* /**
  * `request` (Impact: 2.5)
    * *Intent:* * a built-in pair of `MessagePort` s that are already associated with each * other when the `Worker`...
  * `Symbol.asyncDispose` (Impact: 1.6)
    * *Intent:* /** @deprecated Use `import { Transferable } from "node:worker_threads"` instead. */ // TODO: remove...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 80`, `args: 61`, `func_start: 65`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 10`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 16`, `import: 10`
* *Defense:* `safety: 49`, `doc: 39`, `sync_locks: 3`, `immutability_locks: 15`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:url, node:v8, node:vm, worker_threads, some-js-parsing-library, web, node:events, node:perf_hooks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/buffer.buffer.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.063 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.724 IQR)
- **Top Global Matches:** file_cluster_2: 11.063, file_cluster_16: 11.231, file_cluster_8: 11.852
- **Magnitude:** 4.92 | **LOC:** 467 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/diagnostics_channel.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.188 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.329 IQR)
- **Top Global Matches:** file_cluster_2: 13.188, file_cluster_16: 13.3, file_cluster_13: 13.591
- **Magnitude:** 4.71 | **LOC:** 577 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.7464%), Tech Debt (97.8454%)
**Top Internal Functions/Classes:**
  * `fn` (Impact: 15.4)
    * *Intent:* /** * Check if there are active subscribers to the named channel. This is helpful if * the message y...
  * `tracingChannel` (Impact: 8.4)
    * *Intent:* /** * The `node:diagnostics_channel` module provides an API to create named channels * to report arb...
  * `fn` (Impact: 7.6)
    * *Intent:* /** * Creates a `TracingChannel` wrapper for the given `TracingChannel Channels`. If a name is given...
  * `end` (Impact: 3.2)
  * `asyncStart` (Impact: 3.2)
    * *Intent:* /** * This is the primary entry-point for anyone wanting to publish to a named * channel. It produce...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 31`, `args: 23`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 26`, `doc: 63`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:diagnostics_channel, node:async_hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/readline.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.404 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.889 IQR)
- **Top Global Matches:** file_cluster_13: 12.404, file_cluster_8: 12.499, file_cluster_7: 12.656
- **Magnitude:** 4.25 | **LOC:** 543 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.749%), Tech Debt (97.5313%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 25.7)
  * `moveCursor` (Impact: 4.7)
    * *Intent:* * being emitted. Once the `line` event has been emitted, this property will * be an empty string. * ...
  * `emitKeypressEvents` (Impact: 3.8)
    * *Intent:* /** * The current input data being processed by node. * * This can be used when collecting input fro...
  * `Symbol.asyncIterator` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 29`, `args: 18`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 11`, `doc: 41`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs, node:events, promises, node:readline, node:process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/quic.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.746 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.294 IQR)
- **Top Global Matches:** file_cluster_8: 11.746, file_cluster_7: 11.959, file_cluster_1: 12.154
- **Magnitude:** 4.19 | **LOC:** 911 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5877%), Tech Debt (97.0138%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 6.8)
    * *Intent:* /** * Specifies the congestion control algorithm that will be used. * Must be set to one of either `...
  * `constructor` (Impact: 6.0)
    * *Intent:* /** * The peer server name to target. * @since v23.8.0 */
  * `destroy` (Impact: 5.9)
    * *Intent:* * const alpn = 'foo'; * const client = await connect('123.123.123.123:8888', { alpn }); * await clie...
  * `constructor` (Impact: 3.5)
    * *Intent:* /** * Configures the endpoint to listen as a server. When a new session is initiated by * a remote p...
  * `Symbol.asyncDispose` (Impact: 3.4)
    * *Intent:* /** * Specifies the maximum number of milliseconds a TLS handshake is permitted to take * to complet...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 42`, `args: 27`, `func_start: 17`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `concurrency: 9`, `import: 3`
* *Defense:* `safety: 21`, `doc: 146`, `immutability_locks: 66`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:quic, node:buffer, node:net, web, node:crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/sqlite.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.271 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.434 IQR)
- **Top Global Matches:** file_cluster_8: 12.271, file_cluster_16: 12.401, file_cluster_7: 12.47
- **Magnitude:** 4.13 | **LOC:** 1066 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1348%), Tech Debt (98.9589%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 12.9)
    * *Intent:* /** * If `true`, the database is opened by the constructor. When * this value is `false`, the databa...
  * `setReadBigInts` (Impact: 9.4)
    * *Intent:* /** * The function to call for each row in the aggregation. The * function receives the current stat...
  * `backup` (Impact: 6.9)
    * *Intent:* /** * If `true`, integer fields are read as `BigInt`s.
  * `Symbol.dispose` (Impact: 2.9)
  * `Symbol.dispose` (Impact: 2.1)
    * *Intent:* /** * If `true`, unknown named parameters are ignored when binding. * If `false`, an exception is th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 35`, `args: 49`, `func_start: 42`, `class_start: 14`
* *Risk/State:* `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 20`, `doc: 152`, `immutability_locks: 51`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sqlite, node:sqlite, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/web-globals/performance.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.754 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.455 IQR)
- **Top Global Matches:** file_cluster_16: 11.754, file_cluster_13: 12.329, file_cluster_8: 12.394
- **Magnitude:** 4.07 | **LOC:** 46 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.0283%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 47`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 24`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:perf_hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/cluster.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.304 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 7.384 IQR)
- **Top Global Matches:** file_cluster_13: 13.304, file_cluster_4: 13.349, file_cluster_11: 13.587
- **Magnitude:** 4.04 | **LOC:** 487 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.604%), Tech Debt (95.6769%)
**Top Internal Functions/Classes:**
  * `isConnected` (Impact: 9.4)
    * *Intent:* * const numCPUs = availableParallelism(); * * if (cluster.isPrimary) { * console.log(`Primary ${proc...
  * `setupPrimary` (Impact: 7.7)
    * *Intent:* /** * All workers are created using [`child_process.fork()`](https://nodejs.org/docs/latest-v25.x/ap...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 21`, `args: 13`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `api: 2`, `concurrency: 17`, `import: 3`
* *Defense:* `safety: 9`, `doc: 30`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, node:os, node:net, node:child_process, node:events, node:cluster, node:process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/buffer.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.304 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.722 IQR)
- **Top Global Matches:** file_cluster_16: 13.304, file_cluster_13: 13.366, file_cluster_4: 13.397
- **Magnitude:** 3.95 | **LOC:** 1811 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.0033%), Tech Debt (26.7477%)
**Top Internal Functions/Classes:**
  * `includes` (Impact: 5.7)
    * *Intent:* /** * This function returns `true` if `input` contains only valid UTF-8-encoded data, * including th...
  * `text` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 26`, `args: 33`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `state_mutation: 10`, `orphaned_logic: 1`
* *Architecture:* `api: 10`, `concurrency: 8`, `import: 1`
* *Defense:* `doc: 64`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/events.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.39 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.289 IQR)
- **Top Global Matches:** file_cluster_16: 13.39, file_cluster_2: 13.785, file_cluster_13: 13.806
- **Magnitude:** 3.95 | **LOC:** 1048 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8806%), Tech Debt (99.4762%)
**Top Internal Functions/Classes:**
  * `setMaxListeners` (Impact: 10.1)
    * *Intent:* /** * The `Symbol.for('nodejs.rejection')` method is called in case a * promise rejection happens wh...
  * `emitDestroy` (Impact: 7.1)
    * *Intent:* * ```js * import { EventEmitter } from 'node:events'; * const myEmitter = new EventEmitter(); * * //...
  * `removeListener` (Impact: 3.8)
    * *Intent:* /** * Returns an array listing the events for which the emitter has registered * listeners. * * ```j...
  * `constructor` (Impact: 3.6)
  * `setMaxListeners` (Impact: 2.1)
    * *Intent:* /** * The `EventEmitter` class is defined and exposed by the `node:events` module: * * ```js * impor...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 113`, `args: 65`, `func_start: 56`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 3`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 34`, `doc: 56`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:process, node:assert, node:async_hooks, node:events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `node/timers.d.ts` (TYPESCRIPT) | Magnitude: 3.81 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 27, doc: 23, time_date_logic: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `node/domain.d.ts` (TYPESCRIPT) | Magnitude: 0.33 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 12, indent_spaces: 10, structural_boundaries: 9, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `node/tls.d.ts` (TYPESCRIPT) | Magnitude: 5.83 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 131, doc: 86, branch: 47, structural_boundaries: 46
- `node/cluster.d.ts` (TYPESCRIPT) | Magnitude: 4.04 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 63, ipc_rpc_bridges: 31, doc: 30, structural_boundaries: 21
- `node/path/posix.d.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, io: 8, indent_spaces: 4, api: 2
- `node/path/win32.d.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, io: 8, indent_spaces: 4, api: 2
- `node/readline.d.ts` (TYPESCRIPT) | Magnitude: 4.25 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, doc: 41, branch: 32, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `node/vm.d.ts` (TYPESCRIPT) | Magnitude: 0.55 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, doc: 36, structural_boundaries: 18, branch: 15
- `node/module.d.ts` (TYPESCRIPT) | Magnitude: 8.66 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 204, structural_boundaries: 83, doc: 82, branch: 36
- `node/http2.d.ts` (TYPESCRIPT) | Magnitude: 9.71 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 576, immutability_locks: 253, structural_boundaries: 172, func_start: 138
- `node/buffer.d.ts` (TYPESCRIPT) | Magnitude: 3.95 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 64, indent_spaces: 64, args: 33, func_start: 33
- `node/util/types.d.ts` (TYPESCRIPT) | Magnitude: 0.75 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 87, indent_spaces: 50, doc: 44, args: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `node/web-globals/timers.d.ts` (TYPESCRIPT) | Magnitude: 1.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 19, func_start: 10, generics: 10
- `node/ts5.7/compatibility/float16array.d.ts` (TYPESCRIPT) | Magnitude: 166.4 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 64, func_start: 45, args: 38, branch: 25
- `node/globals.typedarray.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 33, doc: 32, ui_framework: 31, generics: 31
- `node/https.d.ts` (TYPESCRIPT) | Magnitude: 1.71 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 73, io: 47, generics: 47
- `node/diagnostics_channel.d.ts` (TYPESCRIPT) | Magnitude: 4.71 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 91, doc: 63, structural_boundaries: 31, generics: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `node/compatibility/iterators.d.ts` (TYPESCRIPT) | Magnitude: 1.47 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: generics: 11, structural_boundaries: 10, indent_spaces: 5, class_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `node/ts5.6/buffer.buffer.d.ts` (TYPESCRIPT) | Magnitude: 3.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 17, indent_spaces: 9, structural_boundaries: 4, branch: 1
- `node/net.d.ts` (TYPESCRIPT) | Magnitude: 6.4 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 109, branch: 108, doc: 107
- `node/assert.d.ts` (TYPESCRIPT) | Magnitude: 8.95 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: sec_high_risk_execution: 161, indent_spaces: 99, safety: 62, doc: 39
- `node/dns/promises.d.ts` (TYPESCRIPT) | Magnitude: 3.29 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 71, sec_io: 27, immutability_locks: 24, args: 10
- `node/inspector.d.ts` (TYPESCRIPT) | Magnitude: 3.08 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, args: 44, func_start: 44, safety: 43

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `node/web-globals/timers.d.ts` -> **Severity: 593.165** (Blast Radius: 12.5 * Doc Risk: 47.4532%)
- `node/path/posix.d.ts` -> **Severity: 468.042** (Blast Radius: 12.5 * Doc Risk: 37.4434%)
- `node/path/win32.d.ts` -> **Severity: 468.042** (Blast Radius: 12.5 * Doc Risk: 37.4434%)
- `node/web-globals/blob.d.ts` -> **Severity: 364.174** (Blast Radius: 12.5 * Doc Risk: 29.1339%)
- `node/web-globals/messaging.d.ts` -> **Severity: 356.473** (Blast Radius: 12.5 * Doc Risk: 28.5178%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
