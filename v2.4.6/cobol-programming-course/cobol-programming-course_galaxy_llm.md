# ARCHITECTURAL_BRIEF: cobol-programming-course
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/cobol-programming-course` |
| **Timestamp** | `2026-08-03T19:26:12.467258+00:00` |
| **Scan Duration** | `0.73s` |
| **Git Branch** | `master` |
| **Git Commit** | `11aca51998e11181925ff16c20b32c220360ff66` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-programming-course.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 74 malicious artifacts.

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
| Total Artifacts | 360 |
| Analyzed Artifacts (Scanned) | 120 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 240 |
| Total LOC | 4080 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 33.3% |
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
| MARKDOWN | 43 | 0 | 35.8% |
| JCL | 42 | 916 | 35.0% |
| COBOL | 32 | 2770 | 26.7% |
| JSON | 2 | 384 | 1.7% |
| CSV | 1 | 10 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.419`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 77 | 64.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 43 | 35.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 240*

**Composition by Extension & Reason:**
- `.png`: 219x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 5x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.tex`: 4x Excluded (Unsupported Extension: '.tex')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xlsx`: 1x Excluded (Explicitly Denied Extension: '.xlsx')
- `.jcl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 79.1 | 26.0 | 25.9 | 29.2 |
| Error & Exception Exposure | 0.0 | 87.8 | 33.4 | 29.6 | 53.8 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 2.8 | 0.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.9 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 94.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 64.7 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 66.4 | 81.0 | 94.1 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 37.9 | 20.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 42.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` (Hits: 33)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (Hits: 32)
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ADOPTERS.md** (`ADOPTERS.md`) — 0 inbound connections
2. **COBOL Programming Course #1 - Getting Started.md** (`COBOL Programming Course #1 - Getting Started/COBOL Programming Course #1 - Getting Started.md`) — 0 inbound connections
3. **README.md** (`COBOL Programming Course #1 - Getting Started/README.md`) — 0 inbound connections
4. **COBOL Programming Course #2 - Learning COBOL.md** (`COBOL Programming Course #2 - Learning COBOL/COBOL Programming Course #2 - Learning COBOL.md`) — 0 inbound connections
5. **README.md** (`COBOL Programming Course #2 - Learning COBOL/Labs/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **DB2CBL.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl`) — 10 outbound dependencies
2. **IGYWCL.jcl** (`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl`) — 7 outbound dependencies
3. **IGYWCLG.jcl** (`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl`) — 7 outbound dependencies
4. **DB2SETUP.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DB2SETUP.jcl`) — 5 outbound dependencies
5. **IGYWC.jcl** (`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWC.jcl`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **49.6** | LOC: 12
  * *Intent:* ***************************************************** * LIST ALL CLIENTS * *****************************************************...
- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **49.6** | LOC: 12
- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **49.6** | LOC: 12
- `LIST-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **36.9** | LOC: 18
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **36.9** | LOC: 18
  * *Intent:* ***************************************************** * STRUCTURE FOR CUSTOMER RECORD * *****************************************************...
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **36.9** | LOC: 18
  * *Intent:* *
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **36.9** | LOC: 18
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **36.9** | LOC: 18
- `PROCESS-INPUT` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **15.3** | LOC: 7
- `PROCESS-INPUT` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **15.3** | LOC: 7
  * *Intent:* *****************************************************

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `LIMIT-BALANCE-TOTAL` (@ `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol`) -> **O(N^6)**
- `LIMIT-BALANCE-TOTAL` (@ `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol`) -> **O(N^6)**
- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> **O(N^6)**
  * *Intent:* ***************************************************** * LIST ALL CLIENTS * *****************************************************...
- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> **O(N^6)**
- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> **O(N^6)**
- `LIST-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> **O(N^5)**
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> **O(N^5)**
  * *Intent:* ***************************************************** * STRUCTURE FOR CUSTOMER RECORD * *****************************************************...
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> **O(N^5)**
  * *Intent:* *
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> **O(N^5)**
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> **O(N^5)**

### Highest Data Gravity (Database Complexity)
- `LIST-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> DB Complexity: **24**
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> DB Complexity: **24**
  * *Intent:* ***************************************************** * STRUCTURE FOR CUSTOMER RECORD * *****************************************************...
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> DB Complexity: **24**
  * *Intent:* *
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> DB Complexity: **24**
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> DB Complexity: **24**
- `LIMIT-BALANCE-TOTAL` (@ `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol`) -> DB Complexity: **15**
- `LIMIT-BALANCE-TOTAL` (@ `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol`) -> DB Complexity: **15**
- `IS-STATE-VIRGINIA` (@ `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl`) -> DB Complexity: **15**
- `IS-STATE-VIRGINIA` (@ `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl`) -> DB Complexity: **15**
  * *Intent:* *
- `LIMIT-BALANCE-TOTAL` (@ `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol`) -> DB Complexity: **14**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `COBOL Programming Course #2 - Learning COBOL/Labs/jcl` | 23 | 1300.36 | 26.67% | 0.0% |
| `COBOL Programming Course #2 - Learning COBOL/Labs/cbl` | 23 | 645.34 | 23.86% | 37.89% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/cbl` | 3 | 530.7 | 71.55% | 98.4% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc` | 3 | 253.03 | 32.57% | 0.0% |
| `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc` | 3 | 226.04 | 20.82% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/jcl` | 10 | 182.88 | 9.68% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl` | 2 | 168.66 | 58.56% | 37.34% |
| `COBOL Programming Course #2 - Learning COBOL` | 2 | 76.72 | 0.0% | 0.0% |
| `COBOL Programming Course #4 - Testing/Labs/jcl` | 2 | 76.2 | 17.11% | 0.0% |
| `__monolith__` | 15 | 65.28 | 0.88% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0013.cobol` -> **99.9999%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **99.9987%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` -> **99.9141%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/COBOL.cobol` -> **99.8818%** Exposure
- `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` -> **99.708%** Exposure
### Highest State Flux (Mutation/Volatility)
- `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` -> **99.9995%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` -> **99.9994%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/PAYROL00.cobol` -> **99.9447%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/PAYROL0X.cobol` -> **99.9447%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **10** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` -> **9** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` -> **9** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` -> **6** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/COBOL.cobol` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`COBOL Programming Course #4 - Testing/Labs/tests/deptpay.cut`** -> AI Confidence: **99.29%**
2. **`COBOL Programming Course #4 - Testing/Labs/tests/emppay.cut`** -> AI Confidence: **99.29%**
3. **`COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`** -> AI Confidence: **99.17%**
4. **`COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`** -> AI Confidence: **99.17%**
5. **`COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl`** -> AI Confidence: **99.11%**
6. **`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl`** -> AI Confidence: **99.07%**
7. **`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl`** -> AI Confidence: **99.07%**
8. **`COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl`** -> AI Confidence: **99.07%**
9. **`COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol`** -> AI Confidence: **99.06%**
10. **`COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DB2SETUP.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #4 - Testing/Labs/jcl/DEPTPAY.JCL` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/ADDAMT.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0001J.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0002J.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0003J.jcl` -> **100.0%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0004J.jcl` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` -> **100.0%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `83` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL) -> Cumulative Risk: **695.67**
- **Archetype:** `file_cluster_8` (Distance: 11.315 IQR)
- **Magnitude:** 204.64 | **LOC:** 202 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.974%), State Flux (99.8181%)
- **Heaviest Functions:** `SQL-ERROR-HANDLING` (Impact: 49.6), `GET-ALL` (Impact: 36.9), `GET-SPECIFIC` (Impact: 36.9)

### 2. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL) -> Cumulative Risk: **690.59**
- **Archetype:** `file_cluster_8` (Distance: 11.284 IQR)
- **Magnitude:** 202.52 | **LOC:** 189 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9917%), State Flux (99.7125%)
- **Heaviest Functions:** `SQL-ERROR-HANDLING` (Impact: 49.6), `GET-ALL` (Impact: 36.9), `GET-SPECIFIC` (Impact: 36.9)

### 3. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL) -> Cumulative Risk: **673.78**
- **Archetype:** `file_cluster_8` (Distance: 10.782 IQR)
- **Magnitude:** 123.54 | **LOC:** 145 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.033%), Documentation (98.7412%)
- **Heaviest Functions:** `SQL-ERROR-HANDLING` (Impact: 49.6), `LIST-ALL` (Impact: 36.9), `PROG-START` (Impact: 5.2)

### 4. `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` (COBOL) -> Cumulative Risk: **649.02**
- **Archetype:** `file_cluster_8` (Distance: 11.381 IQR)
- **Magnitude:** 50.62 | **LOC:** 55 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9442%), Tech Debt (99.708%)
- **Heaviest Functions:** `PAYMENT-WEEKLY` (Impact: 13.0), `PAYMENT-MONTHLY` (Impact: 7.9), `SHOW-OUTPUT` (Impact: 1.9)

### 5. `COBOL Programming Course #4 - Testing/Labs/cbl/DEPTPAY.CBL` (COBOL) -> Cumulative Risk: **599.44**
- **Archetype:** `file_cluster_8` (Distance: 9.575 IQR)
- **Magnitude:** 10.96 | **LOC:** 37 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8316%), Documentation (99.6886%), Algorithmic Dos (99.2915%)
- **Heaviest Functions:** `AVERAGE-SALARY` (Impact: 3.3)

### 6. `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0014J.jcl` (JCL) -> Cumulative Risk: **552.85**
- **Archetype:** `file_cluster_8` (Distance: 6.392 IQR)
- **Magnitude:** 58.32 | **LOC:** 17 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Injection Surface (100.0%), Logic Bomb (79.8966%)

### 7. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (COBOL) -> Cumulative Risk: **515.27**
- **Archetype:** `file_cluster_8` (Distance: 10.139 IQR)
- **Magnitude:** 56.44 | **LOC:** 131 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9987%), State Flux (90.8066%)
- **Heaviest Functions:** `2100-READ-TEN-RECORDS` (Impact: 12.2), `2300-READ-NEXT-RECORDS` (Impact: 12.2), `2000-READ-FIRST-RECORD` (Impact: 4.7)

### 8. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` (COBOL) -> Cumulative Risk: **493.33**
- **Archetype:** `file_cluster_8` (Distance: 10.068 IQR)
- **Magnitude:** 34.76 | **LOC:** 73 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.7895%), State Flux (99.0919%), Tech Debt (97.4221%)
- **Heaviest Functions:** `LOAD-TABLES` (Impact: 14.3), `SEARCH-RECORD` (Impact: 10.4)

### 9. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` (COBOL) -> Cumulative Risk: **489.72**
- **Archetype:** `file_cluster_8` (Distance: 10.001 IQR)
- **Magnitude:** 32.38 | **LOC:** 74 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.7086%), State Flux (98.9714%), Tech Debt (97.121%)
- **Heaviest Functions:** `LOAD-TABLES` (Impact: 14.3), `SEARCH-RECORD` (Impact: 8.0)

### 10. `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0013J.jcl` (JCL) -> Cumulative Risk: **485.66**
- **Archetype:** `file_cluster_8` (Distance: 6.377 IQR)
- **Magnitude:** 58.32 | **LOC:** 17 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Documentation (98.5936%), Logic Bomb (79.8966%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.315 IQR)
- **Top Global Matches:** file_cluster_8: 11.315, file_cluster_12: 11.742, file_cluster_0: 11.763
- **Magnitude:** 204.64 | **LOC:** 202 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (79.1041%), Tech Debt (98.2513%)
**Top Internal Functions/Classes:**
  * `SQL-ERROR-HANDLING` (Impact: 49.6 | O(N^6) | DB: 1)
  * `GET-ALL` (Impact: 36.9 | O(N^5) | DB: 24)
    * *Intent:* ***************************************************** * STRUCTURE FOR CUSTOMER RECORD * ************...
  * `GET-SPECIFIC` (Impact: 36.9 | O(N^5) | DB: 24)
    * *Intent:* *
  * `PROCESS-INPUT` (Impact: 15.3 | O(N^4) | DB: 4)
  * `PROG-START` (Impact: 10.3 | O(N^4) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 12`, `args: 1`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`, `orphaned_logic: 9`
* *Architecture:* `io: 27`, `api: 1`
* *Defense:* `safety: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.581 IQR)
- **Top Global Matches:** file_cluster_8: 6.581, file_cluster_7: 7.84, file_cluster_1: 8.01
- **Magnitude:** 204.41 | **LOC:** 61 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.6038%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 38`, `args: 2`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 3`
* *Architecture:* `io: 33`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IGY630.SIGYCOMP, &SYSUID..DBRMLIB(&MBR), DSNC10.DBCG.SDSNEXIT, &SYSUID..CBL(&MBR), DSNC10.SDSNLOAD, &SYSUID..LOAD(&MBR), CEE.SCEERUN2, &SYSUID..DBRMLIB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.284 IQR)
- **Top Global Matches:** file_cluster_8: 11.284, file_cluster_12: 11.668, file_cluster_0: 11.68
- **Magnitude:** 202.52 | **LOC:** 189 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (74.8469%), Tech Debt (98.3218%)
**Top Internal Functions/Classes:**
  * `SQL-ERROR-HANDLING` (Impact: 49.6 | O(N^6) | DB: 1)
  * `GET-ALL` (Impact: 36.9 | O(N^5) | DB: 24)
  * `GET-SPECIFIC` (Impact: 36.9 | O(N^5) | DB: 24)
  * `PROCESS-INPUT` (Impact: 15.3 | O(N^4) | DB: 4)
    * *Intent:* *****************************************************
  * `PROG-START` (Impact: 10.3 | O(N^4) | DB: 13)
    * *Intent:* *****************************************************
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 12`, `args: 1`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`, `orphaned_logic: 9`
* *Architecture:* `io: 27`, `api: 1`
* *Defense:* `safety: 8`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.332 IQR)
- **Top Global Matches:** file_cluster_8: 6.332, file_cluster_7: 7.637, file_cluster_1: 7.803
- **Magnitude:** 124.99 | **LOC:** 51 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.0818%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 34`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 2`
* *Architecture:* `io: 26`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..CBL(&SRC), &SYSUID..LOAD(&SRC), &LIBPRFX..SCEERUN, &LNGPRFX..SIGYCOMP, &LIBPRFX..SCEELKED, &LIBPRFX..SCEERUN2, &LIBPRFX..SCEELKEX
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.782 IQR)
- **Top Global Matches:** file_cluster_8: 10.782, file_cluster_0: 11.215, file_cluster_12: 11.259
- **Magnitude:** 123.54 | **LOC:** 145 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (60.7025%), Tech Debt (98.6288%)
**Top Internal Functions/Classes:**
  * `SQL-ERROR-HANDLING` (Impact: 49.6 | O(N^6) | DB: 1)
    * *Intent:* ***************************************************** * LIST ALL CLIENTS * *************************...
  * `LIST-ALL` (Impact: 36.9 | O(N^5) | DB: 24)
  * `PROG-START` (Impact: 5.2 | O(N^4) | DB: 6)
  * `PRINT-AND-GET1` (Impact: 5.2 | O(N^4) | DB: 3)
    * *Intent:* *------------------ *****************************************************
  * `PRINT-A-LINE` (Impact: 2.9 | O(N^4) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 12`, `args: 1`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `orphaned_logic: 6`
* *Architecture:* `io: 15`, `api: 1`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0033J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.361 IQR)
- **Top Global Matches:** file_cluster_8: 6.361, file_cluster_7: 7.647, file_cluster_1: 7.838
- **Magnitude:** 105.6 | **LOC:** 31 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (24.8041%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 6`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 17`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.073 IQR)
- **Top Global Matches:** file_cluster_8: 11.073, file_cluster_17: 11.667, file_cluster_0: 11.673
- **Magnitude:** 89.34 | **LOC:** 205 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (59.3971%), Tech Debt (36.4962%)
**Top Internal Functions/Classes:**
  * `IS-OVERLIMIT` (Impact: 13.2 | O(N^4) | DB: 6)
  * `IS-STATE-VIRGINIA` (Impact: 12.8 | O(N^3) | DB: 15)
    * *Intent:* *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `orphaned_logic: 2`
* *Architecture:* `io: 26`
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.946 IQR)
- **Top Global Matches:** file_cluster_8: 10.946, file_cluster_7: 11.551, file_cluster_0: 11.57
- **Magnitude:** 79.32 | **LOC:** 196 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (57.7238%), Tech Debt (38.193%)
**Top Internal Functions/Classes:**
  * `IS-STATE-VIRGINIA` (Impact: 12.8 | O(N^3) | DB: 15)
  * `IS-OVERLIMIT` (Impact: 6.3 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 8`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`, `orphaned_logic: 2`
* *Architecture:* `io: 26`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.253 IQR)
- **Top Global Matches:** file_cluster_8: 6.253, file_cluster_7: 7.569, file_cluster_1: 7.731
- **Magnitude:** 76.33 | **LOC:** 39 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (24.8755%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 29`, `args: 1`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 2`
* *Architecture:* `io: 20`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..CBL(&SRC), &SYSUID..LOAD(&SRC), &LIBPRFX..SCEERUN, &LNGPRFX..SIGYCOMP, &LIBPRFX..SCEELKED, &LIBPRFX..SCEERUN2, &LIBPRFX..SCEELKEX
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/COBOL Programming Course #2 - Learning COBOL.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 75.72 | **LOC:** 3786 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/ADDAMT.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.04 IQR)
- **Top Global Matches:** file_cluster_8: 6.04, file_cluster_7: 7.391, file_cluster_1: 7.571
- **Magnitude:** 63.52 | **LOC:** 27 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.0168%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 5`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/COBRUN.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.201 IQR)
- **Top Global Matches:** file_cluster_8: 6.201, file_cluster_7: 7.524, file_cluster_1: 7.702
- **Magnitude:** 61.44 | **LOC:** 23 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (27.1796%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..COBRUN.OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0001J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0002J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0003J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0004J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0005J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0006J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0007J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0008J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0009J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0010J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0011J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0012J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL006AJ.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.222 IQR)
- **Top Global Matches:** file_cluster_8: 6.222, file_cluster_7: 7.541, file_cluster_1: 7.719
- **Magnitude:** 60.92 | **LOC:** 22 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.2201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..DATA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL) | Magnitude: 202.52 | Delta: **0.384 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 156, branch: 39, state_mutation: 31, io: 27
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0014.cobol` (COBOL) | Magnitude: 16.26 | Delta: **0.386 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, debug_prints: 2, class_start: 1
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` (COBOL) | Magnitude: 36.3 | Delta: **0.395 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 115, io: 22, state_mutation: 19, structural_boundaries: 8
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0005.cobol` (COBOL) | Magnitude: 36.3 | Delta: **0.395 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 115, io: 22, state_mutation: 19, structural_boundaries: 8
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` (COBOL) | Magnitude: 32.76 | Delta: **0.422 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 26, io: 24, branch: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0014J.jcl` -> **Athar Ramzan** (100.0% isolated ownership) | Magnitude: 58.32

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0014J.jcl` -> **Severity: 833.3** (Blast Radius: 8.333 * Doc Risk: 100.0%)
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` -> **Severity: 833.231** (Blast Radius: 8.333 * Doc Risk: 99.9917%)
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` -> **Severity: 833.083** (Blast Radius: 8.333 * Doc Risk: 99.974%)
- `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` -> **Severity: 832.835** (Blast Radius: 8.333 * Doc Risk: 99.9442%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` -> **Severity: 831.902** (Blast Radius: 8.333 * Doc Risk: 99.8322%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
