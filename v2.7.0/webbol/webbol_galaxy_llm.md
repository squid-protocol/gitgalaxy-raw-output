# ARCHITECTURAL_BRIEF: webbol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jmsdnns/webbol` |
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
| Total Artifacts | 13 |
| Analyzed Artifacts (Scanned) | 13 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 621 |
| Volatility Index | 0.154 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1667 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 10 | 596 | 76.9% |
| MAKEFILE | 1 | 24 | 7.7% |
| MARKDOWN | 1 | 0 | 7.7% |
| HTML | 1 | 1 | 7.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12 | 92.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 7.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 88.1 | 30.8 | 11.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 45.7 | 39.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 55.7 | 19.4 | 10.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 8.9 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 8.2 | 1.9 | 1.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 49.9 | 49.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 13.4 | 2.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 58.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 63.5 | 94.5 | 94.5 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 43.1 | 100.0 | 63.1 | 68.3 | 68.3 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 50.0 | 29.2 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 3 | 3 | 1 | `Makefile` |
| guards | 1 | 1 | 0 | `webserver.cbl` |
| danger | 24 | 6 | 5 | `webserver.cbl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 9 | 6 | 1 | `Makefile` |
| io | 15 | 4 | 5 | `file-ops.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 21 | 2 | 4 | `webserver.cbl` |
| time | 0 | 0 | 0 | - |
| serialization | 8 | 1 | 0 | `http-handler.cbl` |
| regex | 16 | 4 | 2 | `http-handler.cbl` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 12 | 1 | 0 | `webserver.cbl` |
| mutation | 131 | 7 | 28 | `url-decode.cbl` |
| dead_code | 12 | 6 | 2 | `http-handler.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 1 | 1 | 0 | `webserver.cbl` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `file-ops.cbl` (Hits: 5)
- `mime-types.cbl` (Hits: 5)
- `webserver.cbl` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **http-structs.cpy** (`http-structs.cpy`) — 2 inbound connections
2. **config.cpy** (`config.cpy`) — 1 inbound connections
3. **file-structs.cpy** (`file-structs.cpy`) — 1 inbound connections
4. **socket-defs.cpy** (`socket-defs.cpy`) — 1 inbound connections
5. **Makefile** (`Makefile`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **webserver.cbl** (`webserver.cbl`) — 3 outbound dependencies
2. **http-handler.cbl** (`http-handler.cbl`) — 2 outbound dependencies
3. **Makefile** (`Makefile`) — 0 outbound dependencies
4. **README.md** (`README.md`) — 0 outbound dependencies
5. **config.cpy** (`config.cpy`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `DECODE-HEX-CHAR` (@ `url-decode.cbl`) -> Impact: **48.8** | LOC: 76
  * *Intent:* *> Convert two-character hex code to actual character *> Handles common URL-encoded special characters used in web requests
- `MAIN-LOGIC` (@ `file-ops.cbl`) -> Impact: **23.7** | LOC: 94
- `MAIN-LOGIC` (@ `mime-types.cbl`) -> Impact: **22.9** | LOC: 58
  * *Intent:* *> Main MIME type detection logic
- `MAIN-LOGIC` (@ `path-utils.cbl`) -> Impact: **14.6** | LOC: 72
  * *Intent:* *> Main path validation and sanitization logic
- `MAIN-LOGIC` (@ `http-handler.cbl`) -> Impact: **13.9** | LOC: 99
  * *Intent:* *> Main HTTP request processing logic
- `MAIN-LOGIC` (@ `url-decode.cbl`) -> Impact: **9.5** | LOC: 50
  * *Intent:* *> Main URL decoding logic
- `INIT-SOCKET` (@ `webserver.cbl`) -> Impact: **7.8** | LOC: 55
  * *Intent:* *> Create and configure a TCP socket for the web server
- `HANDLE-REQUEST` (@ `webserver.cbl`) -> Impact: **6.5** | LOC: 31
  * *Intent:* *> Read HTTP request from client and generate response
- `MAIN-LOGIC` (@ `webserver.cbl`) -> Impact: **4.0** | LOC: 19
  * *Intent:* *> Main program entry point
- `BUILD-200-RESPONSE` (@ `http-handler.cbl`) -> Impact: **3.0** | LOC: 37
  * *Intent:* *> Build HTTP 200 OK response with file content

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 13 | 504.17 | 28.45% | 17.89% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `path-utils.cbl` -> **55.6575%** Exposure
- `file-ops.cbl` -> **53.9809%** Exposure
- `mime-types.cbl` -> **53.2847%** Exposure
- `url-decode.cbl` -> **27.816%** Exposure
- `webserver.cbl` -> **21.4165%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `file-ops.cbl` -> **100.0%** Exposure
- `mime-types.cbl` -> **100.0%** Exposure
- `path-utils.cbl` -> **100.0%** Exposure
- `url-decode.cbl` -> **100.0%** Exposure
- `http-handler.cbl` -> **99.7728%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `file-ops.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `http-handler.cbl` -> **1** Orphaned Functions | **0** Duplicates
- `mime-types.cbl` -> **1** Orphaned Functions | **0** Duplicates
- `path-utils.cbl` -> **1** Orphaned Functions | **0** Duplicates
- `url-decode.cbl` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `5` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mime-types.cbl` (COBOL) -> Cumulative Risk: **637.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 74.04 | **LOC:** 82 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.417%), Stability (94.4835%)
- **Heaviest Functions:** `MAIN-LOGIC` (Impact: 22.9)

### 2. `path-utils.cbl` (COBOL) -> Cumulative Risk: **634.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 46.8 | **LOC:** 104 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (94.4835%), Safety Score (93.3392%)
- **Heaviest Functions:** `MAIN-LOGIC` (Impact: 14.6), `LS-RETURN-CODE` (Impact: 1.1)

### 3. `url-decode.cbl` (COBOL) -> Cumulative Risk: **591.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 169.24 | **LOC:** 161 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6807%), Cognitive Load (88.0797%)
- **Heaviest Functions:** `DECODE-HEX-CHAR` (Impact: 48.8), `MAIN-LOGIC` (Impact: 9.5)

### 4. `file-ops.cbl` (COBOL) -> Cumulative Risk: **573.52**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 85.08 | **LOC:** 130 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (95.9219%)
- **Heaviest Functions:** `MAIN-LOGIC` (Impact: 23.7), `FILE-CONTROL` (Impact: 2.5)

### 5. `webserver.cbl` (COBOL) -> Cumulative Risk: **523.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 44.6 | **LOC:** 200 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.6875%), Stability (94.4835%), Safety Score (83.3937%)
- **Heaviest Functions:** `INIT-SOCKET` (Impact: 7.8), `HANDLE-REQUEST` (Impact: 6.5), `MAIN-LOGIC` (Impact: 4.0)

### 6. `http-handler.cbl` (COBOL) -> Cumulative Risk: **510.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 54.14 | **LOC:** 239 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), State Flux (99.7728%), Safety Score (77.9569%)
- **Heaviest Functions:** `MAIN-LOGIC` (Impact: 13.9), `BUILD-200-RESPONSE` (Impact: 3.0), `BUILD-404-RESPONSE` (Impact: 1.5)

### 7. `Makefile` (MAKEFILE) -> Cumulative Risk: **229.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 13.58 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (68.26%), Documentation (50.0%), Api Exposure (8.1867%)
- **Heaviest Functions:** `url-decode.o` (Impact: 1.3), `run` (Impact: 1.2), `all` (Impact: 1.1)

### 8. `config.cpy` (COBOL) -> Cumulative Risk: **165.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.6 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Stability (94.4835%), Churn (68.26%), Verification (2.2977%)

### 9. `file-structs.cpy` (COBOL) -> Cumulative Risk: **165.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.73 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Stability (94.4835%), Churn (68.26%), Verification (2.2977%)

### 10. `http-structs.cpy` (COBOL) -> Cumulative Risk: **165.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.76 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Stability (94.4835%), Churn (68.26%), Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `url-decode.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 169.24 | **LOC:** 161 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (27.816%)
**Top Internal Functions/Classes:**
  * `DECODE-HEX-CHAR` (Impact: 48.8)
    * *Intent:* *> Convert two-character hex code to actual character *> Handles common URL-encoded special characte...
  * `MAIN-LOGIC` (Impact: 9.5)
    * *Intent:* *> Main URL decoding logic
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 10`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `file-ops.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 85.08 | **LOC:** 130 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.2646%), Tech Debt (53.9809%)
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` (Impact: 23.7)
  * `FILE-CONTROL` (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 20`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 2`
* *Architecture:* `io: 5`, `api: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mime-types.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 74.04 | **LOC:** 82 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.1391%), Tech Debt (53.2847%)
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` (Impact: 22.9)
    * *Intent:* *> Main MIME type detection logic
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 11`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `http-handler.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 54.14 | **LOC:** 239 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.8791%), Tech Debt (20.365%)
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` (Impact: 13.9)
    * *Intent:* *> Main HTTP request processing logic
  * `BUILD-200-RESPONSE` (Impact: 3.0)
    * *Intent:* *> Build HTTP 200 OK response with file content
  * `BUILD-404-RESPONSE` (Impact: 1.5)
    * *Intent:* *> Build HTTP 404 Not Found response
  * `BUILD-403-RESPONSE` (Impact: 1.5)
    * *Intent:* *> Build HTTP 403 Forbidden response (for security violations)
  * `BUILD-413-RESPONSE` (Impact: 1.5)
    * *Intent:* *> Build HTTP 413 Payload Too Large response (for oversized files)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 17`, `args: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` file-structs, http-structs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `path-utils.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 46.8 | **LOC:** 104 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.4207%), Tech Debt (55.6575%)
**Top Internal Functions/Classes:**
  * `MAIN-LOGIC` (Impact: 14.6)
    * *Intent:* *> Main path validation and sanitization logic
  * `LS-RETURN-CODE` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `webserver.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 44.6 | **LOC:** 200 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.0055%), Tech Debt (21.4165%)
**Top Internal Functions/Classes:**
  * `INIT-SOCKET` (Impact: 7.8)
    * *Intent:* *> Create and configure a TCP socket for the web server
  * `HANDLE-REQUEST` (Impact: 6.5)
    * *Intent:* *> Read HTTP request from client and generate response
  * `MAIN-LOGIC` (Impact: 4.0)
    * *Intent:* *> Main program entry point
  * `ACCEPT-LOOP` (Impact: 2.8)
    * *Intent:* *> Main server loop - accept and handle client connections
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 34`, `args: 18`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 11`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `import: 3`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` config, http-structs, socket-defs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 13.58 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `url-decode.o` (Impact: 1.3)
  * `run` (Impact: 1.2)
    * *Intent:* # Run the server
  * `all` (Impact: 1.1)
    * *Intent:* # Default target
  * `path-utils.o` (Impact: 1.1)
    * *Intent:* # Compile modules to object files
  * `mime-types.o` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.32 | **LOC:** 166 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 68.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `http-structs.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.76 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 116.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `socket-defs.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.76 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 87.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `file-structs.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.73 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 96.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `config.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 0.6 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 87.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `file-ops.cbl` -> Churn: **100.0%** | Cog Load: 68.2646% | Debt: 53.9809%
- `path-utils.cbl` -> Churn: **68.26%** | Cog Load: 67.4207% | Debt: 55.6575%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `url-decode.cbl` -> **Jms Dnns** (100.0% isolated ownership) | Magnitude: 169.24
- `file-ops.cbl` -> **Jms Dnns** (100.0% isolated ownership) | Magnitude: 85.08
- `mime-types.cbl` -> **Jms Dnns** (100.0% isolated ownership) | Magnitude: 74.04
- `http-handler.cbl` -> **Jms Dnns** (100.0% isolated ownership) | Magnitude: 54.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Makefile` -> **Severity: 3401.35** (Blast Radius: 68.027 * Doc Risk: 50.0%)
- `file-ops.cbl` -> **Severity: 3401.35** (Blast Radius: 68.027 * Doc Risk: 50.0%)
- `http-handler.cbl` -> **Severity: 3401.35** (Blast Radius: 68.027 * Doc Risk: 50.0%)
- `mime-types.cbl` -> **Severity: 3401.35** (Blast Radius: 68.027 * Doc Risk: 50.0%)
- `path-utils.cbl` -> **Severity: 3401.35** (Blast Radius: 68.027 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
