# ARCHITECTURAL_BRIEF: express
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/express` |
| **Timestamp** | `2026-08-03T20:14:32.808837+00:00` |
| **Scan Duration** | `0.26s` |
| **Git Branch** | `master` |
| **Git Commit** | `6c4249feec8ab40631817c8e7001baf2ed022224` |
| **Git Remote** | `https://github.com/expressjs/express` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 42 malicious artifacts.

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
| Total Artifacts | 213 |
| Analyzed Artifacts (Scanned) | 79 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 134 |
| Total LOC | 1305 |
| Volatility Index | 0.025 |
| % Scanned of codebase = | 37.1% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -1.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 42 | 1004 | 53.2% |
| HTML | 24 | 256 | 30.4% |
| PLAINTEXT | 5 | 1 | 6.3% |
| MARKDOWN | 4 | 0 | 5.1% |
| CSS | 4 | 44 | 5.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.355`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 47 | 59.5% |
| file_cluster_13 | 20 | 25.3% |
| file_cluster_17 | 1 | 1.3% |
| file_cluster_4 | 1 | 1.3% |
| file_cluster_2 | 1 | 1.3% |
| Unknown | 1 | 1.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 10.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 134*

**Composition by Extension & Reason:**
- `.js`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.txt"')
- `.txt`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tmpl`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hbs`: 3x Excluded (Unsupported Extension: '.hbs')
- `.send`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 73.1 | 18.7 | 8.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 71.4 | 11.1 | 10.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 0.3 | 0.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.3 | 3.9 | 4.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 40.1 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 76.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.5 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 30.5 | 1.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 22.7 | 0.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `examples/markdown/index.js` (Hits: 8)
- `examples/error-pages/views/index.ejs` (Hits: 6)
- `examples/resource/index.js` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **redis.js** (`examples/session/redis.js`) — 2 inbound connections
2. **api_v1.js** (`examples/multi-router/controllers/api_v1.js`) — 1 inbound connections
3. **api_v2.js** (`examples/multi-router/controllers/api_v2.js`) — 1 inbound connections
4. **post.js** (`examples/route-separation/post.js`) — 1 inbound connections
5. **site.js** (`examples/route-separation/site.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`examples/route-separation/index.js`) — 8 outbound dependencies
2. **index.js** (`examples/mvc/index.js`) — 6 outbound dependencies
3. **index.js** (`examples/markdown/index.js`) — 5 outbound dependencies
4. **index.js** (`examples/auth/index.js`) — 4 outbound dependencies
5. **redis.js** (`examples/session/redis.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `range` (@ `examples/resource/index.js`) -> Impact: **52.2** | LOC: 15
- `map` (@ `examples/route-map/index.js`) -> Impact: **47.6** | LOC: 16
- `authenticate` (@ `examples/auth/index.js`) -> Impact: **10.7** | LOC: 14
- `error` (@ `examples/error/index.js`) -> Impact: **9.3** | LOC: 8
  * *Intent:* // error handling middleware have an arity of 4 // instead of the typical (req, res, next), // otherwise they behave exactly like regular // middlewar...
- `count` (@ `examples/view-locals/index.js`) -> Impact: **8.3** | LOC: 7
  * *Intent:* // this approach is cleaner, // less nesting and we have // the variables available
- `users` (@ `examples/view-locals/index.js`) -> Impact: **8.3** | LOC: 7
- `initializeRedis` (@ `examples/search/index.js`) -> Impact: **6.9** | LOC: 18
  * *Intent:* // npm install redis
- `andRestrictToSelf` (@ `examples/route-middleware/index.js`) -> Impact: **6.7** | LOC: 13
- `before` (@ `examples/mvc/controllers/user/index.js`) -> Impact: **6.6** | LOC: 12
- `loadUser` (@ `examples/route-middleware/index.js`) -> Impact: **6.5** | LOC: 10

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `range` (@ `examples/resource/index.js`) -> **O(2^N) [Recursive]**
- `map` (@ `examples/route-map/index.js`) -> **O(2^N) [Recursive]**
- `format` (@ `examples/content-negotiation/index.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // or you could write a tiny middleware like // this to add a layer of abstraction // and make things a bit more declarative:
- `json` (@ `examples/content-negotiation/index.js`) -> **O(2^N) [Recursive]**
- `json` (@ `examples/content-negotiation/users.js`) -> **O(2^N) [Recursive]**
- `error` (@ `examples/error/index.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // error handling middleware have an arity of 4 // instead of the typical (req, res, next), // otherwise they behave exactly like regular // middlewar...
- `show` (@ `examples/mvc/controllers/pet/index.js`) -> **O(2^N) [Recursive]**
- `edit` (@ `examples/mvc/controllers/pet/index.js`) -> **O(2^N) [Recursive]**
- `list` (@ `examples/mvc/controllers/user/index.js`) -> **O(2^N) [Recursive]**
- `edit` (@ `examples/mvc/controllers/user/index.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `resource` (@ `examples/resource/index.js`) -> DB Complexity: **23**
- `format` (@ `examples/content-negotiation/index.js`) -> DB Complexity: **7**
  * *Intent:* // or you could write a tiny middleware like // this to add a layer of abstraction // and make things a bit more declarative:
- `create` (@ `examples/mvc/controllers/user-pet/index.js`) -> DB Complexity: **6**
- `message` (@ `examples/mvc/index.js`) -> DB Complexity: **3**
- `next` (@ `examples/search/index.js`) -> DB Complexity: **3**
  * *Intent:* /** * GET search for :query. */
- `User` (@ `examples/view-locals/user.js`) -> DB Complexity: **3**
  * *Intent:* // faux model
- `range` (@ `examples/resource/index.js`) -> DB Complexity: **2**
- `load` (@ `examples/route-separation/user.js`) -> DB Complexity: **2**
- `authenticate` (@ `examples/auth/index.js`) -> DB Complexity: **1**
- `next` (@ `examples/auth/index.js`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 5 | 5097.38 | 1.0% | 0.0% |
| `examples/resource` | 1 | 89.7 | 49.55% | 0.0% |
| `examples/markdown` | 1 | 81.36 | 37.4% | 0.0% |
| `examples/route-map` | 1 | 79.34 | 63.45% | 0.0% |
| `examples/route-separation` | 4 | 76.04 | 23.48% | 0.0% |
| `examples/error-pages/views` | 5 | 68.78 | 5.8% | 0.0% |
| `examples/mvc` | 2 | 48.98 | 26.04% | 0.0% |
| `examples/route-separation/views/users` | 3 | 48.7 | 7.71% | 0.0% |
| `examples/content-negotiation` | 3 | 47.26 | 11.36% | 0.0% |
| `examples/session` | 2 | 46.92 | 56.65% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/route-map/index.js` -> **0** Orphaned Functions | **4** Duplicates
- `examples/content-negotiation/index.js` -> **2** Orphaned Functions | **0** Duplicates
- `examples/content-negotiation/users.js` -> **2** Orphaned Functions | **0** Duplicates
- `examples/mvc/controllers/pet/index.js` -> **2** Orphaned Functions | **0** Duplicates
- `examples/mvc/controllers/user/index.js` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`examples/cookies/index.js`** -> AI Confidence: **99.09%**
2. **`examples/route-separation/index.js`** -> AI Confidence: **99.07%**
3. **`examples/route-middleware/index.js`** -> AI Confidence: **99.06%**
4. **`examples/session/index.js`** -> AI Confidence: **99.06%**
5. **`examples/view-constructor/index.js`** -> AI Confidence: **99.0%**
6. **`examples/auth/index.js`** -> AI Confidence: **98.96%**
7. **`examples/cookie-sessions/index.js`** -> AI Confidence: **98.96%**
8. **`examples/error/index.js`** -> AI Confidence: **98.96%**
9. **`examples/mvc/index.js`** -> AI Confidence: **98.96%**
10. **`examples/resource/index.js`** -> AI Confidence: **98.96%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Algorithmic DoS Exposure
- `examples/resource/index.js` -> **22.6659%** Exposure
- `examples/content-negotiation/index.js` -> **3.9875%** Exposure
- `examples/route-map/index.js` -> **2.582%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `47` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `examples/search/index.js` (JAVASCRIPT) -> Cumulative Risk: **278.23**
- **Archetype:** `file_cluster_4` (Distance: 12.455 IQR)
- **Magnitude:** 40.88 | **LOC:** 84 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (49.9114%), Churn (17.71%)
- **Heaviest Functions:** `initializeRedis` (Impact: 6.9), `next` (Impact: 2.2)

### 2. `examples/mvc/controllers/user-pet/index.js` (JAVASCRIPT) -> Cumulative Risk: **214.6**
- **Archetype:** `file_cluster_13` (Distance: 13.154 IQR)
- **Magnitude:** 26.8 | **LOC:** 23 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (71.376%), Cognitive Load (34.4987%), Api Exposure (8.7242%)
- **Heaviest Functions:** `create` (Impact: 4.5)

### 3. `examples/resource/index.js` (JAVASCRIPT) -> Cumulative Risk: **198.19**
- **Archetype:** `file_cluster_8` (Distance: 11.08 IQR)
- **Magnitude:** 89.7 | **LOC:** 96 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (49.5456%), Safety Score (22.9465%), Algorithmic Dos (22.6659%)
- **Heaviest Functions:** `range` (Impact: 52.2), `destroy` (Impact: 4.2), `show` (Impact: 3.6)

### 4. `examples/vhost/index.js` (JAVASCRIPT) -> Cumulative Risk: **197.9**
- **Archetype:** `file_cluster_13` (Distance: 12.143 IQR)
- **Magnitude:** 34.48 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (49.4205%), Cognitive Load (45.0184%), Api Exposure (3.4594%)

### 5. `examples/cookies/index.js` (JAVASCRIPT) -> Cumulative Risk: **195.82**
- **Archetype:** `file_cluster_13` (Distance: 14.361 IQR)
- **Magnitude:** 31.64 | **LOC:** 54 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (57.083%), Safety Score (26.4354%), Dead Code (8.84%)

### 6. `examples/session/index.js` (JAVASCRIPT) -> Cumulative Risk: **194.76**
- **Archetype:** `file_cluster_8` (Distance: 10.43 IQR)
- **Magnitude:** 23.44 | **LOC:** 38 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (73.1059%), Safety Score (21.6579%)

### 7. `examples/mvc/index.js` (JAVASCRIPT) -> Cumulative Risk: **192.0**
- **Archetype:** `file_cluster_13` (Distance: 11.668 IQR)
- **Magnitude:** 22.78 | **LOC:** 96 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (47.0715%), Safety Score (41.8986%), Api Exposure (3.0303%)
- **Heaviest Functions:** `message` (Impact: 3.2)

### 8. `examples/view-locals/user.js` (JAVASCRIPT) -> Cumulative Risk: **188.05**
- **Archetype:** `file_cluster_8` (Distance: 11.158 IQR)
- **Magnitude:** 17.16 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (58.609%), Safety Score (23.3967%), Api Exposure (6.0403%)
- **Heaviest Functions:** `User` (Impact: 2.2), `all` (Impact: 1.8), `count` (Impact: 1.7)

### 9. `examples/route-map/index.js` (JAVASCRIPT) -> Cumulative Risk: **183.44**
- **Archetype:** `file_cluster_13` (Distance: 11.485 IQR)
- **Magnitude:** 79.34 | **LOC:** 76 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (63.4534%), Safety Score (14.2136%), Api Exposure (3.1914%)
- **Heaviest Functions:** `map` (Impact: 47.6), `list` (Impact: 3.6), `delete` (Impact: 3.6)

### 10. `examples/error/index.js` (JAVASCRIPT) -> Cumulative Risk: **182.8**
- **Archetype:** `file_cluster_13` (Distance: 15.889 IQR)
- **Magnitude:** 25.48 | **LOC:** 54 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (45.0184%), Safety Score (25.4798%), Dead Code (8.84%)
- **Heaviest Functions:** `error` (Impact: 9.3), `next` (Impact: 2.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/resource/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.08 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.183 IQR)
- **Top Global Matches:** file_cluster_8: 11.08, file_cluster_13: 11.371, file_cluster_15: 11.413
- **Magnitude:** 89.7 | **LOC:** 96 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (49.5456%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `range` (Impact: 52.2 | O(2^N) | DB: 2)
  * `destroy` (Impact: 4.2 | O(N^1) | DB: 1)
  * `show` (Impact: 3.6 | O(N^1))
  * `resource` (Impact: 2.4 | O(N^1) | DB: 23)
  * `index` (Impact: 1.9 | O(N^1))
    * *Intent:* // Fake controller.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 9`, `func_start: 5`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `io: 5`, `api: 1`, `import: 1`
* *Defense:* `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/markdown/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.99 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.485 IQR)
- **Top Global Matches:** file_cluster_13: 11.99, file_cluster_8: 12.614, file_cluster_11: 12.737
- **Magnitude:** 81.36 | **LOC:** 45 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (37.4015%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 8`, `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs, escape-html, marked, node:path, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/route-map/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.485 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.518 IQR)
- **Top Global Matches:** file_cluster_13: 11.485, file_cluster_8: 11.531, file_cluster_17: 11.566
- **Magnitude:** 79.34 | **LOC:** 76 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (63.4534%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `map` (Impact: 47.6 | O(2^N) | DB: 1)
  * `list` (Impact: 3.6 | O(2^N))
  * `delete` (Impact: 3.6 | O(2^N))
  * `delete` (Impact: 3.6 | O(2^N))
  * `get` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 15`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 4`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` express, escape-html
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `History.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 77.76 | **LOC:** 3888 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/search/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.455 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.582 IQR)
- **Top Global Matches:** file_cluster_4: 12.455, file_cluster_13: 12.824, file_cluster_8: 13.073
- **Magnitude:** 40.88 | **LOC:** 84 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (49.9114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initializeRedis` (Impact: 6.9 | O(N^1))
    * *Intent:* // npm install redis
  * `next` (Impact: 2.2 | O(N^1) | DB: 3)
    * *Intent:* /** * GET search for :query. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 16`, `args: 6`, `func_start: 2`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 4`, `concurrency: 21`, `import: 3`
* *Defense:* `safety: 3`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., redis, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/route-separation/user.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.805 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.918 IQR)
- **Top Global Matches:** file_cluster_8: 10.805, file_cluster_0: 10.947, file_cluster_15: 11.216
- **Magnitude:** 38.64 | **LOC:** 48 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (42.6218%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 6.5 | O(N^1) | DB: 2)
  * `update` (Impact: 3.9 | O(N^1) | DB: 1)
  * `view` (Impact: 3.8 | O(2^N))
  * `edit` (Impact: 3.8 | O(2^N))
  * `list` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`, `args: 5`, `func_start: 7`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/auth/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.597 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.244 IQR)
- **Top Global Matches:** file_cluster_13: 10.597, file_cluster_8: 10.599, file_cluster_11: 11.102
- **Magnitude:** 37.08 | **LOC:** 135 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (30.9277%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `authenticate` (Impact: 10.7 | O(N^1) | DB: 1)
  * `restrict` (Impact: 6.4 | O(N^1))
  * `next` (Impact: 1.4 | O(N^1) | DB: 1)
  * `hash` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 16`, `args: 8`, `func_start: 7`
* *Risk/State:* `state_mutation: 15`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` express-session, .., pbkdf2-password, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/mvc/controllers/user/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.34 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.629 IQR)
- **Top Global Matches:** file_cluster_8: 11.34, file_cluster_13: 11.451, file_cluster_15: 11.489
- **Magnitude:** 35.04 | **LOC:** 42 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (46.2867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `before` (Impact: 6.6 | O(N^1) | DB: 1)
  * `list` (Impact: 4.2 | O(2^N))
  * `edit` (Impact: 4.2 | O(2^N))
  * `show` (Impact: 4.2 | O(2^N))
  * `update` (Impact: 2.3 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` db
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/vhost/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.143 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.403 IQR)
- **Top Global Matches:** file_cluster_13: 12.143, file_cluster_8: 12.52, file_cluster_15: 12.648
- **Magnitude:** 34.48 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.0184%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 3`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vhost, morgan, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/cookies/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.361 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.074 IQR)
- **Top Global Matches:** file_cluster_13: 14.361, file_cluster_11: 14.558, file_cluster_0: 14.786
- **Magnitude:** 31.64 | **LOC:** 54 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (57.083%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `args: 3`
* *Risk/State:* `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., morgan, cookie-parser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/route-middleware/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.582 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.245 IQR)
- **Top Global Matches:** file_cluster_8: 10.582, file_cluster_0: 10.665, file_cluster_11: 10.72
- **Magnitude:** 27.86 | **LOC:** 91 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.4089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `andRestrictToSelf` (Impact: 6.7 | O(N^1))
  * `loadUser` (Impact: 6.5 | O(N^1) | DB: 1)
  * `andRestrictTo` (Impact: 5.6 | O(N^1))
  * `next` (Impact: 2.0 | O(N^1))
    * *Intent:* // Middleware for faux authentication // you would of course implement something real, // but this i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 6`, `args: 9`, `func_start: 10`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 2`
* *Architecture:* `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` express
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/route-separation/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.132 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.722 IQR)
- **Top Global Matches:** file_cluster_13: 10.132, file_cluster_8: 10.677, file_cluster_1: 11.087
- **Magnitude:** 27.64 | **LOC:** 56 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (41.2848%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cookie-parser, site, user, method-override, node:path, post, morgan, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/mvc/controllers/pet/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.72 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.784 IQR)
- **Top Global Matches:** file_cluster_8: 11.72, file_cluster_13: 11.732, file_cluster_15: 11.906
- **Magnitude:** 27.42 | **LOC:** 32 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (48.236%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `before` (Impact: 4.3 | O(N^1) | DB: 1)
  * `show` (Impact: 4.2 | O(2^N))
  * `edit` (Impact: 4.2 | O(2^N))
  * `update` (Impact: 2.3 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 4`, `func_start: 5`
* *Risk/State:* `state_mutation: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` db
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/mvc/controllers/user-pet/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.154 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.339 IQR)
- **Top Global Matches:** file_cluster_13: 13.154, file_cluster_8: 13.403, file_cluster_7: 13.665
- **Magnitude:** 26.8 | **LOC:** 23 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (34.4987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 4.5 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 19`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` db
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/mvc/db.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.516 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.007 IQR)
- **Top Global Matches:** file_cluster_8: 11.516, file_cluster_7: 12.093, file_cluster_13: 12.192
- **Magnitude:** 26.2 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/error/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.889 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.297 IQR)
- **Top Global Matches:** file_cluster_13: 15.889, file_cluster_11: 16.035, file_cluster_17: 16.241
- **Magnitude:** 25.48 | **LOC:** 54 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.0184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `error` (Impact: 9.3 | O(2^N))
    * *Intent:* // error handling middleware have an arity of 4 // instead of the typical (req, res, next), // other...
  * `next` (Impact: 2.7 | O(N^1))
    * *Intent:* // We can also pass exceptions to next() // The reason for process.nextTick() is to show that // nex...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., morgan
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/session/redis.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.389 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.181 IQR)
- **Top Global Matches:** file_cluster_13: 10.389, file_cluster_8: 10.711, file_cluster_1: 11.045
- **Magnitude:** 23.48 | **LOC:** 40 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (40.2005%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025641
  * `Imports (Out-Degree: 0):` morgan, .., express-session, connect-redis
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/session/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.43 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.459 IQR)
- **Top Global Matches:** file_cluster_8: 10.43, file_cluster_13: 10.463, file_cluster_1: 10.979
- **Magnitude:** 23.44 | **LOC:** 38 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 4`, `args: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., express-session
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/view-locals/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.771 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.393 IQR)
- **Top Global Matches:** file_cluster_8: 9.771, file_cluster_13: 9.922, file_cluster_17: 10.083
- **Magnitude:** 23.4 | **LOC:** 156 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.9515%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `count` (Impact: 8.3 | O(2^N))
    * *Intent:* // this approach is cleaner, // less nesting and we have // the variables available
  * `users` (Impact: 8.3 | O(2^N))
  * `ferrets` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 9`, `func_start: 5`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 3`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` user, .., node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/mvc/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.668 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.462 IQR)
- **Top Global Matches:** file_cluster_13: 11.668, file_cluster_8: 12.114, file_cluster_11: 12.391
- **Magnitude:** 22.78 | **LOC:** 96 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (47.0715%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `message` (Impact: 3.2 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 18`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` boot, express-session, method-override, node:path, morgan, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/hello-world/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.543 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.589 IQR)
- **Top Global Matches:** file_cluster_13: 11.543, file_cluster_8: 11.762, file_cluster_1: 12.09
- **Magnitude:** 22.2 | **LOC:** 16 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/error-pages/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.9%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.995 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.194 IQR)
- **Top Global Matches:** file_cluster_13: 11.995, file_cluster_8: 12.58, file_cluster_11: 12.614
- **Magnitude:** 21.32 | **LOC:** 104 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (31.123%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`, `args: 2`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 3`, `api: 1`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., morgan, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/downloads/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.256 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.202 IQR)
- **Top Global Matches:** file_cluster_13: 10.256, file_cluster_8: 10.449, file_cluster_15: 10.821
- **Magnitude:** 20.5 | **LOC:** 41 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.8072%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 3`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 3`, `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/ejs/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.621 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.512 IQR)
- **Top Global Matches:** file_cluster_13: 9.621, file_cluster_0: 9.852, file_cluster_8: 9.972
- **Magnitude:** 20.48 | **LOC:** 58 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.3358%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 4`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., ejs, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/auth/index.js` (JAVASCRIPT) | Magnitude: 37.08 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 16, state_mutation: 15, branch: 12
- `examples/route-map/index.js` (JAVASCRIPT) | Magnitude: 79.34 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 15, state_mutation: 15, branch: 9
- `examples/error/index.js` (JAVASCRIPT) | Magnitude: 25.48 | Delta: **0.146 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 9, structural_boundaries: 4, args: 4
- `examples/online/index.js` (JAVASCRIPT) | Magnitude: 8.52 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, state_mutation: 6, args: 5
- `examples/web-service/index.js` (JAVASCRIPT) | Magnitude: 9.36 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, structural_boundaries: 5, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/content-negotiation/index.js` (JAVASCRIPT) | Magnitude: 17.24 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, args: 8, structural_boundaries: 7, closures: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/search/public/client.js` (JAVASCRIPT) | Magnitude: 9.36 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 5, structural_boundaries: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/search/index.js` (JAVASCRIPT) | Magnitude: 40.88 | Delta: **0.369 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, concurrency: 21, structural_boundaries: 16, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/mvc/controllers/pet/index.js` (JAVASCRIPT) | Magnitude: 27.42 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 7, func_start: 5, api: 5
- `examples/params/index.js` (JAVASCRIPT) | Magnitude: 19.26 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 9, structural_boundaries: 8, args: 6
- `examples/session/index.js` (JAVASCRIPT) | Magnitude: 23.44 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, state_mutation: 8, branch: 4, structural_boundaries: 4
- `index.js` (JAVASCRIPT) | Magnitude: 12.04 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 1, import: 1
- `examples/route-middleware/index.js` (JAVASCRIPT) | Magnitude: 27.86 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 30, func_start: 10, args: 9, branch: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `examples/session/redis.js` -> **Severity: 0.513** (Embedded: 0.0256 * Error Risk: 19.9916%)
- `examples/multi-router/controllers/api_v1.js` -> **Severity: 0.182** (Embedded: 0.0128 * Error Risk: 14.1851%)
- `examples/multi-router/controllers/api_v2.js` -> **Severity: 0.182** (Embedded: 0.0128 * Error Risk: 14.1851%)
- `examples/route-separation/post.js` -> **Severity: 0.158** (Embedded: 0.0128 * Error Risk: 12.2871%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `index.js` -> **Severity: 19.289** (Blast Radius: 12.136 * Doc Risk: 1.5894%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
