# ARCHITECTURAL_BRIEF: jcl-assess
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/jcl-assess` |
| **Timestamp** | `2026-08-07T03:51:15.369203+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `master` |
| **Git Commit** | `e8f1033b8987968fd0bb8316ec63c047afb51a80` |
| **Git Remote** | `https://github.com/ykhwong/jcl-assess.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4 malicious artifacts.

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
| Cognitive Load Exposure | 5.0 | 100.0 | 63.9 | 86.9 | 5.0 |
| Error & Exception Exposure | 91.7 | 100.0 | 98.1 | 99.1 | 98.8 |
| Tech Debt Exposure | 0.0 | 100.0 | 68.5 | 100.0 | 100.0 |
| Testing Exposure | 1.7 | 80.0 | 41.1 | 41.7 | 80.0 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 83.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 8.3 | 2.4 | 0.0 | 0.0 |
| Specification Exposure | 60.0 | 100.0 | 87.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 7.2 | 22.4 | 12.2 | 11.9 | 11.9 |
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

- `uniq` (@ `jcl_assess.pl`) -> Impact: **772.5** | LOC: 782
- `cobol_search` (@ `jcl_assess.pl`) -> Impact: **685.7** | LOC: 754
- `jcl_proc_search` (@ `jcl_assess.pl`) -> Impact: **457.3** | LOC: 590
- `parse` (@ `cobol_parser.pl`) -> Impact: **305.7** | LOC: 433
- `process` (@ `jcl_assess.pl`) -> Impact: **82.8** | LOC: 135
- `Anonymous_Block` (@ `make_tree.sh`) -> Impact: **51.4** | LOC: 39
- `Anonymous_Block` (@ `jcl_assess.sh`) -> Impact: **17.8** | LOC: 15
- `Anonymous_Block` (@ `make_tree.sh`) -> Impact: **16.3** | LOC: 14
- `Anonymous_Block` (@ `jcl_assess.sh`) -> Impact: **9.3** | LOC: 7
- `load_file` (@ `jcl_assess.pl`) -> Impact: **7.7** | LOC: 12

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 7 | 3838.64 | 54.78% | 58.69% |

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

1. **`jcl_assess.sh`** -> AI Confidence: **99.17%**
2. **`make_tree.sh`** -> AI Confidence: **99.06%**
3. **`result_split.sh`** -> AI Confidence: **99.06%**
4. **`show_result.sh`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `make_tree.sh` (SHELL) -> Cumulative Risk: **591.89**
- **Archetype:** `file_cluster_12` (Distance: 13.214 IQR)
- **Magnitude:** 148.42 | **LOC:** 78 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9954%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 51.4), `Anonymous_Block` (Impact: 16.3), `Anonymous_Block` (Impact: 5.2)

### 2. `jcl_assess.sh` (SHELL) -> Cumulative Risk: **514.34**
- **Archetype:** `file_cluster_8` (Distance: 11.273 IQR)
- **Magnitude:** 54.1 | **LOC:** 41 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.7527%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 17.8), `Anonymous_Block` (Impact: 9.3), `Anonymous_Block` (Impact: 5.2)

### 3. `cobol_parser.pl` (PERL) -> Cumulative Risk: **497.59**
- **Archetype:** `file_cluster_8` (Distance: 13.484 IQR)
- **Magnitude:** 856.04 | **LOC:** 638 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.76%), Cognitive Load (89.9034%)
- **Heaviest Functions:** `parse` (Impact: 305.7), `_slurp` (Impact: 4.7), `uniq` (Impact: 1.1)

### 4. `jcl_assess.pl` (PERL) -> Cumulative Risk: **493.5**
- **Archetype:** `file_cluster_0` (Distance: 13.492 IQR)
- **Magnitude:** 2761.28 | **LOC:** 894 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.9654%), Cognitive Load (83.83%)
- **Heaviest Functions:** `uniq` (Impact: 772.5), `cobol_search` (Impact: 685.7), `jcl_proc_search` (Impact: 457.3)

### 5. `result_split.sh` (SHELL) -> Cumulative Risk: **373.72**
- **Archetype:** `file_cluster_8` (Distance: 11.795 IQR)
- **Magnitude:** 11.68 | **LOC:** 11 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Safety Score (99.8736%), Spec Match (60.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 4.4), `__global_context__` (Impact: 1.1)

### 6. `show_result.sh` (SHELL) -> Cumulative Risk: **273.14**
- **Archetype:** `file_cluster_8` (Distance: 6.886 IQR)
- **Magnitude:** 5.6 | **LOC:** 11 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Safety Score (91.6827%), Spec Match (66.6667%), Documentation (7.9469%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 4.2), `__global_context__` (Impact: 1.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `jcl_assess.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.492 IQR)
- **Top Global Matches:** file_cluster_0: 13.492, file_cluster_8: 13.825, file_cluster_13: 13.943
- **Magnitude:** 2761.28 | **LOC:** 894 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.83%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `uniq` (Impact: 772.5)
  * `cobol_search` (Impact: 685.7)
  * `jcl_proc_search` (Impact: 457.3)
  * `process` (Impact: 82.8)
  * `load_file` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 181`, `args: 7`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 16`, `state_mutation: 719`, `dead_code: 6`
* *Architecture:* `io: 4`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` POSIX, strict, File::Copy, File::Basename
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol_parser.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.484 IQR)
- **Top Global Matches:** file_cluster_8: 13.484, file_cluster_0: 13.567, file_cluster_13: 13.664
- **Magnitude:** 856.04 | **LOC:** 638 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.9034%), Tech Debt (10.8124%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 305.7)
  * `_slurp` (Impact: 4.7)
  * `uniq` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 78`, `args: 3`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 533`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` POSIX, strict, Encode, File::Basename
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `make_tree.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_12` (Drift: 13.214 IQR)
- **Top Global Matches:** file_cluster_12: 13.214, file_cluster_11: 13.444, file_cluster_8: 13.587
- **Magnitude:** 148.42 | **LOC:** 78 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9792%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 51.4)
  * `Anonymous_Block` (Impact: 16.3)
  * `Anonymous_Block` (Impact: 5.2)
  * `Anonymous_Block` (Impact: 4.2)
  * `__global_context__` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 24`, `args: 2`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 68`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 30`
* *Defense:* `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gei
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jcl_assess.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.273 IQR)
- **Top Global Matches:** file_cluster_8: 11.273, file_cluster_12: 11.384, file_cluster_11: 11.721
- **Magnitude:** 54.1 | **LOC:** 41 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.7527%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 17.8)
  * `Anonymous_Block` (Impact: 9.3)
  * `Anonymous_Block` (Impact: 5.2)
  * `Anonymous_Block` (Impact: 4.2)
  * `__global_context__` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 9`, `args: 1`
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
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 4.4)
  * `__global_context__` (Impact: 1.1)
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
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 4.2)
  * `__global_context__` (Impact: 1.2)
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
- `jcl_assess.pl` (PERL) | Magnitude: 2761.28 | Delta: **0.333 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 746, state_mutation: 719, branch: 334, structural_boundaries: 181

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `make_tree.sh` (SHELL) | Magnitude: 148.42 | Delta: **0.23 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 68, branch: 51, indent_tabs: 45, safety_bypasses: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cobol_parser.pl` (PERL) | Magnitude: 856.04 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 533, indent_spaces: 388, branch: 167, bitwise_ops: 124
- `jcl_assess.sh` (SHELL) | Magnitude: 54.1 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 31, indent_tabs: 19, state_mutation: 15, safety_bypasses: 12
- `result_split.sh` (SHELL) | Magnitude: 11.68 | Delta: **0.173 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: safety_bypasses: 9, state_mutation: 6, branch: 3, structural_boundaries: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jcl_assess.pl` -> **Severity: 3193.625** (Blast Radius: 142.857 * Doc Risk: 22.3554%)
- `cobol_parser.pl` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `jcl_assess.sh` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `make_tree.sh` -> **Severity: 1702.898** (Blast Radius: 142.857 * Doc Risk: 11.9203%)
- `show_result.sh` -> **Severity: 1135.27** (Blast Radius: 142.857 * Doc Risk: 7.9469%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
