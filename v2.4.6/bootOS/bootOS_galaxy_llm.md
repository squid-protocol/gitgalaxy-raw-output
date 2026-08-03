# ARCHITECTURAL_BRIEF: bootOS
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/bootOS` |
| **Timestamp** | `2026-08-03T19:26:49.402834+00:00` |
| **Scan Duration** | `0.17s` |
| **Git Branch** | `master` |
| **Git Commit** | `766f7011a951b29f4e9c87ff6f30f9bab03b4574` |
| **Git Remote** | `https://github.com/nanochess/bootOS.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2 malicious artifacts.

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
| Total Artifacts | 18 |
| Analyzed Artifacts (Scanned) | 8 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 1060 |
| Volatility Index | 0.125 |
| % Scanned of codebase = | 44.4% |
| Dominant Lang | ASSEMBLY |

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
| ASSEMBLY | 5 | 1046 | 62.5% |
| MAKEFILE | 1 | 11 | 12.5% |
| MARKDOWN | 1 | 0 | 12.5% |
| BATCH | 1 | 3 | 12.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.692`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 7 | 87.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 12.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `.img`: 5x Excluded (Unsupported Extension: '.img')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lst`: 2x Excluded (Unsupported Extension: '.lst')
- `.fdd`: 1x Excluded (Unsupported Extension: '.fdd')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 29.3 | 18.2 | 21.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 14.4 | 6.8 | 7.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 50.3 | 46.0 | 0.0 |
| Testing Exposure | 0.5 | 80.0 | 46.4 | 80.0 | 80.0 |
| API Exposure | 0.0 | 12.2 | 1.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 70.6 | 41.0 | 50.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 13.4 | 2.7 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 84.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 2.4 | 16.6 | 11.3 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 6.2 | 1.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.8 | 0.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 0)
- `README.md` (Hits: 0)
- `counter.asm` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Makefile** (`Makefile`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **counter.asm** (`counter.asm`) — 0 inbound connections
4. **os.asm** (`os.asm`) — 0 inbound connections
5. **mine.asm** (`patch/mine.asm`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Makefile** (`Makefile`) — 0 outbound dependencies
2. **README.md** (`README.md`) — 0 outbound dependencies
3. **counter.asm** (`counter.asm`) — 0 outbound dependencies
4. **os.asm** (`os.asm`) — 0 outbound dependencies
5. **mine.asm** (`patch/mine.asm`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `.after_al` (@ `patch/sokoban.asm`) -> Impact: **35.5** | LOC: 59
- `.Empty` (@ `patch/mine.asm`) -> Impact: **26.7** | LOC: 25
- `os6` (@ `os.asm`) -> Impact: **21.8** | LOC: 12
- `update_body` (@ `patch/snake.asm`) -> Impact: **20.2** | LOC: 8
- `disk` (@ `os.asm`) -> Impact: **17.7** | LOC: 14
  * *Intent:* ; ; Do disk operation. ; ; Input: ; AH = 0x02 read disk, 0x03 write disk ; ES:BX = data source/target ; CH = Track number ; CL = Sector number ;...
- `os22` (@ `os.asm`) -> Impact: **17.4** | LOC: 8
- `os19` (@ `os.asm`) -> Impact: **17.4** | LOC: 9
- `.loop` (@ `patch/sokoban.asm`) -> Impact: **14.9** | LOC: 15
- `snake_body_print_loop` (@ `patch/snake.asm`) -> Impact: **14.6** | LOC: 9
- `Flood` (@ `patch/mine.asm`) -> Impact: **13.7** | LOC: 19
  * *Intent:* ;; Flood fill empty cells ;; ;; Parameters: ;; * BP - Cell index ;; Clobbered registers: ;; * Yes [TODO]

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `os6` (@ `os.asm`) -> **O(2^N) [Recursive]**
- `disk` (@ `os.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; ; Do disk operation. ; ; Input: ; AH = 0x02 read disk, 0x03 write disk ; ES:BX = data source/target ; CH = Track number ; CL = Sector number ;...
- `os22` (@ `os.asm`) -> **O(2^N) [Recursive]**
- `os19` (@ `os.asm`) -> **O(2^N) [Recursive]**
- `restart` (@ `os.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; ; Warm start of bootOS ;
- `output_string` (@ `os.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; ; Output string ; ; Entry: ; SI = address ; ; Implementation: ; It assumes that SI never points to a zero length string. ;
- `xdigit` (@ `os.asm`) -> **O(2^N) [Recursive]**
  * *Intent:* ; ; Convert ASCII letter to hexadecimal digit ;
- `update_body` (@ `patch/snake.asm`) -> **O(2^N) [Recursive]**
- `snake_body_print_loop` (@ `patch/snake.asm`) -> **O(2^N) [Recursive]**
- `push_digits` (@ `patch/snake.asm`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `.1` (@ `counter.asm`) -> DB Complexity: **2**
- `get_location` (@ `os.asm`) -> DB Complexity: **2**
  * *Intent:* ; ; Get location of file on disk ; ; Entry: ; DI = Pointer to entry in directory. ; ; Output: ; CH = Track number in disk. ; CL = Sector (always 0x01)...
- `os1` (@ `os.asm`) -> DB Complexity: **2**
- `.loop` (@ `patch/sokoban.asm`) -> DB Complexity: **2**
- `os19` (@ `os.asm`) -> DB Complexity: **1**
- `.loop` (@ `os.asm`) -> DB Complexity: **1**
- `os11` (@ `os.asm`) -> DB Complexity: **1**
  * *Intent:* ; Notice that filenames starting with same characters ; won't be recognized as such (so file dirab cannot be ; executed).
- `format_command` (@ `os.asm`) -> DB Complexity: **1**
  * *Intent:* ; ; >> COMMAND << ; format ;
- `.Right` (@ `patch/mine.asm`) -> DB Complexity: **1**
- `.CmpLeft` (@ `patch/mine.asm`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `patch` | 3 | 577.84 | 26.06% | 75.71% |
| `__monolith__` | 5 | 423.88 | 9.87% | 24.96% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `patch/mine.asm` -> **100.0%** Exposure
- `patch/sokoban.asm` -> **99.9921%** Exposure
- `counter.asm` -> **78.8108%** Exposure
- `os.asm` -> **45.9765%** Exposure
- `patch/snake.asm` -> **27.1234%** Exposure
### Highest State Flux (Mutation/Volatility)
- `patch/snake.asm` -> **70.6147%** Exposure
- `counter.asm` -> **64.8366%** Exposure
- `os.asm` -> **52.337%** Exposure
- `patch/sokoban.asm` -> **50.1316%** Exposure
- `patch/mine.asm` -> **48.7823%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `patch/mine.asm` -> **18** Orphaned Functions | **6** Duplicates
- `patch/sokoban.asm` -> **16** Orphaned Functions | **4** Duplicates
- `os.asm` -> **6** Orphaned Functions | **0** Duplicates
- `patch/snake.asm` -> **2** Orphaned Functions | **0** Duplicates
- `counter.asm` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Makefile`** -> AI Confidence: **98.84%**
2. **`e.bat`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `patch/sokoban.asm` -> **0.8102%** Exposure
### Algorithmic DoS Exposure
- `os.asm` -> **6.2208%** Exposure
- `counter.asm` -> **1.7282%** Exposure
- `patch/sokoban.asm` -> **1.1791%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `patch/sokoban.asm` (ASSEMBLY) -> Cumulative Risk: **392.83**
- **Archetype:** `file_cluster_8` (Distance: 12.506 IQR)
- **Magnitude:** 179.36 | **LOC:** 398 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9921%), Verification (80.0%), State Flux (50.1316%)
- **Heaviest Functions:** `.after_al` (Impact: 35.5), `.loop` (Impact: 14.9), `.mainloop` (Impact: 9.4)

### 2. `patch/mine.asm` (ASSEMBLY) -> Cumulative Risk: **377.74**
- **Archetype:** `file_cluster_8` (Distance: 9.882 IQR)
- **Magnitude:** 198.98 | **LOC:** 405 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Verification (80.0%), State Flux (48.7823%)
- **Heaviest Functions:** `.Empty` (Impact: 26.7), `Flood` (Impact: 13.7), `RightIncIfMineAtCell` (Impact: 13.5)

### 3. `os.asm` (ASSEMBLY) -> Cumulative Risk: **331.82**
- **Archetype:** `file_cluster_8` (Distance: 9.964 IQR)
- **Magnitude:** 360.5 | **LOC:** 656 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (52.337%), Tech Debt (45.9765%)
- **Heaviest Functions:** `os6` (Impact: 21.8), `disk` (Impact: 17.7), `os22` (Impact: 17.4)

### 4. `patch/snake.asm` (ASSEMBLY) -> Cumulative Risk: **328.39**
- **Archetype:** `file_cluster_8` (Distance: 9.968 IQR)
- **Magnitude:** 199.5 | **LOC:** 242 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (70.6147%), Tech Debt (27.1234%)
- **Heaviest Functions:** `update_body` (Impact: 20.2), `snake_body_print_loop` (Impact: 14.6), `print_stuff` (Impact: 12.1)

### 5. `counter.asm` (ASSEMBLY) -> Cumulative Risk: **292.37**
- **Archetype:** `file_cluster_8` (Distance: 9.495 IQR)
- **Magnitude:** 27.48 | **LOC:** 91 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (78.8108%), State Flux (64.8366%), Cognitive Load (18.1165%)
- **Heaviest Functions:** `start` (Impact: 7.9), `.1` (Impact: 7.1), `.2` (Impact: 5.3)

### 6. `Makefile` (MAKEFILE) -> Cumulative Risk: **100.93**
- **Archetype:** `file_cluster_8` (Distance: 6.942 IQR)
- **Magnitude:** 20.22 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (73.3333%), Api Exposure (12.1705%), Documentation (8.7415%), Cognitive Load (5.0%)

### 7. `e.bat` (BATCH) -> Cumulative Risk: **27.84**
- **Archetype:** `file_cluster_8` (Distance: 4.447 IQR)
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (20.0%), Cognitive Load (5.0%), Documentation (2.3841%), Verification (0.4595%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `os.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.964 IQR)
- **Top Global Matches:** file_cluster_8: 9.964, file_cluster_17: 10.629, file_cluster_7: 10.697
- **Magnitude:** 360.5 | **LOC:** 656 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.2541%), Tech Debt (45.9765%)
**Top Internal Functions/Classes:**
  * `os6` (Impact: 21.8 | O(2^N))
  * `disk` (Impact: 17.7 | O(2^N))
    * *Intent:* ; ; Do disk operation. ; ; Input: ; AH = 0x02 read disk, 0x03 write disk ; ES:BX = data source/targe...
  * `os22` (Impact: 17.4 | O(2^N))
  * `os19` (Impact: 17.4 | O(2^N) | DB: 1)
  * `restart` (Impact: 13.6 | O(2^N))
    * *Intent:* ; ; Warm start of bootOS ;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 104`, `args: 129`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`, `dead_code: 1`, `orphaned_logic: 6`
* *Architecture:* None
* *Defense:* `safety: 1`, `sync_locks: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patch/snake.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.968 IQR)
- **Top Global Matches:** file_cluster_8: 9.968, file_cluster_1: 10.51, file_cluster_7: 10.717
- **Magnitude:** 199.5 | **LOC:** 242 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (25.2803%), Tech Debt (27.1234%)
**Top Internal Functions/Classes:**
  * `update_body` (Impact: 20.2 | O(2^N))
  * `snake_body_print_loop` (Impact: 14.6 | O(2^N))
  * `print_stuff` (Impact: 12.1 | O(N^1))
  * `check_collisions` (Impact: 11.9 | O(N^1))
  * `push_digits` (Impact: 11.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 73`, `args: 101`, `func_start: 32`
* *Risk/State:* `state_mutation: 16`, `orphaned_logic: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patch/mine.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.882 IQR)
- **Top Global Matches:** file_cluster_8: 9.882, file_cluster_1: 10.506, file_cluster_7: 10.63
- **Magnitude:** 198.98 | **LOC:** 405 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (29.3107%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `.Empty` (Impact: 26.7 | O(N^1))
  * `Flood` (Impact: 13.7 | O(N^1))
    * *Intent:* ;; Flood fill empty cells ;; ;; Parameters: ;; * BP - Cell index ;; Clobbered registers: ;; * Yes [T...
  * `RightIncIfMineAtCell` (Impact: 13.5 | O(N^1))
  * `LeftIncIfMineAtCell` (Impact: 12.0 | O(N^1))
  * `IncIfMineAtCell` (Impact: 10.3 | O(N^1))
    * *Intent:* ;; TODO: Update comment ;; ;; Increment AX if there is a mine in Map.Mines at index BX, where BX is ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 88`, `args: 117`, `func_start: 36`
* *Risk/State:* `state_mutation: 12`, `planned_debt: 7`, `duplicate_logic: 6`, `orphaned_logic: 18`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `patch/sokoban.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.506 IQR)
- **Top Global Matches:** file_cluster_8: 12.506, file_cluster_0: 12.883, file_cluster_17: 12.891
- **Magnitude:** 179.36 | **LOC:** 398 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (23.5873%), Tech Debt (99.9921%)
**Top Internal Functions/Classes:**
  * `.after_al` (Impact: 35.5 | O(N^1))
  * `.loop` (Impact: 14.9 | O(N^1) | DB: 2)
  * `.mainloop` (Impact: 9.4 | O(N^1))
  * `wait_for_esc` (Impact: 8.9 | O(2^N))
  * `.loop` (Impact: 7.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 83`, `args: 156`, `func_start: 28`
* *Risk/State:* `state_mutation: 12`, `dead_code: 5`, `duplicate_logic: 4`, `orphaned_logic: 16`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `counter.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.495 IQR)
- **Top Global Matches:** file_cluster_8: 9.495, file_cluster_1: 9.873, file_cluster_7: 10.286
- **Magnitude:** 27.48 | **LOC:** 91 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (18.1165%), Tech Debt (78.8108%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 7.9 | O(N^2))
  * `.1` (Impact: 7.1 | O(N^2) | DB: 2)
  * `.2` (Impact: 5.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 38`, `args: 36`, `func_start: 8`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.942 IQR)
- **Top Global Matches:** file_cluster_8: 6.942, file_cluster_7: 7.996, file_cluster_1: 8.2
- **Magnitude:** 20.22 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 5`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e.bat` (BATCH | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 4.12 | **LOC:** 206 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 125.0
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `patch/sokoban.asm` (ASSEMBLY) | Magnitude: 179.36 | Delta: **0.377 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 195, args: 156, structural_boundaries: 83, branch: 75
- `counter.asm` (ASSEMBLY) | Magnitude: 27.48 | Delta: **0.378 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 38, args: 36, func_start: 8
- `patch/snake.asm` (ASSEMBLY) | Magnitude: 199.5 | Delta: **0.542 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_tabs: 172, args: 101, structural_boundaries: 73, branch: 66
- `patch/mine.asm` (ASSEMBLY) | Magnitude: 198.98 | Delta: **0.624 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 192, args: 117, branch: 95, structural_boundaries: 88
- `os.asm` (ASSEMBLY) | Magnitude: 360.5 | Delta: **0.665 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 245, args: 129, structural_boundaries: 104, branch: 78

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `patch/snake.asm` -> **Severity: 2068.913** (Blast Radius: 125.0 * Doc Risk: 16.5513%)
- `patch/sokoban.asm` -> **Severity: 1994.688** (Blast Radius: 125.0 * Doc Risk: 15.9575%)
- `counter.asm` -> **Severity: 1490.037** (Blast Radius: 125.0 * Doc Risk: 11.9203%)
- `os.asm` -> **Severity: 1490.037** (Blast Radius: 125.0 * Doc Risk: 11.9203%)
- `patch/mine.asm` -> **Severity: 1490.037** (Blast Radius: 125.0 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
