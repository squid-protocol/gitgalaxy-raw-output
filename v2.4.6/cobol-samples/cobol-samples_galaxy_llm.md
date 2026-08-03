# ARCHITECTURAL_BRIEF: cobol-samples
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cobol-samples` |
| **Timestamp** | `2026-08-03T19:28:41.488051+00:00` |
| **Scan Duration** | `0.19s` |
| **Git Branch** | `main` |
| **Git Commit** | `11ad5f8c9fc80d0f3fd913ea30afc48bd506541d` |
| **Git Remote** | `https://github.com/neopragma/cobol-samples.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 19 malicious artifacts.

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
| Total Artifacts | 53 |
| Analyzed Artifacts (Scanned) | 35 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 1522 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.0% |
| Dominant Lang | COBOL |

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
| MARKDOWN | 16 | 0 | 45.7% |
| COBOL | 15 | 1458 | 42.9% |
| SHELL | 3 | 63 | 8.6% |
| BINARY_THREAT | 1 | 1 | 2.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.529`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 15 | 42.9% |
| file_cluster_17 | 2 | 5.7% |
| file_cluster_12 | 1 | 2.9% |
| Unknown | 1 | 2.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 45.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `no_extension`: 13x Excluded (Binary Format Detected), 3x Unsupported Format (.undeterminable), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.0 | 40.7 | 35.4 | 0.0 |
| Error & Exception Exposure | 0.0 | 94.5 | 38.9 | 25.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.9 | 2.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 8.8 | 1.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 83.0 | 99.8 | 100.0 |
| Commented Logic Exposure | 0.0 | 45.6 | 5.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 88.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 83.3 | 30.8 | 26.2 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 94.8 | 5.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 1.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/main/cobol/CPSEQFR.CBL` (Hits: 15)
- `src/main/cobol/CPSEQVR.CBL` (Hits: 8)
- `compile` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ATTRACT-notes.md** (`ATTRACT-notes.md`) — 0 inbound connections
2. **BRAKES-notes.md** (`BRAKES-notes.md`) — 0 inbound connections
3. **COND88-notes.md** (`COND88-notes.md`) — 0 inbound connections
4. **CPSEQFR-notes.md** (`CPSEQFR-notes.md`) — 0 inbound connections
5. **CPSEQVR-notes.md** (`CPSEQVR-notes.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compile** (`compile`) — 1 outbound dependencies
2. **ATTRACT-notes.md** (`ATTRACT-notes.md`) — 0 outbound dependencies
3. **BRAKES-notes.md** (`BRAKES-notes.md`) — 0 outbound dependencies
4. **COND88-notes.md** (`COND88-notes.md`) — 0 outbound dependencies
5. **CPSEQFR-notes.md** (`CPSEQFR-notes.md`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Anonymous_Block_[Truncated]` (@ `compile`) -> Impact: **30.6** | LOC: 46
- `PRINT-INVOICE-DETAILS` (@ `src/main/cobol/INVCALC.CBL`) -> Impact: **27.1** | LOC: 42
- `Anonymous_Block` (@ `compile-all`) -> Impact: **8.3** | LOC: 6
- `ComputeAttraction` (@ `src/main/cobol/ATTRACT.CBL`) -> Impact: **6.5** | LOC: 9
- `__global_context__` (@ `compile`) -> Impact: **3.6** | LOC: 15
- `SolicitAttributesOfBody` (@ `src/main/cobol/ATTRACT.CBL`) -> Impact: **2.8** | LOC: 25
- `VerifyAttributesOfBody` (@ `src/main/cobol/ATTRACT.CBL`) -> Impact: **1.9** | LOC: 8
- `__global_context__` (@ `run`) -> Impact: **1.8** | LOC: 8
- `INVALID-INVOICE-DATA` (@ `src/main/cobol/INVCALC.CBL`) -> Impact: **1.6** | LOC: 3
- `show_help` (@ `compile`) -> Impact: **1.4** | LOC: 8

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `PRINT-INVOICE-DETAILS` (@ `src/main/cobol/INVCALC.CBL`) -> **O(N^4)**
- `__global_context__` (@ `compile`) -> **O(N^3)**
- `ComputeAttraction` (@ `src/main/cobol/ATTRACT.CBL`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `compile`) -> DB Complexity: **14**
- `PRINT-INVOICE-DETAILS` (@ `src/main/cobol/INVCALC.CBL`) -> DB Complexity: **12**
- `Anonymous_Block` (@ `compile-all`) -> DB Complexity: **11**
- `show_help` (@ `compile`) -> DB Complexity: **9**
- `SolicitAttributesOfBody` (@ `src/main/cobol/ATTRACT.CBL`) -> DB Complexity: **7**
- `ComputeAttraction` (@ `src/main/cobol/ATTRACT.CBL`) -> DB Complexity: **3**
- `VerifyAttributesOfBody` (@ `src/main/cobol/ATTRACT.CBL`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/main/cobol` | 15 | 835.06 | 44.24% | 2.85% |
| `__monolith__` | 20 | 597.0 | 5.45% | 14.9% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `compile-all` -> **100.0%** Exposure
- `run` -> **100.0%** Exposure
- `compile` -> **97.9619%** Exposure
- `src/main/cobol/INVCALC.CBL` -> **42.822%** Exposure
### Highest State Flux (Mutation/Volatility)
- `compile` -> **100.0%** Exposure
- `compile-all` -> **100.0%** Exposure
- `src/main/cobol/COND88.CBL` -> **100.0%** Exposure
- `src/main/cobol/HEX2TEXT.CBL` -> **100.0%** Exposure
- `src/main/cobol/IFEVAL.CBL` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `compile` -> **2** Orphaned Functions | **0** Duplicates
- `src/main/cobol/INVCALC.CBL` -> **2** Orphaned Functions | **0** Duplicates
- `compile-all` -> **1** Orphaned Functions | **0** Duplicates
- `run` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/main/cobol/COND88.CBL`** -> AI Confidence: **99.29%**
2. **`src/main/cobol/IFEVAL.CBL`** -> AI Confidence: **99.29%**
3. **`src/main/cobol/NOTBOOL.CBL`** -> AI Confidence: **99.29%**
4. **`compile-all`** -> AI Confidence: **99.11%**
5. **`compile`** -> AI Confidence: **99.06%**
6. **`src/main/cobol/CPSEQFR.CBL`** -> AI Confidence: **99.06%**
7. **`src/main/cobol/CPSEQVR.CBL`** -> AI Confidence: **99.06%**
8. **`src/main/cobol/INVCALC.CBL`** -> AI Confidence: **99.06%**
9. **`src/main/cobol/ATTRACT.CBL`** -> AI Confidence: **98.85%**
10. **`src/main/cobol/HEX2TEXT.CBL`** -> AI Confidence: **98.85%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/main/cobol/INVCALC.CBL` -> **20.0%** Exposure
- `src/main/cobol/ATTRACT.CBL` -> **0.0101%** Exposure
### Algorithmic DoS Exposure
- `src/main/cobol/INVCALC.CBL` -> **94.7546%** Exposure
- `src/main/cobol/ATTRACT.CBL` -> **8.735%** Exposure
- `compile` -> **4.0827%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/main/cobol/INVCALC.CBL` (COBOL) -> Cumulative Risk: **523.68**
- **Archetype:** `file_cluster_8` (Distance: 11.705 IQR)
- **Magnitude:** 105.64 | **LOC:** 175 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (94.7546%), Cognitive Load (66.9845%)
- **Heaviest Functions:** `PRINT-INVOICE-DETAILS` (Impact: 27.1), `INVALID-INVOICE-DATA` (Impact: 1.6)

### 2. `compile` (SHELL) -> Cumulative Risk: **498.18**
- **Archetype:** `file_cluster_8` (Distance: 12.237 IQR)
- **Magnitude:** 61.62 | **LOC:** 70 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.0315%), Tech Debt (97.9619%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 30.6), `__global_context__` (Impact: 3.6), `show_help` (Impact: 1.4)

### 3. `src/main/cobol/NOTBOOL.CBL` (COBOL) -> Cumulative Risk: **434.62**
- **Archetype:** `file_cluster_17` (Distance: 18.105 IQR)
- **Magnitude:** 103.68 | **LOC:** 185 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (88.5707%), Safety Score (86.2311%)

### 4. `src/main/cobol/HEX2TEXT.CBL` (COBOL) -> Cumulative Risk: **415.11**
- **Archetype:** `file_cluster_8` (Distance: 10.952 IQR)
- **Magnitude:** 32.7 | **LOC:** 43 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (83.2577%), Cognitive Load (83.2018%)

### 5. `src/main/cobol/IFEVAL.CBL` (COBOL) -> Cumulative Risk: **402.83**
- **Archetype:** `file_cluster_8` (Distance: 13.722 IQR)
- **Magnitude:** 130.9 | **LOC:** 153 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.4981%), Cognitive Load (89.1414%)

### 6. `src/main/cobol/COND88.CBL` (COBOL) -> Cumulative Risk: **400.06**
- **Archetype:** `file_cluster_8` (Distance: 13.151 IQR)
- **Magnitude:** 82.42 | **LOC:** 100 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (90.4954%), Safety Score (81.1095%)

### 7. `compile-all` (SHELL) -> Cumulative Risk: **360.45**
- **Archetype:** `file_cluster_12` (Distance: 13.381 IQR)
- **Magnitude:** 15.86 | **LOC:** 14 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Safety Score (93.9509%), Spec Match (53.3333%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 8.3), `__global_context__` (Impact: 1.4)

### 8. `src/main/cobol/MOVEME.CBL` (COBOL) -> Cumulative Risk: **346.88**
- **Archetype:** `file_cluster_8` (Distance: 10.833 IQR)
- **Magnitude:** 80.48 | **LOC:** 230 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9947%), Documentation (61.124%), Cognitive Load (39.5252%)

### 9. `src/main/cobol/REFORMER.CBL` (COBOL) -> Cumulative Risk: **344.85**
- **Archetype:** `file_cluster_8` (Distance: 12.067 IQR)
- **Magnitude:** 76.14 | **LOC:** 211 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Cognitive Load (59.593%), Documentation (34.3751%)

### 10. `src/main/cobol/ATTRACT.CBL` (COBOL) -> Cumulative Risk: **331.97**
- **Archetype:** `file_cluster_17` (Distance: 13.636 IQR)
- **Magnitude:** 40.8 | **LOC:** 184 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.799%), Documentation (38.8533%), Dead Code (34.25%)
- **Heaviest Functions:** `ComputeAttraction` (Impact: 6.5), `SolicitAttributesOfBody` (Impact: 2.8), `VerifyAttributesOfBody` (Impact: 1.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `TESTIO2.Output.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/IFEVAL.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.722 IQR)
- **Top Global Matches:** file_cluster_8: 13.722, file_cluster_17: 14.111, file_cluster_11: 14.163
- **Magnitude:** 130.9 | **LOC:** 153 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.1414%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 114`
* *Architecture:* None
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/INVCALC.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.705 IQR)
- **Top Global Matches:** file_cluster_8: 11.705, file_cluster_7: 12.353, file_cluster_17: 12.36
- **Magnitude:** 105.64 | **LOC:** 175 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (66.9845%), Tech Debt (42.822%)
**Top Internal Functions/Classes:**
  * `PRINT-INVOICE-DETAILS` (Impact: 27.1 | O(N^4) | DB: 12)
  * `INVALID-INVOICE-DATA` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 22`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/NOTBOOL.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_17` (Drift: 18.105 IQR)
- **Top Global Matches:** file_cluster_17: 18.105, file_cluster_11: 18.202, file_cluster_0: 18.211
- **Magnitude:** 103.68 | **LOC:** 185 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.5707%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 87`, `dead_code: 5`
* *Architecture:* None
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/COND88.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.151 IQR)
- **Top Global Matches:** file_cluster_8: 13.151, file_cluster_17: 13.586, file_cluster_0: 13.644
- **Magnitude:** 82.42 | **LOC:** 100 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.4954%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`
* *Architecture:* None
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/MOVEME.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.833 IQR)
- **Top Global Matches:** file_cluster_8: 10.833, file_cluster_0: 11.446, file_cluster_7: 11.465
- **Magnitude:** 80.48 | **LOC:** 230 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (39.5252%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 80`, `args: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`, `dead_code: 1`
* *Architecture:* `api: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/REFORMER.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.067 IQR)
- **Top Global Matches:** file_cluster_8: 12.067, file_cluster_0: 12.29, file_cluster_17: 12.368
- **Magnitude:** 76.14 | **LOC:** 211 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (59.593%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 25`, `args: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `dead_code: 2`
* *Architecture:* `api: 4`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.237 IQR)
- **Top Global Matches:** file_cluster_8: 12.237, file_cluster_13: 12.256, file_cluster_12: 12.366
- **Magnitude:** 61.62 | **LOC:** 70 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (99.0315%), Tech Debt (97.9619%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 30.6 | O(N^1) | DB: 14)
  * `__global_context__` (Impact: 3.6 | O(N^3))
  * `show_help` (Impact: 1.4 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 15`, `args: 6`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` envvars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/ATTRACT.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.636 IQR)
- **Top Global Matches:** file_cluster_17: 13.636, file_cluster_8: 13.68, file_cluster_0: 13.721
- **Magnitude:** 40.8 | **LOC:** 184 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (32.6716%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ComputeAttraction` (Impact: 6.5 | O(N^3) | DB: 3)
  * `SolicitAttributesOfBody` (Impact: 2.8 | O(N^2) | DB: 7)
  * `VerifyAttributesOfBody` (Impact: 1.9 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 33`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`, `dead_code: 4`
* *Architecture:* None
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/HEX2TEXT.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.952 IQR)
- **Top Global Matches:** file_cluster_8: 10.952, file_cluster_7: 11.632, file_cluster_0: 11.65
- **Magnitude:** 32.7 | **LOC:** 43 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (83.2018%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 7`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/DATE1.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.583 IQR)
- **Top Global Matches:** file_cluster_8: 7.583, file_cluster_7: 8.581, file_cluster_1: 8.811
- **Magnitude:** 31.74 | **LOC:** 176 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 13`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/STRINGIT.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.577 IQR)
- **Top Global Matches:** file_cluster_8: 8.577, file_cluster_7: 9.56, file_cluster_1: 9.736
- **Magnitude:** 30.9 | **LOC:** 113 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 19`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/DATE2.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.164 IQR)
- **Top Global Matches:** file_cluster_8: 7.164, file_cluster_7: 8.26, file_cluster_1: 8.455
- **Magnitude:** 28.9 | **LOC:** 180 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CPSEQVR.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.87 IQR)
- **Top Global Matches:** file_cluster_8: 9.87, file_cluster_17: 10.574, file_cluster_0: 10.617
- **Magnitude:** 28.34 | **LOC:** 83 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (37.9296%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `io: 8`
* *Defense:* `safety: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CPSEQFR.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.973 IQR)
- **Top Global Matches:** file_cluster_8: 9.973, file_cluster_17: 10.616, file_cluster_0: 10.67
- **Magnitude:** 25.36 | **LOC:** 86 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (28.0663%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `io: 15`
* *Defense:* `safety: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/BRAKES.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.565 IQR)
- **Top Global Matches:** file_cluster_8: 9.565, file_cluster_7: 10.403, file_cluster_17: 10.607
- **Magnitude:** 20.5 | **LOC:** 60 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (35.4344%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/HELLO.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.687 IQR)
- **Top Global Matches:** file_cluster_8: 6.687, file_cluster_7: 7.909, file_cluster_1: 8.099
- **Magnitude:** 16.56 | **LOC:** 44 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.9203%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile-all` (SHELL | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_12` (Drift: 13.381 IQR)
- **Top Global Matches:** file_cluster_12: 13.381, file_cluster_8: 13.4, file_cluster_17: 13.478
- **Magnitude:** 15.86 | **LOC:** 14 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 8.3 | O(N^1) | DB: 11)
  * `__global_context__` (Impact: 1.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run` (SHELL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.408 IQR)
- **Top Global Matches:** file_cluster_8: 6.408, file_cluster_7: 7.762, file_cluster_1: 7.786
- **Magnitude:** 1.88 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MOVEME-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.7 | **LOC:** 85 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `HOURGLASS-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.56 | **LOC:** 78 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.26 | **LOC:** 63 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `DATE2-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ATTRACT-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.04 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `BRAKES-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 28.571
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `compile-all` (SHELL) | Magnitude: 15.86 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 7, state_mutation: 6, safety_bypasses: 4, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/main/cobol/ATTRACT.CBL` (COBOL) | Magnitude: 40.8 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 33, state_mutation: 27, debug_prints: 20
- `src/main/cobol/NOTBOOL.CBL` (COBOL) | Magnitude: 103.68 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 87, indent_spaces: 84, branch: 33, safety: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `compile` (SHELL) | Magnitude: 61.62 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 23, branch: 19, structural_boundaries: 15
- `src/main/cobol/REFORMER.CBL` (COBOL) | Magnitude: 76.14 | Delta: **0.223 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 157, state_mutation: 54, structural_boundaries: 25, debug_prints: 20
- `src/main/cobol/IFEVAL.CBL` (COBOL) | Magnitude: 130.9 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 114, indent_spaces: 95, branch: 35, safety: 10
- `src/main/cobol/COND88.CBL` (COBOL) | Magnitude: 82.42 | Delta: **0.435 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 71, state_mutation: 66, branch: 25, safety: 7
- `src/main/cobol/MOVEME.CBL` (COBOL) | Magnitude: 80.48 | Delta: **0.613 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 174, structural_boundaries: 80, debug_prints: 75, state_mutation: 52

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/main/cobol/HEX2TEXT.CBL` -> **Severity: 2378.756** (Blast Radius: 28.571 * Doc Risk: 83.2577%)
- `src/main/cobol/HELLO.CBL` -> **Severity: 1878.523** (Blast Radius: 28.571 * Doc Risk: 65.7493%)
- `src/main/cobol/MOVEME.CBL` -> **Severity: 1746.374** (Blast Radius: 28.571 * Doc Risk: 61.124%)
- `src/main/cobol/INVCALC.CBL` -> **Severity: 1504.623** (Blast Radius: 28.571 * Doc Risk: 52.6626%)
- `src/main/cobol/BRAKES.CBL` -> **Severity: 1329.851** (Blast Radius: 28.571 * Doc Risk: 46.5455%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
