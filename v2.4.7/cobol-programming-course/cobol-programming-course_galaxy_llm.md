# ARCHITECTURAL_BRIEF: cobol-programming-course
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/cobol-programming-course` |
| **Timestamp** | `2026-08-07T03:48:39.825187+00:00` |
| **Scan Duration** | `0.65s` |
| **Git Branch** | `master` |
| **Git Commit** | `11aca51998e11181925ff16c20b32c220360ff66` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-programming-course.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 74 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 79.1 | 19.3 | 13.0 | 13.0 |
| Error & Exception Exposure | 0.0 | 97.7 | 67.3 | 83.2 | 87.8 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 2.8 | 0.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.9 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 94.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 68.5 | 39.7 | 44.7 | 60.8 |
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

- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **14.6** | LOC: 12
  * *Intent:* ***************************************************** * LIST ALL CLIENTS * *****************************************************...
- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **14.6** | LOC: 12
- `SQL-ERROR-HANDLING` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **14.6** | LOC: 12
- `LIST-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **12.9** | LOC: 18
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **12.9** | LOC: 18
  * *Intent:* ***************************************************** * STRUCTURE FOR CUSTOMER RECORD * *****************************************************...
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **12.9** | LOC: 18
  * *Intent:* *
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **12.9** | LOC: 18
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **12.9** | LOC: 18
- `LOAD-TABLES` (@ `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol`) -> Impact: **7.3** | LOC: 7
- `LOAD-TABLES` (@ `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol`) -> Impact: **7.3** | LOC: 7

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `COBOL Programming Course #2 - Learning COBOL/Labs/jcl` | 23 | 1090.36 | 12.3% | 0.0% |
| `COBOL Programming Course #2 - Learning COBOL/Labs/cbl` | 23 | 574.84 | 23.86% | 37.89% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/cbl` | 3 | 245.1 | 71.55% | 98.4% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc` | 3 | 193.42 | 12.7% | 0.0% |
| `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc` | 3 | 183.62 | 9.24% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/jcl` | 10 | 182.88 | 6.13% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl` | 2 | 146.26 | 58.56% | 37.34% |
| `COBOL Programming Course #2 - Learning COBOL` | 2 | 76.72 | 0.0% | 0.0% |
| `COBOL Programming Course #4 - Testing/Labs/jcl` | 2 | 66.2 | 9.01% | 0.0% |
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
6. **`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl`** -> AI Confidence: **99.08%**
7. **`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl`** -> AI Confidence: **99.07%**
8. **`COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl`** -> AI Confidence: **99.07%**
9. **`COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol`** -> AI Confidence: **99.06%**
10. **`COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `83` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL) -> Cumulative Risk: **547.47**
- **Archetype:** `file_cluster_8` (Distance: 11.315 IQR)
- **Magnitude:** 95.94 | **LOC:** 202 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8181%), Tech Debt (98.2513%), Verification (80.0%)
- **Heaviest Functions:** `SQL-ERROR-HANDLING` (Impact: 14.6), `GET-ALL` (Impact: 12.9), `GET-SPECIFIC` (Impact: 12.9)

### 2. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL) -> Cumulative Risk: **543.38**
- **Archetype:** `file_cluster_8` (Distance: 11.284 IQR)
- **Magnitude:** 93.82 | **LOC:** 189 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7125%), Tech Debt (98.3218%), Verification (80.0%)
- **Heaviest Functions:** `SQL-ERROR-HANDLING` (Impact: 14.6), `GET-ALL` (Impact: 12.9), `GET-SPECIFIC` (Impact: 12.9)

### 3. `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` (COBOL) -> Cumulative Risk: **496.21**
- **Archetype:** `file_cluster_8` (Distance: 11.381 IQR)
- **Magnitude:** 37.52 | **LOC:** 55 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.708%), Safety Score (93.7918%)
- **Heaviest Functions:** `PAYMENT-WEEKLY` (Impact: 5.5), `PAYMENT-MONTHLY` (Impact: 3.4), `SHOW-OUTPUT` (Impact: 1.4)

### 4. `COBOL Programming Course #4 - Testing/Labs/cbl/DEPTPAY.CBL` (COBOL) -> Cumulative Risk: **475.26**
- **Archetype:** `file_cluster_8` (Distance: 9.575 IQR)
- **Magnitude:** 9.46 | **LOC:** 37 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8316%), Tech Debt (98.6851%), Safety Score (89.3084%)
- **Heaviest Functions:** `AVERAGE-SALARY` (Impact: 1.8)

### 5. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL) -> Cumulative Risk: **452.09**
- **Archetype:** `file_cluster_8` (Distance: 10.782 IQR)
- **Magnitude:** 55.34 | **LOC:** 145 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.033%), Tech Debt (98.6288%), Safety Score (69.1958%)
- **Heaviest Functions:** `SQL-ERROR-HANDLING` (Impact: 14.6), `LIST-ALL` (Impact: 12.9), `PROG-START` (Impact: 2.1)

### 6. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` (COBOL) -> Cumulative Risk: **428.19**
- **Archetype:** `file_cluster_8` (Distance: 10.068 IQR)
- **Magnitude:** 21.86 | **LOC:** 73 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.0919%), Tech Debt (97.4221%), Safety Score (72.3944%)
- **Heaviest Functions:** `LOAD-TABLES` (Impact: 7.3), `SEARCH-RECORD` (Impact: 4.5)

### 7. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` (COBOL) -> Cumulative Risk: **424.86**
- **Archetype:** `file_cluster_8` (Distance: 10.001 IQR)
- **Magnitude:** 20.88 | **LOC:** 74 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.9714%), Tech Debt (97.121%), Safety Score (72.1333%)
- **Heaviest Functions:** `LOAD-TABLES` (Impact: 7.3), `SEARCH-RECORD` (Impact: 3.5)

### 8. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0013.cobol` (COBOL) -> Cumulative Risk: **422.91**
- **Archetype:** `file_cluster_8` (Distance: 9.494 IQR)
- **Magnitude:** 2.48 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (99.9999%), Spec Match (93.3333%), Safety Score (92.3687%), State Flux (68.0733%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 1.2)

### 9. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/COBOL.cobol` (COBOL) -> Cumulative Risk: **409.48**
- **Archetype:** `file_cluster_8` (Distance: 8.7 IQR)
- **Magnitude:** 12.72 | **LOC:** 68 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8818%), State Flux (90.4463%), Safety Score (73.3376%)
- **Heaviest Functions:** `A000-START` (Impact: 4.3), `A000-DONE` (Impact: 1.4), `A000-COUNT` (Impact: 1.1)

### 10. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (COBOL) -> Cumulative Risk: **401.82**
- **Archetype:** `file_cluster_8` (Distance: 10.139 IQR)
- **Magnitude:** 37.44 | **LOC:** 131 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9987%), State Flux (90.8066%), Safety Score (67.9563%)
- **Heaviest Functions:** `2100-READ-TEN-RECORDS` (Impact: 6.2), `2300-READ-NEXT-RECORDS` (Impact: 6.2), `2000-READ-FIRST-RECORD` (Impact: 3.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.502 IQR)
- **Top Global Matches:** file_cluster_8: 6.502, file_cluster_7: 7.774, file_cluster_1: 7.94
- **Magnitude:** 152.44 | **LOC:** 61 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3921%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 38`, `args: 2`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 3`
* *Architecture:* `io: 33`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CEE.SCEERUN, DSNC10.SDSNLOAD, IGY630.SIGYCOMP, &SYSUID..LOAD(&MBR), DSNC10.DBCG.SDSNEXIT, CEE.SCEELKED, &SYSUID..DBRMLIB(&MBR), &SYSUID..DBRMLIB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.233 IQR)
- **Top Global Matches:** file_cluster_8: 6.233, file_cluster_7: 7.555, file_cluster_1: 7.716
- **Magnitude:** 96.71 | **LOC:** 51 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2793%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 34`, `args: 1`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 2`
* *Architecture:* `io: 26`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &LIBPRFX..SCEERUN, &LIBPRFX..SCEELKEX, &LNGPRFX..SIGYCOMP, &LIBPRFX..SCEERUN2, &LIBPRFX..SCEELKED, &SYSUID..LOAD(&SRC), &SYSUID..CBL(&SRC)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.315 IQR)
- **Top Global Matches:** file_cluster_8: 11.315, file_cluster_12: 11.742, file_cluster_0: 11.763
- **Magnitude:** 95.94 | **LOC:** 202 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1041%), Tech Debt (98.2513%)
**Top Internal Functions/Classes:**
  * `SQL-ERROR-HANDLING` (Impact: 14.6)
  * `GET-ALL` (Impact: 12.9)
    * *Intent:* ***************************************************** * STRUCTURE FOR CUSTOMER RECORD * ************...
  * `GET-SPECIFIC` (Impact: 12.9)
    * *Intent:* *
  * `PROCESS-INPUT` (Impact: 6.3)
  * `PROG-START` (Impact: 4.3)
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

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.284 IQR)
- **Top Global Matches:** file_cluster_8: 11.284, file_cluster_12: 11.668, file_cluster_0: 11.68
- **Magnitude:** 93.82 | **LOC:** 189 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.8469%), Tech Debt (98.3218%)
**Top Internal Functions/Classes:**
  * `SQL-ERROR-HANDLING` (Impact: 14.6)
  * `GET-ALL` (Impact: 12.9)
  * `GET-SPECIFIC` (Impact: 12.9)
  * `PROCESS-INPUT` (Impact: 6.3)
    * *Intent:* *****************************************************
  * `PROG-START` (Impact: 4.3)
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

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0033J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.311 IQR)
- **Top Global Matches:** file_cluster_8: 6.311, file_cluster_7: 7.607, file_cluster_1: 7.793
- **Magnitude:** 85.6 | **LOC:** 31 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.4255%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 6`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 17`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.073 IQR)
- **Top Global Matches:** file_cluster_8: 11.073, file_cluster_17: 11.667, file_cluster_0: 11.673
- **Magnitude:** 75.84 | **LOC:** 205 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.3971%), Tech Debt (36.4962%)
**Top Internal Functions/Classes:**
  * `IS-STATE-VIRGINIA` (Impact: 6.8)
    * *Intent:* *
  * `IS-OVERLIMIT` (Impact: 5.7)
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

### `COBOL Programming Course #2 - Learning COBOL/COBOL Programming Course #2 - Learning COBOL.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 75.72 | **LOC:** 3786 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.946 IQR)
- **Top Global Matches:** file_cluster_8: 10.946, file_cluster_7: 11.551, file_cluster_0: 11.57
- **Magnitude:** 70.42 | **LOC:** 196 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.7238%), Tech Debt (38.193%)
**Top Internal Functions/Classes:**
  * `IS-STATE-VIRGINIA` (Impact: 6.8)
  * `IS-OVERLIMIT` (Impact: 3.4)
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

### `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.178 IQR)
- **Top Global Matches:** file_cluster_8: 6.178, file_cluster_7: 7.505, file_cluster_1: 7.663
- **Magnitude:** 62.19 | **LOC:** 39 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.4221%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 29`, `args: 1`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 2`
* *Architecture:* `io: 20`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &LIBPRFX..SCEERUN, &LIBPRFX..SCEELKEX, &LNGPRFX..SIGYCOMP, &LIBPRFX..SCEERUN2, &LIBPRFX..SCEELKED, &SYSUID..LOAD(&SRC), &SYSUID..CBL(&SRC)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.782 IQR)
- **Top Global Matches:** file_cluster_8: 10.782, file_cluster_0: 11.215, file_cluster_12: 11.259
- **Magnitude:** 55.34 | **LOC:** 145 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.7025%), Tech Debt (98.6288%)
**Top Internal Functions/Classes:**
  * `SQL-ERROR-HANDLING` (Impact: 14.6)
    * *Intent:* ***************************************************** * LIST ALL CLIENTS * *************************...
  * `LIST-ALL` (Impact: 12.9)
  * `PROG-START` (Impact: 2.1)
  * `PRINT-AND-GET1` (Impact: 2.1)
    * *Intent:* *------------------ *****************************************************
  * `PRINT-A-LINE` (Impact: 1.4)
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

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/ADDAMT.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.982 IQR)
- **Top Global Matches:** file_cluster_8: 5.982, file_cluster_7: 7.347, file_cluster_1: 7.521
- **Magnitude:** 53.52 | **LOC:** 27 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1947%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/COBRUN.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.133 IQR)
- **Top Global Matches:** file_cluster_8: 6.133, file_cluster_7: 7.47, file_cluster_1: 7.642
- **Magnitude:** 51.44 | **LOC:** 23 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.3021%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..LOAD, &SYSUID..COBRUN.OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0001J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0002J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0003J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0004J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0005J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0006J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0007J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0008J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0009J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0010J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0011J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0012J.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL006AJ.jcl` (JCL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 6.191, file_cluster_7: 7.517, file_cluster_1: 7.69
- **Magnitude:** 50.92 | **LOC:** 22 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0202%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` &SYSUID..DATA, &SYSUID..LOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL) | Magnitude: 93.82 | Delta: **0.384 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 156, branch: 39, state_mutation: 31, io: 27
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0014.cobol` (COBOL) | Magnitude: 16.26 | Delta: **0.388 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, debug_prints: 2, class_start: 1
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` (COBOL) | Magnitude: 36.3 | Delta: **0.395 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 115, io: 22, state_mutation: 19, structural_boundaries: 8
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0005.cobol` (COBOL) | Magnitude: 36.3 | Delta: **0.395 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 115, io: 22, state_mutation: 19, structural_boundaries: 8
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` (COBOL) | Magnitude: 30.26 | Delta: **0.422 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 26, io: 24, branch: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0013J.jcl` -> **Severity: 570.978** (Blast Radius: 8.333 * Doc Risk: 68.5201%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/jcl/CBL0014J.jcl` -> **Severity: 570.978** (Blast Radius: 8.333 * Doc Risk: 68.5201%)
- `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DSNUPROC.jcl` -> **Severity: 570.978** (Blast Radius: 8.333 * Doc Risk: 68.5201%)
- `COBOL Programming Course #4 - Testing/Labs/jcl/DEPTPAY.JCL` -> **Severity: 559.462** (Blast Radius: 8.333 * Doc Risk: 67.1381%)
- `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2JCL.jcl` -> **Severity: 557.3** (Blast Radius: 8.333 * Doc Risk: 66.8787%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
