# ARCHITECTURAL_BRIEF: editables
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/editables` |
| **Timestamp** | `2026-08-03T21:20:30.359756+00:00` |
| **Scan Duration** | `0.12s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 10 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 297 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 4 | 297 | 57.1% |
| PLAINTEXT | 2 | 0 | 28.6% |
| MARKDOWN | 1 | 0 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.241`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 3 | 42.9% |
| file_cluster_16 | 1 | 14.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 42.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.8 | 90.0 | 36.1 | 24.4 | 42.6 |
| Error & Exception Exposure | 1.5 | 69.0 | 32.5 | 29.7 | 69.0 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.6 | 1.2 | 0.0 |
| API Exposure | 5.1 | 8.9 | 7.5 | 7.9 | 8.8 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.9 | 43.5 | 37.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 50.0 | 50.0 | 100.0 |
| Algorithmic DoS Exposure | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 65.9 | 100.0 | 91.5 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `editables-0.5/tests/test_editable.py` (Hits: 15)
- `editables-0.5/tests/test_redirects.py` (Hits: 14)
- `editables-0.5/src/editables/__init__.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **redirector.py** (`editables-0.5/src/editables/redirector.py`) — 2 inbound connections
2. **LICENSE.txt** (`editables-0.5/LICENSE.txt`) — 0 inbound connections
3. **requirements.txt** (`editables-0.5/tests/requirements.txt`) — 0 inbound connections
4. **README.md** (`editables-0.5/README.md`) — 0 inbound connections
5. **__init__.py** (`editables-0.5/src/editables/__init__.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_editable.py** (`editables-0.5/tests/test_editable.py`) — 9 outbound dependencies
2. **test_redirects.py** (`editables-0.5/tests/test_redirects.py`) — 7 outbound dependencies
3. **__init__.py** (`editables-0.5/src/editables/__init__.py`) — 6 outbound dependencies
4. **redirector.py** (`editables-0.5/src/editables/redirector.py`) — 6 outbound dependencies
5. **LICENSE.txt** (`editables-0.5/LICENSE.txt`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `map` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **67.7** | LOC: 12
- `build_project` (@ `editables-0.5/tests/test_editable.py`) -> Impact: **28.3** | LOC: 11
- `build` (@ `editables-0.5/tests/test_redirects.py`) -> Impact: **28.1** | LOC: 8
- `import_state` (@ `editables-0.5/tests/test_editable.py`) -> Impact: **25.3** | LOC: 21
  * *Intent:* # to test in-process: # Put stuff in somedir # sys.path.append("somedir") # site.addsitedir("somedir") # Check stuff is visible
- `save_import_state` (@ `editables-0.5/tests/test_redirects.py`) -> Impact: **21.7** | LOC: 19
- `files` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **17.7** | LOC: 7
- `install` (@ `editables-0.5/src/editables/redirector.py`) -> Impact: **17.6** | LOC: 6
- `pth_file` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **10.7** | LOC: 7
- `__init__` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **9.4** | LOC: 9
- `test_redirects` (@ `editables-0.5/tests/test_redirects.py`) -> Impact: **8.2** | LOC: 25

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `map` (@ `editables-0.5/src/editables/__init__.py`) -> **O(2^N) [Recursive]**
- `build_project` (@ `editables-0.5/tests/test_editable.py`) -> **O(2^N) [Recursive]**
- `project` (@ `editables-0.5/tests/test_editable.py`) -> **O(2^N) [Recursive]**
- `build` (@ `editables-0.5/tests/test_redirects.py`) -> **O(2^N) [Recursive]**
- `files` (@ `editables-0.5/src/editables/__init__.py`) -> **O(N^4)**
- `install` (@ `editables-0.5/src/editables/redirector.py`) -> **O(N^4)**
- `pth_file` (@ `editables-0.5/src/editables/__init__.py`) -> **O(N^3)**
- `__init__` (@ `editables-0.5/src/editables/__init__.py`) -> **O(N^3)**
- `bootstrap_file` (@ `editables-0.5/src/editables/__init__.py`) -> **O(N^3)**
- `dependencies` (@ `editables-0.5/src/editables/__init__.py`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `import_state` (@ `editables-0.5/tests/test_editable.py`) -> DB Complexity: **45**
  * *Intent:* # to test in-process: # Put stuff in somedir # sys.path.append("somedir") # site.addsitedir("somedir") # Check stuff is visible
- `save_import_state` (@ `editables-0.5/tests/test_redirects.py`) -> DB Complexity: **38**
- `install` (@ `editables-0.5/src/editables/redirector.py`) -> DB Complexity: **7**
- `__init__` (@ `editables-0.5/src/editables/__init__.py`) -> DB Complexity: **6**
- `test_double_install` (@ `editables-0.5/tests/test_redirects.py`) -> DB Complexity: **6**
- `add_to_path` (@ `editables-0.5/src/editables/__init__.py`) -> DB Complexity: **4**
- `map` (@ `editables-0.5/src/editables/__init__.py`) -> DB Complexity: **3**
- `add_to_subpackage` (@ `editables-0.5/src/editables/__init__.py`) -> DB Complexity: **3**
- `make_absolute` (@ `editables-0.5/src/editables/__init__.py`) -> DB Complexity: **3**
- `pth_file` (@ `editables-0.5/src/editables/__init__.py`) -> DB Complexity: **2**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `editables-0.5/src/editables` | 2 | 216.66 | 66.28% | 0.0% |
| `editables-0.5/tests` | 3 | 178.78 | 4.01% | 0.0% |
| `editables-0.5` | 2 | 2.28 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest State Flux (Mutation/Volatility)
- `editables-0.5/src/editables/__init__.py` -> **99.9151%** Exposure
- `editables-0.5/src/editables/redirector.py` -> **74.1414%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `editables-0.5/tests/test_redirects.py` -> **6** Orphaned Functions | **0** Duplicates
- `editables-0.5/tests/test_editable.py` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`editables-0.5/tests/test_redirects.py`** -> AI Confidence: **99.16%**
2. **`editables-0.5/tests/test_editable.py`** -> AI Confidence: **99.15%**
3. **`editables-0.5/src/editables/redirector.py`** -> AI Confidence: **98.96%**
4. **`editables-0.5/src/editables/__init__.py`** -> AI Confidence: **98.93%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `editables-0.5/src/editables/__init__.py` -> **100.0%** Exposure
- `editables-0.5/tests/test_editable.py` -> **100.0%** Exposure
- `editables-0.5/tests/test_redirects.py` -> **99.9996%** Exposure
- `editables-0.5/src/editables/redirector.py` -> **65.8522%** Exposure
### Algorithmic DoS Exposure
- `editables-0.5/src/editables/__init__.py` -> **100.0%** Exposure
- `editables-0.5/src/editables/redirector.py` -> **100.0%** Exposure
- `editables-0.5/tests/test_editable.py` -> **100.0%** Exposure
- `editables-0.5/tests/test_redirects.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `editables-0.5/src/editables/__init__.py` (PYTHON) -> Cumulative Risk: **750.24**
- **Archetype:** `file_cluster_16` (Distance: 10.793 IQR)
- **Magnitude:** 178.74 | **LOC:** 103 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `map` (Impact: 67.7), `files` (Impact: 17.7), `pth_file` (Impact: 10.7)

### 2. `editables-0.5/src/editables/redirector.py` (PYTHON) -> Cumulative Risk: **649.06**
- **Archetype:** `file_cluster_13` (Distance: 10.261 IQR)
- **Magnitude:** 37.92 | **LOC:** 48 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Cognitive Load (89.975%)
- **Heaviest Functions:** `install` (Impact: 17.6), `map_module` (Impact: 3.1), `invalidate_caches` (Impact: 2.9)

### 3. `editables-0.5/tests/test_redirects.py` (PYTHON) -> Cumulative Risk: **364.45**
- **Archetype:** `file_cluster_13` (Distance: 10.653 IQR)
- **Magnitude:** 82.22 | **LOC:** 92 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9996%), Stability (50.0%)
- **Heaviest Functions:** `build` (Impact: 28.1), `save_import_state` (Impact: 21.7), `test_redirects` (Impact: 8.2)

### 4. `editables-0.5/tests/test_editable.py` (PYTHON) -> Cumulative Risk: **362.82**
- **Archetype:** `file_cluster_13` (Distance: 10.264 IQR)
- **Magnitude:** 95.56 | **LOC:** 163 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `build_project` (Impact: 28.3), `import_state` (Impact: 25.3), `project` (Impact: 7.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `editables-0.5/src/editables/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.793 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.893 IQR)
- **Top Global Matches:** file_cluster_16: 10.793, file_cluster_13: 10.904, file_cluster_8: 11.331
- **Magnitude:** 178.74 | **LOC:** 103 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (42.5875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `map` (Impact: 67.7 | O(2^N) | DB: 3)
  * `files` (Impact: 17.7 | O(N^4))
  * `pth_file` (Impact: 10.7 | O(N^3) | DB: 2)
  * `__init__` (Impact: 9.4 | O(N^3) | DB: 6)
  * `bootstrap_file` (Impact: 7.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 33`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 18`
* *Architecture:* `io: 6`, `api: 18`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` re, typing, editables.redirector, os, name, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/tests/test_editable.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.264 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.877 IQR)
- **Top Global Matches:** file_cluster_13: 10.264, file_cluster_0: 10.498, file_cluster_8: 10.576
- **Magnitude:** 95.56 | **LOC:** 163 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (6.2323%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_project` (Impact: 28.3 | O(2^N))
  * `import_state` (Impact: 25.3 | O(N^3) | DB: 45)
    * *Intent:* # to test in-process: # Put stuff in somedir # sys.path.append("somedir") # site.addsitedir("somedir...
  * `project` (Impact: 7.5 | O(2^N))
  * `test_nonexistent_module` (Impact: 5.4 | O(N^2))
  * `test_not_toplevel` (Impact: 5.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 30`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 5`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 15`, `api: 11`, `import: 10`
* *Defense:* `safety: 11`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, foo, editables, pytest, contextlib, site, a.b.foo, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/tests/test_redirects.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.653 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.939 IQR)
- **Top Global Matches:** file_cluster_13: 10.653, file_cluster_0: 10.966, file_cluster_8: 11.052
- **Magnitude:** 82.22 | **LOC:** 92 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (5.8029%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 28.1 | O(2^N))
  * `save_import_state` (Impact: 21.7 | O(N^3) | DB: 38)
  * `test_redirects` (Impact: 8.2 | O(N^3))
  * `test_double_install` (Impact: 5.5 | O(N^2) | DB: 6)
  * `test_cache_invalidation` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `io: 14`, `api: 8`, `import: 7`
* *Defense:* `safety: 10`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pkg.sub, pkg, sys, editables.redirector, importlib, contextlib, mod
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/src/editables/redirector.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.261 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.319 IQR)
- **Top Global Matches:** file_cluster_13: 10.261, file_cluster_0: 10.377, file_cluster_16: 10.596
- **Magnitude:** 37.92 | **LOC:** 48 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (89.975%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `install` (Impact: 17.6 | O(N^4) | DB: 7)
  * `map_module` (Impact: 3.1 | O(N^2))
  * `invalidate_caches` (Impact: 2.9 | O(N^2))
    * *Intent:* # importlib.invalidate_caches calls finders' invalidate_caches methods, # and since we install this ...
  * `find_spec` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 9`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 310.345
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.333333
  * `Imports (Out-Degree: 0):` importlib.abc, importlib.util, sys, typing, types, importlib.machinery
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `editables-0.5/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.28 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/tests/requirements.txt` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `editables-0.5/src/editables/redirector.py` (PYTHON) | Magnitude: 37.92 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 19, api: 9, generics: 8
- `editables-0.5/tests/test_editable.py` (PYTHON) | Magnitude: 95.56 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 30, test: 21, branch: 19
- `editables-0.5/tests/test_redirects.py` (PYTHON) | Magnitude: 82.22 | Delta: **0.313 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 25, io: 14, test: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `editables-0.5/src/editables/__init__.py` (PYTHON) | Magnitude: 178.74 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 33, generics: 23, api: 18

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `editables-0.5/src/editables/redirector.py` -> **Severity: 19.259** (Embedded: 0.3333 * Error Risk: 57.7778%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `editables-0.5/src/editables/redirector.py` -> **Severity: 31034.5** (Blast Radius: 310.345 * Doc Risk: 100.0%)
- `editables-0.5/src/editables/__init__.py` -> **Severity: 11494.2** (Blast Radius: 114.942 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
