# ARCHITECTURAL_BRIEF: zopeneditor-sample
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/zopeneditor-sample` |
| **Timestamp** | `2026-08-03T19:29:18.792017+00:00` |
| **Scan Duration** | `0.19s` |
| **Git Branch** | `main` |
| **Git Commit** | `41f70551d85233829a90f7891af2b56092b471c3` |
| **Git Remote** | `https://github.com/IBM/zopeneditor-sample.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 21 malicious artifacts.

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
| Total Artifacts | 59 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 22 |
| Total LOC | 2015 |
| Volatility Index | 0.027 |
| % Scanned of codebase = | 62.7% |
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
| JCL | 9 | 721 | 24.3% |
| COBOL | 8 | 655 | 21.6% |
| PLAINTEXT | 7 | 0 | 18.9% |
| SHELL | 4 | 95 | 10.8% |
| YAML | 3 | 131 | 8.1% |
| ASSEMBLY | 2 | 207 | 5.4% |
| MARKDOWN | 2 | 0 | 5.4% |
| JSON | 2 | 206 | 5.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.49`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 24 | 64.9% |
| file_cluster_12 | 3 | 8.1% |
| file_cluster_17 | 1 | 2.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 24.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 22*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.inc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.rexx`: 3x Excluded (Unsupported Extension: '.rexx'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pli`: 2x Excluded (Unsupported Extension: '.pli'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpy`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.asm`: 1x Excluded (Lexical Monotony: High structural repetition detected in 6433 LOC)
- `.cbl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jcl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 27.2 | 8.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 27.3 | 18.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.2 | 0.0 | 0.0 |
| Testing Exposure | 0.3 | 80.0 | 7.7 | 2.3 | 2.3 |
| API Exposure | 0.0 | 2.7 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.1 | 11.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 6.6 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 92.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.6 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 22.7 | 0.0 | 0.0 |
| Documentation Exposure | 8.7 | 100.0 | 54.4 | 48.5 | 44.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 29.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `JCL/RUN.jcl` (Hits: 60)
- `JCL/RUNPSAM1.jcl` (Hits: 51)
- `COBOL/SAM1.cbl` (Hits: 50)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **SAM2PAR5.cpy** (`multiroot/copybooks/trans/SAM2PAR5.cpy`) — 1 inbound connections
2. **ASAM1.asm** (`ASM/ASAM1.asm`) — 0 inbound connections
3. **REGISTRS.asm** (`ASMCOPY/REGISTRS.asm`) — 0 inbound connections
4. **SAM1.cbl** (`COBOL/SAM1.cbl`) — 0 inbound connections
5. **SAM2.cbl** (`COBOL/SAM2.cbl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **RUN.jcl** (`JCL/RUN.jcl`) — 14 outbound dependencies
2. **RUNPSAM1.jcl** (`JCL/RUNPSAM1.jcl`) — 13 outbound dependencies
3. **RUNASAM1.jcl** (`JCL/RUNASAM1.jcl`) — 11 outbound dependencies
4. **ALLOCATE.jcl** (`JCL/ALLOCATE.jcl`) — 7 outbound dependencies
5. **PLIALLOC.jcl** (`JCL/PLIALLOC.jcl`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `100-PROCESS-TRANSACTIONS` (@ `COBOL/SAM1.cbl`) -> Impact: **47.5** | LOC: 31
- `100-VALIDATE-TRAN` (@ `COBOL/SAM2.cbl`) -> Impact: **39.5** | LOC: 31
- `200-PROCESS-TRAN` (@ `COBOL/SAM2.cbl`) -> Impact: **39.0** | LOC: 29
- `200-PROCESS-UPDATE-TRAN` (@ `COBOL/SAM1.cbl`) -> Impact: **35.5** | LOC: 18
- `REPORT-FILE` (@ `COBOL/SAM1.cbl`) -> Impact: **28.4** | LOC: 27
- `710-READ-TRAN-FILE` (@ `COBOL/SAM1.cbl`) -> Impact: **25.0** | LOC: 20
- `210-PROCESS-ADD-TRAN` (@ `COBOL/SAM1.cbl`) -> Impact: **22.9** | LOC: 19
- `CURRENT-SECOND` (@ `COBOL/SAM1.cbl`) -> Impact: **21.2** | LOC: 25
- `730-READ-CUSTOMER-FILE` (@ `COBOL/SAM1.cbl`) -> Impact: **18.8** | LOC: 16
- `000-MAIN` (@ `COBOL/SAM2.cbl`) -> Impact: **18.7** | LOC: 14

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `REPORT-FILE` (@ `COBOL/SAM1.cbl`) -> **O(N^5)**
- `CURRENT-SECOND` (@ `COBOL/SAM1.cbl`) -> **O(N^4)**
- `720-POSITION-CUST-FILE` (@ `COBOL/SAM1.cbl`) -> **O(N^4)**
- `000-MAIN` (@ `COBOL/SAM1.cbl`) -> **O(N^4)**
- `700-OPEN-FILES` (@ `COBOL/SAM1.cbl`) -> **O(N^4)**
  * *Intent:* * * Subroutine SAM2 will apply an update to a customer record
- `200-PROCESS-TRAN` (@ `COBOL/SAM2.cbl`) -> **O(N^4)**
- `100-PROCESS-TRANSACTIONS` (@ `COBOL/SAM1.cbl`) -> **O(N^3)**
- `200-PROCESS-UPDATE-TRAN` (@ `COBOL/SAM1.cbl`) -> **O(N^3)**
- `710-READ-TRAN-FILE` (@ `COBOL/SAM1.cbl`) -> **O(N^3)**
- `210-PROCESS-ADD-TRAN` (@ `COBOL/SAM1.cbl`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `850-REPORT-TRAN-STATS` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **53**
- `100-PROCESS-TRANSACTIONS` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **18**
- `220-PROCESS-DELETE-TRAN` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **16**
- `200-PROCESS-TRAN` (@ `COBOL/SAM2.cbl`) -> DB Complexity: **16**
- `210-PROCESS-ADD-TRAN` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **15**
- `299-REPORT-BAD-TRAN` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **15**
- `710-READ-TRAN-FILE` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **14**
- `730-READ-CUSTOMER-FILE` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **13**
- `790-CLOSE-FILES` (@ `COBOL/SAM1.cbl`) -> DB Complexity: **12**
- `100-VALIDATE-TRAN` (@ `COBOL/SAM2.cbl`) -> DB Complexity: **11**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `COBOL` | 2 | 712.12 | 80.76% | 96.88% |
| `JCL` | 8 | 246.8 | 2.68% | 0.0% |
| `__monolith__` | 5 | 72.66 | 4.47% | 0.0% |
| `zowe` | 4 | 67.5 | 99.25% | 99.96% |
| `JCLPROC` | 1 | 63.47 | 11.14% | 0.0% |
| `ASM` | 1 | 18.74 | 6.17% | 0.0% |
| `ASMCOPY` | 1 | 15.4 | 11.92% | 0.0% |
| `multiroot/sam` | 1 | 15.28 | 5.0% | 0.0% |
| `RESOURCES` | 7 | 7.0 | 0.0% | 0.0% |
| `multiroot/copybooks/trans` | 3 | 1.91 | 19.84% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> **100.0%** Exposure
- `zowe/zowecli-cobol-clean.sh` -> **99.9996%** Exposure
- `zowe/zowecli-cobol-upload-run-simple.sh` -> **99.9978%** Exposure
- `zowe/zowecli-create-profiles.sh` -> **99.8499%** Exposure
- `COBOL/SAM1.cbl` -> **99.7632%** Exposure
### Highest State Flux (Mutation/Volatility)
- `COBOL/SAM1.cbl` -> **100.0%** Exposure
- `COBOL/SAM2.cbl` -> **100.0%** Exposure
- `zowe/zowecli-cobol-clean.sh` -> **100.0%** Exposure
- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> **100.0%** Exposure
- `zowe/zowecli-create-profiles.sh` -> **99.9995%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `COBOL/SAM1.cbl` -> **17** Orphaned Functions | **2** Duplicates
- `COBOL/SAM2.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> **1** Orphaned Functions | **2** Duplicates
- `zowe/zowecli-cobol-clean.sh` -> **1** Orphaned Functions | **0** Duplicates
- `zowe/zowecli-cobol-upload-run-simple.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`COBOL/SAM1.cbl`** -> AI Confidence: **99.29%**
2. **`COBOL/SAM2.cbl`** -> AI Confidence: **99.29%**
3. **`zowe/zowecli-cobol-clean.sh`** -> AI Confidence: **99.29%**
4. **`zowe/zowecli-cobol-upload-run-tutorial.sh`** -> AI Confidence: **99.17%**
5. **`JCL/RUN.jcl`** -> AI Confidence: **99.09%**
6. **`JCL/RUNASAM1.jcl`** -> AI Confidence: **99.09%**
7. **`JCL/RUNPSAM1.jcl`** -> AI Confidence: **99.09%**
8. **`JCL/ALLOCATE.jcl`** -> AI Confidence: **99.08%**
9. **`JCL/PLIALLOC.jcl`** -> AI Confidence: **99.08%**
10. **`COPYBOOK/CUSTCOPY.cpy`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `JCL/ALLOCATE.jcl` -> **100.0%** Exposure
- `JCL/ASMALLOC.jcl` -> **100.0%** Exposure
- `JCL/PLIALLOC.jcl` -> **100.0%** Exposure
- `JCL/REXALLOC.jcl` -> **100.0%** Exposure
- `JCL/RUN.jcl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `JCL/ALLOCATE.jcl` -> **100.0%** Exposure
- `JCL/ASMALLOC.jcl` -> **100.0%** Exposure
- `JCL/PLIALLOC.jcl` -> **100.0%** Exposure
- `JCL/REXALLOC.jcl` -> **100.0%** Exposure
- `JCL/RUN.jcl` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `COBOL/SAM1.cbl` -> **100.0%** Exposure
- `COBOL/SAM2.cbl` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `71` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `COBOL/SAM2.cbl` (COBOL) -> Cumulative Risk: **769.5**
- **Archetype:** `file_cluster_8` (Distance: 14.061 IQR)
- **Magnitude:** 241.18 | **LOC:** 159 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9125%)
- **Heaviest Functions:** `100-VALIDATE-TRAN` (Impact: 39.5), `200-PROCESS-TRAN` (Impact: 39.0), `000-MAIN` (Impact: 18.7)

### 2. `zowe/zowecli-cobol-clean.sh` (SHELL) -> Cumulative Risk: **729.67**
- **Archetype:** `file_cluster_12` (Distance: 20.776 IQR)
- **Magnitude:** 15.3 | **LOC:** 26 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `__global_context__` (Impact: 3.0)

### 3. `zowe/zowecli-cobol-upload-run-simple.sh` (SHELL) -> Cumulative Risk: **725.94**
- **Archetype:** `file_cluster_12` (Distance: 19.078 IQR)
- **Magnitude:** 6.84 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9978%)
- **Heaviest Functions:** `__global_context__` (Impact: 2.5)

### 4. `COBOL/SAM1.cbl` (COBOL) -> Cumulative Risk: **710.07**
- **Archetype:** `file_cluster_8` (Distance: 12.455 IQR)
- **Magnitude:** 470.94 | **LOC:** 505 | **CtrlFlow:** 79.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.7632%)
- **Heaviest Functions:** `100-PROCESS-TRANSACTIONS` (Impact: 47.5), `200-PROCESS-UPDATE-TRAN` (Impact: 35.5), `REPORT-FILE` (Impact: 28.4)

### 5. `zowe/zowecli-cobol-upload-run-tutorial.sh` (SHELL) -> Cumulative Risk: **692.73**
- **Archetype:** `file_cluster_17` (Distance: 16.421 IQR)
- **Magnitude:** 34.36 | **LOC:** 55 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.995%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 5.3), `Anonymous_Block` (Impact: 5.3), `__global_context__` (Impact: 3.0)

### 6. `zowe/zowecli-create-profiles.sh` (SHELL) -> Cumulative Risk: **520.42**
- **Archetype:** `file_cluster_12` (Distance: 10.952 IQR)
- **Magnitude:** 11.0 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9995%), Tech Debt (99.8499%)
- **Heaviest Functions:** `__global_context__` (Impact: 1.5)

### 7. `JCL/ALLOCATE.jcl` (JCL) -> Cumulative Risk: **488.4**
- **Archetype:** `file_cluster_8` (Distance: 6.399 IQR)
- **Magnitude:** 18.78 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)

### 8. `JCL/RUN.jcl` (JCL) -> Cumulative Risk: **481.19**
- **Archetype:** `file_cluster_8` (Distance: 7.059 IQR)
- **Magnitude:** 85.3 | **LOC:** 168 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Churn (63.09%)

### 9. `JCL/REXALLOC.jcl` (JCL) -> Cumulative Risk: **468.22**
- **Archetype:** `file_cluster_8` (Distance: 6.516 IQR)
- **Magnitude:** 18.3 | **LOC:** 66 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Documentation (57.9931%)

### 10. `JCL/RUNASAM1.jcl` (JCL) -> Cumulative Risk: **467.96**
- **Archetype:** `file_cluster_8` (Distance: 8.101 IQR)
- **Magnitude:** 31.64 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), State Flux (75.026%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `COBOL/SAM1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.455 IQR)
- **Top Global Matches:** file_cluster_8: 12.455, file_cluster_13: 12.762, file_cluster_17: 12.883
- **Magnitude:** 470.94 | **LOC:** 505 | **CtrlFlow:** 79.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (73.6213%), Tech Debt (99.7632%)
**Top Internal Functions/Classes:**
  * `100-PROCESS-TRANSACTIONS` (Impact: 47.5 | O(N^3) | DB: 18)
  * `200-PROCESS-UPDATE-TRAN` (Impact: 35.5 | O(N^3) | DB: 6)
  * `REPORT-FILE` (Impact: 28.4 | O(N^5) | DB: 8)
  * `710-READ-TRAN-FILE` (Impact: 25.0 | O(N^3) | DB: 14)
  * `210-PROCESS-ADD-TRAN` (Impact: 22.9 | O(N^3) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 27`, `args: 1`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 193`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `io: 50`, `api: 1`, `import: 4`
* *Defense:* `safety: 22`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TRANREC, CUSTCOPY
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL/SAM2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.061 IQR)
- **Top Global Matches:** file_cluster_8: 14.061, file_cluster_13: 14.176, file_cluster_17: 14.321
- **Magnitude:** 241.18 | **LOC:** 159 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (87.9021%), Tech Debt (94.0032%)
**Top Internal Functions/Classes:**
  * `100-VALIDATE-TRAN` (Impact: 39.5 | O(N^3) | DB: 11)
  * `200-PROCESS-TRAN` (Impact: 39.0 | O(N^4) | DB: 16)
  * `000-MAIN` (Impact: 18.7 | O(N^3) | DB: 2)
  * `310-CRUNCH-LOOP` (Impact: 14.4 | O(N^3) | DB: 4)
  * `300-PROCESS-CPU-CRUNCH` (Impact: 6.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 10`, `args: 1`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 120`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TRANREC, CUSTCOPY
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/RUN.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.059 IQR)
- **Top Global Matches:** file_cluster_8: 7.059, file_cluster_7: 8.179, file_cluster_1: 8.374
- **Magnitude:** 85.3 | **LOC:** 168 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.3135%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 74`, `args: 2`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 5`
* *Architecture:* `io: 60`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.OBJ, &HLQ..SAMPLE.LOAD, &HLQ..SAMPLE.COPY, &HLQ..SAMPLE.OBJ(SAM2), &HLQ..SAMPLE.COBOL(SAM1), &HLQ..SAMPLE.CUSTOUT, &CMPLLIB, &HLQ..SAMPLE.OBJ(SAM1)...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCLPROC/COMPROC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.621 IQR)
- **Top Global Matches:** file_cluster_8: 5.621, file_cluster_7: 7.068, file_cluster_1: 7.218
- **Magnitude:** 63.47 | **LOC:** 52 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.136%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 23`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.COPY, &CMPLLIB, &HLQ..SAMPLE.OBJ(SAM2), &HLQ..SAMPLE.COBOL(SAM2)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/RUNPSAM1.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.651 IQR)
- **Top Global Matches:** file_cluster_8: 7.651, file_cluster_7: 8.667, file_cluster_1: 8.867
- **Magnitude:** 38.02 | **LOC:** 86 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 36`, `args: 2`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 4`
* *Architecture:* `io: 51`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.PLIOBJ(PSAM1), &HLQ..SAMPLE.PLIOBJ(PSAM2), &HLQ..SAMPLE.PLILOAD, &HLQ..SAMPLE.PLIOBJ, &HLQ..SAMPLE.PLI(PSAM2), &HLQ..SAMPLE.PLI.CUSTRPT, &HLQ..SAMPLE.PLI.CUSTFILE, &HLQ..SAMPLE.PLI.TRANFILE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-cobol-upload-run-tutorial.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.421 IQR)
- **Top Global Matches:** file_cluster_17: 16.421, file_cluster_9: 16.468, file_cluster_0: 16.475
- **Magnitude:** 34.36 | **LOC:** 55 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (96.993%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 5.3 | O(N^1) | DB: 1)
  * `Anonymous_Block` (Impact: 5.3 | O(N^1) | DB: 1)
  * `__global_context__` (Impact: 3.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 20`, `dead_code: 2`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/RUNASAM1.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.101 IQR)
- **Top Global Matches:** file_cluster_8: 8.101, file_cluster_7: 9.053, file_cluster_1: 9.257
- **Magnitude:** 31.64 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 33`, `args: 1`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 6`
* *Architecture:* `io: 38`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.ASM(ASAM1), &HLQ..SAMPLE.ASMOBJ, &HLQ..SAMPLE.ASMLOAD, &MACLIB, &HLQ..SAMPLE.ASM.FILEIN, &SCEEMAC, &MODGEN, &HLQ..SAMPLE.ASMOBJ(ASAM1)...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/PLIALLOC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.301 IQR)
- **Top Global Matches:** file_cluster_8: 6.301, file_cluster_7: 7.55, file_cluster_1: 7.731
- **Magnitude:** 18.8 | **LOC:** 91 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`
* *Architecture:* `io: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.PLILOAD, &HLQ..SAMPLE.PLI, &HLQ..SAMPLE.PLIOBJ, &HLQ..SAMPLE.PLI.TRANFILE, &HLQ..SAMPLE.PLI.CUSTFILE, &HLQ..SAMPLE.PLI.INCLLIB, &HLQ..SAMPLE.PLINC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/ALLOCATE.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.399 IQR)
- **Top Global Matches:** file_cluster_8: 6.399, file_cluster_7: 7.631, file_cluster_1: 7.809
- **Magnitude:** 18.78 | **LOC:** 90 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`
* *Architecture:* `io: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.OBJ, &HLQ..SAMPLE.LOAD, &HLQ..SAMPLE.COPY, &HLQ..SAMPLE.TRANFILE, &HLQ..SAMPLE.COPYLIB, &HLQ..SAMPLE.COBOL, &HLQ..SAMPLE.CUSTFILE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ASM/ASAM1.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.841 IQR)
- **Top Global Matches:** file_cluster_8: 6.841, file_cluster_7: 8.025, file_cluster_1: 8.216
- **Magnitude:** 18.74 | **LOC:** 188 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1692%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`
* *Risk/State:* None
* *Architecture:* `io: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zapp-example.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.5 IQR)
- **Top Global Matches:** file_cluster_8: 4.5, file_cluster_7: 6.287, file_cluster_1: 6.35
- **Magnitude:** 18.74 | **LOC:** 187 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/ASMALLOC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.43 IQR)
- **Top Global Matches:** file_cluster_8: 6.43, file_cluster_7: 7.651, file_cluster_1: 7.836
- **Magnitude:** 18.46 | **LOC:** 74 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`
* *Architecture:* `io: 20`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.ASM, &HLQ..SAMPLE.ASM.FILEIN, &HLQ..SAMPLE.ASMLOAD, &HLQ..SAMPLE.ASMOBJ, &HLQ..SAMPLE.ASMCOPY
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/REXALLOC.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.516 IQR)
- **Top Global Matches:** file_cluster_8: 6.516, file_cluster_7: 7.719, file_cluster_1: 7.906
- **Magnitude:** 18.3 | **LOC:** 66 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`
* *Architecture:* `io: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &HLQ..SAMPLE.REXX, &HLQ..SAMPLE.REXX.FILEIN1, &HLQ..SAMPLE.REXX.FILEOUT, &HLQ..SAMPLE.REXX.FILEIN2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `JCL/INCLUDE.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.407 IQR)
- **Top Global Matches:** file_cluster_8: 7.407, file_cluster_13: 8.342, file_cluster_7: 8.5
- **Magnitude:** 17.5 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.1553%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` COMPSET
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zapp.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.737 IQR)
- **Top Global Matches:** file_cluster_8: 6.737, file_cluster_7: 7.67, file_cluster_1: 7.875
- **Magnitude:** 17.12 | **LOC:** 123 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.8789%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ASMCOPY/REGISTRS.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.992 IQR)
- **Top Global Matches:** file_cluster_8: 5.992, file_cluster_7: 7.401, file_cluster_1: 7.478
- **Magnitude:** 15.4 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.9203%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 10`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zcodeformat-example.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.38 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.4841%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-cobol-clean.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_12` (Drift: 20.776 IQR)
- **Top Global Matches:** file_cluster_12: 20.776, file_cluster_11: 20.939, file_cluster_9: 20.99
- **Magnitude:** 15.3 | **LOC:** 26 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 3.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 12`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `multiroot/sam/zapp.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.871 IQR)
- **Top Global Matches:** file_cluster_8: 6.871, file_cluster_7: 7.49, file_cluster_1: 7.687
- **Magnitude:** 15.28 | **LOC:** 25 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zcodeformat.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.22 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-create-profiles.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_12` (Drift: 10.952 IQR)
- **Top Global Matches:** file_cluster_12: 10.952, file_cluster_8: 11.017, file_cluster_7: 11.746
- **Magnitude:** 11.0 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.8499%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe/zowecli-cobol-upload-run-simple.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_12` (Drift: 19.078 IQR)
- **Top Global Matches:** file_cluster_12: 19.078, file_cluster_9: 19.211, file_cluster_17: 19.281
- **Magnitude:** 6.84 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9978%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 2.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 4`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 6.2 | **LOC:** 310 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `multiroot/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `RESOURCES/SAMPLE.ASM.FILEIN.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `zowe/zowecli-create-profiles.sh` (SHELL) | Magnitude: 11.0 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 18, state_mutation: 9, io: 3, debug_prints: 3
- `zowe/zowecli-cobol-upload-run-simple.sh` (SHELL) | Magnitude: 6.84 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: reflection_metaprogramming: 14, safety_bypasses: 8, state_mutation: 4, debug_prints: 3
- `zowe/zowecli-cobol-clean.sh` (SHELL) | Magnitude: 15.3 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: reflection_metaprogramming: 18, state_mutation: 12, safety_bypasses: 9, dead_code: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `zowe/zowecli-cobol-upload-run-tutorial.sh` (SHELL) | Magnitude: 34.36 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: safety_bypasses: 32, state_mutation: 20, debug_prints: 12, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `COBOL/SAM2.cbl` (COBOL) | Magnitude: 241.18 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 120, indent_spaces: 119, branch: 54, safety: 17
- `COBOL/SAM1.cbl` (COBOL) | Magnitude: 470.94 | Delta: **0.307 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 417, state_mutation: 193, branch: 102, io: 50
- `multiroot/sam/zapp.yaml` (YAML) | Magnitude: 15.28 | Delta: **0.619 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 9, doc: 3, branch: 1
- `multiroot/copybooks/trans/SAM2PARM.cpy` (COBOL) | Magnitude: 0.58 | Delta: **0.743 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 3, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `zowe/zowecli-cobol-clean.sh` -> Churn: **63.09%** | Cog Load: 100.0% | Debt: 99.9996%
- `zowe/zowecli-cobol-upload-run-simple.sh` -> Churn: **63.09%** | Cog Load: 100.0% | Debt: 99.9978%
- `zowe/zowecli-cobol-upload-run-tutorial.sh` -> Churn: **63.09%** | Cog Load: 96.993% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `JCL/RUN.jcl` -> **Peter Haumer** (100.0% isolated ownership) | Magnitude: 85.3
- `JCLPROC/COMPROC.jcl` -> **Peter Haumer** (100.0% isolated ownership) | Magnitude: 63.47

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `zowe/zowecli-cobol-clean.sh` -> **Severity: 2509.4** (Blast Radius: 25.094 * Doc Risk: 100.0%)
- `zowe/zowecli-cobol-upload-run-simple.sh` -> **Severity: 2509.4** (Blast Radius: 25.094 * Doc Risk: 100.0%)
- `COBOL/SAM2.cbl` -> **Severity: 2507.204** (Blast Radius: 25.094 * Doc Risk: 99.9125%)
- `COBOL/SAM1.cbl` -> **Severity: 2470.567** (Blast Radius: 25.094 * Doc Risk: 98.4525%)
- `ASMCOPY/REGISTRS.asm` -> **Severity: 2390.389** (Blast Radius: 25.094 * Doc Risk: 95.2574%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
