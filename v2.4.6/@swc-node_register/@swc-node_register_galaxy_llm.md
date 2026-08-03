# ARCHITECTURAL_BRIEF: @swc-node_register
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@swc-node_register` |
| **Timestamp** | `2026-08-03T21:10:28.108806+00:00` |
| **Scan Duration** | `0.14s` |
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
| Total Artifacts | 13 |
| Analyzed Artifacts (Scanned) | 9 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 249 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.2% |
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
| TYPESCRIPT | 4 | 7 | 44.4% |
| JAVASCRIPT | 3 | 242 | 33.3% |
| MARKDOWN | 1 | 0 | 11.1% |
| PLAINTEXT | 1 | 0 | 11.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.382`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 4 | 44.4% |
| file_cluster_8 | 2 | 22.2% |
| file_cluster_4 | 1 | 11.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 22.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `.map`: 2x Excluded (Unsupported Extension: '.map')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsbuildinfo`: 1x Excluded (Unsupported Extension: '.tsbuildinfo')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 73.1 | 13.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 4.3 | 0.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 11.7 | 0.3 | 0.2 |
| API Exposure | 0.0 | 11.6 | 4.5 | 5.8 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 10.8 | 1.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 8.9 | 1.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 25.7 | 13.3 | 6.7 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 94.4 | 21.6 | 6.7 | 0.8 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/esm/esm.mjs` (Hits: 22)
- `package/README.md` (Hits: 0)
- `package/esm/esm-register.d.mts` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`package/README.md`) — 0 inbound connections
2. **esm-register.d.mts** (`package/esm/esm-register.d.mts`) — 0 inbound connections
3. **esm.d.mts** (`package/esm/esm.d.mts`) — 0 inbound connections
4. **read-default-tsconfig.d.ts** (`package/read-default-tsconfig.d.ts`) — 0 inbound connections
5. **register.d.ts** (`package/register.d.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **esm.mjs** (`package/esm/esm.mjs`) — 9 outbound dependencies
2. **esm-register.mjs** (`package/esm/esm-register.mjs`) — 2 outbound dependencies
3. **esm.d.mts** (`package/esm/esm.d.mts`) — 1 outbound dependencies
4. **read-default-tsconfig.d.ts** (`package/read-default-tsconfig.d.ts`) — 1 outbound dependencies
5. **register.d.ts** (`package/register.d.ts`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolve` (@ `package/esm/esm.mjs`) -> Impact: **388.7** | LOC: 94
- `load` (@ `package/esm/esm.mjs`) -> Impact: **65.3** | LOC: 27
- `getPackageForFile` (@ `package/esm/esm.mjs`) -> Impact: **49.0** | LOC: 27
- `readFileIfExists` (@ `package/esm/esm.mjs`) -> Impact: **14.5** | LOC: 13
- `getPackageType` (@ `package/esm/esm.mjs`) -> Impact: **8.9** | LOC: 5
- `getModuleType` (@ `package/esm/esm.mjs`) -> Impact: **6.2** | LOC: 4
- `readPackageJSON` (@ `package/esm/esm.mjs`) -> Impact: **5.6** | LOC: 8
- `addShortCircuitSignal` (@ `package/esm/esm.mjs`) -> Impact: **2.9** | LOC: 6

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `resolve` (@ `package/esm/esm.mjs`) -> **O(2^N) [Recursive]**
- `load` (@ `package/esm/esm.mjs`) -> **O(2^N) [Recursive]**
- `getPackageForFile` (@ `package/esm/esm.mjs`) -> **O(N^4)**
- `readFileIfExists` (@ `package/esm/esm.mjs`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `resolve` (@ `package/esm/esm.mjs`) -> DB Complexity: **28**
- `readPackageJSON` (@ `package/esm/esm.mjs`) -> DB Complexity: **16**
- `getPackageForFile` (@ `package/esm/esm.mjs`) -> DB Complexity: **10**
- `readFileIfExists` (@ `package/esm/esm.mjs`) -> DB Complexity: **8**
- `getModuleType` (@ `package/esm/esm.mjs`) -> DB Complexity: **6**
- `load` (@ `package/esm/esm.mjs`) -> DB Complexity: **2**
- `getPackageType` (@ `package/esm/esm.mjs`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/esm` | 4 | 625.16 | 20.78% | 0.0% |
| `package` | 5 | 17.62 | 2.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest State Flux (Mutation/Volatility)
- `package/esm/esm.mjs` -> **10.8011%** Exposure

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/esm/esm.mjs`** -> AI Confidence: **99.31%**
2. **`package/read-default-tsconfig.d.ts`** -> AI Confidence: **99.06%**
3. **`package/esm/esm-register.d.mts`** -> AI Confidence: **98.84%**
4. **`package/esm/esm.d.mts`** -> AI Confidence: **98.84%**
5. **`package/register.d.ts`** -> AI Confidence: **98.84%**
6. **`package/esm/esm-register.mjs`** -> AI Confidence: **98.84%**
7. **`package/index.js`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/esm/esm.mjs` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/esm/esm.mjs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/esm/esm.mjs` (JAVASCRIPT) -> Cumulative Risk: **723.92**
- **Archetype:** `file_cluster_4` (Distance: 11.832 IQR)
- **Magnitude:** 610.84 | **LOC:** 266 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `resolve` (Impact: 388.7), `load` (Impact: 65.3), `getPackageForFile` (Impact: 49.0)

### 2. `package/esm/esm.d.mts` (TYPESCRIPT) -> Cumulative Risk: **188.61**
- **Archetype:** `file_cluster_13` (Distance: 8.538 IQR)
- **Magnitude:** 1.61 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (68.1054%), Stability (50.0%), Spec Match (26.6667%), Documentation (26.6667%)

### 3. `package/esm/esm-register.mjs` (JAVASCRIPT) -> Cumulative Risk: **95.46**
- **Archetype:** `file_cluster_13` (Distance: 8.132 IQR)
- **Magnitude:** 11.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (20.0%), Documentation (19.9994%), Cognitive Load (5.0%)

### 4. `package/index.js` (JAVASCRIPT) -> Cumulative Risk: **70.23**
- **Archetype:** `file_cluster_8` (Distance: 7.455 IQR)
- **Magnitude:** 11.04 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (13.3333%), Cognitive Load (5.0%), Documentation (1.5894%)

### 5. `package/esm/esm-register.d.mts` (TYPESCRIPT) -> Cumulative Risk: **69.27**
- **Archetype:** `file_cluster_8` (Distance: 6.263 IQR)
- **Magnitude:** 1.15 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Documentation (6.6667%), Api Exposure (5.7813%)

### 6. `package/read-default-tsconfig.d.ts` (TYPESCRIPT) -> Cumulative Risk: **68.4**
- **Archetype:** `file_cluster_13` (Distance: 6.663 IQR)
- **Magnitude:** 1.15 | **LOC:** 2 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Api Exposure (5.7813%), Cognitive Load (5.0%)

### 7. `package/register.d.ts` (TYPESCRIPT) -> Cumulative Risk: **63.4**
- **Archetype:** `file_cluster_13` (Distance: 7.171 IQR)
- **Magnitude:** 1.15 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Api Exposure (5.7813%), Documentation (0.7947%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/esm/esm.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.832 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.037 IQR)
- **Top Global Matches:** file_cluster_4: 11.832, file_cluster_13: 12.195, file_cluster_0: 12.336
- **Magnitude:** 610.84 | **LOC:** 266 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 388.7 | O(2^N) | DB: 28)
  * `load` (Impact: 65.3 | O(2^N) | DB: 2)
  * `getPackageForFile` (Impact: 49.0 | O(N^4) | DB: 10)
  * `readFileIfExists` (Impact: 14.5 | O(N^3) | DB: 8)
  * `getPackageType` (Impact: 8.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 65`, `args: 10`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 18`, `dead_code: 2`
* *Architecture:* `io: 22`, `api: 3`, `concurrency: 44`, `import: 9`
* *Defense:* `safety: 37`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` read-default-tsconfig.js, node:url, typescript, node:module, debug, oxc-resolver, register.js, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/esm-register.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.132 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 7.391 IQR)
- **Top Global Matches:** file_cluster_13: 8.132, file_cluster_8: 8.537, file_cluster_0: 8.771
- **Magnitude:** 11.56 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:url, node:module
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.455 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 7.623 IQR)
- **Top Global Matches:** file_cluster_8: 7.455, file_cluster_13: 7.602, file_cluster_7: 8.469
- **Magnitude:** 11.04 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` register
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.6 | **LOC:** 130 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Magnitude:** 1.68 | **LOC:** 84 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `package/esm/esm.d.mts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.538 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.864 IQR)
- **Top Global Matches:** file_cluster_13: 8.538, file_cluster_8: 8.714, file_cluster_4: 8.854
- **Magnitude:** 1.61 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 1`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:module
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/esm-register.d.mts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.263 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.014 IQR)
- **Top Global Matches:** file_cluster_8: 6.263, file_cluster_7: 7.363, file_cluster_1: 7.679
- **Magnitude:** 1.15 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/read-default-tsconfig.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.663 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.099 IQR)
- **Top Global Matches:** file_cluster_13: 6.663, file_cluster_8: 7.524, file_cluster_7: 8.502
- **Magnitude:** 1.15 | **LOC:** 2 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` read-default-tsconfig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/register.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.171 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.826 IQR)
- **Top Global Matches:** file_cluster_13: 7.171, file_cluster_8: 8.018, file_cluster_7: 8.76
- **Magnitude:** 1.15 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` register
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/esm/esm.d.mts` (TYPESCRIPT) | Magnitude: 1.61 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, api: 3, immutability_locks: 3, args: 1
- `package/esm/esm-register.mjs` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.405 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: dependency_injection: 3, structural_boundaries: 2, import: 2, func_start: 1
- `package/register.d.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.847 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, import: 1, dependency_injection: 1
- `package/read-default-tsconfig.d.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.861 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, api: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/esm/esm.mjs` (JAVASCRIPT) | Magnitude: 610.84 | Delta: **0.363 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 196, branch: 67, structural_boundaries: 65, concurrency: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/index.js` (JAVASCRIPT) | Magnitude: 11.04 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: dependency_injection: 3, func_start: 1, import: 1, immutability_locks: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/esm/esm.mjs` -> **Severity: 10483.867** (Blast Radius: 111.111 * Doc Risk: 94.3549%)
- `package/esm/esm.d.mts` -> **Severity: 2962.964** (Blast Radius: 111.111 * Doc Risk: 26.6667%)
- `package/esm/esm-register.mjs` -> **Severity: 2222.153** (Blast Radius: 111.111 * Doc Risk: 19.9994%)
- `package/esm/esm-register.d.mts` -> **Severity: 740.744** (Blast Radius: 111.111 * Doc Risk: 6.6667%)
- `package/index.js` -> **Severity: 176.6** (Blast Radius: 111.111 * Doc Risk: 1.5894%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
