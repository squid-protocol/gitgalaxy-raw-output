# ARCHITECTURAL_BRIEF: config
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/config` |
| **Timestamp** | `2026-08-03T21:11:42.772449+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 8 malicious artifacts.

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
| Total Artifacts | 14 |
| Analyzed Artifacts (Scanned) | 12 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 224 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 85.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4 | 175 | 33.3% |
| TYPESCRIPT | 4 | 34 | 33.3% |
| MARKDOWN | 2 | 0 | 16.7% |
| PLAINTEXT | 1 | 0 | 8.3% |
| JSON | 1 | 15 | 8.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.502`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 4 | 33.3% |
| file_cluster_8 | 2 | 16.7% |
| file_cluster_4 | 1 | 8.3% |
| file_cluster_16 | 1 | 8.3% |
| file_cluster_7 | 1 | 8.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 25.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 1x Excluded (Explicitly Denied Extension: '.tgz')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.9 | 50.0 | 13.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 25.0 | 7.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 44.8 | 5.0 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 80.0 | 10.2 | 1.2 | 2.3 |
| API Exposure | 0.0 | 12.6 | 7.0 | 7.6 | 9.2 |
| Concurrency Exposure | 0.0 | 100.0 | 22.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 64.4 | 46.7 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 5.6 | 33.2 | 15.7 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 99.2 | 11.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 22.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/History.md` (Hits: 0)
- `package/README.md` (Hits: 0)
- `package/async.js` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **defer.js** (`package/defer.js`) — 3 inbound connections
2. **History.md** (`package/History.md`) — 0 inbound connections
3. **README.md** (`package/README.md`) — 0 inbound connections
4. **async.js** (`package/async.js`) — 0 inbound connections
5. **parser.js** (`package/parser.js`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **async.js** (`package/async.js`) — 4 outbound dependencies
2. **defer.js** (`package/defer.js`) — 3 outbound dependencies
3. **parser.js** (`package/parser.js`) — 3 outbound dependencies
4. **async.d.ts** (`package/types/async.d.ts`) — 3 outbound dependencies
5. **defer.d.ts** (`package/types/defer.d.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `coffeeParser` (@ `package/parser.js`) -> Impact: **46.9** | LOC: 106
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `resolveAsyncConfigs` (@ `package/async.js`) -> Impact: **19.5** | LOC: 27
  * *Intent:* /** @typedef {import('./lib/config').Config} Config */ /** @typedef {import('./defer').DeferredConfig} DeferredConfig */ /** * @template T * @overload
- `tsParser` (@ `package/parser.js`) -> Impact: **19.3** | LOC: 23
  * *Intent:* // TODO: decide what to do in case of a missing parser
- `jsParser` (@ `package/parser.js`) -> Impact: **9.1** | LOC: 8
  * *Intent:* /**
- `xmlParser` (@ `package/parser.js`) -> Impact: **5.8** | LOC: 12
- `deferConfig` (@ `package/defer.js`) -> Impact: **3.8** | LOC: 6
  * *Intent:* /**
- `parse` (@ `package/parser.js`) -> Impact: **3.8** | LOC: 7
- `raw` (@ `package/raw.js`) -> Impact: **3.7** | LOC: 5
  * *Intent:* /**
- `raw` (@ `package/types/raw.d.ts`) -> Impact: **2.1** | LOC: 3
  * *Intent:* /**

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `deferConfig` (@ `package/defer.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `coffeeParser` (@ `package/parser.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `raw` (@ `package/raw.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**

### Highest Data Gravity (Database Complexity)
- `resolveAsyncConfigs` (@ `package/async.js`) -> DB Complexity: **6**
  * *Intent:* /** @typedef {import('./lib/config').Config} Config */ /** @typedef {import('./defer').DeferredConfig} DeferredConfig */ /** * @template T * @overload
- `coffeeParser` (@ `package/parser.js`) -> DB Complexity: **6**
  * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
- `xmlParser` (@ `package/parser.js`) -> DB Complexity: **3**
- `tsParser` (@ `package/parser.js`) -> DB Complexity: **1**
  * *Intent:* // TODO: decide what to do in case of a missing parser
- `jsParser` (@ `package/parser.js`) -> DB Complexity: **1**
  * *Intent:* /**
- `parse` (@ `package/parser.js`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package` | 8 | 231.78 | 12.79% | 5.6% |
| `package/types` | 4 | 22.2 | 4.47% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/parser.js` -> **44.7711%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/async.js` -> **100.0%** Exposure
- `package/parser.js` -> **99.9896%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/parser.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/parser.js`** -> AI Confidence: **99.0%**
2. **`package/async.js`** -> AI Confidence: **98.96%**
3. **`package/defer.js`** -> AI Confidence: **98.88%**
4. **`package/types/async.d.ts`** -> AI Confidence: **98.88%**
5. **`package/raw.js`** -> AI Confidence: **98.84%**
6. **`package/types/defer.d.ts`** -> AI Confidence: **98.84%**
7. **`package/types/parser.d.ts`** -> AI Confidence: **98.84%**
8. **`package/types/raw.d.ts`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Weaponizable Injection Vectors
- `package/raw.js` -> **100.0%** Exposure
- `package/types/raw.d.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/async.js` -> **99.2103%** Exposure
- `package/parser.js` -> **3.8462%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/async.js` (JAVASCRIPT) -> Cumulative Risk: **565.3**
- **Archetype:** `file_cluster_4` (Distance: 14.879 IQR)
- **Magnitude:** 58.1 | **LOC:** 92 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.2103%)
- **Heaviest Functions:** `resolveAsyncConfigs` (Impact: 19.5)

### 2. `package/parser.js` (JAVASCRIPT) -> Cumulative Risk: **425.93**
- **Archetype:** `file_cluster_13` (Distance: 13.339 IQR)
- **Magnitude:** 126.52 | **LOC:** 385 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9896%), Verification (80.0%), Stability (50.0%)
- **Heaviest Functions:** `coffeeParser` (Impact: 46.9), `tsParser` (Impact: 19.3), `jsParser` (Impact: 9.1)

### 3. `package/types/raw.d.ts` (TYPESCRIPT) -> Cumulative Risk: **311.52**
- **Archetype:** `file_cluster_13` (Distance: 10.929 IQR)
- **Magnitude:** 0.42 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Injection Surface (100.0%), Safety Score (80.0%), Stability (50.0%), Spec Match (33.3333%)
- **Heaviest Functions:** `raw` (Impact: 2.1)

### 4. `package/types/async.d.ts` (TYPESCRIPT) -> Cumulative Risk: **309.98**
- **Archetype:** `file_cluster_16` (Distance: 13.701 IQR)
- **Magnitude:** 3.16 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (99.9828%), Safety Score (80.0%), Stability (50.0%), Spec Match (33.3333%)

### 5. `package/raw.js` (JAVASCRIPT) -> Cumulative Risk: **216.07**
- **Archetype:** `file_cluster_8` (Distance: 10.197 IQR)
- **Magnitude:** 5.84 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Injection Surface (100.0%), Stability (50.0%), Spec Match (46.6667%), Api Exposure (7.6019%)
- **Heaviest Functions:** `raw` (Impact: 3.7)

### 6. `package/types/parser.d.ts` (TYPESCRIPT) -> Cumulative Risk: **189.95**
- **Archetype:** `file_cluster_7` (Distance: 13.42 IQR)
- **Magnitude:** 17.26 | **LOC:** 133 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Api Exposure (12.6221%), Documentation (11.9203%)

### 7. `package/defer.js` (JAVASCRIPT) -> Cumulative Risk: **115.69**
- **Archetype:** `file_cluster_13` (Distance: 10.493 IQR)
- **Magnitude:** 5.94 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (46.6667%), Api Exposure (7.217%), Documentation (5.5628%)
- **Heaviest Functions:** `deferConfig` (Impact: 3.8)

### 8. `package/types/defer.d.ts` (TYPESCRIPT) -> Cumulative Risk: **104.62**
- **Archetype:** `file_cluster_13` (Distance: 7.032 IQR)
- **Magnitude:** 1.36 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (20.0%), Documentation (20.0%), Api Exposure (9.1631%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/parser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.339 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.622 IQR)
- **Top Global Matches:** file_cluster_13: 13.339, file_cluster_8: 13.5, file_cluster_0: 13.512
- **Magnitude:** 126.52 | **LOC:** 385 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (26.4297%), Tech Debt (44.7711%)
**Top Internal Functions/Classes:**
  * `coffeeParser` (Impact: 46.9 | O(2^N) | DB: 6)
    * *Intent:* /** * @param {string} filename * @param {string} content * @returns {object} */
  * `tsParser` (Impact: 19.3 | O(N^2) | DB: 1)
    * *Intent:* // TODO: decide what to do in case of a missing parser
  * `jsParser` (Impact: 9.1 | O(N^1) | DB: 1)
    * *Intent:* /**
  * `xmlParser` (Impact: 5.8 | O(N^1) | DB: 3)
  * `parse` (Impact: 3.8 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 28`, `args: 13`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 38`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 14`, `doc: 46`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json5, coffee-script, iced-coffee-script
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/async.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.879 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 6.007 IQR)
- **Top Global Matches:** file_cluster_4: 14.879, file_cluster_17: 15.18, file_cluster_13: 15.379
- **Magnitude:** 58.1 | **LOC:** 92 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (49.9872%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveAsyncConfigs` (Impact: 19.5 | O(N^2) | DB: 6)
    * *Intent:* /** @typedef {import('./lib/config').Config} Config */ /** @typedef {import('./defer').DeferredConfi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 7`, `args: 6`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`
* *Architecture:* `api: 2`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` config, util.js, defer, config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/parser.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_7` (Drift: 13.42 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 4.508 IQR)
- **Top Global Matches:** file_cluster_7: 13.42, file_cluster_8: 13.479, file_cluster_16: 13.494
- **Magnitude:** 17.26 | **LOC:** 133 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.8867%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 23`, `args: 21`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 21`
* *Defense:* `safety: 1`, `doc: 77`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.8869%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/History.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 14.22 | **LOC:** 711 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/defer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.493 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.938 IQR)
- **Top Global Matches:** file_cluster_13: 10.493, file_cluster_8: 10.721, file_cluster_7: 10.826
- **Magnitude:** 5.94 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deferConfig` (Impact: 3.8 | O(2^N))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 243.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272727
  * `Imports (Out-Degree: 0):` util.js, defer.js, defer
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/raw.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.197 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.611 IQR)
- **Top Global Matches:** file_cluster_8: 10.197, file_cluster_13: 10.277, file_cluster_7: 10.297
- **Magnitude:** 5.84 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `raw` (Impact: 3.7 | O(2^N))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.66 | **LOC:** 183 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/async.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.701 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 7.019 IQR)
- **Top Global Matches:** file_cluster_16: 13.701, file_cluster_13: 13.868, file_cluster_2: 14.264
- **Magnitude:** 3.16 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 2`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` config, defer, config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.2 | **LOC:** 110 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/defer.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.032 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.825 IQR)
- **Top Global Matches:** file_cluster_13: 7.032, file_cluster_8: 7.567, file_cluster_7: 8.487
- **Magnitude:** 1.36 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` defer.js, defer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/types/raw.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.929 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.271 IQR)
- **Top Global Matches:** file_cluster_13: 10.929, file_cluster_8: 11.21, file_cluster_7: 11.24
- **Magnitude:** 0.42 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `raw` (Impact: 2.1 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/parser.js` (JAVASCRIPT) | Magnitude: 126.52 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 95, doc: 46, state_mutation: 38, structural_boundaries: 28
- `package/defer.js` (JAVASCRIPT) | Magnitude: 5.94 | Delta: **0.228 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, indent_spaces: 3, structural_boundaries: 2, api: 2
- `package/types/raw.d.ts` (TYPESCRIPT) | Magnitude: 0.42 | Delta: **0.281 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 3, args: 2, func_start: 2
- `package/types/defer.d.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.535 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, import: 2, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/types/async.d.ts` (TYPESCRIPT) | Magnitude: 3.16 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 10, generics: 6, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/async.js` (JAVASCRIPT) | Magnitude: 58.1 | Delta: **0.301 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 18, concurrency: 18, doc: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `package/types/parser.d.ts` (TYPESCRIPT) | Magnitude: 17.26 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 77, structural_boundaries: 23, args: 21, api: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/raw.js` (JAVASCRIPT) | Magnitude: 5.84 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, api: 2, indent_spaces: 2, structural_boundaries: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/types/raw.d.ts` -> **Severity: 2280.25** (Blast Radius: 68.729 * Doc Risk: 33.1774%)
- `package/types/async.d.ts` -> **Severity: 2045.451** (Blast Radius: 68.729 * Doc Risk: 29.7611%)
- `package/types/defer.d.ts` -> **Severity: 1374.58** (Blast Radius: 68.729 * Doc Risk: 20.0%)
- `package/defer.js` -> **Severity: 1357.245** (Blast Radius: 243.986 * Doc Risk: 5.5628%)
- `package/async.js` -> **Severity: 819.27** (Blast Radius: 68.729 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
