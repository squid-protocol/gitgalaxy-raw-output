# ARCHITECTURAL_BRIEF: cobol-programming-course
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-programming-course.git` |
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
| Total Artifacts | 360 |
| Analyzed Artifacts (Scanned) | 121 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 239 |
| Total LOC | 3844 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 33.6% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.335 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2855 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7143 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 43 | 0 | 35.5% |
| JCL | 43 | 680 | 35.5% |
| COBOL | 32 | 2770 | 26.4% |
| JSON | 2 | 384 | 1.7% |
| CSV | 1 | 10 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 78 | 64.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 43 | 35.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 239*

**Composition by Extension & Reason:**
- `.png`: 219x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 5x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.tex`: 4x Excluded (Unsupported Extension: '.tex')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xlsx`: 1x Excluded (Explicitly Denied Extension: '.xlsx')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 65.6 | 9.0 | 3.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.8 | 34.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.5 | 2.3 | 2.4 | 2.4 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 0.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.9 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 93.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 88.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1 | 1 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0014.cobol` |
| cleanup | 47 | 25 | 2 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| guards | 2 | 2 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/jcl/LOADTBL.jcl` |
| danger | 54 | 36 | 1 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| concurrency | 7 | 4 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl` |
| connectivity | 6 | 6 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWC.jcl` |
| io | 600 | 57 | 19 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` |
| crypto | 0 | 0 | 0 | - |
| ipc | 35 | 4 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| time | 53 | 14 | 3 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 52 | 15 | 1 | `COBOL Programming Course #4 - Testing/Labs/cbl/DEPTPAY.CBL` |
| mutation | 738 | 65 | 18 | `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` |
| dead_code | 116 | 24 | 5 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` |
| credential | 0 | 0 | 0 | - |
| threat | 32 | 4 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (Hits: 28)
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (Hits: 23)
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 3 inbound connections
2. **DBRMLIB.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DBRMLIB.jcl`) — 2 inbound connections
3. **COMMITTERS.csv** (`COMMITTERS.csv`) — 2 inbound connections
4. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 1 inbound connections
5. **GOVERNANCE.md** (`GOVERNANCE.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **DB2CBL.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl`) — 10 outbound dependencies
2. **README.md** (`README.md`) — 7 outbound dependencies
3. **IGYWCL.jcl** (`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl`) — 7 outbound dependencies
4. **IGYWCLG.jcl** (`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl`) — 7 outbound dependencies
5. **DB2SETUP.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DB2SETUP.jcl`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `LIST-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **6.0** | LOC: 19
  * *Intent:* ***************************************************** * LIST ALL CLIENTS * *****************************************************...
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **6.0** | LOC: 19
  * *Intent:* *
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **6.0** | LOC: 19
  * *Intent:* *
- `GET-ALL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **6.0** | LOC: 19
- `GET-SPECIFIC` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **6.0** | LOC: 19
- `PAYMENT-WEEKLY` (@ `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL`) -> Impact: **5.5** | LOC: 10
- `FILE-CONTROL` (@ `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl`) -> Impact: **5.0** | LOC: 109
- `FILE-CONTROL` (@ `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl`) -> Impact: **5.0** | LOC: 110
- `FILE-CONTROL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **5.0** | LOC: 73
- `FILE-CONTROL` (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **5.0** | LOC: 97

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `COBOL Programming Course #2 - Learning COBOL/Labs/cbl` | 23 | 602.24 | 12.67% | 74.83% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/cbl` | 3 | 181.1 | 59.37% | 51.76% |
| `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl` | 2 | 132.96 | 29.11% | 70.14% |
| `COBOL Programming Course #2 - Learning COBOL/Labs/jcl` | 23 | 106.7 | 3.39% | 0.0% |
| `COBOL Programming Course #2 - Learning COBOL` | 2 | 76.72 | 0.0% | 0.0% |
| `__monolith__` | 15 | 65.28 | 0.0% | 0.0% |
| `COBOL Programming Course #4 - Testing/Labs/cbl` | 2 | 47.98 | 30.78% | 0.0% |
| `COBOL Programming Course #4 - Testing/Labs/tests` | 2 | 42.62 | 6.72% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics` | 2 | 27.72 | 0.0% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/jcl` | 11 | 24.92 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **99.9967%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` -> **99.9621%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` -> **99.9541%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` -> **99.2438%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol` -> **99.2438%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` -> **99.9318%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` -> **99.924%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` -> **99.7546%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` -> **99.6123%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **10** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol` -> **6** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0009.cobol` -> **6** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0010.cobol` -> **6** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol` -> **6** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `98` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL) -> Cumulative Risk: **500.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 40.54 | **LOC:** 145 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.699%), Safety Score (82.6218%)
- **Heaviest Functions:** `LIST-ALL` (Impact: 6.0), `FILE-CONTROL` (Impact: 5.0), `SQL-ERROR-HANDLING` (Impact: 4.7)

### 2. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` (COBOL) -> Cumulative Risk: **500.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 25.76 | **LOC:** 73 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9621%), State Flux (98.7781%)
- **Heaviest Functions:** `SEARCH-RECORD` (Impact: 4.3), `FILE-CONTROL` (Impact: 3.6), `LOAD-TABLES` (Impact: 3.4)

### 3. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` (COBOL) -> Cumulative Risk: **497.97**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 24.88 | **LOC:** 74 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9541%), State Flux (98.6166%)
- **Heaviest Functions:** `FILE-CONTROL` (Impact: 3.7), `LOAD-TABLES` (Impact: 3.4), `SEARCH-RECORD` (Impact: 3.3)

### 4. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL) -> Cumulative Risk: **495.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 71.34 | **LOC:** 202 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7546%), Safety Score (84.9261%)
- **Heaviest Functions:** `GET-ALL` (Impact: 6.0), `GET-SPECIFIC` (Impact: 6.0), `FILE-CONTROL` (Impact: 5.0)

### 5. `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL) -> Cumulative Risk: **493.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 69.22 | **LOC:** 189 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.6123%), Safety Score (84.1636%)
- **Heaviest Functions:** `GET-ALL` (Impact: 6.0), `GET-SPECIFIC` (Impact: 6.0), `FILE-CONTROL` (Impact: 5.0)

### 6. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` (COBOL) -> Cumulative Risk: **486.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 22.22 | **LOC:** 99 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.2438%), State Flux (97.0734%)
- **Heaviest Functions:** `FILE-CONTROL` (Impact: 3.5), `READ-NEXT-RECORD` (Impact: 2.6), `READ-RECORD` (Impact: 2.2)

### 7. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol` (COBOL) -> Cumulative Risk: **486.71**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 21.32 | **LOC:** 80 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.2438%), State Flux (97.0734%)
- **Heaviest Functions:** `FILE-CONTROL` (Impact: 2.8), `READ-NEXT-RECORD` (Impact: 2.4), `READ-RECORD` (Impact: 2.2)

### 8. `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (COBOL) -> Cumulative Risk: **484.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 67.74 | **LOC:** 205 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.924%), Safety Score (84.1369%)
- **Heaviest Functions:** `FILE-CONTROL` (Impact: 5.0), `IS-OVERLIMIT` (Impact: 3.8), `WRITE-OVERLIMIT` (Impact: 3.5)

### 9. `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (COBOL) -> Cumulative Risk: **483.52**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 65.22 | **LOC:** 196 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9318%), Safety Score (80.6186%)
- **Heaviest Functions:** `FILE-CONTROL` (Impact: 5.0), `WRITE-OVERLIMIT` (Impact: 3.5), `READ-NEXT-RECORD` (Impact: 2.5)

### 10. `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` (COBOL) -> Cumulative Risk: **483.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 36.46 | **LOC:** 169 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (94.3608%), Tech Debt (90.1157%)
- **Heaviest Functions:** `FILE-CONTROL` (Impact: 3.5), `READ-NEXT-RECORD` (Impact: 2.4), `READ-RECORD` (Impact: 2.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 71.34 | **LOC:** 202 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.5502%), Tech Debt (43.2735%)
**Top Internal Functions/Classes:**
  * `GET-ALL` (Impact: 6.0)
    * *Intent:* *
  * `GET-SPECIFIC` (Impact: 6.0)
    * *Intent:* *
  * `FILE-CONTROL` (Impact: 5.0)
  * `SQL-ERROR-HANDLING` (Impact: 4.7)
  * `PROCESS-INPUT` (Impact: 4.3)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 3`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 15`, `unreferenced_by_name: 3`
* *Architecture:* `io: 22`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 69.22 | **LOC:** 189 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.7401%), Tech Debt (43.6246%)
**Top Internal Functions/Classes:**
  * `GET-ALL` (Impact: 6.0)
  * `GET-SPECIFIC` (Impact: 6.0)
  * `FILE-CONTROL` (Impact: 5.0)
  * `SQL-ERROR-HANDLING` (Impact: 4.7)
  * `PROCESS-INPUT` (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 3`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 13`, `unreferenced_by_name: 3`
* *Architecture:* `io: 22`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 67.74 | **LOC:** 205 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.0653%), Tech Debt (68.8564%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 5.0)
  * `IS-OVERLIMIT` (Impact: 3.8)
    * *Intent:* *
  * `WRITE-OVERLIMIT` (Impact: 3.5)
    * *Intent:* *
  * `READ-NEXT-RECORD` (Impact: 2.5)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 18`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 24`, `unreferenced_by_name: 5`
* *Architecture:* `io: 23`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 65.22 | **LOC:** 196 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.1482%), Tech Debt (71.4257%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 5.0)
  * `WRITE-OVERLIMIT` (Impact: 3.5)
    * *Intent:* *
  * `READ-NEXT-RECORD` (Impact: 2.5)
    * *Intent:* *
  * `IS-OVERLIMIT` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 16`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 5`
* *Architecture:* `io: 23`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 40.54 | **LOC:** 145 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.832%), Tech Debt (68.3743%)
**Top Internal Functions/Classes:**
  * `LIST-ALL` (Impact: 6.0)
    * *Intent:* ***************************************************** * LIST ALL CLIENTS * *************************...
  * `FILE-CONTROL` (Impact: 5.0)
  * `SQL-ERROR-HANDLING` (Impact: 4.7)
  * `PRINT-A-LINE` (Impact: 1.4)
  * `PROG-START` (Impact: 1.1)
    * *Intent:* *------------------ ***************************************************** * MAIN PROGRAM ROUTINE * *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 20`, `args: 3`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 10`, `unreferenced_by_name: 3`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 38.14 | **LOC:** 131 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.8338%), Tech Debt (99.9967%)
**Top Internal Functions/Classes:**
  * `2300-READ-NEXT-RECORDS` (Impact: 3.2)
    * *Intent:* *THRU or THROUGH list the start and end of which *paragraphs will be executed in a sequential order ...
  * `FILE-CONTROL` (Impact: 2.9)
  * `2100-READ-TEN-RECORDS` (Impact: 2.2)
    * *Intent:* *notice that because of GO TO, this command will *never be executed *
  * `4000-READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `5000-WRITE-RECORD` (Impact: 1.4)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `unreferenced_by_name: 10`
* *Architecture:* `io: 28`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 37.52 | **LOC:** 55 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.5523%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PAYMENT-WEEKLY` (Impact: 5.5)
  * `PAYMENT-MONTHLY` (Impact: 3.4)
  * `SHOW-OUTPUT` (Impact: 1.4)
  * `INITIALIZATION` (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 16`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 36.56 | **LOC:** 174 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.8918%), Tech Debt (88.5488%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` (Impact: 1.4)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 36.46 | **LOC:** 169 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.6911%), Tech Debt (90.1157%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` (Impact: 1.4)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 35.42 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.0575%), Tech Debt (89.1864%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` (Impact: 1.3)
    * *Intent:* * The COMPUTE verb assigns the value of the arithmetic * expression to the TLIMIT and TBALANCE data ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 6`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0009.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 35.42 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.0575%), Tech Debt (89.1864%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` (Impact: 1.3)
    * *Intent:* * The COMPUTE verb assigns the value of the arithmetic * expression to the TLIMIT and TBALANCE data ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 6`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0010.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 35.42 | **LOC:** 184 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.0575%), Tech Debt (89.1864%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` (Impact: 1.3)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 6`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL006A.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34.0 | **LOC:** 173 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2389%), Tech Debt (86.9892%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.5)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-NEWYORK` (Impact: 2.2)
    * *Intent:* * * CHANGE 3: Updated paragraph name and logic to check for New York * Original paragraph: IS-STATE-...
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 5`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBLC1.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34.0 | **LOC:** 171 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2389%), Tech Debt (86.9892%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.5)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-NEWYORK` (Impact: 2.2)
    * *Intent:* * * CHANGE 3: Updated paragraph name and logic to check for New York * Original paragraph: IS-STATE-...
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 5`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0006.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 33.9 | **LOC:** 164 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2389%), Tech Debt (86.9892%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-VIRGINIA` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 5`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0007.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 33.8 | **LOC:** 160 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2389%), Tech Debt (86.9892%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-VIRGINIA` (Impact: 2.1)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 5`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 29.8 | **LOC:** 164 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.9645%), Tech Debt (90.7426%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.6)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *OPEN-FILES-END -- consists of an empty paragraph suffixed by *-END that ends the past one and serve...
  * `WRITE-RECORD` (Impact: 1.3)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0005.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 29.8 | **LOC:** 164 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.9645%), Tech Debt (90.7426%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.6)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` (Impact: 1.5)
    * *Intent:* *OPEN-FILES-END -- consists of an empty paragraph suffixed by *-END that ends the past one and serve...
  * `WRITE-RECORD` (Impact: 1.3)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #4 - Testing/Labs/tests/emppay.cut` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 27.42 | **LOC:** 25 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4471%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/COBOL Programming Course #3 - Advanced Topics.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 26.72 | **LOC:** 1336 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 25.76 | **LOC:** 73 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.7273%), Tech Debt (99.9621%)
**Top Internal Functions/Classes:**
  * `SEARCH-RECORD` (Impact: 4.3)
    * *Intent:* *
  * `FILE-CONTROL` (Impact: 3.6)
  * `LOAD-TABLES` (Impact: 3.4)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `OPEN-FILES` (Impact: 1.1)
    * *Intent:* *------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 14`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 5`
* *Architecture:* `io: 7`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 24.88 | **LOC:** 74 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7546%), Tech Debt (99.9541%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.7)
  * `LOAD-TABLES` (Impact: 3.4)
    * *Intent:* *
  * `SEARCH-RECORD` (Impact: 3.3)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `OPEN-FILES` (Impact: 1.1)
    * *Intent:* *------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 5`
* *Architecture:* `io: 7`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #4 - Testing/COBOL Programming Course #4 - Testing.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 23.44 | **LOC:** 1172 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.22 | **LOC:** 99 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.597%), Tech Debt (99.2438%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 3.5)
  * `READ-NEXT-RECORD` (Impact: 2.6)
    * *Intent:* *
  * `READ-RECORD` (Impact: 2.2)
    * *Intent:* *
  * `WRITE-RECORD` (Impact: 1.4)
    * *Intent:* *
  * `CLOSE-STOP` (Impact: 1.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 4`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DBRMLIB.jcl` -> **Severity: 2112.6** (Blast Radius: 21.126 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
