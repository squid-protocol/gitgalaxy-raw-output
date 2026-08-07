# ARCHITECTURAL_BRIEF: CICS-Cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/CICS-Cobol` |
| **Timestamp** | `2026-08-07T03:50:03.972049+00:00` |
| **Scan Duration** | `0.14s` |
| **Git Branch** | `master` |
| **Git Commit** | `3fd4d46cabc39079ab198c52c235e58ab017beb7` |
| **Git Remote** | `https://github.com/mainframe-projects/CICS-Cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 51 malicious artifacts.

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
| Cognitive Load Exposure | 5.0 | 82.7 | 30.2 | 23.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 95.3 | 84.5 | 87.8 | 87.9 |
| Tech Debt Exposure | 0.0 | 100.0 | 97.0 | 99.9 | 100.0 |
| Testing Exposure | 1.1 | 2.8 | 2.4 | 2.4 | 2.4 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 68.5 | 93.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 86.1 | 1.7 | 0.0 | 0.0 |
| Specification Exposure | 46.7 | 100.0 | 97.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 22.9 | 61.0 | 41.8 | 41.2 | 52.6 |
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

- `MAIN-PROCEDURE` (@ `CBL0501v01DeclaracioCondicionIF.cbl`) -> Impact: **12.2** | LOC: 24
- `0000-MAIN` (@ `CBL0604v01PerformVariying.cbl`) -> Impact: **10.7** | LOC: 14
- `0000-MAIN` (@ `CBL0805v01TableUseIndiceWithSet.cbl`) -> Impact: **8.3** | LOC: 26
- `0000-MAIN` (@ `CBL0804v01TableUseIndice.cbl`) -> Impact: **8.0** | LOC: 19
- `MAIN-PROCEDURE` (@ `CBL0503v01CondicionSigno.cbl`) -> Impact: **7.3** | LOC: 27
- `MAIN-PROCEDURE` (@ `CBL0508v01CondicionVerb.cbl`) -> Impact: **7.1** | LOC: 22
  * *Intent:* ****************************************************************** * Author : * Date : 06/12/2018 * Purpose : * Tectonics : Evaluar verbo es un reempl...
- `MAIN-PROCEDURE` (@ `CBL0506v01CondicionNot.cbl`) -> Impact: **6.7** | LOC: 14
- `MAIN-PROCEDURE` (@ `CBL0502v01CondicionRelacion.cbl`) -> Impact: **5.7** | LOC: 14
  * *Intent:* ****************************************************************** * Author : * Date : 03/12/2018 * Purpose : * Tectonics : Equal to (=), * Greater th...
- `MAIN-PROCEDURE` (@ `CBL0602v01PerformUntil.cbl`) -> Impact: **5.5** | LOC: 9
- `0000-MAIN` (@ `CBL0603v01PerformTimes.cbl`) -> Impact: **5.5** | LOC: 9

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 51 | 453.34 | 30.21% | 97.01% |

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `CBL0304v01ClausuleComp.cbl` (COBOL) -> Cumulative Risk: **535.55**
- **Archetype:** `file_cluster_9` (Distance: 17.362 IQR)
- **Magnitude:** 7.06 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (98.6851%), State Flux (93.9828%), Safety Score (86.6218%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 2.4)

### 2. `CBL0503v01CondicionSigno.cbl` (COBOL) -> Cumulative Risk: **520.9**
- **Archetype:** `file_cluster_8` (Distance: 10.92 IQR)
- **Magnitude:** 19.88 | **LOC:** 44 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.4824%), Safety Score (94.0201%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 7.3)

### 3. `CBL0502v01CondicionRelacion.cbl` (COBOL) -> Cumulative Risk: **517.82**
- **Archetype:** `file_cluster_8` (Distance: 11.357 IQR)
- **Magnitude:** 15.16 | **LOC:** 37 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9313%), Safety Score (86.0678%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 5.7)

### 4. `CBL0603v01PerformTimes.cbl` (COBOL) -> Cumulative Risk: **507.05**
- **Archetype:** `file_cluster_8` (Distance: 10.044 IQR)
- **Magnitude:** 11.1 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.7268%), Safety Score (92.2371%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 5.5), `0100-CONTADOR` (Impact: 1.2)

### 5. `CBL0602v01PerformUntil.cbl` (COBOL) -> Cumulative Risk: **507.04**
- **Archetype:** `file_cluster_8` (Distance: 9.921 IQR)
- **Magnitude:** 11.1 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9842%), State Flux (99.7268%), Safety Score (92.2371%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 5.5), `CONTADOR` (Impact: 1.2)

### 6. `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL) -> Cumulative Risk: **489.99**
- **Archetype:** `file_cluster_8` (Distance: 10.561 IQR)
- **Magnitude:** 27.58 | **LOC:** 69 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.992%), State Flux (99.9851%), Safety Score (89.1811%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 8.3), `200-TWO-DIMENSION` (Impact: 4.1), `300-MOSTRAR` (Impact: 1.2)

### 7. `CBL0604v01PerformVariying.cbl` (COBOL) -> Cumulative Risk: **489.81**
- **Archetype:** `file_cluster_8` (Distance: 9.421 IQR)
- **Magnitude:** 15.38 | **LOC:** 41 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9984%), State Flux (94.7846%), Safety Score (89.5456%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 10.7), `0100-CONTADOR` (Impact: 1.2)

### 8. `CBL0508v01CondicionVerb.cbl` (COBOL) -> Cumulative Risk: **485.5**
- **Archetype:** `file_cluster_8` (Distance: 10.079 IQR)
- **Magnitude:** 11.62 | **LOC:** 41 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7879%), State Flux (98.2941%), Safety Score (77.0837%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 7.1)

### 9. `CBL0703v01StatementString.cbl` (COBOL) -> Cumulative Risk: **483.41**
- **Archetype:** `file_cluster_8` (Distance: 10.202 IQR)
- **Magnitude:** 9.42 | **LOC:** 39 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9201%), Tech Debt (99.7879%), Safety Score (91.2761%)
- **Heaviest Functions:** `0000-MAIN` (Impact: 2.9)

### 10. `CBL0506v01CondicionNot.cbl` (COBOL) -> Cumulative Risk: **482.41**
- **Archetype:** `file_cluster_8` (Distance: 10.216 IQR)
- **Magnitude:** 11.16 | **LOC:** 36 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9313%), State Flux (99.2283%), Safety Score (78.5443%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 6.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.561 IQR)
- **Top Global Matches:** file_cluster_8: 10.561, file_cluster_7: 11.248, file_cluster_13: 11.401
- **Magnitude:** 27.58 | **LOC:** 69 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.4207%), Tech Debt (99.992%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 8.3)
  * `200-TWO-DIMENSION` (Impact: 4.1)
  * `300-MOSTRAR` (Impact: 1.2)
  * `100-ONE-DIMENSION` (Impact: 1.1)
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

### `CBL0804v01TableUseIndice.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.012 IQR)
- **Top Global Matches:** file_cluster_8: 10.012, file_cluster_7: 10.738, file_cluster_13: 10.936
- **Magnitude:** 22.14 | **LOC:** 62 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.6945%), Tech Debt (99.9992%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 8.0)
  * `200-TWO-DIMENSION` (Impact: 4.1)
  * `300-MOSTRAR` (Impact: 1.2)
  * `100-ONE-DIMENSION` (Impact: 1.1)
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
- **Magnitude:** 21.96 | **LOC:** 74 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.7315%), Tech Debt (99.9783%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 4.8)
  * `100-ONE-BUSCAR` (Impact: 3.5)
  * `050-SHOW-BEFORE` (Impact: 1.4)
  * `150-SHOW-AFTER` (Impact: 1.3)
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

### `CBL0503v01CondicionSigno.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.92 IQR)
- **Top Global Matches:** file_cluster_8: 10.92, file_cluster_7: 11.574, file_cluster_17: 11.663
- **Magnitude:** 19.88 | **LOC:** 44 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.888%), Tech Debt (99.4824%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 7.3)
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

### `CBL1001v01ManejoCICS.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.741 IQR)
- **Top Global Matches:** file_cluster_8: 8.741, file_cluster_7: 9.619, file_cluster_1: 9.808
- **Magnitude:** 19.82 | **LOC:** 67 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.75%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `0000-PRINCIPAL` (Impact: 4.2)
  * `2000-PROCESO` (Impact: 4.2)
  * `SPECIAL-NAMES` (Impact: 1.8)
    * *Intent:* ****************************************************************** * Author : ALDV * Date : 28 MAY 2...
  * `2200-CONCATENA-DATOS` (Impact: 1.4)
  * `1000-INICIO` (Impact: 1.1)
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

### `CBL0501v01DeclaracioCondicionIF.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.073 IQR)
- **Top Global Matches:** file_cluster_8: 10.073, file_cluster_7: 10.87, file_cluster_17: 10.88
- **Magnitude:** 15.88 | **LOC:** 45 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.0654%), Tech Debt (98.3978%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 12.2)
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

### `CBL0604v01PerformVariying.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.421 IQR)
- **Top Global Matches:** file_cluster_8: 9.421, file_cluster_7: 10.185, file_cluster_1: 10.403
- **Magnitude:** 15.38 | **LOC:** 41 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.257%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 10.7)
  * `0100-CONTADOR` (Impact: 1.2)
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

### `CBL0502v01CondicionRelacion.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.357 IQR)
- **Top Global Matches:** file_cluster_8: 11.357, file_cluster_17: 11.961, file_cluster_7: 12.033
- **Magnitude:** 15.16 | **LOC:** 37 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.7101%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 5.7)
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

### `CBL0806v01TableSearch.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.202 IQR)
- **Top Global Matches:** file_cluster_8: 9.202, file_cluster_7: 10.022, file_cluster_1: 10.226
- **Magnitude:** 12.02 | **LOC:** 60 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.9244%), Tech Debt (99.854%)
**Top Internal Functions/Classes:**
  * `100-ONE-DIMENSION` (Impact: 3.7)
  * `0000-MAIN` (Impact: 2.6)
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

### `CBL0508v01CondicionVerb.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.079 IQR)
- **Top Global Matches:** file_cluster_8: 10.079, file_cluster_7: 10.857, file_cluster_17: 10.919
- **Magnitude:** 11.62 | **LOC:** 41 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.1454%), Tech Debt (99.7879%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 7.1)
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

### `CBL0901v02AccesoSecuencialFiles.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.518 IQR)
- **Top Global Matches:** file_cluster_8: 6.518, file_cluster_7: 7.707, file_cluster_1: 7.881
- **Magnitude:** 11.34 | **LOC:** 90 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.6065%), Tech Debt (99.8783%)
**Top Internal Functions/Classes:**
  * `SPECIAL-NAMES` (Impact: 3.7)
    * *Intent:* ****************************************************************** * Project : Evaluation COBOL PC *...
  * `0000-MAIN` (Impact: 3.1)
  * `1000-INICIO` (Impact: 1.2)
  * `4000-FINAL` (Impact: 1.2)
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

### `CBL0506v01CondicionNot.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.216 IQR)
- **Top Global Matches:** file_cluster_8: 10.216, file_cluster_7: 10.981, file_cluster_17: 11.007
- **Magnitude:** 11.16 | **LOC:** 36 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.2563%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 6.7)
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
- **Magnitude:** 11.1 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.8688%), Tech Debt (99.9842%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 5.5)
  * `CONTADOR` (Impact: 1.2)
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
- **Magnitude:** 11.1 | **LOC:** 34 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.8688%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 5.5)
  * `0100-CONTADOR` (Impact: 1.2)
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

### `CBL0207v01DivideVerb.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.148 IQR)
- **Top Global Matches:** file_cluster_8: 9.148, file_cluster_7: 9.989, file_cluster_1: 10.17
- **Magnitude:** 10.8 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.5427%), Tech Debt (88.0797%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 2.8)
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

### `CBL0601v01InOutLineLoop.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.078 IQR)
- **Top Global Matches:** file_cluster_8: 9.078, file_cluster_7: 9.98, file_cluster_17: 10.137
- **Magnitude:** 10.78 | **LOC:** 52 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.9998%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `A-PARA` (Impact: 3.2)
  * `MAIN-PROCEDURE` (Impact: 1.4)
    * *Intent:* ****************************************************************** * Author : * Date : 06/12/2018 * ...
  * `B-PARA` (Impact: 1.2)
  * `E-PARA` (Impact: 1.2)
  * `C-PARA` (Impact: 1.1)
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

### `CBL0902v01AccesoAleatorio.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.685 IQR)
- **Top Global Matches:** file_cluster_8: 6.685, file_cluster_7: 7.842, file_cluster_1: 8.019
- **Magnitude:** 10.48 | **LOC:** 79 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0278%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `SPECIAL-NAMES` (Impact: 3.2)
    * *Intent:* ****************************************************************** * Project : Evaluation COBOL PC *...
  * `0000-MAIN` (Impact: 3.1)
  * `1000-INICIO` (Impact: 1.1)
  * `4000-FINAL` (Impact: 1.1)
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

### `CBL0206v01MultiplyVerb.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.358 IQR)
- **Top Global Matches:** file_cluster_8: 9.358, file_cluster_7: 10.175, file_cluster_1: 10.358
- **Magnitude:** 10.38 | **LOC:** 55 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.8791%), Tech Debt (93.1734%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 2.5)
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

### `CBL0903v01AccesoDinamico.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.166 IQR)
- **Top Global Matches:** file_cluster_8: 6.166, file_cluster_7: 7.452, file_cluster_1: 7.594
- **Magnitude:** 9.84 | **LOC:** 80 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.4523%), Tech Debt (99.9498%)
**Top Internal Functions/Classes:**
  * `SPECIAL-NAMES` (Impact: 3.4)
    * *Intent:* ****************************************************************** * Project : Evaluation COBOL PC *...
  * `0000-MAIN` (Impact: 3.1)
  * `4000-FINAL` (Impact: 1.2)
  * `1000-INICIO` (Impact: 1.1)
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
- **Magnitude:** 9.56 | **LOC:** 42 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4468%), Tech Debt (99.6072%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 3.0)
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
- **Magnitude:** 9.42 | **LOC:** 39 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.2562%), Tech Debt (99.7879%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 2.9)
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

### `CBL0203v01MoveVerb.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.293 IQR)
- **Top Global Matches:** file_cluster_8: 9.293, file_cluster_7: 10.127, file_cluster_1: 10.32
- **Magnitude:** 8.7 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.7856%), Tech Debt (98.0708%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0605v01GotoStatement.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.431 IQR)
- **Top Global Matches:** file_cluster_8: 8.431, file_cluster_7: 9.33, file_cluster_1: 9.517
- **Magnitude:** 8.54 | **LOC:** 43 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.7388%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `B-PARA` (Impact: 2.1)
  * `0000-MAIN` (Impact: 1.4)
  * `D-PARA` (Impact: 1.2)
  * `0100-CONTADOR` (Impact: 1.2)
  * `C-PARA` (Impact: 1.1)
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

### `CBL0803v01TableUseSubIndice.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.011 IQR)
- **Top Global Matches:** file_cluster_8: 9.011, file_cluster_7: 9.883, file_cluster_1: 10.067
- **Magnitude:** 8.5 | **LOC:** 58 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.4165%), Tech Debt (95.7912%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 26`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`, `orphaned_logic: 1`
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
- **Magnitude:** 8.36 | **LOC:** 40 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.3403%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 3.9)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `CBL0401v01ClausuleCopy.cbl` (COBOL) | Magnitude: 6.7 | Delta: **0.437 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 16, debug_prints: 10, state_mutation: 4
- `CBL0502v01CondicionRelacion.cbl` (COBOL) | Magnitude: 15.16 | Delta: **0.604 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, state_mutation: 9, debug_prints: 5
- `CBL0503v01CondicionSigno.cbl` (COBOL) | Magnitude: 19.88 | Delta: **0.654 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 15, state_mutation: 12, debug_prints: 9
- `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL) | Magnitude: 27.58 | Delta: **0.687 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 19, debug_prints: 13, branch: 12
- `CBL0603v01PerformTimes.cbl` (COBOL) | Magnitude: 11.1 | Delta: **0.723 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, branch: 4, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `CBL0304v01ClausuleComp.cbl` (COBOL) | Magnitude: 7.06 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 19, debug_prints: 13, state_mutation: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `QG4CX001.cpy` -> **Severity: 1298.192** (Blast Radius: 35.68 * Doc Risk: 36.3843%)
- `CBL0201v01VerbosBasicos.cbl` -> **Severity: 1176.66** (Blast Radius: 19.286 * Doc Risk: 61.0111%)
- `CBL0104v01ProcedureDivision.cbl` -> **Severity: 1158.803** (Blast Radius: 19.286 * Doc Risk: 60.0852%)
- `CBL0102v01DivisionAmbiente.cbl` -> **Severity: 1103.826** (Blast Radius: 19.286 * Doc Risk: 57.2346%)
- `CBL0801v01TableOneDimention.cbl` -> **Severity: 1070.462** (Blast Radius: 19.286 * Doc Risk: 55.5046%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
