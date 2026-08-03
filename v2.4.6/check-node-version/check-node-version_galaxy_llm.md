# ARCHITECTURAL_BRIEF: check-node-version
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/check-node-version` |
| **Timestamp** | `2026-08-03T21:11:40.781016+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6 malicious artifacts.

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
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 402 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2188 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -1.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 5 | 366 | 50.0% |
| MARKDOWN | 2 | 0 | 20.0% |
| PLAINTEXT | 2 | 0 | 20.0% |
| TYPESCRIPT | 1 | 36 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.213`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 5 | 50.0% |
| file_cluster_13 | 1 | 10.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 40.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 92.4 | 24.9 | 10.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 62.2 | 20.4 | 2.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.5 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 80.0 | 15.0 | 2.4 | 0.5 |
| API Exposure | 0.0 | 3.5 | 1.6 | 1.7 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 23.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 86.7 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 2.4 | 11.9 | 10.3 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 52.6 | 12.2 | 0.8 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cli.js` (Hits: 10)
- `package/index.js` (Hits: 5)
- `package/tools.js` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **tools.js** (`package/tools.js`) — 2 inbound connections
2. **cli.js** (`package/cli.js`) — 1 inbound connections
3. **gatekeeper.js** (`package/gatekeeper.js`) — 1 inbound connections
4. **CHANGELOG.md** (`package/CHANGELOG.md`) — 0 inbound connections
5. **README.md** (`package/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cli.js** (`package/cli.js`) — 7 outbound dependencies
2. **index.js** (`package/index.js`) — 7 outbound dependencies
3. **bin.js** (`package/bin.js`) — 2 outbound dependencies
4. **gatekeeper.js** (`package/gatekeeper.js`) — 2 outbound dependencies
5. **tools.js** (`package/tools.js`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `runForWindows` (@ `package/index.js`) -> Impact: **59.1** | LOC: 73
- `parallel` (@ `package/index.js`) -> Impact: **23.0** | LOC: 40
- `runVersionCommand` (@ `package/index.js`) -> Impact: **17.6** | LOC: 40
- `printVersions` (@ `package/cli.js`) -> Impact: **11.6** | LOC: 25
  * *Intent:* //
- `check` (@ `package/index.js`) -> Impact: **10.0** | LOC: 26
  * *Intent:* ;
- `optionsFromPackage` (@ `package/cli.js`) -> Impact: **9.9** | LOC: 24
- `optionsFromVolta` (@ `package/cli.js`) -> Impact: **8.2** | LOC: 25
- `check` (@ `package/cli.js`) -> Impact: **6.4** | LOC: 8
- `hasNvm` (@ `package/tools.js`) -> Impact: **5.9** | LOC: 14
- `getInstallInstructions` (@ `package/tools.js`) -> Impact: **4.6** | LOC: 7

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `runForWindows` (@ `package/index.js`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `optionsFromPackage` (@ `package/cli.js`) -> DB Complexity: **7**
- `optionsFromVolta` (@ `package/cli.js`) -> DB Complexity: **7**
- `runVersionCommand` (@ `package/index.js`) -> DB Complexity: **3**
- `getInstallInstructions` (@ `package/tools.js`) -> DB Complexity: **3**
- `getInstallInstructions` (@ `package/tools.js`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package` | 10 | 271.77 | 14.95% | 11.68% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/tools.js` -> **100.0%** Exposure
- `package/index.js` -> **16.8487%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/gatekeeper.js` -> **100.0%** Exposure
- `package/cli.js` -> **38.014%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/tools.js` -> **0** Orphaned Functions | **5** Duplicates
- `package/index.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/cli.js`** -> AI Confidence: **99.31%**
2. **`package/index.js`** -> AI Confidence: **99.31%**
3. **`package/gatekeeper.js`** -> AI Confidence: **99.06%**
4. **`package/tools.js`** -> AI Confidence: **98.89%**
5. **`package/index.d.ts`** -> AI Confidence: **98.85%**
6. **`package/bin.js`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/cli.js` -> **100.0%** Exposure
- `package/index.js` -> **0.0114%** Exposure
### Weaponizable Injection Vectors
- `package/cli.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `package/index.js` -> **52.6084%** Exposure
- `package/tools.js` -> **18.9338%** Exposure
- `package/cli.js` -> **1.6668%** Exposure

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

### 1. `package/cli.js` (JAVASCRIPT) -> Cumulative Risk: **486.85**
- **Archetype:** `file_cluster_8` (Distance: 10.253 IQR)
- **Magnitude:** 56.78 | **LOC:** 178 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Safety Score (56.1194%)
- **Heaviest Functions:** `printVersions` (Impact: 11.6), `optionsFromPackage` (Impact: 9.9), `optionsFromVolta` (Impact: 8.2)

### 2. `package/gatekeeper.js` (JAVASCRIPT) -> Cumulative Risk: **418.92**
- **Archetype:** `file_cluster_13` (Distance: 11.045 IQR)
- **Magnitude:** 24.32 | **LOC:** 20 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (92.4142%), Safety Score (62.2459%)

### 3. `package/index.js` (JAVASCRIPT) -> Cumulative Risk: **331.1**
- **Archetype:** `file_cluster_8` (Distance: 9.119 IQR)
- **Magnitude:** 126.22 | **LOC:** 240 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Algorithmic Dos (52.6084%), Stability (50.0%)
- **Heaviest Functions:** `runForWindows` (Impact: 59.1), `parallel` (Impact: 23.0), `runVersionCommand` (Impact: 17.6)

### 4. `package/tools.js` (JAVASCRIPT) -> Cumulative Risk: **294.99**
- **Archetype:** `file_cluster_8` (Distance: 7.645 IQR)
- **Magnitude:** 18.84 | **LOC:** 54 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Stability (50.0%), Algorithmic Dos (18.9338%)
- **Heaviest Functions:** `hasNvm` (Impact: 5.9), `getInstallInstructions` (Impact: 4.6), `getInstallInstructions` (Impact: 1.6)

### 5. `package/index.d.ts` (TYPESCRIPT) -> Cumulative Risk: **172.06**
- **Archetype:** `file_cluster_8` (Distance: 11.58 IQR)
- **Magnitude:** 26.47 | **LOC:** 146 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (11.9203%), Cognitive Load (5.0661%)

### 6. `package/bin.js` (JAVASCRIPT) -> Cumulative Risk: **77.84**
- **Archetype:** `file_cluster_8` (Distance: 7.511 IQR)
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (20.0%), Cognitive Load (5.0%), Documentation (2.3841%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.119 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.449 IQR)
- **Top Global Matches:** file_cluster_8: 9.119, file_cluster_13: 9.503, file_cluster_17: 9.901
- **Magnitude:** 126.22 | **LOC:** 240 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (13.1066%), Tech Debt (16.8487%)
**Top Internal Functions/Classes:**
  * `runForWindows` (Impact: 59.1 | O(N^3))
  * `parallel` (Impact: 23.0 | O(N^2))
  * `runVersionCommand` (Impact: 17.6 | O(N^2) | DB: 3)
  * `check` (Impact: 10.0 | O(N^1))
    * *Intent:* ;
  * `normalizeWanted` (Impact: 4.3 | O(N^1))
    * *Intent:* // Return object containing only keys that a program exists for and // something valid was given.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 28`, `args: 19`, `func_start: 22`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `api: 1`, `import: 7`
* *Defense:* `safety: 7`, `immutability_locks: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 77.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path, run-parallel, semver, tools, child_process, object-filter, map-values
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cli.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.253 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.45 IQR)
- **Top Global Matches:** file_cluster_8: 10.253, file_cluster_13: 10.29, file_cluster_17: 10.47
- **Magnitude:** 56.78 | **LOC:** 178 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (25.7367%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `printVersions` (Impact: 11.6 | O(N^2))
    * *Intent:* //
  * `optionsFromPackage` (Impact: 9.9 | O(N^1) | DB: 7)
  * `optionsFromVolta` (Impact: 8.2 | O(N^1) | DB: 7)
  * `check` (Impact: 6.4 | O(N^1))
  * `optionsFromCommandLine` (Impact: 2.0 | O(N^1))
    * *Intent:* //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 13`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 12`
* *Architecture:* `io: 10`, `api: 1`, `import: 9`
* *Defense:* `safety: 4`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 110.369
  * `Choke Point (Betweenness):` 0.013889 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 1):` fs, path, , semver, minimist, tools, chalk
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/index.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.58 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.513 IQR)
- **Top Global Matches:** file_cluster_8: 11.58, file_cluster_7: 11.832, file_cluster_1: 12.03
- **Magnitude:** 26.47 | **LOC:** 146 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0661%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 16`, `args: 5`, `func_start: 2`, `class_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `safety: 5`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/gatekeeper.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.045 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.683 IQR)
- **Top Global Matches:** file_cluster_13: 11.045, file_cluster_8: 11.18, file_cluster_17: 11.818
- **Magnitude:** 24.32 | **LOC:** 20 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.4142%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 9`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 110.369
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` semver, package.json
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/tools.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.645 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.568 IQR)
- **Top Global Matches:** file_cluster_8: 7.645, file_cluster_13: 8.679, file_cluster_7: 8.723
- **Magnitude:** 18.84 | **LOC:** 54 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (8.16%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `hasNvm` (Impact: 5.9 | O(N^1))
  * `getInstallInstructions` (Impact: 4.6 | O(N^2) | DB: 3)
  * `getInstallInstructions` (Impact: 1.6 | O(N^1))
  * `getInstallInstructions` (Impact: 1.6 | O(N^1))
  * `getInstallInstructions` (Impact: 1.6 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 6`, `func_start: 7`
* *Risk/State:* `duplicate_logic: 5`
* *Architecture:* `io: 3`, `api: 1`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 237.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 0):` child_process
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/bin.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.511 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.499 IQR)
- **Top Global Matches:** file_cluster_8: 7.511, file_cluster_13: 7.711, file_cluster_7: 8.689
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 77.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` cli, gatekeeper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 4.44 | **LOC:** 222 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.08 | **LOC:** 54 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.06 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/usage.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 46 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/gatekeeper.js` (JAVASCRIPT) | Magnitude: 24.32 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 9, branch: 3, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/cli.js` (JAVASCRIPT) | Magnitude: 56.78 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, branch: 24, debug_prints: 15, structural_boundaries: 13
- `package/bin.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.2 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: func_start: 2, import: 2
- `package/index.d.ts` (TYPESCRIPT) | Magnitude: 26.47 | Delta: **0.252 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 32, indent_spaces: 17, structural_boundaries: 16, branch: 9
- `package/index.js` (JAVASCRIPT) | Magnitude: 126.22 | Delta: **0.384 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 140, branch: 33, structural_boundaries: 28, func_start: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/cli.js` -> **Severity: 0.528** (Bridge: 0.0139 * Flux: 38.014%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/gatekeeper.js` -> **Severity: 6.916** (Embedded: 0.1111 * Error Risk: 62.2459%)
- `package/cli.js` -> **Severity: 6.235** (Embedded: 0.1111 * Error Risk: 56.1194%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/tools.js` -> **Severity: 2826.291** (Blast Radius: 237.099 * Doc Risk: 11.9203%)
- `package/cli.js` -> **Severity: 1315.632** (Blast Radius: 110.369 * Doc Risk: 11.9203%)
- `package/gatekeeper.js` -> **Severity: 1315.632** (Blast Radius: 110.369 * Doc Risk: 11.9203%)
- `package/index.js` -> **Severity: 923.251** (Blast Radius: 77.452 * Doc Risk: 11.9203%)
- `package/index.d.ts` -> **Severity: 923.251** (Blast Radius: 77.452 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
