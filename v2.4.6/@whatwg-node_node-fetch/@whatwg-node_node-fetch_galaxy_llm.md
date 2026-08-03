# ARCHITECTURAL_BRIEF: @whatwg-node_node-fetch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@whatwg-node_node-fetch` |
| **Timestamp** | `2026-08-03T21:11:17.815076+00:00` |
| **Scan Duration** | `0.28s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 92 malicious artifacts.

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
| Total Artifacts | 94 |
| Analyzed Artifacts (Scanned) | 94 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 4892 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | JAVASCRIPT |

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
| JAVASCRIPT | 46 | 4092 | 48.9% |
| TYPESCRIPT | 46 | 800 | 48.9% |
| PLAINTEXT | 2 | 0 | 2.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.572`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 39 | 41.5% |
| file_cluster_8 | 31 | 33.0% |
| file_cluster_16 | 12 | 12.8% |
| file_cluster_4 | 4 | 4.3% |
| file_cluster_2 | 4 | 4.3% |
| file_cluster_0 | 2 | 2.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 4.0 | 100.0 | 34.3 | 20.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 95.4 | 35.7 | 24.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 27.4 | 2.4 | 80.0 |
| API Exposure | 2.1 | 19.7 | 7.1 | 5.9 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.1 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 83.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 100.0 | 74.3 | 91.1 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 37.3 | 0.7 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 31.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cjs/Request.js` (Hits: 5)
- `package/cjs/fetch.js` (Hits: 5)
- `package/esm/Request.js` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AbortError.js** (`package/cjs/AbortError.js`) — 0 inbound connections
2. **Blob.js** (`package/cjs/Blob.js`) — 0 inbound connections
3. **Body.js** (`package/cjs/Body.js`) — 0 inbound connections
4. **CompressionStream.js** (`package/cjs/CompressionStream.js`) — 0 inbound connections
5. **DecompressionStream.js** (`package/cjs/DecompressionStream.js`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/cjs/index.js`) — 18 outbound dependencies
2. **index.js** (`package/esm/index.js`) — 18 outbound dependencies
3. **index.d.cts** (`package/typings/index.d.cts`) — 18 outbound dependencies
4. **index.d.ts** (`package/typings/index.d.ts`) — 18 outbound dependencies
5. **fetchNodeHttp.js** (`package/cjs/fetchNodeHttp.js`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fetchNodeHttp` (@ `package/cjs/fetchNodeHttp.js`) -> Impact: **673.5** | LOC: 133
- `fetchNodeHttp` (@ `package/esm/fetchNodeHttp.js`) -> Impact: **600.7** | LOC: 133
- `fetchCurl` (@ `package/cjs/fetchCurl.js`) -> Impact: **255.2** | LOC: 134
- `fetchCurl` (@ `package/esm/fetchCurl.js`) -> Impact: **255.2** | LOC: 134
- `constructor` (@ `package/cjs/Request.js`) -> Impact: **237.0** | LOC: 64
- `constructor` (@ `package/esm/Request.js`) -> Impact: **237.0** | LOC: 64
- `json` (@ `package/cjs/Response.js`) -> Impact: **143.0** | LOC: 55
- `json` (@ `package/esm/Response.js`) -> Impact: **143.0** | LOC: 55
- `getMap` (@ `package/cjs/Headers.js`) -> Impact: **136.7** | LOC: 62
  * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
- `getMap` (@ `package/esm/Headers.js`) -> Impact: **136.7** | LOC: 62
  * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `fetchNodeHttp` (@ `package/cjs/fetchNodeHttp.js`) -> **O(2^N) [Recursive]**
- `fetchNodeHttp` (@ `package/esm/fetchNodeHttp.js`) -> **O(2^N) [Recursive]**
- `return` (@ `package/cjs/ReadableStream.js`) -> **O(2^N) [Recursive]**
- `throw` (@ `package/cjs/ReadableStream.js`) -> **O(2^N) [Recursive]**
- `return` (@ `package/esm/ReadableStream.js`) -> **O(2^N) [Recursive]**
- `throw` (@ `package/esm/ReadableStream.js`) -> **O(2^N) [Recursive]**
- `set` (@ `package/cjs/FormData.js`) -> **O(2^N) [Recursive]**
- `revokeObjectURL` (@ `package/cjs/URL.js`) -> **O(2^N) [Recursive]**
- `cleanup` (@ `package/cjs/utils.js`) -> **O(2^N) [Recursive]**
- `set` (@ `package/esm/FormData.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `getMap` (@ `package/cjs/Headers.js`) -> DB Complexity: **34**
  * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
- `getMap` (@ `package/esm/Headers.js`) -> DB Complexity: **34**
  * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
- `constructor` (@ `package/cjs/Request.js`) -> DB Complexity: **33**
- `constructor` (@ `package/esm/Request.js`) -> DB Complexity: **33**
- `blob` (@ `package/cjs/Body.js`) -> DB Complexity: **24**
- `blob` (@ `package/esm/Body.js`) -> DB Complexity: **24**
- `_doCollectChunksFromReadableJob` (@ `package/cjs/Body.js`) -> DB Complexity: **14**
- `_doCollectChunksFromReadableJob` (@ `package/esm/Body.js`) -> DB Complexity: **14**
- `handleContentLengthHeader` (@ `package/cjs/Body.js`) -> DB Complexity: **13**
- `handleContentLengthHeader` (@ `package/esm/Body.js`) -> DB Complexity: **13**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/cjs` | 24 | 4351.46 | 59.98% | 12.48% |
| `package/esm` | 23 | 4217.88 | 51.46% | 13.04% |
| `package/typings` | 46 | 187.76 | 11.51% | 30.74% |
| `package` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/cjs/TextEncoderDecoderStream.js` -> **100.0%** Exposure
- `package/esm/TextEncoderDecoderStream.js` -> **100.0%** Exposure
- `package/typings/ReadableStream.d.cts` -> **100.0%** Exposure
- `package/typings/ReadableStream.d.ts` -> **100.0%** Exposure
- `package/typings/utils.d.cts` -> **99.9992%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/cjs/Body.js` -> **100.0%** Exposure
- `package/cjs/Headers.js` -> **100.0%** Exposure
- `package/cjs/IteratorObject.js` -> **100.0%** Exposure
- `package/cjs/Request.js` -> **100.0%** Exposure
- `package/cjs/URL.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/typings/Blob.d.cts` -> **7** Orphaned Functions | **0** Duplicates
- `package/typings/Blob.d.ts` -> **7** Orphaned Functions | **0** Duplicates
- `package/cjs/TextEncoderDecoderStream.js` -> **0** Orphaned Functions | **4** Duplicates
- `package/esm/TextEncoderDecoderStream.js` -> **0** Orphaned Functions | **4** Duplicates
- `package/typings/ReadableStream.d.cts` -> **1** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/cjs/fetchNodeHttp.js`** -> AI Confidence: **99.39%**
2. **`package/cjs/Request.js`** -> AI Confidence: **99.34%**
3. **`package/cjs/fetchCurl.js`** -> AI Confidence: **99.34%**
4. **`package/cjs/Response.js`** -> AI Confidence: **99.32%**
5. **`package/cjs/Body.js`** -> AI Confidence: **99.31%**
6. **`package/cjs/fetch.js`** -> AI Confidence: **99.31%**
7. **`package/esm/fetchNodeHttp.js`** -> AI Confidence: **99.31%**
8. **`package/esm/Body.js`** -> AI Confidence: **99.23%**
9. **`package/esm/Request.js`** -> AI Confidence: **99.23%**
10. **`package/esm/Response.js`** -> AI Confidence: **99.2%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/cjs/Body.js` -> **100.0%** Exposure
- `package/cjs/FormData.js` -> **100.0%** Exposure
- `package/cjs/Headers.js` -> **100.0%** Exposure
- `package/cjs/IteratorObject.js` -> **100.0%** Exposure
- `package/cjs/ReadableStream.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/cjs/Body.js` -> **100.0%** Exposure
- `package/cjs/FormData.js` -> **100.0%** Exposure
- `package/cjs/Headers.js` -> **100.0%** Exposure
- `package/cjs/IteratorObject.js` -> **100.0%** Exposure
- `package/cjs/ReadableStream.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/cjs/Body.js` (JAVASCRIPT) -> Cumulative Risk: **907.81**
- **Archetype:** `file_cluster_13` (Distance: 14.004 IQR)
- **Magnitude:** 462.4 | **LOC:** 530 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleContentLengthHeader` (Impact: 51.2), `body` (Impact: 37.7), `formData` (Impact: 33.3)

### 2. `package/esm/Body.js` (JAVASCRIPT) -> Cumulative Risk: **907.68**
- **Archetype:** `file_cluster_13` (Distance: 14.015 IQR)
- **Magnitude:** 464.34 | **LOC:** 526 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleContentLengthHeader` (Impact: 51.2), `body` (Impact: 37.7), `formData` (Impact: 33.3)

### 3. `package/cjs/ReadableStream.js` (JAVASCRIPT) -> Cumulative Risk: **852.37**
- **Archetype:** `file_cluster_4` (Distance: 12.984 IQR)
- **Magnitude:** 448.98 | **LOC:** 246 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 112.3), `return` (Impact: 41.9), `throw` (Impact: 41.9)

### 4. `package/esm/ReadableStream.js` (JAVASCRIPT) -> Cumulative Risk: **850.54**
- **Archetype:** `file_cluster_4` (Distance: 13.025 IQR)
- **Magnitude:** 447.9 | **LOC:** 242 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 112.3), `return` (Impact: 41.9), `throw` (Impact: 41.9)

### 5. `package/esm/WritableStream.js` (JAVASCRIPT) -> Cumulative Risk: **821.45**
- **Archetype:** `file_cluster_4` (Distance: 12.282 IQR)
- **Magnitude:** 148.4 | **LOC:** 112 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 67.0), `getWriter` (Impact: 23.1), `close` (Impact: 11.8)

### 6. `package/cjs/WritableStream.js` (JAVASCRIPT) -> Cumulative Risk: **819.39**
- **Archetype:** `file_cluster_4` (Distance: 12.132 IQR)
- **Magnitude:** 147.48 | **LOC:** 116 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 67.0), `getWriter` (Impact: 23.1), `close` (Impact: 11.8)

### 7. `package/esm/TransformStream.js` (JAVASCRIPT) -> Cumulative Risk: **812.6**
- **Archetype:** `file_cluster_13` (Distance: 12.584 IQR)
- **Magnitude:** 107.0 | **LOC:** 76 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9983%)
- **Heaviest Functions:** `constructor` (Impact: 77.5)

### 8. `package/cjs/TransformStream.js` (JAVASCRIPT) -> Cumulative Risk: **810.86**
- **Archetype:** `file_cluster_13` (Distance: 12.388 IQR)
- **Magnitude:** 106.08 | **LOC:** 80 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9972%)
- **Heaviest Functions:** `constructor` (Impact: 77.5)

### 9. `package/cjs/Request.js` (JAVASCRIPT) -> Cumulative Risk: **810.24**
- **Archetype:** `file_cluster_13` (Distance: 14.426 IQR)
- **Magnitude:** 415.76 | **LOC:** 129 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 237.0), `url` (Impact: 17.9), `parsedUrl` (Impact: 17.9)

### 10. `package/esm/Request.js` (JAVASCRIPT) -> Cumulative Risk: **809.08**
- **Archetype:** `file_cluster_13` (Distance: 14.485 IQR)
- **Magnitude:** 414.68 | **LOC:** 125 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 237.0), `url` (Impact: 17.9), `parsedUrl` (Impact: 17.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/cjs/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.067 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.961 IQR)
- **Top Global Matches:** file_cluster_13: 10.067, file_cluster_8: 10.176, file_cluster_11: 10.556
- **Magnitude:** 704.98 | **LOC:** 156 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (36.9942%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` (Impact: 673.5 | O(2^N) | DB: 4)
  * `getRequestFnForProtocol` (Impact: 13.4 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 18`, `args: 10`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:https, node:stream, promise-helpers, URL.js, node:http, tslib, Request.js, utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.101 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.636 IQR)
- **Top Global Matches:** file_cluster_13: 10.101, file_cluster_8: 10.191, file_cluster_11: 10.604
- **Magnitude:** 632.1 | **LOC:** 152 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (31.8646%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` (Impact: 600.7 | O(2^N) | DB: 4)
  * `getRequestFnForProtocol` (Impact: 13.4 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 28`, `args: 10`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 6`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:https, node:stream, promise-helpers, URL.js, node:http, Request.js, utils.js, node:zlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Body.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.015 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.731 IQR)
- **Top Global Matches:** file_cluster_13: 14.015, file_cluster_4: 14.052, file_cluster_11: 14.131
- **Magnitude:** 464.34 | **LOC:** 526 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (82.5059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleContentLengthHeader` (Impact: 51.2 | O(N^4) | DB: 13)
  * `body` (Impact: 37.7 | O(N^6) | DB: 1)
  * `formData` (Impact: 33.3 | O(N^4) | DB: 12)
  * `_doCollectChunksFromReadableJob` (Impact: 31.7 | O(N^5) | DB: 14)
  * `blob` (Impact: 29.8 | O(N^4) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 54`, `args: 24`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 232`
* *Architecture:* `api: 5`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 14`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:stream, promise-helpers, File.js, ReadableStream.js, busboy, node:buffer, utils.js, Blob.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Body.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.004 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.907 IQR)
- **Top Global Matches:** file_cluster_13: 14.004, file_cluster_4: 14.054, file_cluster_11: 14.11
- **Magnitude:** 462.4 | **LOC:** 530 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (83.3208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleContentLengthHeader` (Impact: 51.2 | O(N^4) | DB: 13)
  * `body` (Impact: 37.7 | O(N^6) | DB: 1)
  * `formData` (Impact: 33.3 | O(N^4) | DB: 12)
  * `_doCollectChunksFromReadableJob` (Impact: 31.7 | O(N^5) | DB: 14)
  * `blob` (Impact: 29.8 | O(N^4) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 44`, `args: 24`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 230`
* *Architecture:* `api: 5`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 14`, `doc: 1`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:stream, promise-helpers, File.js, ReadableStream.js, busboy, node:buffer, utils.js, Blob.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/ReadableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.984 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.756 IQR)
- **Top Global Matches:** file_cluster_4: 12.984, file_cluster_13: 13.216, file_cluster_8: 13.249
- **Magnitude:** 448.98 | **LOC:** 246 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (92.3565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 112.3 | O(N^6) | DB: 8)
  * `return` (Impact: 41.9 | O(2^N) | DB: 2)
  * `throw` (Impact: 41.9 | O(2^N) | DB: 2)
  * `createController` (Impact: 36.7 | O(N^4) | DB: 9)
  * `getReader` (Impact: 26.7 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 71`, `args: 44`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 94`
* *Architecture:* `api: 4`, `concurrency: 32`, `import: 6`
* *Defense:* `safety: 20`, `immutability_locks: 20`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events, node:stream, promises, promise-helpers, node:buffer, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/ReadableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.025 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.689 IQR)
- **Top Global Matches:** file_cluster_4: 13.025, file_cluster_13: 13.262, file_cluster_8: 13.293
- **Magnitude:** 447.9 | **LOC:** 242 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (92.0561%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 112.3 | O(N^6) | DB: 8)
  * `return` (Impact: 41.9 | O(2^N) | DB: 2)
  * `throw` (Impact: 41.9 | O(2^N) | DB: 2)
  * `createController` (Impact: 36.7 | O(N^4) | DB: 9)
  * `getReader` (Impact: 26.7 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 78`, `args: 44`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 94`
* *Architecture:* `api: 3`, `concurrency: 32`, `import: 6`
* *Defense:* `safety: 20`, `immutability_locks: 14`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events, node:stream, promises, promise-helpers, node:buffer, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Request.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.426 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.977 IQR)
- **Top Global Matches:** file_cluster_13: 14.426, file_cluster_11: 14.644, file_cluster_8: 14.694
- **Magnitude:** 415.76 | **LOC:** 129 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (98.4162%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 237.0 | O(N^4) | DB: 33)
  * `url` (Impact: 17.9 | O(N^4) | DB: 5)
  * `parsedUrl` (Impact: 17.9 | O(N^4) | DB: 8)
  * `signal` (Impact: 10.6 | O(2^N) | DB: 2)
  * `isURL` (Impact: 3.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 13`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 117`
* *Architecture:* `io: 5`, `api: 5`, `import: 5`
* *Defense:* `safety: 26`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:https, Headers.js, URL.js, node:http, Body.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Request.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.485 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.655 IQR)
- **Top Global Matches:** file_cluster_13: 14.485, file_cluster_11: 14.733, file_cluster_17: 14.736
- **Magnitude:** 414.68 | **LOC:** 125 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (98.202%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 237.0 | O(N^4) | DB: 33)
  * `url` (Impact: 17.9 | O(N^4) | DB: 5)
  * `parsedUrl` (Impact: 17.9 | O(N^4) | DB: 8)
  * `signal` (Impact: 10.6 | O(2^N) | DB: 2)
  * `isURL` (Impact: 3.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 19`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 117`
* *Architecture:* `io: 5`, `api: 4`, `import: 5`
* *Defense:* `safety: 26`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:https, Headers.js, URL.js, node:http, Body.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Headers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.128 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.174 IQR)
- **Top Global Matches:** file_cluster_13: 14.128, file_cluster_17: 14.183, file_cluster_8: 14.2
- **Magnitude:** 309.5 | **LOC:** 310 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (82.1607%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMap` (Impact: 136.7 | O(N^6) | DB: 34)
    * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
  * `append` (Impact: 14.4 | O(N^3) | DB: 5)
  * `has` (Impact: 8.8 | O(N^3) | DB: 2)
  * `isHeadersLike` (Impact: 7.1 | O(N^1))
  * `get` (Impact: 6.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 11`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 127`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:util, IteratorObject.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Headers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.207 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.103 IQR)
- **Top Global Matches:** file_cluster_13: 14.207, file_cluster_17: 14.239, file_cluster_8: 14.288
- **Magnitude:** 308.4 | **LOC:** 305 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (80.3691%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMap` (Impact: 136.7 | O(N^6) | DB: 34)
    * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
  * `append` (Impact: 14.4 | O(N^3) | DB: 5)
  * `has` (Impact: 8.8 | O(N^3) | DB: 2)
  * `isHeadersLike` (Impact: 7.1 | O(N^1))
  * `get` (Impact: 6.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 15`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 127`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:util, IteratorObject.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Response.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.66 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.012 IQR)
- **Top Global Matches:** file_cluster_13: 12.66, file_cluster_8: 12.739, file_cluster_11: 12.931
- **Magnitude:** 296.66 | **LOC:** 109 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (87.6853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `json` (Impact: 143.0 | O(N^5) | DB: 6)
  * `constructor` (Impact: 78.6 | O(N^4) | DB: 8)
  * `redirect` (Impact: 13.5 | O(N^4))
  * `ok` (Impact: 5.3 | O(N^2) | DB: 2)
  * `error` (Impact: 3.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 10`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 42`
* *Architecture:* `io: 1`, `api: 6`, `import: 3`
* *Defense:* `safety: 14`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, Body.js, Headers.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Response.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.718 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.817 IQR)
- **Top Global Matches:** file_cluster_13: 12.718, file_cluster_8: 12.801, file_cluster_0: 13.016
- **Magnitude:** 295.58 | **LOC:** 105 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (86.3675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `json` (Impact: 143.0 | O(N^5) | DB: 6)
  * `constructor` (Impact: 78.6 | O(N^4) | DB: 8)
  * `redirect` (Impact: 13.5 | O(N^4))
  * `ok` (Impact: 5.3 | O(N^2) | DB: 2)
  * `error` (Impact: 3.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 14`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 42`
* *Architecture:* `io: 1`, `api: 5`, `import: 3`
* *Defense:* `safety: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:http, Body.js, Headers.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/fetchCurl.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.833 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.776 IQR)
- **Top Global Matches:** file_cluster_8: 10.833, file_cluster_13: 10.899, file_cluster_17: 11.16
- **Magnitude:** 269.98 | **LOC:** 140 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (23.3787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchCurl` (Impact: 255.2 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 17`, `args: 10`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 16`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:stream, promise-helpers, utils.js, node:tls, Response.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/fetchCurl.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.786 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.942 IQR)
- **Top Global Matches:** file_cluster_8: 10.786, file_cluster_13: 10.892, file_cluster_17: 11.162
- **Magnitude:** 269.04 | **LOC:** 143 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (25.2654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchCurl` (Impact: 255.2 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 11`, `args: 10`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 16`, `immutability_locks: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:stream, promise-helpers, utils.js, node:tls, Response.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/FormData.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.941 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.074 IQR)
- **Top Global Matches:** file_cluster_8: 11.941, file_cluster_13: 11.945, file_cluster_11: 12.13
- **Magnitude:** 260.58 | **LOC:** 151 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (91.4089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` (Impact: 106.3 | O(N^6) | DB: 5)
  * `set` (Impact: 16.3 | O(2^N) | DB: 2)
  * `append` (Impact: 12.6 | O(N^3) | DB: 5)
  * `getNormalizedFile` (Impact: 9.4 | O(N^2))
  * `get` (Impact: 8.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 32`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 52`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `immutability_locks: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, IteratorObject.js, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/FormData.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.982 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.001 IQR)
- **Top Global Matches:** file_cluster_13: 11.982, file_cluster_8: 11.99, file_cluster_11: 12.189
- **Magnitude:** 260.48 | **LOC:** 146 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (91.399%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` (Impact: 106.3 | O(N^6) | DB: 5)
  * `set` (Impact: 16.3 | O(2^N) | DB: 2)
  * `append` (Impact: 12.6 | O(N^3) | DB: 5)
  * `getNormalizedFile` (Impact: 9.4 | O(N^2))
  * `get` (Impact: 8.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 37`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`
* *Architecture:* `api: 6`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, IteratorObject.js, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/IteratorObject.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.788 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.036 IQR)
- **Top Global Matches:** file_cluster_13: 11.788, file_cluster_8: 11.862, file_cluster_0: 12.008
- **Magnitude:** 186.58 | **LOC:** 135 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (71.6136%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `flatMap` (Impact: 17.9 | O(N^3) | DB: 2)
  * `some` (Impact: 11.1 | O(N^4) | DB: 2)
  * `every` (Impact: 11.1 | O(N^4) | DB: 2)
  * `find` (Impact: 11.1 | O(N^4) | DB: 2)
  * `take` (Impact: 9.0 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 32`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` disposablestack, node:util, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/IteratorObject.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.826 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.976 IQR)
- **Top Global Matches:** file_cluster_13: 11.826, file_cluster_8: 11.895, file_cluster_17: 12.05
- **Magnitude:** 185.5 | **LOC:** 131 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (68.9974%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `flatMap` (Impact: 17.9 | O(N^3) | DB: 2)
  * `some` (Impact: 11.1 | O(N^4) | DB: 2)
  * `every` (Impact: 11.1 | O(N^4) | DB: 2)
  * `find` (Impact: 11.1 | O(N^4) | DB: 2)
  * `take` (Impact: 9.0 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 36`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` disposablestack, node:util, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.794 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.1 IQR)
- **Top Global Matches:** file_cluster_0: 13.794, file_cluster_13: 13.874, file_cluster_17: 13.885
- **Magnitude:** 157.0 | **LOC:** 111 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (31.6821%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cleanup` (Impact: 34.9 | O(2^N))
  * `getHeadersObj` (Impact: 16.1 | O(N^2))
  * `getSupportedFormats` (Impact: 16.1 | O(N^2) | DB: 2)
  * `defaultHeadersSerializer` (Impact: 10.9 | O(N^3) | DB: 1)
  * `shouldRedirect` (Impact: 8.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 32`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `dead_code: 2`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 16`, `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promise-helpers, node:events, node:signal, node:zlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/utils.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.365 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.986 IQR)
- **Top Global Matches:** file_cluster_0: 13.365, file_cluster_13: 13.366, file_cluster_11: 13.4
- **Magnitude:** 152.9 | **LOC:** 126 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (35.4344%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cleanup` (Impact: 34.9 | O(2^N))
  * `getSupportedFormats` (Impact: 18.7 | O(N^2) | DB: 2)
  * `getHeadersObj` (Impact: 16.1 | O(N^2))
  * `defaultHeadersSerializer` (Impact: 10.9 | O(N^3) | DB: 1)
  * `shouldRedirect` (Impact: 8.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 20`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 11`, `dead_code: 2`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `safety: 16`, `immutability_locks: 8`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events, node:signal, promise-helpers, tslib, node:zlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/WritableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.282 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.355 IQR)
- **Top Global Matches:** file_cluster_4: 12.282, file_cluster_13: 12.358, file_cluster_8: 12.429
- **Magnitude:** 148.4 | **LOC:** 112 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (73.8148%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 67.0 | O(N^6) | DB: 3)
  * `getWriter` (Impact: 23.1 | O(N^5) | DB: 1)
  * `close` (Impact: 11.8 | O(N^3) | DB: 5)
  * `abort` (Impact: 2.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 29`, `args: 23`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 8`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promise-helpers, node:events, node:stream, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/WritableStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.132 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.393 IQR)
- **Top Global Matches:** file_cluster_4: 12.132, file_cluster_13: 12.189, file_cluster_8: 12.252
- **Magnitude:** 147.48 | **LOC:** 116 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (71.704%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 67.0 | O(N^6) | DB: 3)
  * `getWriter` (Impact: 23.1 | O(N^5) | DB: 1)
  * `close` (Impact: 11.8 | O(N^3) | DB: 5)
  * `abort` (Impact: 2.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 24`, `args: 23`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `api: 4`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 12`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promise-helpers, node:events, node:stream, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/TransformStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.584 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_13: 12.584, file_cluster_8: 12.703, file_cluster_4: 12.723
- **Magnitude:** 107.0 | **LOC:** 76 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (69.8465%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 77.5 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 11`, `args: 12`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 2`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 9`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, node:stream, utils.js, WritableStream.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/TransformStream.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.388 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.636 IQR)
- **Top Global Matches:** file_cluster_13: 12.388, file_cluster_8: 12.492, file_cluster_4: 12.572
- **Magnitude:** 106.08 | **LOC:** 80 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (66.7345%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 77.5 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 6`, `args: 12`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`
* *Architecture:* `api: 3`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 9`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, node:stream, utils.js, WritableStream.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/fetch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.628 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.223 IQR)
- **Top Global Matches:** file_cluster_8: 8.628, file_cluster_13: 8.928, file_cluster_7: 9.481
- **Magnitude:** 101.44 | **LOC:** 108 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (13.6919%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fetchPonyfill` (Impact: 42.7 | O(2^N))
  * `getResponseForFile` (Impact: 31.6 | O(N^4) | DB: 12)
  * `getResponseForDataUri` (Impact: 9.8 | O(N^4))
  * `getResponseForBlob` (Impact: 7.6 | O(N^3))
  * `isURL` (Impact: 3.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 6`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fetchNodeHttp.js, URL.js, node:buffer, node:url, Request.js, utils.js, node:fs, Response.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/cjs/utils.js` (JAVASCRIPT) | Magnitude: 152.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, branch: 32, structural_boundaries: 20, args: 18
- `package/esm/utils.js` (JAVASCRIPT) | Magnitude: 157.0 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 32, branch: 31, api: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/esm/FormData.js` (JAVASCRIPT) | Magnitude: 260.48 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 52, structural_boundaries: 37, branch: 29
- `package/esm/Headers.js` (JAVASCRIPT) | Magnitude: 308.4 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 127, indent_spaces: 99, branch: 35, structural_boundaries: 15
- `package/esm/Body.js` (JAVASCRIPT) | Magnitude: 464.34 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 232, indent_spaces: 194, structural_boundaries: 54, branch: 43
- `package/esm/Blob.js` (JAVASCRIPT) | Magnitude: 75.76 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 21, branch: 20, api: 17
- `package/cjs/Body.js` (JAVASCRIPT) | Magnitude: 462.4 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 230, indent_spaces: 194, structural_boundaries: 44, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/typings/AbortError.d.cts` (TYPESCRIPT) | Magnitude: 3.77 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, func_start: 2, indent_spaces: 2
- `package/typings/AbortError.d.ts` (TYPESCRIPT) | Magnitude: 3.77 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, func_start: 2, indent_spaces: 2
- `package/typings/Response.d.cts` (TYPESCRIPT) | Magnitude: 23.44 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, branch: 8, generics: 7
- `package/typings/Response.d.ts` (TYPESCRIPT) | Magnitude: 23.44 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, branch: 8, generics: 7
- `package/typings/TransformStream.d.cts` (TYPESCRIPT) | Magnitude: 3.4 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, generics: 5, indent_spaces: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/typings/Body.d.cts` (TYPESCRIPT) | Magnitude: 1.68 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, ui_framework: 19, structural_boundaries: 16, branch: 15
- `package/typings/Body.d.ts` (TYPESCRIPT) | Magnitude: 1.68 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, ui_framework: 19, structural_boundaries: 16, branch: 15
- `package/typings/Blob.d.cts` (TYPESCRIPT) | Magnitude: 4.37 | Delta: **0.169 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 27, args: 24, func_start: 23
- `package/typings/Blob.d.ts` (TYPESCRIPT) | Magnitude: 4.37 | Delta: **0.169 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 27, args: 24, func_start: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/cjs/WritableStream.js` (JAVASCRIPT) | Magnitude: 147.48 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 25, structural_boundaries: 24, args: 23
- `package/esm/WritableStream.js` (JAVASCRIPT) | Magnitude: 148.4 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 29, state_mutation: 27, args: 23
- `package/cjs/ReadableStream.js` (JAVASCRIPT) | Magnitude: 448.98 | Delta: **0.232 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 222, state_mutation: 94, structural_boundaries: 71, branch: 49
- `package/esm/ReadableStream.js` (JAVASCRIPT) | Magnitude: 447.9 | Delta: **0.237 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 222, state_mutation: 94, structural_boundaries: 78, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/cjs/FormData.js` (JAVASCRIPT) | Magnitude: 260.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 52, structural_boundaries: 32, branch: 29
- `package/typings/URLSearchParams.d.cts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, branch: 1, args: 1
- `package/typings/URLSearchParams.d.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, branch: 1, args: 1
- `package/esm/fetchCurl.js` (JAVASCRIPT) | Magnitude: 269.98 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, branch: 40, structural_boundaries: 17, safety: 16
- `package/typings/CompressionStream.d.cts` (TYPESCRIPT) | Magnitude: 1.93 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, api: 2, indent_spaces: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/cjs/TextEncoderDecoder.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/cjs/index.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/esm/TextEncoderDecoder.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/esm/index.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/typings/index.d.cts` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
