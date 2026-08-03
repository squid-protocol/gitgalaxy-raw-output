# ARCHITECTURAL_BRIEF: CICS-Cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/CICS-Cobol` |
| **Timestamp** | `2026-08-03T19:27:46.132955+00:00` |
| **Scan Duration** | `0.19s` |
| **Git Branch** | `master` |
| **Git Commit** | `3fd4d46cabc39079ab198c52c235e58ab017beb7` |
| **Git Remote** | `https://github.com/mainframe-projects/CICS-Cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 51 malicious artifacts.

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
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 51 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 1520 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.4% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 51 | 1520 | 100.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.767`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 50 | 98.0% |
| file_cluster_9 | 1 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cbl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 88.8 | 42.8 | 41.7 | 35.4 |
| Error & Exception Exposure | 0.0 | 80.0 | 42.6 | 46.7 | 46.7 |
| Tech Debt Exposure | 0.0 | 100.0 | 97.0 | 99.9 | 100.0 |
| Testing Exposure | 1.1 | 4.0 | 2.6 | 2.5 | 2.4 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 68.5 | 93.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 86.1 | 1.7 | 0.0 | 0.0 |
| Specification Exposure | 46.7 | 100.0 | 97.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 46.7 | 100.0 | 95.1 | 99.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 39.9 | 4.8 | 2.4 | 3.3 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `CBL0101v01EstructuraInicial.COB` (Hits: 0)
- `CBL0102v01DivisionAmbiente.cbl` (Hits: 0)
- `CBL0103v01DivisionData.cbl` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **QG4CX001.cpy** (`QG4CX001.cpy`) — 1 inbound connections
2. **CBL0101v01EstructuraInicial.COB** (`CBL0101v01EstructuraInicial.COB`) — 0 inbound connections
3. **CBL0102v01DivisionAmbiente.cbl** (`CBL0102v01DivisionAmbiente.cbl`) — 0 inbound connections
4. **CBL0103v01DivisionData.cbl** (`CBL0103v01DivisionData.cbl`) — 0 inbound connections
5. **CBL0104v01ProcedureDivision.cbl** (`CBL0104v01ProcedureDivision.cbl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CBL0401v01ClausuleCopy.cbl** (`CBL0401v01ClausuleCopy.cbl`) — 1 outbound dependencies
2. **CBL0101v01EstructuraInicial.COB** (`CBL0101v01EstructuraInicial.COB`) — 0 outbound dependencies
3. **CBL0102v01DivisionAmbiente.cbl** (`CBL0102v01DivisionAmbiente.cbl`) — 0 outbound dependencies
4. **CBL0103v01DivisionData.cbl** (`CBL0103v01DivisionData.cbl`) — 0 outbound dependencies
5. **CBL0104v01ProcedureDivision.cbl** (`CBL0104v01ProcedureDivision.cbl`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `0000-MAIN` (@ `CBL0604v01PerformVariying.cbl`) -> Impact: **35.7** | LOC: 14
- `MAIN-PROCEDURE` (@ `CBL0501v01DeclaracioCondicionIF.cbl`) -> Impact: **34.2** | LOC: 24
- `MAIN-PROCEDURE` (@ `CBL0508v01CondicionVerb.cbl`) -> Impact: **16.1** | LOC: 22
  * *Intent:* ****************************************************************** * Author : * Date : 06/12/2018 * Purpose : * Tectonics : Evaluar verbo es un reempl...
- `0000-MAIN` (@ `CBL0805v01TableUseIndiceWithSet.cbl`) -> Impact: **15.3** | LOC: 26
- `A-PARA` (@ `CBL0601v01InOutLineLoop.cbl`) -> Impact: **15.2** | LOC: 4
- `0000-MAIN` (@ `CBL0804v01TableUseIndice.cbl`) -> Impact: **14.9** | LOC: 19
- `MAIN-PROCEDURE` (@ `CBL0503v01CondicionSigno.cbl`) -> Impact: **13.3** | LOC: 27
- `MAIN-PROCEDURE` (@ `CBL0502v01CondicionRelacion.cbl`) -> Impact: **13.2** | LOC: 14
  * *Intent:* ****************************************************************** * Author : * Date : 03/12/2018 * Purpose : * Tectonics : Equal to (=), * Greater th...
- `MAIN-PROCEDURE` (@ `CBL0506v01CondicionNot.cbl`) -> Impact: **12.7** | LOC: 14
- `MAIN-PROCEDURE` (@ `CBL0602v01PerformUntil.cbl`) -> Impact: **10.4** | LOC: 9

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `A-PARA` (@ `CBL0601v01InOutLineLoop.cbl`) -> **O(2^N) [Recursive]**
- `B-PARA` (@ `CBL0601v01InOutLineLoop.cbl`) -> **O(2^N) [Recursive]**
- `E-PARA` (@ `CBL0601v01InOutLineLoop.cbl`) -> **O(2^N) [Recursive]**
- `C-PARA` (@ `CBL0601v01InOutLineLoop.cbl`) -> **O(2^N) [Recursive]**
- `D-PARA` (@ `CBL0601v01InOutLineLoop.cbl`) -> **O(2^N) [Recursive]**
- `B-PARA` (@ `CBL0605v01GotoStatement.cbl`) -> **O(2^N) [Recursive]**
- `D-PARA` (@ `CBL0605v01GotoStatement.cbl`) -> **O(2^N) [Recursive]**
- `C-PARA` (@ `CBL0605v01GotoStatement.cbl`) -> **O(2^N) [Recursive]**
- `0000-MAIN` (@ `CBL0604v01PerformVariying.cbl`) -> **O(N^6)**
- `MAIN-PROCEDURE` (@ `CBL0501v01DeclaracioCondicionIF.cbl`) -> **O(N^5)**

### Highest Data Gravity (Database Complexity)
- `0000-MAIN` (@ `CBL0703v01StatementString.cbl`) -> DB Complexity: **10**
- `0000-MAIN` (@ `CBL0704v01StatementNotString.cbl`) -> DB Complexity: **10**
- `MAIN-PROCEDURE` (@ `CBL0206v01MultiplyVerb.cbl`) -> DB Complexity: **7**
- `MAIN-PROCEDURE` (@ `CBL0207v01DivideVerb.cbl`) -> DB Complexity: **7**
- `MAIN-PROCEDURE` (@ `CBL0203v01MoveVerb.cbl`) -> DB Complexity: **6**
- `0000-MAIN` (@ `CBL0805v01TableUseIndiceWithSet.cbl`) -> DB Complexity: **6**
- `0000-MAIN` (@ `CBL0803v01TableUseSubIndice.cbl`) -> DB Complexity: **5**
- `MAIN-PROCEDURE` (@ `CBL0303v01ClausuleUse.cbl`) -> DB Complexity: **4**
- `MAIN-PROCEDURE` (@ `CBL0304v01ClausuleComp.cbl`) -> DB Complexity: **4**
- `MAIN-PROCEDURE` (@ `CBL0305v01ClausuleComp-1.cbl`) -> DB Complexity: **4**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 51 | 691.64 | 42.8% | 97.01% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `CBL0101v01EstructuraInicial.COB` -> **100.0%** Exposure
- `CBL0102v01DivisionAmbiente.cbl` -> **100.0%** Exposure
- `CBL0601v01InOutLineLoop.cbl` -> **100.0%** Exposure
- `CBL0605v01GotoStatement.cbl` -> **100.0%** Exposure
- `CBL1001v01ManejoCICS.cbl` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `CBL0502v01CondicionRelacion.cbl` -> **99.9999%** Exposure
- `CBL0503v01CondicionSigno.cbl` -> **99.9999%** Exposure
- `CBL0805v01TableUseIndiceWithSet.cbl` -> **99.9851%** Exposure
- `CBL0703v01StatementString.cbl` -> **99.9201%** Exposure
- `CBL0704v01StatementNotString.cbl` -> **99.8455%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `CBL1001v01ManejoCICS.cbl` -> **8** Orphaned Functions | **0** Duplicates
- `CBL0601v01InOutLineLoop.cbl` -> **6** Orphaned Functions | **0** Duplicates
- `CBL0605v01GotoStatement.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `CBL0804v01TableUseIndice.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `CBL0805v01TableUseIndiceWithSet.cbl` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`CBL0604v01PerformVariying.cbl`** -> AI Confidence: **98.96%**
2. **`CBL0804v01TableUseIndice.cbl`** -> AI Confidence: **98.96%**
3. **`CBL0502v01CondicionRelacion.cbl`** -> AI Confidence: **98.89%**
4. **`CBL0503v01CondicionSigno.cbl`** -> AI Confidence: **98.89%**
5. **`CBL0508v01CondicionVerb.cbl`** -> AI Confidence: **98.89%**
6. **`CBL0807v01TableSearchAll.cbl`** -> AI Confidence: **98.89%**
7. **`CBL0602v01PerformUntil.cbl`** -> AI Confidence: **98.86%**
8. **`CBL0603v01PerformTimes.cbl`** -> AI Confidence: **98.86%**
9. **`CBL0501v01DeclaracioCondicionIF.cbl`** -> AI Confidence: **98.85%**
10. **`CBL0506v01CondicionNot.cbl`** -> AI Confidence: **98.85%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `CBL0807v01TableSearchAll.cbl` -> **0.0014%** Exposure
- `CBL0502v01CondicionRelacion.cbl` -> **0.0009%** Exposure
- `CBL0604v01PerformVariying.cbl` -> **0.0006%** Exposure
- `CBL0805v01TableUseIndiceWithSet.cbl` -> **0.0002%** Exposure
- `CBL0501v01DeclaracioCondicionIF.cbl` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `CBL0703v01StatementString.cbl` -> **39.913%** Exposure
- `CBL0704v01StatementNotString.cbl` -> **38.8159%** Exposure
- `CBL1001v01ManejoCICS.cbl` -> **18.478%** Exposure
- `CBL0206v01MultiplyVerb.cbl` -> **11.9745%** Exposure
- `CBL0207v01DivideVerb.cbl` -> **11.2047%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `CBL0304v01ClausuleComp.cbl` (COBOL) -> Cumulative Risk: **573.4**
- **Archetype:** `file_cluster_9` (Distance: 17.362 IQR)
- **Magnitude:** 8.06 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.1401%), Tech Debt (98.6851%), State Flux (93.9828%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 3.4)

### 2. `CBL0503v01CondicionSigno.cbl` (COBOL) -> Cumulative Risk: **560.47**
- **Archetype:** `file_cluster_8` (Distance: 10.92 IQR)
- **Magnitude:** 25.88 | **LOC:** 44 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (99.9282%), Tech Debt (99.4824%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 13.3)

### 3. `CBL0703v01StatementString.cbl` (COBOL) -> Cumulative Risk: **558.51**
- **Archetype:** `file_cluster_8` (Distance: 10.202 IQR)
- **Magnitude:** 12.42 | **LOC:** 39 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9682%), State Flux (99.9201%), Tech Debt (99.7879%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 5.9)

### 4. `CBL0704v01StatementNotString.cbl` (COBOL) -> Cumulative Risk: **547.8**
- **Archetype:** `file_cluster_8` (Distance: 10.103 IQR)
- **Magnitude:** 12.56 | **LOC:** 42 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9316%), State Flux (99.8455%), Tech Debt (99.6072%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 6.0)

### 5. `CBL0603v01PerformTimes.cbl` (COBOL) -> Cumulative Risk: **542.51**
- **Archetype:** `file_cluster_8` (Distance: 10.044 IQR)
- **Magnitude:** 17.0 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), State Flux (99.7268%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 10.4), `0100-CONTADOR` (Impact: 2.2)

### 6. `CBL0602v01PerformUntil.cbl` (COBOL) -> Cumulative Risk: **542.49**
- **Archetype:** `file_cluster_8` (Distance: 9.921 IQR)
- **Magnitude:** 17.0 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9842%), State Flux (99.7268%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 10.4), `CONTADOR` (Impact: 2.2)

### 7. `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL) -> Cumulative Risk: **533.76**
- **Archetype:** `file_cluster_8` (Distance: 10.561 IQR)
- **Magnitude:** 38.18 | **LOC:** 69 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.992%), State Flux (99.9851%), Documentation (99.9045%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 15.3), `200-TWO-DIMENSION` (Impact: 6.1), `100-ONE-DIMENSION` (Impact: 2.1)

### 8. `CBL0604v01PerformVariying.cbl` (COBOL) -> Cumulative Risk: **529.04**
- **Archetype:** `file_cluster_8` (Distance: 9.421 IQR)
- **Magnitude:** 41.38 | **LOC:** 41 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.9984%), State Flux (94.7846%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 35.7), `0100-CONTADOR` (Impact: 2.2)

### 9. `CBL0804v01TableUseIndice.cbl` (COBOL) -> Cumulative Risk: **517.21**
- **Archetype:** `file_cluster_8` (Distance: 10.012 IQR)
- **Magnitude:** 32.54 | **LOC:** 62 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9992%), Documentation (99.98%), State Flux (99.5796%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 14.9), `200-TWO-DIMENSION` (Impact: 6.1), `100-ONE-DIMENSION` (Impact: 2.1)

### 10. `CBL0105v01DeclararElementoGrupo.cbl` (COBOL) -> Cumulative Risk: **512.81**
- **Archetype:** `file_cluster_8` (Distance: 9.299 IQR)
- **Magnitude:** 5.9 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9907%), Tech Debt (99.9842%), State Flux (98.016%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 2.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `CBL0604v01PerformVariying.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.421 IQR)
- **Top Global Matches:** file_cluster_8: 9.421, file_cluster_7: 10.185, file_cluster_1: 10.403
- **Magnitude:** 41.38 | **LOC:** 41 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (76.2542%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 35.7 | O(N^6) | DB: 1)
  * `0100-CONTADOR` (Impact: 2.2 | O(N^3))
    * *Intent:* * * Inicia en uno y avanza de uno en uno, el tope es 20 y llega
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.561 IQR)
- **Top Global Matches:** file_cluster_8: 10.561, file_cluster_7: 11.248, file_cluster_13: 11.401
- **Magnitude:** 38.18 | **LOC:** 69 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (76.5275%), Tech Debt (99.992%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 15.3 | O(N^3) | DB: 6)
  * `200-TWO-DIMENSION` (Impact: 6.1 | O(N^2))
  * `100-ONE-DIMENSION` (Impact: 2.1 | O(N^3))
  * `300-MOSTRAR` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 19`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`, `orphaned_logic: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0501v01DeclaracioCondicionIF.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.073 IQR)
- **Top Global Matches:** file_cluster_8: 10.073, file_cluster_7: 10.87, file_cluster_17: 10.88
- **Magnitude:** 37.88 | **LOC:** 45 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (37.0654%), Tech Debt (98.3978%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 34.2 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 17`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0601v01InOutLineLoop.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.078 IQR)
- **Top Global Matches:** file_cluster_8: 9.078, file_cluster_7: 9.98, file_cluster_17: 10.137
- **Magnitude:** 35.78 | **LOC:** 52 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (48.2765%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `A-PARA` (Impact: 15.2 | O(2^N))
  * `B-PARA` (Impact: 4.2 | O(2^N))
  * `E-PARA` (Impact: 4.2 | O(2^N))
  * `C-PARA` (Impact: 4.1 | O(2^N))
  * `D-PARA` (Impact: 4.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 15`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 6`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0804v01TableUseIndice.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.012 IQR)
- **Top Global Matches:** file_cluster_8: 10.012, file_cluster_7: 10.738, file_cluster_13: 10.936
- **Magnitude:** 32.54 | **LOC:** 62 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (70.928%), Tech Debt (99.9992%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 14.9 | O(N^3) | DB: 3)
  * `200-TWO-DIMENSION` (Impact: 6.1 | O(N^2))
  * `100-ONE-DIMENSION` (Impact: 2.1 | O(N^3))
  * `300-MOSTRAR` (Impact: 1.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 14`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `orphaned_logic: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0807v01TableSearchAll.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.983 IQR)
- **Top Global Matches:** file_cluster_8: 9.983, file_cluster_7: 10.732, file_cluster_1: 10.924
- **Magnitude:** 31.46 | **LOC:** 74 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (99.9783%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 8.8 | O(N^3) | DB: 2)
  * `100-ONE-BUSCAR` (Impact: 8.0 | O(N^4) | DB: 2)
  * `050-SHOW-BEFORE` (Impact: 1.9 | O(N^2))
  * `150-SHOW-AFTER` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 20`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 10`, `orphaned_logic: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL1001v01ManejoCICS.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.741 IQR)
- **Top Global Matches:** file_cluster_8: 8.741, file_cluster_7: 9.619, file_cluster_1: 9.808
- **Magnitude:** 28.32 | **LOC:** 67 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (48.7807%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `0000-PRINCIPAL` (Impact: 6.2 | O(N^2))
  * `2000-PROCESO` (Impact: 6.2 | O(N^2))
  * `2200-CONCATENA-DATOS` (Impact: 2.9 | O(N^4) | DB: 4)
  * `SPECIAL-NAMES` (Impact: 2.8 | O(N^3))
    * *Intent:* ****************************************************************** * Author : ALDV * Date : 28 MAY 2...
  * `1000-INICIO` (Impact: 1.6 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `orphaned_logic: 8`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0503v01CondicionSigno.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.92 IQR)
- **Top Global Matches:** file_cluster_8: 10.92, file_cluster_7: 11.574, file_cluster_17: 11.663
- **Magnitude:** 25.88 | **LOC:** 44 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (88.785%), Tech Debt (99.4824%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 13.3 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0502v01CondicionRelacion.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.357 IQR)
- **Top Global Matches:** file_cluster_8: 11.357, file_cluster_17: 11.961, file_cluster_7: 12.033
- **Magnitude:** 22.66 | **LOC:** 37 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (82.7101%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 13.2 | O(N^4) | DB: 3)
    * *Intent:* ****************************************************************** * Author : * Date : 03/12/2018 * ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0605v01GotoStatement.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.431 IQR)
- **Top Global Matches:** file_cluster_8: 8.431, file_cluster_7: 9.33, file_cluster_1: 9.517
- **Magnitude:** 22.64 | **LOC:** 43 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (42.4652%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `B-PARA` (Impact: 8.2 | O(2^N))
  * `D-PARA` (Impact: 4.2 | O(2^N))
  * `C-PARA` (Impact: 4.1 | O(2^N))
  * `0000-MAIN` (Impact: 2.4 | O(N^3) | DB: 1)
  * `0100-CONTADOR` (Impact: 2.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 14`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0508v01CondicionVerb.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.079 IQR)
- **Top Global Matches:** file_cluster_8: 10.079, file_cluster_7: 10.857, file_cluster_17: 10.919
- **Magnitude:** 20.62 | **LOC:** 41 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (63.1454%), Tech Debt (99.7879%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 16.1 | O(N^4) | DB: 2)
    * *Intent:* ****************************************************************** * Author : * Date : 06/12/2018 * ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0806v01TableSearch.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.202 IQR)
- **Top Global Matches:** file_cluster_8: 9.202, file_cluster_7: 10.022, file_cluster_1: 10.226
- **Magnitude:** 18.62 | **LOC:** 60 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (47.2251%), Tech Debt (99.854%)
**Top Internal Functions/Classes:**
  * `100-ONE-DIMENSION` (Impact: 8.2 | O(N^4) | DB: 1)
  * `0000-MAIN` (Impact: 4.7 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0506v01CondicionNot.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.216 IQR)
- **Top Global Matches:** file_cluster_8: 10.216, file_cluster_7: 10.981, file_cluster_17: 11.007
- **Magnitude:** 17.16 | **LOC:** 36 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (53.2563%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 12.7 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0602v01PerformUntil.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.921 IQR)
- **Top Global Matches:** file_cluster_8: 9.921, file_cluster_7: 10.652, file_cluster_17: 10.819
- **Magnitude:** 17.0 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (80.2184%), Tech Debt (99.9842%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 10.4 | O(N^3) | DB: 1)
  * `CONTADOR` (Impact: 2.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0603v01PerformTimes.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.044 IQR)
- **Top Global Matches:** file_cluster_8: 10.044, file_cluster_7: 10.767, file_cluster_17: 10.93
- **Magnitude:** 17.0 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (80.2184%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 10.4 | O(N^3) | DB: 1)
  * `0100-CONTADOR` (Impact: 2.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0901v02AccesoSecuencialFiles.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.518 IQR)
- **Top Global Matches:** file_cluster_8: 6.518, file_cluster_7: 7.707, file_cluster_1: 7.881
- **Magnitude:** 16.94 | **LOC:** 90 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.1228%), Tech Debt (99.8783%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 6.2 | O(N^3))
  * `SPECIAL-NAMES` (Impact: 4.7 | O(N^3))
    * *Intent:* ****************************************************************** * Project : Evaluation COBOL PC *...
  * `1000-INICIO` (Impact: 2.2 | O(N^3) | DB: 1)
  * `4000-FINAL` (Impact: 1.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0902v01AccesoAleatorio.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.685 IQR)
- **Top Global Matches:** file_cluster_8: 6.685, file_cluster_7: 7.842, file_cluster_1: 8.019
- **Magnitude:** 16.08 | **LOC:** 79 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (19.3321%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 6.2 | O(N^3))
  * `SPECIAL-NAMES` (Impact: 4.2 | O(N^3))
    * *Intent:* ****************************************************************** * Project : Evaluation COBOL PC *...
  * `1000-INICIO` (Impact: 2.1 | O(N^3) | DB: 1)
  * `4000-FINAL` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0903v01AccesoDinamico.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.166 IQR)
- **Top Global Matches:** file_cluster_8: 6.166, file_cluster_7: 7.452, file_cluster_1: 7.594
- **Magnitude:** 15.44 | **LOC:** 80 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.0489%), Tech Debt (99.9498%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 6.2 | O(N^3))
  * `SPECIAL-NAMES` (Impact: 4.4 | O(N^3))
    * *Intent:* ****************************************************************** * Project : Evaluation COBOL PC *...
  * `1000-INICIO` (Impact: 2.1 | O(N^3))
  * `4000-FINAL` (Impact: 1.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0704v01StatementNotString.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.103 IQR)
- **Top Global Matches:** file_cluster_8: 10.103, file_cluster_7: 10.87, file_cluster_13: 10.976
- **Magnitude:** 12.56 | **LOC:** 42 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (57.0947%), Tech Debt (99.6072%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 6.0 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 14`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0703v01StatementString.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.202 IQR)
- **Top Global Matches:** file_cluster_8: 10.202, file_cluster_7: 10.959, file_cluster_13: 11.053
- **Magnitude:** 12.42 | **LOC:** 39 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (63.1454%), Tech Debt (99.7879%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 5.9 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0207v01DivideVerb.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.148 IQR)
- **Top Global Matches:** file_cluster_8: 9.148, file_cluster_7: 9.989, file_cluster_1: 10.17
- **Magnitude:** 11.8 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (25.3506%), Tech Debt (88.0797%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 3.8 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0901v01AccesoSecuencial.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.01 IQR)
- **Top Global Matches:** file_cluster_8: 7.01, file_cluster_7: 8.106, file_cluster_1: 8.293
- **Magnitude:** 11.62 | **LOC:** 63 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (19.0858%), Tech Debt (99.9909%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 6.2 | O(N^3))
  * `1000-INICIO` (Impact: 2.1 | O(N^3) | DB: 1)
  * `4000-FINAL` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0206v01MultiplyVerb.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.358 IQR)
- **Top Global Matches:** file_cluster_8: 9.358, file_cluster_7: 10.175, file_cluster_1: 10.358
- **Magnitude:** 11.38 | **LOC:** 55 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (30.615%), Tech Debt (93.1734%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 3.5 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0505v01CondicionName.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.497 IQR)
- **Top Global Matches:** file_cluster_8: 9.497, file_cluster_7: 10.28, file_cluster_1: 10.483
- **Magnitude:** 11.26 | **LOC:** 40 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (61.7337%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 6.8 | O(N^3) | DB: 2)
    * *Intent:* ****************************************************************** * Author : * Date : 05/12/2018 * ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0504v01CondicionClass.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.896 IQR)
- **Top Global Matches:** file_cluster_8: 7.896, file_cluster_7: 8.862, file_cluster_1: 9.058
- **Magnitude:** 10.48 | **LOC:** 38 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (37.7541%), Tech Debt (99.8968%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 9.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `CBL0401v01ClausuleCopy.cbl` (COBOL) | Magnitude: 7.7 | Delta: **0.437 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 16, debug_prints: 10, state_mutation: 4
- `CBL0502v01CondicionRelacion.cbl` (COBOL) | Magnitude: 22.66 | Delta: **0.604 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, state_mutation: 9, debug_prints: 5
- `CBL0503v01CondicionSigno.cbl` (COBOL) | Magnitude: 25.88 | Delta: **0.654 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 15, state_mutation: 12, debug_prints: 9
- `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL) | Magnitude: 38.18 | Delta: **0.687 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 19, debug_prints: 13, branch: 12
- `CBL0603v01PerformTimes.cbl` (COBOL) | Magnitude: 17.0 | Delta: **0.723 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, branch: 4, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `CBL0304v01ClausuleComp.cbl` (COBOL) | Magnitude: 8.06 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 19, debug_prints: 13, state_mutation: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `CBL0601v01InOutLineLoop.cbl` -> **Severity: 1928.6** (Blast Radius: 19.286 * Doc Risk: 100.0%)
- `CBL0602v01PerformUntil.cbl` -> **Severity: 1928.6** (Blast Radius: 19.286 * Doc Risk: 100.0%)
- `CBL0603v01PerformTimes.cbl` -> **Severity: 1928.6** (Blast Radius: 19.286 * Doc Risk: 100.0%)
- `CBL0605v01GotoStatement.cbl` -> **Severity: 1928.6** (Blast Radius: 19.286 * Doc Risk: 100.0%)
- `CBL0604v01PerformVariying.cbl` -> **Severity: 1928.598** (Blast Radius: 19.286 * Doc Risk: 99.9999%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
