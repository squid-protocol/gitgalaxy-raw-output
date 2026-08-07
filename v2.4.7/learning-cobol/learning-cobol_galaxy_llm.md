# ARCHITECTURAL_BRIEF: learning-cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/learning-cobol` |
| **Timestamp** | `2026-08-07T03:51:18.770683+00:00` |
| **Scan Duration** | `0.09s` |
| **Git Branch** | `master` |
| **Git Commit** | `c420efd949ced56cd84c6c47c715391af1b8fd4a` |
| **Git Remote** | `https://github.com/deniseyu/learning-cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6 malicious artifacts.

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
| Total Artifacts | 8 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 178 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.5% |
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
| COBOL | 5 | 177 | 71.4% |
| MARKDOWN | 1 | 0 | 14.3% |
| SHELL | 1 | 1 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.512`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 6 | 85.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 14.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 83.5 | 45.3 | 48.4 | 5.0 |
| Error & Exception Exposure | 87.1 | 96.2 | 90.6 | 89.4 | 88.2 |
| Tech Debt Exposure | 0.0 | 100.0 | 66.3 | 98.8 | 0.0 |
| Testing Exposure | 0.2 | 2.7 | 1.8 | 2.4 | 2.4 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 58.8 | 76.5 | 100.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 73.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 11.9 | 8.7 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `fizzbuzz.cob` (Hits: 0)
- `game-of-life.cob` (Hits: 0)
- `greet.cob` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fizzbuzz.cob** (`fizzbuzz.cob`) — 0 inbound connections
2. **game-of-life.cob** (`game-of-life.cob`) — 0 inbound connections
3. **greet.cob** (`greet.cob`) — 0 inbound connections
4. **hello-world.cob** (`hello-world.cob`) — 0 inbound connections
5. **rock-paper-scissors.cob** (`rock-paper-scissors.cob`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **fizzbuzz.cob** (`fizzbuzz.cob`) — 0 outbound dependencies
2. **game-of-life.cob** (`game-of-life.cob`) — 0 outbound dependencies
3. **greet.cob** (`greet.cob`) — 0 outbound dependencies
4. **hello-world.cob** (`hello-world.cob`) — 0 outbound dependencies
5. **rock-paper-scissors.cob** (`rock-paper-scissors.cob`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `check-neighbours` (@ `game-of-life.cob`) -> Impact: **27.1** | LOC: 43
- `PLAY-FIZZBUZZ` (@ `fizzbuzz.cob`) -> Impact: **7.8** | LOC: 15
- `print-world` (@ `game-of-life.cob`) -> Impact: **7.5** | LOC: 9
- `iterate-rows` (@ `game-of-life.cob`) -> Impact: **4.1** | LOC: 2
- `iterate-columns` (@ `game-of-life.cob`) -> Impact: **4.1** | LOC: 2
- `A000-FIRST-PARA` (@ `greet.cob`) -> Impact: **1.5** | LOC: 10
- `__global_context__` (@ `run-in-docker.sh`) -> Impact: **1.1** | LOC: 1

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 7 | 178.48 | 38.85% | 56.8% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `run-in-docker.sh` -> **100.0%** Exposure
- `greet.cob` -> **99.9955%** Exposure
- `fizzbuzz.cob` -> **98.9347%** Exposure
- `game-of-life.cob` -> **98.6851%** Exposure
### Highest State Flux (Mutation/Volatility)
- `fizzbuzz.cob` -> **100.0%** Exposure
- `game-of-life.cob` -> **100.0%** Exposure
- `rock-paper-scissors.cob` -> **100.0%** Exposure
- `greet.cob` -> **53.0518%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `game-of-life.cob` -> **4** Orphaned Functions | **0** Duplicates
- `fizzbuzz.cob` -> **1** Orphaned Functions | **0** Duplicates
- `greet.cob` -> **1** Orphaned Functions | **0** Duplicates
- `run-in-docker.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`game-of-life.cob`** -> AI Confidence: **99.17%**
2. **`rock-paper-scissors.cob`** -> AI Confidence: **99.06%**
3. **`fizzbuzz.cob`** -> AI Confidence: **98.96%**
4. **`greet.cob`** -> AI Confidence: **98.84%**
5. **`hello-world.cob`** -> AI Confidence: **98.84%**
6. **`run-in-docker.sh`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `game-of-life.cob` (COBOL) -> Cumulative Risk: **485.03**
- **Archetype:** `file_cluster_8` (Distance: 13.71 IQR)
- **Magnitude:** 92.34 | **LOC:** 84 | **CtrlFlow:** 76.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.6851%), Safety Score (88.239%)
- **Heaviest Functions:** `check-neighbours` (Impact: 27.1), `print-world` (Impact: 7.5), `iterate-rows` (Impact: 4.1)

### 2. `fizzbuzz.cob` (COBOL) -> Cumulative Risk: **483.22**
- **Archetype:** `file_cluster_8` (Distance: 12.363 IQR)
- **Magnitude:** 26.44 | **LOC:** 39 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.9347%), Safety Score (88.1602%)
- **Heaviest Functions:** `PLAY-FIZZBUZZ` (Impact: 7.8)

### 3. `rock-paper-scissors.cob` (COBOL) -> Cumulative Risk: **378.96**
- **Archetype:** `file_cluster_8` (Distance: 12.056 IQR)
- **Magnitude:** 39.9 | **LOC:** 55 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (87.1106%), Cognitive Load (77.6337%)

### 4. `greet.cob` (COBOL) -> Cumulative Risk: **376.93**
- **Archetype:** `file_cluster_8` (Distance: 8.534 IQR)
- **Magnitude:** 2.86 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9955%), Safety Score (90.4651%), State Flux (53.0518%)
- **Heaviest Functions:** `A000-FIRST-PARA` (Impact: 1.5)

### 5. `run-in-docker.sh` (SHELL) -> Cumulative Risk: **205.86**
- **Archetype:** `file_cluster_8` (Distance: 7.841 IQR)
- **Magnitude:** 1.12 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Safety Score (93.1775%), Spec Match (6.6667%), Cognitive Load (5.0%)
- **Heaviest Functions:** `__global_context__` (Impact: 1.1)

### 6. `hello-world.cob` (COBOL) -> Cumulative Risk: **139.36**
- **Archetype:** `file_cluster_8` (Distance: 7.706 IQR)
- **Magnitude:** 12.6 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (96.2312%), Spec Match (33.3333%), Cognitive Load (5.0%), Documentation (3.9734%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `game-of-life.cob` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.71 IQR)
- **Top Global Matches:** file_cluster_8: 13.71, file_cluster_17: 13.874, file_cluster_0: 13.947
- **Magnitude:** 92.34 | **LOC:** 84 | **CtrlFlow:** 76.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.493%), Tech Debt (98.6851%)
**Top Internal Functions/Classes:**
  * `check-neighbours` (Impact: 27.1)
  * `print-world` (Impact: 7.5)
  * `iterate-rows` (Impact: 4.1)
  * `iterate-columns` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 48`, `orphaned_logic: 4`
* *Architecture:* None
* *Defense:* `safety: 14`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rock-paper-scissors.cob` (COBOL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.056 IQR)
- **Top Global Matches:** file_cluster_8: 12.056, file_cluster_17: 12.583, file_cluster_0: 12.664
- **Magnitude:** 39.9 | **LOC:** 55 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6337%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* None
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fizzbuzz.cob` (COBOL | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.363 IQR)
- **Top Global Matches:** file_cluster_8: 12.363, file_cluster_17: 12.801, file_cluster_0: 12.893
- **Magnitude:** 26.44 | **LOC:** 39 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.7574%), Tech Debt (98.9347%)
**Top Internal Functions/Classes:**
  * `PLAY-FIZZBUZZ` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 9`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hello-world.cob` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.706 IQR)
- **Top Global Matches:** file_cluster_8: 7.706, file_cluster_7: 8.798, file_cluster_1: 8.915
- **Magnitude:** 12.6 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `readme.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 3.22 | **LOC:** 161 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greet.cob` (COBOL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.534 IQR)
- **Top Global Matches:** file_cluster_8: 8.534, file_cluster_7: 9.426, file_cluster_1: 9.613
- **Magnitude:** 2.86 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.0858%), Tech Debt (99.9955%)
**Top Internal Functions/Classes:**
  * `A000-FIRST-PARA` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run-in-docker.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.841 IQR)
- **Top Global Matches:** file_cluster_8: 7.841, file_cluster_7: 8.776, file_cluster_1: 8.965
- **Magnitude:** 1.12 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `game-of-life.cob` (COBOL) | Magnitude: 92.34 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 77, state_mutation: 48, branch: 42, safety: 14
- `fizzbuzz.cob` (COBOL) | Magnitude: 26.44 | Delta: **0.438 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 18, structural_boundaries: 9, branch: 7
- `rock-paper-scissors.cob` (COBOL) | Magnitude: 39.9 | Delta: **0.527 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 24, structural_boundaries: 10, branch: 9
- `greet.cob` (COBOL) | Magnitude: 2.86 | Delta: **0.892 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 12, debug_prints: 6, func_start: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `fizzbuzz.cob` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `game-of-life.cob` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `greet.cob` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `rock-paper-scissors.cob` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `hello-world.cob` -> **Severity: 567.628** (Blast Radius: 142.857 * Doc Risk: 3.9734%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
