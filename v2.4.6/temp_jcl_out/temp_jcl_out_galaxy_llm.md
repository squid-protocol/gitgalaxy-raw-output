# ARCHITECTURAL_BRIEF: temp_jcl_out
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/temp_jcl_out` |
| **Timestamp** | `2026-08-03T21:38:28.435546+00:00` |
| **Scan Duration** | `0.38s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 29 malicious artifacts.

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
| Total Artifacts | 29 |
| Analyzed Artifacts (Scanned) | 29 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 24371 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | JCL |

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
| JCL | 29 | 24371 | 100.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.979`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 29 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 7.3 | 5.9 | 6.1 | 6.1 |
| Error & Exception Exposure | 5.0 | 15.9 | 6.3 | 5.3 | 6.7 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 2.3 | 2.3 | 2.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 12.5 | 41.1 | 15.6 | 13.1 | 16.4 |
| Algorithmic DoS Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 44.4 | 19.4 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 28.6 | 0.0 | 100.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `BUILD_BANKDATA.jcl` (Hits: 6)
- `BUILD_ABNDPROC.jcl` (Hits: 5)
- `BUILD_BNK1CAC.jcl` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **BUILD_ABNDPROC.jcl** (`BUILD_ABNDPROC.jcl`) — 0 inbound connections
2. **BUILD_BANKDATA.jcl** (`BUILD_BANKDATA.jcl`) — 0 inbound connections
3. **BUILD_BNK1CAC.jcl** (`BUILD_BNK1CAC.jcl`) — 0 inbound connections
4. **BUILD_BNK1CCA.jcl** (`BUILD_BNK1CCA.jcl`) — 0 inbound connections
5. **BUILD_BNK1CCS.jcl** (`BUILD_BNK1CCS.jcl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **BUILD_BANKDATA.jcl** (`BUILD_BANKDATA.jcl`) — 2 outbound dependencies
2. **BUILD_ABNDPROC.jcl** (`BUILD_ABNDPROC.jcl`) — 1 outbound dependencies
3. **BUILD_BNK1CAC.jcl** (`BUILD_BNK1CAC.jcl`) — 1 outbound dependencies
4. **BUILD_BNK1CCA.jcl** (`BUILD_BNK1CCA.jcl`) — 1 outbound dependencies
5. **BUILD_BNK1CCS.jcl** (`BUILD_BNK1CCS.jcl`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

*No complex functions detected.*

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 29 | 24307.42 | 5.88% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`BUILD_BANKDATA.jcl`** -> AI Confidence: **99.29%**
2. **`BUILD_BNK1CAC.jcl`** -> AI Confidence: **99.29%**
3. **`BUILD_BNK1CCA.jcl`** -> AI Confidence: **99.29%**
4. **`BUILD_BNK1CCS.jcl`** -> AI Confidence: **99.29%**
5. **`BUILD_BNK1CRA.jcl`** -> AI Confidence: **99.29%**
6. **`BUILD_BNK1DAC.jcl`** -> AI Confidence: **99.29%**
7. **`BUILD_BNK1DCS.jcl`** -> AI Confidence: **99.29%**
8. **`BUILD_BNK1TFN.jcl`** -> AI Confidence: **99.29%**
9. **`BUILD_BNK1UAC.jcl`** -> AI Confidence: **99.29%**
10. **`BUILD_BNKMENU.jcl`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `BUILD_BNK1CAC.jcl` -> **100.0%** Exposure
- `BUILD_BNK1CCA.jcl` -> **100.0%** Exposure
- `BUILD_BNK1CCS.jcl` -> **100.0%** Exposure
- `BUILD_BNK1CRA.jcl` -> **100.0%** Exposure
- `BUILD_BNK1DAC.jcl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `BUILD_ABNDPROC.jcl` -> **100.0%** Exposure
- `BUILD_CRDTAGY1.jcl` -> **100.0%** Exposure
- `BUILD_CRDTAGY2.jcl` -> **100.0%** Exposure
- `BUILD_CRDTAGY3.jcl` -> **100.0%** Exposure
- `BUILD_CRDTAGY4.jcl` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `30` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `BUILD_GETCOMPY.jcl` (JCL) -> Cumulative Risk: **354.92**
- **Archetype:** `file_cluster_8` (Distance: 5.02 IQR)
- **Magnitude:** 16.22 | **LOC:** 77 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Logic Bomb (45.6439%)

### 2. `BUILD_GETSCODE.jcl` (JCL) -> Cumulative Risk: **340.03**
- **Archetype:** `file_cluster_8` (Distance: 4.943 IQR)
- **Magnitude:** 16.42 | **LOC:** 89 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Logic Bomb (38.0632%)

### 3. `BUILD_ABNDPROC.jcl` (JCL) -> Cumulative Risk: **289.56**
- **Archetype:** `file_cluster_8` (Distance: 6.532 IQR)
- **Magnitude:** 48.52 | **LOC:** 224 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Documentation (19.2816%)

### 4. `BUILD_CRDTAGY1.jcl` (JCL) -> Cumulative Risk: **283.03**
- **Archetype:** `file_cluster_8` (Distance: 6.991 IQR)
- **Magnitude:** 140.4 | **LOC:** 330 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Documentation (16.3881%)

### 5. `BUILD_CRDTAGY2.jcl` (JCL) -> Cumulative Risk: **283.03**
- **Archetype:** `file_cluster_8` (Distance: 6.991 IQR)
- **Magnitude:** 140.4 | **LOC:** 330 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Documentation (16.3881%)

### 6. `BUILD_CRDTAGY3.jcl` (JCL) -> Cumulative Risk: **283.03**
- **Archetype:** `file_cluster_8` (Distance: 6.991 IQR)
- **Magnitude:** 140.4 | **LOC:** 329 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Documentation (16.3881%)

### 7. `BUILD_CRDTAGY4.jcl` (JCL) -> Cumulative Risk: **283.03**
- **Archetype:** `file_cluster_8` (Distance: 6.991 IQR)
- **Magnitude:** 140.4 | **LOC:** 332 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Documentation (16.3881%)

### 8. `BUILD_CRDTAGY5.jcl` (JCL) -> Cumulative Risk: **283.03**
- **Archetype:** `file_cluster_8` (Distance: 6.991 IQR)
- **Magnitude:** 140.4 | **LOC:** 332 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Stability (50.0%), Documentation (16.3881%)

### 9. `BUILD_BNK1UAC.jcl` (JCL) -> Cumulative Risk: **277.2**
- **Archetype:** `file_cluster_8` (Distance: 8.223 IQR)
- **Magnitude:** 1764.6 | **LOC:** 1458 | **CtrlFlow:** 99.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Stability (50.0%), Documentation (12.8007%)

### 10. `BUILD_BNK1CCA.jcl` (JCL) -> Cumulative Risk: **277.18**
- **Archetype:** `file_cluster_8` (Distance: 7.945 IQR)
- **Magnitude:** 902.44 | **LOC:** 1045 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Stability (50.0%), Documentation (13.1779%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `BUILD_XFRFUN.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.563 IQR)
- **Top Global Matches:** file_cluster_8: 8.563, file_cluster_7: 9.538, file_cluster_1: 9.711
- **Magnitude:** 2316.16 | **LOC:** 2179 | **CtrlFlow:** 99.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.6372%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1DCS.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.569 IQR)
- **Top Global Matches:** file_cluster_8: 8.569, file_cluster_7: 9.541, file_cluster_1: 9.716
- **Magnitude:** 2091.16 | **LOC:** 2184 | **CtrlFlow:** 99.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.4345%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1UAC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.223 IQR)
- **Top Global Matches:** file_cluster_8: 8.223, file_cluster_7: 9.237, file_cluster_1: 9.413
- **Magnitude:** 1764.6 | **LOC:** 1458 | **CtrlFlow:** 99.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.9558%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1CCS.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.367 IQR)
- **Top Global Matches:** file_cluster_8: 8.367, file_cluster_7: 9.361, file_cluster_1: 9.537
- **Magnitude:** 1528.56 | **LOC:** 1710 | **CtrlFlow:** 99.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.3288%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1CAC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.166 IQR)
- **Top Global Matches:** file_cluster_8: 8.166, file_cluster_7: 9.185, file_cluster_1: 9.362
- **Magnitude:** 1462.84 | **LOC:** 1351 | **CtrlFlow:** 99.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.7093%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1TFN.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.115 IQR)
- **Top Global Matches:** file_cluster_8: 8.115, file_cluster_7: 9.139, file_cluster_1: 9.317
- **Magnitude:** 1356.52 | **LOC:** 1277 | **CtrlFlow:** 98.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.6877%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_CRECUST.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.387 IQR)
- **Top Global Matches:** file_cluster_8: 8.387, file_cluster_7: 9.375, file_cluster_1: 9.552
- **Magnitude:** 1333.94 | **LOC:** 1747 | **CtrlFlow:** 98.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.0961%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNKMENU.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.152 IQR)
- **Top Global Matches:** file_cluster_8: 8.152, file_cluster_7: 9.17, file_cluster_1: 9.348
- **Magnitude:** 1237.3 | **LOC:** 1364 | **CtrlFlow:** 98.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.4336%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1CRA.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.07 IQR)
- **Top Global Matches:** file_cluster_8: 8.07, file_cluster_7: 9.099, file_cluster_1: 9.277
- **Magnitude:** 1235.36 | **LOC:** 1219 | **CtrlFlow:** 98.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.6213%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1DAC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.097 IQR)
- **Top Global Matches:** file_cluster_8: 8.097, file_cluster_7: 9.122, file_cluster_1: 9.3
- **Magnitude:** 1220.98 | **LOC:** 1246 | **CtrlFlow:** 98.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.5337%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_DBCRFUN.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.98 IQR)
- **Top Global Matches:** file_cluster_8: 7.98, file_cluster_7: 9.02, file_cluster_1: 9.199
- **Magnitude:** 1098.34 | **LOC:** 1082 | **CtrlFlow:** 98.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.6194%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_INQCUST.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.737 IQR)
- **Top Global Matches:** file_cluster_8: 7.737, file_cluster_7: 8.808, file_cluster_1: 8.989
- **Magnitude:** 943.84 | **LOC:** 829 | **CtrlFlow:** 98.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.9811%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BNK1CCA.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.945 IQR)
- **Top Global Matches:** file_cluster_8: 7.945, file_cluster_7: 8.986, file_cluster_1: 9.166
- **Magnitude:** 902.44 | **LOC:** 1045 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.3681%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_BANKDATA.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.372 IQR)
- **Top Global Matches:** file_cluster_8: 8.372, file_cluster_7: 9.356, file_cluster_1: 9.535
- **Magnitude:** 837.08 | **LOC:** 1586 | **CtrlFlow:** 96.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.6578%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.DATA.VSAM, HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_CREACC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.351 IQR)
- **Top Global Matches:** file_cluster_8: 8.351, file_cluster_7: 9.337, file_cluster_1: 9.516
- **Magnitude:** 792.06 | **LOC:** 1609 | **CtrlFlow:** 98.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.6114%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_INQACCCU.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.978 IQR)
- **Top Global Matches:** file_cluster_8: 7.978, file_cluster_7: 9.012, file_cluster_1: 9.193
- **Magnitude:** 752.92 | **LOC:** 1077 | **CtrlFlow:** 98.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.0593%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_INQACC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.03 IQR)
- **Top Global Matches:** file_cluster_8: 8.03, file_cluster_7: 9.056, file_cluster_1: 9.237
- **Magnitude:** 693.9 | **LOC:** 1131 | **CtrlFlow:** 97.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.8888%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_UPDCUST.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.278 IQR)
- **Top Global Matches:** file_cluster_8: 7.278, file_cluster_7: 8.409, file_cluster_1: 8.595
- **Magnitude:** 547.9 | **LOC:** 483 | **CtrlFlow:** 97.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.281%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_DELCUS.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.022 IQR)
- **Top Global Matches:** file_cluster_8: 8.022, file_cluster_7: 9.044, file_cluster_1: 9.226
- **Magnitude:** 498.42 | **LOC:** 1087 | **CtrlFlow:** 96.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.615%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_DELACC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.883 IQR)
- **Top Global Matches:** file_cluster_8: 7.883, file_cluster_7: 8.924, file_cluster_1: 9.106
- **Magnitude:** 465.74 | **LOC:** 916 | **CtrlFlow:** 96.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.7228%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_UPDACC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.414 IQR)
- **Top Global Matches:** file_cluster_8: 7.414, file_cluster_7: 8.521, file_cluster_1: 8.707
- **Magnitude:** 444.2 | **LOC:** 533 | **CtrlFlow:** 96.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.4793%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_CRDTAGY1.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.991 IQR)
- **Top Global Matches:** file_cluster_8: 6.991, file_cluster_7: 8.149, file_cluster_1: 8.339
- **Magnitude:** 140.4 | **LOC:** 330 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1035%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_CRDTAGY2.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.991 IQR)
- **Top Global Matches:** file_cluster_8: 6.991, file_cluster_7: 8.149, file_cluster_1: 8.339
- **Magnitude:** 140.4 | **LOC:** 330 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1035%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_CRDTAGY3.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.991 IQR)
- **Top Global Matches:** file_cluster_8: 6.991, file_cluster_7: 8.149, file_cluster_1: 8.339
- **Magnitude:** 140.4 | **LOC:** 329 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1035%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BUILD_CRDTAGY4.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.991 IQR)
- **Top Global Matches:** file_cluster_8: 6.991, file_cluster_7: 8.149, file_cluster_1: 8.339
- **Magnitude:** 140.4 | **LOC:** 332 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1035%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 34.483
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HERC01.LOADLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `BUILD_GETCOMPY.jcl` -> **Severity: 1416.565** (Blast Radius: 34.483 * Doc Risk: 41.0801%)
- `BUILD_GETSCODE.jcl` -> **Severity: 1228.557** (Blast Radius: 34.483 * Doc Risk: 35.6279%)
- `BUILD_ABNDPROC.jcl` -> **Severity: 664.887** (Blast Radius: 34.483 * Doc Risk: 19.2816%)
- `BUILD_CRDTAGY1.jcl` -> **Severity: 565.111** (Blast Radius: 34.483 * Doc Risk: 16.3881%)
- `BUILD_CRDTAGY2.jcl` -> **Severity: 565.111** (Blast Radius: 34.483 * Doc Risk: 16.3881%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
