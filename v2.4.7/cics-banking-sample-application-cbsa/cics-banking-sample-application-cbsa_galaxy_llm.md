# ARCHITECTURAL_BRIEF: cics-banking-sample-application-cbsa
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cics-banking-sample-application-cbsa` |
| **Timestamp** | `2026-08-07T03:50:46.414245+00:00` |
| **Scan Duration** | `1.76s` |
| **Git Branch** | `main` |
| **Git Commit** | `46cbda52051d5cded017d72ad653df68b8ec1b60` |
| **Git Remote** | `https://github.com/cicsdev/cics-banking-sample-application-cbsa.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 292 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 13.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 16.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.9 | 2.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 78.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.2 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.9 | 17.9 | 0.0 |
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

- `find_maven_basedir_[Truncated]` (@ `mvnw`) -> Impact: **186.9** | LOC: 145
  * *Intent:* # traverses directory structure from process work directory to filesystem root # first directory with .mvn subdirectory is considered project base dir...
- `EIBRESP-TOSTRING` (@ `src/base/cobol_copy/RESPSTR.cpy`) -> Impact: **130.8** | LOC: 236
- `ED010` (@ `src/base/cobol_src/BNK1CCS.cbl`) -> Impact: **115.6** | LOC: 352
- `CC010` (@ `src/base/cobol_src/CRECUST.cbl`) -> Impact: **84.2** | LOC: 383
- `IOT010` (@ `src/base/cobol_src/BNKMENU.cbl`) -> Impact: **73.5** | LOC: 489
- `UAD010` (@ `src/base/cobol_src/XFRFUN.cbl`) -> Impact: **71.0** | LOC: 480
- `ED010` (@ `src/base/cobol_src/BNK1CAC.cbl`) -> Impact: **69.8** | LOC: 275
- `deleteCustomerInternal` (@ `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java`) -> Impact: **68.8** | LOC: 168
- `createCustomerInternal` (@ `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java`) -> Impact: **51.2** | LOC: 219
- `createAccountInternal` (@ `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java`) -> Impact: **50.2** | LOC: 172

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/base/cobol_src` | 29 | 12829.4 | 86.74% | 34.16% |
| `src/bank-application-frontend` | 6 | 5031.56 | 2.5% | 16.67% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json` | 19 | 1647.56 | 10.95% | 59.86% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces` | 7 | 1013.18 | 9.13% | 75.44% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2` | 2 | 988.18 | 43.25% | 85.72% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access` | 5 | 801.16 | 27.98% | 76.05% |
| `etc/install/base/buildjcl` | 46 | 653.64 | 4.57% | 0.0% |
| `__monolith__` | 6 | 543.2 | 17.5% | 16.67% |
| `etc/install/base/db2jcl` | 32 | 492.54 | 10.35% | 0.0% |
| `etc/install/base/installjcl` | 25 | 422.02 | 9.45% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/bank-application-frontend/updateWebUI.sh` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/InqaccJson.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createaccount/CreaccJson.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createcustomer/CrecustJson.java` -> **100.0%** Exposure
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
10. **`mvnw`** -> AI Confidence: **99.29%**
11. **`src/base/cobol_copy/DELACCZ.cpy`** -> AI Confidence: **99.29%**
12. **`src/base/cobol_copy/INQACCCU.cpy`** -> AI Confidence: **99.29%**
13. **`src/base/cobol_copy/INQACCCZ.cpy`** -> AI Confidence: **99.29%**
14. **`src/base/cobol_copy/RESPSTR.cpy`** -> AI Confidence: **99.29%**
15. **`src/base/cobol_src/INQACCCU.cbl`** -> AI Confidence: **99.25%**
16. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java`** -> AI Confidence: **99.24%**
17. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java`** -> AI Confidence: **99.24%**
18. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/AccountList.java`** -> AI Confidence: **99.24%**
19. **`src/base/cobol_src/BNK1CAC.cbl`** -> AI Confidence: **99.2%**
20. **`src/base/cobol_src/BNK1CRA.cbl`** -> AI Confidence: **99.2%**
21. **`src/base/cobol_src/BNK1UAC.cbl`** -> AI Confidence: **99.2%**
22. **`src/base/cobol_src/BNKMENU.cbl`** -> AI Confidence: **99.2%**
23. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CreditScoreCICS540.java`** -> AI Confidence: **99.18%**
24. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionResource.java`** -> AI Confidence: **99.18%**
25. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/Account.java`** -> AI Confidence: **99.18%**
26. **`src/base/cobol_src/BNK1CCA.cbl`** -> AI Confidence: **99.17%**
27. **`src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers/WebController.java`** -> AI Confidence: **99.16%**
28. **`src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/controllers/WebController.java`** -> AI Confidence: **99.16%**
29. **`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `38` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `964` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mvnw` (SHELL) -> Cumulative Risk: **702.43**
- **Archetype:** `file_cluster_4` (Distance: 13.007 IQR)
- **Magnitude:** 510.58 | **LOC:** 312 | **CtrlFlow:** 90.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9928%)
- **Heaviest Functions:** `find_maven_basedir_[Truncated]` (Impact: 186.9), `Anonymous_Block` (Impact: 28.2), `Anonymous_Block` (Impact: 15.6)

### 2. `src/base/cobol_src/CRECUST.cbl` (COBOL) -> Cumulative Risk: **622.35**
- **Archetype:** `file_cluster_11` (Distance: 13.949 IQR)
- **Magnitude:** 749.38 | **LOC:** 1498 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.9734%), Safety Score (86.5913%)
- **Heaviest Functions:** `CC010` (Impact: 84.2), `P010` (Impact: 30.5), `GLCV010` (Impact: 26.6)

### 3. `src/bank-application-frontend/src/content/AccountDeletePage/AccountDeleteTables.js` (JAVASCRIPT) -> Cumulative Risk: **608.44**
- **Archetype:** `file_cluster_4` (Distance: 10.651 IQR)
- **Magnitude:** 188.6 | **LOC:** 408 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (88.0034%), Verification (80.0%)
- **Heaviest Functions:** `getAccountByNum` (Impact: 16.4), `deleteAccount` (Impact: 11.4), `getOtherAccounts` (Impact: 10.3)

### 4. `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/updatecustomer/UpdcustJson.java` (JAVA) -> Cumulative Risk: **578.25**
- **Archetype:** `file_cluster_8` (Distance: 9.68 IQR)
- **Magnitude:** 110.04 | **LOC:** 210 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (80.1488%)
- **Heaviest Functions:** `UpdcustJson` (Impact: 19.6), `toString` (Impact: 2.8), `setCommEye` (Impact: 2.4)

### 5. `src/base/cobol_src/BNK1UAC.cbl` (COBOL) -> Cumulative Risk: **576.67**
- **Archetype:** `file_cluster_11` (Distance: 14.475 IQR)
- **Magnitude:** 890.36 | **LOC:** 1409 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (95.5224%), Safety Score (94.9576%)
- **Heaviest Functions:** `VD010` (Impact: 48.0), `A010` (Impact: 29.1), `SM010` (Impact: 28.5)

### 6. `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/listaccounts/AccountDetails.java` (JAVA) -> Cumulative Risk: **576.17**
- **Archetype:** `file_cluster_0` (Distance: 12.086 IQR)
- **Magnitude:** 115.66 | **LOC:** 240 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9998%), Verification (80.0%)
- **Heaviest Functions:** `toPrettyString` (Impact: 23.1), `toString` (Impact: 2.9), `setCommActualBalance` (Impact: 2.4)

### 7. `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/deleteaccount/DelaccJson.java` (JAVA) -> Cumulative Risk: **573.9**
- **Archetype:** `file_cluster_8` (Distance: 9.484 IQR)
- **Magnitude:** 175.26 | **LOC:** 360 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Verification (80.0%)
- **Heaviest Functions:** `setDelaccAccType` (Impact: 7.3), `toString` (Impact: 3.2), `setDelaccSuccess` (Impact: 2.4)

### 8. `src/base/cobol_src/BNK1CCA.cbl` (COBOL) -> Cumulative Risk: **570.9**
- **Archetype:** `file_cluster_11` (Distance: 13.896 IQR)
- **Magnitude:** 489.78 | **LOC:** 956 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.7186%), Safety Score (90.4793%)
- **Heaviest Functions:** `GCD010` (Impact: 39.0), `SM010` (Impact: 28.5), `A010` (Impact: 24.2)

### 9. `src/base/cobol_src/BNK1DCS.cbl` (COBOL) -> Cumulative Risk: **569.86**
- **Archetype:** `file_cluster_11` (Distance: 14.763 IQR)
- **Magnitude:** 1217.92 | **LOC:** 2057 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.0041%), Safety Score (95.3481%)
- **Heaviest Functions:** `A010` (Impact: 37.4), `SM010` (Impact: 32.0), `PM010` (Impact: 31.4)

### 10. `src/base/cobol_src/DBCRFUN.cbl` (COBOL) -> Cumulative Risk: **569.75**
- **Archetype:** `file_cluster_11` (Distance: 14.737 IQR)
- **Magnitude:** 301.44 | **LOC:** 862 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Cognitive Load (95.3695%), Safety Score (82.3078%)
- **Heaviest Functions:** `WTPD010` (Impact: 22.9), `AH010` (Impact: 19.7), `UAD010` (Impact: 19.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/bank-application-frontend/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Magnitude:** 1217.92 | **LOC:** 2057 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.0041%), Tech Debt (33.9781%)
**Top Internal Functions/Classes:**
  * `A010` (Impact: 37.4)
  * `SM010` (Impact: 32.0)
  * `PM010` (Impact: 31.4)
  * `ED2010` (Impact: 21.4)
  * `UPDCD010` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 48`, `args: 1`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 2`, `state_mutation: 915`, `dead_code: 21`, `orphaned_logic: 23`
* *Architecture:* `io: 2`, `api: 1`, `import: 7`
* *Defense:* `safety: 48`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BNK1DCM, INQCUST, DELCUS, DFHAID, DFHBMSCA, ABNDINFO, UPDCUST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CCS.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.941 IQR)
- **Top Global Matches:** file_cluster_11: 13.941, file_cluster_8: 13.959, file_cluster_0: 14.073
- **Magnitude:** 1169.78 | **LOC:** 1661 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.1196%), Tech Debt (26.5409%)
**Top Internal Functions/Classes:**
  * `ED010` (Impact: 115.6)
  * `SM010` (Impact: 32.0)
  * `A010` (Impact: 30.9)
  * `CCD010` (Impact: 22.0)
  * `RM010` (Impact: 20.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 92`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 866`, `dead_code: 9`, `orphaned_logic: 16`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 40`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, DFHAID, BNK1CCM
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1UAC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.475 IQR)
- **Top Global Matches:** file_cluster_11: 14.475, file_cluster_0: 14.581, file_cluster_17: 14.586
- **Magnitude:** 890.36 | **LOC:** 1409 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.5224%), Tech Debt (41.8922%)
**Top Internal Functions/Classes:**
  * `VD010` (Impact: 48.0)
    * *Intent:* * * Retrieve the data
  * `A010` (Impact: 29.1)
  * `SM010` (Impact: 28.5)
  * `WS-CONVERTED-VAL2` (Impact: 16.2)
  * `PM010` (Impact: 14.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 42`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 674`, `dead_code: 14`, `duplicate_logic: 2`, `orphaned_logic: 15`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 43`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BNK1UAM, DFHAID, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/XFRFUN.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.384 IQR)
- **Top Global Matches:** file_cluster_11: 14.384, file_cluster_0: 14.488, file_cluster_13: 14.553
- **Magnitude:** 790.14 | **LOC:** 1925 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.4775%), Tech Debt (12.0634%)
**Top Internal Functions/Classes:**
  * `UAD010` (Impact: 71.0)
  * `UADT010` (Impact: 36.1)
  * `COMM-AMT` (Impact: 26.2)
    * *Intent:* * * Check if SQLCODE indicates that Storm Drain processing * is applicable in a workload if activate...
  * `AH010` (Impact: 19.6)
  * `UADF010` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 73`, `args: 1`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 536`, `dead_code: 23`, `duplicate_logic: 2`
* *Architecture:* `io: 19`, `api: 17`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 47`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` SORTCODE, XFRFUN, ACCOUNT, ACCDB2, PROCTRAN, SQLCA, PROCDB2, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CAC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.899 IQR)
- **Top Global Matches:** file_cluster_11: 13.899, file_cluster_8: 13.957, file_cluster_0: 14.016
- **Magnitude:** 785.38 | **LOC:** 1302 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.045%), Tech Debt (26.0696%)
**Top Internal Functions/Classes:**
  * `ED010` (Impact: 69.8)
  * `CAD010` (Impact: 30.0)
  * `SM010` (Impact: 28.5)
  * `A010` (Impact: 27.8)
  * `RM010` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 54`, `args: 1`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 569`, `dead_code: 10`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `safety: 33`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BNK1CAM, DFHAID, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BANKDATA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.818 IQR)
- **Top Global Matches:** file_cluster_8: 12.818, file_cluster_13: 13.107, file_cluster_11: 13.127
- **Magnitude:** 756.18 | **LOC:** 1464 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.923%), Tech Debt (51.8287%)
**Top Internal Functions/Classes:**
  * `DBR010` (Impact: 48.4)
  * `RANDOM-SEED` (Impact: 40.0)
  * `SOURCE-COMPUTER` (Impact: 23.9)
    * *Intent:* ****************************************************************** * * * Copyright IBM Corp. 2023 * ...
  * `HV-ACCOUNT-ACTUAL-BALANCE` (Impact: 14.7)
    * *Intent:* * *** Close the files *
  * `ACCOUNT-OVERDRAFT-COUNT` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 84`, `args: 3`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 545`, `dead_code: 3`, `orphaned_logic: 26`
* *Architecture:* `io: 32`, `api: 3`, `import: 7`
* *Defense:* `safety: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` SORTCODE, ACCTCTRL, CUSTCTRL, CONTDB2, ACCDB2, CUSTOMER, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/CRECUST.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.949 IQR)
- **Top Global Matches:** file_cluster_11: 13.949, file_cluster_0: 14.048, file_cluster_13: 14.058
- **Magnitude:** 749.38 | **LOC:** 1498 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.9734%), Tech Debt (36.2108%)
**Top Internal Functions/Classes:**
  * `CC010` (Impact: 84.2)
  * `P010` (Impact: 30.5)
  * `GLCV010` (Impact: 26.6)
  * `WCV010` (Impact: 13.6)
    * *Intent:* * * Convert the integer date back to YYYYMMDD * format
  * `WPD010` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 73`, `args: 3`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 470`, `dead_code: 13`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 22`, `api: 29`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 46`, `doc: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` SORTCODE, CEEIGZCT, CUSTCTRL, CRECUST, PROCTRAN, CUSTOMER, SQLCA, PROCDB2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNKMENU.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.671 IQR)
- **Top Global Matches:** file_cluster_8: 13.671, file_cluster_11: 13.692, file_cluster_12: 13.756
- **Magnitude:** 725.64 | **LOC:** 1315 | **CtrlFlow:** 77.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.6661%), Tech Debt (30.6275%)
**Top Internal Functions/Classes:**
  * `IOT010` (Impact: 73.5)
  * `SMM010` (Impact: 28.5)
  * `A010` (Impact: 22.8)
  * `RMM010` (Impact: 12.4)
  * `STM010` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 533`, `dead_code: 6`, `orphaned_logic: 13`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 29`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DFHAID, ABNDINFO, BNK1MAI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1TFN.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.955 IQR)
- **Top Global Matches:** file_cluster_11: 13.955, file_cluster_8: 14.001, file_cluster_0: 14.059
- **Magnitude:** 720.76 | **LOC:** 1228 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.0869%), Tech Debt (31.2316%)
**Top Internal Functions/Classes:**
  * `SM010` (Impact: 28.5)
  * `A010` (Impact: 24.1)
  * `GCD010` (Impact: 23.9)
  * `WS-NUM-COUNT-MINUS` (Impact: 22.9)
  * `VA010` (Impact: 14.6)
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

### `src/base/cobol_src/BNK1CRA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.834 IQR)
- **Top Global Matches:** file_cluster_11: 13.834, file_cluster_8: 13.854, file_cluster_0: 13.942
- **Magnitude:** 668.68 | **LOC:** 1170 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.0075%), Tech Debt (30.3384%)
**Top Internal Functions/Classes:**
  * `VA010` (Impact: 32.2)
  * `SM010` (Impact: 28.5)
  * `A010` (Impact: 26.6)
  * `UCD010` (Impact: 22.2)
  * `ED010` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 36`, `args: 1`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 493`, `dead_code: 8`, `orphaned_logic: 12`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 32`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DFHAID, ABNDINFO, BNK1CDM
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1DAC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.023 IQR)
- **Top Global Matches:** file_cluster_11: 14.023, file_cluster_8: 14.122, file_cluster_0: 14.131
- **Magnitude:** 659.94 | **LOC:** 1162 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.4755%), Tech Debt (33.1644%)
**Top Internal Functions/Classes:**
  * `A010` (Impact: 32.5)
  * `SM010` (Impact: 30.8)
  * `PM010` (Impact: 16.1)
  * `DAD010` (Impact: 15.5)
  * `GAD010` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 47`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 492`, `dead_code: 10`, `orphaned_logic: 13`
* *Architecture:* `io: 3`, `api: 1`, `import: 4`
* *Defense:* `safety: 29`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, DFHAID, BNK1DAM, INQACC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/CREACC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.735 IQR)
- **Top Global Matches:** file_cluster_8: 12.735, file_cluster_13: 12.819, file_cluster_11: 12.894
- **Magnitude:** 573.8 | **LOC:** 1248 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.9086%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `FNA010` (Impact: 30.0)
  * `CD010` (Impact: 23.9)
  * `REQUIRED-SORT-CODE2` (Impact: 20.8)
  * `WAD010` (Impact: 9.9)
  * `ATC010` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 74`, `args: 1`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 377`, `dead_code: 3`
* *Architecture:* `io: 18`, `api: 27`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 20`, `doc: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` SORTCODE, ACCTCTRL, INQCUST, CREACC, ACCOUNT, INQACCCU, ACCDB2, PROCTRAN...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/ProcessedTransaction.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.144 IQR)
- **Top Global Matches:** file_cluster_8: 11.144, file_cluster_13: 11.515, file_cluster_7: 11.722
- **Magnitude:** 514.9 | **LOC:** 1012 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.7925%), Tech Debt (73.607%)
**Top Internal Functions/Classes:**
  * `getProcessedTransactions` (Impact: 29.0)
  * `sortOutDateTimeTaskString` (Impact: 18.9)
  * `writeDeleteCustomer` (Impact: 16.4)
  * `writeCreateCustomer` (Impact: 13.4)
  * `writeCreateAccount` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 99`, `args: 57`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 165`, `duplicate_logic: 11`
* *Architecture:* `io: 2`, `api: 55`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.002037
  * `Imports (Out-Degree: 2):` com.ibm.cics.cip.bankliberty.api.json.HBankDataAccess, java.sql.PreparedStatement, java.util.logging.Level, java.math.RoundingMode, com.ibm.cics.server.Task, com.ibm.cics.cip.bankliberty.datainterfaces.PROCTRAN, java.math.BigDecimal, java.sql.ResultSet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mvnw` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.007 IQR)
- **Top Global Matches:** file_cluster_4: 13.007, file_cluster_11: 13.512, file_cluster_12: 13.606
- **Magnitude:** 510.58 | **LOC:** 312 | **CtrlFlow:** 90.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9773%), Tech Debt (99.9928%)
**Top Internal Functions/Classes:**
  * `find_maven_basedir_[Truncated]` (Impact: 186.9)
    * *Intent:* # traverses directory structure from process work directory to filesystem root # first directory wit...
  * `Anonymous_Block` (Impact: 28.2)
    * *Intent:* # For Mingw, ensure paths are in UNIX format before anything is touched
  * `Anonymous_Block` (Impact: 15.6)
  * `Anonymous_Block` (Impact: 14.2)
  * `Anonymous_Block` (Impact: 13.6)
    * *Intent:* # # Required ENV vars: # ------------------ # JAVA_HOME - location of a JDK home dir # # Optional EN...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 25`, `args: 7`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 141`, `dead_code: 1`, `duplicate_logic: 9`, `orphaned_logic: 2`
* *Architecture:* `io: 23`, `api: 5`, `concurrency: 54`, `import: 2`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mavenrc, .mavenrc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CCA.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.896 IQR)
- **Top Global Matches:** file_cluster_11: 13.896, file_cluster_8: 14.012, file_cluster_13: 14.018
- **Magnitude:** 489.78 | **LOC:** 956 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.7186%), Tech Debt (39.8889%)
**Top Internal Functions/Classes:**
  * `GCD010` (Impact: 39.0)
    * *Intent:* * * Preserve the RESP and RESP2, then set up the * standard ABEND info before getting the applid, * ...
  * `SM010` (Impact: 28.5)
    * *Intent:* * * Empty the account numbers in the on screen array *
  * `A010` (Impact: 24.2)
  * `RM010` (Impact: 7.5)
  * `STM010` (Impact: 7.5)
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

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.091 IQR)
- **Top Global Matches:** file_cluster_8: 11.091, file_cluster_13: 11.343, file_cluster_0: 11.635
- **Magnitude:** 473.28 | **LOC:** 1362 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.7101%), Tech Debt (97.8314%)
**Top Internal Functions/Classes:**
  * `createAccount` (Impact: 42.0)
  * `updateThis` (Impact: 25.1)
  * `getAccount` (Impact: 24.1)
  * `try` (Impact: 19.6)
  * `deleteAccount` (Impact: 19.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 79`, `args: 52`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 100`, `duplicate_logic: 16`
* *Architecture:* `io: 11`, `api: 47`, `import: 12`
* *Defense:* `safety: 15`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.465
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.003666
  * `Imports (Out-Degree: 2):` com.ibm.cics.cip.bankliberty.api.json.HBankDataAccess, java.sql.PreparedStatement, java.util.logging.Level, com.ibm.cics.server.InvalidRequestException, java.math.BigDecimal, java.sql.ResultSet, java.util.logging.Logger, java.sql.SQLException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.377 IQR)
- **Top Global Matches:** file_cluster_8: 11.377, file_cluster_0: 11.543, file_cluster_13: 11.588
- **Magnitude:** 434.98 | **LOC:** 1231 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (50.7939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteCustomerInternal` (Impact: 68.8)
  * `createCustomerInternal` (Impact: 51.2)
  * `getCustomersSurnameInternal` (Impact: 9.0)
  * `getCustomersAgeInternal` (Impact: 9.0)
  * `getCustomersTownInternal` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 138`, `args: 51`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 219`
* *Architecture:* `io: 9`, `api: 30`, `import: 24`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.211
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.004073
  * `Imports (Out-Degree: 1):` jakarta.ws.rs.QueryParam, jakarta.ws.rs.core.MediaType, jakarta.ws.rs.DELETE, java.util.logging.Level, jakarta.ws.rs.Path, jakarta.ws.rs.PUT, jakarta.ws.rs.Consumes, java.sql.Date...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/INQACC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.963 IQR)
- **Top Global Matches:** file_cluster_8: 12.963, file_cluster_11: 12.978, file_cluster_13: 13.016
- **Magnitude:** 433.58 | **LOC:** 1003 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.7458%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AH010` (Impact: 22.6)
  * `RAD010` (Impact: 20.3)
  * `FD010` (Impact: 13.2)
    * *Intent:* *
  * `A010` (Impact: 10.7)
  * `GLAD010` (Impact: 10.0)
    * *Intent:* * * Preserve the RESP and RESP2, then set up the * standard ABEND info before getting the applid, * ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 66`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 300`, `dead_code: 5`
* *Architecture:* `io: 17`, `api: 15`, `import: 6`
* *Defense:* `safety: 21`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` SORTCODE, INQACC, ACCOUNT, ACCDB2, SQLCA, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQACCCU.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.149 IQR)
- **Top Global Matches:** file_cluster_11: 13.149, file_cluster_13: 13.175, file_cluster_0: 13.243
- **Magnitude:** 384.52 | **LOC:** 883 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.0591%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RAD010` (Impact: 27.6)
    * *Intent:* *
  * `FD010` (Impact: 22.7)
    * *Intent:* *
  * `AH010` (Impact: 19.5)
  * `CC010` (Impact: 9.4)
    * *Intent:* * * Evaluate the Abend code that is returned
  * `CFSDD010` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 58`, `args: 1`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 250`, `dead_code: 5`
* *Architecture:* `io: 15`, `api: 12`, `import: 8`
* *Defense:* `safety: 25`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` SORTCODE, INQCUST, ACCOUNT, INQACCCU, ACCDB2, CUSTOMER, SQLCA, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.579 IQR)
- **Top Global Matches:** file_cluster_8: 10.579, file_cluster_13: 10.729, file_cluster_7: 11.204
- **Magnitude:** 340.16 | **LOC:** 1953 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.4154%), Tech Debt (14.0827%)
**Top Internal Functions/Classes:**
  * `getCustomersBySurname` (Impact: 42.6)
  * `getCustomersByName` (Impact: 30.4)
  * `getCustomers` (Impact: 27.6)
  * `getCustomer` (Impact: 25.0)
  * `getCustomersByNameCountOnly` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 131`, `args: 35`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 50`, `duplicate_logic: 2`
* *Architecture:* `api: 29`, `import: 37`
* *Defense:* `safety: 38`, `doc: 1`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.465
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.003666
  * `Imports (Out-Degree: 4):` com.ibm.cics.server.LogicException, java.util.logging.Level, com.ibm.cics.server.DuplicateRecordException, com.ibm.cics.server.KeyedFileBrowse, com.ibm.cics.server.NoSpaceException, com.ibm.cics.server.KeyHolder, com.ibm.cics.server.LengthErrorException, com.ibm.cics.server.FileNotFoundException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/INQCUST.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.658 IQR)
- **Top Global Matches:** file_cluster_11: 13.658, file_cluster_0: 13.754, file_cluster_13: 13.808
- **Magnitude:** 331.56 | **LOC:** 712 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.6204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RCV010` (Impact: 33.6)
  * `GLCV010` (Impact: 28.8)
  * `AH010` (Impact: 17.7)
  * `P010` (Impact: 17.4)
  * `RCN010` (Impact: 4.2)
    * *Intent:* * * For a random customer generate a CUSTOMER number
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 49`, `args: 1`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 181`, `dead_code: 7`
* *Architecture:* `io: 16`, `api: 17`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 27`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` INQCUST, SORTCODE, CUSTOMER, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.095 IQR)
- **Top Global Matches:** file_cluster_8: 11.095, file_cluster_13: 11.288, file_cluster_0: 11.29
- **Magnitude:** 328.4 | **LOC:** 1765 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.8621%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createAccountInternal` (Impact: 50.2)
  * `updateAccountInternal` (Impact: 24.4)
  * `getAccountInternal` (Impact: 17.8)
  * `debitAccountInternal` (Impact: 7.4)
  * `createAccountExternal` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 120`, `args: 42`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 173`
* *Architecture:* `io: 8`, `api: 28`, `import: 21`
* *Defense:* `safety: 6`, `doc: 10`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.211
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.004073
  * `Imports (Out-Degree: 1):` jakarta.ws.rs.QueryParam, jakarta.ws.rs.core.MediaType, jakarta.ws.rs.DELETE, java.util.logging.Level, jakarta.ws.rs.Path, jakarta.ws.rs.PUT, jakarta.ws.rs.Consumes, java.io.IOException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/DBCRFUN.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.737 IQR)
- **Top Global Matches:** file_cluster_11: 14.737, file_cluster_0: 14.802, file_cluster_17: 14.811
- **Magnitude:** 301.44 | **LOC:** 862 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.3695%), Tech Debt (75.0186%)
**Top Internal Functions/Classes:**
  * `WTPD010` (Impact: 22.9)
  * `AH010` (Impact: 19.7)
  * `UAD010` (Impact: 19.6)
  * `CFSDD010` (Impact: 9.0)
  * `COMM-ACT-BAL` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 47`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 192`, `dead_code: 14`, `orphaned_logic: 17`
* *Architecture:* `io: 11`, `api: 1`, `import: 8`
* *Defense:* `safety: 23`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` SORTCODE, ACCOUNT, ACCDB2, PAYDBCR, PROCTRAN, SQLCA, PROCDB2, ABNDINFO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/CustomerControl.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.831 IQR)
- **Top Global Matches:** file_cluster_8: 9.831, file_cluster_7: 10.164, file_cluster_1: 10.521
- **Magnitude:** 262.56 | **LOC:** 518 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.1592%), Tech Debt (28.8526%)
**Top Internal Functions/Classes:**
  * `setCustomerControlEyecatcher` (Impact: 5.0)
    * *Intent:* * </pre> */
  * `setCustomerControlSortcode` (Impact: 5.0)
  * `setCustomerControlNumber` (Impact: 5.0)
  * `setNumberOfCustomers` (Impact: 5.0)
  * `setLastCustomerNumber` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 44`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 37`, `duplicate_logic: 2`
* *Architecture:* `api: 95`
* *Defense:* `doc: 17`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.685
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003621
  * `Imports (Out-Degree: 0):` com.ibm.jzos.fields.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/AccountEnquiryForm.java` (JAVA) | Magnitude: 19.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 23, api: 9, structural_boundaries: 7, args: 5
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionTransferLocalJSON.java` (JAVA) | Magnitude: 16.8 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 10, api: 5, args: 4
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountJSON.java` (JAVA) | Magnitude: 117.9 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 137, api: 39, structural_boundaries: 34, args: 24
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/customerenquiry/CustomerEnquiryForm.java` (JAVA) | Magnitude: 19.6 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, api: 9, structural_boundaries: 7, args: 5
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerJSON.java` (JAVA) | Magnitude: 95.32 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 119, structural_boundaries: 30, api: 27, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/base/cobol_src/BNK1CCS.cbl` (COBOL) | Magnitude: 1169.78 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1164, state_mutation: 866, branch: 191, structural_boundaries: 92
- `src/base/cobol_src/BNK1CRA.cbl` (COBOL) | Magnitude: 668.68 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 794, state_mutation: 493, branch: 97, reflection_metaprogramming: 45
- `src/base/cobol_src/INQACCCU.cbl` (COBOL) | Magnitude: 384.52 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 571, state_mutation: 250, branch: 65, structural_boundaries: 58
- `src/base/cobol_src/BNK1TFN.cbl` (COBOL) | Magnitude: 720.76 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 833, state_mutation: 537, branch: 102, structural_boundaries: 52
- `src/base/cobol_src/UPDCUST.cbl` (COBOL) | Magnitude: 167.16 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 208, state_mutation: 100, branch: 33, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/CustomerServices.java` (JAVA) | Magnitude: 7.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 8, import: 5, api: 2
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/PaymentInterface.java` (JAVA) | Magnitude: 7.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 8, import: 5, api: 2
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/listaccounts/ListAccJson.java` (JAVA) | Magnitude: 15.56 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 9, api: 7, args: 3
- `src/bank-application-frontend/src/App.js` (JAVASCRIPT) | Magnitude: 15.66 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 73, ui_framework: 30, structural_boundaries: 22, io: 18
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java` (JAVA) | Magnitude: 110.26 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 155, structural_boundaries: 28, branch: 22, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/bank-application-frontend/src/content/CustomerDeletePage/CustomerDeletePage.js` (JAVASCRIPT) | Magnitude: 106.42 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 137, concurrency: 37, ui_framework: 29, structural_boundaries: 26
- `src/bank-application-frontend/src/content/CustomerDeletePage/CustomerDeleteTables.js` (JAVASCRIPT) | Magnitude: 109.12 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 254, structural_boundaries: 47, concurrency: 43, ui_framework: 41
- `src/bank-application-frontend/src/content/CustomerDetailsPage/CustomerDetailsPage.js` (JAVASCRIPT) | Magnitude: 146.3 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 195, concurrency: 38, structural_boundaries: 34, ui_framework: 32
- `src/bank-application-frontend/src/content/AccountDetailsPage/AccountDetailsTable.js` (JAVASCRIPT) | Magnitude: 76.3 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 260, ui_framework: 36, func_start: 32, structural_boundaries: 30
- `src/bank-application-frontend/src/content/AccountCreationPage/AccountCreationPage.js` (JAVASCRIPT) | Magnitude: 101.3 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 231, ui_framework: 43, func_start: 31, structural_boundaries: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/bank-application-frontend/src/content/AccountDeletePage/AccountDeleteTables.js` (JAVASCRIPT) | Magnitude: 188.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 333, concurrency: 74, structural_boundaries: 46, ui_framework: 36
- `mvnw` (SHELL) | Magnitude: 510.58 | Delta: **0.505 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 229, indent_spaces: 169, state_mutation: 141, concurrency: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/base/cobol_src/INQACC.cbl` (COBOL) | Magnitude: 433.58 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 664, state_mutation: 300, structural_boundaries: 66, branch: 56
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java` (JAVA) | Magnitude: 22.92 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 11, api: 7, args: 4
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/JsonPropertyNamingStrategy.java` (JAVA) | Magnitude: 22.92 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 11, api: 7, args: 4
- `src/base/cobol_src/BNKMENU.cbl` (COBOL) | Magnitude: 725.64 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 847, state_mutation: 533, branch: 104, reflection_metaprogramming: 65
- `src/base/cobol_src/GETSCODE.cbl` (COBOL) | Magnitude: 8.38 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, func_start: 4, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/base/cobol_src/UPDACC.cbl` (COBOL) | Magnitude: 106.56 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 208, state_mutation: 65, structural_boundaries: 26, dead_code: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers/WebController.java` -> Churn: **100.0%** | Cog Load: 7.7861% | Debt: 99.9148%
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/controllers/WebController.java` -> Churn: **100.0%** | Cog Load: 7.7856% | Debt: 99.979%
- `src/bank-application-frontend/updateWebUI.sh` -> Churn: **63.09%** | Cog Load: 5.0% | Debt: 100.0%
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/jsonclasses/paymentinterface/TransferForm.java` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 99.2255%
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/DebitCreditAccountJSON.java` -> Churn: **63.09%** | Cog Load: 4.1722% | Debt: 99.9955%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/base/cobol_src/BNK1DCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 1217.92
- `src/base/cobol_src/BNK1CCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 1169.78
- `src/base/cobol_src/BNK1UAC.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 890.36
- `src/base/cobol_src/BNK1CAC.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 785.38
- `src/base/cobol_src/CRECUST.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 749.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.712%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.1227%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 94.6249%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 43.291%)
- `src/bank-application-frontend/src/App.js` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 27.0976%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **Severity: 1.041** (Embedded: 0.0185 * Error Risk: 56.2177%)
- `src/base/cobol_copy/PROCTRAN.cpy` -> **Severity: 0.998** (Embedded: 0.0163 * Error Risk: 61.2467%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java` -> **Severity: 0.405** (Embedded: 0.0061 * Error Risk: 66.323%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` -> **Severity: 0.361** (Embedded: 0.0041 * Error Risk: 88.7087%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.346** (Embedded: 0.0041 * Error Risk: 84.8829%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java` -> **Severity: 2497.485** (Blast Radius: 26.341 * Doc Risk: 94.8136%)
- `src/base/cobol_copy/ABNDINFO.cpy` -> **Severity: 1478.421** (Blast Radius: 24.232 * Doc Risk: 61.0111%)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **Severity: 715.022** (Blast Radius: 8.671 * Doc Risk: 82.4613%)
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/JsonPropertyNamingStrategy.java` -> **Severity: 663.506** (Blast Radius: 6.998 * Doc Risk: 94.8136%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/GetSortCode.java` -> **Severity: 446.343** (Blast Radius: 4.465 * Doc Risk: 99.9648%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
