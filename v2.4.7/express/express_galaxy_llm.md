# ARCHITECTURAL_BRIEF: express
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/express` |
| **Timestamp** | `2026-08-07T04:34:56.241103+00:00` |
| **Scan Duration** | `0.21s` |
| **Git Branch** | `master` |
| **Git Commit** | `6c4249feec8ab40631817c8e7001baf2ed022224` |
| **Git Remote** | `https://github.com/expressjs/express` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 42 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 94.9 | 40.3 | 62.2 | 0.0 |
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

- `range` (@ `examples/resource/index.js`) -> Impact: **17.9** | LOC: 15
- `map` (@ `examples/route-map/index.js`) -> Impact: **16.4** | LOC: 16
- `authenticate` (@ `examples/auth/index.js`) -> Impact: **10.7** | LOC: 14
- `next` (@ `examples/params/index.js`) -> Impact: **7.4** | LOC: 14
- `initializeRedis` (@ `examples/search/index.js`) -> Impact: **6.9** | LOC: 18
  * *Intent:* // npm install redis
- `andRestrictToSelf` (@ `examples/route-middleware/index.js`) -> Impact: **6.7** | LOC: 13
- `before` (@ `examples/mvc/controllers/user/index.js`) -> Impact: **6.6** | LOC: 12
- `loadUser` (@ `examples/route-middleware/index.js`) -> Impact: **6.5** | LOC: 10
- `load` (@ `examples/route-separation/user.js`) -> Impact: **6.5** | LOC: 11
- `restrict` (@ `examples/auth/index.js`) -> Impact: **6.4** | LOC: 8

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 5 | 5097.38 | 1.0% | 0.0% |
| `examples/markdown` | 1 | 81.36 | 37.4% | 0.0% |
| `examples/route-separation` | 4 | 73.04 | 23.48% | 0.0% |
| `examples/error-pages/views` | 5 | 68.78 | 5.8% | 0.0% |
| `examples/resource` | 1 | 55.4 | 49.55% | 0.0% |
| `examples/mvc` | 2 | 48.98 | 26.04% | 0.0% |
| `examples/route-separation/views/users` | 3 | 48.7 | 7.71% | 0.0% |
| `examples/session` | 2 | 46.92 | 56.65% | 0.0% |
| `examples/auth/views` | 3 | 46.8 | 10.02% | 0.0% |
| `examples/route-map` | 1 | 43.04 | 63.45% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/auth/index.js` -> **1** Orphaned Functions | **4** Duplicates
- `examples/route-middleware/index.js` -> **0** Orphaned Functions | **5** Duplicates
- `examples/params/index.js` -> **0** Orphaned Functions | **4** Duplicates
- `examples/route-map/index.js` -> **0** Orphaned Functions | **4** Duplicates
- `examples/content-negotiation/index.js` -> **2** Orphaned Functions | **0** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `47` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `examples/search/index.js` (JAVASCRIPT) -> Cumulative Risk: **329.45**
- **Archetype:** `file_cluster_4` (Distance: 12.455 IQR)
- **Magnitude:** 40.88 | **LOC:** 84 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Safety Score (61.3657%), Cognitive Load (49.9114%)
- **Heaviest Functions:** `initializeRedis` (Impact: 6.9), `next` (Impact: 2.2)

### 2. `examples/session/index.js` (JAVASCRIPT) -> Cumulative Risk: **251.45**
- **Archetype:** `file_cluster_8` (Distance: 10.43 IQR)
- **Magnitude:** 23.44 | **LOC:** 38 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (78.3421%), Cognitive Load (73.1059%)

### 3. `examples/cookies/index.js` (JAVASCRIPT) -> Cumulative Risk: **250.05**
- **Archetype:** `file_cluster_13` (Distance: 14.361 IQR)
- **Magnitude:** 31.64 | **LOC:** 54 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.6661%), Cognitive Load (57.083%), Dead Code (8.84%)

### 4. `examples/view-locals/user.js` (JAVASCRIPT) -> Cumulative Risk: **244.23**
- **Archetype:** `file_cluster_8` (Distance: 11.158 IQR)
- **Magnitude:** 17.16 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (79.5835%), Cognitive Load (58.609%), Api Exposure (6.0403%)
- **Heaviest Functions:** `User` (Impact: 2.2), `all` (Impact: 1.8), `count` (Impact: 1.7)

### 5. `examples/vhost/index.js` (JAVASCRIPT) -> Cumulative Risk: **238.74**
- **Archetype:** `file_cluster_13` (Distance: 12.143 IQR)
- **Magnitude:** 34.48 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (90.2632%), Cognitive Load (45.0184%), Api Exposure (3.4594%)

### 6. `examples/mvc/index.js` (JAVASCRIPT) -> Cumulative Risk: **238.18**
- **Archetype:** `file_cluster_13` (Distance: 11.668 IQR)
- **Magnitude:** 22.78 | **LOC:** 96 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (88.0754%), Cognitive Load (47.0715%), Api Exposure (3.0303%)
- **Heaviest Functions:** `message` (Impact: 3.2)

### 7. `examples/mvc/controllers/user-pet/index.js` (JAVASCRIPT) -> Cumulative Risk: **238.14**
- **Archetype:** `file_cluster_13` (Distance: 13.154 IQR)
- **Magnitude:** 26.8 | **LOC:** 23 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (94.9213%), Cognitive Load (34.4987%), Api Exposure (8.7242%)
- **Heaviest Functions:** `create` (Impact: 4.5)

### 8. `examples/error/index.js` (JAVASCRIPT) -> Cumulative Risk: **237.24**
- **Archetype:** `file_cluster_13` (Distance: 15.889 IQR)
- **Magnitude:** 21.08 | **LOC:** 54 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (79.921%), Cognitive Load (45.0184%), Dead Code (8.84%)
- **Heaviest Functions:** `error` (Impact: 4.9), `next` (Impact: 2.7)

### 9. `examples/route-map/index.js` (JAVASCRIPT) -> Cumulative Risk: **236.33**
- **Archetype:** `file_cluster_13` (Distance: 11.485 IQR)
- **Magnitude:** 43.04 | **LOC:** 76 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (69.6822%), Cognitive Load (63.4534%), Api Exposure (3.1914%)
- **Heaviest Functions:** `map` (Impact: 16.4), `list` (Impact: 1.9), `get` (Impact: 1.9)

### 10. `examples/mvc/controllers/pet/index.js` (JAVASCRIPT) -> Cumulative Risk: **235.02**
- **Archetype:** `file_cluster_8` (Distance: 11.72 IQR)
- **Magnitude:** 23.22 | **LOC:** 32 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (76.5386%), Cognitive Load (48.236%), Api Exposure (10.2489%)
- **Heaviest Functions:** `before` (Impact: 4.3), `update` (Impact: 2.3), `show` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `examples/markdown/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.99 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.485 IQR)
- **Top Global Matches:** file_cluster_13: 11.99, file_cluster_8: 12.614, file_cluster_11: 12.737
- **Magnitude:** 81.36 | **LOC:** 45 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.4015%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 8`, `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:fs, marked, node:path, escape-html
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `History.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 77.76 | **LOC:** 3888 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Magnitude:** 55.4 | **LOC:** 96 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5456%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `range` (Impact: 17.9)
  * `destroy` (Impact: 4.2)
  * `show` (Impact: 3.6)
  * `resource` (Impact: 2.4)
  * `index` (Impact: 1.9)
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

### `examples/route-map/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.485 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.518 IQR)
- **Top Global Matches:** file_cluster_13: 11.485, file_cluster_8: 11.531, file_cluster_17: 11.566
- **Magnitude:** 43.04 | **LOC:** 76 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4534%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `map` (Impact: 16.4)
  * `list` (Impact: 1.9)
  * `get` (Impact: 1.9)
  * `delete` (Impact: 1.9)
  * `list` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 15`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 4`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` escape-html, express
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/search/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.455 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.582 IQR)
- **Top Global Matches:** file_cluster_4: 12.455, file_cluster_13: 12.824, file_cluster_8: 13.073
- **Magnitude:** 40.88 | **LOC:** 84 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.9114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initializeRedis` (Impact: 6.9)
    * *Intent:* // npm install redis
  * `next` (Impact: 2.2)
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

### `examples/auth/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.556 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.926 IQR)
- **Top Global Matches:** file_cluster_13: 10.556, file_cluster_8: 10.582, file_cluster_11: 11.074
- **Magnitude:** 40.38 | **LOC:** 135 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.9277%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `authenticate` (Impact: 10.7)
  * `restrict` (Impact: 6.4)
  * `next` (Impact: 2.2)
  * `next` (Impact: 1.4)
  * `hash` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 16`, `args: 8`, `func_start: 7`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., pbkdf2-password, express-session, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/route-middleware/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.558 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.433 IQR)
- **Top Global Matches:** file_cluster_8: 10.558, file_cluster_0: 10.605, file_cluster_11: 10.681
- **Magnitude:** 37.36 | **LOC:** 91 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.4089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `andRestrictToSelf` (Impact: 6.7)
  * `loadUser` (Impact: 6.5)
  * `andRestrictTo` (Impact: 5.6)
  * `next` (Impact: 2.7)
  * `next` (Impact: 2.4)
    * *Intent:* // If our authenticated user is the user we are viewing
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 6`, `args: 9`, `func_start: 10`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` express
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/route-separation/user.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.793 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.918 IQR)
- **Top Global Matches:** file_cluster_8: 10.793, file_cluster_0: 10.935, file_cluster_15: 11.205
- **Magnitude:** 37.34 | **LOC:** 48 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.6218%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 6.5)
  * `update` (Impact: 3.9)
  * `next` (Impact: 2.3)
  * `view` (Impact: 2.0)
  * `edit` (Impact: 2.0)
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

### `examples/vhost/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.143 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.403 IQR)
- **Top Global Matches:** file_cluster_13: 12.143, file_cluster_8: 12.52, file_cluster_15: 12.648
- **Magnitude:** 34.48 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.0184%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 3`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` morgan, vhost, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/cookies/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.361 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.074 IQR)
- **Top Global Matches:** file_cluster_13: 14.361, file_cluster_11: 14.558, file_cluster_0: 14.786
- **Magnitude:** 31.64 | **LOC:** 54 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.083%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `args: 3`
* *Risk/State:* `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` morgan, .., cookie-parser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/mvc/controllers/user/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.34 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.629 IQR)
- **Top Global Matches:** file_cluster_8: 11.34, file_cluster_13: 11.451, file_cluster_15: 11.489
- **Magnitude:** 28.74 | **LOC:** 42 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.2867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `before` (Impact: 6.6)
  * `update` (Impact: 2.3)
  * `list` (Impact: 2.1)
  * `edit` (Impact: 2.1)
  * `show` (Impact: 2.1)
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

### `examples/route-separation/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.132 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.722 IQR)
- **Top Global Matches:** file_cluster_13: 10.132, file_cluster_8: 10.677, file_cluster_1: 11.087
- **Magnitude:** 27.64 | **LOC:** 56 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.2848%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` user, .., post, morgan, site, cookie-parser, method-override, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/mvc/controllers/user-pet/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.154 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.339 IQR)
- **Top Global Matches:** file_cluster_13: 13.154, file_cluster_8: 13.403, file_cluster_7: 13.665
- **Magnitude:** 26.8 | **LOC:** 23 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.4987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 4.5)
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

### `examples/params/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.858 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.048 IQR)
- **Top Global Matches:** file_cluster_8: 10.858, file_cluster_13: 10.868, file_cluster_15: 11.074
- **Magnitude:** 24.86 | **LOC:** 75 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.8754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 7.4)
  * `next` (Impact: 2.2)
  * `next` (Impact: 2.2)
  * `next` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 8`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http-errors, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/session/redis.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.389 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.181 IQR)
- **Top Global Matches:** file_cluster_13: 10.389, file_cluster_8: 10.711, file_cluster_1: 11.045
- **Magnitude:** 23.48 | **LOC:** 40 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
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

### `examples/mvc/controllers/pet/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.72 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.784 IQR)
- **Top Global Matches:** file_cluster_8: 11.72, file_cluster_13: 11.732, file_cluster_15: 11.906
- **Magnitude:** 23.22 | **LOC:** 32 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.236%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `before` (Impact: 4.3)
  * `update` (Impact: 2.3)
  * `show` (Impact: 2.1)
  * `edit` (Impact: 2.1)
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

### `examples/mvc/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.668 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.462 IQR)
- **Top Global Matches:** file_cluster_13: 11.668, file_cluster_8: 12.114, file_cluster_11: 12.391
- **Magnitude:** 22.78 | **LOC:** 96 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.0715%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `message` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 18`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., boot, express-session, morgan, method-override, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/hello-world/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.543 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.589 IQR)
- **Top Global Matches:** file_cluster_13: 11.543, file_cluster_8: 11.762, file_cluster_1: 12.09
- **Magnitude:** 22.2 | **LOC:** 16 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
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
- **Risk Profile:** Cognitive Load (31.123%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5`, `args: 2`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 3`, `api: 1`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` morgan, .., node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/error/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.889 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.297 IQR)
- **Top Global Matches:** file_cluster_13: 15.889, file_cluster_11: 16.035, file_cluster_17: 16.241
- **Magnitude:** 21.08 | **LOC:** 54 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.0184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `error` (Impact: 4.9)
    * *Intent:* // error handling middleware have an arity of 4 // instead of the typical (req, res, next), // other...
  * `next` (Impact: 2.7)
    * *Intent:* // We can also pass exceptions to next() // The reason for process.nextTick() is to show that // nex...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` morgan, ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/downloads/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.256 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.202 IQR)
- **Top Global Matches:** file_cluster_13: 10.256, file_cluster_8: 10.449, file_cluster_15: 10.821
- **Magnitude:** 20.5 | **LOC:** 41 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
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
- **Risk Profile:** Cognitive Load (15.3358%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 4`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ejs, .., node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/auth/index.js` (JAVASCRIPT) | Magnitude: 40.38 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 16, state_mutation: 15, branch: 12
- `examples/route-map/index.js` (JAVASCRIPT) | Magnitude: 43.04 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 15, state_mutation: 15, branch: 9
- `examples/error/index.js` (JAVASCRIPT) | Magnitude: 21.08 | Delta: **0.146 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 9, structural_boundaries: 4, args: 4
- `examples/online/index.js` (JAVASCRIPT) | Magnitude: 8.52 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, state_mutation: 6, args: 5
- `examples/web-service/index.js` (JAVASCRIPT) | Magnitude: 9.36 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, structural_boundaries: 5, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/content-negotiation/index.js` (JAVASCRIPT) | Magnitude: 12.64 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, args: 8, structural_boundaries: 7, closures: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/search/public/client.js` (JAVASCRIPT) | Magnitude: 9.36 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 5, structural_boundaries: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/search/index.js` (JAVASCRIPT) | Magnitude: 40.88 | Delta: **0.369 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, concurrency: 21, structural_boundaries: 16, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/params/index.js` (JAVASCRIPT) | Magnitude: 24.86 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 9, structural_boundaries: 8, args: 6
- `examples/mvc/controllers/pet/index.js` (JAVASCRIPT) | Magnitude: 23.22 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 7, func_start: 5, api: 5
- `examples/session/index.js` (JAVASCRIPT) | Magnitude: 23.44 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, state_mutation: 8, branch: 4, structural_boundaries: 4
- `index.js` (JAVASCRIPT) | Magnitude: 12.04 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 1, import: 1
- `examples/route-middleware/index.js` (JAVASCRIPT) | Magnitude: 37.36 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 30, func_start: 10, args: 9, branch: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `examples/session/redis.js` -> **Severity: 1.972** (Embedded: 0.0256 * Error Risk: 76.9252%)
- `examples/multi-router/controllers/api_v1.js` -> **Severity: 0.912** (Embedded: 0.0128 * Error Risk: 71.095%)
- `examples/multi-router/controllers/api_v2.js` -> **Severity: 0.912** (Embedded: 0.0128 * Error Risk: 71.095%)
- `examples/route-separation/post.js` -> **Severity: 0.878** (Embedded: 0.0128 * Error Risk: 68.4788%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `index.js` -> **Severity: 19.289** (Blast Radius: 12.136 * Doc Risk: 1.5894%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
