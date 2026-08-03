# ARCHITECTURAL_BRIEF: cics-genapp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/cics-genapp` |
| **Timestamp** | `2026-08-03T19:25:30.250694+00:00` |
| **Scan Duration** | `0.45s` |
| **Git Branch** | `main` |
| **Git Commit** | `63eca1b670d9199637bdc2ca7df6e4189a58c892` |
| **Git Remote** | `https://github.com/cicsdev/cics-genapp.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 75 malicious artifacts.

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
| Total Artifacts | 139 |
| Analyzed Artifacts (Scanned) | 129 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 10865 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.8% |
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
| COBOL | 44 | 6794 | 34.1% |
| PLAINTEXT | 41 | 0 | 31.8% |
| JCL | 30 | 4054 | 23.3% |
| MARKDOWN | 13 | 0 | 10.1% |
| SHELL | 1 | 17 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.978`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 61 | 47.3% |
| file_cluster_11 | 8 | 6.2% |
| file_cluster_13 | 3 | 2.3% |
| file_cluster_12 | 1 | 0.8% |
| file_cluster_4 | 1 | 0.8% |
| file_cluster_0 | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 54 | 41.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 124 LOC), 1x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.rexx`: 2x Excluded (Unsupported Extension: '.rexx')
- `.evbind`: 1x Excluded (Unsupported Extension: '.evbind')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 24204 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 41.8 | 11.8 | 0.0 |
| Error & Exception Exposure | 0.0 | 87.2 | 26.2 | 23.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.6 | 2.3 | 2.3 |
| API Exposure | 0.0 | 2.9 | 0.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 28.3 | 3.8 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 94.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 82.5 | 22.7 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 41.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 24.9 | 20.0 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.0 | 1.3 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `base/src/lgsetup.cbl` (Hits: 55)
- `base/cntl/db2cre.jcl` (Hits: 54)
- `base/cntl/sampwui.jcl` (Hits: 51)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Changes.md** (`Changes.md`) — 0 inbound connections
2. **MAINTAINERS.md** (`MAINTAINERS.md`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **Building.md** (`base/Building.md`) — 0 inbound connections
5. **Installation.md** (`base/Installation.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lgacdb01.cbl** (`base/src/lgacdb01.cbl`) — 3 outbound dependencies
2. **lgapdb01.cbl** (`base/src/lgapdb01.cbl`) — 3 outbound dependencies
3. **lgicdb01.cbl** (`base/src/lgicdb01.cbl`) — 3 outbound dependencies
4. **lgipdb01.cbl** (`base/src/lgipdb01.cbl`) — 3 outbound dependencies
5. **lgucdb01.cbl** (`base/src/lgucdb01.cbl`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `UPDATE-POLICY-DB2-INFO` (@ `base/src/lgupdb01.cbl`) -> Impact: **125.1** | LOC: 102
  * *Intent:* ******************************************************************
- `MAINLINE` (@ `base/src/lgwebst5.cbl`) -> Impact: **100.5** | LOC: 448
- `A-GAIN` (@ `base/src/lgtestp4.cbl`) -> Impact: **93.8** | LOC: 197
- `MAINLINE` (@ `base/src/lgicvs01.cbl`) -> Impact: **90.2** | LOC: 124
- `A-GAIN` (@ `base/src/lgtestp1.cbl`) -> Impact: **72.0** | LOC: 201
- `A-GAIN` (@ `base/src/lgtestp2.cbl`) -> Impact: **72.0** | LOC: 189
- `A-GAIN` (@ `base/src/lgtestp3.cbl`) -> Impact: **72.0** | LOC: 185
- `GET-ENDOW-DB2-INFO` (@ `base/src/lgipdb01.cbl`) -> Impact: **70.8** | LOC: 87
- `GET-Commercial-DB2-INFO-3` (@ `base/src/lgipdb01.cbl`) -> Impact: **67.3** | LOC: 27
- `GET-Commercial-DB2-INFO-5` (@ `base/src/lgipdb01.cbl`) -> Impact: **67.3** | LOC: 26

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `GET-Commercial-DB2-INFO-3` (@ `base/src/lgipdb01.cbl`) -> **O(2^N) [Recursive]**
- `GET-Commercial-DB2-INFO-5` (@ `base/src/lgipdb01.cbl`) -> **O(2^N) [Recursive]**
- `INSERT-CUSTOMER` (@ `base/src/lgacdb01.cbl`) -> **O(N^6)**
  * *Intent:* *----------------------------------------------------------------* * Process incoming commarea * *----------------------------------------------------...
- `MAINLINE` (@ `base/src/lgacdb01.cbl`) -> **O(N^6)**
  * *Intent:* *----------------------------------------------------------------* * Definitions required for data manipulation * *-----------------------------------...
- `Obtain-CUSTOMER-Number` (@ `base/src/lgacdb01.cbl`) -> **O(N^6)**
  * *Intent:* *----------------------------------------------------------------* * Common code * *----------------------------------------------------------------* ...
- `INSERT-CUSTOMER-PASSWORD` (@ `base/src/lgacdb02.cbl`) -> **O(N^6)**
- `INSERT-CUSTOMER` (@ `base/src/lgacus01.cbl`) -> **O(N^6)**
- `A-EXIT` (@ `base/src/lgacvs01.cbl`) -> **O(N^6)**
  * *Intent:* *----------------------------------------------------------------* *****************************************************************
- `INSERT-COMMERCIAL` (@ `base/src/lgapdb01.cbl`) -> **O(N^6)**
- `INSERT-POLICY` (@ `base/src/lgapdb01.cbl`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `MAINLINE` (@ `base/src/lgwebst5.cbl`) -> DB Complexity: **226**
- `MAINLINE` (@ `base/src/lgsetup.cbl`) -> DB Complexity: **133**
- `A-GAIN` (@ `base/src/lgtestp1.cbl`) -> DB Complexity: **87**
- `A-GAIN` (@ `base/src/lgtestp4.cbl`) -> DB Complexity: **81**
- `A-GAIN` (@ `base/src/lgtestp2.cbl`) -> DB Complexity: **80**
- `MAINLINE` (@ `base/src/lgicvs01.cbl`) -> DB Complexity: **79**
- `A-GAIN` (@ `base/src/lgtestp3.cbl`) -> DB Complexity: **75**
- `UPDATE-POLICY-DB2-INFO` (@ `base/src/lgupdb01.cbl`) -> DB Complexity: **65**
  * *Intent:* ******************************************************************
- `A-GAIN` (@ `base/src/lgtestc1.cbl`) -> DB Complexity: **58**
- `ERROR-OUT` (@ `base/src/lgtestc1.cbl`) -> DB Complexity: **47**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `base/src` | 47 | 5582.44 | 61.04% | 35.54% |
| `base/cntl` | 30 | 581.22 | 5.42% | 0.0% |
| `base/wsim` | 39 | 79.64 | 0.0% | 0.0% |
| `base` | 5 | 9.46 | 0.0% | 0.0% |
| `base/bin` | 1 | 6.24 | 100.0% | 100.0% |
| `__monolith__` | 3 | 3.78 | 0.0% | 0.0% |
| `base/data` | 2 | 2.0 | 0.0% | 0.0% |
| `base/exec` | 1 | 1.58 | 0.0% | 0.0% |
| `base/event-bindings` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `base/bin/install.sh` -> **99.9978%** Exposure
- `base/src/lgicus01.cbl` -> **87.2926%** Exposure
- `base/src/lgtestp3.cbl` -> **79.219%** Exposure
- `base/src/lgstsq.cbl` -> **78.9768%** Exposure
- `base/src/lgtestp2.cbl` -> **78.4314%** Exposure
### Highest State Flux (Mutation/Volatility)
- `base/src/lgacus01.cbl` -> **100.0%** Exposure
- `base/src/lgapvs01.cbl` -> **100.0%** Exposure
- `base/src/lgdpdb01.cbl` -> **100.0%** Exposure
- `base/src/lgicdb01.cbl` -> **100.0%** Exposure
- `base/src/lgicus01.cbl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `base/src/lgipdb01.cbl` -> **10** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp1.cbl` -> **8** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp2.cbl` -> **8** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp3.cbl` -> **8** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp4.cbl` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`base/src/lgipdb01.cbl`** -> AI Confidence: **99.32%**
2. **`base/src/lgupdb01.cbl`** -> AI Confidence: **99.32%**
3. **`base/src/lgtestp4.cbl`** -> AI Confidence: **99.29%**
4. **`base/src/lgapdb01.cbl`** -> AI Confidence: **99.2%**
5. **`base/src/lgtestc1.cbl`** -> AI Confidence: **99.17%**
6. **`base/src/lgtestp1.cbl`** -> AI Confidence: **99.17%**
7. **`base/src/lgtestp2.cbl`** -> AI Confidence: **99.17%**
8. **`base/src/lgtestp3.cbl`** -> AI Confidence: **99.17%**
9. **`base/src/lgacdb01.cbl`** -> AI Confidence: **99.09%**
10. **`base/src/lgicdb01.cbl`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `base/cntl/adef121.jcl` -> **100.0%** Exposure
- `base/cntl/asmmap.jcl` -> **100.0%** Exposure
- `base/cntl/cobol.jcl` -> **100.0%** Exposure
- `base/cntl/db2cre.jcl` -> **100.0%** Exposure
- `base/cntl/defdrep.jcl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `base/cntl/adef121.jcl` -> **100.0%** Exposure
- `base/cntl/asmmap.jcl` -> **100.0%** Exposure
- `base/cntl/cdef121.jcl` -> **100.0%** Exposure
- `base/cntl/cdef122.jcl` -> **100.0%** Exposure
- `base/cntl/cdef123.jcl` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `base/src/lgacdb01.cbl` -> **99.0093%** Exposure
### Algorithmic DoS Exposure
- `base/src/lgacdb01.cbl` -> **100.0%** Exposure
- `base/src/lgacdb02.cbl` -> **100.0%** Exposure
- `base/src/lgacus01.cbl` -> **100.0%** Exposure
- `base/src/lgacvs01.cbl` -> **100.0%** Exposure
- `base/src/lgapdb01.cbl` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `50` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `base/src/lgtestc1.cbl` (COBOL) -> Cumulative Risk: **707.59**
- **Archetype:** `file_cluster_8` (Distance: 12.194 IQR)
- **Magnitude:** 266.34 | **LOC:** 348 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (99.4854%)
- **Heaviest Functions:** `A-GAIN` (Impact: 63.9), `ERROR-OUT` (Impact: 38.7), `MAINLINE` (Impact: 6.8)

### 2. `base/src/lgicvs01.cbl` (COBOL) -> Cumulative Risk: **692.32**
- **Archetype:** `file_cluster_4` (Distance: 12.146 IQR)
- **Magnitude:** 177.4 | **LOC:** 231 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `MAINLINE` (Impact: 90.2), `A-EXIT` (Impact: 1.6)

### 3. `base/src/lgacdb01.cbl` (COBOL) -> Cumulative Risk: **677.03**
- **Archetype:** `file_cluster_8` (Distance: 12.873 IQR)
- **Magnitude:** 181.46 | **LOC:** 329 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9989%), Secrets Risk (99.0093%)
- **Heaviest Functions:** `INSERT-CUSTOMER` (Impact: 57.5), `MAINLINE` (Impact: 30.4), `Obtain-CUSTOMER-Number` (Impact: 14.7)

### 4. `base/src/lgtestp3.cbl` (COBOL) -> Cumulative Risk: **668.09**
- **Archetype:** `file_cluster_8` (Distance: 12.724 IQR)
- **Magnitude:** 264.62 | **LOC:** 300 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (99.276%)
- **Heaviest Functions:** `A-GAIN` (Impact: 72.0), `MAINLINE` (Impact: 6.9), `CLEARIT` (Impact: 3.5)

### 5. `base/src/lgtestp2.cbl` (COBOL) -> Cumulative Risk: **666.73**
- **Archetype:** `file_cluster_8` (Distance: 12.726 IQR)
- **Magnitude:** 267.58 | **LOC:** 301 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (99.2433%)
- **Heaviest Functions:** `A-GAIN` (Impact: 72.0), `MAINLINE` (Impact: 6.8), `CLEARIT` (Impact: 3.5)

### 6. `base/src/lgupol01.cbl` (COBOL) -> Cumulative Risk: **664.2**
- **Archetype:** `file_cluster_8` (Distance: 12.917 IQR)
- **Magnitude:** 132.84 | **LOC:** 202 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (94.099%)
- **Heaviest Functions:** `MAINLINE` (Impact: 45.0), `UPDATE-POLICY-DB2-INFO` (Impact: 22.9), `MAINLINE-EXIT` (Impact: 1.6)

### 7. `base/src/lgtestp1.cbl` (COBOL) -> Cumulative Risk: **659.13**
- **Archetype:** `file_cluster_8` (Distance: 12.718 IQR)
- **Magnitude:** 279.08 | **LOC:** 319 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (99.1675%)
- **Heaviest Functions:** `A-GAIN` (Impact: 72.0), `MAINLINE` (Impact: 7.0), `CLEARIT` (Impact: 3.5)

### 8. `base/src/lgtestp4.cbl` (COBOL) -> Cumulative Risk: **650.28**
- **Archetype:** `file_cluster_8` (Distance: 12.632 IQR)
- **Magnitude:** 292.18 | **LOC:** 319 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (98.5397%)
- **Heaviest Functions:** `A-GAIN` (Impact: 93.8), `MAINLINE` (Impact: 7.2), `CLEARIT` (Impact: 3.5)

### 9. `base/src/lgupdb01.cbl` (COBOL) -> Cumulative Risk: **649.07**
- **Archetype:** `file_cluster_11` (Distance: 15.008 IQR)
- **Magnitude:** 365.98 | **LOC:** 536 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Cognitive Load (92.2833%)
- **Heaviest Functions:** `UPDATE-POLICY-DB2-INFO` (Impact: 125.1), `UPDATE-MOTOR-DB2-INFO` (Impact: 45.2), `UPDATE-HOUSE-DB2-INFO` (Impact: 22.4)

### 10. `base/src/lgapvs01.cbl` (COBOL) -> Cumulative Risk: **647.02**
- **Archetype:** `file_cluster_8` (Distance: 11.807 IQR)
- **Magnitude:** 142.22 | **LOC:** 189 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (88.6431%)
- **Heaviest Functions:** `MAINLINE` (Impact: 35.5), `A-EXIT` (Impact: 22.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `base/src/lgipdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.768 IQR)
- **Top Global Matches:** file_cluster_11: 13.768, file_cluster_8: 13.77, file_cluster_0: 13.792
- **Magnitude:** 854.28 | **LOC:** 1031 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (80.5046%), Tech Debt (27.3354%)
**Top Internal Functions/Classes:**
  * `GET-ENDOW-DB2-INFO` (Impact: 70.8 | O(N^6) | DB: 22)
  * `GET-Commercial-DB2-INFO-3` (Impact: 67.3 | O(2^N) | DB: 22)
  * `GET-Commercial-DB2-INFO-5` (Impact: 67.3 | O(2^N) | DB: 21)
  * `GET-MOTOR-DB2-INFO` (Impact: 56.5 | O(N^6) | DB: 23)
  * `GET-HOUSE-DB2-INFO` (Impact: 56.0 | O(N^6) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 21`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 341`, `dead_code: 10`, `orphaned_logic: 10`
* *Architecture:* `io: 31`, `api: 1`, `import: 3`
* *Defense:* `safety: 34`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgwebst5.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.356 IQR)
- **Top Global Matches:** file_cluster_8: 11.356, file_cluster_12: 11.867, file_cluster_7: 11.978
- **Magnitude:** 426.64 | **LOC:** 803 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 226
- **Risk Profile:** Cognitive Load (95.8899%), Tech Debt (14.1625%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 100.5 | O(N^6) | DB: 226)
  * `Tran-Rate-Interval` (Impact: 8.5 | O(N^6) | DB: 21)
  * `Tran-Rate-Counts` (Impact: 4.0 | O(N^5) | DB: 5)
  * `A-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 52`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 295`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.008 IQR)
- **Top Global Matches:** file_cluster_11: 15.008, file_cluster_0: 15.07, file_cluster_17: 15.074
- **Magnitude:** 365.98 | **LOC:** 536 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (92.2833%), Tech Debt (43.4787%)
**Top Internal Functions/Classes:**
  * `UPDATE-POLICY-DB2-INFO` (Impact: 125.1 | O(N^5) | DB: 65)
    * *Intent:* ******************************************************************
  * `UPDATE-MOTOR-DB2-INFO` (Impact: 45.2 | O(N^6) | DB: 22)
  * `UPDATE-HOUSE-DB2-INFO` (Impact: 22.4 | O(N^5) | DB: 12)
  * `UPDATE-ENDOW-DB2-INFO` (Impact: 18.9 | O(N^4) | DB: 12)
  * `MAINLINE` (Impact: 14.2 | O(N^4) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 17`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 128`, `dead_code: 10`, `orphaned_logic: 6`
* *Architecture:* `io: 29`, `api: 1`, `import: 3`
* *Defense:* `safety: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgapdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.833 IQR)
- **Top Global Matches:** file_cluster_11: 13.833, file_cluster_0: 13.864, file_cluster_17: 13.901
- **Magnitude:** 340.06 | **LOC:** 596 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (85.0088%), Tech Debt (32.6724%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 66.7 | O(N^4) | DB: 28)
  * `INSERT-COMMERCIAL` (Impact: 36.5 | O(N^6) | DB: 25)
  * `INSERT-POLICY` (Impact: 30.9 | O(N^6) | DB: 24)
  * `INSERT-ENDOW` (Impact: 27.6 | O(N^6) | DB: 15)
  * `INSERT-MOTOR` (Impact: 16.0 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 17`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 136`, `dead_code: 9`, `orphaned_logic: 6`
* *Architecture:* `io: 19`, `api: 1`, `import: 3`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp4.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.632 IQR)
- **Top Global Matches:** file_cluster_8: 12.632, file_cluster_13: 12.897, file_cluster_2: 12.942
- **Magnitude:** 292.18 | **LOC:** 319 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (98.5397%), Tech Debt (73.1803%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 93.8 | O(N^6) | DB: 81)
  * `MAINLINE` (Impact: 7.2 | O(N^5) | DB: 14)
  * `CLEARIT` (Impact: 3.5 | O(N^5) | DB: 1)
  * `ERROR-OUT` (Impact: 3.5 | O(N^5) | DB: 3)
  * `ENDIT` (Impact: 3.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 166`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.718 IQR)
- **Top Global Matches:** file_cluster_8: 12.718, file_cluster_2: 12.921, file_cluster_12: 12.937
- **Magnitude:** 279.08 | **LOC:** 319 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (99.1675%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 72.0 | O(N^6) | DB: 87)
  * `MAINLINE` (Impact: 7.0 | O(N^5) | DB: 9)
  * `CLEARIT` (Impact: 3.5 | O(N^5) | DB: 1)
  * `ERROR-OUT` (Impact: 3.5 | O(N^5) | DB: 3)
  * `ENDIT` (Impact: 3.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 175`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.726 IQR)
- **Top Global Matches:** file_cluster_8: 12.726, file_cluster_12: 12.935, file_cluster_2: 12.936
- **Magnitude:** 267.58 | **LOC:** 301 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 80
- **Risk Profile:** Cognitive Load (99.2433%), Tech Debt (78.4314%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 72.0 | O(N^6) | DB: 80)
  * `MAINLINE` (Impact: 6.8 | O(N^5) | DB: 5)
  * `CLEARIT` (Impact: 3.5 | O(N^5) | DB: 1)
  * `ERROR-OUT` (Impact: 3.5 | O(N^5) | DB: 3)
  * `ENDIT` (Impact: 3.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 164`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestc1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.194 IQR)
- **Top Global Matches:** file_cluster_8: 12.194, file_cluster_12: 12.41, file_cluster_13: 12.477
- **Magnitude:** 266.34 | **LOC:** 348 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (99.4854%), Tech Debt (60.4806%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 63.9 | O(N^6) | DB: 58)
  * `ERROR-OUT` (Impact: 38.7 | O(N^6) | DB: 47)
  * `MAINLINE` (Impact: 6.8 | O(N^5) | DB: 4)
  * `CLEARIT` (Impact: 3.5 | O(N^5) | DB: 1)
    * *Intent:* * Send message to terminal and return
  * `ENDIT` (Impact: 3.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 8`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 131`, `orphaned_logic: 7`
* *Architecture:* `io: 23`, `concurrency: 7`, `import: 2`
* *Defense:* `safety: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp3.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.724 IQR)
- **Top Global Matches:** file_cluster_8: 12.724, file_cluster_12: 12.929, file_cluster_2: 12.93
- **Magnitude:** 264.62 | **LOC:** 300 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (99.276%), Tech Debt (79.219%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 72.0 | O(N^6) | DB: 75)
  * `MAINLINE` (Impact: 6.9 | O(N^5) | DB: 7)
  * `CLEARIT` (Impact: 3.5 | O(N^5) | DB: 1)
  * `ERROR-OUT` (Impact: 3.5 | O(N^5) | DB: 3)
  * `ENDIT` (Impact: 3.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 161`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgacdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.873 IQR)
- **Top Global Matches:** file_cluster_8: 12.873, file_cluster_13: 12.882, file_cluster_11: 12.887
- **Magnitude:** 181.46 | **LOC:** 329 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (87.4239%), Tech Debt (37.6438%)
**Top Internal Functions/Classes:**
  * `INSERT-CUSTOMER` (Impact: 57.5 | O(N^6) | DB: 28)
    * *Intent:* *----------------------------------------------------------------* * Process incoming commarea * *--...
  * `MAINLINE` (Impact: 30.4 | O(N^6) | DB: 20)
    * *Intent:* *----------------------------------------------------------------* * Definitions required for data m...
  * `Obtain-CUSTOMER-Number` (Impact: 14.7 | O(N^6) | DB: 3)
    * *Intent:* *----------------------------------------------------------------* * Common code * *----------------...
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
    * *Intent:* *----------------------------------------------------------------*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `dead_code: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 9`, `api: 1`, `import: 3`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgicvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.146 IQR)
- **Top Global Matches:** file_cluster_4: 12.146, file_cluster_8: 12.262, file_cluster_17: 12.478
- **Magnitude:** 177.4 | **LOC:** 231 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 79
- **Risk Profile:** Cognitive Load (96.4808%), Tech Debt (33.3045%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 90.2 | O(N^6) | DB: 79)
  * `A-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 30`, `api: 1`, `concurrency: 12`
* *Defense:* `safety: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.943 IQR)
- **Top Global Matches:** file_cluster_8: 11.943, file_cluster_12: 12.301, file_cluster_13: 12.366
- **Magnitude:** 160.24 | **LOC:** 207 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (91.8321%), Tech Debt (37.8992%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 45.2 | O(N^5) | DB: 39)
  * `A-EXIT` (Impact: 22.8 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 14`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 1`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgapvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.807 IQR)
- **Top Global Matches:** file_cluster_8: 11.807, file_cluster_13: 12.237, file_cluster_12: 12.247
- **Magnitude:** 142.22 | **LOC:** 189 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (88.6431%), Tech Debt (43.1932%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 35.5 | O(N^5) | DB: 30)
  * `A-EXIT` (Impact: 22.8 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 14`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupol01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.917 IQR)
- **Top Global Matches:** file_cluster_8: 12.917, file_cluster_11: 12.958, file_cluster_0: 13.002
- **Magnitude:** 132.84 | **LOC:** 202 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (94.099%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 45.0 | O(N^4) | DB: 21)
  * `UPDATE-POLICY-DB2-INFO` (Impact: 22.9 | O(N^6) | DB: 7)
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgicdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.736 IQR)
- **Top Global Matches:** file_cluster_11: 13.736, file_cluster_13: 13.74, file_cluster_0: 13.796
- **Magnitude:** 130.22 | **LOC:** 246 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (91.33%), Tech Debt (62.5787%)
**Top Internal Functions/Classes:**
  * `GET-CUSTOMER-INFO` (Impact: 49.0 | O(N^6) | DB: 18)
    * *Intent:* ****************************************************************** * P R O C E D U R E S
  * `MAINLINE` (Impact: 13.2 | O(N^3) | DB: 15)
  * `MAINLINE-END` (Impact: 1.6 | O(N^2))
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `dead_code: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 6`, `api: 1`, `import: 3`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgdpdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.167 IQR)
- **Top Global Matches:** file_cluster_11: 13.167, file_cluster_13: 13.198, file_cluster_0: 13.213
- **Magnitude:** 125.92 | **LOC:** 246 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (93.441%), Tech Debt (31.3794%)
**Top Internal Functions/Classes:**
  * `MAINLINE-EXIT` (Impact: 34.1 | O(N^6) | DB: 25)
    * *Intent:* ****************************************************************** * P R O C E D U R E S ***********...
  * `MAINLINE` (Impact: 32.2 | O(N^5) | DB: 21)
    * *Intent:* *----------------------------------------------------------------* * Definitions required for data m...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 13`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `api: 1`, `import: 2`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgucdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.629 IQR)
- **Top Global Matches:** file_cluster_13: 12.629, file_cluster_11: 12.703, file_cluster_8: 12.717
- **Magnitude:** 112.32 | **LOC:** 223 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (88.005%), Tech Debt (45.1395%)
**Top Internal Functions/Classes:**
  * `UPDATE-CUSTOMER-INFO` (Impact: 45.0 | O(N^6) | DB: 18)
    * *Intent:* *----------------------------------------------------------------* * Common code *...
  * `MAINLINE` (Impact: 13.9 | O(N^4) | DB: 14)
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 13`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 7`, `api: 1`, `import: 3`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgacdb02.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.959 IQR)
- **Top Global Matches:** file_cluster_13: 12.959, file_cluster_11: 12.962, file_cluster_0: 12.992
- **Magnitude:** 104.62 | **LOC:** 226 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (91.16%), Tech Debt (51.9831%)
**Top Internal Functions/Classes:**
  * `INSERT-CUSTOMER-PASSWORD` (Impact: 34.1 | O(N^6) | DB: 16)
  * `MAINLINE` (Impact: 19.4 | O(N^3) | DB: 14)
    * *Intent:* *----------------------------------------------------------------* *--------------------------------...
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 13`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 5`, `api: 1`, `import: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgdpol01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.549 IQR)
- **Top Global Matches:** file_cluster_11: 13.549, file_cluster_0: 13.578, file_cluster_17: 13.581
- **Magnitude:** 97.02 | **LOC:** 187 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (94.3314%), Tech Debt (43.2348%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 31.9 | O(N^4) | DB: 17)
  * `MAINLINE-EXIT` (Impact: 23.1 | O(N^6) | DB: 10)
    * *Intent:* *----------------------------------------------------------------* * Common code * *----------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 12`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgipvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.368 IQR)
- **Top Global Matches:** file_cluster_8: 11.368, file_cluster_12: 11.9, file_cluster_0: 11.926
- **Magnitude:** 93.12 | **LOC:** 150 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (85.393%), Tech Debt (60.5379%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 33.3 | O(N^5) | DB: 43)
  * `A-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`, `orphaned_logic: 2`
* *Architecture:* `io: 14`, `api: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgacus01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.651 IQR)
- **Top Global Matches:** file_cluster_11: 14.651, file_cluster_17: 14.691, file_cluster_13: 14.693
- **Magnitude:** 84.8 | **LOC:** 180 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (92.8801%), Tech Debt (71.5257%)
**Top Internal Functions/Classes:**
  * `INSERT-CUSTOMER` (Impact: 22.9 | O(N^6) | DB: 7)
  * `MAINLINE` (Impact: 15.4 | O(N^3) | DB: 15)
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 42`, `dead_code: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgicus01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.755 IQR)
- **Top Global Matches:** file_cluster_8: 11.755, file_cluster_13: 11.981, file_cluster_12: 12.127
- **Magnitude:** 84.12 | **LOC:** 167 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (92.7012%), Tech Debt (87.2926%)
**Top Internal Functions/Classes:**
  * `GET-CUSTOMER-INFO` (Impact: 22.9 | O(N^6) | DB: 7)
    * *Intent:* *
  * `MAINLINE` (Impact: 13.1 | O(N^3) | DB: 15)
  * `MAINLINE-END` (Impact: 1.6 | O(N^2))
    * *Intent:* ****************************************************************** * P R O C E D U R E S
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 42`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgucus01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.393 IQR)
- **Top Global Matches:** file_cluster_0: 13.393, file_cluster_11: 13.394, file_cluster_17: 13.402
- **Magnitude:** 78.72 | **LOC:** 173 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (91.16%), Tech Debt (70.7943%)
**Top Internal Functions/Classes:**
  * `UPDATE-CUSTOMER-INFO` (Impact: 22.9 | O(N^6) | DB: 7)
  * `MAINLINE` (Impact: 15.3 | O(N^3) | DB: 13)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
    * *Intent:* ******************************************************************
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgastat1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.392 IQR)
- **Top Global Matches:** file_cluster_8: 10.392, file_cluster_12: 10.942, file_cluster_13: 10.957
- **Magnitude:** 77.72 | **LOC:** 141 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (80.4568%), Tech Debt (40.6764%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 45.0 | O(N^6) | DB: 14)
  * `MAINLINE-EXIT` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/cntl/adef121.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.142 IQR)
- **Top Global Matches:** file_cluster_8: 6.142, file_cluster_7: 7.473, file_cluster_1: 7.64
- **Magnitude:** 76.48 | **LOC:** 74 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.3504%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 16`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 6`
* *Architecture:* `io: 20`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `base/src/lgucus01.cbl` (COBOL) | Magnitude: 78.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 96, state_mutation: 36, structural_boundaries: 12, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `base/src/lgipdb01.cbl` (COBOL) | Magnitude: 854.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 739, state_mutation: 341, branch: 117, safety: 34
- `base/src/lgicdb01.cbl` (COBOL) | Magnitude: 130.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 61, branch: 18, structural_boundaries: 13
- `base/src/lgapol01.cbl` (COBOL) | Magnitude: 75.98 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 34, structural_boundaries: 11, branch: 10
- `base/src/lgdpol01.cbl` (COBOL) | Magnitude: 97.02 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, state_mutation: 39, branch: 16, structural_boundaries: 12
- `base/src/lgapdb01.cbl` (COBOL) | Magnitude: 340.06 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 408, state_mutation: 136, branch: 51, reflection_metaprogramming: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `base/bin/install.sh` (SHELL) | Magnitude: 6.24 | Delta: **0.31 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 25, structural_boundaries: 9, state_mutation: 3, sec_entropy: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `base/src/lgacdb02.cbl` (COBOL) | Magnitude: 104.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 46, branch: 16, structural_boundaries: 13
- `base/src/lgucdb01.cbl` (COBOL) | Magnitude: 112.32 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 48, branch: 15, structural_boundaries: 13
- `base/src/lgipol01.cbl` (COBOL) | Magnitude: 64.34 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 30, structural_boundaries: 11, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `base/src/lgicvs01.cbl` (COBOL) | Magnitude: 177.4 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 180, state_mutation: 69, io: 30, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `base/src/lgacdb01.cbl` (COBOL) | Magnitude: 181.46 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 213, state_mutation: 72, branch: 24, reflection_metaprogramming: 18
- `base/src/lgupol01.cbl` (COBOL) | Magnitude: 132.84 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 60, branch: 21, structural_boundaries: 12
- `base/src/lgstsq.cbl` (COBOL) | Magnitude: 66.4 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 38, io: 15, structural_boundaries: 11
- `base/src/lgtestp1.cbl` (COBOL) | Magnitude: 279.08 | Delta: **0.203 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 259, state_mutation: 175, reflection_metaprogramming: 26, branch: 22
- `base/src/lgtestp3.cbl` (COBOL) | Magnitude: 264.62 | Delta: **0.205 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 241, state_mutation: 161, reflection_metaprogramming: 25, branch: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `base/src/lgtestp3.cbl` -> **Severity: 639.477** (Blast Radius: 7.752 * Doc Risk: 82.4919%)
- `base/src/lgtestp2.cbl` -> **Severity: 634.22** (Blast Radius: 7.752 * Doc Risk: 81.8137%)
- `base/src/lgapdb01.cbl` -> **Severity: 610.906** (Blast Radius: 7.752 * Doc Risk: 78.8063%)
- `base/src/lgtestp4.cbl` -> **Severity: 610.117** (Blast Radius: 7.752 * Doc Risk: 78.7044%)
- `base/src/lgtestp1.cbl` -> **Severity: 608.931** (Blast Radius: 7.752 * Doc Risk: 78.5515%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
