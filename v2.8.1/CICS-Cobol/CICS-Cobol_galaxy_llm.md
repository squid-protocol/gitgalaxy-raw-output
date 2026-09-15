# ARCHITECTURAL_BRIEF: CICS-Cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mainframe-projects/CICS-Cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 52 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 1543 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.3% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 52 | 1543 | 100.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z +2.11; from the repo's file-archetype mix)
> **File Composition:** I/O & Config Routines Files 62%, Interface Declarations Files 35%, Data / Markup / Trivial 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 52 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 41.1 | 5.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.7 | 77.1 | 78.3 | 78.3 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 65.0 | 62.2 | 62.2 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.5 | 2.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 99.9 | 47.8 | 50.0 | 50.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 86.1 | 1.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 98.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 96.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6 | 3 | 0 | `CBL0301v01DataLayoutRedefine.cbl` |
| cleanup | 0 | 0 | 0 | - |
| guards | 0 | 0 | 0 | - |
| danger | 104 | 51 | 2 | `CBL0605v01GotoStatement.cbl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 0 | 0 | 0 | - |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `CBL0201v01VerbosBasicos.cbl` |
| serialization | 7 | 3 | 0 | `CBL0703v01StatementString.cbl` |
| regex | 10 | 4 | 0 | `CBL0701v01StatementInspect.cbl` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 429 | 51 | 16 | `CBL0301v01DataLayoutRedefine.cbl` |
| mutation | 128 | 46 | 4 | `CBL0206v01MultiplyVerb.cbl` |
| dead_code | 66 | 50 | 2 | `CBL0304v01ClausuleComp.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 10 | 5 | 0 | `CBL0301v01DataLayoutRedefine.cbl` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

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

- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0501v01DeclaracioCondicionIF.cbl`) -> Impact: **9.3** | LOC: 27
- `0000-MAIN` **(I/O & Config Routines)** (@ `CBL0604v01PerformVariying.cbl`) -> Impact: **8.0** | LOC: 19
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0503v01CondicionSigno.cbl`) -> Impact: **7.3** | LOC: 27
- `0000-MAIN` **(I/O & Config Routines)** (@ `CBL0805v01TableUseIndiceWithSet.cbl`) -> Impact: **6.3** | LOC: 27
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0508v01CondicionVerb.cbl`) -> Impact: **6.1** | LOC: 22
- `0000-MAIN` **(I/O & Config Routines)** (@ `CBL0804v01TableUseIndice.cbl`) -> Impact: **6.0** | LOC: 20
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0506v01CondicionNot.cbl`) -> Impact: **5.8** | LOC: 17
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0504v01CondicionClass.cbl`) -> Impact: **5.0** | LOC: 20
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0502v01CondicionRelacion.cbl`) -> Impact: **4.8** | LOC: 16
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0505v01CondicionName.cbl`) -> Impact: **3.9** | LOC: 17

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 52 | 428.7 | 5.78% | 64.98% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `CBL0601v01InOutLineLoop.cbl` -> **99.8499%** Exposure
- `CBL0902v01AccesoAleatorio.cbl` -> **98.9013%** Exposure
- `CBL0903v01AccesoDinamico.cbl` -> **98.5667%** Exposure
- `CBL0901v02AccesoSecuencialFiles.cbl` -> **97.4428%** Exposure
- `CBL0102v01DivisionAmbiente.cbl` -> **92.4142%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `CBL0503v01CondicionSigno.cbl` -> **99.9254%** Exposure
- `CBL0805v01TableUseIndiceWithSet.cbl` -> **99.9254%** Exposure
- `CBL0502v01CondicionRelacion.cbl` -> **99.1837%** Exposure
- `CBL0807v01TableSearchAll.cbl` -> **98.2014%** Exposure
- `CBL0206v01MultiplyVerb.cbl` -> **96.0834%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `CBL0601v01InOutLineLoop.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `CBL0901v02AccesoSecuencialFiles.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `CBL0902v01AccesoAleatorio.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `CBL0903v01AccesoDinamico.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `CBL0102v01DivisionAmbiente.cbl` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

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

### 1. `CBL0304v01ClausuleComp.cbl` (COBOL) -> Cumulative Risk: **499.42**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z -0.00)
- **Magnitude:** 7.06 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Dead Code (86.0737%), Safety Score (79.7611%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (I/O & Config Routines, Impact: 2.4)

### 2. `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL) -> Cumulative Risk: **494.41**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.38)
- **Magnitude:** 24.58 | **LOC:** 69 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9254%), Safety Score (88.6667%)
- **Heaviest Functions:** `0000-MAIN` (I/O & Config Routines, Impact: 6.3), `200-TWO-DIMENSION` (Compute Cores, Impact: 3.1), `300-MOSTRAR` (Interface Declarations, Impact: 1.2)

### 3. `CBL0503v01CondicionSigno.cbl` (COBOL) -> Cumulative Risk: **486.88**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.10)
- **Magnitude:** 19.88 | **LOC:** 44 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9254%), Safety Score (88.6667%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (I/O & Config Routines, Impact: 7.3)

### 4. `CBL0807v01TableSearchAll.cbl` (COBOL) -> Cumulative Risk: **476.31**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.97)
- **Magnitude:** 16.96 | **LOC:** 74 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.2014%), Safety Score (84.7391%)
- **Heaviest Functions:** `100-ONE-BUSCAR` (I/O & Config Routines, Impact: 3.5), `0000-MAIN` (I/O & Config Routines, Impact: 1.8), `050-SHOW-BEFORE` (Interface Declarations, Impact: 1.4)

### 5. `CBL0502v01CondicionRelacion.cbl` (COBOL) -> Cumulative Risk: **470.7**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.13)
- **Magnitude:** 14.26 | **LOC:** 37 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.1837%), Safety Score (85.8149%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (I/O & Config Routines, Impact: 4.8)

### 6. `CBL0804v01TableUseIndice.cbl` (COBOL) -> Cumulative Risk: **468.26**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.44)
- **Magnitude:** 19.14 | **LOC:** 62 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.0834%), Safety Score (83.5974%)
- **Heaviest Functions:** `0000-MAIN` (I/O & Config Routines, Impact: 6.0), `200-TWO-DIMENSION` (Compute Cores, Impact: 3.1), `300-MOSTRAR` (Interface Declarations, Impact: 1.2)

### 7. `CBL0207v01DivideVerb.cbl` (COBOL) -> Cumulative Risk: **444.28**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z -0.05)
- **Magnitude:** 10.8 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.0834%), Safety Score (83.5974%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (I/O & Config Routines, Impact: 2.8)

### 8. `CBL0206v01MultiplyVerb.cbl` (COBOL) -> Cumulative Risk: **444.27**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z -0.06)
- **Magnitude:** 10.38 | **LOC:** 55 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.0834%), Safety Score (83.5974%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (I/O & Config Routines, Impact: 2.5)

### 9. `CBL0803v01TableUseSubIndice.cbl` (COBOL) -> Cumulative Risk: **440.41**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z -0.12)
- **Magnitude:** 8.6 | **LOC:** 58 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (83.2018%), Safety Score (81.1095%)
- **Heaviest Functions:** `0000-MAIN` (I/O & Config Routines, Impact: 2.8)

### 10. `CBL0203v01MoveVerb.cbl` (COBOL) -> Cumulative Risk: **438.66**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z -0.06)
- **Magnitude:** 8.7 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (91.6827%), Safety Score (82.388%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (I/O & Config Routines, Impact: 2.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 24.58 | **LOC:** 69 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.096%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 6.3)
  * `200-TWO-DIMENSION` **(Compute Cores)** (Impact: 3.1)
  * `300-MOSTRAR` **(Interface Declarations)** (Impact: 1.2)
  * `100-ONE-DIMENSION` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 22`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0503v01CondicionSigno.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 19.88 | **LOC:** 44 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.6261%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0804v01TableUseIndice.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 19.14 | **LOC:** 62 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.8667%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 6.0)
  * `200-TWO-DIMENSION` **(Compute Cores)** (Impact: 3.1)
  * `300-MOSTRAR` **(Interface Declarations)** (Impact: 1.2)
  * `100-ONE-DIMENSION` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 17`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0807v01TableSearchAll.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.96 | **LOC:** 74 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.7%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `100-ONE-BUSCAR` **(I/O & Config Routines)** (Impact: 3.5)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 1.8)
  * `050-SHOW-BEFORE` **(Interface Declarations)** (Impact: 1.4)
  * `150-SHOW-AFTER` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 23`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL1001v01ManejoCICS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.12 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `SPECIAL-NAMES` **(I/O & Config Routines)** (Impact: 2.0)
  * `2200-CONCATENA-DATOS` **(I/O & Config Routines)** (Impact: 1.4)
  * `0000-PRINCIPAL` **(Interface Declarations)** (Impact: 1.2)
  * `2000-PROCESO` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* *
  * `1000-INICIO` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0502v01CondicionRelacion.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 14.26 | **LOC:** 37 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.0818%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0101v01EstructuraInicial.COB` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 13.64 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0501v01DeclaracioCondicionIF.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 12.98 | **LOC:** 45 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.3467%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 17`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0604v01PerformVariying.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 12.68 | **LOC:** 41 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.5067%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 8.0)
  * `0100-CONTADOR` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 15`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0207v01DivideVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.8 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0508v01CondicionVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.62 | **LOC:** 41 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2465%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0206v01MultiplyVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.38 | **LOC:** 55 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0901v02AccesoSecuencialFiles.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.34 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (97.4428%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 3.5)
  * `SPECIAL-NAMES` **(Interface Declarations)** (Impact: 1.2)
  * `1000-INICIO` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* *
  * `4000-FINAL` **(Interface Declarations)** (Impact: 1.2)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *************************
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0506v01CondicionNot.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.26 | **LOC:** 36 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.5067%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0902v01AccesoAleatorio.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9.58 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (98.9013%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 3.1)
  * `SPECIAL-NAMES` **(Interface Declarations)** (Impact: 1.2)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *************************
  * `1000-INICIO` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
  * `4000-FINAL` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0602v01PerformUntil.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9.1 | **LOC:** 34 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.975%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 3.5)
  * `CONTADOR` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0603v01PerformTimes.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9.1 | **LOC:** 34 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.975%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 3.5)
  * `0100-CONTADOR` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0806v01TableSearch.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9.02 | **LOC:** 60 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.7168%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `100-ONE-DIMENSION` **(I/O & Config Routines)** (Impact: 3.7)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0601v01InOutLineLoop.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8.88 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.8499%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 1.4)
  * `A-PARA` **(Interface Declarations)** (Impact: 1.3)
    * *Intent:* * in line
  * `B-PARA` **(Interface Declarations)** (Impact: 1.2)
  * `E-PARA` **(I/O & Config Routines)** (Impact: 1.2)
  * `C-PARA` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0903v01AccesoDinamico.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8.84 | **LOC:** 80 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (98.5667%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 3.2)
  * `SPECIAL-NAMES` **(Interface Declarations)** (Impact: 1.2)
  * `4000-FINAL` **(Interface Declarations)** (Impact: 1.2)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *************************
  * `1000-INICIO` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0203v01MoveVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8.7 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0803v01TableUseSubIndice.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8.6 | **LOC:** 58 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.5067%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 26`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0605v01GotoStatement.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 8.54 | **LOC:** 43 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.5131%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `B-PARA` **(I/O & Config Routines)** (Impact: 2.1)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 1.4)
  * `D-PARA` **(Interface Declarations)** (Impact: 1.2)
  * `0100-CONTADOR` **(Interface Declarations)** (Impact: 1.2)
  * `C-PARA` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 14`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0505v01CondicionName.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8.36 | **LOC:** 40 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.975%), Tech Debt (62.2459%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0901v01AccesoSecuencial.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7.52 | **LOC:** 63 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 2.5)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *************************
  * `1000-INICIO` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
  * `4000-FINAL` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
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

- `CBL0102v01DivisionAmbiente.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0103v01DivisionData.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0104v01ProcedureDivision.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0105v01DeclararElementoGrupo.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0106v01ClausulaImagen.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
