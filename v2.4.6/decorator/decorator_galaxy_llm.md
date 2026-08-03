# ARCHITECTURAL_BRIEF: decorator
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/decorator` |
| **Timestamp** | `2026-08-03T21:20:11.348350+00:00` |
| **Scan Duration** | `0.17s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3 malicious artifacts.

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
| Total Artifacts | 11 |
| Analyzed Artifacts (Scanned) | 6 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 602 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 54.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 2 | 0 | 33.3% |
| PYTHON | 2 | 589 | 33.3% |
| MARKDOWN | 1 | 0 | 16.7% |
| SHELL | 1 | 13 | 16.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.757`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1 | 16.7% |
| file_cluster_13 | 1 | 16.7% |
| file_cluster_0 | 1 | 16.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 50.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 44.6 | 18.7 | 6.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 46.6 | 17.6 | 6.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 37.9 | 13.8 | 100.0 |
| Testing Exposure | 0.0 | 80.0 | 27.3 | 2.0 | 2.0 |
| API Exposure | 0.0 | 8.5 | 3.6 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 95.6 | 61.2 | 88.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.8 | 4.9 | 5.0 | 0.0 |
| Specification Exposure | 86.7 | 100.0 | 95.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 92.7 | 34.4 | 10.3 | 10.3 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 66.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 66.7 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `decorator-5.2.1/src/decorator.py` (Hits: 3)
- `decorator-5.2.1/CHANGES.md` (Hits: 0)
- `decorator-5.2.1/LICENSE.txt` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **decorator.py** (`decorator-5.2.1/src/decorator.py`) — 1 inbound connections
2. **CHANGES.md** (`decorator-5.2.1/CHANGES.md`) — 0 inbound connections
3. **LICENSE.txt** (`decorator-5.2.1/LICENSE.txt`) — 0 inbound connections
4. **MANIFEST.in** (`decorator-5.2.1/MANIFEST.in`) — 0 inbound connections
5. **performance.sh** (`decorator-5.2.1/performance.sh`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **documentation.py** (`decorator-5.2.1/tests/documentation.py`) — 14 outbound dependencies
2. **decorator.py** (`decorator-5.2.1/src/decorator.py`) — 7 outbound dependencies
3. **CHANGES.md** (`decorator-5.2.1/CHANGES.md`) — 0 outbound dependencies
4. **LICENSE.txt** (`decorator-5.2.1/LICENSE.txt`) — 0 outbound dependencies
5. **MANIFEST.in** (`decorator-5.2.1/MANIFEST.in`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `make` (@ `decorator-5.2.1/src/decorator.py`) -> Impact: **713.5** | LOC: 209
- `_trace` (@ `decorator-5.2.1/tests/documentation.py`) -> Impact: **382.1** | LOC: 361
- `check` (@ `decorator-5.2.1/src/decorator.py`) -> Impact: **298.5** | LOC: 90
  * *Intent:* # ############################ dispatch_on ############################ # """ Append ``a`` to the list of the virtual ancestors, unless it is already ...
- `__init__` (@ `decorator-5.2.1/src/decorator.py`) -> Impact: **191.6** | LOC: 51
- `update` (@ `decorator-5.2.1/src/decorator.py`) -> Impact: **32.9** | LOC: 17
  * *Intent:* # check existence required attributes assert hasattr(self, 'name') if not hasattr(self, 'signature'): raise TypeError('You are decorating a non functi...
- `to_method` (@ `decorator-5.2.1/tests/documentation.py`) -> Impact: **3.2** | LOC: 13
- `chattywrapper` (@ `decorator-5.2.1/tests/documentation.py`) -> Impact: **2.9** | LOC: 6
  * *Intent:* ## Mimicking the behavior of functools.wrap
- `__init__` (@ `decorator-5.2.1/tests/documentation.py`) -> Impact: **2.7** | LOC: 2
- `chatty` (@ `decorator-5.2.1/tests/documentation.py`) -> Impact: **2.1** | LOC: 3
- `bar` (@ `decorator-5.2.1/tests/documentation.py`) -> Impact: **2.1** | LOC: 2

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `make` (@ `decorator-5.2.1/src/decorator.py`) -> **O(2^N) [Recursive]**
- `check` (@ `decorator-5.2.1/src/decorator.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # ############################ dispatch_on ############################ # """ Append ``a`` to the list of the virtual ancestors, unless it is already ...
- `_trace` (@ `decorator-5.2.1/tests/documentation.py`) -> **O(2^N) [Recursive]**
- `update` (@ `decorator-5.2.1/src/decorator.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # check existence required attributes assert hasattr(self, 'name') if not hasattr(self, 'signature'): raise TypeError('You are decorating a non functi...
- `__init__` (@ `decorator-5.2.1/src/decorator.py`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `decorator-5.2.1/src/decorator.py`) -> DB Complexity: **23**
- `make` (@ `decorator-5.2.1/src/decorator.py`) -> DB Complexity: **10**
- `_trace` (@ `decorator-5.2.1/tests/documentation.py`) -> DB Complexity: **8**
- `update` (@ `decorator-5.2.1/src/decorator.py`) -> DB Complexity: **4**
  * *Intent:* # check existence required attributes assert hasattr(self, 'name') if not hasattr(self, 'signature'): raise TypeError('You are decorating a non functi...
- `check` (@ `decorator-5.2.1/src/decorator.py`) -> DB Complexity: **2**
  * *Intent:* # ############################ dispatch_on ############################ # """ Append ``a`` to the list of the virtual ancestors, unless it is already ...
- `to_method` (@ `decorator-5.2.1/tests/documentation.py`) -> DB Complexity: **1**
- `__init__` (@ `decorator-5.2.1/tests/documentation.py`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `decorator-5.2.1/src` | 1 | 1359.52 | 44.62% | 13.76% |
| `decorator-5.2.1/tests` | 1 | 501.06 | 6.53% | 0.0% |
| `decorator-5.2.1` | 4 | 12.04 | 1.25% | 25.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `decorator-5.2.1/performance.sh` -> **100.0%** Exposure
- `decorator-5.2.1/src/decorator.py` -> **13.7579%** Exposure
### Highest State Flux (Mutation/Volatility)
- `decorator-5.2.1/src/decorator.py` -> **99.9918%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `decorator-5.2.1/tests/documentation.py` -> **6** Orphaned Functions | **0** Duplicates
- `decorator-5.2.1/performance.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`decorator-5.2.1/src/decorator.py`** -> AI Confidence: **99.31%**
2. **`decorator-5.2.1/tests/documentation.py`** -> AI Confidence: **99.08%**
3. **`decorator-5.2.1/performance.sh`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `decorator-5.2.1/src/decorator.py` -> **100.0%** Exposure
- `decorator-5.2.1/tests/documentation.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `decorator-5.2.1/src/decorator.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `decorator-5.2.1/src/decorator.py` -> **100.0%** Exposure
- `decorator-5.2.1/tests/documentation.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `21` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `decorator-5.2.1/src/decorator.py` (PYTHON) -> Cumulative Risk: **935.57**
- **Archetype:** `file_cluster_13` (Distance: 13.493 IQR)
- **Magnitude:** 1359.52 | **LOC:** 460 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `make` (Impact: 713.5), `check` (Impact: 298.5), `__init__` (Impact: 191.6)

### 2. `decorator-5.2.1/tests/documentation.py` (PYTHON) -> Cumulative Risk: **464.21**
- **Archetype:** `file_cluster_0` (Distance: 11.007 IQR)
- **Magnitude:** 501.06 | **LOC:** 1891 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (88.0152%)
- **Heaviest Functions:** `_trace` (Impact: 382.1), `to_method` (Impact: 3.2), `chattywrapper` (Impact: 2.9)

### 3. `decorator-5.2.1/performance.sh` (SHELL) -> Cumulative Risk: **254.03**
- **Archetype:** `file_cluster_8` (Distance: 5.071 IQR)
- **Magnitude:** 1.86 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (86.6667%), Stability (50.0%), Documentation (10.3309%)
- **Heaviest Functions:** `__global_context__` (Impact: 1.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `decorator-5.2.1/src/decorator.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.493 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.997 IQR)
- **Top Global Matches:** file_cluster_13: 13.493, file_cluster_17: 13.599, file_cluster_11: 13.711
- **Magnitude:** 1359.52 | **LOC:** 460 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (44.6238%), Tech Debt (13.7579%)
**Top Internal Functions/Classes:**
  * `make` (Impact: 713.5 | O(2^N) | DB: 10)
  * `check` (Impact: 298.5 | O(2^N) | DB: 2)
    * *Intent:* # ############################ dispatch_on ############################ # """ Append ``a`` to the li...
  * `__init__` (Impact: 191.6 | O(N^6) | DB: 23)
  * `update` (Impact: 32.9 | O(2^N) | DB: 4)
    * *Intent:* # check existence required attributes assert hasattr(self, 'name') if not hasattr(self, 'signature')...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 84`, `args: 28`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 88`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 25`, `concurrency: 4`, `import: 8`
* *Defense:* `safety: 35`, `doc: 34`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 270.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.2
  * `Imports (Out-Degree: 0):` itertools, contextlib, sys, re, operator, functools, inspect
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `decorator-5.2.1/tests/documentation.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.007 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.053 IQR)
- **Top Global Matches:** file_cluster_0: 11.007, file_cluster_13: 11.277, file_cluster_8: 11.546
- **Magnitude:** 501.06 | **LOC:** 1891 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (6.5268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_trace` (Impact: 382.1 | O(2^N) | DB: 8)
  * `to_method` (Impact: 3.2 | O(N^2) | DB: 1)
  * `chattywrapper` (Impact: 2.9 | O(N^2))
    * *Intent:* ## Mimicking the behavior of functools.wrap
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
  * `chatty` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 157`, `args: 65`, `func_start: 65`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 68`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 9`, `doc: 30`, `test: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 145.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` itertools, a, time, contextlib, doctest, collections.abc, logging, asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decorator-5.2.1/CHANGES.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 8.18 | **LOC:** 409 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 145.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decorator-5.2.1/performance.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.071 IQR)
- **Top Global Matches:** file_cluster_8: 5.071, file_cluster_7: 6.679, file_cluster_1: 6.743
- **Magnitude:** 1.86 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 1.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 145.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decorator-5.2.1/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 145.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decorator-5.2.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 145.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `decorator-5.2.1/tests/documentation.py` (PYTHON) | Magnitude: 501.06 | Delta: **0.27 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 157, api: 68, args: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `decorator-5.2.1/src/decorator.py` (PYTHON) | Magnitude: 1359.52 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 279, state_mutation: 88, structural_boundaries: 84, encapsulation: 83

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `decorator-5.2.1/src/decorator.py` -> **Severity: 9.322** (Embedded: 0.2 * Error Risk: 46.6113%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `decorator-5.2.1/src/decorator.py` -> **Severity: 25049.217** (Blast Radius: 270.073 * Doc Risk: 92.7498%)
- `decorator-5.2.1/performance.sh` -> **Severity: 1508.156** (Blast Radius: 145.985 * Doc Risk: 10.3309%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
