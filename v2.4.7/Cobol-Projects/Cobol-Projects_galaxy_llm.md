# ARCHITECTURAL_BRIEF: Cobol-Projects
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/Cobol-Projects` |
| **Timestamp** | `2026-08-07T03:50:09.779238+00:00` |
| **Scan Duration** | `0.76s` |
| **Git Branch** | `release` |
| **Git Commit** | `2cc05108d07d8d1ee2297e4f5bd6d274638b7f6e` |
| **Git Remote** | `https://github.com/dscobol/Cobol-Projects.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 272 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 25.2 | 15.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 69.9 | 78.4 | 98.7 |
| Tech Debt Exposure | 0.0 | 100.0 | 60.6 | 96.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.3 | 2.3 | 1.8 |
| API Exposure | 0.0 | 11.8 | 0.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 73.9 | 99.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 81.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.3 | 99.6 | 35.0 | 31.3 | 48.6 |
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

- `2000-Process` (@ `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl`) -> Impact: **165.9** | LOC: 320
- `2900-Display-The-Tables` (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> Impact: **137.5** | LOC: 190
  * *Intent:* * Find EVERYBODY who's studied BIOL ogy
- `2900-Display-The-Tables` (@ `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl`) -> Impact: **137.5** | LOC: 190
  * *Intent:* * Find EVERYBODY who's studied BIOL ogy * Use a REF-MOD to filter out all the classes. * Note the difference between this search and the next....
- `2900-Display-The-Tables` (@ `OpenCobol/ECBAP/cbl/tablena.cbl`) -> Impact: **137.5** | LOC: 190
- `2900-Display-The-Tables` (@ `OpenCobol/ECBAP/cbl/tablewa.cbl`) -> Impact: **137.5** | LOC: 190
- `2000-Process` (@ `OpenCobol/ECBAP/cbl/TABLE1.cbl`) -> Impact: **85.7** | LOC: 186
- `2200-Do-Some-Searching` (@ `OpenCobol/ECBAP/cbl/tablena.cbl`) -> Impact: **58.2** | LOC: 185
- `2200-Do-Some-Searching` (@ `OpenCobol/ECBAP/cbl/tablewa.cbl`) -> Impact: **58.2** | LOC: 185
- `2200-Do-Some-Searching` (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> Impact: **57.9** | LOC: 178
- `2200-Do-Some-Searching` (@ `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl`) -> Impact: **57.9** | LOC: 178

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `OpenCobol/ECBAP/cbl` | 59 | 5127.12 | 31.79% | 47.1% |
| `Mainframe/ZOS/ECBAP/cbl` | 25 | 4197.06 | 41.19% | 64.84% |
| `OpenCobol/dastagg/cbl` | 28 | 1121.46 | 33.81% | 43.86% |
| `Mainframe/ZOS/Normal/cbl` | 16 | 773.86 | 42.89% | 79.49% |
| `OpenCobol/ECBAP/jcl` | 37 | 496.72 | 5.79% | 99.99% |
| `Mainframe/ZOS/Normal/jcl` | 9 | 449.36 | 16.36% | 0.0% |
| `OpenCobol/prod/cbl` | 11 | 344.7 | 41.55% | 90.66% |
| `Mainframe/ZOS/Internal-Sort/cbl` | 5 | 206.74 | 23.87% | 99.97% |
| `OpenCobol/Internal-Sort/cbl` | 5 | 206.74 | 23.87% | 99.97% |
| `pgm_templates/CICS` | 2 | 194.86 | 82.15% | 98.93% |

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

1. **`Mainframe/ZOS/Zowe/Initialize/SCRIPTS/cleanup.sh`** -> AI Confidence: **99.29%**
2. **`Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/cleanup.sh`** -> AI Confidence: **99.29%**
3. **`OpenCobol/ECBAP/jcl/CHARFUNC.sh`** -> AI Confidence: **99.29%**
4. **`OpenCobol/ECBAP/jcl/FAHR2CEL.sh`** -> AI Confidence: **99.29%**
5. **`OpenCobol/ECBAP/jcl/FAVRPT.sh`** -> AI Confidence: **99.29%**
6. **`OpenCobol/ECBAP/jcl/FILECALC.sh`** -> AI Confidence: **99.29%**
7. **`OpenCobol/ECBAP/jcl/HOSPEDIT.sh`** -> AI Confidence: **99.29%**
8. **`OpenCobol/ECBAP/jcl/INSPECT1.sh`** -> AI Confidence: **99.29%**
9. **`OpenCobol/ECBAP/jcl/INTEG1.sh`** -> AI Confidence: **99.29%**
10. **`OpenCobol/ECBAP/jcl/INTRDATE.sh`** -> AI Confidence: **99.29%**
11. **`OpenCobol/ECBAP/jcl/INTRFINA.sh`** -> AI Confidence: **99.29%**
12. **`OpenCobol/ECBAP/jcl/INTRNUM.sh`** -> AI Confidence: **99.29%**
13. **`OpenCobol/ECBAP/jcl/INTRSTAT.sh`** -> AI Confidence: **99.29%**
14. **`OpenCobol/ECBAP/jcl/PAYROL01.sh`** -> AI Confidence: **99.29%**
15. **`OpenCobol/ECBAP/jcl/PAYROL0B.sh`** -> AI Confidence: **99.29%**
16. **`OpenCobol/ECBAP/jcl/STRING1.sh`** -> AI Confidence: **99.29%**
17. **`OpenCobol/ECBAP/jcl/STRING2.sh`** -> AI Confidence: **99.29%**
18. **`OpenCobol/ECBAP/jcl/TABLE1.sh`** -> AI Confidence: **99.29%**
19. **`OpenCobol/ECBAP/jcl/TABLES01.sh`** -> AI Confidence: **99.29%**
20. **`OpenCobol/ECBAP/jcl/TABLOAD1.sh`** -> AI Confidence: **99.29%**
21. **`OpenCobol/ECBAP/jcl/TABLOAD2.sh`** -> AI Confidence: **99.29%**
22. **`OpenCobol/ECBAP/jcl/TRIM1.sh`** -> AI Confidence: **99.29%**
23. **`OpenCobol/ECBAP/jcl/UNSTRNG.sh`** -> AI Confidence: **99.29%**
24. **`OpenCobol/ECBAP/jcl/WS120.sh`** -> AI Confidence: **99.29%**
25. **`OpenCobol/ECBAP/jcl/WS162E.sh`** -> AI Confidence: **99.29%**
26. **`OpenCobol/ECBAP/jcl/WS172A.sh`** -> AI Confidence: **99.29%**
27. **`OpenCobol/ECBAP/jcl/WS532.sh`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `OpenCobol/ECBAP/cbl/ws81c.cbl` -> **75.3102%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` -> **73.5779%** Exposure
- `OpenCobol/ECBAP/cbl/ws81d.cbl` -> **61.0229%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` -> **59.2107%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` -> **49.6269%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `108` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Mainframe/ZOS/Zowe/Create_Test_DataSet/create-vsam/allocate.sh` (SHELL) -> Cumulative Risk: **616.71**
- **Archetype:** `file_cluster_8` (Distance: 11.668 IQR)
- **Magnitude:** 14.8 | **LOC:** 55 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9996%)
- **Heaviest Functions:** `__global_context__` (Impact: 2.5)

### 2. `Mainframe/ZOS/Zowe/Create_Test_DataSet/zowe-only-method/allocate.sh` (SHELL) -> Cumulative Risk: **611.3**
- **Archetype:** `file_cluster_8` (Distance: 11.393 IQR)
- **Magnitude:** 18.02 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9998%), Concurrency (99.9595%)
- **Heaviest Functions:** `__global_context__` (Impact: 1.5)

### 3. `Mainframe/ZOS/Zowe/Simple_Report/SCRIPTS/run-project.sh` (SHELL) -> Cumulative Risk: **602.96**
- **Archetype:** `file_cluster_4` (Distance: 20.345 IQR)
- **Magnitude:** 1.28 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (99.9999%), Concurrency (99.9978%), State Flux (99.9911%), Spec Match (93.3333%)
- **Heaviest Functions:** `__global_context__` (Impact: 2.5)

### 4. `OpenCobol/ECBAP/cbl/ws81c.cbl` (COBOL) -> Cumulative Risk: **602.14**
- **Archetype:** `file_cluster_8` (Distance: 11.69 IQR)
- **Magnitude:** 256.32 | **LOC:** 523 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9959%), Tech Debt (87.1595%), Verification (80.0%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 43.6), `2100-Create-RFP` (Impact: 8.8), `5100-Read-RFPIN` (Impact: 8.8)

### 5. `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` (COBOL) -> Cumulative Risk: **597.75**
- **Archetype:** `file_cluster_8` (Distance: 11.635 IQR)
- **Magnitude:** 256.54 | **LOC:** 508 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9945%), Tech Debt (85.8937%), Verification (80.0%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 43.6), `2100-Create-RFP` (Impact: 8.8), `5100-Read-RFPIN` (Impact: 8.8)

### 6. `OpenCobol/ECBAP/cbl/ws81d.cbl` (COBOL) -> Cumulative Risk: **596.53**
- **Archetype:** `file_cluster_8` (Distance: 12.443 IQR)
- **Magnitude:** 345.4 | **LOC:** 627 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9987%), Tech Debt (93.3486%), Verification (80.0%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 43.6), `2100-Create-RFP` (Impact: 12.2), `5100-Read-RFPIN` (Impact: 8.8)

### 7. `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` (COBOL) -> Cumulative Risk: **591.99**
- **Archetype:** `file_cluster_8` (Distance: 12.384 IQR)
- **Magnitude:** 345.66 | **LOC:** 626 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9982%), Tech Debt (92.5423%), Verification (80.0%)
- **Heaviest Functions:** `2120-Calculate-Inst-Price` (Impact: 43.6), `2100-Create-RFP` (Impact: 12.2), `5100-Read-RFPIN` (Impact: 8.8)

### 8. `pgm_templates/CICS/basecics.cbl` (COBOL) -> Cumulative Risk: **584.51**
- **Archetype:** `file_cluster_8` (Distance: 13.024 IQR)
- **Magnitude:** 192.82 | **LOC:** 336 | **CtrlFlow:** 88.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.1551%), Cognitive Load (97.4017%)
- **Heaviest Functions:** `WCM-A-HOURLY-WAGE` (Impact: 24.2), `0000-MAINLINE` (Impact: 13.8), `1000-RECIEVE-MAP` (Impact: 6.9)

### 9. `Mainframe/ZOS/ECBAP/scripts/upload_data.sh` (SHELL) -> Cumulative Risk: **582.77**
- **Archetype:** `file_cluster_12` (Distance: 9.801 IQR)
- **Magnitude:** 1.35 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Concurrency (99.2509%), Tech Debt (89.0107%)
- **Heaviest Functions:** `__global_context__` (Impact: 1.5)

### 10. `OpenCobol/ECBAP/cbl/TABLES01.cbl` (COBOL) -> Cumulative Risk: **576.75**
- **Archetype:** `file_cluster_8` (Distance: 12.344 IQR)
- **Magnitude:** 127.74 | **LOC:** 202 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (95.4302%), Verification (80.0%)
- **Heaviest Functions:** `400-TOTAL-PROJ-EXPENSE` (Impact: 8.8), `000-HOUSEKEEPING` (Impact: 8.7), `410-Calculate-Employee-Expense` (Impact: 7.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `OpenCobol/ECBAP/cbl/tablena.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.56 IQR)
- **Top Global Matches:** file_cluster_8: 11.56, file_cluster_7: 12.172, file_cluster_0: 12.228
- **Magnitude:** 547.94 | **LOC:** 1244 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.6449%), Tech Debt (73.0205%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 137.5)
  * `2200-Do-Some-Searching` (Impact: 58.2)
  * `WS-Show-Number` (Impact: 23.1)
  * `WS-Company-Counter` (Impact: 16.1)
  * `WS-Company-Total` (Impact: 14.6)
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
- **Magnitude:** 547.36 | **LOC:** 1235 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.3504%), Tech Debt (73.6191%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 137.5)
    * *Intent:* * Find EVERYBODY who's studied BIOL ogy
  * `2200-Do-Some-Searching` (Impact: 57.9)
  * `WS-Show-Number` (Impact: 23.1)
  * `WS-Company-Counter` (Impact: 16.1)
  * `WS-Company-Total` (Impact: 14.6)
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
- **Magnitude:** 453.36 | **LOC:** 1198 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.8411%), Tech Debt (73.7316%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 137.5)
  * `2200-Do-Some-Searching` (Impact: 58.2)
  * `WS-Company-Total` (Impact: 17.3)
    * *Intent:* * On to 3D tables. This is "Company Data". * It breaks down into: * Division: * Region:...
  * `WS-Company-Total` (Impact: 10.5)
  * `WS-Company-Total` (Impact: 10.5)
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
- **Magnitude:** 452.78 | **LOC:** 1189 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.4069%), Tech Debt (74.3494%)
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` (Impact: 137.5)
    * *Intent:* * Find EVERYBODY who's studied BIOL ogy * Use a REF-MOD to filter out all the classes. * Note the di...
  * `2200-Do-Some-Searching` (Impact: 57.9)
  * `WS-Company-Total` (Impact: 17.3)
    * *Intent:* * On to 3D tables. This is "Company Data". * It breaks down into: * Division: * Region:...
  * `WS-Company-Total` (Impact: 10.5)
  * `WS-Company-Total` (Impact: 10.5)
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
- **Magnitude:** 375.3 | **LOC:** 710 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.5919%), Tech Debt (88.6598%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 43.6)
  * `2100-Create-RFP` (Impact: 13.5)
  * `5100-Read-RFPIN` (Impact: 8.8)
  * `2180-Validate-RFP-Record` (Impact: 8.4)
  * `6100-Write-R1` (Impact: 7.3)
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
- **Magnitude:** 375.3 | **LOC:** 702 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.5919%), Tech Debt (88.6598%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 43.6)
  * `2100-Create-RFP` (Impact: 13.5)
  * `5100-Read-RFPIN` (Impact: 8.8)
  * `2180-Validate-RFP-Record` (Impact: 8.4)
  * `6100-Write-R1` (Impact: 7.3)
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

### `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.618 IQR)
- **Top Global Matches:** file_cluster_8: 11.618, file_cluster_0: 12.049, file_cluster_13: 12.084
- **Magnitude:** 347.04 | **LOC:** 639 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.2981%), Tech Debt (30.1678%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 165.9)
  * `1015-Load-Type` (Impact: 9.1)
  * `1099-Verify-Type-Table` (Impact: 7.8)
  * `1010-Load-Type-Table` (Impact: 4.3)
  * `0000-Mainline` (Impact: 4.2)
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

### `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.384 IQR)
- **Top Global Matches:** file_cluster_8: 12.384, file_cluster_17: 12.797, file_cluster_0: 12.82
- **Magnitude:** 345.66 | **LOC:** 626 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.1784%), Tech Debt (92.5423%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 43.6)
  * `2100-Create-RFP` (Impact: 12.2)
  * `5100-Read-RFPIN` (Impact: 8.8)
  * `2180-Validate-RFP-Record` (Impact: 8.4)
  * `6100-Write-R1` (Impact: 7.3)
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
- **Magnitude:** 345.4 | **LOC:** 627 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.1337%), Tech Debt (93.3486%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 43.6)
  * `2100-Create-RFP` (Impact: 12.2)
  * `5100-Read-RFPIN` (Impact: 8.8)
  * `2180-Validate-RFP-Record` (Impact: 8.4)
  * `6100-Write-R1` (Impact: 7.3)
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

### `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.111 IQR)
- **Top Global Matches:** file_cluster_8: 12.111, file_cluster_13: 12.45, file_cluster_17: 12.642
- **Magnitude:** 338.38 | **LOC:** 696 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.1754%), Tech Debt (99.4553%)
**Top Internal Functions/Classes:**
  * `2100-Process-INFile-Records` (Impact: 13.1)
  * `6135-Display-Ins-Type-Messages` (Impact: 13.1)
  * `1015-Load-Type` (Impact: 9.1)
  * `WS-OutFile-Patient-NAME` (Impact: 8.8)
  * `5000-Read-INFILE` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 49`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 194`, `fragile_debt: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 51`, `import: 8`
* *Defense:* `safety: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSDT, WSFST, PATIENT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws162e.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.114 IQR)
- **Top Global Matches:** file_cluster_8: 12.114, file_cluster_13: 12.445, file_cluster_17: 12.64
- **Magnitude:** 338.38 | **LOC:** 696 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.1754%), Tech Debt (99.4553%)
**Top Internal Functions/Classes:**
  * `2100-Process-INFile-Records` (Impact: 13.1)
  * `6135-Display-Ins-Type-Messages` (Impact: 13.1)
  * `1015-Load-Type` (Impact: 9.1)
  * `WS-OutFile-Patient-NAME` (Impact: 8.8)
  * `5000-Read-INFILE` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 49`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 194`, `fragile_debt: 1`, `orphaned_logic: 27`
* *Architecture:* `io: 51`, `import: 8`
* *Defense:* `safety: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSDT, WSFST, PATIENT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.635 IQR)
- **Top Global Matches:** file_cluster_8: 11.635, file_cluster_0: 12.164, file_cluster_17: 12.168
- **Magnitude:** 256.54 | **LOC:** 508 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4732%), Tech Debt (85.8937%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 43.6)
  * `2100-Create-RFP` (Impact: 8.8)
  * `5100-Read-RFPIN` (Impact: 8.8)
  * `6100-Write-R1` (Impact: 7.3)
  * `2110-Move-Fixed-Fields` (Impact: 7.2)
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
- **Magnitude:** 256.32 | **LOC:** 523 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.5251%), Tech Debt (87.1595%)
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` (Impact: 43.6)
  * `2100-Create-RFP` (Impact: 8.8)
  * `5100-Read-RFPIN` (Impact: 8.8)
  * `6100-Write-R1` (Impact: 7.3)
  * `2110-Move-Fixed-Fields` (Impact: 7.2)
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

### `OpenCobol/ECBAP/cbl/ws172a.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.852 IQR)
- **Top Global Matches:** file_cluster_8: 11.852, file_cluster_13: 12.224, file_cluster_17: 12.394
- **Magnitude:** 217.38 | **LOC:** 416 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.2224%), Tech Debt (94.7024%)
**Top Internal Functions/Classes:**
  * `R1-Student-Name` (Impact: 17.7)
  * `2120-Calculate-Grades` (Impact: 10.4)
  * `5000-Read-STCOURS` (Impact: 8.8)
  * `2110-Print-Stdt-Total-Report` (Impact: 8.1)
  * `6100-Write-R1` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 26`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 124`, `orphaned_logic: 17`
* *Architecture:* `io: 39`, `import: 4`
* *Defense:* `safety: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS172A.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.855 IQR)
- **Top Global Matches:** file_cluster_8: 11.855, file_cluster_13: 12.232, file_cluster_17: 12.4
- **Magnitude:** 217.36 | **LOC:** 416 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.4633%), Tech Debt (94.7817%)
**Top Internal Functions/Classes:**
  * `R1-Student-Name` (Impact: 17.7)
  * `2120-Calculate-Grades` (Impact: 10.4)
  * `5000-Read-STCOURS` (Impact: 8.8)
  * `2110-Print-Stdt-Total-Report` (Impact: 8.1)
  * `6100-Write-R1` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 26`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 124`, `orphaned_logic: 17`
* *Architecture:* `io: 39`, `import: 4`
* *Defense:* `safety: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.072 IQR)
- **Top Global Matches:** file_cluster_8: 11.072, file_cluster_13: 11.643, file_cluster_0: 11.658
- **Magnitude:** 204.98 | **LOC:** 449 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.2444%), Tech Debt (48.5163%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 85.7)
  * `1015-Load-Type` (Impact: 9.1)
  * `1099-Verify-Type-Table` (Impact: 7.7)
  * `1010-Load-Type-Table` (Impact: 4.3)
  * `0000-Mainline` (Impact: 4.2)
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

### `Mainframe/ZOS/ECBAP/cbl/WS120.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.996 IQR)
- **Top Global Matches:** file_cluster_8: 11.996, file_cluster_13: 12.357, file_cluster_17: 12.52
- **Magnitude:** 203.6 | **LOC:** 387 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.2456%), Tech Debt (93.3965%)
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` (Impact: 14.1)
  * `5100-Read-INSClaim` (Impact: 8.8)
  * `2100-Process-Claims` (Impact: 7.6)
  * `6100-Write-R1` (Impact: 7.3)
  * `2120-Move-Fixed-Fields` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 16`
* *Architecture:* `io: 33`, `import: 4`
* *Defense:* `safety: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST, CLAIMREC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS193.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.996 IQR)
- **Top Global Matches:** file_cluster_8: 11.996, file_cluster_13: 12.357, file_cluster_17: 12.52
- **Magnitude:** 203.6 | **LOC:** 387 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.2456%), Tech Debt (93.3965%)
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` (Impact: 14.1)
  * `5100-Read-INSClaim` (Impact: 8.8)
  * `2100-Process-Claims` (Impact: 7.6)
  * `6100-Write-R1` (Impact: 7.3)
  * `2120-Move-Fixed-Fields` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 16`
* *Architecture:* `io: 33`, `import: 4`
* *Defense:* `safety: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST, CLAIMREC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws120.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.997 IQR)
- **Top Global Matches:** file_cluster_8: 11.997, file_cluster_13: 12.355, file_cluster_17: 12.519
- **Magnitude:** 203.6 | **LOC:** 387 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.2456%), Tech Debt (93.3965%)
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` (Impact: 14.1)
  * `5100-Read-INSClaim` (Impact: 8.8)
  * `2100-Process-Claims` (Impact: 7.6)
  * `6100-Write-R1` (Impact: 7.3)
  * `2120-Move-Fixed-Fields` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 16`
* *Architecture:* `io: 33`, `import: 4`
* *Defense:* `safety: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST, CLAIMREC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.962 IQR)
- **Top Global Matches:** file_cluster_8: 10.962, file_cluster_7: 11.475, file_cluster_0: 11.551
- **Magnitude:** 193.56 | **LOC:** 488 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.0365%), Tech Debt (82.8923%)
**Top Internal Functions/Classes:**
  * `100-MAINLINE` (Impact: 23.4)
  * `OBJECT-COMPUTER` (Impact: 14.0)
  * `WS-OUTPUT-REC` (Impact: 5.7)
    * *Intent:* * DISPLAY "HOUSEKEEPING".
  * `INS-TYPE-O` (Impact: 2.5)
  * `200-CLEANUP` (Impact: 2.0)
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

### `pgm_templates/CICS/basecics.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.024 IQR)
- **Top Global Matches:** file_cluster_8: 13.024, file_cluster_17: 13.131, file_cluster_11: 13.248
- **Magnitude:** 192.82 | **LOC:** 336 | **CtrlFlow:** 88.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.4017%), Tech Debt (98.1551%)
**Top Internal Functions/Classes:**
  * `WCM-A-HOURLY-WAGE` (Impact: 24.2)
  * `0000-MAINLINE` (Impact: 13.8)
    * *Intent:* *COPY MANUALLY CODED MAP HERE. *COPY DFHEIBLK COPY BOOK HERE. *COPY ATTRIBUTES COPY BOOK HERE.
  * `1000-RECIEVE-MAP` (Impact: 6.9)
  * `5500-COMPUTE-RESULTS` (Impact: 6.8)
  * `0500-NORMAL-PROCESSING` (Impact: 6.5)
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

### `OpenCobol/ECBAP/cbl/ws162o.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.552 IQR)
- **Top Global Matches:** file_cluster_8: 11.552, file_cluster_13: 11.845, file_cluster_17: 12.109
- **Magnitude:** 178.32 | **LOC:** 483 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.0246%), Tech Debt (93.1734%)
**Top Internal Functions/Classes:**
  * `2100-Process-INFile-Records` (Impact: 13.1)
  * `1015-Load-Type` (Impact: 9.1)
  * `5100-Read-INFILE` (Impact: 8.8)
  * `2180-Validate-RFP-Record` (Impact: 8.4)
  * `1099-Verify-Type-Table` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 42`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`, `orphaned_logic: 19`
* *Architecture:* `io: 46`, `import: 9`
* *Defense:* `safety: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSDT, WSFST, PATIENT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLE2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.802 IQR)
- **Top Global Matches:** file_cluster_8: 10.802, file_cluster_7: 11.462, file_cluster_0: 11.483
- **Magnitude:** 161.2 | **LOC:** 543 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.8889%), Tech Debt (64.3339%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 40.5)
  * `WS-Company-Total` (Impact: 10.4)
    * *Intent:* * Okay, Calculating is fine. * Now, can we calculate and print subtotals in one go.
  * `WS-Company-Total` (Impact: 10.2)
  * `0000-Mainline` (Impact: 4.2)
  * `1000-Begin-Job` (Impact: 2.1)
    * *Intent:* * Division
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

### `OpenCobol/ECBAP/cbl/ws182.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.7 IQR)
- **Top Global Matches:** file_cluster_8: 11.7, file_cluster_13: 11.971, file_cluster_17: 12.037
- **Magnitude:** 158.7 | **LOC:** 390 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.2608%), Tech Debt (95.5405%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 13.7)
  * `5000-Read-ACCTREC` (Impact: 8.8)
  * `6100-Write-R1` (Impact: 7.3)
  * `2910-Print-Detail-Line` (Impact: 6.5)
  * `1000-Begin-Job` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `dead_code: 2`, `orphaned_logic: 16`
* *Architecture:* `io: 35`, `import: 3`
* *Defense:* `safety: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS182.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.234 IQR)
- **Top Global Matches:** file_cluster_8: 11.234, file_cluster_13: 11.718, file_cluster_0: 11.887
- **Magnitude:** 158.6 | **LOC:** 380 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.2608%), Tech Debt (95.5405%)
**Top Internal Functions/Classes:**
  * `2000-Process` (Impact: 13.6)
  * `5000-Read-ACCTREC` (Impact: 8.8)
  * `6100-Write-R1` (Impact: 7.3)
  * `2910-Print-Detail-Line` (Impact: 6.5)
  * `1000-Begin-Job` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `orphaned_logic: 16`
* *Architecture:* `io: 35`, `import: 3`
* *Defense:* `safety: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.979
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `OpenCobol/ECBAP/jcl/MAINPGM.sh` (SHELL) | Magnitude: 16.34 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: safety_bypasses: 19, indent_spaces: 13, branch: 5, state_mutation: 5

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
- `Mainframe/ZOS/Zowe/Simple_Report/COBOL/prtrpt1.cbl` (COBOL) | Magnitude: 85.46 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 41, branch: 29, io: 19
- `OpenCobol/prod/cbl/prtrpt1.cbl` (COBOL) | Magnitude: 85.46 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 41, branch: 29, io: 19
- `Mainframe/ZOS/Zowe/Create_Test_DataSet/zowe-only-method/allocate.sh` (SHELL) | Magnitude: 18.02 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: reflection_metaprogramming: 17, state_mutation: 10, indent_spaces: 7, concurrency: 6
- `pgm_templates/CICS/basecics.cbl` (COBOL) | Magnitude: 192.82 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 251, state_mutation: 112, branch: 55, safety: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `common/cpy/PATIENT.cpy` -> **Severity: 614.189** (Blast Radius: 10.577 * Doc Risk: 58.0684%)
- `Mainframe/ZOS/Zowe/Simple_Report/COPYBOOK/wsfst.cpy` -> **Severity: 431.016** (Blast Radius: 18.174 * Doc Risk: 23.7161%)
- `OpenCobol/prod/cbl/TDSPTAB.cbl` -> **Severity: 296.688** (Blast Radius: 2.979 * Doc Risk: 99.593%)
- `Mainframe/ZOS/ECBAP/cbl/SUB01.cbl` -> **Severity: 296.419** (Blast Radius: 2.979 * Doc Risk: 99.5028%)
- `OpenCobol/ECBAP/cbl/SUB01.cbl` -> **Severity: 296.419** (Blast Radius: 2.979 * Doc Risk: 99.5028%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
