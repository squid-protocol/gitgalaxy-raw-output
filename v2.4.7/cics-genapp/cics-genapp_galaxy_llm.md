# ARCHITECTURAL_BRIEF: cics-genapp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/cics-genapp` |
| **Timestamp** | `2026-08-07T03:47:59.765498+00:00` |
| **Scan Duration** | `0.36s` |
| **Git Branch** | `main` |
| **Git Commit** | `63eca1b670d9199637bdc2ca7df6e4189a58c892` |
| **Git Remote** | `https://github.com/cicsdev/cics-genapp.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 75 malicious artifacts.

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
| Total Artifacts | 139 |
| Analyzed Artifacts (Scanned) | 129 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 10865 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.8% |
| Dominant Lang | COBOL |

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
| COBOL | 44 | 6794 | 34.1% |
| PLAINTEXT | 41 | 0 | 31.8% |
| JCL | 30 | 4054 | 23.3% |
| MARKDOWN | 13 | 0 | 10.1% |
| SHELL | 1 | 17 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.978`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 61 | 47.3% |
| file_cluster_11 | 8 | 6.2% |
| file_cluster_13 | 3 | 2.3% |
| file_cluster_12 | 1 | 0.8% |
| file_cluster_4 | 1 | 0.8% |
| file_cluster_0 | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 54 | 41.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 124 LOC), 1x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.rexx`: 2x Excluded (Unsupported Extension: '.rexx')
- `.evbind`: 1x Excluded (Unsupported Extension: '.evbind')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 24204 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 40.8 | 9.2 | 0.0 |
| Error & Exception Exposure | 0.0 | 97.5 | 57.3 | 79.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 2.9 | 0.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 92.4 | 2.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 28.3 | 3.8 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 94.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 11.9 | 11.0 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 99.0 | 1.3 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `base/src/lgsetup.cbl` (Hits: 55)
- `base/cntl/db2cre.jcl` (Hits: 54)
- `base/cntl/sampwui.jcl` (Hits: 51)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Changes.md** (`Changes.md`) — 0 inbound connections
2. **MAINTAINERS.md** (`MAINTAINERS.md`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **Building.md** (`base/Building.md`) — 0 inbound connections
5. **Installation.md** (`base/Installation.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lgacdb01.cbl** (`base/src/lgacdb01.cbl`) — 3 outbound dependencies
2. **lgapdb01.cbl** (`base/src/lgapdb01.cbl`) — 3 outbound dependencies
3. **lgicdb01.cbl** (`base/src/lgicdb01.cbl`) — 3 outbound dependencies
4. **lgipdb01.cbl** (`base/src/lgipdb01.cbl`) — 3 outbound dependencies
5. **lgucdb01.cbl** (`base/src/lgucdb01.cbl`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `UPDATE-POLICY-DB2-INFO` (@ `base/src/lgupdb01.cbl`) -> Impact: **45.1** | LOC: 102
  * *Intent:* ******************************************************************
- `MAINLINE` (@ `base/src/lgwebst5.cbl`) -> Impact: **38.0** | LOC: 448
- `A-GAIN` (@ `base/src/lgtestp4.cbl`) -> Impact: **33.9** | LOC: 197
- `MAINLINE` (@ `base/src/lgicvs01.cbl`) -> Impact: **30.2** | LOC: 124
- `MAINLINE` (@ `base/src/lgapdb01.cbl`) -> Impact: **29.1** | LOC: 83
- `A-GAIN` (@ `base/src/lgtestp1.cbl`) -> Impact: **27.0** | LOC: 201
- `A-GAIN` (@ `base/src/lgtestp2.cbl`) -> Impact: **27.0** | LOC: 189
- `A-GAIN` (@ `base/src/lgtestp3.cbl`) -> Impact: **27.0** | LOC: 185
- `MAINLINE` (@ `base/src/lgipdb01.cbl`) -> Impact: **24.2** | LOC: 64
- `A-GAIN` (@ `base/src/lgtestc1.cbl`) -> Impact: **23.9** | LOC: 157

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `base/src` | 47 | 3898.84 | 61.04% | 35.54% |
| `base/cntl` | 30 | 521.22 | 2.94% | 0.0% |
| `base/wsim` | 39 | 79.64 | 0.0% | 0.0% |
| `base` | 5 | 9.46 | 0.0% | 0.0% |
| `base/bin` | 1 | 6.24 | 100.0% | 100.0% |
| `__monolith__` | 3 | 3.78 | 0.0% | 0.0% |
| `base/data` | 2 | 2.0 | 0.0% | 0.0% |
| `base/exec` | 1 | 1.58 | 0.0% | 0.0% |
| `base/event-bindings` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `base/bin/install.sh` -> **99.9978%** Exposure
- `base/src/lgicus01.cbl` -> **87.2926%** Exposure
- `base/src/lgtestp3.cbl` -> **79.219%** Exposure
- `base/src/lgstsq.cbl` -> **78.9768%** Exposure
- `base/src/lgtestp2.cbl` -> **78.4314%** Exposure
### Highest State Flux (Mutation/Volatility)
- `base/src/lgacus01.cbl` -> **100.0%** Exposure
- `base/src/lgapvs01.cbl` -> **100.0%** Exposure
- `base/src/lgdpdb01.cbl` -> **100.0%** Exposure
- `base/src/lgicdb01.cbl` -> **100.0%** Exposure
- `base/src/lgicus01.cbl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `base/src/lgipdb01.cbl` -> **10** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp1.cbl` -> **8** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp2.cbl` -> **8** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp3.cbl` -> **8** Orphaned Functions | **0** Duplicates
- `base/src/lgtestp4.cbl` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`base/src/lgipdb01.cbl`** -> AI Confidence: **99.32%**
2. **`base/src/lgupdb01.cbl`** -> AI Confidence: **99.32%**
3. **`base/src/lgtestp4.cbl`** -> AI Confidence: **99.29%**
4. **`base/src/lgapdb01.cbl`** -> AI Confidence: **99.2%**
5. **`base/src/lgtestc1.cbl`** -> AI Confidence: **99.17%**
6. **`base/src/lgtestp1.cbl`** -> AI Confidence: **99.17%**
7. **`base/src/lgtestp2.cbl`** -> AI Confidence: **99.17%**
8. **`base/src/lgtestp3.cbl`** -> AI Confidence: **99.17%**
9. **`base/src/lgacdb01.cbl`** -> AI Confidence: **99.09%**
10. **`base/src/lgicdb01.cbl`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `base/src/lgacdb01.cbl` -> **99.0093%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `50` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `base/src/lgupdb01.cbl` (COBOL) -> Cumulative Risk: **539.18**
- **Archetype:** `file_cluster_11` (Distance: 15.008 IQR)
- **Magnitude:** 222.08 | **LOC:** 536 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (92.2833%), Safety Score (80.9909%)
- **Heaviest Functions:** `UPDATE-POLICY-DB2-INFO` (Impact: 45.1), `UPDATE-MOTOR-DB2-INFO` (Impact: 15.2), `UPDATE-ENDOW-DB2-INFO` (Impact: 8.4)

### 2. `base/src/lgacdb01.cbl` (COBOL) -> Cumulative Risk: **534.3**
- **Archetype:** `file_cluster_8` (Distance: 12.873 IQR)
- **Magnitude:** 113.36 | **LOC:** 329 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9989%), Secrets Risk (99.0093%), Cognitive Load (87.4239%)
- **Heaviest Functions:** `INSERT-CUSTOMER` (Impact: 19.9), `MAINLINE` (Impact: 10.4), `Obtain-CUSTOMER-Number` (Impact: 4.7)

### 3. `base/src/lgicvs01.cbl` (COBOL) -> Cumulative Risk: **529.33**
- **Archetype:** `file_cluster_4` (Distance: 12.146 IQR)
- **Magnitude:** 116.9 | **LOC:** 231 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Cognitive Load (96.4808%), Concurrency (92.3971%)
- **Heaviest Functions:** `MAINLINE` (Impact: 30.2), `A-EXIT` (Impact: 1.1)

### 4. `base/src/lgapdb01.cbl` (COBOL) -> Cumulative Risk: **513.18**
- **Archetype:** `file_cluster_11` (Distance: 13.833 IQR)
- **Magnitude:** 222.06 | **LOC:** 596 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9987%), Cognitive Load (85.0088%), Verification (80.0%)
- **Heaviest Functions:** `MAINLINE` (Impact: 29.1), `INSERT-COMMERCIAL` (Impact: 14.0), `INSERT-POLICY` (Impact: 10.9)

### 5. `base/src/lgtestc1.cbl` (COBOL) -> Cumulative Risk: **509.91**
- **Archetype:** `file_cluster_8` (Distance: 12.194 IQR)
- **Magnitude:** 191.24 | **LOC:** 348 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.4854%), Safety Score (92.1835%)
- **Heaviest Functions:** `A-GAIN` (Impact: 23.9), `ERROR-OUT` (Impact: 13.7), `MAINLINE` (Impact: 2.8)

### 6. `base/src/lgipdb01.cbl` (COBOL) -> Cumulative Risk: **502.05**
- **Archetype:** `file_cluster_11` (Distance: 13.768 IQR)
- **Magnitude:** 518.08 | **LOC:** 1031 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (85.3021%), Cognitive Load (80.5046%)
- **Heaviest Functions:** `MAINLINE` (Impact: 24.2), `GET-ENDOW-DB2-INFO` (Impact: 23.4), `GET-MOTOR-DB2-INFO` (Impact: 19.1)

### 7. `base/src/lgacus01.cbl` (COBOL) -> Cumulative Risk: **491.82**
- **Archetype:** `file_cluster_11` (Distance: 14.651 IQR)
- **Magnitude:** 62.3 | **LOC:** 180 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (92.8801%), Safety Score (85.6233%)
- **Heaviest Functions:** `MAINLINE` (Impact: 8.4), `INSERT-CUSTOMER` (Impact: 7.9), `MAINLINE-EXIT` (Impact: 1.1)

### 8. `base/src/lgstsq.cbl` (COBOL) -> Cumulative Risk: **489.66**
- **Archetype:** `file_cluster_8` (Distance: 12.332 IQR)
- **Magnitude:** 51.9 | **LOC:** 127 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (93.3099%), Safety Score (87.2138%)
- **Heaviest Functions:** `MAINLINE` (Impact: 10.1), `A-EXIT` (Impact: 1.1)

### 9. `base/src/lgtestp3.cbl` (COBOL) -> Cumulative Risk: **487.84**
- **Archetype:** `file_cluster_8` (Distance: 12.724 IQR)
- **Magnitude:** 206.52 | **LOC:** 300 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.276%), Safety Score (97.4281%)
- **Heaviest Functions:** `A-GAIN` (Impact: 27.0), `MAINLINE` (Impact: 2.9), `NO-ADD` (Impact: 2.1)

### 10. `base/src/lgtestp2.cbl` (COBOL) -> Cumulative Risk: **487.05**
- **Archetype:** `file_cluster_8` (Distance: 12.726 IQR)
- **Magnitude:** 209.48 | **LOC:** 301 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.2433%), Safety Score (97.4527%)
- **Heaviest Functions:** `A-GAIN` (Impact: 27.0), `MAINLINE` (Impact: 2.8), `NO-ADD` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `base/src/lgipdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.768 IQR)
- **Top Global Matches:** file_cluster_11: 13.768, file_cluster_8: 13.77, file_cluster_0: 13.792
- **Magnitude:** 518.08 | **LOC:** 1031 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.5046%), Tech Debt (27.3354%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 24.2)
  * `GET-ENDOW-DB2-INFO` (Impact: 23.4)
  * `GET-MOTOR-DB2-INFO` (Impact: 19.1)
  * `GET-HOUSE-DB2-INFO` (Impact: 18.6)
  * `GET-Commercial-DB2-INFO-2` (Impact: 15.5)
    * *Intent:* * Select was successful * Calculate size of commarea required to return all data
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 21`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 341`, `dead_code: 10`, `orphaned_logic: 10`
* *Architecture:* `io: 31`, `api: 1`, `import: 3`
* *Defense:* `safety: 34`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgwebst5.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.356 IQR)
- **Top Global Matches:** file_cluster_8: 11.356, file_cluster_12: 11.867, file_cluster_7: 11.978
- **Magnitude:** 356.64 | **LOC:** 803 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.8899%), Tech Debt (14.1625%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 38.0)
  * `Tran-Rate-Interval` (Impact: 3.5)
  * `Tran-Rate-Counts` (Impact: 2.0)
  * `A-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 52`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 295`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.008 IQR)
- **Top Global Matches:** file_cluster_11: 15.008, file_cluster_0: 15.07, file_cluster_17: 15.074
- **Magnitude:** 222.08 | **LOC:** 536 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.2833%), Tech Debt (43.4787%)
**Top Internal Functions/Classes:**
  * `UPDATE-POLICY-DB2-INFO` (Impact: 45.1)
    * *Intent:* ******************************************************************
  * `UPDATE-MOTOR-DB2-INFO` (Impact: 15.2)
  * `UPDATE-ENDOW-DB2-INFO` (Impact: 8.4)
  * `UPDATE-HOUSE-DB2-INFO` (Impact: 8.4)
  * `MAINLINE` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 17`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 128`, `dead_code: 10`, `orphaned_logic: 6`
* *Architecture:* `io: 29`, `api: 1`, `import: 3`
* *Defense:* `safety: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgapdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.833 IQR)
- **Top Global Matches:** file_cluster_11: 13.833, file_cluster_0: 13.864, file_cluster_17: 13.901
- **Magnitude:** 222.06 | **LOC:** 596 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.0088%), Tech Debt (32.6724%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 29.1)
  * `INSERT-COMMERCIAL` (Impact: 14.0)
  * `INSERT-POLICY` (Impact: 10.9)
  * `INSERT-ENDOW` (Impact: 10.2)
  * `INSERT-MOTOR` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 17`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 136`, `dead_code: 9`, `orphaned_logic: 6`
* *Architecture:* `io: 19`, `api: 1`, `import: 3`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.718 IQR)
- **Top Global Matches:** file_cluster_8: 12.718, file_cluster_2: 12.921, file_cluster_12: 12.937
- **Magnitude:** 220.98 | **LOC:** 319 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.1675%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 27.0)
  * `MAINLINE` (Impact: 3.0)
  * `NO-ADD` (Impact: 2.1)
  * `ERROR-OUT` (Impact: 1.5)
  * `ENDIT` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 175`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SSMAP, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp4.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.632 IQR)
- **Top Global Matches:** file_cluster_8: 12.632, file_cluster_13: 12.897, file_cluster_2: 12.942
- **Magnitude:** 219.18 | **LOC:** 319 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.5397%), Tech Debt (73.1803%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 33.9)
  * `MAINLINE` (Impact: 3.2)
  * `NO-ADD` (Impact: 2.1)
  * `ERROR-OUT` (Impact: 1.5)
  * `ENDIT` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 166`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SSMAP, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.726 IQR)
- **Top Global Matches:** file_cluster_8: 12.726, file_cluster_12: 12.935, file_cluster_2: 12.936
- **Magnitude:** 209.48 | **LOC:** 301 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.2433%), Tech Debt (78.4314%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 27.0)
  * `MAINLINE` (Impact: 2.8)
  * `NO-ADD` (Impact: 2.1)
  * `ERROR-OUT` (Impact: 1.5)
  * `ENDIT` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 164`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SSMAP, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp3.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.724 IQR)
- **Top Global Matches:** file_cluster_8: 12.724, file_cluster_12: 12.929, file_cluster_2: 12.93
- **Magnitude:** 206.52 | **LOC:** 300 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.276%), Tech Debt (79.219%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 27.0)
  * `MAINLINE` (Impact: 2.9)
  * `NO-ADD` (Impact: 2.1)
  * `ERROR-OUT` (Impact: 1.5)
  * `ENDIT` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 161`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SSMAP, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestc1.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.194 IQR)
- **Top Global Matches:** file_cluster_8: 12.194, file_cluster_12: 12.41, file_cluster_13: 12.477
- **Magnitude:** 191.24 | **LOC:** 348 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.4854%), Tech Debt (60.4806%)
**Top Internal Functions/Classes:**
  * `A-GAIN` (Impact: 23.9)
  * `ERROR-OUT` (Impact: 13.7)
  * `MAINLINE` (Impact: 2.8)
  * `ENDIT` (Impact: 1.4)
  * `CLEARIT` (Impact: 1.4)
    * *Intent:* * Send message to terminal and return
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 8`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 131`, `orphaned_logic: 7`
* *Architecture:* `io: 23`, `concurrency: 7`, `import: 2`
* *Defense:* `safety: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SSMAP, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.943 IQR)
- **Top Global Matches:** file_cluster_8: 11.943, file_cluster_12: 12.301, file_cluster_13: 12.366
- **Magnitude:** 117.24 | **LOC:** 207 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.8321%), Tech Debt (37.8992%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 17.2)
  * `A-EXIT` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 14`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 1`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgicvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.146 IQR)
- **Top Global Matches:** file_cluster_4: 12.146, file_cluster_8: 12.262, file_cluster_17: 12.478
- **Magnitude:** 116.9 | **LOC:** 231 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.4808%), Tech Debt (33.3045%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 30.2)
  * `A-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 30`, `api: 1`, `concurrency: 12`
* *Defense:* `safety: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgacdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.873 IQR)
- **Top Global Matches:** file_cluster_8: 12.873, file_cluster_13: 12.882, file_cluster_11: 12.887
- **Magnitude:** 113.36 | **LOC:** 329 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.4239%), Tech Debt (37.6438%)
**Top Internal Functions/Classes:**
  * `INSERT-CUSTOMER` (Impact: 19.9)
    * *Intent:* *----------------------------------------------------------------* * Process incoming commarea * *--...
  * `MAINLINE` (Impact: 10.4)
    * *Intent:* *----------------------------------------------------------------* * Definitions required for data m...
  * `Obtain-CUSTOMER-Number` (Impact: 4.7)
    * *Intent:* *----------------------------------------------------------------* * Common code * *----------------...
  * `MAINLINE-EXIT` (Impact: 1.1)
    * *Intent:* *----------------------------------------------------------------*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `dead_code: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 9`, `api: 1`, `import: 3`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgapvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.807 IQR)
- **Top Global Matches:** file_cluster_8: 11.807, file_cluster_13: 12.237, file_cluster_12: 12.247
- **Magnitude:** 105.22 | **LOC:** 189 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.6431%), Tech Debt (43.1932%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 13.5)
  * `A-EXIT` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 14`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupol01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.917 IQR)
- **Top Global Matches:** file_cluster_8: 12.917, file_cluster_11: 12.958, file_cluster_0: 13.002
- **Magnitude:** 91.84 | **LOC:** 202 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.099%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 19.5)
  * `UPDATE-POLICY-DB2-INFO` (Impact: 7.9)
  * `MAINLINE-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgicdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.736 IQR)
- **Top Global Matches:** file_cluster_11: 13.736, file_cluster_13: 13.74, file_cluster_0: 13.796
- **Magnitude:** 90.72 | **LOC:** 246 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.33%), Tech Debt (62.5787%)
**Top Internal Functions/Classes:**
  * `GET-CUSTOMER-INFO` (Impact: 16.5)
    * *Intent:* ****************************************************************** * P R O C E D U R E S
  * `MAINLINE` (Impact: 7.2)
  * `MAINLINE-END` (Impact: 1.1)
  * `MAINLINE-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `dead_code: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 6`, `api: 1`, `import: 3`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgdpdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.167 IQR)
- **Top Global Matches:** file_cluster_11: 13.167, file_cluster_13: 13.198, file_cluster_0: 13.213
- **Magnitude:** 83.42 | **LOC:** 246 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.441%), Tech Debt (31.3794%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 12.2)
    * *Intent:* *----------------------------------------------------------------* * Definitions required for data m...
  * `MAINLINE-EXIT` (Impact: 11.6)
    * *Intent:* ****************************************************************** * P R O C E D U R E S ***********...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 13`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `api: 1`, `import: 2`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgucdb01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.629 IQR)
- **Top Global Matches:** file_cluster_13: 12.629, file_cluster_11: 12.703, file_cluster_8: 12.717
- **Magnitude:** 74.42 | **LOC:** 223 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.005%), Tech Debt (45.1395%)
**Top Internal Functions/Classes:**
  * `UPDATE-CUSTOMER-INFO` (Impact: 15.0)
    * *Intent:* *----------------------------------------------------------------* * Common code *...
  * `MAINLINE` (Impact: 6.5)
  * `MAINLINE-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 13`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 7`, `api: 1`, `import: 3`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgacdb02.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.959 IQR)
- **Top Global Matches:** file_cluster_13: 12.959, file_cluster_11: 12.962, file_cluster_0: 12.992
- **Magnitude:** 72.72 | **LOC:** 226 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.16%), Tech Debt (51.9831%)
**Top Internal Functions/Classes:**
  * `INSERT-CUSTOMER-PASSWORD` (Impact: 11.7)
  * `MAINLINE` (Impact: 10.4)
    * *Intent:* *----------------------------------------------------------------* *--------------------------------...
  * `MAINLINE-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 13`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 5`, `api: 1`, `import: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgipvs01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.368 IQR)
- **Top Global Matches:** file_cluster_8: 11.368, file_cluster_12: 11.9, file_cluster_0: 11.926
- **Magnitude:** 72.62 | **LOC:** 150 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.393%), Tech Debt (60.5379%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 13.3)
  * `A-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`, `orphaned_logic: 2`
* *Architecture:* `io: 14`, `api: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgdpol01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.549 IQR)
- **Top Global Matches:** file_cluster_11: 13.549, file_cluster_0: 13.578, file_cluster_17: 13.581
- **Magnitude:** 63.92 | **LOC:** 187 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.3314%), Tech Debt (43.2348%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 13.8)
  * `MAINLINE-EXIT` (Impact: 8.1)
    * *Intent:* *----------------------------------------------------------------* * Common code * *----------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 12`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgacus01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.651 IQR)
- **Top Global Matches:** file_cluster_11: 14.651, file_cluster_17: 14.691, file_cluster_13: 14.693
- **Magnitude:** 62.3 | **LOC:** 180 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.8801%), Tech Debt (71.5257%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 8.4)
  * `INSERT-CUSTOMER` (Impact: 7.9)
  * `MAINLINE-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 42`, `dead_code: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgicus01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.755 IQR)
- **Top Global Matches:** file_cluster_8: 11.755, file_cluster_13: 11.981, file_cluster_12: 12.127
- **Magnitude:** 62.22 | **LOC:** 167 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.7012%), Tech Debt (87.2926%)
**Top Internal Functions/Classes:**
  * `GET-CUSTOMER-INFO` (Impact: 8.0)
    * *Intent:* *
  * `MAINLINE` (Impact: 7.1)
  * `MAINLINE-END` (Impact: 1.1)
    * *Intent:* ****************************************************************** * P R O C E D U R E S
  * `MAINLINE-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 42`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGPOLICY, LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgucus01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.393 IQR)
- **Top Global Matches:** file_cluster_0: 13.393, file_cluster_11: 13.394, file_cluster_17: 13.402
- **Magnitude:** 56.22 | **LOC:** 173 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.16%), Tech Debt (70.7943%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 8.3)
    * *Intent:* *----------------------------------------------------------------*
  * `UPDATE-CUSTOMER-INFO` (Impact: 7.9)
  * `MAINLINE-EXIT` (Impact: 1.1)
    * *Intent:* ******************************************************************
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgstsq.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.332 IQR)
- **Top Global Matches:** file_cluster_8: 12.332, file_cluster_0: 12.419, file_cluster_17: 12.424
- **Magnitude:** 51.9 | **LOC:** 127 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.3099%), Tech Debt (78.9768%)
**Top Internal Functions/Classes:**
  * `MAINLINE` (Impact: 10.1)
  * `A-EXIT` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 15`, `api: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgapol01.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.65 IQR)
- **Top Global Matches:** file_cluster_11: 14.65, file_cluster_17: 14.663, file_cluster_0: 14.665
- **Magnitude:** 51.88 | **LOC:** 170 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.6827%), Tech Debt (50.7022%)
**Top Internal Functions/Classes:**
  * `MAINLINE-EXIT` (Impact: 7.6)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 34`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.752
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LGCMAREA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `base/src/lgucus01.cbl` (COBOL) | Magnitude: 56.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 96, state_mutation: 36, structural_boundaries: 12, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `base/src/lgipdb01.cbl` (COBOL) | Magnitude: 518.08 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 739, state_mutation: 341, branch: 117, safety: 34
- `base/src/lgicdb01.cbl` (COBOL) | Magnitude: 90.72 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 61, branch: 18, structural_boundaries: 13
- `base/src/lgapol01.cbl` (COBOL) | Magnitude: 51.88 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 34, structural_boundaries: 11, branch: 10
- `base/src/lgdpol01.cbl` (COBOL) | Magnitude: 63.92 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, state_mutation: 39, branch: 16, structural_boundaries: 12
- `base/src/lgapdb01.cbl` (COBOL) | Magnitude: 222.06 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 408, state_mutation: 136, branch: 51, reflection_metaprogramming: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `base/bin/install.sh` (SHELL) | Magnitude: 6.24 | Delta: **0.31 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 25, structural_boundaries: 9, state_mutation: 3, sec_entropy: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `base/src/lgacdb02.cbl` (COBOL) | Magnitude: 72.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 46, branch: 16, structural_boundaries: 13
- `base/src/lgucdb01.cbl` (COBOL) | Magnitude: 74.42 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 48, branch: 15, structural_boundaries: 13
- `base/src/lgipol01.cbl` (COBOL) | Magnitude: 45.24 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 30, structural_boundaries: 11, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `base/src/lgicvs01.cbl` (COBOL) | Magnitude: 116.9 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 180, state_mutation: 69, io: 30, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `base/src/lgacdb01.cbl` (COBOL) | Magnitude: 113.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 213, state_mutation: 72, branch: 24, reflection_metaprogramming: 18
- `base/src/lgupol01.cbl` (COBOL) | Magnitude: 91.84 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 60, branch: 21, structural_boundaries: 12
- `base/src/lgstsq.cbl` (COBOL) | Magnitude: 51.9 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 38, io: 15, structural_boundaries: 11
- `base/src/lgtestp1.cbl` (COBOL) | Magnitude: 220.98 | Delta: **0.203 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 259, state_mutation: 175, reflection_metaprogramming: 26, branch: 22
- `base/src/lgtestp3.cbl` (COBOL) | Magnitude: 206.52 | Delta: **0.205 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 241, state_mutation: 161, reflection_metaprogramming: 25, branch: 22

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `base/cntl/adef121.jcl` -> **Severity: 92.406** (Blast Radius: 7.752 * Doc Risk: 11.9203%)
- `base/cntl/asmmap.jcl` -> **Severity: 92.406** (Blast Radius: 7.752 * Doc Risk: 11.9203%)
- `base/cntl/cdef121.jcl` -> **Severity: 92.406** (Blast Radius: 7.752 * Doc Risk: 11.9203%)
- `base/cntl/cdef122.jcl` -> **Severity: 92.406** (Blast Radius: 7.752 * Doc Risk: 11.9203%)
- `base/cntl/cdef123.jcl` -> **Severity: 92.406** (Blast Radius: 7.752 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
