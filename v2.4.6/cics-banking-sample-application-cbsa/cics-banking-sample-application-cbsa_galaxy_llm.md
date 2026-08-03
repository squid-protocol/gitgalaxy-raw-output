# ARCHITECTURAL_BRIEF: cics-banking-sample-application-cbsa
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cics-banking-sample-application-cbsa` |
| **Timestamp** | `2026-08-03T19:28:32.588634+00:00` |
| **Scan Duration** | `1.93s` |
| **Git Branch** | `main` |
| **Git Commit** | `46cbda52051d5cded017d72ad653df68b8ec1b60` |
| **Git Remote** | `https://github.com/cicsdev/cics-banking-sample-application-cbsa.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 292 malicious artifacts.

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
| Total Artifacts | 801 |
| Analyzed Artifacts (Scanned) | 492 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 309 |
| Total LOC | 44156 |
| Volatility Index | 0.026 |
| % Scanned of codebase = | 61.4% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7325 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4095 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.2909 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 31 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JCL | 110 | 3091 | 22.4% |
| JAVA | 81 | 11544 | 16.5% |
| COBOL | 66 | 18395 | 13.4% |
| JSON | 53 | 5224 | 10.8% |
| XML | 47 | 0 | 9.6% |
| CSS | 32 | 1158 | 6.5% |
| JAVASCRIPT | 31 | 3044 | 6.3% |
| MARKDOWN | 28 | 0 | 5.7% |
| PLAINTEXT | 15 | 1 | 3.0% |
| HTML | 13 | 702 | 2.6% |
| YAML | 12 | 618 | 2.4% |
| SHELL | 2 | 224 | 0.4% |
| BATCH | 2 | 155 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.604`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 378 | 76.8% |
| file_cluster_13 | 31 | 6.3% |
| file_cluster_11 | 14 | 2.8% |
| file_cluster_0 | 12 | 2.4% |
| file_cluster_2 | 11 | 2.2% |
| file_cluster_4 | 2 | 0.4% |
| Unknown | 1 | 0.2% |
| file_cluster_9 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 42 | 8.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 309*

**Composition by Extension & Reason:**
- `.jpg`: 123x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 27x Unsupported Format (.undeterminable), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.lked`: 31x Excluded (Unsupported Extension: '.lked')
- `.png`: 30x Excluded (Explicitly Denied Extension: '.png')
- `.si`: 20x Unsupported Format (.si)
- `.map`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.prefs`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.aar`: 10x Excluded (Unsupported Extension: '.aar')
- `.sar`: 10x Excluded (Unsupported Extension: '.sar')
- `.java`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1036 LOC)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.properties`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.baseline`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.9 | 2.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 78.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.2 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 39.0 | 29.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 12.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `etc/install/base/installjcl/CICSTS56.jcl` (Hits: 123)
- `etc/install/base/buildjcl/BATCH.jcl` (Hits: 43)
- `etc/install/base/buildjcl/CICS.jcl` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ABNDINFO.cpy** (`src/base/cobol_copy/ABNDINFO.cpy`) — 26 inbound connections
2. **JsonPropertyNamingStrategy.java** (`src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java`) — 22 inbound connections
3. **SORTCODE.cpy** (`src/base/cobol_copy/SORTCODE.cpy`) — 18 inbound connections
4. **OutputFormatUtils.java** (`src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java`) — 9 inbound connections
5. **ACCDB2.cpy** (`src/base/cobol_copy/ACCDB2.cpy`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Customer.java** (`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java`) — 37 outbound dependencies
2. **WebController.java** (`src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers/WebController.java`) — 36 outbound dependencies
3. **CreditScoreCICS540.java** (`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CreditScoreCICS540.java`) — 29 outbound dependencies
4. **CustomerResource.java** (`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java`) — 24 outbound dependencies
5. **CICSTS56.jcl** (`etc/install/base/installjcl/CICSTS56.jcl`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `IOT010` (@ `src/base/cobol_src/BNKMENU.cbl`) -> Impact: **367.4** | LOC: 489
- `UAD010` (@ `src/base/cobol_src/XFRFUN.cbl`) -> Impact: **353.0** | LOC: 480
- `ED010` (@ `src/base/cobol_src/BNK1CCS.cbl`) -> Impact: **311.6** | LOC: 352
- `find_maven_basedir_[Truncated]` (@ `mvnw`) -> Impact: **258.3** | LOC: 145
  * *Intent:* # traverses directory structure from process work directory to filesystem root # first directory with .mvn subdirectory is considered project base dir...
- `EIBRESP-TOSTRING` (@ `src/base/cobol_copy/RESPSTR.cpy`) -> Impact: **249.8** | LOC: 236
- `CC010` (@ `src/base/cobol_src/CRECUST.cbl`) -> Impact: **246.7** | LOC: 383
- `GCD010` (@ `src/base/cobol_src/BNK1CCA.cbl`) -> Impact: **224.9** | LOC: 159
  * *Intent:* * * Preserve the RESP and RESP2, then set up the * standard ABEND info before getting the applid, * date/time etc. and linking to the Abend Handler * ...
- `A010` (@ `src/base/cobol_src/BNK1DCS.cbl`) -> Impact: **217.3** | LOC: 147
- `ED010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> Impact: **209.8** | LOC: 275
- `RANDOM-SEED` (@ `src/base/cobol_src/BANKDATA.cbl`) -> Impact: **208.1** | LOC: 241

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `RANDOM-SEED` (@ `src/base/cobol_src/BANKDATA.cbl`) -> **O(2^N) [Recursive]**
- `ACCOUNT-TYPES-COUNT` (@ `src/base/cobol_src/BANKDATA.cbl`) -> **O(2^N) [Recursive]**
- `ACCOUNT-INT-RATES-COUNT` (@ `src/base/cobol_src/BANKDATA.cbl`) -> **O(2^N) [Recursive]**
- `TIMESTAMP` (@ `src/base/cobol_src/BANKDATA.cbl`) -> **O(2^N) [Recursive]**
- `A010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> **O(2^N) [Recursive]**
- `CAD010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> **O(2^N) [Recursive]**
- `SM010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> **O(2^N) [Recursive]**
- `RM010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> **O(2^N) [Recursive]**
- `STM010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> **O(2^N) [Recursive]**
- `GCD010` (@ `src/base/cobol_src/BNK1CCA.cbl`) -> **O(2^N) [Recursive]**
  * *Intent:* * * Preserve the RESP and RESP2, then set up the * standard ABEND info before getting the applid, * date/time etc. and linking to the Abend Handler * ...

### Highest Data Gravity (Database Complexity)
- `EIBRESP-TOSTRING` (@ `src/base/cobol_copy/RESPSTR.cpy`) -> DB Complexity: **468**
- `IA010` (@ `src/base/cobol_src/BANKDATA.cbl`) -> DB Complexity: **225**
  * *Intent:* * * If it is a LOAN or a MORTGAGE then it should really have * a negative balance (it doesn't make any sense for these * accounts to have a positive b...
- `IOT010` (@ `src/base/cobol_src/BNKMENU.cbl`) -> DB Complexity: **200**
- `UAD010` (@ `src/base/cobol_src/XFRFUN.cbl`) -> DB Complexity: **156**
- `CC010` (@ `src/base/cobol_src/CRECUST.cbl`) -> DB Complexity: **138**
- `ED010` (@ `src/base/cobol_src/BNK1CCS.cbl`) -> DB Complexity: **125**
- `FNA010` (@ `src/base/cobol_src/CREACC.cbl`) -> DB Complexity: **121**
- `RANDOM-SEED` (@ `src/base/cobol_src/BANKDATA.cbl`) -> DB Complexity: **112**
- `ED010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> DB Complexity: **96**
- `CAD010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> DB Complexity: **92**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/base/cobol_src` | 29 | 21588.4 | 86.75% | 34.16% |
| `src/bank-application-frontend` | 6 | 5031.56 | 2.5% | 16.67% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json` | 19 | 2254.16 | 10.07% | 44.56% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces` | 7 | 1013.18 | 9.13% | 75.44% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2` | 2 | 935.38 | 52.59% | 18.54% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access` | 5 | 856.36 | 29.25% | 59.79% |
| `etc/install/base/buildjcl` | 46 | 653.64 | 4.57% | 0.0% |
| `__monolith__` | 6 | 580.0 | 17.5% | 16.67% |
| `etc/install/base/installjcl` | 25 | 522.02 | 24.41% | 0.0% |
| `etc/install/base/db2jcl` | 32 | 507.54 | 21.33% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/bank-application-frontend/updateWebUI.sh` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/AccountEnquiryForm.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/InqaccJson.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createaccount/CreaccJson.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `etc/install/base/buildjcl/DEFAULT.jcl` -> **100.0%** Exposure
- `mvnw` -> **100.0%** Exposure
- `src/base/cobol_copy/RESPSTR.cpy` -> **100.0%** Exposure
- `src/base/cobol_src/BANKDATA.cbl` -> **100.0%** Exposure
- `src/base/cobol_src/BNK1CAC.cbl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/deleteaccount/DelaccJson.java` -> **39** Orphaned Functions | **2** Duplicates
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/InqaccJson.java` -> **29** Orphaned Functions | **0** Duplicates
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/updateaccount/UpdaccJson.java` -> **25** Orphaned Functions | **4** Duplicates
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createaccount/CreaccJson.java` -> **26** Orphaned Functions | **2** Duplicates
- `src/base/cobol_src/BANKDATA.cbl` -> **26** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/base/cobol_src/BNK1DCS.cbl`** -> AI Confidence: **99.48%**
2. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java`** -> AI Confidence: **99.31%**
3. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/CustomerList.java`** -> AI Confidence: **99.31%**
4. **`src/base/cobol_src/BANKDATA.cbl`** -> AI Confidence: **99.31%**
5. **`src/base/cobol_src/CREACC.cbl`** -> AI Confidence: **99.31%**
6. **`src/base/cobol_src/CRECUST.cbl`** -> AI Confidence: **99.31%**
7. **`src/base/cobol_src/DBCRFUN.cbl`** -> AI Confidence: **99.31%**
8. **`src/base/cobol_src/DELCUS.cbl`** -> AI Confidence: **99.31%**
9. **`src/base/cobol_src/XFRFUN.cbl`** -> AI Confidence: **99.31%**
10. **`src/base/bms_src/BNK1ACC.bms`** -> AI Confidence: **99.29%**
11. **`src/base/bms_src/BNK1CCM.bms`** -> AI Confidence: **99.29%**
12. **`src/base/bms_src/BNK1DAM.bms`** -> AI Confidence: **99.29%**
13. **`src/base/bms_src/BNK1DCM.bms`** -> AI Confidence: **99.29%**
14. **`src/base/bms_src/BNK1MAI.bms`** -> AI Confidence: **99.29%**
15. **`mvnw`** -> AI Confidence: **99.29%**
16. **`src/base/cobol_copy/DELACCZ.cpy`** -> AI Confidence: **99.29%**
17. **`src/base/cobol_copy/INQACCCU.cpy`** -> AI Confidence: **99.29%**
18. **`src/base/cobol_copy/INQACCCZ.cpy`** -> AI Confidence: **99.29%**
19. **`src/base/cobol_copy/RESPSTR.cpy`** -> AI Confidence: **99.29%**
20. **`src/base/cobol_src/INQACCCU.cbl`** -> AI Confidence: **99.25%**
21. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java`** -> AI Confidence: **99.24%**
22. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java`** -> AI Confidence: **99.24%**
23. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/AccountList.java`** -> AI Confidence: **99.24%**
24. **`src/base/cobol_src/BNK1CAC.cbl`** -> AI Confidence: **99.2%**
25. **`src/base/cobol_src/BNK1CRA.cbl`** -> AI Confidence: **99.2%**
26. **`src/base/cobol_src/BNK1UAC.cbl`** -> AI Confidence: **99.2%**
27. **`src/base/cobol_src/BNKMENU.cbl`** -> AI Confidence: **99.2%**
28. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CreditScoreCICS540.java`** -> AI Confidence: **99.18%**
29. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionResource.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `etc/install/base/buildjcl/BATCH.jcl` -> **100.0%** Exposure
- `etc/install/base/buildjcl/CICS.jcl` -> **100.0%** Exposure
- `etc/install/base/db2jcl/DB2BIND.jcl` -> **100.0%** Exposure
- `etc/install/base/installjcl/BANKDATA.jcl` -> **100.0%** Exposure
- `etc/install/base/installjcl/CICSTS56.jcl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `etc/install/base/buildjcl/BATCH.jcl` -> **100.0%** Exposure
- `etc/install/base/buildjcl/CICS.jcl` -> **100.0%** Exposure
- `etc/install/base/db2jcl/BTCHSQL.jcl` -> **100.0%** Exposure
- `etc/install/base/db2jcl/CREDB00.jcl` -> **100.0%** Exposure
- `etc/install/base/db2jcl/CREI101.jcl` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `mvnw` -> **100.0%** Exposure
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **100.0%** Exposure
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CreditScoreCICS540.java` -> **100.0%** Exposure
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/AccountList.java` -> **100.0%** Exposure
- `src/bank-application-frontend/src/App.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `38` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `964` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/base/cobol_src/CRECUST.cbl` (COBOL) -> Cumulative Risk: **805.52**
- **Archetype:** `file_cluster_11` (Distance: 13.949 IQR)
- **Magnitude:** 1122.78 | **LOC:** 1498 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `CC010` (Impact: 246.7), `GLCV010` (Impact: 84.0), `P010` (Impact: 82.5)

### 2. `mvnw` (SHELL) -> Cumulative Risk: **795.27**
- **Archetype:** `file_cluster_4` (Distance: 12.955 IQR)
- **Magnitude:** 547.38 | **LOC:** 312 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `find_maven_basedir_[Truncated]` (Impact: 258.3), `Anonymous_Block` (Impact: 23.8), `Anonymous_Block` (Impact: 12.8)

### 3. `src/base/cobol_src/CRDTAGY4.cbl` (COBOL) -> Cumulative Risk: **776.8**
- **Archetype:** `file_cluster_8` (Distance: 10.64 IQR)
- **Magnitude:** 144.24 | **LOC:** 276 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9975%), State Flux (99.941%)
- **Heaviest Functions:** `A010` (Impact: 75.4), `OBJECT-COMPUTER` (Impact: 7.5), `PTD010` (Impact: 3.5)

### 4. `src/base/cobol_src/CRDTAGY1.cbl` (COBOL) -> Cumulative Risk: **776.79**
- **Archetype:** `file_cluster_8` (Distance: 10.64 IQR)
- **Magnitude:** 144.14 | **LOC:** 274 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9975%), State Flux (99.941%)
- **Heaviest Functions:** `A010` (Impact: 75.3), `OBJECT-COMPUTER` (Impact: 7.5), `PTD010` (Impact: 3.5)

### 5. `src/base/cobol_src/CRDTAGY2.cbl` (COBOL) -> Cumulative Risk: **776.79**
- **Archetype:** `file_cluster_8` (Distance: 10.64 IQR)
- **Magnitude:** 144.14 | **LOC:** 274 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9975%), State Flux (99.941%)
- **Heaviest Functions:** `A010` (Impact: 75.3), `OBJECT-COMPUTER` (Impact: 7.5), `PTD010` (Impact: 3.5)

### 6. `src/base/cobol_src/BNK1UAC.cbl` (COBOL) -> Cumulative Risk: **757.29**
- **Archetype:** `file_cluster_11` (Distance: 14.475 IQR)
- **Magnitude:** 1413.86 | **LOC:** 1409 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `A010` (Impact: 167.2), `SM010` (Impact: 142.5), `VD010` (Impact: 140.4)

### 7. `src/base/cobol_src/CRDTAGY5.cbl` (COBOL) -> Cumulative Risk: **755.84**
- **Archetype:** `file_cluster_8` (Distance: 10.64 IQR)
- **Magnitude:** 144.34 | **LOC:** 276 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9975%), State Flux (99.941%)
- **Heaviest Functions:** `A010` (Impact: 75.5), `OBJECT-COMPUTER` (Impact: 7.5), `PTD010` (Impact: 3.5)

### 8. `src/base/cobol_src/CRDTAGY3.cbl` (COBOL) -> Cumulative Risk: **755.82**
- **Archetype:** `file_cluster_8` (Distance: 10.64 IQR)
- **Magnitude:** 144.14 | **LOC:** 273 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9975%), State Flux (99.941%)
- **Heaviest Functions:** `A010` (Impact: 75.3), `OBJECT-COMPUTER` (Impact: 7.5), `PTD010` (Impact: 3.5)

### 9. `src/base/cobol_src/BNK1DCS.cbl` (COBOL) -> Cumulative Risk: **752.04**
- **Archetype:** `file_cluster_11` (Distance: 14.763 IQR)
- **Magnitude:** 2074.12 | **LOC:** 2057 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `A010` (Impact: 217.3), `SM010` (Impact: 163.9), `UPDCD010` (Impact: 105.0)

### 10. `src/base/cobol_src/BNK1CCS.cbl` (COBOL) -> Cumulative Risk: **743.77**
- **Archetype:** `file_cluster_11` (Distance: 13.941 IQR)
- **Magnitude:** 1947.78 | **LOC:** 1661 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (97.2294%)
- **Heaviest Functions:** `ED010` (Impact: 311.6), `A010` (Impact: 174.9), `SM010` (Impact: 163.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/bank-application-frontend/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1DCS.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.763 IQR)
- **Top Global Matches:** file_cluster_11: 14.763, file_cluster_0: 14.891, file_cluster_17: 14.919
- **Magnitude:** 2074.12 | **LOC:** 2057 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (96.1451%), Tech Debt (33.9781%)
**Top Internal Functions/Classes:**
  * `A010` (Impact: 217.3 | O(2^N) | DB: 44)
  * `SM010` (Impact: 163.9 | O(2^N) | DB: 75)
  * `UPDCD010` (Impact: 105.0 | O(2^N) | DB: 72)
  * `DCD010` (Impact: 103.5 | O(2^N) | DB: 55)
  * `RM010` (Impact: 97.5 | O(2^N) | DB: 54)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 48`, `args: 1`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 2`, `state_mutation: 915`, `dead_code: 21`, `orphaned_logic: 23`
* *Architecture:* `io: 2`, `api: 1`, `import: 7`
* *Defense:* `safety: 48`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BNK1DCM, DFHBMSCA, DFHAID, DELCUS, INQCUST, ABNDINFO, UPDCUST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CCS.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.941 IQR)
- **Top Global Matches:** file_cluster_11: 13.941, file_cluster_8: 13.959, file_cluster_0: 14.073
- **Magnitude:** 1947.78 | **LOC:** 1661 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 125
- **Risk Profile:** Cognitive Load (97.2294%), Tech Debt (26.5409%)
**Top Internal Functions/Classes:**
  * `ED010` (Impact: 311.6 | O(N^5) | DB: 125)
  * `A010` (Impact: 174.9 | O(2^N) | DB: 43)
  * `SM010` (Impact: 163.9 | O(2^N) | DB: 75)
  * `CCD010` (Impact: 118.0 | O(2^N) | DB: 47)
  * `RM010` (Impact: 98.0 | O(2^N) | DB: 73)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 92`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 866`, `dead_code: 9`, `orphaned_logic: 16`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 40`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DFHAID, BNK1CCM, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1UAC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.475 IQR)
- **Top Global Matches:** file_cluster_11: 14.475, file_cluster_0: 14.581, file_cluster_17: 14.586
- **Magnitude:** 1413.86 | **LOC:** 1409 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (95.5224%), Tech Debt (41.8922%)
**Top Internal Functions/Classes:**
  * `A010` (Impact: 167.2 | O(2^N) | DB: 45)
  * `SM010` (Impact: 142.5 | O(2^N) | DB: 75)
  * `VD010` (Impact: 140.4 | O(N^6) | DB: 74)
    * *Intent:* * * Retrieve the data
  * `IAD010` (Impact: 61.2 | O(2^N) | DB: 58)
  * `WS-CONVERTED-VAL2` (Impact: 43.7 | O(N^6) | DB: 57)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 42`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 674`, `dead_code: 14`, `duplicate_logic: 2`, `orphaned_logic: 15`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 43`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DFHAID, BNK1UAM, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CAC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.899 IQR)
- **Top Global Matches:** file_cluster_11: 13.899, file_cluster_8: 13.957, file_cluster_0: 14.016
- **Magnitude:** 1374.38 | **LOC:** 1302 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 96
- **Risk Profile:** Cognitive Load (96.045%), Tech Debt (26.0696%)
**Top Internal Functions/Classes:**
  * `ED010` (Impact: 209.8 | O(N^6) | DB: 96)
  * `A010` (Impact: 159.8 | O(2^N) | DB: 38)
  * `CAD010` (Impact: 156.0 | O(2^N) | DB: 92)
  * `SM010` (Impact: 142.5 | O(2^N) | DB: 75)
  * `RM010` (Impact: 37.5 | O(2^N) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 54`, `args: 1`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 569`, `dead_code: 10`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `safety: 33`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DFHAID, ABNDINFO, BNK1CAM
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNKMENU.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.671 IQR)
- **Top Global Matches:** file_cluster_8: 13.671, file_cluster_11: 13.692, file_cluster_12: 13.756
- **Magnitude:** 1346.04 | **LOC:** 1315 | **CtrlFlow:** 77.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 200
- **Risk Profile:** Cognitive Load (97.6661%), Tech Debt (30.6275%)
**Top Internal Functions/Classes:**
  * `IOT010` (Impact: 367.4 | O(2^N) | DB: 200)
  * `SMM010` (Impact: 142.5 | O(2^N) | DB: 75)
  * `A010` (Impact: 130.8 | O(2^N) | DB: 32)
  * `RMM010` (Impact: 66.4 | O(2^N) | DB: 28)
  * `STM010` (Impact: 37.5 | O(2^N) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 533`, `dead_code: 6`, `orphaned_logic: 13`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 29`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DFHAID, BNK1MAI, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/XFRFUN.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.384 IQR)
- **Top Global Matches:** file_cluster_11: 14.384, file_cluster_0: 14.488, file_cluster_13: 14.553
- **Magnitude:** 1333.74 | **LOC:** 1925 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 156
- **Risk Profile:** Cognitive Load (97.5673%), Tech Debt (12.0634%)
**Top Internal Functions/Classes:**
  * `UAD010` (Impact: 353.0 | O(2^N) | DB: 156)
  * `AH010` (Impact: 103.5 | O(2^N) | DB: 25)
  * `UADT010` (Impact: 93.7 | O(N^6) | DB: 90)
  * `COMM-AMT` (Impact: 71.2 | O(N^6) | DB: 48)
    * *Intent:* * * Check if SQLCODE indicates that Storm Drain processing * is applicable in a workload if activate...
  * `WTPD010` (Impact: 38.5 | O(2^N) | DB: 47)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 73`, `args: 1`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 536`, `dead_code: 23`, `duplicate_logic: 2`
* *Architecture:* `io: 19`, `api: 17`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 47`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` PROCTRAN, SQLCA, PROCDB2, SORTCODE, ABNDINFO, XFRFUN, ACCOUNT, ACCDB2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1TFN.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.955 IQR)
- **Top Global Matches:** file_cluster_11: 13.955, file_cluster_8: 14.001, file_cluster_0: 14.059
- **Magnitude:** 1249.76 | **LOC:** 1228 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (95.0869%), Tech Debt (31.2316%)
**Top Internal Functions/Classes:**
  * `SM010` (Impact: 142.5 | O(2^N) | DB: 75)
  * `A010` (Impact: 138.2 | O(2^N) | DB: 30)
  * `GCD010` (Impact: 126.0 | O(2^N) | DB: 69)
  * `WS-NUM-COUNT-MINUS` (Impact: 107.9 | O(2^N) | DB: 41)
  * `VA010` (Impact: 38.5 | O(N^5) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 52`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 537`, `dead_code: 9`, `orphaned_logic: 13`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 34`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BNK1TFM, DFHAID, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BANKDATA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.813 IQR)
- **Top Global Matches:** file_cluster_8: 12.813, file_cluster_13: 13.103, file_cluster_11: 13.124
- **Magnitude:** 1206.18 | **LOC:** 1464 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 225
- **Risk Profile:** Cognitive Load (91.923%), Tech Debt (51.8287%)
**Top Internal Functions/Classes:**
  * `RANDOM-SEED` (Impact: 208.1 | O(2^N) | DB: 112)
  * `DBR010` (Impact: 128.4 | O(N^5) | DB: 54)
  * `HV-ACCOUNT-ACTUAL-BALANCE` (Impact: 69.7 | O(2^N) | DB: 10)
    * *Intent:* * *** Close the files *
  * `SOURCE-COMPUTER` (Impact: 58.9 | O(N^6) | DB: 9)
    * *Intent:* ****************************************************************** * * * Copyright IBM Corp. 2023 * ...
  * `ACCOUNT-TYPES-COUNT` (Impact: 21.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 84`, `args: 3`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 545`, `dead_code: 3`, `orphaned_logic: 26`
* *Architecture:* `io: 32`, `api: 3`, `import: 7`
* *Defense:* `safety: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CUSTOMER, CUSTCTRL, ACCTCTRL, SQLCA, SORTCODE, CONTDB2, ACCDB2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CRA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.834 IQR)
- **Top Global Matches:** file_cluster_11: 13.834, file_cluster_8: 13.854, file_cluster_0: 13.942
- **Magnitude:** 1140.78 | **LOC:** 1170 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (96.0075%), Tech Debt (30.3384%)
**Top Internal Functions/Classes:**
  * `A010` (Impact: 152.7 | O(2^N) | DB: 35)
  * `SM010` (Impact: 142.4 | O(2^N) | DB: 75)
  * `UCD010` (Impact: 118.2 | O(2^N) | DB: 49)
  * `VA010` (Impact: 80.2 | O(N^5) | DB: 59)
  * `RM010` (Impact: 37.5 | O(2^N) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 36`, `args: 1`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 493`, `dead_code: 8`, `orphaned_logic: 12`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 32`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DFHAID, BNK1CDM, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1DAC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.023 IQR)
- **Top Global Matches:** file_cluster_11: 14.023, file_cluster_8: 14.122, file_cluster_0: 14.131
- **Magnitude:** 1138.24 | **LOC:** 1162 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (95.4755%), Tech Debt (33.1644%)
**Top Internal Functions/Classes:**
  * `A010` (Impact: 188.6 | O(2^N) | DB: 47)
  * `SM010` (Impact: 156.8 | O(2^N) | DB: 76)
  * `DAD010` (Impact: 63.5 | O(2^N) | DB: 39)
  * `GAD010` (Impact: 54.0 | O(2^N) | DB: 52)
  * `PM010` (Impact: 38.6 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 47`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 492`, `dead_code: 10`, `orphaned_logic: 13`
* *Architecture:* `io: 3`, `api: 1`, `import: 4`
* *Defense:* `safety: 29`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` INQACC, DFHAID, BNK1DAM, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/CRECUST.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.949 IQR)
- **Top Global Matches:** file_cluster_11: 13.949, file_cluster_0: 14.048, file_cluster_13: 14.058
- **Magnitude:** 1122.78 | **LOC:** 1498 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 138
- **Risk Profile:** Cognitive Load (96.9734%), Tech Debt (36.2108%)
**Top Internal Functions/Classes:**
  * `CC010` (Impact: 246.7 | O(N^6) | DB: 138)
  * `GLCV010` (Impact: 84.0 | O(N^6) | DB: 20)
  * `P010` (Impact: 82.5 | O(N^5) | DB: 30)
  * `WPD010` (Impact: 39.5 | O(2^N) | DB: 46)
  * `WCV010` (Impact: 35.6 | O(N^5) | DB: 18)
    * *Intent:* * * Convert the integer date back to YYYYMMDD * format
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 73`, `args: 3`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 470`, `dead_code: 13`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 22`, `api: 29`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 46`, `doc: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CUSTOMER, CRECUST, CUSTCTRL, PROCTRAN, SQLCA, CEEIGZCT, PROCDB2, SORTCODE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CCA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.896 IQR)
- **Top Global Matches:** file_cluster_11: 13.896, file_cluster_8: 14.012, file_cluster_13: 14.018
- **Magnitude:** 986.18 | **LOC:** 956 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (96.7186%), Tech Debt (39.8889%)
**Top Internal Functions/Classes:**
  * `GCD010` (Impact: 224.9 | O(2^N) | DB: 59)
    * *Intent:* * * Preserve the RESP and RESP2, then set up the * standard ABEND info before getting the applid, * ...
  * `SM010` (Impact: 142.5 | O(2^N) | DB: 75)
    * *Intent:* * * Empty the account numbers in the on screen array *
  * `A010` (Impact: 138.2 | O(2^N) | DB: 32)
  * `RM010` (Impact: 37.5 | O(2^N) | DB: 26)
  * `STM010` (Impact: 37.5 | O(2^N) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 32`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 342`, `dead_code: 9`, `orphaned_logic: 12`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` INQACCCU, DFHAID, ABNDINFO, BNK1ACC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.4 IQR)
- **Top Global Matches:** file_cluster_8: 11.4, file_cluster_0: 11.565, file_cluster_13: 11.609
- **Magnitude:** 839.38 | **LOC:** 1231 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (31.9176%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteCustomerInternal` (Impact: 189.5 | O(2^N) | DB: 18)
  * `createCustomerInternal` (Impact: 91.4 | O(2^N) | DB: 26)
  * `updateCustomerInternal` (Impact: 46.5 | O(2^N) | DB: 14)
  * `getCustomersInternal` (Impact: 40.5 | O(2^N) | DB: 12)
  * `getCustomersByNameInternal` (Impact: 27.9 | O(2^N) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 138`, `args: 51`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 219`
* *Architecture:* `io: 9`, `api: 30`, `import: 24`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.211
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.004073
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.InvalidRequestException, java.util.logging.Logger, jakarta.ws.rs.GET, java.util.TimeZone, jakarta.ws.rs.core.Response, java.util.Calendar, java.io.IOException, jakarta.ws.rs.Path...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/CREACC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.735 IQR)
- **Top Global Matches:** file_cluster_8: 12.735, file_cluster_13: 12.819, file_cluster_11: 12.894
- **Magnitude:** 777.8 | **LOC:** 1248 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 121
- **Risk Profile:** Cognitive Load (96.9086%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CD010` (Impact: 76.3 | O(N^6) | DB: 13)
  * `FNA010` (Impact: 67.5 | O(N^6) | DB: 121)
  * `REQUIRED-SORT-CODE2` (Impact: 56.8 | O(N^5) | DB: 12)
  * `WPD010` (Impact: 39.0 | O(2^N) | DB: 44)
  * `ATC010` (Impact: 23.1 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 74`, `args: 1`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 377`, `dead_code: 3`
* *Architecture:* `io: 18`, `api: 27`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 20`, `doc: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` CUSTOMER, ACCTCTRL, CREACC, PROCTRAN, SQLCA, INQCUST, INQACCCU, PROCDB2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQACC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.963 IQR)
- **Top Global Matches:** file_cluster_8: 12.963, file_cluster_11: 12.978, file_cluster_13: 13.016
- **Magnitude:** 723.08 | **LOC:** 1003 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (95.8769%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AH010` (Impact: 112.7 | O(2^N) | DB: 45)
  * `RAD010` (Impact: 104.3 | O(2^N) | DB: 70)
  * `FD010` (Impact: 67.2 | O(2^N) | DB: 28)
    * *Intent:* *
  * `GLAD010` (Impact: 35.0 | O(2^N) | DB: 50)
    * *Intent:* * * Preserve the RESP and RESP2, then set up the * standard ABEND info before getting the applid, * ...
  * `CFSDCD010` (Impact: 25.1 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 66`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 300`, `dead_code: 5`
* *Architecture:* `io: 17`, `api: 15`, `import: 6`
* *Defense:* `safety: 21`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` INQACC, SQLCA, SORTCODE, ABNDINFO, ACCOUNT, ACCDB2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQACCCU.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.149 IQR)
- **Top Global Matches:** file_cluster_11: 13.149, file_cluster_13: 13.175, file_cluster_0: 13.243
- **Magnitude:** 710.62 | **LOC:** 883 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (96.0591%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RAD010` (Impact: 141.6 | O(2^N) | DB: 81)
    * *Intent:* *
  * `FD010` (Impact: 112.7 | O(2^N) | DB: 62)
    * *Intent:* *
  * `AH010` (Impact: 103.5 | O(2^N) | DB: 24)
  * `CFSDD010` (Impact: 24.9 | O(N^5) | DB: 2)
  * `CC010` (Impact: 17.4 | O(N^3) | DB: 9)
    * *Intent:* * * Evaluate the Abend code that is returned
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 58`, `args: 1`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 250`, `dead_code: 5`
* *Architecture:* `io: 15`, `api: 12`, `import: 8`
* *Defense:* `safety: 25`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` CUSTOMER, SQLCA, INQCUST, INQACCCU, SORTCODE, ABNDINFO, ACCOUNT, ACCDB2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQCUST.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.658 IQR)
- **Top Global Matches:** file_cluster_11: 13.658, file_cluster_0: 13.754, file_cluster_13: 13.808
- **Magnitude:** 655.66 | **LOC:** 712 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (97.6204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RCV010` (Impact: 195.7 | O(2^N) | DB: 56)
  * `AH010` (Impact: 95.7 | O(2^N) | DB: 24)
  * `GLCV010` (Impact: 76.8 | O(N^5) | DB: 8)
  * `P010` (Impact: 39.9 | O(N^4) | DB: 34)
  * `RCN010` (Impact: 8.2 | O(N^3) | DB: 1)
    * *Intent:* * * For a random customer generate a CUSTOMER number
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 49`, `args: 1`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 181`, `dead_code: 7`
* *Architecture:* `io: 16`, `api: 17`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 27`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CUSTOMER, INQCUST, SORTCODE, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mvnw` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.955 IQR)
- **Top Global Matches:** file_cluster_4: 12.955, file_cluster_11: 13.476, file_cluster_12: 13.55
- **Magnitude:** 547.38 | **LOC:** 312 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (99.9773%), Tech Debt (99.9928%)
**Top Internal Functions/Classes:**
  * `find_maven_basedir_[Truncated]` (Impact: 258.3 | O(N^4) | DB: 75)
    * *Intent:* # traverses directory structure from process work directory to filesystem root # first directory wit...
  * `Anonymous_Block` (Impact: 23.8 | O(N^2) | DB: 10)
    * *Intent:* # For Mingw, ensure paths are in UNIX format before anything is touched
  * `Anonymous_Block` (Impact: 12.8 | O(N^2))
  * `Anonymous_Block` (Impact: 10.2 | O(N^1) | DB: 14)
  * `Anonymous_Block` (Impact: 9.6 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 27`, `args: 7`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 141`, `dead_code: 1`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `io: 23`, `api: 5`, `concurrency: 54`, `import: 2`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mavenrc, .mavenrc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/DBCRFUN.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.737 IQR)
- **Top Global Matches:** file_cluster_11: 14.737, file_cluster_0: 14.802, file_cluster_17: 14.811
- **Magnitude:** 538.34 | **LOC:** 862 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (95.3695%), Tech Debt (75.0186%)
**Top Internal Functions/Classes:**
  * `WTPD010` (Impact: 112.8 | O(2^N) | DB: 51)
  * `AH010` (Impact: 103.7 | O(2^N) | DB: 25)
  * `UAD010` (Impact: 49.6 | O(N^5) | DB: 17)
  * `CFSDD010` (Impact: 25.0 | O(N^5) | DB: 2)
  * `COMM-ACT-BAL` (Impact: 8.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 47`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 192`, `dead_code: 14`, `orphaned_logic: 17`
* *Architecture:* `io: 11`, `api: 1`, `import: 8`
* *Defense:* `safety: 23`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` PAYDBCR, PROCTRAN, SQLCA, PROCDB2, SORTCODE, ABNDINFO, ACCOUNT, ACCDB2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/ProcessedTransaction.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.417 IQR)
- **Top Global Matches:** file_cluster_8: 11.417, file_cluster_13: 11.766, file_cluster_7: 11.978
- **Magnitude:** 512.5 | **LOC:** 1012 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (61.0971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getProcessedTransactions` (Impact: 29.0 | O(N^1) | DB: 15)
  * `sortOutDateTimeTaskString` (Impact: 18.9 | O(N^1))
  * `writeDeleteCustomer` (Impact: 16.4 | O(N^1) | DB: 9)
  * `writeCreateCustomer` (Impact: 13.4 | O(N^1) | DB: 9)
  * `writeCreateAccount` (Impact: 11.3 | O(N^1) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 99`, `args: 57`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 197`
* *Architecture:* `io: 2`, `api: 55`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.002037
  * `Imports (Out-Degree: 2):` com.ibm.cics.cip.bankliberty.datainterfaces.PROCTRAN, java.sql.PreparedStatement, com.ibm.cics.server.Task, java.util.Calendar, java.sql.ResultSet, java.util.logging.Logger, java.math.BigDecimal, com.ibm.cics.cip.bankliberty.api.json.HBankDataAccess...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.121 IQR)
- **Top Global Matches:** file_cluster_8: 11.121, file_cluster_13: 11.312, file_cluster_0: 11.315
- **Magnitude:** 440.3 | **LOC:** 1765 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (24.8621%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createAccountInternal` (Impact: 50.2 | O(N^1) | DB: 25)
  * `getAccountsByCustomerInternal` (Impact: 35.9 | O(N^2) | DB: 18)
  * `transferLocalExternal` (Impact: 34.5 | O(2^N) | DB: 2)
  * `updateAccountInternal` (Impact: 24.4 | O(N^1) | DB: 19)
  * `getAccountInternal` (Impact: 17.8 | O(N^1) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 120`, `args: 42`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 173`
* *Architecture:* `io: 8`, `api: 28`, `import: 21`
* *Defense:* `safety: 6`, `doc: 10`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.211
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.004073
  * `Imports (Out-Degree: 1):` com.ibm.cics.server.InvalidRequestException, java.util.logging.Logger, jakarta.ws.rs.GET, jakarta.ws.rs.core.Response, java.io.IOException, jakarta.ws.rs.Path, jakarta.ws.rs.DELETE, jakarta.ws.rs.POST...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.191 IQR)
- **Top Global Matches:** file_cluster_8: 11.191, file_cluster_13: 11.441, file_cluster_11: 11.722
- **Magnitude:** 422.88 | **LOC:** 1362 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (44.0928%), Tech Debt (37.0892%)
**Top Internal Functions/Classes:**
  * `createAccount` (Impact: 42.0 | O(N^1) | DB: 9)
  * `getAccount` (Impact: 33.6 | O(N^2) | DB: 9)
  * `updateThis` (Impact: 25.1 | O(N^1) | DB: 9)
  * `deleteAccount` (Impact: 19.3 | O(N^1) | DB: 7)
  * `getAccountsCountOnly` (Impact: 17.6 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 79`, `args: 52`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 106`, `duplicate_logic: 5`
* *Architecture:* `io: 11`, `api: 47`, `import: 12`
* *Defense:* `safety: 15`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.465
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.003666
  * `Imports (Out-Degree: 2):` com.ibm.cics.server.InvalidRequestException, java.sql.PreparedStatement, com.ibm.cics.cip.bankliberty.api.json.AccountJSON, com.ibm.cics.server.Task, java.util.Calendar, java.sql.ResultSet, java.util.logging.Logger, java.math.BigDecimal...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/DELCUS.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.71 IQR)
- **Top Global Matches:** file_cluster_8: 11.71, file_cluster_13: 11.791, file_cluster_11: 11.967
- **Magnitude:** 412.2 | **LOC:** 762 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (91.2989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DCV010` (Impact: 88.6 | O(2^N) | DB: 34)
  * `COMM-CREDIT-SCORE` (Impact: 39.6 | O(N^6) | DB: 38)
  * `WPCD010` (Impact: 32.0 | O(2^N) | DB: 46)
    * *Intent:* * * Preserve the RESP and RESP2, then set up the
  * `INQCUST-CUSTNO` (Impact: 21.9 | O(N^5) | DB: 5)
  * `DA010` (Impact: 15.7 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 38`, `args: 1`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 146`, `dead_code: 2`
* *Architecture:* `io: 19`, `api: 18`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CUSTOMER, PROCTRAN, SQLCA, DELCUS, INQACCCU, INQCUST, PROCDB2, SORTCODE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.578 IQR)
- **Top Global Matches:** file_cluster_8: 10.578, file_cluster_13: 10.73, file_cluster_7: 11.204
- **Magnitude:** 329.36 | **LOC:** 1953 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (16.5052%), Tech Debt (14.0827%)
**Top Internal Functions/Classes:**
  * `getCustomersByName` (Impact: 42.7 | O(N^2) | DB: 8)
  * `getCustomersBySurname` (Impact: 42.6 | O(N^1) | DB: 2)
  * `getCustomers` (Impact: 27.6 | O(N^1) | DB: 8)
  * `getCustomer` (Impact: 25.0 | O(N^1) | DB: 1)
  * `getCustomersByNameCountOnly` (Impact: 22.9 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 131`, `args: 35`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 50`, `duplicate_logic: 2`
* *Architecture:* `api: 28`, `import: 37`
* *Defense:* `safety: 38`, `doc: 1`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.465
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.003666
  * `Imports (Out-Degree: 4):` com.ibm.cics.server.InvalidRequestException, java.util.logging.Logger, com.ibm.cics.server.NotAuthorisedException, com.ibm.cics.server.DuplicateRecordException, java.util.TimeZone, com.ibm.cics.server.ResourceUnavailableException, com.ibm.cics.server.ISCInvalidRequestException, com.ibm.cics.server.IOErrorException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/AccountEnquiryForm.java` (JAVA) | Magnitude: 21.88 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 23, api: 9, structural_boundaries: 7, args: 5
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionTransferLocalJSON.java` (JAVA) | Magnitude: 16.8 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 10, api: 5, args: 4
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountJSON.java` (JAVA) | Magnitude: 117.9 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 137, api: 39, structural_boundaries: 34, args: 24
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerJSON.java` (JAVA) | Magnitude: 95.32 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 119, structural_boundaries: 30, api: 27, args: 16
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/customerenquiry/CustomerEnquiryForm.java` (JAVA) | Magnitude: 21.3 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, api: 9, structural_boundaries: 7, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/base/cobol_src/BNK1CCS.cbl` (COBOL) | Magnitude: 1947.78 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1164, state_mutation: 866, branch: 191, structural_boundaries: 92
- `src/base/cobol_src/BNK1CRA.cbl` (COBOL) | Magnitude: 1140.78 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 794, state_mutation: 493, branch: 97, reflection_metaprogramming: 45
- `src/base/cobol_src/INQACCCU.cbl` (COBOL) | Magnitude: 710.62 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 571, state_mutation: 250, branch: 65, structural_boundaries: 58
- `src/base/cobol_src/BNK1TFN.cbl` (COBOL) | Magnitude: 1249.76 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 833, state_mutation: 537, branch: 102, structural_boundaries: 52
- `src/base/cobol_src/UPDCUST.cbl` (COBOL) | Magnitude: 223.16 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 208, state_mutation: 100, branch: 33, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/CustomerServices.java` (JAVA) | Magnitude: 7.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 8, import: 5, api: 2
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/PaymentInterface.java` (JAVA) | Magnitude: 7.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 8, import: 5, api: 2
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/listaccounts/ListAccJson.java` (JAVA) | Magnitude: 15.26 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 9, api: 7, args: 3
- `src/bank-application-frontend/src/App.js` (JAVASCRIPT) | Magnitude: 14.86 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 73, ui_framework: 30, structural_boundaries: 22, io: 18
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java` (JAVA) | Magnitude: 143.06 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 155, structural_boundaries: 28, branch: 22, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/bank-application-frontend/src/content/CustomerDetailsPage/CustomerDetailsPage.js` (JAVASCRIPT) | Magnitude: 154.0 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 195, concurrency: 43, structural_boundaries: 34, ui_framework: 32
- `src/bank-application-frontend/src/content/AccountDetailsPage/AccountDetailsTable.js` (JAVASCRIPT) | Magnitude: 92.8 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 260, ui_framework: 36, func_start: 32, structural_boundaries: 30
- `src/bank-application-frontend/src/content/AccountCreationPage/AccountCreationPage.js` (JAVASCRIPT) | Magnitude: 77.2 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 231, ui_framework: 43, func_start: 31, structural_boundaries: 20
- `src/bank-application-frontend/src/content/CustomerDeletePage/CustomerDeleteTables.js` (JAVASCRIPT) | Magnitude: 113.02 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 254, structural_boundaries: 47, concurrency: 43, ui_framework: 41
- `src/bank-application-frontend/src/content/CustomerDeletePage/CustomerDeletePage.js` (JAVASCRIPT) | Magnitude: 106.52 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 137, concurrency: 37, ui_framework: 29, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/bank-application-frontend/src/content/AccountDeletePage/AccountDeleteTables.js` (JAVASCRIPT) | Magnitude: 206.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 333, concurrency: 74, structural_boundaries: 46, ui_framework: 36
- `mvnw` (SHELL) | Magnitude: 547.38 | Delta: **0.521 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 169, state_mutation: 141, branch: 127, concurrency: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/base/cobol_src/INQACC.cbl` (COBOL) | Magnitude: 723.08 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 664, state_mutation: 300, structural_boundaries: 66, branch: 56
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java` (JAVA) | Magnitude: 22.62 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 11, args: 7, api: 7
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/JsonPropertyNamingStrategy.java` (JAVA) | Magnitude: 22.62 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 11, args: 7, api: 7
- `src/base/cobol_src/BNKMENU.cbl` (COBOL) | Magnitude: 1346.04 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 847, state_mutation: 533, branch: 104, reflection_metaprogramming: 65
- `src/base/cobol_src/GETSCODE.cbl` (COBOL) | Magnitude: 9.58 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, func_start: 4, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/base/cobol_src/UPDACC.cbl` (COBOL) | Magnitude: 130.16 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 208, state_mutation: 65, structural_boundaries: 26, dead_code: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers/WebController.java` -> Churn: **100.0%** | Cog Load: 7.7861% | Debt: 75.8532%
- `src/bank-application-frontend/updateWebUI.sh` -> Churn: **63.09%** | Cog Load: 5.0% | Debt: 100.0%
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/AccountEnquiryForm.java` -> Churn: **63.09%** | Cog Load: 6.772% | Debt: 100.0%
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/customerenquiry/CustomerEnquiryForm.java` -> Churn: **63.09%** | Cog Load: 6.7138% | Debt: 99.9999%
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/jsonclasses/paymentinterface/TransferForm.java` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 99.9995%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/base/cobol_src/BNK1DCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 2074.12
- `src/base/cobol_src/BNK1CCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 1947.78
- `src/base/cobol_src/BNK1UAC.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 1413.86
- `src/base/cobol_src/BNK1CAC.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 1374.38
- `src/base/cobol_src/BNKMENU.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 1346.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.712%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.1227%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 96.2554%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 43.291%)
- `src/bank-application-frontend/src/App.js` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 27.0976%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **Severity: 1.041** (Embedded: 0.0185 * Error Risk: 56.2177%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java` -> **Severity: 0.405** (Embedded: 0.0061 * Error Risk: 66.323%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` -> **Severity: 0.361** (Embedded: 0.0041 * Error Risk: 88.7087%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.346** (Embedded: 0.0041 * Error Risk: 84.8829%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` -> **Severity: 0.283** (Embedded: 0.0037 * Error Risk: 77.2096%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java` -> **Severity: 2628.031** (Blast Radius: 26.341 * Doc Risk: 99.7696%)
- `src/base/cobol_copy/ABNDINFO.cpy` -> **Severity: 2352.685** (Blast Radius: 24.232 * Doc Risk: 97.09%)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **Severity: 852.714** (Blast Radius: 8.671 * Doc Risk: 98.3409%)
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/JsonPropertyNamingStrategy.java` -> **Severity: 698.188** (Blast Radius: 6.998 * Doc Risk: 99.7696%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/GetSortCode.java` -> **Severity: 446.5** (Blast Radius: 4.465 * Doc Risk: 99.9999%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
