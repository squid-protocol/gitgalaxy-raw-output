# ARCHITECTURAL_BRIEF: node-cleanup
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/node-cleanup` |
| **Timestamp** | `2026-08-03T21:12:46.294144+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 7 malicious artifacts.

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
| Total Artifacts | 11 |
| Analyzed Artifacts (Scanned) | 9 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 1027 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.8% |
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
| JAVASCRIPT | 7 | 1027 | 77.8% |
| MARKDOWN | 1 | 0 | 11.1% |
| PLAINTEXT | 1 | 0 | 11.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.983`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4 | 44.4% |
| file_cluster_4 | 1 | 11.1% |
| file_cluster_13 | 1 | 11.1% |
| file_cluster_11 | 1 | 11.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 22.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.6 | 49.3 | 15.0 | 5.0 | 49.3 |
| Error & Exception Exposure | 4.9 | 71.7 | 23.2 | 5.8 | 4.9 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 1.4 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 75.5 | 19.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.0 | 14.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 34.7 | 6.6 | 0.0 | 0.0 |
| Specification Exposure | 80.0 | 100.0 | 97.1 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 11.9 | 1.7 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 74.5 | 11.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/tests/bin/groupable.js` (Hits: 4)
- `package/node-cleanup.js` (Hits: 2)
- `package/README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`package/README.md`) — 0 inbound connections
2. **node-cleanup.js** (`package/node-cleanup.js`) — 0 inbound connections
3. **grandchild.js** (`package/tests/bin/grandchild.js`) — 0 inbound connections
4. **groupable.js** (`package/tests/bin/groupable.js`) — 0 inbound connections
5. **stackable.js** (`package/tests/bin/stackable.js`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **groupable.js** (`package/tests/bin/groupable.js`) — 3 outbound dependencies
2. **multiple.js** (`package/tests/multiple.js`) — 2 outbound dependencies
3. **nocleanup.js** (`package/tests/nocleanup.js`) — 2 outbound dependencies
4. **single.js** (`package/tests/single.js`) — 2 outbound dependencies
5. **node-cleanup.js** (`package/node-cleanup.js`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `install` (@ `package/node-cleanup.js`) -> Impact: **47.0** | LOC: 40
  * *Intent:* //// MAIN /////////////////////////////////////////////////////////////////////
- `nodeCleanup` (@ `package/tests/bin/groupable.js`) -> Impact: **26.4** | LOC: 9
- `signalHandler` (@ `package/node-cleanup.js`) -> Impact: **21.5** | LOC: 15
  * *Intent:* //// HANDLERS /////////////////////////////////////////////////////////////////
- `cleanup1` (@ `package/tests/bin/stackable.js`) -> Impact: **10.7** | LOC: 6
- `nodeCleanup` (@ `package/tests/bin/stackable.js`) -> Impact: **9.3** | LOC: 7
- `exceptionHandler` (@ `package/node-cleanup.js`) -> Impact: **8.1** | LOC: 7
- `uninstall` (@ `package/node-cleanup.js`) -> Impact: **5.8** | LOC: 12
- `setTimeout` (@ `package/tests/bin/stackable.js`) -> Impact: **5.6** | LOC: 8
- `exitHandler` (@ `package/node-cleanup.js`) -> Impact: **2.9** | LOC: 6
- `setTimeout` (@ `package/tests/bin/grandchild.js`) -> Impact: **2.0** | LOC: 6

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `nodeCleanup` (@ `package/tests/bin/groupable.js`) -> **O(2^N) [Recursive]**
- `cleanup1` (@ `package/tests/bin/stackable.js`) -> **O(2^N) [Recursive]**
- `nodeCleanup` (@ `package/tests/bin/stackable.js`) -> **O(2^N) [Recursive]**
- `install` (@ `package/node-cleanup.js`) -> **O(N^3)**
  * *Intent:* //// MAIN /////////////////////////////////////////////////////////////////////
- `signalHandler` (@ `package/node-cleanup.js`) -> **O(N^3)**
  * *Intent:* //// HANDLERS /////////////////////////////////////////////////////////////////

### Highest Data Gravity (Database Complexity)
- `install` (@ `package/node-cleanup.js`) -> DB Complexity: **2**
  * *Intent:* //// MAIN /////////////////////////////////////////////////////////////////////
- `signalHandler` (@ `package/node-cleanup.js`) -> DB Complexity: **1**
  * *Intent:* //// HANDLERS /////////////////////////////////////////////////////////////////
- `nodeCleanup` (@ `package/tests/bin/groupable.js`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package` | 3 | 114.5 | 16.43% | 0.0% |
| `package/tests/bin` | 3 | 79.16 | 15.94% | 0.0% |
| `package/tests` | 3 | 68.16 | 2.69% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest State Flux (Mutation/Volatility)
- `package/node-cleanup.js` -> **98.9716%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/tests/bin/grandchild.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/tests/bin/stackable.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/node-cleanup.js`** -> AI Confidence: **99.17%**
2. **`package/tests/bin/stackable.js`** -> AI Confidence: **99.17%**
3. **`package/tests/multiple.js`** -> AI Confidence: **99.06%**
4. **`package/tests/nocleanup.js`** -> AI Confidence: **99.06%**
5. **`package/tests/bin/groupable.js`** -> AI Confidence: **98.89%**
6. **`package/tests/bin/grandchild.js`** -> AI Confidence: **98.85%**
7. **`package/tests/single.js`** -> AI Confidence: **98.85%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/node-cleanup.js` -> **0.0888%** Exposure
### Algorithmic DoS Exposure
- `package/node-cleanup.js` -> **74.5492%** Exposure
- `package/tests/bin/stackable.js` -> **1.2966%** Exposure
- `package/tests/bin/groupable.js` -> **1.2222%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/node-cleanup.js` (JAVASCRIPT) -> Cumulative Risk: **471.1**
- **Archetype:** `file_cluster_8` (Distance: 11.707 IQR)
- **Magnitude:** 109.42 | **LOC:** 149 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.9716%), Verification (80.0%), Algorithmic Dos (74.5492%)
- **Heaviest Functions:** `install` (Impact: 47.0), `signalHandler` (Impact: 21.5), `exceptionHandler` (Impact: 8.1)

### 2. `package/tests/bin/stackable.js` (JAVASCRIPT) -> Cumulative Risk: **331.42**
- **Archetype:** `file_cluster_11` (Distance: 16.681 IQR)
- **Magnitude:** 31.18 | **LOC:** 76 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (75.4538%), Stability (50.0%), Safety Score (47.2414%)
- **Heaviest Functions:** `cleanup1` (Impact: 10.7), `nodeCleanup` (Impact: 9.3), `setTimeout` (Impact: 5.6)

### 3. `package/tests/bin/grandchild.js` (JAVASCRIPT) -> Cumulative Risk: **264.65**
- **Archetype:** `file_cluster_4` (Distance: 13.624 IQR)
- **Magnitude:** 9.24 | **LOC:** 24 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (80.0%), Safety Score (71.6667%), Concurrency (57.9851%), Stability (50.0%)
- **Heaviest Functions:** `setTimeout` (Impact: 2.0)

### 4. `package/tests/bin/groupable.js` (JAVASCRIPT) -> Cumulative Risk: **205.01**
- **Archetype:** `file_cluster_13` (Distance: 18.051 IQR)
- **Magnitude:** 38.74 | **LOC:** 93 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (22.0974%), Cognitive Load (20.1011%)
- **Heaviest Functions:** `nodeCleanup` (Impact: 26.4)

### 5. `package/tests/nocleanup.js` (JAVASCRIPT) -> Cumulative Risk: **158.63**
- **Archetype:** `file_cluster_8` (Distance: 7.62 IQR)
- **Magnitude:** 20.14 | **LOC:** 176 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (5.7508%), Cognitive Load (2.8766%)

### 6. `package/tests/multiple.js` (JAVASCRIPT) -> Cumulative Risk: **157.82**
- **Archetype:** `file_cluster_8` (Distance: 7.818 IQR)
- **Magnitude:** 23.66 | **LOC:** 359 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (5.2252%), Cognitive Load (2.598%)

### 7. `package/tests/single.js` (JAVASCRIPT) -> Cumulative Risk: **157.78**
- **Archetype:** `file_cluster_8` (Distance: 7.645 IQR)
- **Magnitude:** 24.36 | **LOC:** 400 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (5.1798%), Cognitive Load (2.6023%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/node-cleanup.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.707 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.711 IQR)
- **Top Global Matches:** file_cluster_8: 11.707, file_cluster_0: 11.921, file_cluster_17: 11.939
- **Magnitude:** 109.42 | **LOC:** 149 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (49.2861%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `install` (Impact: 47.0 | O(N^3) | DB: 2)
    * *Intent:* //// MAIN /////////////////////////////////////////////////////////////////////
  * `signalHandler` (Impact: 21.5 | O(N^3) | DB: 1)
    * *Intent:* //// HANDLERS /////////////////////////////////////////////////////////////////
  * `exceptionHandler` (Impact: 8.1 | O(N^2))
  * `uninstall` (Impact: 5.8 | O(N^2))
  * `exitHandler` (Impact: 2.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 10`, `args: 8`, `func_start: 14`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node-cleanup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tests/bin/groupable.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 18.051 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 6.098 IQR)
- **Top Global Matches:** file_cluster_13: 18.051, file_cluster_11: 18.133, file_cluster_17: 18.243
- **Magnitude:** 38.74 | **LOC:** 93 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.1011%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `nodeCleanup` (Impact: 26.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `io: 4`, `import: 3`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., path, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tests/bin/stackable.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.681 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.705 IQR)
- **Top Global Matches:** file_cluster_11: 16.681, file_cluster_13: 16.685, file_cluster_4: 16.69
- **Magnitude:** 31.18 | **LOC:** 76 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.7089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cleanup1` (Impact: 10.7 | O(2^N))
  * `nodeCleanup` (Impact: 9.3 | O(2^N))
  * `setTimeout` (Impact: 5.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 3`, `args: 2`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 1`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tests/single.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.645 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.734 IQR)
- **Top Global Matches:** file_cluster_8: 7.645, file_cluster_7: 8.744, file_cluster_1: 8.883
- **Magnitude:** 24.36 | **LOC:** 400 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.6023%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 42`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tap, library
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tests/multiple.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.818 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.59 IQR)
- **Top Global Matches:** file_cluster_8: 7.818, file_cluster_7: 8.878, file_cluster_1: 9.031
- **Magnitude:** 23.66 | **LOC:** 359 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.598%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 2`, `args: 32`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tap, library
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tests/nocleanup.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.62 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.977 IQR)
- **Top Global Matches:** file_cluster_8: 7.62, file_cluster_7: 8.699, file_cluster_1: 8.86
- **Magnitude:** 20.14 | **LOC:** 176 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.8766%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 2`, `args: 22`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tap, library
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tests/bin/grandchild.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.624 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 7.301 IQR)
- **Top Global Matches:** file_cluster_4: 13.624, file_cluster_8: 13.641, file_cluster_15: 13.737
- **Magnitude:** 9.24 | **LOC:** 24 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setTimeout` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 4.08 | **LOC:** 204 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/tests/bin/stackable.js` (JAVASCRIPT) | Magnitude: 31.18 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, branch: 8, func_start: 6, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/tests/bin/groupable.js` (JAVASCRIPT) | Magnitude: 38.74 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 12, structural_boundaries: 9, indent_spaces: 8, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/tests/bin/grandchild.js` (JAVASCRIPT) | Magnitude: 9.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 6, indent_spaces: 4, structural_boundaries: 2, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/node-cleanup.js` (JAVASCRIPT) | Magnitude: 109.42 | Delta: **0.214 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, branch: 27, state_mutation: 19, func_start: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/node-cleanup.js` -> **Severity: 1324.476** (Blast Radius: 111.111 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
