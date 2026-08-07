# ARCHITECTURAL_BRIEF: watchfiles
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/watchfiles` |
| **Timestamp** | `2026-08-07T05:27:22.648930+00:00` |
| **Scan Duration** | `0.17s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Total Artifacts | 42 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 1826 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 73.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2388 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1953 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0769 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 15 | 1763 | 48.4% |
| PLAINTEXT | 13 | 0 | 41.9% |
| MARKDOWN | 2 | 0 | 6.5% |
| MAKEFILE | 1 | 63 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.835`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 9 | 29.0% |
| file_cluster_13 | 3 | 9.7% |
| file_cluster_4 | 2 | 6.5% |
| file_cluster_16 | 2 | 6.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 48.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.6 | 33.4 | 10.8 | 6.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 68.8 | 23.5 | 7.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.4 | 0.9 | 0.2 | 0.0 |
| API Exposure | 0.0 | 13.5 | 5.1 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 17.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.9 | 8.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.3 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 84.2 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.3 | 19.1 | 10.3 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `watchfiles-1.1.1/tests/test_cli.py` (Hits: 56)
- `watchfiles-1.1.1/tests/test_run_process.py` (Hits: 28)
- `watchfiles-1.1.1/watchfiles/cli.py` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **main.py** (`watchfiles-1.1.1/watchfiles/main.py`) — 7 inbound connections
2. **filters.py** (`watchfiles-1.1.1/watchfiles/filters.py`) — 4 inbound connections
3. **_rust_notify.pyi** (`watchfiles-1.1.1/watchfiles/_rust_notify.pyi`) — 3 inbound connections
4. **run.py** (`watchfiles-1.1.1/watchfiles/run.py`) — 3 inbound connections
5. **cli.py** (`watchfiles-1.1.1/watchfiles/cli.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **run.py** (`watchfiles-1.1.1/watchfiles/run.py`) — 23 outbound dependencies
2. **main.py** (`watchfiles-1.1.1/watchfiles/main.py`) — 14 outbound dependencies
3. **cli.py** (`watchfiles-1.1.1/watchfiles/cli.py`) — 13 outbound dependencies
4. **test_run_process.py** (`watchfiles-1.1.1/tests/test_run_process.py`) — 12 outbound dependencies
5. **test_watch.py** (`watchfiles-1.1.1/tests/test_watch.py`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `cli` (@ `watchfiles-1.1.1/watchfiles/cli.py`) -> Impact: **83.4** | LOC: 188
  * *Intent:* """ Watch one or more directories and execute either a shell command or a python function on file changes. Example of watching the current directory a...
- `__call__` (@ `watchfiles-1.1.1/watchfiles/filters.py`) -> Impact: **16.7** | LOC: 14
  * *Intent:* """ def __init__(self) -> None: self._ignore_dirs = set(self.ignore_dirs) self._ignore_entity_regexes = tuple(re.compile(r) for r in self.ignore_entit...
- `stop` (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **13.2** | LOC: 23
- `set_tty` (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **10.6** | LOC: 12
- `test_awatch_unexpected_signal` (@ `watchfiles-1.1.1/tests/test_watch.py`) -> Impact: **9.4** | LOC: 9
- `test_does_not_exist_message` (@ `watchfiles-1.1.1/tests/test_rust_notify.py`) -> Impact: **8.2** | LOC: 4
- `test_does_not_exist_polling` (@ `watchfiles-1.1.1/tests/test_rust_notify.py`) -> Impact: **8.2** | LOC: 4
- `detect_target_type` (@ `watchfiles-1.1.1/watchfiles/run.py`) -> Impact: **7.6** | LOC: 11
- `test_awatch_interrupt_warning` (@ `watchfiles-1.1.1/tests/test_watch.py`) -> Impact: **7.4** | LOC: 9
- `test_move_internal` (@ `watchfiles-1.1.1/tests/test_rust_notify.py`) -> Impact: **7.1** | LOC: 22
  * *Intent:* # can't use tmp_path as it causes problems on Windows (different drive), and macOS (delayed events) src = test_dir / 'dir_a' dst = test_dir / 'dir_b' ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `watchfiles-1.1.1/tests` | 7 | 625.96 | 11.15% | 0.0% |
| `watchfiles-1.1.1/watchfiles` | 8 | 339.22 | 11.3% | 0.0% |
| `watchfiles-1.1.1` | 2 | 66.44 | 1.8% | 0.0% |
| `watchfiles-1.1.1/tests/test_files/dir_a` | 8 | 8.0 | 0.0% | 0.0% |
| `watchfiles-1.1.1/tests/test_files` | 6 | 6.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest State Flux (Mutation/Volatility)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **99.9269%** Exposure
- `watchfiles-1.1.1/watchfiles/run.py` -> **16.9335%** Exposure
- `watchfiles-1.1.1/watchfiles/cli.py` -> **16.2698%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `watchfiles-1.1.1/tests/test_rust_notify.py` -> **28** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_run_process.py` -> **21** Orphaned Functions | **4** Duplicates
- `watchfiles-1.1.1/tests/test_watch.py` -> **21** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_cli.py` -> **17** Orphaned Functions | **0** Duplicates
- `watchfiles-1.1.1/tests/test_filters.py` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`watchfiles-1.1.1/watchfiles/main.py`** -> AI Confidence: **99.31%**
2. **`watchfiles-1.1.1/watchfiles/cli.py`** -> AI Confidence: **99.24%**
3. **`watchfiles-1.1.1/tests/test_rust_notify.py`** -> AI Confidence: **99.18%**
4. **`watchfiles-1.1.1/watchfiles/run.py`** -> AI Confidence: **99.16%**
5. **`watchfiles-1.1.1/tests/test_cli.py`** -> AI Confidence: **99.08%**
6. **`watchfiles-1.1.1/tests/test_filters.py`** -> AI Confidence: **99.08%**
7. **`watchfiles-1.1.1/tests/test_run_process.py`** -> AI Confidence: **99.08%**
8. **`watchfiles-1.1.1/tests/test_watch.py`** -> AI Confidence: **99.07%**
9. **`watchfiles-1.1.1/Makefile`** -> AI Confidence: **99.06%**
10. **`watchfiles-1.1.1/watchfiles/filters.py`** -> AI Confidence: **98.93%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `100` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `watchfiles-1.1.1/watchfiles/run.py` (PYTHON) -> Cumulative Risk: **372.06**
- **Archetype:** `file_cluster_13` (Distance: 10.739 IQR)
- **Magnitude:** 114.74 | **LOC:** 439 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (78.1229%), Safety Score (68.7931%), Stability (50.0%)
- **Heaviest Functions:** `stop` (Impact: 13.2), `set_tty` (Impact: 10.6), `detect_target_type` (Impact: 7.6)

### 2. `watchfiles-1.1.1/watchfiles/filters.py` (PYTHON) -> Cumulative Risk: **365.77**
- **Archetype:** `file_cluster_13` (Distance: 11.787 IQR)
- **Magnitude:** 49.6 | **LOC:** 150 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9269%), Safety Score (67.0092%), Stability (50.0%)
- **Heaviest Functions:** `__call__` (Impact: 16.7), `__init__` (Impact: 3.7), `__repr__` (Impact: 3.6)

### 3. `watchfiles-1.1.1/tests/test_watch.py` (PYTHON) -> Cumulative Risk: **295.62**
- **Archetype:** `file_cluster_4` (Distance: 12.638 IQR)
- **Magnitude:** 161.56 | **LOC:** 241 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9838%), Stability (50.0%), Cognitive Load (30.8424%)
- **Heaviest Functions:** `test_awatch_unexpected_signal` (Impact: 9.4), `test_awatch_interrupt_warning` (Impact: 7.4), `test_awatch_interrupt_raise` (Impact: 6.8)

### 4. `watchfiles-1.1.1/tests/test_run_process.py` (PYTHON) -> Cumulative Risk: **284.95**
- **Archetype:** `file_cluster_4` (Distance: 12.323 IQR)
- **Magnitude:** 150.2 | **LOC:** 280 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.7892%), Stability (50.0%), Cognitive Load (24.3051%)
- **Heaviest Functions:** `test_alive_terminates` (Impact: 6.7), `test_function_string_not_win` (Impact: 6.7), `test_command_with_args` (Impact: 6.7)

### 5. `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` (PYTHON) -> Cumulative Risk: **272.31**
- **Archetype:** `file_cluster_16` (Distance: 10.115 IQR)
- **Magnitude:** 12.22 | **LOC:** 112 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (68.4615%), Stability (50.0%), Documentation (44.412%)
- **Heaviest Functions:** `__init__` (Impact: 1.4), `watch` (Impact: 1.3)

### 6. `watchfiles-1.1.1/Makefile` (MAKEFILE) -> Cumulative Risk: **267.66**
- **Archetype:** `file_cluster_8` (Distance: 8.092 IQR)
- **Magnitude:** 64.26 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.2846%), Stability (50.0%), Api Exposure (13.4774%)

### 7. `watchfiles-1.1.1/watchfiles/cli.py` (PYTHON) -> Cumulative Risk: **257.16**
- **Archetype:** `file_cluster_8` (Distance: 9.187 IQR)
- **Magnitude:** 100.44 | **LOC:** 225 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (50.6232%), Stability (50.0%), Documentation (22.7172%)
- **Heaviest Functions:** `cli` (Impact: 83.4), `resolve_path` (Impact: 6.3)

### 8. `watchfiles-1.1.1/watchfiles/main.py` (PYTHON) -> Cumulative Risk: **235.5**
- **Archetype:** `file_cluster_16` (Distance: 9.671 IQR)
- **Magnitude:** 21.78 | **LOC:** 374 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (48.5758%), Documentation (11.9203%)
- **Heaviest Functions:** `watch` (Impact: 2.4), `raw_str` (Impact: 1.8)

### 9. `watchfiles-1.1.1/watchfiles/__init__.py` (PYTHON) -> Cumulative Risk: **216.99**
- **Archetype:** `file_cluster_8` (Distance: 5.914 IQR)
- **Magnitude:** 16.32 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (55.5328%), Stability (50.0%), Cognitive Load (7.5858%)

### 10. `watchfiles-1.1.1/tests/test_force_polling.py` (PYTHON) -> Cumulative Risk: **198.9**
- **Archetype:** `file_cluster_8` (Distance: 8.549 IQR)
- **Magnitude:** 36.4 | **LOC:** 105 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (40.0832%), Api Exposure (4.459%)
- **Heaviest Functions:** `test_default_force_polling_wsl` (Impact: 5.6), `test_default_force_polling` (Impact: 5.2), `test_watch_polling_env` (Impact: 3.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `watchfiles-1.1.1/tests/test_watch.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.638 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.294 IQR)
- **Top Global Matches:** file_cluster_4: 12.638, file_cluster_13: 12.802, file_cluster_0: 12.91
- **Magnitude:** 161.56 | **LOC:** 241 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.8424%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_awatch_unexpected_signal` (Impact: 9.4)
  * `test_awatch_interrupt_warning` (Impact: 7.4)
  * `test_awatch_interrupt_raise` (Impact: 6.8)
  * `test_awatch_yield_on_timeout` (Impact: 4.9)
  * `test_watch_yield_on_timeout` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 87`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 16`, `orphaned_logic: 21`
* *Architecture:* `io: 3`, `api: 22`, `concurrency: 30`, `import: 12`
* *Defense:* `safety: 37`, `test: 61`, `sync_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` conftest, sys, watchfiles.main, time, contextlib, watchfiles, pathlib, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_rust_notify.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.111 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.386 IQR)
- **Top Global Matches:** file_cluster_8: 11.111, file_cluster_0: 11.214, file_cluster_13: 11.374
- **Magnitude:** 153.0 | **LOC:** 343 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_does_not_exist_message` (Impact: 8.2)
  * `test_does_not_exist_polling` (Impact: 8.2)
  * `test_move_internal` (Impact: 7.1)
    * *Intent:* # can't use tmp_path as it causes problems on Windows (different drive), and macOS (delayed events) ...
  * `test_close` (Impact: 6.5)
  * `test_wrong_type_event_is_set` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 75`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 28`
* *Architecture:* `io: 5`, `api: 30`, `import: 9`
* *Defense:* `safety: 28`, `test: 67`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` re, sys, os, watchfiles.main, .conftest, watchfiles._rust_notify, typing, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_run_process.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.323 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.023 IQR)
- **Top Global Matches:** file_cluster_4: 12.323, file_cluster_0: 12.335, file_cluster_13: 12.415
- **Magnitude:** 150.2 | **LOC:** 280 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.3051%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_alive_terminates` (Impact: 6.7)
  * `test_function_string_not_win` (Impact: 6.7)
  * `test_command_with_args` (Impact: 6.7)
  * `test_import_string` (Impact: 5.4)
  * `poll` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 119`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 7`, `duplicate_logic: 4`, `orphaned_logic: 21`
* *Architecture:* `io: 28`, `api: 30`, `concurrency: 23`, `import: 12`
* *Defense:* `safety: 54`, `test: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` multiprocessing.context, conftest, sys, watchfiles.main, os, dirty_equals, watchfiles.run, watchfiles...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/run.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.739 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.239 IQR)
- **Top Global Matches:** file_cluster_13: 10.739, file_cluster_16: 10.821, file_cluster_0: 11.187
- **Magnitude:** 114.74 | **LOC:** 439 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.9579%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stop` (Impact: 13.2)
  * `set_tty` (Impact: 10.6)
  * `detect_target_type` (Impact: 7.6)
  * `import_string` (Impact: 6.7)
  * `is_alive` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 80`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 4`
* *Architecture:* `io: 9`, `api: 19`, `concurrency: 10`, `import: 21`
* *Defense:* `safety: 22`, `doc: 12`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.432
  * `Choke Point (Betweenness):` 0.002299 | `Ripple Effect (Closeness):` 0.119048
  * `Imports (Out-Degree: 2):` multiprocessing.context, logging, shlex, signal, inspect, subprocess, multiprocessing, anyio...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/cli.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.187 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.587 IQR)
- **Top Global Matches:** file_cluster_8: 9.187, file_cluster_13: 9.217, file_cluster_17: 9.564
- **Magnitude:** 100.44 | **LOC:** 225 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.7348%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cli` (Impact: 83.4)
    * *Intent:* """ Watch one or more directories and execute either a shell command or a python function on file ch...
  * `resolve_path` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 53`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`
* *Architecture:* `io: 11`, `api: 4`, `import: 13`
* *Defense:* `safety: 9`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 45.438
  * `Choke Point (Betweenness):` 0.011494 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 3):` , .run, logging, sys, shlex, os, .filters, .version...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.691 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.685 IQR)
- **Top Global Matches:** file_cluster_8: 8.691, file_cluster_13: 9.518, file_cluster_7: 9.594
- **Magnitude:** 74.16 | **LOC:** 332 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.6028%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_invalid_import2` (Impact: 4.5)
  * `test_invalid_import1` (Impact: 4.4)
  * `test_invalid_path` (Impact: 3.9)
  * `test_args` (Impact: 3.3)
  * `test_ignore_paths` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 48`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 17`
* *Architecture:* `io: 56`, `api: 18`, `import: 7`
* *Defense:* `safety: 15`, `test: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, os, dirty_equals, watchfiles.cli, watchfiles, pytest, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.092 IQR)
- **Top Global Matches:** file_cluster_8: 8.092, file_cluster_7: 8.694, file_cluster_1: 8.933
- **Magnitude:** 64.26 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.6027%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `func_start: 14`
* *Risk/State:* None
* *Architecture:* `api: 18`
* *Defense:* `doc: 3`, `test: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/filters.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.787 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.394 IQR)
- **Top Global Matches:** file_cluster_13: 11.787, file_cluster_16: 11.842, file_cluster_8: 12.124
- **Magnitude:** 49.6 | **LOC:** 150 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4094%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 16.7)
    * *Intent:* """ def __init__(self) -> None: self._ignore_dirs = set(self.ignore_dirs) self._ignore_entity_regexe...
  * `__init__` (Impact: 3.7)
  * `__repr__` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `io: 3`, `api: 5`, `import: 6`
* *Defense:* `safety: 1`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 132.564
  * `Choke Point (Betweenness):` 0.001724 | `Ripple Effect (Closeness):` 0.208333
  * `Imports (Out-Degree: 1):` logging, re, os, .main, typing, pathlib
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/tests/test_filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.55 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.746 IQR)
- **Top Global Matches:** file_cluster_13: 11.55, file_cluster_8: 11.633, file_cluster_0: 11.79
- **Magnitude:** 40.12 | **LOC:** 101 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0658%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_web_filter` (Impact: 4.6)
    * *Intent:* # test case from docs class WebFilter(DefaultFilter): allowed_extensions = '.html', '.css', '.js' de...
  * `__call__` (Impact: 4.1)
  * `test_simple_function` (Impact: 2.4)
  * `test_customising_filters` (Impact: 2.3)
  * `test_ignore_file` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 44`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 11`, `import: 8`
* *Defense:* `safety: 16`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` conftest, re, sys, dirty_equals, watchfiles, typing, pytest, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_force_polling.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.549 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.552 IQR)
- **Top Global Matches:** file_cluster_8: 8.549, file_cluster_13: 8.852, file_cluster_0: 9.065
- **Magnitude:** 36.4 | **LOC:** 105 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_default_force_polling_wsl` (Impact: 5.6)
  * `test_default_force_polling` (Impact: 5.2)
  * `test_watch_polling_env` (Impact: 3.9)
  * `test_watch_polling_env_with_custom_delay` (Impact: 3.9)
  * `test_watch_polling_not_env` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 32`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `orphaned_logic: 7`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 3`, `test: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` watchfiles.main, __future__, watchfiles, .conftest, typing, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/main.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.671 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.605 IQR)
- **Top Global Matches:** file_cluster_16: 9.671, file_cluster_13: 9.782, file_cluster_8: 10.11
- **Magnitude:** 21.78 | **LOC:** 374 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5075%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `watch` (Impact: 2.4)
  * `raw_str` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 56`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 8`, `concurrency: 6`, `import: 14`
* *Defense:* `safety: 2`, `doc: 22`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 193.188
  * `Choke Point (Betweenness):` 0.010345 | `Ripple Effect (Closeness):` 0.222222
  * `Imports (Out-Degree: 2):` asyncio, logging, sys, warnings, os, trio, ._rust_notify, enum...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/__init__.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.914 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.781 IQR)
- **Top Global Matches:** file_cluster_8: 5.914, file_cluster_13: 6.329, file_cluster_7: 7.161
- **Magnitude:** 16.32 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5858%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .filters, .version, .run, .main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/watchfiles/version.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.26 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.535 IQR)
- **Top Global Matches:** file_cluster_8: 6.26, file_cluster_13: 6.345, file_cluster_7: 7.333
- **Magnitude:** 12.56 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.28
  * `Choke Point (Betweenness):` 0.004023 | `Ripple Effect (Closeness):` 0.088889
  * `Imports (Out-Degree: 1):` ._rust_notify
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.115 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.392 IQR)
- **Top Global Matches:** file_cluster_16: 10.115, file_cluster_8: 10.645, file_cluster_7: 10.74
- **Magnitude:** 12.22 | **LOC:** 112 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.1714%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1.4)
  * `watch` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 134.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.208696
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `watchfiles-1.1.1/watchfiles/__main__.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.246 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.088 IQR)
- **Top Global Matches:** file_cluster_8: 5.246, file_cluster_13: 5.657, file_cluster_7: 6.759
- **Magnitude:** 11.56 | **LOC:** 5 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .cli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.18 | **LOC:** 109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/a.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/a_non_recursive.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/b.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/c.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/c_non_recursive.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/dir_a/a.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `watchfiles-1.1.1/tests/test_files/dir_a/a_non_recursive.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `watchfiles-1.1.1/watchfiles/filters.py` (PYTHON) | Magnitude: 49.6 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 69, encapsulation: 27, structural_boundaries: 24, doc: 22
- `watchfiles-1.1.1/watchfiles/run.py` (PYTHON) | Magnitude: 114.74 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 80, branch: 50, generics: 44
- `watchfiles-1.1.1/tests/test_filters.py` (PYTHON) | Magnitude: 40.12 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 44, test: 28, safety: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `watchfiles-1.1.1/watchfiles/main.py` (PYTHON) | Magnitude: 21.78 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 56, branch: 55, generics: 38
- `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` (PYTHON) | Magnitude: 12.22 | Delta: **0.53 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 16, structural_boundaries: 11, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `watchfiles-1.1.1/tests/test_run_process.py` (PYTHON) | Magnitude: 150.2 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 119, test: 104, safety: 54
- `watchfiles-1.1.1/tests/test_watch.py` (PYTHON) | Magnitude: 161.56 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 87, test: 61, safety: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `watchfiles-1.1.1/watchfiles/cli.py` (PYTHON) | Magnitude: 100.44 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 53, branch: 38, import: 13
- `watchfiles-1.1.1/watchfiles/version.py` (PYTHON) | Magnitude: 12.56 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 4, structural_boundaries: 2, api: 1, import: 1
- `watchfiles-1.1.1/tests/test_rust_notify.py` (PYTHON) | Magnitude: 153.0 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 75, test: 67, explicit_casts: 55
- `watchfiles-1.1.1/tests/test_force_polling.py` (PYTHON) | Magnitude: 36.4 | Delta: **0.303 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 32, test: 16, args: 8
- `watchfiles-1.1.1/watchfiles/__main__.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.411 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, encapsulation: 2, branch: 1, import: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `watchfiles-1.1.1/watchfiles/cli.py` -> **Severity: 0.187** (Bridge: 0.0115 * Flux: 16.2698%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 0.172** (Bridge: 0.0017 * Flux: 99.9269%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 0.039** (Bridge: 0.0023 * Flux: 16.9335%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` -> **Severity: 14.288** (Embedded: 0.2087 * Error Risk: 68.4615%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 13.96** (Embedded: 0.2083 * Error Risk: 67.0092%)
- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 10.795** (Embedded: 0.2222 * Error Risk: 48.5758%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 8.19** (Embedded: 0.119 * Error Risk: 68.7931%)
- `watchfiles-1.1.1/watchfiles/cli.py` -> **Severity: 3.375** (Embedded: 0.0667 * Error Risk: 50.6232%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `watchfiles-1.1.1/watchfiles/_rust_notify.pyi` -> **Severity: 5967.64** (Blast Radius: 134.37 * Doc Risk: 44.412%)
- `watchfiles-1.1.1/watchfiles/main.py` -> **Severity: 2302.859** (Blast Radius: 193.188 * Doc Risk: 11.9203%)
- `watchfiles-1.1.1/Makefile` -> **Severity: 1654.032** (Blast Radius: 16.829 * Doc Risk: 98.2846%)
- `watchfiles-1.1.1/watchfiles/filters.py` -> **Severity: 1580.203** (Blast Radius: 132.564 * Doc Risk: 11.9203%)
- `watchfiles-1.1.1/watchfiles/run.py` -> **Severity: 1464.407** (Blast Radius: 40.432 * Doc Risk: 36.219%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
