# ARCHITECTURAL_BRIEF: shellingham
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/shellingham` |
| **Timestamp** | `2026-08-03T21:25:14.723388+00:00` |
| **Scan Duration** | `0.16s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 9 malicious artifacts.

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
| Total Artifacts | 15 |
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 361 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 9 | 361 | 90.0% |
| PLAINTEXT | 1 | 0 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.377`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 5 | 50.0% |
| file_cluster_13 | 4 | 40.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 17.9 | 8.3 | 8.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 16.5 | 3.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.9 | 2.6 | 0.3 |
| API Exposure | 0.0 | 5.4 | 2.0 | 1.6 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 76.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.9 | 58.7 | 59.9 | 1.6 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 56.7 | 96.8 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `shellingham-1.5.4/src/shellingham/posix/proc.py` (Hits: 9)
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` (Hits: 7)
- `shellingham-1.5.4/tests/test_posix.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_core.py** (`shellingham-1.5.4/src/shellingham/_core.py`) — 1 inbound connections
2. **_core.py** (`shellingham-1.5.4/src/shellingham/posix/_core.py`) — 1 inbound connections
3. **MANIFEST.in** (`shellingham-1.5.4/MANIFEST.in`) — 0 inbound connections
4. **setup.py** (`shellingham-1.5.4/setup.py`) — 0 inbound connections
5. **__init__.py** (`shellingham-1.5.4/src/shellingham/__init__.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **nt.py** (`shellingham-1.5.4/src/shellingham/nt.py`) — 5 outbound dependencies
2. **proc.py** (`shellingham-1.5.4/src/shellingham/posix/proc.py`) — 5 outbound dependencies
3. **__init__.py** (`shellingham-1.5.4/src/shellingham/posix/__init__.py`) — 4 outbound dependencies
4. **ps.py** (`shellingham-1.5.4/src/shellingham/posix/ps.py`) — 4 outbound dependencies
5. **test_posix.py** (`shellingham-1.5.4/tests/test_posix.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `iter_process_parents` (@ `shellingham-1.5.4/src/shellingham/posix/ps.py`) -> Impact: **40.2** | LOC: 41
  * *Intent:* """Try to look up the process tree via the output of `ps`."""
- `_get_interpreter_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **30.9** | LOC: 11
- `get_shell` (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> Impact: **29.3** | LOC: 32
- `unpatch` (@ `shellingham-1.5.4/tests/test_posix.py`) -> Impact: **17.7** | LOC: 8
- `_get_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **16.4** | LOC: 16
- `detect_shell` (@ `shellingham-1.5.4/src/shellingham/__init__.py`) -> Impact: **16.3** | LOC: 15
- `_iter_process_parents` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **14.4** | LOC: 10
- `get_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> Impact: **14.3** | LOC: 9
- `iter_process_parents` (@ `shellingham-1.5.4/src/shellingham/posix/proc.py`) -> Impact: **13.9** | LOC: 18
- `_check_expected` (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> Impact: **10.9** | LOC: 10

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_get_interpreter_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> **O(N^4)**
- `iter_process_parents` (@ `shellingham-1.5.4/src/shellingham/posix/proc.py`) -> **O(N^4)**
- `unpatch` (@ `shellingham-1.5.4/tests/test_posix.py`) -> **O(N^4)**
- `get_shell` (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> **O(N^3)**
- `_check_expected` (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> **O(N^3)**
- `_iter_processes` (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> **O(N^3)**
- `_get_full_path` (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> **O(N^3)**
- `_check_handle` (@ `shellingham-1.5.4/src/shellingham/nt.py`) -> **O(N^3)**
- `_iter_process_parents` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> **O(N^3)**
- `get_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `patch` (@ `shellingham-1.5.4/tests/test_posix.py`) -> DB Complexity: **12**
- `detect_proc` (@ `shellingham-1.5.4/src/shellingham/posix/proc.py`) -> DB Complexity: **9**
  * *Intent:* """Detect /proc filesystem style. This checks the /proc/{pid} directory for possible formats. Returns one of the following as str: * `stat`: Linux-sty...
- `_get_cmdline` (@ `shellingham-1.5.4/src/shellingham/posix/proc.py`) -> DB Complexity: **9**
- `unpatch` (@ `shellingham-1.5.4/tests/test_posix.py`) -> DB Complexity: **7**
- `_get_interpreter_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> DB Complexity: **6**
- `_get_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> DB Complexity: **6**
- `_get_login_shell` (@ `shellingham-1.5.4/src/shellingham/posix/__init__.py`) -> DB Complexity: **6**
- `_get_ppid` (@ `shellingham-1.5.4/src/shellingham/posix/proc.py`) -> DB Complexity: **6**
- `iter_process_parents` (@ `shellingham-1.5.4/src/shellingham/posix/ps.py`) -> DB Complexity: **6**
  * *Intent:* """Try to look up the process tree via the output of `ps`."""
- `detect_shell` (@ `shellingham-1.5.4/src/shellingham/__init__.py`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `shellingham-1.5.4/src/shellingham/posix` | 4 | 190.68 | 7.07% | 63.31% |
| `shellingham-1.5.4/src/shellingham` | 3 | 119.1 | 10.37% | 7.31% |
| `shellingham-1.5.4/tests` | 1 | 55.9 | 10.18% | 0.0% |
| `shellingham-1.5.4` | 2 | 12.04 | 2.5% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `shellingham-1.5.4/src/shellingham/posix/ps.py` -> **99.9955%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **99.956%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **53.2847%** Exposure
- `shellingham-1.5.4/src/shellingham/nt.py` -> **21.9173%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `shellingham-1.5.4/tests/test_posix.py` -> **2** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/nt.py` -> **1** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **1** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **1** Orphaned Functions | **0** Duplicates
- `shellingham-1.5.4/src/shellingham/posix/ps.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`shellingham-1.5.4/src/shellingham/__init__.py`** -> AI Confidence: **99.0%**
2. **`shellingham-1.5.4/src/shellingham/posix/__init__.py`** -> AI Confidence: **98.96%**
3. **`shellingham-1.5.4/src/shellingham/posix/proc.py`** -> AI Confidence: **98.96%**
4. **`shellingham-1.5.4/src/shellingham/posix/ps.py`** -> AI Confidence: **98.96%**
5. **`shellingham-1.5.4/src/shellingham/nt.py`** -> AI Confidence: **98.93%**
6. **`shellingham-1.5.4/tests/test_posix.py`** -> AI Confidence: **98.88%**
7. **`shellingham-1.5.4/setup.py`** -> AI Confidence: **98.84%**
8. **`shellingham-1.5.4/src/shellingham/_core.py`** -> AI Confidence: **98.84%**
9. **`shellingham-1.5.4/src/shellingham/posix/_core.py`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `shellingham-1.5.4/tests/test_posix.py` -> **99.9958%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **73.7017%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **57.6598%** Exposure
- `shellingham-1.5.4/src/shellingham/nt.py` -> **0.0004%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/ps.py` -> **0.0004%** Exposure
### Algorithmic DoS Exposure
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **100.0%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **100.0%** Exposure
- `shellingham-1.5.4/tests/test_posix.py` -> **100.0%** Exposure
- `shellingham-1.5.4/src/shellingham/posix/ps.py` -> **99.9186%** Exposure
- `shellingham-1.5.4/src/shellingham/nt.py` -> **96.8127%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `22` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `shellingham-1.5.4/src/shellingham/posix/proc.py` (PYTHON) -> Cumulative Risk: **569.36**
- **Archetype:** `file_cluster_13` (Distance: 9.041 IQR)
- **Magnitude:** 50.38 | **LOC:** 84 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.956%), Documentation (98.7641%)
- **Heaviest Functions:** `iter_process_parents` (Impact: 13.9), `detect_proc` (Impact: 10.8), `_get_ppid` (Impact: 8.2)

### 2. `shellingham-1.5.4/src/shellingham/posix/__init__.py` (PYTHON) -> Cumulative Risk: **566.02**
- **Archetype:** `file_cluster_8` (Distance: 8.871 IQR)
- **Magnitude:** 86.34 | **LOC:** 113 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8655%), Verification (80.0%)
- **Heaviest Functions:** `_get_interpreter_shell` (Impact: 30.9), `_get_shell` (Impact: 16.4), `_iter_process_parents` (Impact: 14.4)

### 3. `shellingham-1.5.4/src/shellingham/nt.py` (PYTHON) -> Cumulative Risk: **462.58**
- **Archetype:** `file_cluster_8` (Distance: 7.829 IQR)
- **Magnitude:** 84.74 | **LOC:** 164 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.8865%), Algorithmic Dos (96.8127%), Verification (80.0%)
- **Heaviest Functions:** `get_shell` (Impact: 29.3), `_check_expected` (Impact: 10.9), `_iter_processes` (Impact: 10.8)

### 4. `shellingham-1.5.4/src/shellingham/posix/ps.py` (PYTHON) -> Cumulative Risk: **421.92**
- **Archetype:** `file_cluster_13` (Distance: 10.474 IQR)
- **Magnitude:** 42.92 | **LOC:** 52 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9955%), Algorithmic Dos (99.9186%), Documentation (55.9166%)
- **Heaviest Functions:** `iter_process_parents` (Impact: 40.2)

### 5. `shellingham-1.5.4/tests/test_posix.py` (PYTHON) -> Cumulative Risk: **372.97**
- **Archetype:** `file_cluster_13` (Distance: 10.653 IQR)
- **Magnitude:** 55.9 | **LOC:** 86 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9958%), Stability (50.0%)
- **Heaviest Functions:** `unpatch` (Impact: 17.7), `patch` (Impact: 10.7), `__init__` (Impact: 2.7)

### 6. `shellingham-1.5.4/src/shellingham/__init__.py` (PYTHON) -> Cumulative Risk: **285.58**
- **Archetype:** `file_cluster_13` (Distance: 10.152 IQR)
- **Magnitude:** 18.68 | **LOC:** 24 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.682%), Stability (50.0%), Cognitive Load (17.8533%)
- **Heaviest Functions:** `detect_shell` (Impact: 16.3)

### 7. `shellingham-1.5.4/src/shellingham/_core.py` (PYTHON) -> Cumulative Risk: **261.72**
- **Archetype:** `file_cluster_8` (Distance: 6.299 IQR)
- **Magnitude:** 15.68 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (80.0%), Spec Match (60.0%), Documentation (59.9389%), Stability (50.0%)

### 8. `shellingham-1.5.4/src/shellingham/posix/_core.py` (PYTHON) -> Cumulative Risk: **81.97**
- **Archetype:** `file_cluster_8` (Distance: 6.385 IQR)
- **Magnitude:** 11.04 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (13.3333%), Documentation (13.3333%), Cognitive Load (5.0%)

### 9. `shellingham-1.5.4/setup.py` (PYTHON) -> Cumulative Risk: **70.23**
- **Archetype:** `file_cluster_8` (Distance: 6.535 IQR)
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (13.3333%), Cognitive Load (5.0%), Documentation (1.5894%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `shellingham-1.5.4/src/shellingham/posix/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.871 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.453 IQR)
- **Top Global Matches:** file_cluster_8: 8.871, file_cluster_13: 9.172, file_cluster_7: 9.299
- **Magnitude:** 86.34 | **LOC:** 113 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (8.9267%), Tech Debt (53.2847%)
**Top Internal Functions/Classes:**
  * `_get_interpreter_shell` (Impact: 30.9 | O(N^4) | DB: 6)
  * `_get_shell` (Impact: 16.4 | O(N^2) | DB: 6)
  * `_iter_process_parents` (Impact: 14.4 | O(N^3))
  * `get_shell` (Impact: 14.3 | O(N^3) | DB: 3)
  * `_get_login_shell` (Impact: 8.2 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 1`, `import: 4`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , os, .._core, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/nt.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.829 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.261 IQR)
- **Top Global Matches:** file_cluster_8: 7.829, file_cluster_13: 8.419, file_cluster_7: 8.592
- **Magnitude:** 84.74 | **LOC:** 164 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (8.2426%), Tech Debt (21.9173%)
**Top Internal Functions/Classes:**
  * `get_shell` (Impact: 29.3 | O(N^3) | DB: 3)
  * `_check_expected` (Impact: 10.9 | O(N^3))
  * `_iter_processes` (Impact: 10.8 | O(N^3))
  * `_get_full_path` (Impact: 10.7 | O(N^3))
  * `_handle` (Impact: 9.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 28`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 5`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, ctypes.wintypes, shellingham._core, os, ctypes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/tests/test_posix.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.653 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.658 IQR)
- **Top Global Matches:** file_cluster_13: 10.653, file_cluster_0: 10.859, file_cluster_8: 10.891
- **Magnitude:** 55.9 | **LOC:** 86 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (10.1814%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unpatch` (Impact: 17.7 | O(N^4) | DB: 7)
  * `patch` (Impact: 10.7 | O(N^3) | DB: 12)
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 2)
  * `test_get_shell` (Impact: 2.4 | O(N^1))
  * `environ` (Impact: 2.0 | O(N^1))
    * *Intent:* """Provide environment variable override, and restore on finalize. """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `orphaned_logic: 2`
* *Architecture:* `io: 5`, `api: 5`, `import: 4`
* *Defense:* `safety: 3`, `doc: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, shellingham.posix._core, pytest, shellingham
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/posix/proc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.041 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.375 IQR)
- **Top Global Matches:** file_cluster_13: 9.041, file_cluster_8: 9.203, file_cluster_7: 9.465
- **Magnitude:** 50.38 | **LOC:** 84 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (5.9601%), Tech Debt (99.956%)
**Top Internal Functions/Classes:**
  * `iter_process_parents` (Impact: 13.9 | O(N^4))
  * `detect_proc` (Impact: 10.8 | O(N^3) | DB: 9)
    * *Intent:* """Detect /proc filesystem style. This checks the /proc/{pid} directory for possible formats. Return...
  * `_get_ppid` (Impact: 8.2 | O(N^2) | DB: 6)
  * `_get_cmdline` (Impact: 8.2 | O(N^2) | DB: 9)
  * `_use_bsd_stat_format` (Impact: 5.4 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 9`, `api: 3`, `import: 5`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._core, sys, re, os, io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/posix/ps.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.474 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.999 IQR)
- **Top Global Matches:** file_cluster_13: 10.474, file_cluster_8: 10.71, file_cluster_7: 10.963
- **Magnitude:** 42.92 | **LOC:** 52 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (8.3848%), Tech Debt (99.9955%)
**Top Internal Functions/Classes:**
  * `iter_process_parents` (Impact: 40.2 | O(N^3) | DB: 6)
    * *Intent:* """Try to look up the process tree via the output of `ps`."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 4`
* *Defense:* `safety: 8`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, ._core, errno, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.97 IQR)
- **Top Global Matches:** file_cluster_13: 10.152, file_cluster_8: 10.293, file_cluster_17: 10.554
- **Magnitude:** 18.68 | **LOC:** 24 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (17.8533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `detect_shell` (Impact: 16.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._core, os, importlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/_core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.299 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.631 IQR)
- **Top Global Matches:** file_cluster_8: 6.299, file_cluster_2: 6.821, file_cluster_7: 7.476
- **Magnitude:** 15.68 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 158.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `shellingham-1.5.4/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.535 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.738 IQR)
- **Top Global Matches:** file_cluster_8: 6.535, file_cluster_13: 6.617, file_cluster_7: 7.817
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shellingham-1.5.4/src/shellingham/posix/_core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.385 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.703 IQR)
- **Top Global Matches:** file_cluster_8: 6.385, file_cluster_13: 6.524, file_cluster_7: 7.699
- **Magnitude:** 11.04 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 158.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` collections
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `shellingham-1.5.4/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `shellingham-1.5.4/src/shellingham/__init__.py` (PYTHON) | Magnitude: 18.68 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 6, branch: 5, safety: 4
- `shellingham-1.5.4/src/shellingham/posix/proc.py` (PYTHON) | Magnitude: 50.38 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 24, branch: 9, io: 9
- `shellingham-1.5.4/tests/test_posix.py` (PYTHON) | Magnitude: 55.9 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 14, state_mutation: 14, test: 9
- `shellingham-1.5.4/src/shellingham/posix/ps.py` (PYTHON) | Magnitude: 42.92 | Delta: **0.236 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 13, branch: 10, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `shellingham-1.5.4/setup.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1
- `shellingham-1.5.4/src/shellingham/posix/_core.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, import: 1
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` (PYTHON) | Magnitude: 86.34 | Delta: **0.301 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 23, branch: 19, encapsulation: 11
- `shellingham-1.5.4/src/shellingham/_core.py` (PYTHON) | Magnitude: 15.68 | Delta: **0.522 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 2, class_start: 1, safety_bypasses: 1
- `shellingham-1.5.4/src/shellingham/nt.py` (PYTHON) | Magnitude: 84.74 | Delta: **0.59 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 28, branch: 16, encapsulation: 16

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `shellingham-1.5.4/src/shellingham/_core.py` -> **Severity: 8.889** (Embedded: 0.1111 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `shellingham-1.5.4/src/shellingham/_core.py` -> **Severity: 9477.539** (Blast Radius: 158.12 * Doc Risk: 59.9389%)
- `shellingham-1.5.4/src/shellingham/nt.py` -> **Severity: 8537.299** (Blast Radius: 85.47 * Doc Risk: 99.8865%)
- `shellingham-1.5.4/src/shellingham/posix/__init__.py` -> **Severity: 8535.504** (Blast Radius: 85.47 * Doc Risk: 99.8655%)
- `shellingham-1.5.4/src/shellingham/posix/proc.py` -> **Severity: 8441.368** (Blast Radius: 85.47 * Doc Risk: 98.7641%)
- `shellingham-1.5.4/src/shellingham/__init__.py` -> **Severity: 8434.351** (Blast Radius: 85.47 * Doc Risk: 98.682%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
