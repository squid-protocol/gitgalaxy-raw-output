# ARCHITECTURAL_BRIEF: jcl-assess
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/jcl-assess` |
| **Timestamp** | `2026-08-03T19:29:05.487994+00:00` |
| **Scan Duration** | `0.17s` |
| **Git Branch** | `master` |
| **Git Commit** | `e8f1033b8987968fd0bb8316ec63c047afb51a80` |
| **Git Remote** | `https://github.com/ykhwong/jcl-assess.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 23 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 1526 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 30.4% |
| Dominant Lang | PERL |

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
| SHELL | 4 | 125 | 57.1% |
| PERL | 2 | 1401 | 28.6% |
| MARKDOWN | 1 | 0 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.086`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4 | 57.1% |
| file_cluster_0 | 1 | 14.3% |
| file_cluster_12 | 1 | 14.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 14.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `no_extension`: 9x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lst`: 6x Excluded (Unsupported Extension: '.lst')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 100.0 | 66.6 | 95.0 | 5.0 |
| Error & Exception Exposure | 80.0 | 100.0 | 94.6 | 96.7 | 94.8 |
| Tech Debt Exposure | 0.0 | 100.0 | 68.5 | 100.0 | 100.0 |
| Testing Exposure | 1.7 | 80.0 | 41.1 | 41.5 | 80.0 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 83.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 8.3 | 2.4 | 0.0 | 0.0 |
| Specification Exposure | 60.0 | 100.0 | 87.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 7.2 | 18.2 | 11.6 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `make_tree.sh` (Hits: 30)
- `jcl_assess.sh` (Hits: 6)
- `jcl_assess.pl` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`README.md`) — 0 inbound connections
2. **cobol_parser.pl** (`cobol_parser.pl`) — 0 inbound connections
3. **jcl_assess.pl** (`jcl_assess.pl`) — 0 inbound connections
4. **jcl_assess.sh** (`jcl_assess.sh`) — 0 inbound connections
5. **make_tree.sh** (`make_tree.sh`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cobol_parser.pl** (`cobol_parser.pl`) — 4 outbound dependencies
2. **jcl_assess.pl** (`jcl_assess.pl`) — 4 outbound dependencies
3. **make_tree.sh** (`make_tree.sh`) — 1 outbound dependencies
4. **README.md** (`README.md`) — 0 outbound dependencies
5. **jcl_assess.sh** (`jcl_assess.sh`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `uniq` (@ `jcl_assess.pl`) -> Impact: **2870.0** | LOC: 782
- `parse` (@ `cobol_parser.pl`) -> Impact: **2058.5** | LOC: 433
- `Anonymous_Block` (@ `make_tree.sh`) -> Impact: **34.5** | LOC: 39
- `Anonymous_Block` (@ `make_tree.sh`) -> Impact: **13.4** | LOC: 14
- `Anonymous_Block` (@ `jcl_assess.sh`) -> Impact: **11.8** | LOC: 15
- `cp_file` (@ `jcl_assess.pl`) -> Impact: **9.1** | LOC: 8
- `save_file` (@ `jcl_assess.pl`) -> Impact: **8.4** | LOC: 9
- `load_file` (@ `jcl_assess.pl`) -> Impact: **7.7** | LOC: 12
- `Anonymous_Block` (@ `jcl_assess.sh`) -> Impact: **7.3** | LOC: 7
- `_slurp` (@ `cobol_parser.pl`) -> Impact: **4.7** | LOC: 9

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `parse` (@ `cobol_parser.pl`) -> **O(2^N) [Recursive]**
- `uniq` (@ `jcl_assess.pl`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `uniq` (@ `jcl_assess.pl`) -> DB Complexity: **227**
- `parse` (@ `cobol_parser.pl`) -> DB Complexity: **171**
- `Anonymous_Block` (@ `make_tree.sh`) -> DB Complexity: **80**
- `Anonymous_Block` (@ `make_tree.sh`) -> DB Complexity: **38**
- `_slurp` (@ `cobol_parser.pl`) -> DB Complexity: **12**
- `Anonymous_Block` (@ `jcl_assess.sh`) -> DB Complexity: **10**
- `load_file` (@ `jcl_assess.pl`) -> DB Complexity: **9**
- `Anonymous_Block` (@ `result_split.sh`) -> DB Complexity: **9**
- `save_file` (@ `jcl_assess.pl`) -> DB Complexity: **7**
- `Anonymous_Block` (@ `jcl_assess.sh`) -> DB Complexity: **7**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 7 | 6444.04 | 57.09% | 58.69% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `jcl_assess.sh` -> **100.0%** Exposure
- `make_tree.sh` -> **100.0%** Exposure
- `result_split.sh` -> **100.0%** Exposure
- `show_result.sh` -> **100.0%** Exposure
- `cobol_parser.pl` -> **10.8124%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cobol_parser.pl` -> **100.0%** Exposure
- `jcl_assess.pl` -> **100.0%** Exposure
- `jcl_assess.sh` -> **100.0%** Exposure
- `make_tree.sh` -> **100.0%** Exposure
- `result_split.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jcl_assess.sh` -> **1** Orphaned Functions | **4** Duplicates
- `make_tree.sh` -> **1** Orphaned Functions | **4** Duplicates
- `cobol_parser.pl` -> **1** Orphaned Functions | **0** Duplicates
- `result_split.sh` -> **1** Orphaned Functions | **0** Duplicates
- `show_result.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jcl_assess.sh`** -> AI Confidence: **99.11%**
2. **`make_tree.sh`** -> AI Confidence: **99.06%**
3. **`result_split.sh`** -> AI Confidence: **99.06%**
4. **`show_result.sh`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `cobol_parser.pl` -> **100.0%** Exposure
- `jcl_assess.pl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `make_tree.sh` -> **100.0%** Exposure
- `jcl_assess.pl` -> **0.0206%** Exposure
### Algorithmic DoS Exposure
- `cobol_parser.pl` -> **100.0%** Exposure
- `jcl_assess.pl` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cobol_parser.pl` (PERL) -> Cumulative Risk: **700.98**
- **Archetype:** `file_cluster_8` (Distance: 13.517 IQR)
- **Magnitude:** 2614.84 | **LOC:** 638 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `parse` (Impact: 2058.5), `_slurp` (Impact: 4.7), `uniq` (Impact: 1.1)

### 2. `jcl_assess.pl` (PERL) -> Cumulative Risk: **695.35**
- **Archetype:** `file_cluster_0` (Distance: 13.57 IQR)
- **Magnitude:** 3639.88 | **LOC:** 894 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `uniq` (Impact: 2870.0), `cp_file` (Impact: 9.1), `save_file` (Impact: 8.4)

### 3. `make_tree.sh` (SHELL) -> Cumulative Risk: **691.9**
- **Archetype:** `file_cluster_12` (Distance: 13.17 IQR)
- **Magnitude:** 126.52 | **LOC:** 78 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 34.5), `Anonymous_Block` (Impact: 13.4), `Anonymous_Block` (Impact: 4.2)

### 4. `jcl_assess.sh` (SHELL) -> Cumulative Risk: **512.18**
- **Archetype:** `file_cluster_8` (Distance: 11.214 IQR)
- **Magnitude:** 44.0 | **LOC:** 41 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.7527%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 11.8), `Anonymous_Block` (Impact: 7.3), `Anonymous_Block` (Impact: 4.2)

### 5. `result_split.sh` (SHELL) -> Cumulative Risk: **373.58**
- **Archetype:** `file_cluster_8` (Distance: 11.795 IQR)
- **Magnitude:** 11.68 | **LOC:** 11 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Safety Score (99.7259%), Spec Match (60.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 4.4), `__global_context__` (Impact: 1.1)

### 6. `show_result.sh` (SHELL) -> Cumulative Risk: **261.46**
- **Archetype:** `file_cluster_8` (Distance: 6.886 IQR)
- **Magnitude:** 5.6 | **LOC:** 11 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Safety Score (80.0%), Spec Match (66.6667%), Documentation (7.9469%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 4.2), `__global_context__` (Impact: 1.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `jcl_assess.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.57 IQR)
- **Top Global Matches:** file_cluster_0: 13.57, file_cluster_8: 13.91, file_cluster_11: 14.009
- **Magnitude:** 3639.88 | **LOC:** 894 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 227
- **Risk Profile:** Cognitive Load (98.9282%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `uniq` (Impact: 2870.0 | O(2^N) | DB: 227)
  * `cp_file` (Impact: 9.1 | O(N^1))
  * `save_file` (Impact: 8.4 | O(N^1) | DB: 7)
  * `load_file` (Impact: 7.7 | O(N^1) | DB: 9)
  * `uniq_helper` (Impact: 1.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 171`, `args: 7`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 727`, `dead_code: 6`
* *Architecture:* `io: 4`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, File::Copy, POSIX, File::Basename
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol_parser.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.517 IQR)
- **Top Global Matches:** file_cluster_8: 13.517, file_cluster_0: 13.601, file_cluster_13: 13.696
- **Magnitude:** 2614.84 | **LOC:** 638 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 171
- **Risk Profile:** Cognitive Load (90.9935%), Tech Debt (10.8124%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 2058.5 | O(2^N) | DB: 171)
  * `_slurp` (Impact: 4.7 | O(N^1) | DB: 12)
  * `uniq` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 71`, `args: 3`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 539`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, POSIX, File::Basename, Encode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `make_tree.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_12` (Drift: 13.17 IQR)
- **Top Global Matches:** file_cluster_12: 13.17, file_cluster_11: 13.42, file_cluster_8: 13.527
- **Magnitude:** 126.52 | **LOC:** 78 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 80
- **Risk Profile:** Cognitive Load (99.9878%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 34.5 | O(N^1) | DB: 80)
  * `Anonymous_Block` (Impact: 13.4 | O(N^1) | DB: 38)
  * `Anonymous_Block` (Impact: 4.2 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 3.1 | O(N^1))
  * `__global_context__` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 24`, `args: 2`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 68`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 30`
* *Defense:* `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gei
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jcl_assess.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.214 IQR)
- **Top Global Matches:** file_cluster_8: 11.214, file_cluster_12: 11.345, file_cluster_13: 11.703
- **Magnitude:** 44.0 | **LOC:** 41 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (99.7527%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 11.8 | O(N^1) | DB: 7)
  * `Anonymous_Block` (Impact: 7.3 | O(N^1) | DB: 10)
  * `Anonymous_Block` (Impact: 4.2 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 3.1 | O(N^1))
  * `__global_context__` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 9`, `args: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 15`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 6`
* *Defense:* `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `result_split.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.795 IQR)
- **Top Global Matches:** file_cluster_8: 11.795, file_cluster_12: 11.968, file_cluster_11: 12.188
- **Magnitude:** 11.68 | **LOC:** 11 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 4.4 | O(N^1) | DB: 9)
  * `__global_context__` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `show_result.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.886 IQR)
- **Top Global Matches:** file_cluster_8: 6.886, file_cluster_7: 7.991, file_cluster_1: 8.166
- **Magnitude:** 5.6 | **LOC:** 11 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 4.2 | O(N^1) | DB: 6)
  * `__global_context__` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.52 | **LOC:** 76 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `jcl_assess.pl` (PERL) | Magnitude: 3639.88 | Delta: **0.34 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 746, state_mutation: 727, branch: 436, structural_boundaries: 171

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `make_tree.sh` (SHELL) | Magnitude: 126.52 | Delta: **0.25 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 68, indent_tabs: 45, safety_bypasses: 36, branch: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cobol_parser.pl` (PERL) | Magnitude: 2614.84 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 539, indent_spaces: 388, branch: 173, bitwise_ops: 124
- `jcl_assess.sh` (SHELL) | Magnitude: 44.0 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 21, indent_tabs: 19, state_mutation: 15, safety_bypasses: 12
- `result_split.sh` (SHELL) | Magnitude: 11.68 | Delta: **0.173 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: safety_bypasses: 9, state_mutation: 6, branch: 3, structural_boundaries: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cobol_parser.pl` -> **Severity: 2597.94** (Blast Radius: 142.857 * Doc Risk: 18.1856%)
- `jcl_assess.pl` -> **Severity: 1742.655** (Blast Radius: 142.857 * Doc Risk: 12.1986%)
- `jcl_assess.sh` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `make_tree.sh` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `show_result.sh` -> **Severity: 1135.27** (Blast Radius: 142.857 * Doc Risk: 7.9469%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
