# ARCHITECTURAL_BRIEF: aws-mainframe-modernization-carddemo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/aws-samples/aws-mainframe-modernization-carddemo` |
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
| Total Artifacts | 329 |
| Analyzed Artifacts (Scanned) | 201 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 128 |
| Total LOC | 34606 |
| Volatility Index | 0.025 |
| % Scanned of codebase = | 61.1% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4154 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.006 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 105 | 31942 | 52.2% |
| JCL | 62 | 2200 | 30.8% |
| PLAINTEXT | 11 | 0 | 5.5% |
| SHELL | 9 | 297 | 4.5% |
| MARKDOWN | 6 | 0 | 3.0% |
| SQLITE | 6 | 53 | 3.0% |
| ASSEMBLY | 2 | 114 | 1.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z -1.33; from the repo's file-archetype mix)
> **File Composition:** I/O & Config Routines Files 40%, Declarative / Non-Code 30%, Data / Markup / Trivial 17%, Interface Declarations Files 8%, Large Core Modules 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 184 | 91.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 8.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 128*

**Composition by Extension & Reason:**
- `no_extension`: 30x Excluded: Neighborhood Micro-Mass Limit Exceeded, 15x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bms`: 2x Zero-Density Threshold (LOC: 167, Signals: 0), 2x Zero-Density Threshold (LOC: 463, Signals: 0), 1x Zero-Density Threshold (LOC: 515, Signals: 0)
- `.ps`: 12x Excluded (Unsupported Extension: '.PS')
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.ctl`: 8x Excluded (Unsupported Extension: '.ctl')
- `.csd`: 3x Excluded (Unsupported Extension: '.csd'), 1x Excluded (Unsupported Extension: '.CSD')
- `.dbd`: 2x Excluded (Unsupported Extension: '.dbd'), 2x Excluded (Unsupported Extension: '.DBD')
- `.psb`: 2x Excluded (Unsupported Extension: '.PSB'), 2x Excluded (Unsupported Extension: '.psb')
- `.dcl`: 3x Excluded (Unsupported Extension: '.dcl')
- `.mac`: 2x Excluded (Unsupported Extension: '.mac')
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.dat`: 1x Excluded (Unsupported Extension: '.dat')
- `.init`: 1x Excluded (Unsupported Extension: '.INIT')
- `.ca7`: 1x Excluded (Unsupported Extension: '.ca7')
- `.controlm`: 1x Excluded (Unsupported Extension: '.controlm')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.9 | 18.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 32.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 48.0 | 3.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 82.2 | 1.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 13.6 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 90.0 | 1.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 62.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 58.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 96.0 | 0.6 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 767 | 54 | 12 | `app/app-authorization-ims-db2-mq/cpy-bms/COPAU00.cpy` |
| cleanup | 104 | 44 | 2 | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` |
| guards | 188 | 46 | 3 | `app/asm/COBDATFT.asm` |
| danger | 375 | 56 | 2 | `app/cbl/COACTUPC.cbl` |
| concurrency | 61 | 27 | 1 | `samples/jcl/IMSMQCMP.jcl` |
| connectivity | 202 | 47 | 1 | `app/cbl/CBEXPORT.cbl` |
| io | 1622 | 110 | 22 | `app/cbl/CBSTM03A.CBL` |
| crypto | 0 | 0 | 0 | - |
| ipc | 205 | 45 | 4 | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` |
| time | 100 | 39 | 2 | `app/cbl/CBIMPORT.cbl` |
| serialization | 267 | 26 | 2 | `app/cbl/COACTUPC.cbl` |
| regex | 83 | 18 | 0 | `app/cbl/COACTUPC.cbl` |
| events | 107 | 79 | 2 | `app/app-vsam-mq/cbl/COACCT01.cbl` |
| tests | 0 | 0 | 0 | - |
| docs | 18 | 9 | 0 | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` |
| debt | 639 | 41 | 12 | `app/cbl/CBTRN03C.cbl` |
| mutation | 7155 | 120 | 114 | `app/cbl/COACTUPC.cbl` |
| dead_code | 154 | 50 | 2 | `app/cbl/COCRDLIC.cbl` |
| credential | 2 | 2 | 0 | `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL` |
| threat | 1126 | 69 | 20 | `app/cbl/COACTUPC.cbl` |
| ml_ai | 4 | 2 | 0 | `scripts/upld_module.sh` |
| ui | 40 | 21 | 1 | `app/cbl/COACTVWC.cbl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/cbl/CBSTM03A.CBL` (Hits: 143)
- `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` (Hits: 111)
- `app/cbl/COACTUPC.cbl` (Hits: 101)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **COCOM01Y.cpy** (`app/cpy/COCOM01Y.cpy`) — 21 inbound connections
2. **COTTL01Y.cpy** (`app/cpy/COTTL01Y.cpy`) — 21 inbound connections
3. **CSDAT01Y.cpy** (`app/cpy/CSDAT01Y.cpy`) — 21 inbound connections
4. **CSMSG01Y.cpy** (`app/cpy/CSMSG01Y.cpy`) — 21 inbound connections
5. **CSUSR01Y.cpy** (`app/cpy/CSUSR01Y.cpy`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **BLDCIDB2.prc** (`samples/proc/BLDCIDB2.prc`) — 20 outbound dependencies
2. **COACTUPC.cbl** (`app/cbl/COACTUPC.cbl`) — 18 outbound dependencies
3. **COACTVWC.cbl** (`app/cbl/COACTVWC.cbl`) — 15 outbound dependencies
4. **IMSMQCMP.jcl** (`samples/jcl/IMSMQCMP.jcl`) — 14 outbound dependencies
5. **BUILDONL.prc** (`samples/proc/BUILDONL.prc`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `1100-RECEIVE-MAP` **(Compute Cores)** (@ `app/cbl/COACTUPC.cbl`) -> Impact: **117.3** | LOC: 387
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `app/cbl/COACTUPC.cbl`) -> Impact: **116.5** | LOC: 451
- `0000-MAIN` **(I/O & Config Routines)** (@ `app/app-transaction-type-db2/cbl/COTRTLIC.cbl`) -> Impact: **61.0** | LOC: 401
- `VALIDATE-INPUT-DATA-FIELDS` **(Compute Cores)** (@ `app/cbl/COTRN02C.cbl`) -> Impact: **56.1** | LOC: 203
  * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-DATA-FIELDS *-----------------------------------------------------...
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `app/cbl/COCRDUPC.cbl`) -> Impact: **47.5** | LOC: 151
- `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (@ `app/cbl/CORPT00C.cbl`) -> Impact: **41.5** | LOC: 249
  * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *--------------------------------------------------------------...
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `app/app-transaction-type-db2/cbl/COTRTUPC.cbl`) -> Impact: **38.8** | LOC: 95
- `0000-MAIN` **(I/O & Config Routines)** (@ `app/cbl/COCRDLIC.cbl`) -> Impact: **38.2** | LOC: 305
- `0000-MAIN` **(I/O & Config Routines)** (@ `app/app-transaction-type-db2/cbl/COTRTUPC.cbl`) -> Impact: **36.7** | LOC: 214
- `YYYY-STORE-PFKEY` **(Compute Cores)** (@ `app/cpy/CSSTRPFY.cpy`) -> Impact: **33.1** | LOC: 63
  * *Intent:* * All Rights Reserved. * * Licensed under the Apache License, Version 2.0 (the "License"). * You may not use this file except in compliance with the L...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `app/cbl` | 31 | 11386.78 | 70.99% | 13.65% |
| `app/app-authorization-ims-db2-mq/cbl` | 8 | 2119.86 | 52.47% | 18.77% |
| `app/app-transaction-type-db2/cbl` | 3 | 1999.7 | 69.26% | 16.36% |
| `app/app-vsam-mq/cbl` | 2 | 581.98 | 58.47% | 9.73% |
| `app/jcl` | 38 | 193.24 | 0.0% | 0.0% |
| `app/catlg` | 1 | 79.14 | 0.0% | 0.0% |
| `samples/proc` | 4 | 49.48 | 1.24% | 0.0% |
| `samples/jcl` | 9 | 48.76 | 0.0% | 0.0% |
| `app/cpy` | 29 | 41.06 | 6.22% | 0.0% |
| `app/asm` | 2 | 32.28 | 2.48% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `app/app-transaction-type-db2/cpy/CSDB2RPY.cpy` -> **47.985%** Exposure
- `app/cbl/CSUTLDTC.cbl` -> **32.1778%** Exposure
- `app/app-transaction-type-db2/cbl/COBTUPDT.cbl` -> **31.1593%** Exposure
- `app/app-authorization-ims-db2-mq/cbl/DBUNLDGS.CBL` -> **30.1275%** Exposure
- `app/app-authorization-ims-db2-mq/cbl/PAUDBUNL.CBL` -> **28.4261%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl` -> **100.0%** Exposure
- `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl` -> **100.0%** Exposure
- `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl` -> **100.0%** Exposure
- `app/cbl/CBCUS01C.cbl` -> **100.0%** Exposure
- `app/cbl/CBTRN01C.cbl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/cbl/COACTVWC.cbl` -> **2** Orphaned Functions | **2** Duplicates
- `app/cbl/COCRDLIC.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `app/cbl/COCRDSLC.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `app/app-authorization-ims-db2-mq/cbl/PAUDBLOD.CBL` -> **95.9799%** Exposure
- `app/app-transaction-type-db2/cbl/COTRTUPC.cbl` -> **16.1415%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `476` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `app/cbl/CBEXPORT.cbl` (COBOL) -> Cumulative Risk: **627.72**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.53)
- **Magnitude:** 284.62 | **LOC:** 583 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), State Flux (99.9835%)
- **Heaviest Functions:** `1100-OPEN-FILES` (I/O & Config Routines, Impact: 9.2), `2200-CREATE-CUSTOMER-EXP-REC` (I/O & Config Routines, Impact: 4.0), `5200-CREATE-TRAN-EXP-REC` (I/O & Config Routines, Impact: 3.9)

### 2. `app/cbl/CBIMPORT.cbl` (COBOL) -> Cumulative Risk: **624.63**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.70)
- **Magnitude:** 183.04 | **LOC:** 488 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), State Flux (99.9775%)
- **Heaviest Functions:** `1100-OPEN-FILES` (I/O & Config Routines, Impact: 10.5), `2200-PROCESS-RECORD-BY-TYPE` (I/O & Config Routines, Impact: 8.8), `2300-PROCESS-CUSTOMER-RECORD` (I/O & Config Routines, Impact: 3.7)

### 3. `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl` (COBOL) -> Cumulative Risk: **594.04**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.44)
- **Magnitude:** 495.32 | **LOC:** 1027 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (92.6067%)
- **Heaviest Functions:** `6000-MAKE-DECISION` (I/O & Config Routines, Impact: 23.8), `8400-UPDATE-SUMMARY` (I/O & Config Routines, Impact: 10.6), `8500-INSERT-AUTH` (I/O & Config Routines, Impact: 8.5)

### 4. `app/cbl/COCRDLIC.cbl` (COBOL) -> Cumulative Risk: **589.46**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +3.43)
- **Magnitude:** 735.86 | **LOC:** 1460 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (98.6301%), Safety Score (93.3686%)
- **Heaviest Functions:** `0000-MAIN` (I/O & Config Routines, Impact: 38.2), `9000-READ-FORWARD` (I/O & Config Routines, Impact: 28.9), `1250-SETUP-ARRAY-ATTRIBS` (I/O & Config Routines, Impact: 27.2)

### 5. `app/cbl/COUSR02C.cbl` (COBOL) -> Cumulative Risk: **585.13**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.51)
- **Magnitude:** 291.56 | **LOC:** 415 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.1571%)
- **Heaviest Functions:** `UPDATE-USER-INFO` (I/O & Config Routines, Impact: 18.4), `MAIN-PARA` (I/O & Config Routines, Impact: 17.9), `PROCESS-ENTER-KEY` (I/O & Config Routines, Impact: 7.5)

### 6. `app/cbl/COMEN01C.cbl` (COBOL) -> Cumulative Risk: **583.42**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.49)
- **Magnitude:** 191.56 | **LOC:** 309 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.3536%)
- **Heaviest Functions:** `BUILD-MENU-OPTIONS` (I/O & Config Routines, Impact: 19.1), `PROCESS-ENTER-KEY` (I/O & Config Routines, Impact: 15.8), `MAIN-PARA` (I/O & Config Routines, Impact: 10.8)

### 7. `app/cbl/COTRN02C.cbl` (COBOL) -> Cumulative Risk: **583.28**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.76)
- **Magnitude:** 570.98 | **LOC:** 784 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.7392%)
- **Heaviest Functions:** `VALIDATE-INPUT-DATA-FIELDS` (Compute Cores, Impact: 56.1), `MAIN-PARA` (I/O & Config Routines, Impact: 16.6), `PROCESS-ENTER-KEY` (I/O & Config Routines, Impact: 10.2)

### 8. `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` (COBOL) -> Cumulative Risk: **582.75**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.55)
- **Magnitude:** 1163.82 | **LOC:** 2099 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (99.1453%), Safety Score (93.6298%)
- **Heaviest Functions:** `0000-MAIN` (I/O & Config Routines, Impact: 61.0), `8000-READ-FORWARD` (I/O & Config Routines, Impact: 27.1), `2500-SETUP-MESSAGE` (I/O & Config Routines, Impact: 22.9)

### 9. `app/cbl/COACTUPC.cbl` (COBOL) -> Cumulative Risk: **581.58**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +3.19)
- **Magnitude:** 2199.06 | **LOC:** 4237 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.8095%), Safety Score (94.4424%)
- **Heaviest Functions:** `1100-RECEIVE-MAP` (Compute Cores, Impact: 117.3), `3300-SETUP-SCREEN-ATTRS` (I/O & Config Routines, Impact: 116.5), `2000-DECIDE-ACTION` (I/O & Config Routines, Impact: 24.1)

### 10. `app/cbl/COACTVWC.cbl` (COBOL) -> Cumulative Risk: **580.89**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +2.13)
- **Magnitude:** 392.66 | **LOC:** 942 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.999%), Documentation (94.6429%), Safety Score (89.8371%)
- **Heaviest Functions:** `0000-MAIN` (I/O & Config Routines, Impact: 23.6), `1200-SETUP-SCREEN-VARS` (I/O & Config Routines, Impact: 11.8), `1300-SETUP-SCREEN-ATTRS` (I/O & Config Routines, Impact: 10.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `app/cbl/COACTUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2199.06 | **LOC:** 4237 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.044%), Tech Debt (8.3472%)
**Top Internal Functions/Classes:**
  * `1100-RECEIVE-MAP` **(Compute Cores)** (Impact: 117.3)
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 116.5)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 24.1)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 23.4)
  * `1200-EDIT-MAP-INPUTS` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 384 instances
* *State Mutation (weighted view):* 1468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 299`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 700`, `dead_code: 14`, `unreferenced_by_name: 3`
* *Architecture:* `io: 101`, `api: 1`, `import: 56`
* *Defense:* `safety: 14`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` COACTUP, COCOM01Y, COTTL01Y, CSDAT01Y, CSLKPCDY, CSMSG01Y, CSMSG02Y, CSSETATY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1163.82 | **LOC:** 2099 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.3244%), Tech Debt (9.014%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 61.0)
  * `8000-READ-FORWARD` **(I/O & Config Routines)** (Impact: 27.1)
  * `2500-SETUP-MESSAGE` **(I/O & Config Routines)** (Impact: 22.9)
  * `2400-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 22.1)
  * `2300-SCREEN-ARRAY-INIT` **(I/O & Config Routines)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 759
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 238`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 321`, `dead_code: 9`, `unreferenced_by_name: 3`
* *Architecture:* `io: 111`, `api: 1`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` COCOM01Y, COTRTLI, COTTL01Y, CSDAT01Y, CSMSG01Y, CSSTRPFY, CSUSR01Y, CVACT02Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COCRDUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 814.0 | **LOC:** 1561 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.4449%), Tech Debt (9.1888%)
**Top Internal Functions/Classes:**
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 47.5)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 29.9)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 24.1)
  * `1100-RECEIVE-MAP` **(I/O & Config Routines)** (Impact: 15.9)
  * `3200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 509
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 132`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 283`, `dead_code: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 18`, `api: 1`, `import: 13`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` COCOM01Y, COCRDUP, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 777.34 | **LOC:** 1033 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.6647%), Tech Debt (9.0248%)
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 20.9)
    * *Intent:* *****************************************************************
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 19.0)
    * *Intent:* *****************************************************************
  * `POPULATE-AUTH-LIST` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *****************************************************************
  * `INITIALIZE-AUTH-DATA` **(I/O & Config Routines)** (Impact: 12.8)
    * *Intent:* *****************************************************************
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 12.0)
    * *Intent:* *****************************************************************
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 165 instances
* *State Mutation (weighted view):* 602
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 78`, `args: 3`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 272`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `api: 1`, `import: 14`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` CIPAUDTY, CIPAUSMY, COCOM01Y, COPAU00, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-transaction-type-db2/cbl/COTRTUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 761.98 | **LOC:** 1703 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.2173%), Tech Debt (8.9069%)
**Top Internal Functions/Classes:**
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 38.8)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 36.7)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 29.2)
  * `3250-SETUP-INFOMSG` **(I/O & Config Routines)** (Impact: 21.8)
  * `3200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 94 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 184`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 211`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 71`, `api: 1`, `import: 14`
* *Defense:* `safety: 5`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` COCOM01Y, COTRTUP, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSETATY, CSSTRPFY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COCRDLIC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 735.86 | **LOC:** 1460 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.1034%), Tech Debt (11.024%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 38.2)
  * `9000-READ-FORWARD` **(I/O & Config Routines)** (Impact: 28.9)
  * `1250-SETUP-ARRAY-ATTRIBS` **(I/O & Config Routines)** (Impact: 27.2)
  * `9100-READ-BACKWARDS` **(I/O & Config Routines)** (Impact: 19.4)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 143`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 297`, `dead_code: 17`, `unreferenced_by_name: 4`
* *Architecture:* `io: 44`, `api: 1`, `import: 11`
* *Defense:* `safety: 10`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` COCOM01Y, COCRDLI, COTTL01Y, CSDAT01Y, CSMSG01Y, CSSTRPFY, CSUSR01Y, CVACT02Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COTRN00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 688.58 | **LOC:** 700 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.8928%), Tech Debt (9.8283%)
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `POPULATE-TRAN-DATA` **(I/O & Config Routines)** (Impact: 16.2)
    * *Intent:* *----------------------------------------------------------------* * POPULATE-TRAN-DATA *-----------...
  * `INITIALIZE-TRAN-DATA` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* *----------------------------------------------------------------* * INITIALIZE-TRAN-DATA *---------...
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 15.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-FORWARD *---------...
  * `PROCESS-PAGE-BACKWARD` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-BACKWARD *--------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 64`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 200`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` COCOM01Y, COTRN00, COTTL01Y, CSDAT01Y, CSMSG01Y, CVTRA05Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COUSR00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 675.32 | **LOC:** 696 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6075%), Tech Debt (9.8189%)
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `POPULATE-USER-DATA` **(I/O & Config Routines)** (Impact: 15.9)
    * *Intent:* *----------------------------------------------------------------* * POPULATE-USER-DATA *-----------...
  * `INITIALIZE-USER-DATA` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* *----------------------------------------------------------------* * INITIALIZE-USER-DATA *---------...
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 15.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-FORWARD *---------...
  * `PROCESS-PAGE-BACKWARD` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-BACKWARD *--------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 163 instances
* *State Mutation (weighted view):* 521
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 63`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 195`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` COCOM01Y, COTTL01Y, COUSR00, CSDAT01Y, CSMSG01Y, CSUSR01Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COTRN02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 570.98 | **LOC:** 784 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.9716%), Tech Debt (9.4859%)
**Top Internal Functions/Classes:**
  * `VALIDATE-INPUT-DATA-FIELDS` **(Compute Cores)** (Impact: 56.1)
    * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-DATA-FIELDS *---...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 16.6)
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `VALIDATE-INPUT-KEY-FIELDS` **(I/O & Config Routines)** (Impact: 8.9)
    * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-KEY-FIELDS *----...
  * `WRITE-TRANSACT-FILE` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* *----------------------------------------------------------------* * WRITE-TRANSACT-FILE *----------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 84`, `args: 2`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 190`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `api: 1`, `import: 11`
* *Defense:* `safety: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` COCOM01Y, COTRN02, COTTL01Y, CSDAT01Y, CSMSG01Y, CVACT01Y, CVACT03Y, CVTRA05Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 495.32 | **LOC:** 1027 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.6067%), Tech Debt (11.4453%)
**Top Internal Functions/Classes:**
  * `6000-MAKE-DECISION` **(I/O & Config Routines)** (Impact: 23.8)
    * *Intent:* * * ------------------------------------------------------------- *
  * `8400-UPDATE-SUMMARY` **(I/O & Config Routines)** (Impact: 10.6)
    * *Intent:* * * ------------------------------------------------------------- *
  * `8500-INSERT-AUTH` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* * * ------------------------------------------------------------- *
  * `3100-READ-REQUEST-MQ` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* * * ------------------------------------------------------------- *
  * `5100-READ-XREF-RECORD` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* * * ------------------------------------------------------------- *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 139`, `args: 8`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 228`, `unreferenced_by_name: 3`
* *Architecture:* `io: 41`, `api: 4`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` CCPAUERY, CCPAURLY, CCPAURQY, CIPAUDTY, CIPAUSMY, CMQGMOV, CMQMDV, CMQODV...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CBTRN02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 410.18 | **LOC:** 732 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.0583%), Tech Debt (9.469%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 17.4)
  * `1000-DALYTRAN-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *---------------------------------------------------------------*
  * `2700-UPDATE-TCATBAL` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* *---------------------------------------------------------------*
  * `1500-B-LOOKUP-ACCT` **(I/O & Config Routines)** (Impact: 8.5)
  * `2700-A-CREATE-TCATBAL-REC` **(I/O & Config Routines)** (Impact: 6.1)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 160`, `args: 2`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 136`, `unreferenced_by_name: 1`
* *Architecture:* `io: 36`, `import: 5`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CVACT01Y, CVACT03Y, CVTRA01Y, CVTRA05Y, CVTRA06Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COCRDSLC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 402.04 | **LOC:** 888 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.4396%), Tech Debt (14.1965%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 25.2)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 18.9)
  * `1200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 11.1)
  * `Today` **(I/O & Config Routines)** (Impact: 9.5)
  * `9100-GETCARD-BYACCTCARD` **(I/O & Config Routines)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 82`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 138`, `dead_code: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`, `api: 1`, `import: 13`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` COCOM01Y, COCRDSL, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CBSTM03A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 398.48 | **LOC:** 925 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (9.0407%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 20.0)
  * `0000-START` **(I/O & Config Routines)** (Impact: 8.9)
  * `8500-READTRNX-READ` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* *---------------------------------------------------------------*
  * `4000-TRNXFILE-GET` **(I/O & Config Routines)** (Impact: 8.1)
  * `8100-TRNXFILE-OPEN` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 4 instances
* *Amplified Cascading Flux:* 40 instances
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 112`, `args: 13`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 4`, `state_mutation: 183`, `unreferenced_by_name: 1`
* *Architecture:* `io: 143`, `api: 4`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` COSTM01, CUSTREC, CVACT01Y, CVACT03Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COACTVWC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 392.66 | **LOC:** 942 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.0147%), Tech Debt (19.2609%)
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 23.6)
  * `1200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 11.8)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 10.6)
  * `Today` **(I/O & Config Routines)** (Impact: 8.5)
  * `9200-GETCARDXREF-BYACCT` **(I/O & Config Routines)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 84`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 153`, `dead_code: 6`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 18`, `api: 1`, `import: 15`
* *Defense:* `safety: 8`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` COACTVW, COCOM01Y, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 371.22 | **LOC:** 605 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.0319%), Tech Debt (10.2053%)
**Top Internal Functions/Classes:**
  * `READ-AUTH-RECORD` **(I/O & Config Routines)** (Impact: 15.1)
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 13.5)
  * `POPULATE-AUTH-DETAILS` **(I/O & Config Routines)** (Impact: 11.4)
  * `MARK-AUTH-FRAUD` **(I/O & Config Routines)** (Impact: 8.8)
  * `UPDATE-AUTH-DETAILS` **(I/O & Config Routines)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 42`, `args: 4`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 120`, `unreferenced_by_name: 1`
* *Architecture:* `io: 13`, `api: 2`, `import: 10`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` CIPAUDTY, CIPAUSMY, COCOM01Y, COPAU01, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CORPT00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 369.76 | **LOC:** 650 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.2228%), Tech Debt (9.9859%)
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 41.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `SUBMIT-JOB-TO-INTRDR` **(I/O & Config Routines)** (Impact: 12.4)
    * *Intent:* *----------------------------------------------------------------* * SUBMIT-JOB-TO-INTRDR *---------...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 11.0)
  * `WIRTE-JOBSUB-TDQ` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* *----------------------------------------------------------------* * WIRTE-JOBSUB-TDQ *-------------...
  * `SEND-TRNRPT-SCREEN` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* *----------------------------------------------------------------* * SEND-TRNRPT-SCREEN *-----------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 49`, `args: 2`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 147`, `unreferenced_by_name: 1`
* *Architecture:* `io: 35`, `api: 1`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` COCOM01Y, CORPT00, COTTL01Y, CSDAT01Y, CSMSG01Y, CVTRA05Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CBACT04C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 341.04 | **LOC:** 653 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.3908%), Tech Debt (9.7241%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 19.3)
  * `1000-TCATBALF-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *---------------------------------------------------------------*
  * `1200-GET-INTEREST-RATE` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* *---------------------------------------------------------------*
  * `1300-B-WRITE-TX` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* *---------------------------------------------------------------*
  * `1100-GET-ACCT-DATA` **(I/O & Config Routines)** (Impact: 7.0)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 149`, `args: 3`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`, `unreferenced_by_name: 1`
* *Architecture:* `io: 28`, `api: 1`, `import: 5`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CVACT01Y, CVACT03Y, CVTRA01Y, CVTRA02Y, CVTRA05Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CBTRN03C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 337.5 | **LOC:** 650 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.0009%), Tech Debt (9.7548%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 18.5)
  * `0550-DATEPARM-READ` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* * Read the date parameter file.
  * `1000-TRANFILE-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* ***************************************************************** * I/O ROUTINES TO ACCESS A KSDS, V...
  * `1111-WRITE-REPORT-REC` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `0000-TRANFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 166`, `args: 2`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 116`, `unreferenced_by_name: 1`
* *Architecture:* `io: 60`, `import: 5`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CVACT03Y, CVTRA03Y, CVTRA04Y, CVTRA05Y, CVTRA07Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COBIL00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 335.2 | **LOC:** 573 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.0215%), Tech Debt (10.5001%)
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 22.6)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 15.6)
  * `WRITE-TRANSACT-FILE` **(I/O & Config Routines)** (Impact: 7.9)
    * *Intent:* *----------------------------------------------------------------* * WRITE-TRANSACT-FILE *----------...
  * `READ-ACCTDAT-FILE` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* *----------------------------------------------------------------* * READ-ACCTDAT-FILE *------------...
  * `READ-CXACAIX-FILE` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* *----------------------------------------------------------------* * READ-CXACAIX-FILE *------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 57`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`, `unreferenced_by_name: 1`
* *Architecture:* `io: 14`, `api: 1`, `import: 10`
* *Defense:* `safety: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` COBIL00, COCOM01Y, COTTL01Y, CSDAT01Y, CSMSG01Y, CVACT01Y, CVACT03Y, CVTRA05Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CBTRN01C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 313.8 | **LOC:** 495 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.8989%), Tech Debt (13.0381%)
**Top Internal Functions/Classes:**
  * `1000-DALYTRAN-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* ***************************************************************** * READS FILE * *******************...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 9.2)
  * `0000-DALYTRAN-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `0100-CUSTFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `0200-XREFFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 120`, `args: 2`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `unreferenced_by_name: 2`
* *Architecture:* `io: 36`, `import: 6`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` CVACT01Y, CVACT02Y, CVACT03Y, CVCUS01Y, CVTRA05Y, CVTRA06Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-vsam-mq/cbl/COACCT01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 310.22 | **LOC:** 621 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.5901%), Tech Debt (9.5314%)
**Top Internal Functions/Classes:**
  * `4000-PROCESS-REQUEST-REPLY` **(I/O & Config Routines)** (Impact: 10.6)
  * `3000-GET-REQUEST` **(I/O & Config Routines)** (Impact: 8.8)
  * `4100-PUT-REPLY` **(I/O & Config Routines)** (Impact: 7.0)
  * `2100-OPEN-ERROR-QUEUE` **(I/O & Config Routines)** (Impact: 6.8)
  * `9000-ERROR` **(I/O & Config Routines)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 215
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 46`, `args: 9`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 141`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `api: 1`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CMQGMOV, CMQMDV, CMQODV, CMQPMOV, CMQTML, CMQV, CVACT01Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/COUSR02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 291.56 | **LOC:** 415 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.8102%), Tech Debt (11.8684%)
**Top Internal Functions/Classes:**
  * `UPDATE-USER-INFO` **(I/O & Config Routines)** (Impact: 18.4)
    * *Intent:* *----------------------------------------------------------------* * UPDATE-USER-INFO *-------------...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 17.9)
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 7.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `READ-USER-SEC-FILE` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* *----------------------------------------------------------------* * READ-USER-SEC-FILE *-----------...
  * `UPDATE-USER-SEC-FILE` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* *----------------------------------------------------------------* * UPDATE-USER-SEC-FILE *---------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 43`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 1`, `import: 8`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` COCOM01Y, COTTL01Y, COUSR02, CSDAT01Y, CSMSG01Y, CSUSR01Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CBEXPORT.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 284.62 | **LOC:** 583 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.224%), Tech Debt (13.3694%)
**Top Internal Functions/Classes:**
  * `1100-OPEN-FILES` **(I/O & Config Routines)** (Impact: 9.2)
    * *Intent:* *****************************************************************
  * `2200-CREATE-CUSTOMER-EXP-REC` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* *****************************************************************
  * `5200-CREATE-TRAN-EXP-REC` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* *****************************************************************
  * `3200-CREATE-ACCOUNT-EXP-REC` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* *****************************************************************
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 97`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 100`, `unreferenced_by_name: 2`
* *Architecture:* `io: 41`, `api: 95`, `import: 6`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` CVACT01Y, CVACT02Y, CVACT03Y, CVCUS01Y, CVEXPORT, CVTRA05Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-vsam-mq/cbl/CODATE01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 271.76 | **LOC:** 525 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.3499%), Tech Debt (9.9327%)
**Top Internal Functions/Classes:**
  * `3000-GET-REQUEST` **(I/O & Config Routines)** (Impact: 8.8)
  * `4100-PUT-REPLY` **(I/O & Config Routines)** (Impact: 7.0)
  * `2100-OPEN-ERROR-QUEUE` **(I/O & Config Routines)** (Impact: 6.8)
  * `9000-ERROR` **(I/O & Config Routines)** (Impact: 6.8)
  * `2300-OPEN-INPUT-QUEUE` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 42`, `args: 9`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`, `unreferenced_by_name: 1`
* *Architecture:* `io: 15`, `api: 1`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CMQGMOV, CMQMDV, CMQODV, CMQPMOV, CMQTML, CMQV
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/cbl/CBACT01C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 234.86 | **LOC:** 431 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.8725%), Tech Debt (11.0957%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 13.7)
  * `1000-ACCTFILE-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.7)
    * *Intent:* ***************************************************************** * I/O ROUTINES TO ACCESS A KSDS, V...
  * `0000-ACCTFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `2000-OUTFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
  * `3000-ARRFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 108`, `args: 3`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 35`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CODATECN, CVACT01Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/cbl/CBEXPORT.cbl` -> **Arunkumar Selvam** (100.0% isolated ownership) | Magnitude: 284.62
- `app/cbl/CBIMPORT.cbl` -> **Arunkumar Selvam** (100.0% isolated ownership) | Magnitude: 183.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `app/cpy/CSSTRPFY.cpy` -> **Severity: 3.139** (Embedded: 0.0315 * Error Risk: 99.5536%)
- `app/cpy/CSSETATY.cpy` -> **Severity: 0.608** (Embedded: 0.009 * Error Risk: 67.4492%)
- `app/cpy/CSUTLDPY.cpy` -> **Severity: 0.442** (Embedded: 0.0045 * Error Risk: 98.07%)
- `app/cpy/COADM02Y.cpy` -> **Severity: 0.266** (Embedded: 0.0045 * Error Risk: 59.0077%)
- `app/cpy/COMEN02Y.cpy` -> **Severity: 0.259** (Embedded: 0.0045 * Error Risk: 57.5315%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `app/cpy/CSSTRPFY.cpy` -> **Severity: 622.7** (Blast Radius: 6.227 * Doc Risk: 100.0%)
- `app/cpy/CSUTLDPY.cpy` -> **Severity: 412.5** (Blast Radius: 4.125 * Doc Risk: 100.0%)
- `app/app-authorization-ims-db2-mq/jcl/CBPAUP0J.jcl` -> **Severity: 390.4** (Blast Radius: 3.904 * Doc Risk: 100.0%)
- `app/app-authorization-ims-db2-mq/jcl/DBPAUTP0.jcl` -> **Severity: 390.4** (Blast Radius: 3.904 * Doc Risk: 100.0%)
- `app/app-authorization-ims-db2-mq/jcl/LOADPADB.JCL` -> **Severity: 390.4** (Blast Radius: 3.904 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
