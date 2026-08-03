# ARCHITECTURAL_BRIEF: pillman
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/pillman` |
| **Timestamp** | `2026-08-03T19:27:35.213252+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `master` |
| **Git Commit** | `d3945524359134f7db890affe64742515b1d25bd` |
| **Git Remote** | `https://github.com/nanochess/pillman.git` |
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
| Total Artifacts | 13 |
| Analyzed Artifacts (Scanned) | 9 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 1592 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.2% |
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
| ASSEMBLY | 6 | 1573 | 66.7% |
| MAKEFILE | 1 | 16 | 11.1% |
| MARKDOWN | 1 | 0 | 11.1% |
| BATCH | 1 | 3 | 11.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.834`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 8 | 88.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 11.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.com`: 1x Excluded (Unsupported Extension: '.com')
- `.img`: 1x Excluded (Unsupported Extension: '.img')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 23.5 | 18.3 | 21.4 | 10.4 |
| Error & Exception Exposure | 0.0 | 9.4 | 6.8 | 8.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 14.0 | 4.3 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 80.0 | 60.3 | 80.0 | 80.0 |
| API Exposure | 0.0 | 11.9 | 1.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 59.6 | 38.4 | 45.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.0 | 5.9 | 6.9 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 90.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 24.1 | 12.1 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 4.8 | 3.4 | 4.5 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 0)
- `README` (Hits: 0)
- `e.bat` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Makefile** (`Makefile`) — 0 inbound connections
2. **README** (`README`) — 0 inbound connections
3. **e.bat** (`e.bat`) — 0 inbound connections
4. **pillman0.asm** (`old/pillman0.asm`) — 0 inbound connections
5. **pillman1.asm** (`old/pillman1.asm`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Makefile** (`Makefile`) — 0 outbound dependencies
2. **README** (`README`) — 0 outbound dependencies
3. **e.bat** (`e.bat`) — 0 outbound dependencies
4. **pillman0.asm** (`old/pillman0.asm`) — 0 outbound dependencies
5. **pillman1.asm** (`old/pillman1.asm`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ms9` (@ `old/pillman1.asm`) -> Impact: **34.3** | LOC: 7
- `ms9` (@ `old/pillman2.asm`) -> Impact: **30.0** | LOC: 6
- `in0` (@ `old/pillman0.asm`) -> Impact: **26.1** | LOC: 13
- `g9` (@ `old/pillman0.asm`) -> Impact: **20.2** | LOC: 22
- `move_ghost` (@ `old/pillman0.asm`) -> Impact: **20.2** | LOC: 22
  * *Intent:* ; ; Move ghost ;
- `game_loop` (@ `old/pillman3.asm`) -> Impact: **18.0** | LOC: 20
- `g1` (@ `old/pillman2.asm`) -> Impact: **17.7** | LOC: 14
- `close_mouth` (@ `old/pillman3.asm`) -> Impact: **17.7** | LOC: 14
- `ms9` (@ `old/pillman3.asm`) -> Impact: **17.3** | LOC: 6
- `ms9` (@ `old/pillman4.asm`) -> Impact: **17.3** | LOC: 6

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `in0` (@ `old/pillman0.asm`) -> **O(2^N) [Recursive]**
- `clock_wait` (@ `old/pillman0.asm`) -> **O(2^N) [Recursive]**
- `ms9` (@ `old/pillman1.asm`) -> **O(2^N) [Recursive]**
- `clock_wait` (@ `old/pillman1.asm`) -> **O(2^N) [Recursive]**
- `ms9` (@ `old/pillman2.asm`) -> **O(2^N) [Recursive]**
- `clock_wait` (@ `old/pillman2.asm`) -> **O(2^N) [Recursive]**
- `game_loop` (@ `old/pillman3.asm`) -> **O(2^N) [Recursive]**
- `ms9` (@ `old/pillman3.asm`) -> **O(2^N) [Recursive]**
- `dm3` (@ `old/pillman3.asm`) -> **O(2^N) [Recursive]**
- `ms9` (@ `old/pillman4.asm`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `g9` (@ `old/pillman0.asm`) -> DB Complexity: **3**
- `move_ghost` (@ `old/pillman0.asm`) -> DB Complexity: **2**
  * *Intent:* ; ; Move ghost ;
- `g9` (@ `old/pillman1.asm`) -> DB Complexity: **2**
- `move_ghost` (@ `old/pillman1.asm`) -> DB Complexity: **2**
  * *Intent:* ; ; Move ghost ;
- `g9` (@ `old/pillman2.asm`) -> DB Complexity: **2**
- `move_ghost` (@ `old/pillman2.asm`) -> DB Complexity: **2**
  * *Intent:* ; ; Move ghost ;
- `no_key` (@ `old/pillman3.asm`) -> DB Complexity: **2**
- `move_ghost` (@ `old/pillman3.asm`) -> DB Complexity: **2**
  * *Intent:* ; ; Move ghost ; bh = color ;
- `no_key2` (@ `old/pillman4.asm`) -> DB Complexity: **2**
- `move_ghost` (@ `old/pillman4.asm`) -> DB Complexity: **2**
  * *Intent:* ; ; Move ghost ; bh = color ;

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `old` | 5 | 1243.1 | 22.28% | 6.95% |
| `__monolith__` | 4 | 272.52 | 8.77% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `old/pillman1.asm` -> **13.9518%** Exposure
- `old/pillman2.asm` -> **13.8357%** Exposure
- `old/pillman0.asm` -> **6.9458%** Exposure
### Highest State Flux (Mutation/Volatility)
- `old/pillman3.asm` -> **59.6348%** Exposure
- `old/pillman0.asm` -> **57.2932%** Exposure
- `old/pillman2.asm` -> **55.3157%** Exposure
- `old/pillman4.asm` -> **46.5252%** Exposure
- `old/pillman1.asm` -> **44.5146%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `old/pillman1.asm` -> **1** Orphaned Functions | **0** Duplicates
- `old/pillman2.asm` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Makefile`** -> AI Confidence: **98.84%**
2. **`e.bat`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Algorithmic DoS Exposure
- `old/pillman2.asm` -> **4.8408%** Exposure
- `old/pillman3.asm` -> **4.7593%** Exposure
- `old/pillman4.asm` -> **4.6596%** Exposure
- `pillman.asm` -> **4.5831%** Exposure
- `old/pillman0.asm` -> **4.3451%** Exposure

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

### 1. `old/pillman2.asm` (ASSEMBLY) -> Cumulative Risk: **305.67**
- **Archetype:** `file_cluster_8` (Distance: 10.743 IQR)
- **Magnitude:** 260.16 | **LOC:** 346 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (55.3157%), Cognitive Load (22.7254%)
- **Heaviest Functions:** `ms9` (Impact: 30.0), `g1` (Impact: 17.7), `dm1` (Impact: 15.2)

### 2. `old/pillman0.asm` (ASSEMBLY) -> Cumulative Risk: **299.52**
- **Archetype:** `file_cluster_8` (Distance: 10.359 IQR)
- **Magnitude:** 254.78 | **LOC:** 339 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (57.2932%), Cognitive Load (23.5483%)
- **Heaviest Functions:** `in0` (Impact: 26.1), `g9` (Impact: 20.2), `move_ghost` (Impact: 20.2)

### 3. `old/pillman3.asm` (ASSEMBLY) -> Cumulative Risk: **296.33**
- **Archetype:** `file_cluster_8` (Distance: 10.797 IQR)
- **Magnitude:** 237.74 | **LOC:** 332 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (59.6348%), Cognitive Load (22.4219%)
- **Heaviest Functions:** `game_loop` (Impact: 18.0), `close_mouth` (Impact: 17.7), `ms9` (Impact: 17.3)

### 4. `old/pillman1.asm` (ASSEMBLY) -> Cumulative Risk: **291.59**
- **Archetype:** `file_cluster_8` (Distance: 10.189 IQR)
- **Magnitude:** 255.82 | **LOC:** 337 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (44.5146%), Cognitive Load (21.6579%)
- **Heaviest Functions:** `ms9` (Impact: 34.3), `g1` (Impact: 15.4), `dm1` (Impact: 15.2)

### 5. `old/pillman4.asm` (ASSEMBLY) -> Cumulative Risk: **283.09**
- **Archetype:** `file_cluster_8` (Distance: 11.196 IQR)
- **Magnitude:** 234.6 | **LOC:** 336 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (46.5252%), Cognitive Load (21.0557%)
- **Heaviest Functions:** `ms9` (Impact: 17.3), `close_mouth` (Impact: 15.4), `dm1` (Impact: 15.2)

### 6. `pillman.asm` (ASSEMBLY) -> Cumulative Risk: **278.16**
- **Archetype:** `file_cluster_8` (Distance: 11.05 IQR)
- **Magnitude:** 238.16 | **LOC:** 388 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (44.1685%), Cognitive Load (19.7343%)
- **Heaviest Functions:** `ms9` (Impact: 17.3), `close_mouth` (Impact: 15.6), `dm1` (Impact: 15.2)

### 7. `Makefile` (MAKEFILE) -> Cumulative Risk: **224.61**
- **Archetype:** `file_cluster_8` (Distance: 6.764 IQR)
- **Magnitude:** 21.32 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Api Exposure (11.9451%), Cognitive Load (10.3633%)

### 8. `e.bat` (BATCH) -> Cumulative Risk: **45.46**
- **Archetype:** `file_cluster_8` (Distance: 4.447 IQR)
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (20.0%), Documentation (20.0%), Cognitive Load (5.0%), Verification (0.4595%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `old/pillman2.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.743 IQR)
- **Top Global Matches:** file_cluster_8: 10.743, file_cluster_7: 11.367, file_cluster_1: 11.421
- **Magnitude:** 260.16 | **LOC:** 346 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (22.7254%), Tech Debt (13.8357%)
**Top Internal Functions/Classes:**
  * `ms9` (Impact: 30.0 | O(2^N))
  * `g1` (Impact: 17.7 | O(N^2))
  * `dm1` (Impact: 15.2 | O(N^2))
  * `move_sprite` (Impact: 14.4 | O(N^2))
  * `clock_wait` (Impact: 13.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 73`, `args: 148`, `func_start: 52`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman1.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.189 IQR)
- **Top Global Matches:** file_cluster_8: 10.189, file_cluster_7: 10.871, file_cluster_1: 10.902
- **Magnitude:** 255.82 | **LOC:** 337 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.6579%), Tech Debt (13.9518%)
**Top Internal Functions/Classes:**
  * `ms9` (Impact: 34.3 | O(2^N))
  * `g1` (Impact: 15.4 | O(N^2))
  * `dm1` (Impact: 15.2 | O(N^2))
  * `move_sprite` (Impact: 14.3 | O(N^2))
    * *Intent:* ; ; DI = address on screen ; BL = wanted direction ;
  * `clock_wait` (Impact: 13.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 78`, `args: 153`, `func_start: 48`
* *Risk/State:* `state_mutation: 21`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman0.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.359 IQR)
- **Top Global Matches:** file_cluster_8: 10.359, file_cluster_7: 11.021, file_cluster_1: 11.056
- **Magnitude:** 254.78 | **LOC:** 339 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (23.5483%), Tech Debt (6.9458%)
**Top Internal Functions/Classes:**
  * `in0` (Impact: 26.1 | O(2^N) | DB: 1)
  * `g9` (Impact: 20.2 | O(N^2) | DB: 3)
  * `move_ghost` (Impact: 20.2 | O(N^2) | DB: 2)
    * *Intent:* ; ; Move ghost ;
  * `g1` (Impact: 15.4 | O(N^2))
  * `move_sprite` (Impact: 15.2 | O(N^2))
    * *Intent:* ; ; Try to move sprite in desired direction ; ; Input: ; DI = address on screen ; BX = offset of mov...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 80`, `args: 148`, `func_start: 47`
* *Risk/State:* `state_mutation: 24`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* None
* *Defense:* `sync_locks: 7`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pillman.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.05 IQR)
- **Top Global Matches:** file_cluster_8: 11.05, file_cluster_7: 11.646, file_cluster_1: 11.685
- **Magnitude:** 238.16 | **LOC:** 388 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (19.7343%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ms9` (Impact: 17.3 | O(2^N))
  * `close_mouth` (Impact: 15.6 | O(N^2))
  * `dm1` (Impact: 15.2 | O(N^2))
  * `move_sprite` (Impact: 14.7 | O(N^2))
  * `game_loop` (Impact: 13.3 | O(2^N))
    * *Intent:* ; ; Main game loop ;
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 72`, `args: 151`, `func_start: 52`
* *Risk/State:* `state_mutation: 21`, `dead_code: 3`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman3.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.797 IQR)
- **Top Global Matches:** file_cluster_8: 10.797, file_cluster_7: 11.416, file_cluster_1: 11.468
- **Magnitude:** 237.74 | **LOC:** 332 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (22.4219%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `game_loop` (Impact: 18.0 | O(2^N))
  * `close_mouth` (Impact: 17.7 | O(N^2))
  * `ms9` (Impact: 17.3 | O(2^N))
  * `dm1` (Impact: 15.2 | O(N^2))
  * `move_sprite` (Impact: 14.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 73`, `args: 151`, `func_start: 49`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `old/pillman4.asm` (ASSEMBLY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.196 IQR)
- **Top Global Matches:** file_cluster_8: 11.196, file_cluster_7: 11.782, file_cluster_0: 11.824
- **Magnitude:** 234.6 | **LOC:** 336 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.0557%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ms9` (Impact: 17.3 | O(2^N))
  * `close_mouth` (Impact: 15.4 | O(N^2))
  * `dm1` (Impact: 15.2 | O(N^2))
  * `move_sprite` (Impact: 14.5 | O(N^2))
  * `game_loop` (Impact: 13.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 71`, `args: 150`, `func_start: 51`
* *Risk/State:* `state_mutation: 21`, `dead_code: 3`
* *Architecture:* None
* *Defense:* `sync_locks: 6`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.764 IQR)
- **Top Global Matches:** file_cluster_8: 6.764, file_cluster_7: 7.856, file_cluster_1: 8.057
- **Magnitude:** 21.32 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.3633%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 6`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.48 | **LOC:** 74 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 111.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `old/pillman4.asm` (ASSEMBLY) | Magnitude: 234.6 | Delta: **0.586 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 204, args: 150, structural_boundaries: 71, branch: 55
- `pillman.asm` (ASSEMBLY) | Magnitude: 238.16 | Delta: **0.596 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 216, args: 151, structural_boundaries: 72, branch: 55
- `old/pillman3.asm` (ASSEMBLY) | Magnitude: 237.74 | Delta: **0.619 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 208, args: 151, structural_boundaries: 73, branch: 55
- `old/pillman2.asm` (ASSEMBLY) | Magnitude: 260.16 | Delta: **0.624 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 216, args: 148, structural_boundaries: 73, branch: 61
- `old/pillman0.asm` (ASSEMBLY) | Magnitude: 254.78 | Delta: **0.662 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 212, args: 148, structural_boundaries: 80, branch: 65

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Makefile` -> **Severity: 11111.1** (Blast Radius: 111.111 * Doc Risk: 100.0%)
- `e.bat` -> **Severity: 2222.22** (Blast Radius: 111.111 * Doc Risk: 20.0%)
- `old/pillman1.asm` -> **Severity: 1391.043** (Blast Radius: 111.111 * Doc Risk: 12.5194%)
- `old/pillman3.asm` -> **Severity: 1356.299** (Blast Radius: 111.111 * Doc Risk: 12.2067%)
- `old/pillman2.asm` -> **Severity: 1337.499** (Blast Radius: 111.111 * Doc Risk: 12.0375%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
