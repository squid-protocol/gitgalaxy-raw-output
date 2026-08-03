# ARCHITECTURAL_BRIEF: Cobol-Projects
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/Cobol-Projects` |
| **Timestamp** | `2026-08-03T19:27:52.836403+00:00` |
| **Scan Duration** | `0.86s` |
| **Git Branch** | `release` |
| **Git Commit** | `2cc05108d07d8d1ee2297e4f5bd6d274638b7f6e` |
| **Git Remote** | `https://github.com/dscobol/Cobol-Projects.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 272 malicious artifacts.

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
| Total Artifacts | 349 |
| Analyzed Artifacts (Scanned) | 328 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21 |
| Total LOC | 29282 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.0% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4444 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7143 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 176 | 23998 | 53.7% |
| SHELL | 68 | 671 | 20.7% |
| PLAINTEXT | 50 | 0 | 15.2% |
| JCL | 24 | 4565 | 7.3% |
| MARKDOWN | 6 | 0 | 1.8% |
| PYTHON | 4 | 48 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.981`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 264 | 80.5% |
| file_cluster_12 | 3 | 0.9% |
| file_cluster_4 | 3 | 0.9% |
| file_cluster_0 | 1 | 0.3% |
| file_cluster_17 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 56 | 17.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21*

**Composition by Extension & Reason:**
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.cbl`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 3x Excluded (Unsupported Extension: '.dat')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 7423 LOC)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.csv`: 1x Excluded (Static Asset Blob without Intent: 1002 LOC)
- `.xls`: 1x Excluded (Explicitly Denied Extension: '.xls')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 26.7 | 19.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 37.1 | 22.7 | 94.2 |
| Tech Debt Exposure | 0.0 | 100.0 | 60.6 | 96.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.0 | 2.3 | 80.0 |
| API Exposure | 0.0 | 11.8 | 0.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 73.9 | 99.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 81.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 100.0 | 68.1 | 71.9 | 60.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 30.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 75.3 | 1.4 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (Hits: 51)
- `OpenCobol/ECBAP/cbl/ws162e.cbl` (Hits: 51)
- `OpenCobol/ECBAP/cbl/ws162o.cbl` (Hits: 46)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wsfst.cpy** (`Mainframe/ZOS/Zowe/Simple_Report/COPYBOOK/wsfst.cpy`) — 6 inbound connections
2. **PATIENT.cpy** (`common/cpy/PATIENT.cpy`) — 3 inbound connections
3. **blue.py** (`Extra-Stuff/Blue/blue.py`) — 0 inbound connections
4. **mvt-convert.py** (`Extra-Stuff/MVT-Convert/mvt-convert.py`) — 0 inbound connections
5. **unnum.py** (`Extra-Stuff/UnNumRight/unnum.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ALLOCATE.jcl** (`Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl`) — 5 outbound dependencies
2. **VSIOINST.JCL** (`Mainframe/MVS/herc01/jcl/VSIOINST.JCL`) — 4 outbound dependencies
3. **allocate.jcl** (`Mainframe/ZOS/Zowe/Initialize/JCL/allocate.jcl`) — 4 outbound dependencies
4. **EXE4.jcl** (`Mainframe/ZOS/Normal/jcl/EXE4.jcl`) — 3 outbound dependencies
5. **WS120.cbl** (`Mainframe/ZOS/ECBAP/cbl/WS120.cbl`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `2000-Process` (@ `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl`) -> Impact: **915.4** | LOC: 320
- `2000-Process` (@ `OpenCobol/ECBAP/cbl/TABLE1.cbl`) -> Impact: **467.5** | LOC: 186
- `2120-Calculate-Inst-Price` (@ `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl`) -> Impact: **283.6** | LOC: 73
- `2120-Calculate-Inst-Price` (@ `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl`) -> Impact: **283.6** | LOC: 73
- `2120-Calculate-Inst-Price` (@ `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl`) -> Impact: **283.6** | LOC: 73
- `2120-Calculate-Inst-Price` (@ `OpenCobol/ECBAP/cbl/ws81c.cbl`) -> Impact: **283.6** | LOC: 73
- `2120-Calculate-Inst-Price` (@ `OpenCobol/ECBAP/cbl/ws81d.cbl`) -> Impact: **283.6** | LOC: 73
- `2120-Calculate-Inst-Price` (@ `OpenCobol/ECBAP/cbl/ws81e.cbl`) -> Impact: **283.6** | LOC: 73
- `2900-Display-The-Tables` (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> Impact: **201.5** | LOC: 190
  * *Intent:* * Find EVERYBODY who's studied BIOL ogy
- `2900-Display-The-Tables` (@ `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl`) -> Impact: **201.5** | LOC: 190
  * *Intent:* * Find EVERYBODY who's studied BIOL ogy * Use a REF-MOD to filter out all the classes. * Note the difference between this search and the next....

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `2120-Calculate-Inst-Price` (@ `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl`) -> **O(2^N) [Recursive]**
- `2120-Calculate-Inst-Price` (@ `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl`) -> **O(2^N) [Recursive]**
- `2120-Calculate-Inst-Price` (@ `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl`) -> **O(2^N) [Recursive]**
- `2120-Calculate-Inst-Price` (@ `OpenCobol/ECBAP/cbl/ws81c.cbl`) -> **O(2^N) [Recursive]**
- `2120-Calculate-Inst-Price` (@ `OpenCobol/ECBAP/cbl/ws81d.cbl`) -> **O(2^N) [Recursive]**
- `2120-Calculate-Inst-Price` (@ `OpenCobol/ECBAP/cbl/ws81e.cbl`) -> **O(2^N) [Recursive]**
- `2000-Process` (@ `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl`) -> **O(2^N) [Recursive]**
- `WS-Company-Counter` (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> **O(2^N) [Recursive]**
- `WS-Company-Total` (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> **O(2^N) [Recursive]**
- `WS-Company-Total` (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> **O(2^N) [Recursive]**
  * *Intent:* * Let's move on to a 2D table and do some reporting. * This is the Student-Course-Grade table. * Print a line showing the student name, then follow th...

### Highest Data Gravity (Database Complexity)
- `200-CLEANUP` (@ `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl`) -> DB Complexity: **72**
- `100-MAINLINE` (@ `OpenCobol/dastagg/cbl/HOSPEDIT.cbl`) -> DB Complexity: **44**
- `2000-Process` (@ `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl`) -> DB Complexity: **32**
- `100-MAINLINE` (@ `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl`) -> DB Complexity: **32**
- `WCM-A-HOURLY-WAGE` (@ `pgm_templates/CICS/basecics.cbl`) -> DB Complexity: **32**
- `2910-Print-Detail-Line` (@ `Mainframe/ZOS/ECBAP/cbl/WS182.cbl`) -> DB Complexity: **27**
- `2910-Print-Detail-Line` (@ `OpenCobol/ECBAP/cbl/ws182.cbl`) -> DB Complexity: **27**
- `PRINT-LINE` (@ `Mainframe/ZOS/Normal/cbl/ODS0001.cbl`) -> DB Complexity: **25**
- `6010-WRITE-HEADERS` (@ `Mainframe/ZOS/Normal/cbl/ODS0106.cbl`) -> DB Complexity: **25**
- `OBJECT-COMPUTER` (@ `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl`) -> DB Complexity: **25**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `OpenCobol/ECBAP/cbl` | 59 | 8942.12 | 31.79% | 47.1% |
| `Mainframe/ZOS/ECBAP/cbl` | 25 | 7908.06 | 41.19% | 64.84% |
| `Mainframe/MVS/herc01/jcl` | 2 | 6491.01 | 4.99% | 0.0% |
| `OpenCobol/dastagg/cbl` | 28 | 1503.16 | 33.81% | 43.86% |
| `Mainframe/ZOS/Normal/cbl` | 16 | 1114.16 | 44.88% | 79.49% |
| `Mainframe/ZOS/Normal/jcl` | 9 | 539.36 | 32.99% | 0.0% |
| `OpenCobol/prod/cbl` | 11 | 487.9 | 44.2% | 90.66% |
| `Mainframe/ZOS/Internal-Sort/cbl` | 5 | 453.04 | 23.87% | 99.97% |
| `OpenCobol/Internal-Sort/cbl` | 5 | 453.04 | 23.87% | 99.97% |
| `OpenCobol/ECBAP/jcl` | 37 | 422.72 | 5.65% | 99.99% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Mainframe/MVS/Utilities/scripts/submit.sh` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/hybrid-method/allocate.sh` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Initialize/SCRIPTS/allocate.sh` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Initialize/SCRIPTS/cleanup.sh` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/cleanup.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/hybrid-method/allocate.sh` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Initialize/SCRIPTS/cleanup.sh` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/cleanup.sh` -> **100.0%** Exposure
- `OpenCobol/ECBAP/jcl/CHARFUNC.sh` -> **100.0%** Exposure
- `OpenCobol/ECBAP/jcl/HOSPEDIT.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` -> **27** Orphaned Functions | **0** Duplicates
- `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` -> **27** Orphaned Functions | **0** Duplicates
- `OpenCobol/ECBAP/cbl/ws162e.cbl` -> **27** Orphaned Functions | **0** Duplicates
- `OpenCobol/ECBAP/cbl/ws81e.cbl` -> **27** Orphaned Functions | **0** Duplicates
- `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` -> **26** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Mainframe/MVS/herc01/jcl/VSIOINST.JCL`** -> AI Confidence: **99.29%**
2. **`Mainframe/ZOS/Zowe/Initialize/SCRIPTS/cleanup.sh`** -> AI Confidence: **99.29%**
3. **`Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/cleanup.sh`** -> AI Confidence: **99.29%**
4. **`OpenCobol/ECBAP/jcl/CHARFUNC.sh`** -> AI Confidence: **99.29%**
5. **`OpenCobol/ECBAP/jcl/FAHR2CEL.sh`** -> AI Confidence: **99.29%**
6. **`OpenCobol/ECBAP/jcl/FAVRPT.sh`** -> AI Confidence: **99.29%**
7. **`OpenCobol/ECBAP/jcl/FILECALC.sh`** -> AI Confidence: **99.29%**
8. **`OpenCobol/ECBAP/jcl/HOSPEDIT.sh`** -> AI Confidence: **99.29%**
9. **`OpenCobol/ECBAP/jcl/INSPECT1.sh`** -> AI Confidence: **99.29%**
10. **`OpenCobol/ECBAP/jcl/INTEG1.sh`** -> AI Confidence: **99.29%**
11. **`OpenCobol/ECBAP/jcl/INTRDATE.sh`** -> AI Confidence: **99.29%**
12. **`OpenCobol/ECBAP/jcl/INTRFINA.sh`** -> AI Confidence: **99.29%**
13. **`OpenCobol/ECBAP/jcl/INTRNUM.sh`** -> AI Confidence: **99.29%**
14. **`OpenCobol/ECBAP/jcl/INTRSTAT.sh`** -> AI Confidence: **99.29%**
15. **`OpenCobol/ECBAP/jcl/PAYROL01.sh`** -> AI Confidence: **99.29%**
16. **`OpenCobol/ECBAP/jcl/PAYROL0B.sh`** -> AI Confidence: **99.29%**
17. **`OpenCobol/ECBAP/jcl/STRING1.sh`** -> AI Confidence: **99.29%**
18. **`OpenCobol/ECBAP/jcl/STRING2.sh`** -> AI Confidence: **99.29%**
19. **`OpenCobol/ECBAP/jcl/TABLE1.sh`** -> AI Confidence: **99.29%**
20. **`OpenCobol/ECBAP/jcl/TABLES01.sh`** -> AI Confidence: **99.29%**
21. **`OpenCobol/ECBAP/jcl/TABLOAD1.sh`** -> AI Confidence: **99.29%**
22. **`OpenCobol/ECBAP/jcl/TABLOAD2.sh`** -> AI Confidence: **99.29%**
23. **`OpenCobol/ECBAP/jcl/TRIM1.sh`** -> AI Confidence: **99.29%**
24. **`OpenCobol/ECBAP/jcl/UNSTRNG.sh`** -> AI Confidence: **99.29%**
25. **`OpenCobol/ECBAP/jcl/WS120.sh`** -> AI Confidence: **99.29%**
26. **`OpenCobol/ECBAP/jcl/WS162E.sh`** -> AI Confidence: **99.29%**
27. **`OpenCobol/ECBAP/jcl/WS172A.sh`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Mainframe/MVS/Utilities/jcl/allocate.jcl` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/create-vsam/qsam.jcl` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/create-vsam/vsam.jcl` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/hybrid-method/allocate.jcl` -> **100.0%** Exposure
- `Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Mainframe/MVS/Utilities/jcl/allocate.jcl` -> **100.0%** Exposure
- `Mainframe/MVS/herc01/jcl/VSTEST01.JCL` -> **100.0%** Exposure
- `Mainframe/MVS/herc03/jcl/cbl0001j.jcl` -> **100.0%** Exposure
- `Mainframe/ZOS/Normal/jcl/BDS0702.jcl` -> **100.0%** Exposure
- `Mainframe/ZOS/Normal/jcl/BDS0704.jcl` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `OpenCobol/ECBAP/cbl/ws81c.cbl` -> **75.3102%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` -> **73.5779%** Exposure
- `OpenCobol/ECBAP/cbl/ws81d.cbl` -> **61.0229%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` -> **59.2107%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` -> **49.6269%** Exposure
### Algorithmic DoS Exposure
- `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` -> **100.0%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/TABLE2.cbl` -> **100.0%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/TABLE2A.cbl` -> **100.0%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl` -> **100.0%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `108` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `OpenCobol/dastagg/cbl/BDS1005.cbl` (COBOL) -> Cumulative Risk: **764.73**
- **Archetype:** `file_cluster_8` (Distance: 11.792 IQR)
- **Magnitude:** 213.1 | **LOC:** 223 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Documentation (99.996%), Injection Surface (99.6423%)
- **Heaviest Functions:** `Begin` (Impact: 39.8), `ProcessOneTransaction` (Impact: 28.4), `ApplySubtractFromStock` (Impact: 18.1)

### 2. `OpenCobol/ECBAP/cbl/ws81c.cbl` (COBOL) -> Cumulative Risk: **751.43**
- **Archetype:** `file_cluster_8` (Distance: 11.69 IQR)
- **Magnitude:** 604.62 | **LOC:** 523 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9959%), Documentation (97.612%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 283.6), `5100-Read-RFPIN` (Impact: 40.8), `2130-Calculate-Shipping` (Impact: 36.6)

### 3. `OpenCobol/ECBAP/cbl/ws81d.cbl` (COBOL) -> Cumulative Risk: **748.8**
- **Archetype:** `file_cluster_8` (Distance: 12.443 IQR)
- **Magnitude:** 736.0 | **LOC:** 627 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9987%), Documentation (99.3692%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 283.6), `5100-Read-RFPIN` (Impact: 40.8), `2130-Calculate-Shipping` (Impact: 36.6)

### 4. `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` (COBOL) -> Cumulative Risk: **745.71**
- **Archetype:** `file_cluster_8` (Distance: 11.635 IQR)
- **Magnitude:** 604.84 | **LOC:** 508 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9945%), Documentation (97.5309%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 283.6), `5100-Read-RFPIN` (Impact: 40.8), `2130-Calculate-Shipping` (Impact: 36.6)

### 5. `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` (COBOL) -> Cumulative Risk: **743.62**
- **Archetype:** `file_cluster_8` (Distance: 12.384 IQR)
- **Magnitude:** 736.26 | **LOC:** 626 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9982%), Documentation (99.2882%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 283.6), `5100-Read-RFPIN` (Impact: 40.8), `2130-Calculate-Shipping` (Impact: 36.6)

### 6. `pgm_templates/CICS/basecics.cbl` (COBOL) -> Cumulative Risk: **737.73**
- **Archetype:** `file_cluster_8` (Distance: 13.024 IQR)
- **Magnitude:** 362.52 | **LOC:** 336 | **CtrlFlow:** 88.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8801%)
- **Heaviest Functions:** `WCM-A-HOURLY-WAGE` (Impact: 129.2), `0000-MAINLINE` (Impact: 33.3), `1000-RECIEVE-MAP` (Impact: 18.9)

### 7. `Mainframe/ZOS/Zowe/Simple_Report/COBOL/prtrpt1.cbl` (COBOL) -> Cumulative Risk: **729.34**
- **Archetype:** `file_cluster_8` (Distance: 11.957 IQR)
- **Magnitude:** 126.16 | **LOC:** 166 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9978%), Algorithmic Dos (99.9189%), Tech Debt (99.8147%)
- **Heaviest Functions:** `5000-Read-Member-File` (Impact: 18.1), `1010-Open-Report` (Impact: 15.5), `1020-Open-Member-File` (Impact: 15.5)

### 8. `OpenCobol/ECBAP/cbl/ws81e.cbl` (COBOL) -> Cumulative Risk: **726.49**
- **Archetype:** `file_cluster_8` (Distance: 12.295 IQR)
- **Magnitude:** 773.0 | **LOC:** 702 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9978%), Documentation (99.0452%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 283.6), `5100-Read-RFPIN` (Impact: 40.8), `2130-Calculate-Shipping` (Impact: 36.6)

### 9. `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` (COBOL) -> Cumulative Risk: **726.46**
- **Archetype:** `file_cluster_8` (Distance: 12.294 IQR)
- **Magnitude:** 773.0 | **LOC:** 710 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9978%), Documentation (99.0207%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 283.6), `5100-Read-RFPIN` (Impact: 40.8), `2130-Calculate-Shipping` (Impact: 36.6)

### 10. `Mainframe/ZOS/Normal/cbl/BDS0801.cbl` (COBOL) -> Cumulative Risk: **723.97**
- **Archetype:** `file_cluster_8` (Distance: 11.373 IQR)
- **Magnitude:** 61.66 | **LOC:** 82 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (99.9986%), State Flux (99.9965%), Documentation (99.9923%)
- **Heaviest Functions:** `1000-BOJ` (Impact: 10.5), `5010-Summarize-Country-Sales` (Impact: 10.5), `0000-Mainline` (Impact: 6.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Mainframe/MVS/herc01/jcl/VSIOINST.JCL` (JCL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.328 IQR)
- **Top Global Matches:** file_cluster_8: 9.328, file_cluster_7: 10.224, file_cluster_1: 10.395
- **Magnitude:** 6458.47 | **LOC:** 3958 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.6444%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 14`, `args: 1`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`
* *Architecture:* `io: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SYS2.VSAMIO.SOURCE(VSAMIOS), SYS2.VSAMIO.OBJECT(VSAMIO), SYS2.VSAMIO.SOURCE, SYS1.MACLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.618 IQR)
- **Top Global Matches:** file_cluster_8: 11.618, file_cluster_0: 12.049, file_cluster_13: 12.084
- **Magnitude:** 1143.14 | **LOC:** 639 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (68.2981%), Tech Debt (30.1678%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 915.4 | O(2^N) | DB: 32)
  * `1099-Verify-Type-Table` (Impact: 35.8 | O(2^N) | DB: 1)
  * `1015-Load-Type` (Impact: 21.1 | O(N^4) | DB: 18)
  * `1010-Load-Type-Table` (Impact: 6.3 | O(N^2) | DB: 11)
  * `0000-Mainline` (Impact: 6.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 159`, `args: 4`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 115`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 8`, `api: 24`, `import: 1`
* *Defense:* `safety: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tablena.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.56 IQR)
- **Top Global Matches:** file_cluster_8: 11.56, file_cluster_7: 12.172, file_cluster_0: 12.228
- **Magnitude:** 1019.24 | **LOC:** 1244 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (57.6449%), Tech Debt (73.0205%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 201.5 | O(N^2) | DB: 8)
  * `2200-Do-Some-Searching` (Impact: 180.8 | O(N^6) | DB: 17)
  * `WS-Company-Counter` (Impact: 86.0 | O(2^N) | DB: 13)
  * `WS-Company-Total` (Impact: 79.5 | O(2^N) | DB: 6)
  * `WS-Show-Number` (Impact: 75.6 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 241`, `args: 13`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 208`, `duplicate_logic: 10`, `orphaned_logic: 10`
* *Architecture:* `api: 14`
* *Defense:* `safety: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.577 IQR)
- **Top Global Matches:** file_cluster_8: 11.577, file_cluster_7: 12.188, file_cluster_0: 12.241
- **Magnitude:** 994.06 | **LOC:** 1235 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (58.3504%), Tech Debt (73.6191%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 201.5 | O(N^2) | DB: 8)
    * *Intent:* * Find EVERYBODY who's studied BIOL ogy
  * `2200-Do-Some-Searching` (Impact: 155.9 | O(N^5) | DB: 17)
  * `WS-Company-Counter` (Impact: 86.0 | O(2^N) | DB: 13)
  * `WS-Company-Total` (Impact: 79.5 | O(2^N) | DB: 6)
  * `WS-Show-Number` (Impact: 75.6 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 240`, `args: 13`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 208`, `duplicate_logic: 10`, `orphaned_logic: 10`
* *Architecture:* `api: 14`
* *Defense:* `safety: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tablewa.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.149 IQR)
- **Top Global Matches:** file_cluster_8: 11.149, file_cluster_7: 11.791, file_cluster_0: 11.88
- **Magnitude:** 828.56 | **LOC:** 1198 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (39.8411%), Tech Debt (73.7316%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 201.5 | O(N^2) | DB: 8)
  * `2200-Do-Some-Searching` (Impact: 180.8 | O(N^6) | DB: 17)
  * `WS-Company-Total` (Impact: 56.3 | O(N^6) | DB: 6)
    * *Intent:* * On to 3D tables. This is "Company Data". * It breaks down into: * Division: * Region:...
  * `WS-Company-Total` (Impact: 55.5 | O(2^N) | DB: 6)
  * `WS-Company-Total` (Impact: 55.5 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 228`, `args: 16`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 145`, `duplicate_logic: 10`, `orphaned_logic: 9`
* *Architecture:* `api: 14`
* *Defense:* `safety: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.166 IQR)
- **Top Global Matches:** file_cluster_8: 11.166, file_cluster_7: 11.807, file_cluster_0: 11.893
- **Magnitude:** 803.38 | **LOC:** 1189 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (40.4069%), Tech Debt (74.3494%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 201.5 | O(N^2) | DB: 8)
    * *Intent:* * Find EVERYBODY who's studied BIOL ogy * Use a REF-MOD to filter out all the classes. * Note the di...
  * `2200-Do-Some-Searching` (Impact: 155.9 | O(N^5) | DB: 17)
  * `WS-Company-Total` (Impact: 56.3 | O(N^6) | DB: 6)
    * *Intent:* * On to 3D tables. This is "Company Data". * It breaks down into: * Division: * Region:...
  * `WS-Company-Total` (Impact: 55.5 | O(2^N) | DB: 6)
  * `WS-Company-Total` (Impact: 55.5 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 228`, `args: 16`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 145`, `duplicate_logic: 10`, `orphaned_logic: 9`
* *Architecture:* `api: 14`
* *Defense:* `safety: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.294 IQR)
- **Top Global Matches:** file_cluster_8: 12.294, file_cluster_17: 12.736, file_cluster_0: 12.755
- **Magnitude:** 773.0 | **LOC:** 710 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (65.5919%), Tech Debt (88.6598%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 283.6 | O(2^N) | DB: 18)
  * `5100-Read-RFPIN` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2130-Calculate-Shipping` (Impact: 36.6 | O(2^N) | DB: 2)
  * `2100-Create-RFP` (Impact: 31.5 | O(N^4) | DB: 18)
  * `2110-Move-Fixed-Fields` (Impact: 16.2 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 49`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 199`, `dead_code: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 41`
* *Defense:* `safety: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81e.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.295 IQR)
- **Top Global Matches:** file_cluster_8: 12.295, file_cluster_17: 12.734, file_cluster_0: 12.748
- **Magnitude:** 773.0 | **LOC:** 702 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (65.5919%), Tech Debt (88.6598%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 283.6 | O(2^N) | DB: 18)
  * `5100-Read-RFPIN` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2130-Calculate-Shipping` (Impact: 36.6 | O(2^N) | DB: 2)
  * `2100-Create-RFP` (Impact: 31.5 | O(N^4) | DB: 18)
  * `2110-Move-Fixed-Fields` (Impact: 16.2 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 49`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 199`, `dead_code: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 41`
* *Defense:* `safety: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.384 IQR)
- **Top Global Matches:** file_cluster_8: 12.384, file_cluster_17: 12.797, file_cluster_0: 12.82
- **Magnitude:** 736.26 | **LOC:** 626 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (69.1784%), Tech Debt (92.5423%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 283.6 | O(2^N) | DB: 18)
  * `5100-Read-RFPIN` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2130-Calculate-Shipping` (Impact: 36.6 | O(2^N) | DB: 2)
  * `2100-Create-RFP` (Impact: 28.8 | O(N^4) | DB: 13)
  * `2110-Move-Fixed-Fields` (Impact: 16.2 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 44`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 177`, `dead_code: 1`, `orphaned_logic: 26`
* *Architecture:* `io: 31`
* *Defense:* `safety: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81d.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.443 IQR)
- **Top Global Matches:** file_cluster_8: 12.443, file_cluster_17: 12.839, file_cluster_0: 12.861
- **Magnitude:** 736.0 | **LOC:** 627 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (71.1337%), Tech Debt (93.3486%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 283.6 | O(2^N) | DB: 18)
  * `5100-Read-RFPIN` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2130-Calculate-Shipping` (Impact: 36.6 | O(2^N) | DB: 2)
  * `2100-Create-RFP` (Impact: 28.8 | O(N^4) | DB: 13)
  * `2110-Move-Fixed-Fields` (Impact: 16.2 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 44`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 177`, `dead_code: 1`, `orphaned_logic: 26`
* *Architecture:* `io: 31`
* *Defense:* `safety: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.072 IQR)
- **Top Global Matches:** file_cluster_8: 11.072, file_cluster_13: 11.643, file_cluster_0: 11.658
- **Magnitude:** 633.48 | **LOC:** 449 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (54.2444%), Tech Debt (48.5163%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 467.5 | O(2^N) | DB: 14)
  * `1099-Verify-Type-Table` (Impact: 35.7 | O(2^N) | DB: 1)
  * `1015-Load-Type` (Impact: 21.1 | O(N^4) | DB: 17)
  * `1010-Load-Type-Table` (Impact: 6.3 | O(N^2) | DB: 7)
  * `0000-Mainline` (Impact: 6.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 117`, `args: 4`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 67`, `orphaned_logic: 8`
* *Architecture:* `io: 7`, `api: 14`, `import: 1`
* *Defense:* `safety: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.635 IQR)
- **Top Global Matches:** file_cluster_8: 11.635, file_cluster_0: 12.164, file_cluster_17: 12.168
- **Magnitude:** 604.84 | **LOC:** 508 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (63.4732%), Tech Debt (85.8937%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 283.6 | O(2^N) | DB: 18)
  * `5100-Read-RFPIN` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2130-Calculate-Shipping` (Impact: 36.6 | O(2^N) | DB: 2)
  * `2100-Create-RFP` (Impact: 16.9 | O(N^3) | DB: 15)
  * `2110-Move-Fixed-Fields` (Impact: 16.2 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 26`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 133`, `dead_code: 1`, `orphaned_logic: 18`
* *Architecture:* `io: 33`
* *Defense:* `safety: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81c.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.69 IQR)
- **Top Global Matches:** file_cluster_8: 11.69, file_cluster_0: 12.199, file_cluster_17: 12.204
- **Magnitude:** 604.62 | **LOC:** 523 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (65.5251%), Tech Debt (87.1595%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 283.6 | O(2^N) | DB: 18)
  * `5100-Read-RFPIN` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2130-Calculate-Shipping` (Impact: 36.6 | O(2^N) | DB: 2)
  * `2100-Create-RFP` (Impact: 16.9 | O(N^3) | DB: 15)
  * `2110-Move-Fixed-Fields` (Impact: 16.2 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 26`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 133`, `dead_code: 1`, `orphaned_logic: 18`
* *Architecture:* `io: 33`
* *Defense:* `safety: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.111 IQR)
- **Top Global Matches:** file_cluster_8: 12.111, file_cluster_13: 12.45, file_cluster_17: 12.642
- **Magnitude:** 529.08 | **LOC:** 696 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (60.1754%), Tech Debt (99.4553%)
**Top Internal Functions/Classes:**
  * `1015-Load-Type` (Impact: 41.1 | O(2^N) | DB: 15)
  * `5000-Read-INFILE` (Impact: 40.8 | O(2^N) | DB: 17)
  * `6135-Display-Ins-Type-Messages` (Impact: 37.1 | O(N^5) | DB: 11)
  * `2100-Process-INFile-Records` (Impact: 31.1 | O(N^4) | DB: 15)
  * `WS-OutFile-Patient-NAME` (Impact: 19.3 | O(N^4) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 49`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 194`, `fragile_debt: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 51`, `import: 8`
* *Defense:* `safety: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSFST, WSDT, PATIENT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws162e.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.114 IQR)
- **Top Global Matches:** file_cluster_8: 12.114, file_cluster_13: 12.445, file_cluster_17: 12.64
- **Magnitude:** 529.08 | **LOC:** 696 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (60.1754%), Tech Debt (99.4553%)
**Top Internal Functions/Classes:**
  * `1015-Load-Type` (Impact: 41.1 | O(2^N) | DB: 15)
  * `5000-Read-INFILE` (Impact: 40.8 | O(2^N) | DB: 17)
  * `6135-Display-Ins-Type-Messages` (Impact: 37.1 | O(N^5) | DB: 11)
  * `2100-Process-INFile-Records` (Impact: 31.1 | O(N^4) | DB: 15)
  * `WS-OutFile-Patient-NAME` (Impact: 19.3 | O(N^4) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 49`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 194`, `fragile_debt: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 51`, `import: 8`
* *Defense:* `safety: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSFST, WSDT, PATIENT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pgm_templates/CICS/basecics.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.024 IQR)
- **Top Global Matches:** file_cluster_8: 13.024, file_cluster_17: 13.131, file_cluster_11: 13.248
- **Magnitude:** 362.52 | **LOC:** 336 | **CtrlFlow:** 88.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (97.4017%), Tech Debt (98.1551%)
**Top Internal Functions/Classes:**
  * `WCM-A-HOURLY-WAGE` (Impact: 129.2 | O(2^N) | DB: 32)
  * `0000-MAINLINE` (Impact: 33.3 | O(N^4))
    * *Intent:* *COPY MANUALLY CODED MAP HERE. *COPY DFHEIBLK COPY BOOK HERE. *COPY ATTRIBUTES COPY BOOK HERE.
  * `1000-RECIEVE-MAP` (Impact: 18.9 | O(N^5) | DB: 2)
  * `5500-COMPUTE-RESULTS` (Impact: 18.8 | O(N^5) | DB: 4)
  * `0500-NORMAL-PROCESSING` (Impact: 12.5 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 7`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`, `dead_code: 2`, `orphaned_logic: 15`
* *Architecture:* `api: 1`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws172a.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.852 IQR)
- **Top Global Matches:** file_cluster_8: 11.852, file_cluster_13: 12.224, file_cluster_17: 12.394
- **Magnitude:** 349.48 | **LOC:** 416 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (68.2224%), Tech Debt (94.7024%)
**Top Internal Functions/Classes:**
  * `R1-Student-Name` (Impact: 49.7 | O(N^5) | DB: 21)
  * `5000-Read-STCOURS` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2120-Calculate-Grades` (Impact: 32.9 | O(N^6) | DB: 9)
  * `2110-Print-Stdt-Total-Report` (Impact: 18.6 | O(N^4) | DB: 15)
  * `6100-Write-R1` (Impact: 14.3 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 26`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 124`, `orphaned_logic: 17`
* *Architecture:* `io: 39`, `import: 4`
* *Defense:* `safety: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST, WSDT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS172A.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.855 IQR)
- **Top Global Matches:** file_cluster_8: 11.855, file_cluster_13: 12.232, file_cluster_17: 12.4
- **Magnitude:** 349.46 | **LOC:** 416 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (68.4633%), Tech Debt (94.7817%)
**Top Internal Functions/Classes:**
  * `R1-Student-Name` (Impact: 49.7 | O(N^5) | DB: 21)
  * `5000-Read-STCOURS` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2120-Calculate-Grades` (Impact: 32.9 | O(N^6) | DB: 9)
  * `2110-Print-Stdt-Total-Report` (Impact: 18.6 | O(N^4) | DB: 15)
  * `6100-Write-R1` (Impact: 14.3 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 26`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 124`, `orphaned_logic: 17`
* *Architecture:* `io: 39`, `import: 4`
* *Defense:* `safety: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST, WSDT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws162o.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.552 IQR)
- **Top Global Matches:** file_cluster_8: 11.552, file_cluster_13: 11.845, file_cluster_17: 12.109
- **Magnitude:** 337.52 | **LOC:** 483 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (33.0246%), Tech Debt (93.1734%)
**Top Internal Functions/Classes:**
  * `1015-Load-Type` (Impact: 41.0 | O(2^N) | DB: 14)
  * `5100-Read-INFILE` (Impact: 40.8 | O(2^N) | DB: 17)
  * `1099-Verify-Type-Table` (Impact: 35.7 | O(2^N) | DB: 1)
  * `2100-Process-INFile-Records` (Impact: 31.1 | O(N^4) | DB: 13)
  * `FD-OutFile-Patient-Record` (Impact: 16.6 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 42`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`, `orphaned_logic: 19`
* *Architecture:* `io: 46`, `import: 9`
* *Defense:* `safety: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSFST, WSDT, PATIENT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS120.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.996 IQR)
- **Top Global Matches:** file_cluster_8: 11.996, file_cluster_13: 12.357, file_cluster_17: 12.52
- **Magnitude:** 307.1 | **LOC:** 387 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (65.2456%), Tech Debt (93.3965%)
**Top Internal Functions/Classes:**
  * `5100-Read-INSClaim` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2112-Check-Deductible` (Impact: 38.0 | O(N^5) | DB: 15)
  * `2120-Move-Fixed-Fields` (Impact: 15.8 | O(N^4) | DB: 10)
  * `2100-Process-Claims` (Impact: 14.6 | O(N^3) | DB: 8)
  * `6100-Write-R1` (Impact: 14.3 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 16`
* *Architecture:* `io: 33`, `import: 4`
* *Defense:* `safety: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST, CLAIMREC, WSDT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS193.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.996 IQR)
- **Top Global Matches:** file_cluster_8: 11.996, file_cluster_13: 12.357, file_cluster_17: 12.52
- **Magnitude:** 307.1 | **LOC:** 387 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (65.2456%), Tech Debt (93.3965%)
**Top Internal Functions/Classes:**
  * `5100-Read-INSClaim` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2112-Check-Deductible` (Impact: 38.0 | O(N^5) | DB: 15)
  * `2120-Move-Fixed-Fields` (Impact: 15.8 | O(N^4) | DB: 10)
  * `2100-Process-Claims` (Impact: 14.6 | O(N^3) | DB: 8)
  * `6100-Write-R1` (Impact: 14.3 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 16`
* *Architecture:* `io: 33`, `import: 4`
* *Defense:* `safety: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST, CLAIMREC, WSDT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws120.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.997 IQR)
- **Top Global Matches:** file_cluster_8: 11.997, file_cluster_13: 12.355, file_cluster_17: 12.519
- **Magnitude:** 307.1 | **LOC:** 387 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (65.2456%), Tech Debt (93.3965%)
**Top Internal Functions/Classes:**
  * `5100-Read-INSClaim` (Impact: 40.8 | O(2^N) | DB: 17)
  * `2112-Check-Deductible` (Impact: 38.0 | O(N^5) | DB: 15)
  * `2120-Move-Fixed-Fields` (Impact: 15.8 | O(N^4) | DB: 10)
  * `2100-Process-Claims` (Impact: 14.6 | O(N^3) | DB: 8)
  * `6100-Write-R1` (Impact: 14.3 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 16`
* *Architecture:* `io: 33`, `import: 4`
* *Defense:* `safety: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST, CLAIMREC, WSDT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLE2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.802 IQR)
- **Top Global Matches:** file_cluster_8: 10.802, file_cluster_7: 11.462, file_cluster_0: 11.483
- **Magnitude:** 299.7 | **LOC:** 543 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (44.8889%), Tech Debt (64.3339%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 128.0 | O(N^6) | DB: 20)
  * `WS-Company-Total` (Impact: 32.9 | O(N^6) | DB: 2)
    * *Intent:* * Okay, Calculating is fine. * Now, can we calculate and print subtotals in one go.
  * `WS-Company-Total` (Impact: 32.6 | O(N^6) | DB: 4)
  * `0000-Mainline` (Impact: 6.2 | O(N^2))
  * `WS-Company-Total` (Impact: 3.5 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 68`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 78`, `dead_code: 1`, `duplicate_logic: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 3`
* *Defense:* `safety: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tabldna.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.266 IQR)
- **Top Global Matches:** file_cluster_8: 11.266, file_cluster_13: 11.756, file_cluster_0: 11.884
- **Magnitude:** 284.2 | **LOC:** 366 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (49.6429%), Tech Debt (93.0169%)
**Top Internal Functions/Classes:**
  * `2200-Do-Some-Searching` (Impact: 49.9 | O(N^5) | DB: 2)
  * `1019-Verify-Emp-Table` (Impact: 35.7 | O(2^N) | DB: 1)
  * `1119-Verify-Student-Table` (Impact: 35.7 | O(2^N) | DB: 1)
  * `1013-Load-Employees` (Impact: 23.4 | O(N^4) | DB: 13)
  * `1113-Load-Students` (Impact: 23.4 | O(N^4) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 41`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `orphaned_logic: 13`
* *Architecture:* `io: 10`, `import: 2`
* *Defense:* `safety: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.962 IQR)
- **Top Global Matches:** file_cluster_8: 10.962, file_cluster_7: 11.475, file_cluster_0: 11.551
- **Magnitude:** 257.96 | **LOC:** 488 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (69.0365%), Tech Debt (82.8923%)
**Top Internal Functions/Classes:**
  * `100-MAINLINE` (Impact: 65.3 | O(N^5) | DB: 32)
  * `OBJECT-COMPUTER` (Impact: 23.0 | O(N^4) | DB: 25)
  * `WS-OUTPUT-REC` (Impact: 10.7 | O(N^3) | DB: 19)
    * *Intent:* * DISPLAY "HOUSEKEEPING".
  * `INS-TYPE-O` (Impact: 4.5 | O(N^3) | DB: 9)
  * `200-CLEANUP` (Impact: 2.5 | O(N^2) | DB: 72)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 25`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 125`, `dead_code: 1`, `orphaned_logic: 16`
* *Architecture:* `io: 40`
* *Defense:* `safety: 8`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `OpenCobol/ECBAP/jcl/MAINPGM.sh` (SHELL) | Magnitude: 14.34 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: safety_bypasses: 19, indent_spaces: 13, state_mutation: 5, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Mainframe/ZOS/Zowe/Initialize/SCRIPTS/cleanup.sh` (SHELL) | Magnitude: 2.1 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 12, reflection_metaprogramming: 12, concurrency: 6, branch: 1
- `Mainframe/ZOS/ECBAP/scripts/upload_data.sh` (SHELL) | Magnitude: 1.35 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 84, thread_sleeps: 14, time_date_logic: 14, concurrency: 6
- `Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/cleanup.sh` (SHELL) | Magnitude: 2.12 | Delta: **0.253 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: reflection_metaprogramming: 15, state_mutation: 12, concurrency: 6, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `OpenCobol/ECBAP/cbl/FAHR2CEL.cbl` (COBOL) | Magnitude: 39.64 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 24, structural_boundaries: 9, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Mainframe/ZOS/Zowe/Initialize/SCRIPTS/allocate.sh` (SHELL) | Magnitude: 0.85 | Delta: **0.254 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 6, structural_boundaries: 1, state_mutation: 1, reflection_metaprogramming: 1
- `Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/just-run-job.sh` (SHELL) | Magnitude: 0.85 | Delta: **0.254 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 6, structural_boundaries: 1, state_mutation: 1, reflection_metaprogramming: 1
- `Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/run-project.sh` (SHELL) | Magnitude: 1.28 | Delta: **0.297 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: reflection_metaprogramming: 11, concurrency: 6, state_mutation: 4, debug_prints: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/hybrid-method/allocate.sh` (SHELL) | Magnitude: 14.24 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 6, concurrency: 6, reflection_metaprogramming: 6, debug_prints: 2
- `Mainframe/ZOS/Zowe/Simple_Report/COBOL/prtrpt1.cbl` (COBOL) | Magnitude: 126.16 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 41, branch: 29, io: 19
- `OpenCobol/prod/cbl/prtrpt1.cbl` (COBOL) | Magnitude: 126.16 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 41, branch: 29, io: 19
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/zowe-only-method/allocate.sh` (SHELL) | Magnitude: 18.02 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: reflection_metaprogramming: 17, state_mutation: 10, indent_spaces: 7, concurrency: 6
- `pgm_templates/CICS/basecics.cbl` (COBOL) | Magnitude: 362.52 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 251, state_mutation: 112, branch: 55, safety: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `common/cpy/PATIENT.cpy` -> **Severity: 965.427** (Blast Radius: 10.577 * Doc Risk: 91.2761%)
- `Mainframe/ZOS/Zowe/Simple_Report/COPYBOOK/wsfst.cpy` -> **Severity: 484.641** (Blast Radius: 18.174 * Doc Risk: 26.6667%)
- `Mainframe/ZOS/Normal/cbl/BDS1004.cbl` -> **Severity: 297.892** (Blast Radius: 2.979 * Doc Risk: 99.9973%)
- `OpenCobol/dastagg/cbl/BDS1004.cbl` -> **Severity: 297.892** (Blast Radius: 2.979 * Doc Risk: 99.9973%)
- `OpenCobol/prod/cbl/TDSPTA2.cbl` -> **Severity: 297.892** (Blast Radius: 2.979 * Doc Risk: 99.9973%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
