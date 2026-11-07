# ARCHITECTURAL_BRIEF: cics-banking-sample-application-cbsa
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cicsdev/cics-banking-sample-application-cbsa.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 485 analyzed artifact(s), 45263 LOC.
- **Load-bearing artifact:** `etc/install/base/installjcl/CICSTS56.jcl` -- 29 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 485 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 316 |
| Total LOC | 45263 |
| Volatility Index | 0.027 |
| % Scanned of codebase = | 60.5% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7515 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3548 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7077 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 42 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JCL | 101 | 1462 | 20.8% |
| JAVA | 81 | 13778 | 16.7% |
| COBOL | 66 | 18335 | 13.6% |
| JSON | 53 | 5224 | 10.9% |
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
| CSD | 1 | 384 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 484 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Interface Declarations Files 17%, Declarative / Non-Code 12%, Parameter Forwarders Files 6%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 442 | 91.1% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 42 | 8.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 316*

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
- `.java`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1036 LOC)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.properties`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.baseline`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.9 | 9.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.1 | 20.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 73.7 | 7.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 1.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.2 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.5 | 93.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 353 | 55 | 2 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/Account.java` |
| cleanup | 41 | 14 | 0 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/Account.java` |
| guards | 1838 | 119 | 8 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` |
| danger | 790 | 102 | 2 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` |
| concurrency | 144 | 25 | 0 | `src/base/cobol_src/CRECUST.cbl` |
| connectivity | 1601 | 168 | 10 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/CRECUST.java` |
| io | 697 | 112 | 4 | `etc/install/base/installjcl/CICSTS56.jcl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 302 | 33 | 0 | `src/base/cobol_src/BNKMENU.cbl` |
| time | 128 | 38 | 0 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` |
| serialization | 392 | 29 | 0 | `src/base/cobol_src/BNK1DCS.cbl` |
| regex | 74 | 13 | 0 | `src/base/cobol_src/BNK1CAC.cbl` |
| events | 374 | 82 | 2 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` |
| tests | 3 | 1 | 0 | `src/bank-application-frontend/src/App.test.js` |
| docs | 183 | 57 | 1 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/CRECUST.java` |
| debt | 268 | 45 | 0 | `src/base/cobol_src/XFRFUN.cbl` |
| mutation | 11658 | 252 | 60 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` |
| dead_code | 670 | 73 | 3 | `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/deleteaccount/DelaccJson.java` |
| credential | 74 | 1 | 0 | `src/webui/WebContent/asset-manifest.json` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 192 | 25 | 0 | `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` |
| ui | 991 | 65 | 2 | `src/base/bms_src/BNK1UAM.bms` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `etc/install/base/installjcl/CICSTS56.jcl` (Hits: 65)
- `mvnw` (Hits: 23)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers/WebController.java` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CICSTS56.jcl** (`etc/install/base/installjcl/CICSTS56.jcl`) — 29 inbound connections
2. **ABNDINFO.cpy** (`src/base/cobol_copy/ABNDINFO.cpy`) — 26 inbound connections
3. **ABNDPROC.cbl** (`src/base/cobol_src/ABNDPROC.cbl`) — 23 inbound connections
4. **JsonPropertyNamingStrategy.java** (`src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java`) — 22 inbound connections
5. **SORTCODE.cpy** (`src/base/cobol_copy/SORTCODE.cpy`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Customer.java** (`src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java`) — 37 outbound dependencies
2. **WebController.java** (`src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers/WebController.java`) — 36 outbound dependencies
3. **CBSA_BMS_User_Guide.md** (`etc/usage/base/doc/CBSA_BMS_User_Guide.md`) — 35 outbound dependencies
4. **CBSA_Customer_Services_Interface_User_Guide.md** (`etc/usage/springBoot/doc/CBSA_Customer_Services_Interface_User_Guide.md`) — 32 outbound dependencies
5. **BANK.csd** (`etc/install/base/installjcl/BANK.csd`) — 30 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `EIBRESP-TOSTRING` **(Defensive Guards)** (@ `src/base/cobol_copy/RESPSTR.cpy`) -> Impact: **129.8** | LOC: 236
  * *Intent:* ****************************************************************** * * * Copyright IBM Corp. 2023 * * * * * ******************************************...
- `ED010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BNK1CCS.cbl`) -> Impact: **98.8** | LOC: 355
- `CC010` **(I/O & Config Routines)** (@ `src/base/cobol_src/CRECUST.cbl`) -> Impact: **66.0** | LOC: 499
- `ED010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BNK1CAC.cbl`) -> Impact: **53.7** | LOC: 314
- `UAD010` **(I/O & Config Routines)** (@ `src/base/cobol_src/XFRFUN.cbl`) -> Impact: **43.5** | LOC: 605
- `UADT010` **(I/O & Config Routines)** (@ `src/base/cobol_src/XFRFUN.cbl`) -> Impact: **35.5** | LOC: 516
- `IOT010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BNKMENU.cbl`) -> Impact: **33.5** | LOC: 588
- `DBR010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BANKDATA.cbl`) -> Impact: **31.7** | LOC: 194
- `doGet` **(Many-Argument Workhorses)** (@ `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/AccountList.java`) -> Impact: **29.0** | LOC: 180
- `VD010` **(I/O & Config Routines)** (@ `src/base/cobol_src/BNK1UAC.cbl`) -> Impact: **28.5** | LOC: 245

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/base/cobol_src` | 29 | 9653.3 | 82.23% | 27.14% |
| `src/bank-application-frontend` | 6 | 5031.56 | 0.0% | 0.0% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json` | 19 | 1806.04 | 13.25% | 41.35% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2` | 2 | 1136.26 | 64.38% | 0.0% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces` | 7 | 867.38 | 18.5% | 28.57% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access` | 5 | 748.86 | 51.87% | 45.48% |
| `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam` | 1 | 693.46 | 54.95% | 0.0% |
| `__monolith__` | 8 | 357.22 | 12.36% | 0.0% |
| `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/updateaccount` | 3 | 246.98 | 27.57% | 33.33% |
| `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/controllers` | 2 | 204.6 | 2.89% | 39.28% |

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
- `src/base/cobol_src/BNK1DCS.cbl` -> **30** Orphaned Functions | **0** Duplicates
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
- **Binary Anomalies (X-Ray):** `26` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `932` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/bank-application-frontend/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CCS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.579)
- **Top Global Matches:** file_cluster_12: 7.579, file_cluster_11: 8.533, file_cluster_15: 9.357
- **Magnitude:** 913.44 | **LOC:** 1661 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ED010` **(I/O & Config Routines)** (Impact: 98.8)
  * `A010` **(I/O & Config Routines)** (Impact: 20.2)
  * `SM010` **(I/O & Config Routines)** (Impact: 15.0)
  * `CCD010` **(I/O & Config Routines)** (Impact: 12.0)
  * `RM010` **(I/O & Config Routines)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 165 instances
* *State Mutation (weighted view):* 685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 133`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 355`, `unreferenced_by_name: 21`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ABNDINFO, BNK1CCM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1DCS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.758)
- **Top Global Matches:** file_cluster_11: 6.758, file_cluster_12: 7.185, file_cluster_2: 7.807
- **Magnitude:** 895.5 | **LOC:** 2057 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A010` **(I/O & Config Routines)** (Impact: 24.2)
  * `ED2010` **(I/O & Config Routines)** (Impact: 19.1)
  * `SM010` **(I/O & Config Routines)** (Impact: 15.0)
  * `PM010` **(I/O & Config Routines)** (Impact: 14.5)
  * `UPDCD010` **(I/O & Config Routines)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 683
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 106`, `args: 1`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 463`, `unreferenced_by_name: 30`
* *Architecture:* `io: 2`, `api: 1`, `import: 7`
* *Defense:* `safety: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ABNDINFO, BNK1DCM, DELCUS, DFHAID, DFHBMSCA, INQCUST, UPDCUST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.783)
- **Top Global Matches:** file_cluster_12: 8.783, file_cluster_7: 10.476, file_cluster_5: 10.63
- **Magnitude:** 737.18 | **LOC:** 1765 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 3.1; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.1%), Complexity Load (formerly Cognitive Load) (54.4%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateNewAccount` **(Compute Cores)** (Impact: 28.1)
  * `updateAccountInternal` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `getAccountsInternal` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `createAccountInternal` **(Compute Cores)** (Impact: 20.1)
  * `debitCreditAccount` **(Many-Argument Workhorses)** (Impact: 17.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 522
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 191`, `args: 81`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 288`
* *Architecture:* `io: 10`, `api: 37`, `import: 21`
* *Defense:* `safety: 14`, `doc: 10`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.1
  * `Choke Point (Betweenness):` 0.000305 | `Ripple Effect (Closeness):` 0.008081
  * `Imports (Out-Degree: 10):` com.ibm.cics.cip.bankliberty.web.db2.Account, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.Task, com.ibm.json.java.JSONArray, com.ibm.json.java.JSONObject, jakarta.ws.rs.Consumes, jakarta.ws.rs.DELETE, jakarta.ws.rs.GET...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_12: 6.727, file_cluster_7: 7.753, file_cluster_5: 8.669
- **Magnitude:** 693.46 | **LOC:** 1953 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 1.708; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.3%), Complexity Load (formerly Cognitive Load) (55.0%), Connectivity (formerly Api Exposure) (22.1%)
- **Documentation Coverage:** 97.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createCustomer` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `getCustomer` **(Many-Argument Workhorses)** (Impact: 16.3)
  * `deleteCustomer` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `getCustomersByName` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `getCustomersByName` **(Many-Argument Workhorses)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 419
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 251`, `args: 50`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 257`
* *Architecture:* `api: 32`, `import: 37`
* *Defense:* `safety: 96`, `doc: 1`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.708
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.005823
  * `Imports (Out-Degree: 4):` com.ibm.cics.cip.bankliberty.api.json.CreditScore, com.ibm.cics.cip.bankliberty.api.json.CustomerJSON, com.ibm.cics.cip.bankliberty.datainterfaces.CUSTOMER, com.ibm.cics.cip.bankliberty.datainterfaces.CustomerControl, com.ibm.cics.server.ChangedException, com.ibm.cics.server.DuplicateKeyException, com.ibm.cics.server.DuplicateRecordException, com.ibm.cics.server.EndOfFileException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/BNK1UAC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.491)
- **Top Global Matches:** file_cluster_12: 7.491, file_cluster_11: 7.886, file_cluster_2: 8.731
- **Magnitude:** 667.76 | **LOC:** 1409 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VD010` **(I/O & Config Routines)** (Impact: 28.5)
  * `A010` **(I/O & Config Routines)** (Impact: 21.1)
  * `UAD010` **(I/O & Config Routines)** (Impact: 14.5)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `PM010` **(I/O & Config Routines)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 518
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 59`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 304`, `dead_code: 2`, `unreferenced_by_name: 19`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ABNDINFO, BNK1UAM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/CRECUST.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.224)
- **Top Global Matches:** file_cluster_4: 8.224, file_cluster_11: 8.287, file_cluster_15: 9.203
- **Magnitude:** 665.82 | **LOC:** 1498 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 1.839; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.5%), Concurrency Surface (formerly Concurrency) (92.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CC010` **(I/O & Config Routines)** (Impact: 66.0)
  * `P010` **(I/O & Config Routines)** (Impact: 22.9)
  * `GLCV010` **(I/O & Config Routines)** (Impact: 14.8)
  * `WCV010` **(I/O & Config Routines)** (Impact: 10.0)
  * `DOBC010` **(I/O & Config Routines)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 95 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 395
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 99`, `args: 6`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 205`, `fragile_debt: 1`
* *Architecture:* `io: 13`, `api: 25`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 22`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.00202
  * `Imports (Out-Degree: 8):` ABNDINFO, CEEIGZCT, CRECUST, CUSTCTRL, CUSTOMER, PROCDB2, PROCTRAN, SORTCODE...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/BNK1CAC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.245)
- **Top Global Matches:** file_cluster_4: 8.245, file_cluster_12: 9.934, file_cluster_11: 10.939
- **Magnitude:** 619.98 | **LOC:** 1302 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ED010` **(I/O & Config Routines)** (Impact: 53.7)
  * `CAD010` **(I/O & Config Routines)** (Impact: 25.0)
  * `A010` **(I/O & Config Routines)** (Impact: 20.7)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `RM010` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 454
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 70`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 246`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ABNDINFO, BNK1CAM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BANKDATA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.994)
- **Top Global Matches:** file_cluster_11: 6.994, file_cluster_2: 7.977, file_cluster_15: 8.136
- **Magnitude:** 609.82 | **LOC:** 1464 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 2.651; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DBR010` **(I/O & Config Routines)** (Impact: 31.7)
  * `A010` **(I/O & Config Routines)** (Impact: 26.2)
  * `PA010` **(I/O & Config Routines)** (Impact: 14.0)
  * `GOD010` **(I/O & Config Routines)** (Impact: 4.5)
  * `DA010` **(I/O & Config Routines)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 479
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 77`, `args: 3`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 377`, `dead_code: 1`, `unreferenced_by_name: 17`
* *Architecture:* `io: 18`, `api: 1`, `import: 7`
* *Defense:* `safety: 12`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.651
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.00202
  * `Imports (Out-Degree: 6):` ACCDB2, ACCTCTRL, CONTDB2, CUSTCTRL, CUSTOMER, SORTCODE, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/Account.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.131)
- **Top Global Matches:** file_cluster_12: 6.131, file_cluster_7: 9.09, file_cluster_5: 9.125
- **Magnitude:** 592.16 | **LOC:** 1362 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 1.696; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%), Complexity Load (formerly Cognitive Load) (39.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getNextMonth` **(Stateful Encapsulated Methods)** (Impact: 22.0)
  * `getAccount` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `getAccountsByBalance` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `getAccountsByBalance` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `deleteAccount` **(Many-Argument Workhorses)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 125`, `args: 74`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 151`
* *Architecture:* `io: 17`, `api: 41`, `import: 12`
* *Defense:* `safety: 30`, `immutability_locks: 33`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.696
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.005594
  * `Imports (Out-Degree: 3):` com.ibm.cics.cip.bankliberty.api.json.AccountJSON, com.ibm.cics.cip.bankliberty.api.json.HBankDataAccess, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.Task, java.math.BigDecimal, java.sql.Date, java.sql.PreparedStatement, java.sql.ResultSet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/db2/ProcessedTransaction.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.026)
- **Top Global Matches:** file_cluster_15: 6.026, file_cluster_11: 6.537, file_cluster_16: 6.956
- **Magnitude:** 544.1 | **LOC:** 1012 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 1.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getProcessedTransactions` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `writeDeleteCustomer` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `sortOutDateTimeTaskString` **(I/O & Config Routines)** (Impact: 10.9)
  * `writeCreateCustomer` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `sortOutCustomerDOB` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 99`, `args: 57`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 207`
* *Architecture:* `io: 2`, `api: 42`, `import: 13`
* *Defense:* `safety: 16`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.619
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006157
  * `Imports (Out-Degree: 1):` com.ibm.cics.cip.bankliberty.api.json.HBankDataAccess, com.ibm.cics.cip.bankliberty.datainterfaces.PROCTRAN, com.ibm.cics.server.Task, java.math.BigDecimal, java.math.RoundingMode, java.sql.Date, java.sql.PreparedStatement, java.sql.ResultSet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/XFRFUN.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.982)
- **Top Global Matches:** file_cluster_4: 7.982, file_cluster_11: 9.535, file_cluster_12: 9.918
- **Magnitude:** 543.34 | **LOC:** 1925 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 1.839; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UAD010` **(I/O & Config Routines)** (Impact: 43.5)
  * `UADT010` **(I/O & Config Routines)** (Impact: 35.5)
  * `AH010` **(I/O & Config Routines)** (Impact: 14.7)
  * `UADF010` **(I/O & Config Routines)** (Impact: 8.5)
  * `CFSDD010` **(I/O & Config Routines)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 91`, `args: 1`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 230`
* *Architecture:* `io: 15`, `api: 17`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.00202
  * `Imports (Out-Degree: 8):` ABNDINFO, ACCDB2, ACCOUNT, PROCDB2, PROCTRAN, SORTCODE, SQLCA, SQLDA...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/BNK1TFN.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.656)
- **Top Global Matches:** file_cluster_12: 6.656, file_cluster_7: 8.283, file_cluster_11: 8.866
- **Magnitude:** 519.42 | **LOC:** 1228 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VA010` **(I/O & Config Routines)** (Impact: 22.5)
  * `A010` **(I/O & Config Routines)** (Impact: 17.9)
  * `GCD010` **(I/O & Config Routines)** (Impact: 17.5)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `ED010` **(I/O & Config Routines)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 53`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 217`, `dead_code: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ABNDINFO, BNK1TFM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1CRA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.593)
- **Top Global Matches:** file_cluster_12: 6.593, file_cluster_11: 8.338, file_cluster_7: 8.562
- **Magnitude:** 486.18 | **LOC:** 1170 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A010` **(I/O & Config Routines)** (Impact: 19.6)
  * `VA010` **(I/O & Config Routines)** (Impact: 19.5)
  * `UCD010` **(I/O & Config Routines)** (Impact: 16.0)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `ED010` **(I/O & Config Routines)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 53`, `args: 1`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 191`, `unreferenced_by_name: 15`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ABNDINFO, BNK1CDM, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNK1DAC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.956)
- **Top Global Matches:** file_cluster_11: 6.956, file_cluster_12: 7.096, file_cluster_2: 7.937
- **Magnitude:** 482.82 | **LOC:** 1162 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A010` **(I/O & Config Routines)** (Impact: 23.6)
  * `SM010` **(I/O & Config Routines)** (Impact: 15.0)
  * `DAD010` **(I/O & Config Routines)** (Impact: 9.5)
  * `PM010` **(I/O & Config Routines)** (Impact: 8.4)
  * `GAD010` **(I/O & Config Routines)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 57`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 235`, `unreferenced_by_name: 17`
* *Architecture:* `io: 3`, `api: 1`, `import: 4`
* *Defense:* `safety: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ABNDINFO, BNK1DAM, DFHAID, INQACC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/BNKMENU.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.219)
- **Top Global Matches:** file_cluster_11: 7.219, file_cluster_2: 8.182, file_cluster_15: 8.393
- **Magnitude:** 451.42 | **LOC:** 1315 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IOT010` **(I/O & Config Routines)** (Impact: 33.5)
  * `A010` **(I/O & Config Routines)** (Impact: 16.4)
  * `SMM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `RMM010` **(I/O & Config Routines)** (Impact: 7.5)
  * `STM010` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 65`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 225`, `unreferenced_by_name: 16`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ABNDINFO, BNK1MAI, DFHAID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/CREACC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.701)
- **Top Global Matches:** file_cluster_11: 6.701, file_cluster_2: 7.814, file_cluster_15: 7.926
- **Magnitude:** 438.16 | **LOC:** 1248 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 1.839; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CD010` **(I/O & Config Routines)** (Impact: 23.2)
  * `FNA010` **(I/O & Config Routines)** (Impact: 14.5)
  * `P010` **(I/O & Config Routines)** (Impact: 10.6)
  * `ATC010` **(I/O & Config Routines)** (Impact: 8.8)
  * `WAD010` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 70`, `args: 1`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `state_mutation: 195`
* *Architecture:* `io: 10`, `api: 24`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.00202
  * `Imports (Out-Degree: 14):` ABNDINFO, ACCDB2, ACCOUNT, ACCTCTRL, CREACC, CUSTOMER, INQACCCU, INQCUST...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.524)
- **Top Global Matches:** file_cluster_12: 7.524, file_cluster_7: 8.197, file_cluster_5: 9.063
- **Magnitude:** 416.18 | **LOC:** 1231 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **24**; blast radius 2.914; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (42.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createCustomerInternal` **(Compute Cores)** (Impact: 26.5)
  * `deleteCustomerInternal` **(Compute Cores)** (Impact: 18.3)
  * `getCustomersSurnameInternal` **(I/O & Config Routines)** (Impact: 5.1)
  * `getCustomersAgeInternal` **(Compute Cores)** (Impact: 5.1)
  * `getCustomersTownInternal` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 138`, `args: 51`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 153`
* *Architecture:* `io: 9`, `api: 30`, `import: 24`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.914
  * `Choke Point (Betweenness):` 0.00027 | `Ripple Effect (Closeness):` 0.007273
  * `Imports (Out-Degree: 9):` com.ibm.cics.cip.bankliberty.web.vsam.Customer, com.ibm.cics.server.InvalidRequestException, com.ibm.cics.server.Task, com.ibm.json.java.JSONArray, com.ibm.json.java.JSONObject, jakarta.ws.rs.Consumes, jakarta.ws.rs.DELETE, jakarta.ws.rs.GET...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/BNK1CCA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.19)
- **Top Global Matches:** file_cluster_11: 7.19, file_cluster_2: 8.204, file_cluster_15: 8.361
- **Magnitude:** 345.78 | **LOC:** 956 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.433; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GCD010` **(I/O & Config Routines)** (Impact: 26.4)
  * `A010` **(I/O & Config Routines)** (Impact: 17.9)
  * `SM010` **(I/O & Config Routines)** (Impact: 13.5)
  * `RM010` **(I/O & Config Routines)** (Impact: 4.0)
  * `STM010` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 54`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 142`, `unreferenced_by_name: 15`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ABNDINFO, BNK1ACC, DFHAID, INQACCCU
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQACC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.708)
- **Top Global Matches:** file_cluster_11: 5.708, file_cluster_2: 6.866, file_cluster_15: 7.261
- **Magnitude:** 335.68 | **LOC:** 1003 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 1.981; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AH010` **(I/O & Config Routines)** (Impact: 16.5)
  * `RAD010` **(I/O & Config Routines)** (Impact: 14.0)
  * `FD010` **(I/O & Config Routines)** (Impact: 9.0)
  * `CFSDCD010` **(I/O & Config Routines)** (Impact: 7.3)
  * `A010` **(I/O & Config Routines)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 58`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 144`
* *Architecture:* `io: 10`, `api: 17`, `import: 6`
* *Defense:* `safety: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.981
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.00404
  * `Imports (Out-Degree: 6):` ABNDINFO, ACCDB2, ACCOUNT, INQACC, SORTCODE, SQLCA
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mvnw` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.76)
- **Top Global Matches:** file_cluster_7: 7.76, file_cluster_12: 9.494, file_cluster_14: 9.697
- **Magnitude:** 308.9 | **LOC:** 312 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.433; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.9%), Guard Balance (formerly Safety Score) (83.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_maven_basedir` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* # traverses directory structure from process work directory to filesystem root # first directory wit...
  * `concat_lines` **(Parameter Forwarders)** (Impact: 3.1)
    * *Intent:* # concatenates all lines of a file
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.433
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .mavenrc, mavenrc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base/cobol_src/INQACCCU.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.842)
- **Top Global Matches:** file_cluster_11: 6.842, file_cluster_12: 6.907, file_cluster_2: 7.925
- **Magnitude:** 263.6 | **LOC:** 883 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 1.953; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RAD010` **(I/O & Config Routines)** (Impact: 15.0)
  * `AH010` **(I/O & Config Routines)** (Impact: 14.8)
  * `FD010` **(I/O & Config Routines)** (Impact: 12.5)
  * `CFSDD010` **(I/O & Config Routines)** (Impact: 7.2)
  * `CC010` **(I/O & Config Routines)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 61`, `args: 1`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 99`
* *Architecture:* `io: 10`, `api: 13`, `import: 8`
* *Defense:* `safety: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.953
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.007215
  * `Imports (Out-Degree: 9):` ABNDINFO, ACCDB2, ACCOUNT, CUSTOMER, INQACCCU, INQCUST, SORTCODE, SQLCA
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/base/cobol_src/INQCUST.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.419)
- **Top Global Matches:** file_cluster_12: 6.419, file_cluster_11: 8.136, file_cluster_7: 8.682
- **Magnitude:** 262.5 | **LOC:** 712 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 1.985; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.7%), Guard Balance (formerly Safety Score) (62.6%), Connectivity (formerly Api Exposure) (58.6%)
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
* *Structure:* `branch: 37`, `structural_boundaries: 51`, `args: 1`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 75`
* *Architecture:* `io: 8`, `api: 16`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.985
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.009091
  * `Imports (Out-Degree: 5):` ABNDINFO, CUSTOMER, INQCUST, SORTCODE
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/Account.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.396)
- **Top Global Matches:** file_cluster_7: 8.396, file_cluster_12: 10.01, file_cluster_14: 10.098
- **Magnitude:** 249.18 | **LOC:** 586 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 2.319; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.4%)
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
* *Structure:* `branch: 9`, `structural_boundaries: 60`, `args: 42`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 95`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 31`, `import: 12`
* *Defense:* `safety: 10`, `immutability_locks: 10`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.319
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.004848
  * `Imports (Out-Degree: 2):` com.ibm.cics.cip.bankliberty.api.json.AccountJSON, com.ibm.cics.cip.bankliberty.api.json.AccountsResource, com.ibm.json.java.JSONObject, jakarta.ws.rs.core.Response, java.io.IOException, java.math.BigDecimal, java.math.RoundingMode, java.sql.Date...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/datainterfaces/CustomerControl.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.429)
- **Top Global Matches:** file_cluster_12: 6.429, file_cluster_11: 7.415, file_cluster_15: 7.515
- **Magnitude:** 241.76 | **LOC:** 518 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.796; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%), Connectivity (formerly Api Exposure) (52.8%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005172
  * `Imports (Out-Degree: 0):` com.ibm.jzos.fields.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/bank-application-frontend/src/content/CustomerDeletePage/CustomerDeletePage.js` (JAVASCRIPT) | Magnitude: 70.16 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 174, core_var_decl: 38, structural_boundaries: 33, ui_framework: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/updateaccount/UpdateAccountJson.java` (JAVA) | Magnitude: 20.64 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 58, structural_boundaries: 12, api: 7, args: 6
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/customerenquiry/InqCustDob.java` (JAVA) | Magnitude: 23.74 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 39, structural_boundaries: 13, api: 9, args: 8
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/customerenquiry/InqCustReviewDate.java` (JAVA) | Magnitude: 23.86 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 13, api: 9, args: 8
- `src/base/cobol_src/INQACCCU.cbl` (COBOL) | Magnitude: 263.6 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 570, state_mutation: 99, structural_boundaries: 61, reflection_metaprogramming: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/createaccount/CreateAccountJson.java` (JAVA) | Magnitude: 20.28 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 55, structural_boundaries: 12, api: 7, args: 6
- `src/Z-OS-Connect-Payment-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/paymentinterface/controllers/WebController.java` (JAVA) | Magnitude: 46.4 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 116, structural_boundaries: 48, import: 19, core_var_decl: 16
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/jsonclasses/deleteaccount/DeleteAccountJson.java` (JAVA) | Magnitude: 16.44 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 11, api: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/base/cobol_src/CRECUST.cbl` (COBOL) | Magnitude: 665.82 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 986, state_mutation: 205, structural_boundaries: 99, branch: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/webui/data_access/CustomerList.java` (JAVA) | Magnitude: 132.04 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 235, core_var_decl: 66, design_camel_case: 45, structural_boundaries: 33

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

- `src/base/cobol_src/BNK1CCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 913.44
- `src/base/cobol_src/BNK1DCS.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 895.5
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 693.46
- `src/base/cobol_src/BNK1UAC.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 667.76
- `src/base/cobol_src/CRECUST.cbl` -> **JAMOGRAD** (100.0% isolated ownership) | Magnitude: 665.82

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 99.9988%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/CustomerResource.java` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 99.9871%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/SortCodeResource.java` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 72.7164%)
- `etc/install/base/installjcl/CRELIBS.jcl` -> **Severity: 0.009** (Bridge: 0.0005 * Flux: 16.7982%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/web/vsam/Customer.java` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 99.9616%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/base/cobol_src/ABNDPROC.cbl` -> **Severity: 2.305** (Embedded: 0.0465 * Error Risk: 49.6154%)
- `etc/install/base/installjcl/CRELIBS.jcl` -> **Severity: 1.229** (Embedded: 0.0242 * Error Risk: 50.7142%)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/OutputFormatUtils.java` -> **Severity: 0.944** (Embedded: 0.0184 * Error Risk: 51.4282%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/HBankDataAccess.java` -> **Severity: 0.778** (Embedded: 0.0126 * Error Risk: 61.7919%)
- `src/webui/src/main/java/com/ibm/cics/cip/bankliberty/api/json/AccountsResource.java` -> **Severity: 0.575** (Embedded: 0.0081 * Error Risk: 71.1286%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `etc/install/base/installjcl/CRELIBS.jcl` -> **Severity: 5750.3** (Blast Radius: 57.503 * Doc Risk: 100.0%)
- `etc/install/base/installjcl/CICSTS56.jcl` -> **Severity: 3675.5** (Blast Radius: 36.755 * Doc Risk: 100.0%)
- `src/Z-OS-Connect-Customer-Services-Interface/src/main/java/com/ibm/cics/cip/bank/springboot/customerservices/JsonPropertyNamingStrategy.java` -> **Severity: 2178.5** (Blast Radius: 21.785 * Doc Risk: 100.0%)
- `src/base/cobol_src/ABNDPROC.cbl` -> **Severity: 847.3** (Blast Radius: 8.473 * Doc Risk: 100.0%)
- `etc/install/base/installjcl/CREDB2L.jcl` -> **Severity: 548.8** (Blast Radius: 5.488 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `180` files carry mainframe facts -- `279` call sites, `163` dataset bindings, `3670` record items.

- **DB2 schemas:** `24` columns of `EXEC SQL DECLARE ... TABLE` (inline or DCLGEN members), full shape in `sql_table_data`.

- **DB2 table access:** `39` embedded SQL statements touching `3` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

- **CICS resources:** `68` CSD `DEFINE` records (FILE→DSNAME, TDQUEUE, DB2TRAN→DB2ENTRY→PLAN, MAPSET, LIBRARY, ...), full attributes in `csd_resource_data`.

- **CICS operations:** `99` EXEC CICS operations naming a resource (`2` CHANNEL, `14` CONTAINER, `46` FILE, `37` MAP); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

- **CICS task control:** `23` commands (`17` DELAY, `2` DEQ, `2` ENQ, `1` FETCH ANY, `1` RUN); child transid (or its STRING-built pattern), channel, CHILD/REQID token and timing in `cics_task_data`.

### `src/base/cobol_src/BNK1DCS.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID ODCS`, `LINK WS-ABEND-PGM`, `LINK INQCUST`, `LINK DELCUS`, `LINK UPDCUST`
- **COMMAREA passed:** `RETURN TRANSID ODCS ← WS-COMM-AREA LENGTH(266)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK INQCUST ← INQCUST-COMMAREA`, `LINK DELCUS ← DELCUS-COMMAREA`, `LINK UPDCUST ← UPDCUST-COMMAREA`
- **Record layouts (115 items):** `WS-COMM-AREA (13)`, `DFHCOMMAREA (13)`, `COMM-DOB-UPD-FORMAT (9)`, `COMM-CS-REVIEW-UPD-FORMAT (9)`, `WS-FAIL-INFO (8)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `CREDIT-SCORE-UPD-FORMAT (5)`, `COMM-DOB-SPLIT (4)`, `COMM-ADDR-SPLIT (4)` … (+19 more)
- **CICS operations:** `MAP BNK1DC (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 575 (INITIALIZE 29, MOVE 387, STRING 158, UNSTRING 1); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ABEND->ABEND-HANDLING`, `ABEND->CANCEL`; `12/15` RESP results tested

### `src/base/cobol_src/BANKDATA.cbl` (COBOL)
- **Calls:** `CALL CEEGMT`, `CALL CEEDATM`
- **Datasets:** `VSAM(OUTPUT)`
- **Record layouts (186 items):** `TITLE-ALPHABET (37)`, `HOST-ACCOUNT-ROW (33)`, `TIME-DATA (13)`, `WS-CURRENT-DATE-DATA (11)`, `HOST-CONTROL-ROW (4)`, `DISP-LOT (3)`, `CUSTOMER-VSAM-STATUS (3)`, `PARM-BUFFER (3)`, `FORENAMES (2)`, `STREET-NAME-TREES (2)`, `STREET-NAME-ROADS (2)`, `TOWNS (2)` … (+64 more)
- **DB2 table access:** `CONTROL (insert/delete)`, `ACCOUNT (insert/delete)`
- **Keyed files:** `CUSTOMER-FILE INDEXED/RANDOM key CUSTOMER-KEY`
- **Data moves:** 402 (ADD 9, COMPUTE 23, DIVIDE 4, INITIALIZE 1, MOVE 333, STRING 28, UNSTRING 4); most-fed items `CUSTOMER-ADDRESS`, `CUSTOMER-NAME`, `HV-CONTROL-NAME`, `DISP-SQLCD`, `FORENAMES-PTR`, `WS-SQLCODE-DISPLAY`
- **Unit of work:** `3` commit / `0` rollback points; handlers none; `0/0` RESP results tested

### `src/base/cobol_src/BNK1CCS.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID OCCS`, `LINK WS-ABEND-PGM`, `LINK CRECUST`
- **COMMAREA passed:** `RETURN TRANSID OCCS ← WS-COMM-AREA`, `RETURN TRANSID OCCS ← WS-COMM-AREA LENGTH(248)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK CRECUST ← SUBPGM-PARMS`
- **Record layouts (94 items):** `SUBPGM-PARMS (16)`, `DATE-REFORMED (10)`, `WS-FAIL-INFO (8)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `COMM-DOB-SPLIT (4)`, `COMM-ADDR-SPLIT (4)`, `WS-ADDR-SPLIT (4)`, `WS-CICS-WORK-AREA (3)`, `SWITCHES (3)` … (+15 more)
- **CICS operations:** `MAP BNK1CCM (write)`, `MAP BNK1CC (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 432 (INITIALIZE 21, MOVE 297, STRING 114); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ABEND->HANDLE-ABEND`, `ABEND->CANCEL`; `10/14` RESP results tested

### `src/base/cobol_src/XFRFUN.cbl` (COBOL)
- **Calls:** `LINK WS-ABEND-PGM`
- **COMMAREA passed:** `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (116 items):** `HOST-ACCOUNT-ROW (14)`, `HOST-PROCTRAN-ROW (10)`, `WS-PASSED-DATA (7)`, `DB2-DATE-REFORMAT (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `WS-CICS-WORK-AREA (3)`, `DESIRED-ACC-KEY (3)`, `WS-REJ-REAS (3)`, `WS-PROC-REAS (3)`, `WS-TESTING-DB-NAME (3)` … (+36 more)
- **DB2 table access:** `ACCOUNT (read/update)`, `PROCTRAN (insert)`
- **CICS task control:** `DELAY`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 357 (ADD 2, COMPUTE 8, INITIALIZE 17, MOVE 176, STRING 154); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `8` rollback points; handlers `ABEND->ABEND-HANDLING`; `8/8` RESP results tested

### `src/base/cobol_src/BNK1UAC.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID OUAC`, `LINK WS-ABEND-PGM`, `LINK INQACC`, `LINK UPDACC`
- **COMMAREA passed:** `RETURN TRANSID OUAC ← WS-COMM-AREA LENGTH(99)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK INQACC ← DFHCOMMAREA`, `LINK UPDACC ← DFHCOMMAREA`
- **Record layouts (120 items):** `DFHCOMMAREA (15)`, `WS-COMM-AREA (14)`, `WS-FAIL-INFO (8)`, `WS-CONVERSION (7)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `WS-DATE-SPLIT (4)`, `INT-RT-CONVERT (4)`, `WS-CICS-WORK-AREA (3)`, `SWITCHES (3)` … (+32 more)
- **CICS operations:** `MAP BNK1UA (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 375 (ADD 2, COMPUTE 15, INITIALIZE 19, MOVE 244, STRING 95); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `8/9` RESP results tested

### `src/base/cobol_src/CRECUST.cbl` (COBOL)
- **Calls:** `RUN TRANSID WS-RUN-TRANSID`, `LINK WS-ABEND-PGM`, `CALL CEEDAYS`, `CALL CEELOCT`
- **COMMAREA passed:** `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (193 items):** `WS-CHILD-DATA (16)`, `WS-CURRENT-DATE-DATA (11)`, `FC (11)`, `HOST-PROCTRAN-ROW (10)`, `NCS-CUST-NO-STUFF (8)`, `WS-TODAY-GREGORIAN (8)`, `WS-TIME-DATA (6)`, `RETURN-DATA (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-CICSTS-LEVEL-DATA (6)`, `DATE-OF-BIRTH-FOR-CEEDAYS (5)` … (+73 more)
- **DB2 table access:** `PROCTRAN (insert)`
- **CICS operations:** `CONTAINER WS-PUT-CONT-NAME? (write)`, `CHANNEL CIPCREDCHANN (pass)`, `CONTAINER WS-CONTAINER-NAME? (read)`, `FILE CUSTOMER (read/update/write)`
- **CICS task control:** `ENQ NCS-CUST-NO-NAME`, `DEQ NCS-CUST-NO-NAME`, `RUN OCR[0-9]`, `DELAY`, `FETCH ANY`
- **Data moves:** 240 (ADD 5, COMPUTE 17, INITIALIZE 6, MOVE 171, STRING 38, SUBTRACT 2, UNSTRING 1); most-fed items `COMM-CS-REVIEW-DATE`, `HV-PROCTRAN-DESC`, `WS-ACTUAL-CS-SCR`, `WS-NEW-REVIEW-DATE-INT`, `ABND-FREEFORM`, `ABND-TIME`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `12/12` RESP results tested

### `src/base/cobol_src/CREACC.cbl` (COBOL)
- **Calls:** `LINK INQCUST`, `LINK WS-ABEND-PGM`, `LINK INQACCCU`
- **COMMAREA passed:** `LINK INQCUST ← INQCUST-COMMAREA`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK INQACCCU ← INQACCCU-COMMAREA`
- **Record layouts (146 items):** `HOST-ACCOUNT-ROW (31)`, `HOST-PROCTRAN-ROW (10)`, `NCS-ACC-NO-STUFF (8)`, `RETURN-DATA (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-FUTURE-CONV (6)`, `WS-TIME-DATA (6)`, `HOST-CONTROL-ROW (4)`, `WS-CICS-WORK-AREA (4)`, `WS-FUT (4)`, `CUSTOMER-KY (3)` … (+47 more)
- **DB2 table access:** `CONTROL (read/update)`, `ACCOUNT (insert)`, `PROCTRAN (insert)`
- **CICS task control:** `ENQ NCS-ACC-NO-NAME`, `DEQ NCS-ACC-NO-NAME`
- **Data moves:** 272 (ADD 16, COMPUTE 8, DIVIDE 12, INITIALIZE 10, MOVE 156, STRING 70); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `WS-INTEGER`, `SQLCODE-DISPLAY`, `WS-STDT-X`, `ABND-DATE`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `3/4` RESP results tested

### `src/base/cobol_src/BNK1DAC.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID ODAC`, `LINK WS-ABEND-PGM`, `LINK INQACC`, `LINK DELACC`
- **COMMAREA passed:** `RETURN TRANSID ODAC ← WS-COMM-AREA LENGTH(102)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK INQACC ← INQACC-COMMAREA`, `LINK DELACC ← PARMS-SUBPGM`
- **Record layouts (122 items):** `PARMS-SUBPGM (22)`, `WS-COMM-AREA (17)`, `DFHCOMMAREA (17)`, `WS-FAIL-INFO (8)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `COMM-OPENED-SPLIT (4)`, `COMM-LAST-ST-SPLIT (4)`, `COMM-NEXT-ST-SPLIT (4)`, `WS-CICS-WORK-AREA (3)` … (+15 more)
- **CICS operations:** `MAP BNK1DA (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 293 (COMPUTE 1, INITIALIZE 21, MOVE 187, STRING 84); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `WS-CICS-RESP-DISP`, `WS-CICS-RESP2-DISP`, `ABND-DATE`, `ABND-RESP2CODE`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `8/9` RESP results tested

### `src/base/cobol_src/BNK1CAC.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID OCAC`, `LINK WS-ABEND-PGM`, `LINK CREACC`
- **COMMAREA passed:** `RETURN TRANSID OCAC ← WS-COMM-AREA LENGTH(32)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK CREACC ← SUBPGM-PARMS`
- **Record layouts (98 items):** `SUBPGM-PARMS (16)`, `DATE-REFORMED (10)`, `WS-FAIL-INFO (8)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `WS-COMM-AREA (5)`, `DFHCOMMAREA (5)`, `COMM-DOB-SPLIT (4)`, `MORE-STRING-CONVS (4)`, `WS-CICS-WORK-AREA (3)` … (+17 more)
- **CICS operations:** `MAP BNK1CA (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 315 (ADD 2, COMPUTE 2, INITIALIZE 16, MOVE 191, STRING 102, SUBTRACT 2); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `7/8` RESP results tested

### `src/base/cobol_src/BNKMENU.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `LINK WS-ABEND-PGM`, `RETURN TRANSID ODCS`, `RETURN TRANSID ODAC`, `RETURN TRANSID OCCS`, `RETURN TRANSID OCAC`, `RETURN TRANSID OUAC`, `RETURN TRANSID OCRA`, `RETURN TRANSID OTFN`, `RETURN TRANSID OCCA`
- **COMMAREA passed:** `RETURN TRANSID OMEN ← COMMUNICATION-AREA LENGTH(1)`, `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (47 items):** `WS-FAIL-INFO (8)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `WS-CICS-WORK-AREA (3)`, `SWITCHES (3)`, `ACTION-ALPHA (2)`, `END-OF-SESSION-MESSAGE (1)`, `RESPONSE-CODE (1)`, `COMMUNICATION-AREA (1)`, `WS-U-TIME (1)` … (+4 more)
- **CICS operations:** `MAP BNK1ME (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 333 (INITIALIZE 28, MOVE 165, STRING 140); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `14/14` RESP results tested

### `src/base/cobol_src/BNK1TFN.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID OTFN`, `LINK WS-ABEND-PGM`, `LINK XFRFUN`
- **COMMAREA passed:** `RETURN TRANSID OTFN ← WS-COMMAREA LENGTH(29)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK XFRFUN ← SUBPGM-PARMS`
- **Record layouts (103 items):** `SUBPGM-PARMS (12)`, `WS-FAIL-INFO (8)`, `WS-CONVERSIONA (6)`, `WS-CONVERSIONB (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `COMM-DOB-SPLIT (4)`, `COMM-ADDR-SPLIT (4)`, `WS-COMMAREA (4)`, `DFHCOMMAREA (4)` … (+27 more)
- **CICS operations:** `MAP BNK1TF (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 283 (ADD 4, COMPUTE 4, INITIALIZE 15, MOVE 167, STRING 89, SUBTRACT 2, UNSTRING 2); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `7/8` RESP results tested

### `src/base/cobol_src/BNK1CRA.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID OCRA`, `LINK WS-ABEND-PGM`, `LINK DBCRFUN`
- **COMMAREA passed:** `RETURN TRANSID OCRA ← WS-COMM-AREA LENGTH(21)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK DBCRFUN ← SUBPGM-PARMS`
- **Record layouts (108 items):** `SUBPGM-PARMS (15)`, `WS-FAIL-INFO (8)`, `WS-CONVERSIONA (6)`, `WS-CONVERSIONB (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `WS-COMM-AREA (4)`, `DFHCOMMAREA (4)`, `WS-CICS-WORK-AREA (3)`, `SWITCHES (3)` … (+29 more)
- **CICS operations:** `MAP BNK1CD (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 258 (ADD 4, COMPUTE 5, INITIALIZE 15, MOVE 143, STRING 87, SUBTRACT 2, UNSTRING 2); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `7/8` RESP results tested

### `src/base/cobol_copy/BANKMAP.cpy` (COBOL)
- **Record layouts (368 items):** `BANKMAPO (210)`, `BANKMAPI (158)`

### `src/base/cobol_src/BNK1CCA.cbl` (COBOL)
- **Calls:** `RETURN TRANSID OMEN`, `RETURN TRANSID OCCA`, `LINK WS-ABEND-PGM`, `LINK INQACCCU-PROGRAM`
- **COMMAREA passed:** `RETURN TRANSID OCCA ← WS-COMM-AREA LENGTH(248)`, `LINK ABNDPROC ← ABNDINFO-REC`, `LINK INQACCCU ← INQACCCU-COMMAREA`
- **Record layouts (87 items):** `WS-CONVERSION (9)`, `WS-FAIL-INFO (8)`, `WS-COMM-AREA (7)`, `DFHCOMMAREA (7)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `FLAGS (5)`, `COMM-DOB-SPLIT (4)`, `COMM-ADDR-SPLIT (4)`, `WS-CICS-WORK-AREA (3)`, `SWITCHES (3)` … (+18 more)
- **CICS operations:** `MAP BNK1ACC (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 212 (INITIALIZE 15, MOVE 105, STRING 92); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ACCOUNTO`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `7/8` RESP results tested

### `src/base/cobol_src/INQACC.cbl` (COBOL)
- **Calls:** `LINK WS-ABEND-PGM`
- **COMMAREA passed:** `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (90 items):** `RETURNED-DATA (14)`, `HOST-ACCOUNT-ROW (13)`, `NCS-ACC-NO-STUFF (8)`, `DB2-DATE-REFORMAT (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `WS-CICS-WORK-AREA (3)`, `DATA-STORE-TYPE (3)`, `ACCOUNT-KY (3)`, `ACCOUNT-KY2 (3)`, `EXIT-BROWSE-LOOP (1)` … (+18 more)
- **DB2 table access:** `ACCOUNT (read)`
- **Data moves:** 191 (INITIALIZE 9, MOVE 123, STRING 59); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `1` rollback points; handlers `ABEND->ABEND-HANDLING`; `1/1` RESP results tested

### `src/base/cobol_src/DELCUS.cbl` (COBOL)
- **Calls:** `LINK INQCUST-PROGRAM`, `LINK DELACC`, `LINK INQACCCU`, `LINK WS-ABEND-PGM`
- **COMMAREA passed:** `LINK INQCUST ← INQCUST-COMMAREA`, `LINK DELACC ← DELACC-COMMAREA`, `LINK INQACCCU ← INQACCCU-COMMAREA`, `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (129 items):** `DELACC-COMMAREA (20)`, `RETURNED-DATA (14)`, `HOST-PROCTRAN-ROW (10)`, `WS-STOREDC-CUSTOMER (9)`, `DB2-DATE-REFORMAT (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `VAR-REMIX (4)`, `WS-CICS-WORK-AREA (3)`, `DESIRED-KEY-ACCTCUST (3)`, `DESIRED-KEY (3)` … (+38 more)
- **DB2 table access:** `PROCTRAN (insert)`
- **CICS operations:** `FILE CUSTOMER (delete/read)`
- **CICS task control:** `DELAY`
- **Data moves:** 123 (INITIALIZE 8, MOVE 79, STRING 36); most-fed items `ABND-FREEFORM`, `ABND-TIME`, `HV-PROCTRAN-DESC`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `4/4` RESP results tested

### `src/base/cobol_src/INQACCCU.cbl` (COBOL)
- **Calls:** `LINK WS-ABEND-PGM`, `LINK INQCUST`
- **COMMAREA passed:** `LINK ABNDPROC ← ABNDINFO-REC`, `LINK INQCUST ← INQCUST-COMMAREA`
- **Record layouts (87 items):** `RETURNED-DATA (14)`, `HOST-ACCOUNT-ROW (13)`, `EIBRCODE-NICE (7)`, `DB2-DATE-REFORMAT (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `WS-CICS-WORK-AREA (4)`, `DESIRED-KEY (3)`, `DATA-STORE-TYPE (3)`, `CUSTOMER-KY (3)`, `EXIT-BROWSE-LOOP (1)` … (+15 more)
- **DB2 table access:** `ACCOUNT (read)`
- **Data moves:** 147 (ADD 2, INITIALIZE 5, MOVE 82, STRING 58); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `SQLCODE-DISPLAY`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`
- **Unit of work:** `0` commit / `4` rollback points; handlers `ABEND->ABEND-HANDLING`; `4/4` RESP results tested

### `src/base/cobol_src/DELACC.cbl` (COBOL)
- **Calls:** `LINK WS-ABEND-PGM`
- **COMMAREA passed:** `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (98 items):** `RETURNED-DATA (14)`, `HOST-ACCOUNT-ROW (13)`, `HOST-PROCTRAN-ROW (10)`, `DB2-DATE-REFORMAT (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `WS-CICS-WORK-AREA (4)`, `DATA-STORE-TYPE (3)`, `ACCOUNT-KEY-RID (3)`, `SYSIDERR-RETRY (1)`, `FILE-RETRY (1)` … (+25 more)
- **DB2 table access:** `ACCOUNT (read/delete)`, `PROCTRAN (insert)`
- **Data moves:** 114 (INITIALIZE 5, MOVE 84, STRING 25); most-fed items `ABND-FREEFORM`, `ABND-TIME`, `DB2-DATE-REFORMAT`, `ABND-DATE`, `ABND-SQLCODE`, `ABND-TASKNO-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/0` RESP results tested

### `src/base/cobol_src/INQCUST.cbl` (COBOL)
- **Calls:** `LINK WS-ABEND-PGM`
- **COMMAREA passed:** `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (80 items):** `NCS-CUST-NO-STUFF (8)`, `WS-PASSED-DATA (7)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `WS-SORT-DIV (4)`, `VAR-REMIX (4)`, `VAR-REMIX2 (4)`, `WS-CICS-WORK-AREA (3)`, `CUSTOMER-KY (3)`, `CUSTOMER-KY2 (3)`, `SYSIDERR-RETRY (1)` … (+25 more)
- **CICS operations:** `FILE CUSTOMER (browse/read)`
- **CICS task control:** `DELAY`
- **Data moves:** 97 (ADD 2, COMPUTE 3, INITIALIZE 4, MOVE 64, STRING 24); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `REQUIRED-CUST-NUMBER`, `RANDOM-CUSTOMER`, `ABND-DATE`, `ABND-RESP2CODE`
- **Unit of work:** `0` commit / `1` rollback points; handlers `ABEND->ABEND-HANDLING`; `9/9` RESP results tested

### `src/base/cobol_src/DBCRFUN.cbl` (COBOL)
- **Calls:** `LINK WS-ABEND-PGM`
- **COMMAREA passed:** `LINK ABNDPROC ← ABNDINFO-REC`
- **Record layouts (88 items):** `HOST-ACCOUNT-ROW (14)`, `HOST-PROCTRAN-ROW (10)`, `WS-PASSED-DATA (7)`, `DB2-DATE-REFORMAT (6)`, `WS-ORIG-DATE-GRP (6)`, `WS-ORIG-DATE-GRP-X (6)`, `WS-TIME-DATA (6)`, `DATA-STORE-TYPE (4)`, `WS-CICS-WORK-AREA (3)`, `DESIRED-ACC-KEY (3)`, `SYSIDERR-RETRY (1)`, `FILE-RETRY (1)` … (+21 more)
- **DB2 table access:** `ACCOUNT (read/update)`, `PROCTRAN (insert)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 102 (COMPUTE 6, INITIALIZE 4, MOVE 66, STRING 26); most-fed items `ABND-TIME`, `ABND-FREEFORM`, `SQLCODE-DISPLAY`, `ABND-DATE`, `ABND-RESP2CODE`, `ABND-RESPCODE`
- **Unit of work:** `0` commit / `2` rollback points; handlers `ABEND->ABEND-HANDLING`; `2/2` RESP results tested

*(+160 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 100% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (42 gaps); BMS map sources (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3813 call pairs -- scoped 38.4%, unique 2.6%, ambiguous 6.0%, external 53.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 3034 | 35.4% | 1.0% | 7.6% | 56.0% |
| cobol | 330 | 98.8% | 0.0% | 0.0% | 1.2% |
| javascript | 285 | 22.1% | 0.0% | 0.0% | 77.9% |
| jcl | 152 | 0.0% | 44.7% | 0.0% | 55.3% |
| shell | 12 | 0.0% | 0.0% | 0.0% | 100.0% |

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
