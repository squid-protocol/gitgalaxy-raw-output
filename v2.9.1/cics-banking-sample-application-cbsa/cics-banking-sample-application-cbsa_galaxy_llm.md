# ARCHITECTURAL_BRIEF: cics-banking-sample-application-cbsa
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cicsdev/cics-banking-sample-application-cbsa.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 483 analyzed artifact(s), 44934 LOC.
- **Load-bearing artifact:** `src/base/cobol_copy/ABNDINFO.cpy` -- 26 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` -- pulls in 37 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/bank-application-frontend/.env` at magnitude 5000.0 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 801 |
| Analyzed Artifacts (Scanned) | 483 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 318 |
| Total LOC | 44934 |
| Volatility Index | 0.027 |
| % Scanned of codebase = | 60.3% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7397 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3917 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2539 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 33 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JCL | 101 | 1462 | 20.9% |
| JAVA | 80 | 13773 | 16.6% |
| COBOL | 66 | 18395 | 13.7% |
| JSON | 53 | 5224 | 11.0% |
| XML | 47 | 0 | 9.7% |
| CSS | 32 | 1158 | 6.6% |
| JAVASCRIPT | 31 | 3134 | 6.4% |
| MARKDOWN | 28 | 0 | 5.8% |
| PLAINTEXT | 15 | 1 | 3.1% |
| HTML | 13 | 702 | 2.7% |
| BMS | 9 | 667 | 1.9% |
| BATCH | 3 | 163 | 0.6% |
| SHELL | 3 | 237 | 0.6% |
| YAML | 2 | 18 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.681`
> **Composition Archetype:** `Mid Flat Project` (z +2.68; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Interface Declarations Files 17%, Declarative / Non-Code 11%, Parameter Forwarders Files 6%, Large Core Modules (3) 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 440 | 91.1% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 42 | 8.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 318*

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
- `.yml`: 10x Zero-Density Threshold (LOC: 60, Signals: 0)
- `.java`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1036 LOC), 1x Statistical Anomaly (Z-Score: -4.69 < -4.55)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.properties`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.baseline`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.9 | 10.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 25.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 73.7 | 7.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 1.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.2 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 400 | 57 | 2 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/Account.java` |
| cleanup | 43 | 14 | 0 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/Account.java` |
| guards | 1838 | 119 | 8 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` |
| danger | 790 | 102 | 2 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` |
| concurrency | 144 | 25 | 0 | `src/base/cobol_src/CRECUST.cbl` |
| connectivity | 1580 | 166 | 10 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/CRECUST.java` |
| io | 785 | 113 | 4 | `etc/install/base/installjcl/CICSTS56.jcl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 302 | 33 | 0 | `src/base/cobol_src/BNKMENU.cbl` |
| time | 148 | 38 | 0 | `src/base/cobol_src/CRECUST.cbl` |
| serialization | 771 | 30 | 0 | `src/base/cobol_copy/RESPSTR.cpy` |
| regex | 74 | 13 | 0 | `src/base/cobol_src/BNK1CAC.cbl` |
| events | 374 | 82 | 2 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` |
| tests | 3 | 1 | 0 | `src/bank-application-frontend/src/App.test.js` |
| docs | 183 | 57 | 1 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/CRECUST.java` |
| debt | 476 | 46 | 0 | `src/base/cobol_src/BANKDATA.cbl` |
| mutation | 11595 | 251 | 59 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` |
| dead_code | 887 | 83 | 5 | `src/base/cobol_src/BNK1DCS.cbl` |
| credential | 74 | 1 | 0 | `src/webui/WebContent/asset-manifest.json` |
| threat | 1030 | 55 | 1 | `src/base/cobol_src/XFRFUN.cbl` |
| ml_ai | 192 | 25 | 0 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` |
| ui | 991 | 65 | 2 | `src/base/bms_src/BNK1UAM.bms` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `etc/install/base/installjcl/CICSTS56.jcl` (Hits: 65)
- `src/base/cobol_src/BANKDATA.cbl` (Hits: 30)
- `mvnw` (Hits: 23)

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
3. **CBSA_BMS_User_Guide.md** (`etc/usage/base/doc/CBSA_BMS_User_Guide.md`) — 35 outbound dependencies
4. **CBSA_Customer_Services_Interface_User_Guide.md** (`etc/usage/springBoot/doc/CBSA_Customer_Services_Interface_User_Guide.md`) — 32 outbound dependencies
5. **CreditScoreCICS540.java** (`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CreditScoreCICS540.java`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `EIBRESP-TOSTRING` **(Defensive Guards)** (@ `src/base/cobol_copy/RESPSTR.cpy`) -> Impact: **129.8** | LOC: 236
  * *Intent:* ****************************************************************** * * * Copyright IBM Corp. 2023 * * * * * ******************************************...
- `ED010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BNK1CCS.cbl`) -> Impact: **98.8** | LOC: 355
- `CC010` **(I/O & Config Routines)** (@ `src/base/cobol_src/CRECUST.cbl`) -> Impact: **66.0** | LOC: 499
- `ED010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BNK1CAC.cbl`) -> Impact: **53.7** | LOC: 314
- `UAD010` **(I/O & Config Routines)** (@ `src/base/cobol_src/XFRFUN.cbl`) -> Impact: **43.5** | LOC: 605
- `deleteCustomerInternal` **(Compute Cores)** (@ `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java`) -> Impact: **40.9** | LOC: 168
- `createCustomerInternal` **(Compute Cores)** (@ `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java`) -> Impact: **33.6** | LOC: 219
- `IOT010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BNKMENU.cbl`) -> Impact: **33.5** | LOC: 588
- `Anonymous_Block` **(Compute Cores)** (@ `mvnw`) -> Impact: **32.5** | LOC: 71
  * *Intent:* ########################################################################################## # Extension to allow automatically downloading the maven-wr...
- `createAccount` **(Many-Argument Workhorses)** (@ `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java`) -> Impact: **31.8** | LOC: 117

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/base/cobol_src` | 29 | 9676.8 | 82.09% | 34.9% |
| `src/bank-application-frontend` | 6 | 5031.56 | 0.0% | 0.0% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json` | 19 | 1864.14 | 15.41% | 41.35% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2` | 2 | 1238.66 | 69.47% | 0.0% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces` | 7 | 867.38 | 18.5% | 28.57% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access` | 5 | 751.86 | 52.07% | 45.48% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam` | 1 | 710.36 | 56.42% | 0.0% |
| `__monolith__` | 8 | 357.22 | 12.36% | 0.0% |
| `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/updateaccount` | 3 | 263.08 | 36.84% | 33.33% |
| `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers` | 2 | 225.6 | 3.15% | 39.28% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/InqaccJson.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createaccount/CreaccJson.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/deletecustomer/DelcusJson.java` -> **100.0%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createcustomer/CrecustJson.java` -> **99.9999%** Exposure
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/customerenquiry/InqCustZJson.java` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `mvnw` -> **100.0%** Exposure
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/ProcessedTransaction.java` -> **100.0%** Exposure
- `src/bank-application-frontend/src/components/Admin-Header/Admin-Header.js` -> **100.0%** Exposure
- `src/bank-application-frontend/src/components/Homepage-Header/Homepage-Header.js` -> **100.0%** Exposure
- `src/base/cobol_copy/RESPSTR.cpy` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/deleteaccount/DelaccJson.java` -> **39** Orphaned Functions | **0** Duplicates
- `src/base/cobol_src/BNK1DCS.cbl` -> **31** Orphaned Functions | **0** Duplicates
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/accountenquiry/InqaccJson.java` -> **29** Orphaned Functions | **0** Duplicates
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createaccount/CreaccJson.java` -> **26** Orphaned Functions | **0** Duplicates
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/updateaccount/UpdaccJson.java` -> **25** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `974` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/bank-application-frontend/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CCS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 910.68 | **LOC:** 1661 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Complexity Load (formerly Cognitive Load) (97.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ED010` **(I/O & Config Routines)** (Impact: 98.8)
  * `A010` **(I/O & Config Routines)** (Impact: 15.9)
  * `SM010` **(I/O & Config Routines)** (Impact: 15.0)
  * `CCD010` **(I/O & Config Routines)** (Impact: 12.0)
  * `RM010` **(I/O & Config Routines)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 165 instances
* *State Mutation (weighted view):* 686
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 134`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 356`, `dead_code: 9`, `unreferenced_by_name: 22`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1CCM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1DCS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 892.12 | **LOC:** 2057 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.7%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A010` **(I/O & Config Routines)** (Impact: 19.9)
  * `ED2010` **(I/O & Config Routines)** (Impact: 19.1)
  * `SM010` **(I/O & Config Routines)** (Impact: 15.0)
  * `PM010` **(I/O & Config Routines)** (Impact: 14.5)
  * `UPDCD010` **(I/O & Config Routines)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 681
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 108`, `args: 1`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 463`, `dead_code: 21`, `unreferenced_by_name: 31`
* *Architecture:* `io: 2`, `api: 1`, `import: 7`
* *Defense:* `safety: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1DCM, DELCUS, DFHAID, DFHBMSCA, INQCUST, UPDCUST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 754.38 | **LOC:** 1765 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 3.175; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.3%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateNewAccount` **(Compute Cores)** (Impact: 28.1)
  * `createAccountInternal` **(Compute Cores)** (Impact: 27.1)
  * `updateAccountInternal` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `getAccountsInternal` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `debitCreditAccount` **(Many-Argument Workhorses)** (Impact: 17.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 120 instances
* *State Mutation (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 191`, `args: 81`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 288`, `dead_code: 2`
* *Architecture:* `io: 10`, `api: 37`, `import: 21`
* *Defense:* `safety: 14`, `doc: 10`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.175
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.004049
  * `Imports (Out-Degree: 1):` com.ibm.cics.cip.bankliberty.web.db2.Account, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.Task, com.ibm.json.java.JSONArray, com.ibm.json.java.JSONObject, jakarta.ws.rs.Consumes, jakarta.ws.rs.DELETE, jakarta.ws.rs.GET...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 710.36 | **LOC:** 1953 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 4.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Complexity Load (formerly Cognitive Load) (56.4%), Connectivity (formerly Api Exposure) (22.1%)
- **Documentation Coverage:** 97.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCustomer` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `createCustomer` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `deleteCustomer` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `getCustomersByName` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `getCustomersByName` **(Many-Argument Workhorses)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 251`, `args: 50`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 257`
* *Architecture:* `api: 32`, `import: 37`
* *Defense:* `safety: 96`, `doc: 1`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.414
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.003644
  * `Imports (Out-Degree: 4):` com.ibm.cics.cip.bankliberty.api.json.CreditScore, com.ibm.cics.cip.bankliberty.api.json.CustomerJSON, com.ibm.cics.cip.bankliberty.datainterfaces.CUSTOMER, com.ibm.cics.cip.bankliberty.datainterfaces.CustomerControl, com.ibm.cics.server.ChangedException, com.ibm.cics.server.DuplicateKeyException, com.ibm.cics.server.DuplicateRecordException, com.ibm.cics.server.EndOfFileException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 688.56 | **LOC:** 1362 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 4.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createAccount` **(Many-Argument Workhorses)** (Impact: 31.8)
  * `getNextMonth` **(Compute Cores)** (Impact: 30.5)
  * `getAccount` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `getAccountsByBalance` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `deleteAccount` **(Many-Argument Workhorses)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 125`, `args: 74`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 151`
* *Architecture:* `io: 17`, `api: 41`, `import: 12`
* *Defense:* `safety: 30`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.414
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.003644
  * `Imports (Out-Degree: 2):` com.ibm.cics.cip.bankliberty.api.json.AccountJSON, com.ibm.cics.cip.bankliberty.api.json.HBankDataAccess, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.Task, java.math.BigDecimal, java.sql.Date, java.sql.PreparedStatement, java.sql.ResultSet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/BNK1UAC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 665.66 | **LOC:** 1409 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Complexity Load (formerly Cognitive Load) (95.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VD010` **(I/O & Config Routines)** (Impact: 28.5)
  * `A010` **(I/O & Config Routines)** (Impact: 16.9)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `WS-CONVERTED-VAL2` **(I/O & Config Routines)** (Impact: 11.9)
  * `IAD010` **(I/O & Config Routines)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 105 instances
* *State Mutation (weighted view):* 514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 69`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 304`, `dead_code: 14`, `unreferenced_by_name: 19`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1UAM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/CRECUST.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 659.38 | **LOC:** 1498 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.3%), Guard Balance (formerly Safety Score) (89.9%), Concurrency Surface (formerly Concurrency) (84.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CC010` **(I/O & Config Routines)** (Impact: 66.0)
  * `P010` **(I/O & Config Routines)** (Impact: 17.7)
  * `GLCV010` **(I/O & Config Routines)** (Impact: 14.7)
  * `WCV010` **(I/O & Config Routines)** (Impact: 10.2)
  * `WPD010` **(I/O & Config Routines)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 95 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 395
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 114`, `args: 6`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 205`, `dead_code: 13`, `fragile_debt: 1`
* *Architecture:* `io: 22`, `api: 27`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 22`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ABNDINFO, CEEIGZCT, CRECUST, CUSTCTRL, CUSTOMER, PROCDB2, PROCTRAN, SORTCODE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CAC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 616.98 | **LOC:** 1302 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Guard Balance (formerly Safety Score) (95.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ED010` **(I/O & Config Routines)** (Impact: 53.7)
  * `CAD010` **(I/O & Config Routines)** (Impact: 26.3)
  * `A010` **(I/O & Config Routines)** (Impact: 16.4)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `RM010` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 454
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 76`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 246`, `dead_code: 10`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1CAM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BANKDATA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 597.18 | **LOC:** 1464 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.4%), Complexity Load (formerly Cognitive Load) (90.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DBR010` **(I/O & Config Routines)** (Impact: 31.7)
  * `HV-ACCOUNT-ACTUAL-BALANCE` **(I/O & Config Routines)** (Impact: 11.2)
  * `ACCOUNT-OVERDRAFT-COUNT` **(I/O & Config Routines)** (Impact: 6.5)
  * `PA010` **(I/O & Config Routines)** (Impact: 4.5)
  * `CUSTOMER-BIRTH-YEAR` **(I/O & Config Routines)** (Impact: 4.4)
    * *Intent:* * FUNCTION RANDOM) +
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 467
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 108`, `args: 3`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 377`, `dead_code: 3`, `unreferenced_by_name: 19`
* *Architecture:* `io: 30`, `api: 1`, `import: 7`
* *Defense:* `safety: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ACCDB2, ACCTCTRL, CONTDB2, CUSTCTRL, CUSTOMER, SORTCODE, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/ProcessedTransaction.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 550.1 | **LOC:** 1012 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 2.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.4%), Guard Balance (formerly Safety Score) (91.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getProcessedTransactions` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `writeDeleteCustomer` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `sortOutDateTimeTaskString` **(I/O & Config Routines)** (Impact: 10.9)
  * `writeCreateCustomer` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `sortOutCustomerDOB` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 99`, `args: 57`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 207`
* *Architecture:* `io: 2`, `api: 42`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.445
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.002024
  * `Imports (Out-Degree: 2):` com.ibm.cics.cip.bankliberty.api.json.HBankDataAccess, com.ibm.cics.cip.bankliberty.datainterfaces.PROCTRAN, com.ibm.cics.server.Task, java.math.BigDecimal, java.math.RoundingMode, java.sql.Date, java.sql.PreparedStatement, java.sql.ResultSet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/XFRFUN.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 549.94 | **LOC:** 1925 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.7%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UAD010` **(I/O & Config Routines)** (Impact: 43.5)
  * `UADT010` **(I/O & Config Routines)** (Impact: 23.5)
  * `COMM-AMT` **(I/O & Config Routines)** (Impact: 16.5)
  * `AH010` **(I/O & Config Routines)** (Impact: 14.7)
  * `UADF010` **(I/O & Config Routines)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 103`, `args: 1`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 230`, `dead_code: 23`
* *Architecture:* `io: 19`, `api: 18`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ABNDINFO, ACCDB2, ACCOUNT, PROCDB2, PROCTRAN, SORTCODE, SQLCA, XFRFUN
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1TFN.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 517.96 | **LOC:** 1228 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (95.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GCD010` **(I/O & Config Routines)** (Impact: 19.9)
  * `WS-NUM-COUNT-MINUS` **(I/O & Config Routines)** (Impact: 14.0)
  * `A010` **(I/O & Config Routines)** (Impact: 13.7)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `VA010` **(I/O & Config Routines)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 385
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 75`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 217`, `dead_code: 9`, `unreferenced_by_name: 16`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1TFM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1DAC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 484.74 | **LOC:** 1162 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Guard Balance (formerly Safety Score) (94.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A010` **(I/O & Config Routines)** (Impact: 19.4)
  * `SM010` **(I/O & Config Routines)** (Impact: 15.0)
  * `DAD010` **(I/O & Config Routines)** (Impact: 11.5)
  * `GAD010` **(I/O & Config Routines)** (Impact: 11.0)
  * `PM010` **(I/O & Config Routines)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 73`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 235`, `dead_code: 10`, `unreferenced_by_name: 18`
* *Architecture:* `io: 3`, `api: 1`, `import: 4`
* *Defense:* `safety: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1DAM, DFHAID, INQACC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CRA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 483.88 | **LOC:** 1170 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VA010` **(I/O & Config Routines)** (Impact: 19.5)
  * `UCD010` **(I/O & Config Routines)** (Impact: 17.9)
  * `A010` **(I/O & Config Routines)** (Impact: 15.4)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `ED010` **(I/O & Config Routines)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 59`, `args: 1`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 191`, `dead_code: 8`, `unreferenced_by_name: 16`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1CDM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/CREACC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 454.4 | **LOC:** 1248 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FNA010` **(I/O & Config Routines)** (Impact: 23.5)
  * `CD010` **(I/O & Config Routines)** (Impact: 23.2)
  * `REQUIRED-SORT-CODE2` **(I/O & Config Routines)** (Impact: 10.4)
  * `ATC010` **(I/O & Config Routines)** (Impact: 8.8)
  * `WAD010` **(I/O & Config Routines)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 99`, `args: 1`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 197`, `dead_code: 3`
* *Architecture:* `io: 18`, `api: 26`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ABNDINFO, ACCDB2, ACCOUNT, ACCTCTRL, CREACC, CUSTOMER, INQACCCU, INQCUST...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 452.08 | **LOC:** 1231 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 3.175; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deleteCustomerInternal` **(Compute Cores)** (Impact: 40.9)
  * `createCustomerInternal` **(Compute Cores)** (Impact: 33.6)
  * `getCustomersSurnameInternal` **(Compute Cores)** (Impact: 6.5)
  * `getCustomersAgeInternal` **(Compute Cores)** (Impact: 6.5)
  * `getCustomersTownInternal` **(Compute Cores)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 138`, `args: 51`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 153`
* *Architecture:* `io: 9`, `api: 30`, `import: 24`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.175
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.004049
  * `Imports (Out-Degree: 1):` com.ibm.cics.cip.bankliberty.web.vsam.Customer, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.Task, com.ibm.json.java.JSONArray, com.ibm.json.java.JSONObject, jakarta.ws.rs.Consumes, jakarta.ws.rs.DELETE, jakarta.ws.rs.GET...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/BNKMENU.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 447.34 | **LOC:** 1315 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.7%), Guard Balance (formerly Safety Score) (89.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOT010` **(I/O & Config Routines)** (Impact: 33.5)
  * `SMM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `A010` **(I/O & Config Routines)** (Impact: 12.2)
  * `RMM010` **(I/O & Config Routines)** (Impact: 7.5)
  * `STM010` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 67`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 225`, `dead_code: 6`, `unreferenced_by_name: 17`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1MAI, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQACC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 343.88 | **LOC:** 1003 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Guard Balance (formerly Safety Score) (85.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AH010` **(I/O & Config Routines)** (Impact: 17.4)
  * `RAD010` **(I/O & Config Routines)** (Impact: 15.3)
  * `FD010` **(I/O & Config Routines)** (Impact: 11.0)
  * `GLAD010` **(I/O & Config Routines)** (Impact: 7.5)
  * `CFSDCD010` **(I/O & Config Routines)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 82`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 144`, `dead_code: 5`
* *Architecture:* `io: 14`, `api: 19`, `import: 6`
* *Defense:* `safety: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ABNDINFO, ACCDB2, ACCOUNT, INQACC, SORTCODE, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CCA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 341.58 | **LOC:** 956 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Guard Balance (formerly Safety Score) (89.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GCD010` **(I/O & Config Routines)** (Impact: 26.4)
  * `A010` **(I/O & Config Routines)** (Impact: 13.7)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `RM010` **(I/O & Config Routines)** (Impact: 4.0)
  * `STM010` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 60`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 142`, `dead_code: 9`, `unreferenced_by_name: 16`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ABNDINFO, BNK1ACC, DFHAID, INQACCCU
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mvnw` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 308.9 | **LOC:** 312 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.716; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (98.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Compute Cores)** (Impact: 32.5)
    * *Intent:* ########################################################################################## # Extensi...
  * `Anonymous_Block` **(Compute Cores)** (Impact: 8.9)
  * `find_maven_basedir` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* # traverses directory structure from process work directory to filesystem root # first directory wit...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 7.2)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 231`, `args: 7`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 47`, `dead_code: 1`
* *Architecture:* `io: 23`, `api: 5`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .mavenrc, mavenrc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQACCCU.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 269.52 | **LOC:** 883 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RAD010` **(I/O & Config Routines)** (Impact: 16.8)
  * `AH010` **(I/O & Config Routines)** (Impact: 14.8)
  * `FD010` **(I/O & Config Routines)** (Impact: 14.5)
  * `CFSDD010` **(I/O & Config Routines)** (Impact: 7.2)
  * `CC010` **(I/O & Config Routines)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 80`, `args: 1`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 99`, `dead_code: 5`
* *Architecture:* `io: 12`, `api: 15`, `import: 8`
* *Defense:* `safety: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ABNDINFO, ACCDB2, ACCOUNT, CUSTOMER, INQACCCU, INQCUST, SORTCODE, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQCUST.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 264.56 | **LOC:** 712 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.5%), Guard Balance (formerly Safety Score) (82.9%), Connectivity (formerly Api Exposure) (60.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RCV010` **(I/O & Config Routines)** (Impact: 21.2)
  * `GLCV010` **(I/O & Config Routines)** (Impact: 18.2)
  * `AH010` **(I/O & Config Routines)** (Impact: 12.9)
  * `P010` **(I/O & Config Routines)** (Impact: 10.7)
  * `RCN010` **(I/O & Config Routines)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 69`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 75`, `dead_code: 7`
* *Architecture:* `io: 22`, `api: 18`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ABNDINFO, CUSTOMER, INQCUST, SORTCODE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/Account.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 250.18 | **LOC:** 586 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.716; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateThis` **(Type Conversions)** (Impact: 6.5)
  * `addToDB` **(Type Conversions)** (Impact: 5.5)
  * `deleteFromDB` **(Type Conversions)** (Impact: 5.0)
  * `inDB` **(Type Conversions)** (Impact: 5.0)
  * `setNextStatement` **(Compute Cores)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 60`, `args: 42`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 95`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 31`, `import: 12`
* *Defense:* `safety: 10`, `immutability_locks: 10`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` com.ibm.cics.cip.bankliberty.api.json.AccountJSON, com.ibm.cics.cip.bankliberty.api.json.AccountsResource, com.ibm.json.java.JSONObject, jakarta.ws.rs.core.Response, java.io.IOException, java.math.BigDecimal, java.math.RoundingMode, java.sql.Date...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/CustomerControl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 241.76 | **LOC:** 518 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 2.654; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setCustomerControlEyecatcher` **(Parameter Forwarders)** (Impact: 3.4)
  * `setCustomerControlSortcode` **(Compute Cores)** (Impact: 3.4)
  * `setCustomerControlNumber` **(Compute Cores)** (Impact: 3.4)
  * `setNumberOfCustomers` **(Compute Cores)** (Impact: 3.4)
  * `setLastCustomerNumber` **(Compute Cores)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 44`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 41`
* *Architecture:* `api: 70`
* *Defense:* `doc: 17`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.654
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003599
  * `Imports (Out-Degree: 0):` com.ibm.jzos.fields.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/DebitCreditAccountJSON.java` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 81.7574%
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionAccountJSON.java` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 99.9998%
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionCreateCustomerJSON.java` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 99.9998%
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionDebitCreditJSON.java` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 81.7574%
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/ProcessedTransactionDeleteCustomerJSON.java` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 99.9998%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/base/cobol_src/BNK1CCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 910.68
- `src/base/cobol_src/BNK1DCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 892.12
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 710.36
- `src/base/cobol_src/BNK1UAC.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 665.66
- `src/base/cobol_src/CRECUST.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 659.38

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9881%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9635%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.999%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.978%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/SortCodeResource.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 72.7164%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **Severity: 0.999** (Embedded: 0.0184 * Error Risk: 54.2752%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java` -> **Severity: 0.457** (Embedded: 0.0061 * Error Risk: 75.2679%)
- `src/bank-application-frontend/src/components/Homepage-Header/Homepage-Header.js` -> **Severity: 0.386** (Embedded: 0.0046 * Error Risk: 84.6433%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.38** (Embedded: 0.004 * Error Risk: 93.8746%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` -> **Severity: 0.375** (Embedded: 0.004 * Error Risk: 92.6224%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java` -> **Severity: 2604.1** (Blast Radius: 26.041 * Doc Risk: 100.0%)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **Severity: 857.2** (Blast Radius: 8.572 * Doc Risk: 100.0%)
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/JsonPropertyNamingStrategy.java` -> **Severity: 494.214** (Blast Radius: 6.919 * Doc Risk: 71.4286%)
- `src/base/cobol_copy/PROCTRAN.cpy` -> **Severity: 493.7** (Blast Radius: 4.937 * Doc Risk: 100.0%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java` -> **Severity: 463.1** (Blast Radius: 4.631 * Doc Risk: 100.0%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
