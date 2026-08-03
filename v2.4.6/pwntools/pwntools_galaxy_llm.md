# ARCHITECTURAL_BRIEF: pwntools
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pwntools` |
| **Timestamp** | `2026-08-03T21:18:59.003352+00:00` |
| **Scan Duration** | `0.45s` |
| **Git Branch** | `dev` |
| **Git Commit** | `fd3cf3d43f39d4b50c1d0f33875bdc733afb48fa` |
| **Git Remote** | `https://github.com/Gallopsled/pwntools.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 53 malicious artifacts.

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
| Total Artifacts | 1461 |
| Analyzed Artifacts (Scanned) | 68 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1393 |
| Total LOC | 1227 |
| Volatility Index | 0.015 |
| % Scanned of codebase = | 4.7% |
| Dominant Lang | DOCKERFILE |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6667 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 32 | 602 | 47.1% |
| MARKDOWN | 12 | 0 | 17.6% |
| SHELL | 10 | 301 | 14.7% |
| DOCKERFILE | 6 | 198 | 8.8% |
| PLAINTEXT | 3 | 0 | 4.4% |
| MAKEFILE | 3 | 84 | 4.4% |
| C | 2 | 42 | 2.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.084`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 32 | 47.1% |
| file_cluster_13 | 13 | 19.1% |
| file_cluster_9 | 2 | 2.9% |
| file_cluster_4 | 2 | 2.9% |
| file_cluster_1 | 1 | 1.5% |
| file_cluster_12 | 1 | 1.5% |
| file_cluster_2 | 1 | 1.5% |
| file_cluster_17 | 1 | 1.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 22.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1393*

**Composition by Extension & Reason:**
- `.asm`: 816x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 194x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 141x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 117x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 104 LOC), 1x Excluded (Unsupported Extension: '.YAML-tmLanguage')
- `.rst`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.native`: 2x Excluded (Unsupported Extension: '.native')
- `.native32`: 2x Excluded (Unsupported Extension: '.native32')
- `.c`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.aarch64`: 1x Excluded (Unsupported Extension: '.aarch64')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 3.2 | 100.0 | 21.8 | 5.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 58.5 | 80.0 | 80.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 10.4 | 1.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 69.6 | 5.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 15.4 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 73.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.0 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 29.8 | 2.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.7 | 15.2 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `travis/install.sh` (Hits: 29)
- `travis/ssh_setup.sh` (Hits: 25)
- `travis/docker/Dockerfile` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **asm.py** (`examples/asm.py`) — 1 inbound connections
2. **remote.py** (`examples/remote.py`) — 1 inbound connections
3. **splash.py** (`examples/splash.py`) — 1 inbound connections
4. **ssh.py** (`examples/ssh.py`) — 1 inbound connections
5. **toplevel.py** (`pwn/toplevel.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **toplevel.py** (`pwn/toplevel.py`) — 67 outbound dependencies
2. **10-import.py** (`extra/docker/develop/10-import.py`) — 12 outbound dependencies
3. **10-import.py** (`travis/docker/10-import.py`) — 12 outbound dependencies
4. **setup.py** (`setup.py`) — 7 outbound dependencies
5. **printf.c** (`examples/fmtstr/printf.c`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Anonymous_Block` (@ `travis/install.sh`) -> Impact: **45.6** | LOC: 43
- `Anonymous_Block` (@ `extra/bash_completion.d/shellcraft`) -> Impact: **39.5** | LOC: 40
- `exploit` (@ `examples/fmtstr/exploit2.py`) -> Impact: **34.0** | LOC: 57
- `Anonymous_Block` (@ `travis/setup_avd.sh`) -> Impact: **16.4** | LOC: 28
  * *Intent:* # If we are running on Travis CI, and there were no changes to Android # or ADB code, then we do not need the emulator
- `Anonymous_Block` (@ `travis/install.sh`) -> Impact: **14.8** | LOC: 15
- `submit_data` (@ `examples/clean_and_log.py`) -> Impact: **10.8** | LOC: 8
- `Anonymous_Block` (@ `travis/ssh_setup.sh`) -> Impact: **10.3** | LOC: 8
- `Anonymous_Block` (@ `travis/install.sh`) -> Impact: **9.6** | LOC: 11
- `Anonymous_Block` (@ `travis/install.sh`) -> Impact: **8.0** | LOC: 9
- `main` (@ `examples/fmtstr/printf.c`) -> Impact: **7.9** | LOC: 19
  * *Intent:* #ifdef _FORTIFY_SOURCE #undef _FORTIFY_SOURCE #endif #include <stdio.h> #include <stdlib.h> #include <unistd.h> #include <sys/mman.h> #define MEMORY_A...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Anonymous_Block` (@ `extra/bash_completion.d/shellcraft`) -> **O(N^4)**
- `submit_data` (@ `examples/clean_and_log.py`) -> **O(N^3)**
- `exploit` (@ `examples/fmtstr/exploit2.py`) -> **O(N^3)**
- `demo_async_breakpoint` (@ `examples/gdb_api.py`) -> **O(N^3)**
  * *Intent:* # set the asynchronous breakpoint on ``write``
- `continuation_prompt_tokens` (@ `extra/docker/develop/ipython_config.py`) -> **O(N^3)**
- `in_prompt_tokens` (@ `extra/docker/develop/ipython_config.py`) -> **O(N^3)**
- `continuation_prompt_tokens` (@ `travis/docker/ipython_config.py`) -> **O(N^3)**
- `in_prompt_tokens` (@ `travis/docker/ipython_config.py`) -> **O(N^3)**
- `main` (@ `examples/fmtstr/printf.c`) -> **O(N^3)**
  * *Intent:* #ifdef _FORTIFY_SOURCE #undef _FORTIFY_SOURCE #endif #include <stdio.h> #include <stdlib.h> #include <unistd.h> #include <sys/mman.h> #define MEMORY_A...

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block` (@ `travis/install.sh`) -> DB Complexity: **48**
- `Anonymous_Block` (@ `travis/setup_avd.sh`) -> DB Complexity: **24**
  * *Intent:* # If we are running on Travis CI, and there were no changes to Android # or ADB code, then we do not need the emulator
- `Anonymous_Block` (@ `travis/install.sh`) -> DB Complexity: **16**
- `Anonymous_Block` (@ `travis/install.sh`) -> DB Complexity: **15**
- `main` (@ `examples/fmtstr/printf.c`) -> DB Complexity: **13**
  * *Intent:* #ifdef _FORTIFY_SOURCE #undef _FORTIFY_SOURCE #endif #include <stdio.h> #include <stdlib.h> #include <unistd.h> #include <sys/mman.h> #define MEMORY_A...
- `Anonymous_Block` (@ `travis/setup_avd.sh`) -> DB Complexity: **12**
- `Anonymous_Block` (@ `extra/bash_completion.d/shellcraft`) -> DB Complexity: **10**
- `Anonymous_Block` (@ `extra/bash_completion.d/install.sh`) -> DB Complexity: **9**
- `main` (@ `examples/fmtstr/printf-loop.c`) -> DB Complexity: **7**
  * *Intent:* #include <stdio.h> #include <unistd.h>
- `Anonymous_Block` (@ `travis/docker/doctest3`) -> DB Complexity: **7**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `travis/docker` | 8 | 377.14 | 20.94% | 50.0% |
| `examples` | 23 | 317.38 | 13.64% | 0.0% |
| `travis` | 5 | 217.38 | 53.51% | 80.0% |
| `extra/docker/base` | 1 | 172.26 | 43.88% | 0.0% |
| `extra/docker/develop` | 3 | 151.21 | 11.92% | 33.33% |
| `examples/fmtstr` | 5 | 110.98 | 17.47% | 0.0% |
| `extra/bash_completion.d` | 3 | 80.54 | 35.0% | 65.61% |
| `__monolith__` | 10 | 59.28 | 1.29% | 0.0% |
| `extra/docker` | 2 | 49.66 | 22.6% | 0.0% |
| `pwn` | 2 | 32.44 | 5.84% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `extra/docker/develop/ipython_config.py` -> **100.0%** Exposure
- `travis/docker/ipython_config.py` -> **100.0%** Exposure
- `extra/bash_completion.d/install.sh` -> **100.0%** Exposure
- `travis/docker/run.sh` -> **100.0%** Exposure
- `travis/docker/tmux.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `travis/coverage_chdir.py` -> **100.0%** Exposure
- `extra/bash_completion.d/shellcraft` -> **100.0%** Exposure
- `extra/bash_completion.d/install.sh` -> **99.9987%** Exposure
- `travis/docker/doctest3` -> **99.9973%** Exposure
- `travis/ssh_setup.sh` -> **99.995%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `travis/install.sh` -> **1** Orphaned Functions | **9** Duplicates
- `travis/setup_avd.sh` -> **2** Orphaned Functions | **3** Duplicates
- `extra/docker/develop/ipython_config.py` -> **4** Orphaned Functions | **0** Duplicates
- `travis/docker/ipython_config.py` -> **4** Orphaned Functions | **0** Duplicates
- `travis/ssh_setup.sh` -> **1** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`extra/docker/base/Dockerfile`** -> AI Confidence: **99.29%**
2. **`setup.py`** -> AI Confidence: **99.23%**
3. **`extra/bash_completion.d/shellcraft`** -> AI Confidence: **99.17%**
4. **`travis/install.sh`** -> AI Confidence: **99.17%**
5. **`travis/ssh_setup.sh`** -> AI Confidence: **99.17%**
6. **`pwn/toplevel.py`** -> AI Confidence: **99.09%**
7. **`extra/docker/develop/10-import.py`** -> AI Confidence: **99.07%**
8. **`travis/docker/10-import.py`** -> AI Confidence: **99.07%**
9. **`examples/args.py`** -> AI Confidence: **99.06%**
10. **`examples/fmtstr/exploit2.py`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `travis/coverage_chdir.py` -> **100.0%** Exposure
- `extra/docker/develop/ipython_config.py` -> **32.6177%** Exposure
- `travis/docker/ipython_config.py` -> **32.6177%** Exposure
- `examples/fmtstr/printf.c` -> **20.0%** Exposure
- `examples/fmtstr/exploit2.py` -> **0.2555%** Exposure
### Weaponizable Injection Vectors
- `travis/coverage_chdir.py` -> **100.0%** Exposure
- `travis/docker/doctest3` -> **100.0%** Exposure
- `travis/docker/run.sh` -> **100.0%** Exposure
- `travis/install.sh` -> **100.0%** Exposure
- `travis/ssh_setup.sh` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `examples/fmtstr/printf.c` -> **100.0%** Exposure
- `travis/install.sh` -> **100.0%** Exposure
- `extra/docker/develop/ipython_config.py` -> **99.027%** Exposure
- `travis/docker/ipython_config.py` -> **99.027%** Exposure
- `extra/bash_completion.d/shellcraft` -> **98.065%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `148` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `travis/install.sh` (SHELL) -> Cumulative Risk: **787.03**
- **Archetype:** `file_cluster_8` (Distance: 9.781 IQR)
- **Magnitude:** 100.68 | **LOC:** 132 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 45.6), `Anonymous_Block` (Impact: 14.8), `Anonymous_Block` (Impact: 9.6)

### 2. `travis/setup_avd.sh` (SHELL) -> Cumulative Risk: **658.4**
- **Archetype:** `file_cluster_4` (Distance: 9.462 IQR)
- **Magnitude:** 49.92 | **LOC:** 97 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Injection Surface (99.9991%), Documentation (94.9049%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 16.4), `Anonymous_Block` (Impact: 7.2), `__global_context__` (Impact: 4.8)

### 3. `travis/ssh_setup.sh` (SHELL) -> Cumulative Risk: **645.14**
- **Archetype:** `file_cluster_8` (Distance: 11.216 IQR)
- **Magnitude:** 35.0 | **LOC:** 66 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.995%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 10.3), `Anonymous_Block` (Impact: 7.5), `__global_context__` (Impact: 4.4)

### 4. `extra/bash_completion.d/shellcraft` (SHELL) -> Cumulative Risk: **630.78**
- **Archetype:** `file_cluster_12` (Distance: 14.583 IQR)
- **Magnitude:** 70.66 | **LOC:** 49 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9915%), Documentation (99.7363%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 39.5), `__global_context__` (Impact: 1.4)

### 5. `travis/docker/doctest3` (SHELL) -> Cumulative Risk: **615.88**
- **Archetype:** `file_cluster_8` (Distance: 11.203 IQR)
- **Magnitude:** 15.08 | **LOC:** 36 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.9973%), Tech Debt (99.9912%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 5.5), `__global_context__` (Impact: 2.2)

### 6. `travis/coverage_chdir.py` (PYTHON) -> Cumulative Risk: **522.03**
- **Archetype:** `file_cluster_13` (Distance: 10.616 IQR)
- **Magnitude:** 21.2 | **LOC:** 13 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Safety Score (90.025%)

### 7. `travis/setup_avd_fast.sh` (SHELL) -> Cumulative Risk: **514.03**
- **Archetype:** `file_cluster_4` (Distance: 10.131 IQR)
- **Magnitude:** 10.58 | **LOC:** 27 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (97.377%), Spec Match (93.3333%), Documentation (93.3278%)
- **Heaviest Functions:** `__global_context__` (Impact: 2.2), `Anonymous_Block_[Truncated]` (Impact: 2.1)

### 8. `travis/docker/run.sh` (SHELL) -> Cumulative Risk: **434.35**
- **Archetype:** `file_cluster_8` (Distance: 11.385 IQR)
- **Magnitude:** 0.25 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Injection Surface (100.0%), State Flux (99.9629%), Safety Score (98.7258%)
- **Heaviest Functions:** `__global_context__` (Impact: 1.4)

### 9. `travis/docker/ipython_config.py` (PYTHON) -> Cumulative Risk: **396.7**
- **Archetype:** `file_cluster_9` (Distance: 24.041 IQR)
- **Magnitude:** 18.72 | **LOC:** 564 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (99.027%), Logic Bomb (32.6177%)
- **Heaviest Functions:** `continuation_prompt_tokens` (Impact: 4.2), `in_prompt_tokens` (Impact: 3.7), `rewrite_prompt_tokens` (Impact: 2.7)

### 10. `extra/docker/develop/ipython_config.py` (PYTHON) -> Cumulative Risk: **386.34**
- **Archetype:** `file_cluster_9` (Distance: 24.032 IQR)
- **Magnitude:** 18.72 | **LOC:** 564 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (99.027%), Logic Bomb (32.6177%)
- **Heaviest Functions:** `continuation_prompt_tokens` (Impact: 4.2), `in_prompt_tokens` (Impact: 3.7), `rewrite_prompt_tokens` (Impact: 2.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `travis/docker/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.557 IQR)
- **Top Global Matches:** file_cluster_17: 12.557, file_cluster_0: 12.639, file_cluster_8: 12.692
- **Magnitude:** 310.84 | **LOC:** 139 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (24.7431%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 13`, `args: 1`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`, `dead_code: 2`
* *Architecture:* `io: 16`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwntools:base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/docker/base/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.989 IQR)
- **Top Global Matches:** file_cluster_8: 9.989, file_cluster_13: 10.282, file_cluster_7: 10.573
- **Magnitude:** 172.26 | **LOC:** 50 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (43.8774%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 2`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ubuntu:noble
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/docker/develop/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.459 IQR)
- **Top Global Matches:** file_cluster_8: 9.459, file_cluster_13: 10.027, file_cluster_7: 10.249
- **Magnitude:** 118.89 | **LOC:** 83 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.9787%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 3`, `args: 1`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `io: 13`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwntools:base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/install.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.781 IQR)
- **Top Global Matches:** file_cluster_8: 9.781, file_cluster_0: 9.983, file_cluster_4: 10.085
- **Magnitude:** 100.68 | **LOC:** 132 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (99.7798%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 45.6 | O(N^2) | DB: 48)
  * `Anonymous_Block` (Impact: 14.8 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 9.6 | O(N^2) | DB: 4)
  * `Anonymous_Block` (Impact: 8.0 | O(N^2) | DB: 15)
  * `Anonymous_Block` (Impact: 1.8 | O(N^1) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 21`, `args: 3`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 11`, `state_mutation: 8`, `duplicate_logic: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 29`, `api: 3`, `concurrency: 1`
* *Defense:* `safety: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/bash_completion.d/shellcraft` (SHELL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_12` (Drift: 14.583 IQR)
- **Top Global Matches:** file_cluster_12: 14.583, file_cluster_8: 14.608, file_cluster_11: 14.828
- **Magnitude:** 70.66 | **LOC:** 49 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (99.9915%), Tech Debt (96.8356%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 39.5 | O(N^4) | DB: 10)
  * `__global_context__` (Impact: 1.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 29`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/setup_avd.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.462 IQR)
- **Top Global Matches:** file_cluster_4: 9.462, file_cluster_8: 9.462, file_cluster_0: 9.705
- **Magnitude:** 49.92 | **LOC:** 97 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (61.6663%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 16.4 | O(N^1) | DB: 24)
    * *Intent:* # If we are running on Travis CI, and there were no changes to Android # or ADB code, then we do not...
  * `Anonymous_Block` (Impact: 7.2 | O(N^1) | DB: 12)
  * `__global_context__` (Impact: 4.8 | O(N^1))
  * `Anonymous_Block` (Impact: 4.2 | O(N^1))
  * `Anonymous_Block_[Truncated]` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 29`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 6`, `duplicate_logic: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 15`, `api: 6`, `concurrency: 2`
* *Defense:* `safety: 1`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/docker/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.809 IQR)
- **Top Global Matches:** file_cluster_8: 7.809, file_cluster_12: 8.699, file_cluster_7: 8.821
- **Magnitude:** 48.6 | **LOC:** 40 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.1959%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/fmtstr/exploit2.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.919 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.119 IQR)
- **Top Global Matches:** file_cluster_8: 10.919, file_cluster_13: 11.096, file_cluster_0: 11.311
- **Magnitude:** 36.92 | **LOC:** 69 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.2319%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `exploit` (Impact: 34.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 1`, `doc: 2`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwn
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/ssh_setup.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.216 IQR)
- **Top Global Matches:** file_cluster_8: 11.216, file_cluster_0: 11.282, file_cluster_17: 11.348
- **Magnitude:** 35.0 | **LOC:** 66 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (96.0834%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 10.3 | O(N^1))
  * `Anonymous_Block` (Impact: 7.5 | O(N^1) | DB: 3)
  * `__global_context__` (Impact: 4.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 5`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 3`, `state_mutation: 12`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 25`
* *Defense:* `safety: 1`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 27.6 | **LOC:** 1380 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/fmtstr/printf.c` (C | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.444 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.937 IQR)
- **Top Global Matches:** file_cluster_13: 11.444, file_cluster_8: 11.811, file_cluster_0: 12.208
- **Magnitude:** 23.48 | **LOC:** 30 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (54.2997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 7.9 | O(N^3) | DB: 13)
    * *Intent:* #ifdef _FORTIFY_SOURCE #undef _FORTIFY_SOURCE #endif #include <stdio.h> #include <stdlib.h> #include...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 10`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 5`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, mman.h, unistd.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/gdb_api.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.129 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.419 IQR)
- **Top Global Matches:** file_cluster_8: 10.129, file_cluster_7: 10.412, file_cluster_13: 10.532
- **Magnitude:** 22.64 | **LOC:** 113 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.0742%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `demo_async_breakpoint` (Impact: 5.7 | O(N^3) | DB: 1)
    * *Intent:* # set the asynchronous breakpoint on ``write``
  * `main` (Impact: 3.6 | O(N^1))
    * *Intent:* ''', api=True) as cat: # the process is stopped # set the synchronous breakpoint on ``read`` cat.gdb...
  * `demo_sync_breakpoint` (Impact: 3.2 | O(N^1))
  * `check_write` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 3`, `doc: 12`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwn
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/docker/beta/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.311 IQR)
- **Top Global Matches:** file_cluster_13: 10.311, file_cluster_8: 10.338, file_cluster_17: 11.047
- **Magnitude:** 22.6 | **LOC:** 7 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwntools:stable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/docker/dev/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.311 IQR)
- **Top Global Matches:** file_cluster_13: 10.311, file_cluster_8: 10.338, file_cluster_17: 11.047
- **Magnitude:** 22.6 | **LOC:** 7 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwntools:stable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/docker/stable/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.311 IQR)
- **Top Global Matches:** file_cluster_13: 10.311, file_cluster_8: 10.338, file_cluster_17: 11.047
- **Magnitude:** 22.6 | **LOC:** 7 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwntools:base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/fmtstr/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.384 IQR)
- **Top Global Matches:** file_cluster_8: 6.384, file_cluster_7: 7.53, file_cluster_1: 7.74
- **Magnitude:** 22.54 | **LOC:** 54 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.5776%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `api: 7`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.465 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.291 IQR)
- **Top Global Matches:** file_cluster_8: 8.465, file_cluster_13: 8.607, file_cluster_7: 9.378
- **Magnitude:** 22.22 | **LOC:** 82 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.8556%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `io: 10`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, distutils.sysconfig, distutils.command.install, glob, distutils.util, sys, setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/coverage_chdir.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.616 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.735 IQR)
- **Top Global Matches:** file_cluster_13: 10.616, file_cluster_8: 11.274, file_cluster_17: 11.567
- **Magnitude:** 21.2 | **LOC:** 13 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`
* *Architecture:* `io: 6`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, coverage, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/docker/develop/ipython_config.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_9` (Drift: 24.032 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.481 IQR)
- **Top Global Matches:** file_cluster_9: 24.032, file_cluster_6: 24.114, file_cluster_0: 24.118
- **Magnitude:** 18.72 | **LOC:** 564 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.7923%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `continuation_prompt_tokens` (Impact: 4.2 | O(N^3))
  * `in_prompt_tokens` (Impact: 3.7 | O(N^3))
  * `rewrite_prompt_tokens` (Impact: 2.7 | O(N^2))
  * `out_prompt_tokens` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `dead_code: 7`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` any, IPython.terminal.prompts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/docker/ipython_config.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_9` (Drift: 24.041 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.481 IQR)
- **Top Global Matches:** file_cluster_9: 24.041, file_cluster_6: 24.122, file_cluster_0: 24.127
- **Magnitude:** 18.72 | **LOC:** 564 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.7923%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `continuation_prompt_tokens` (Impact: 4.2 | O(N^3))
  * `in_prompt_tokens` (Impact: 3.7 | O(N^3))
  * `rewrite_prompt_tokens` (Impact: 2.7 | O(N^2))
  * `out_prompt_tokens` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `dead_code: 7`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` any, IPython.terminal.prompts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/spinners.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.187 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.72 IQR)
- **Top Global Matches:** file_cluster_8: 10.187, file_cluster_13: 10.316, file_cluster_7: 10.599
- **Magnitude:** 18.32 | **LOC:** 26 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (21.8912%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwn
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pwn/toplevel.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.468 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.453 IQR)
- **Top Global Matches:** file_cluster_13: 8.468, file_cluster_8: 8.959, file_cluster_7: 9.932
- **Magnitude:** 17.76 | **LOC:** 105 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.6834%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 129`
* *Risk/State:* `safety_bypasses: 24`
* *Architecture:* `concurrency: 1`, `import: 73`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.27
  * `Choke Point (Betweenness):` 0.000905 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 4):` math, signal, pwnlib.util.crc, pwnlib.tubes.process, logging, pwnlib.flag, pwnlib.dynelf, pwnlib.ui...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/fmtstr/printf-loop.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.25 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.857 IQR)
- **Top Global Matches:** file_cluster_13: 12.25, file_cluster_8: 12.665, file_cluster_0: 13.028
- **Magnitude:** 17.76 | **LOC:** 15 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 2.5 | O(N^1) | DB: 7)
    * *Intent:* #include <stdio.h> #include <unistd.h>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `travis/docker/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.197 IQR)
- **Top Global Matches:** file_cluster_8: 7.197, file_cluster_7: 8.291, file_cluster_1: 8.396
- **Magnitude:** 17.54 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.0359%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `io: 4`, `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/sigreturn_corefile_aarch64.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.364 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.005 IQR)
- **Top Global Matches:** file_cluster_8: 8.364, file_cluster_13: 9.209, file_cluster_12: 9.37
- **Magnitude:** 15.5 | **LOC:** 34 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (58.904%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 3`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.2
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pwn
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `examples/remote.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.306 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, safety_bypasses: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `extra/bash_completion.d/shellcraft` (SHELL) | Magnitude: 70.66 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 29, branch: 14, safety: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `extra/docker/beta/Dockerfile` (DOCKERFILE) | Magnitude: 22.6 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, func_start: 2, sec_high_risk_execution: 2, branch: 1
- `extra/docker/dev/Dockerfile` (DOCKERFILE) | Magnitude: 22.6 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, func_start: 2, sec_high_risk_execution: 2, branch: 1
- `extra/docker/stable/Dockerfile` (DOCKERFILE) | Magnitude: 22.6 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, func_start: 2, sec_high_risk_execution: 2, branch: 1
- `examples/options.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.189 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, branch: 1, safety_bypasses: 1
- `examples/port_forward.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.204 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, branch: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `travis/docker/Dockerfile` (DOCKERFILE) | Magnitude: 310.84 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 27, func_start: 19, branch: 17, io: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `travis/docker/tmux.sh` (SHELL) | Magnitude: 0.11 | Delta: **0.254 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ui_framework: 1, orphaned_logic: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `travis/setup_avd.sh` (SHELL) | Magnitude: 49.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 29, branch: 25, indent_spaces: 21, io: 15
- `travis/setup_avd_fast.sh` (SHELL) | Magnitude: 10.58 | Delta: **0.473 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, safety_bypasses: 4, io: 3, globals: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/remote_gdb_debugging.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, import: 2, safety_bypasses: 1
- `travis/ssh_setup.sh` (SHELL) | Magnitude: 35.0 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: io: 25, safety_bypasses: 16, ipc_rpc_bridges: 15, branch: 13
- `examples/yesno.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, doc: 2, debug_prints: 2
- `examples/attach.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, safety_bypasses: 1, import: 1
- `travis/docker/doctest3` (SHELL) | Magnitude: 15.08 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, io: 7, state_mutation: 6, debug_prints: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `travis/docker/ipython_config.py` (PYTHON) | Magnitude: 18.72 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, dead_code: 7, api: 5
- `extra/docker/develop/ipython_config.py` (PYTHON) | Magnitude: 18.72 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, dead_code: 7, api: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `extra/docker/base/Dockerfile` -> **peace-maker** (100.0% isolated ownership) | Magnitude: 172.26

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `examples/asm.py` -> **Severity: 1.592** (Embedded: 0.0199 * Error Risk: 80.0%)
- `examples/remote.py` -> **Severity: 1.592** (Embedded: 0.0199 * Error Risk: 80.0%)
- `examples/splash.py` -> **Severity: 1.592** (Embedded: 0.0199 * Error Risk: 80.0%)
- `pwn/toplevel.py` -> **Severity: 1.194** (Embedded: 0.0149 * Error Risk: 80.0%)
- `examples/ssh.py` -> **Severity: 0.995** (Embedded: 0.0199 * Error Risk: 50.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `extra/bash_completion.d/shellcraft` -> **Severity: 1416.255** (Blast Radius: 14.2 * Doc Risk: 99.7363%)
- `travis/setup_avd.sh` -> **Severity: 1347.65** (Blast Radius: 14.2 * Doc Risk: 94.9049%)
- `travis/setup_avd_fast.sh` -> **Severity: 1325.255** (Blast Radius: 14.2 * Doc Risk: 93.3278%)
- `extra/docker/base/Dockerfile` -> **Severity: 1053.336** (Blast Radius: 14.2 * Doc Risk: 74.1786%)
- `travis/coverage_chdir.py` -> **Severity: 833.821** (Blast Radius: 14.2 * Doc Risk: 58.7198%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
