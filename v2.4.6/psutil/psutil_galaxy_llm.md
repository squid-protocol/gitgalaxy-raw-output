# ARCHITECTURAL_BRIEF: psutil
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/psutil` |
| **Timestamp** | `2026-08-03T21:23:29.885753+00:00` |
| **Scan Duration** | `0.79s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 134 malicious artifacts.

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
| Total Artifacts | 150 |
| Analyzed Artifacts (Scanned) | 140 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 29549 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5487 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3658 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4545 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 103 | 12964 | 73.6% |
| PYTHON | 30 | 16278 | 21.4% |
| MARKDOWN | 3 | 0 | 2.1% |
| PLAINTEXT | 2 | 0 | 1.4% |
| YAML | 1 | 52 | 0.7% |
| MAKEFILE | 1 | 255 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.327`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 67 | 47.9% |
| file_cluster_8 | 56 | 40.0% |
| file_cluster_0 | 12 | 8.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.jsonc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.5 | 48.5 | 57.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 88.7 | 25.7 | 22.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.6 | 23.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 31.9 | 2.5 | 80.0 |
| API Exposure | 0.0 | 18.2 | 11.2 | 12.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 64.8 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 11.5 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 99.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 75.4 | 99.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 79.9 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 29.0 | 20.0 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `psutil-7.2.2/tests/test_linux.py` (Hits: 144)
- `psutil-7.2.2/tests/__init__.py` (Hits: 106)
- `psutil-7.2.2/psutil/_pslinux.py` (Hits: 83)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_common.py** (`psutil-7.2.2/psutil/_common.py`) — 16 inbound connections
2. **ntextapi.h** (`psutil-7.2.2/psutil/arch/windows/ntextapi.h`) — 3 inbound connections
3. **_pslinux.py** (`psutil-7.2.2/psutil/_pslinux.py`) — 2 inbound connections
4. **_psposix.py** (`psutil-7.2.2/psutil/_psposix.py`) — 2 inbound connections
5. **_pswindows.py** (`psutil-7.2.2/psutil/_pswindows.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`psutil-7.2.2/tests/__init__.py`) — 33 outbound dependencies
2. **_psutil_aix.c** (`psutil-7.2.2/psutil/_psutil_aix.c`) — 25 outbound dependencies
3. **test_process.py** (`psutil-7.2.2/tests/test_process.py`) — 24 outbound dependencies
4. **__init__.py** (`psutil-7.2.2/psutil/__init__.py`) — 21 outbound dependencies
5. **test_windows.py** (`psutil-7.2.2/tests/test_windows.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `calculate_avail_vmem` (@ `psutil-7.2.2/psutil/_pslinux.py`) -> Impact: **4644.0** | LOC: 1947
  * *Intent:* # ===================================================================== # --- system memory # ========================================================...
- `_check_conn_kind` (@ `psutil-7.2.2/psutil/__init__.py`) -> Impact: **2164.5** | LOC: 855
- `test_ips` (@ `psutil-7.2.2/tests/test_linux.py`) -> Impact: **1441.2** | LOC: 1302
- `adjust_proc_create_time` (@ `psutil-7.2.2/psutil/_psbsd.py`) -> Impact: **956.5** | LOC: 459
- `is_win_secure_system_proc` (@ `psutil-7.2.2/tests/__init__.py`) -> Impact: **844.5** | LOC: 644
  * *Intent:* # It should show up in pids() and process_iter(). # Call all methods. ns = process_namespace(proc) for fun, name in ns.iter(ns.all, clear_cache=True):...
- `macos_version` (@ `psutil-7.2.2/tests/__init__.py`) -> Impact: **767.9** | LOC: 463
- `create_time` (@ `psutil-7.2.2/tests/test_process_all.py`) -> Impact: **576.4** | LOC: 327
  * *Intent:* # on AIX, "<exiting>" processes don't have names
- `psutil_net_connections` (@ `psutil-7.2.2/psutil/arch/sunos/net.c`) -> Impact: **534.9** | LOC: 306
  * *Intent:* /*
- `psutil_gather_inet` (@ `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c`) -> Impact: **484.8** | LOC: 171
- `psutil_net_connections` (@ `psutil-7.2.2/psutil/arch/windows/socks.c`) -> Impact: **297.1** | LOC: 363
  * *Intent:* /*

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_check_conn_kind` (@ `psutil-7.2.2/psutil/__init__.py`) -> **O(2^N) [Recursive]**
- `cpu_freq` (@ `psutil-7.2.2/psutil/__init__.py`) -> **O(2^N) [Recursive]**
- `adjust_proc_create_time` (@ `psutil-7.2.2/psutil/_psbsd.py`) -> **O(2^N) [Recursive]**
- `calculate_avail_vmem` (@ `psutil-7.2.2/psutil/_pslinux.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # ===================================================================== # --- system memory # ========================================================...
- `exe` (@ `psutil-7.2.2/tests/test_process_all.py`) -> **O(2^N) [Recursive]**
- `net_if_addrs` (@ `psutil-7.2.2/psutil/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # ===================================================================== # --- CPU related functions # ================================================...
- `sensors_temperatures` (@ `psutil-7.2.2/psutil/__init__.py`) -> **O(2^N) [Recursive]**
- `__exit__` (@ `psutil-7.2.2/psutil/__init__.py`) -> **O(2^N) [Recursive]**
- `cpu_stats` (@ `psutil-7.2.2/psutil/_psbsd.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # XXX # Note about intrs: the C extension returns 0. intrs # can be determined via /proc/stat; it has the same value as # soft_intrs thought so the ke...
- `cpu_freq` (@ `psutil-7.2.2/psutil/_psbsd.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_ips` (@ `psutil-7.2.2/tests/test_linux.py`) -> DB Complexity: **266**
- `calculate_avail_vmem` (@ `psutil-7.2.2/psutil/_pslinux.py`) -> DB Complexity: **232**
  * *Intent:* # ===================================================================== # --- system memory # ========================================================...
- `is_win_secure_system_proc` (@ `psutil-7.2.2/tests/__init__.py`) -> DB Complexity: **152**
  * *Intent:* # It should show up in pids() and process_iter(). # Call all methods. ns = process_namespace(proc) for fun, name in ns.iter(ns.all, clear_cache=True):...
- `macos_version` (@ `psutil-7.2.2/tests/__init__.py`) -> DB Complexity: **97**
- `psutil_net_connections` (@ `psutil-7.2.2/psutil/arch/sunos/net.c`) -> DB Complexity: **79**
  * *Intent:* /*
- `psutil_net_connections` (@ `psutil-7.2.2/psutil/arch/windows/socks.c`) -> DB Complexity: **69**
  * *Intent:* /*
- `_check_conn_kind` (@ `psutil-7.2.2/psutil/__init__.py`) -> DB Complexity: **63**
- `test_terminate` (@ `psutil-7.2.2/tests/test_testutils.py`) -> DB Complexity: **51**
- `exe` (@ `psutil-7.2.2/psutil/_psaix.py`) -> DB Complexity: **45**
  * *Intent:* # if cwd has changed, we're out of luck - this may be wrong!
- `test_cwd_2` (@ `psutil-7.2.2/tests/test_process.py`) -> DB Complexity: **43**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `psutil-7.2.2/psutil` | 16 | 24303.22 | 18.85% | 33.38% |
| `psutil-7.2.2/tests` | 20 | 12640.52 | 6.07% | 0.0% |
| `psutil-7.2.2/psutil/arch/windows` | 19 | 4768.44 | 64.02% | 38.59% |
| `psutil-7.2.2/psutil/arch/freebsd` | 9 | 3066.88 | 73.98% | 45.89% |
| `psutil-7.2.2` | 7 | 2864.19 | 2.87% | 6.58% |
| `psutil-7.2.2/psutil/arch/sunos` | 8 | 1981.78 | 68.4% | 39.87% |
| `psutil-7.2.2/psutil/arch/osx` | 12 | 1668.08 | 65.74% | 37.98% |
| `psutil-7.2.2/psutil/arch/netbsd` | 7 | 1333.16 | 74.26% | 58.88% |
| `psutil-7.2.2/psutil/arch/aix` | 7 | 1159.92 | 38.1% | 16.16% |
| `psutil-7.2.2/psutil/arch/posix` | 7 | 995.4 | 53.52% | 48.28% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `psutil-7.2.2/psutil/_psaix.py` -> **99.999%** Exposure
- `psutil-7.2.2/psutil/arch/netbsd/cpu.c` -> **99.999%** Exposure
- `psutil-7.2.2/psutil/arch/openbsd/cpu.c` -> **99.9989%** Exposure
- `psutil-7.2.2/psutil/arch/bsd/proc.c` -> **99.9955%** Exposure
- `psutil-7.2.2/psutil/arch/windows/mem.c` -> **99.9881%** Exposure
### Highest State Flux (Mutation/Volatility)
- `psutil-7.2.2/psutil/_psutil_aix.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/aix/common.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/aix/ifaddrs.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/all/init.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/all/pids.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `psutil-7.2.2/tests/test_process.py` -> **63** Orphaned Functions | **0** Duplicates
- `psutil-7.2.2/tests/test_memleaks.py` -> **49** Orphaned Functions | **10** Duplicates
- `psutil-7.2.2/tests/test_misc.py` -> **45** Orphaned Functions | **2** Duplicates
- `psutil-7.2.2/tests/test_linux.py` -> **28** Orphaned Functions | **9** Duplicates
- `psutil-7.2.2/tests/test_system.py` -> **32** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`psutil-7.2.2/psutil/arch/all/init.h`** -> AI Confidence: **99.48%**
2. **`psutil-7.2.2/psutil/arch/bsd/disk.c`** -> AI Confidence: **99.48%**
3. **`psutil-7.2.2/psutil/arch/openbsd/socks.c`** -> AI Confidence: **99.48%**
4. **`psutil-7.2.2/psutil/arch/osx/disk.c`** -> AI Confidence: **99.48%**
5. **`psutil-7.2.2/psutil/arch/sunos/net.c`** -> AI Confidence: **99.48%**
6. **`psutil-7.2.2/psutil/arch/bsd/proc.c`** -> AI Confidence: **99.39%**
7. **`psutil-7.2.2/psutil/arch/osx/cpu.c`** -> AI Confidence: **99.39%**
8. **`psutil-7.2.2/psutil/arch/osx/proc.c`** -> AI Confidence: **99.39%**
9. **`psutil-7.2.2/psutil/arch/osx/proc_utils.c`** -> AI Confidence: **99.39%**
10. **`psutil-7.2.2/psutil/arch/windows/net.c`** -> AI Confidence: **99.34%**
11. **`psutil-7.2.2/psutil/arch/linux/init.h`** -> AI Confidence: **99.32%**
12. **`psutil-7.2.2/psutil/arch/openbsd/users.c`** -> AI Confidence: **99.32%**
13. **`psutil-7.2.2/psutil/arch/windows/proc_info.c`** -> AI Confidence: **99.32%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `psutil-7.2.2/setup.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `psutil-7.2.2/psutil/__init__.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_common.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psaix.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psbsd.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_pslinux.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `psutil-7.2.2/psutil/_psaix.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_pssunos.py` -> **100.0%** Exposure
- `psutil-7.2.2/tests/test_memleaks.py` -> **100.0%** Exposure
- `psutil-7.2.2/tests/test_windows.py` -> **100.0%** Exposure
- `psutil-7.2.2/Makefile` -> **95.1871%** Exposure
### Raw Memory Manipulation
- `psutil-7.2.2/psutil/arch/netbsd/socks.c` -> **9.993%** Exposure
- `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c` -> **9.9601%** Exposure
- `psutil-7.2.2/psutil/arch/sunos/proc.c` -> **2.471%** Exposure
- `psutil-7.2.2/psutil/arch/freebsd/proc.c` -> **1.4196%** Exposure
- `psutil-7.2.2/psutil/_psutil_aix.c` -> **0.5248%** Exposure
### Algorithmic DoS Exposure
- `psutil-7.2.2/psutil/__init__.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_common.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psaix.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psbsd.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_pslinux.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `795` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `psutil-7.2.2/psutil/_common.py` (PYTHON) -> Cumulative Risk: **857.56**
- **Archetype:** `file_cluster_13` (Distance: 12.395 IQR)
- **Magnitude:** 614.54 | **LOC:** 862 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (97.4325%)
- **Heaviest Functions:** `deprecated_method` (Impact: 134.4), `conn_to_ntuple` (Impact: 55.0), `memoize_when_activated` (Impact: 28.3)

### 2. `psutil-7.2.2/psutil/_psaix.py` (PYTHON) -> Cumulative Risk: **828.88**
- **Archetype:** `file_cluster_0` (Distance: 11.143 IQR)
- **Magnitude:** 542.26 | **LOC:** 547 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `exe` (Impact: 88.0), `disk_partitions` (Impact: 44.3), `net_connections` (Impact: 42.8)

### 3. `psutil-7.2.2/psutil/arch/netbsd/proc.c` (C) -> Cumulative Risk: **811.44**
- **Archetype:** `file_cluster_8` (Distance: 12.934 IQR)
- **Magnitude:** 304.92 | **LOC:** 291 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9996%)
- **Heaviest Functions:** `psutil_proc_threads` (Impact: 76.4), `psutil_proc_cmdline` (Impact: 70.0), `psutil_proc_num_fds` (Impact: 5.5)

### 4. `psutil-7.2.2/psutil/arch/sunos/net.c` (C) -> Cumulative Risk: **801.43**
- **Archetype:** `file_cluster_8` (Distance: 13.199 IQR)
- **Magnitude:** 782.22 | **LOC:** 567 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.4407%)
- **Heaviest Functions:** `psutil_net_connections` (Impact: 534.9)

### 5. `psutil-7.2.2/psutil/_pssunos.py` (PYTHON) -> Cumulative Risk: **789.56**
- **Archetype:** `file_cluster_0` (Distance: 10.866 IQR)
- **Magnitude:** 781.46 | **LOC:** 705 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `net_connections` (Impact: 79.3), `memory_maps` (Impact: 68.9), `disk_partitions` (Impact: 63.6)

### 6. `psutil-7.2.2/psutil/arch/windows/services.c` (C) -> Cumulative Risk: **789.55**
- **Archetype:** `file_cluster_8` (Distance: 12.266 IQR)
- **Magnitude:** 497.62 | **LOC:** 553 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Documentation (99.9956%)
- **Heaviest Functions:** `psutil_winservice_enumerate` (Impact: 42.4), `psutil_winservice_query_descr` (Impact: 40.0), `psutil_winservice_query_config` (Impact: 33.1)

### 7. `psutil-7.2.2/psutil/arch/sunos/cpu.c` (C) -> Cumulative Risk: **783.68**
- **Archetype:** `file_cluster_13` (Distance: 12.56 IQR)
- **Magnitude:** 187.56 | **LOC:** 141 | **CtrlFlow:** 84.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `psutil_per_cpu_times` (Impact: 34.9), `psutil_cpu_count_cores` (Impact: 29.6), `psutil_cpu_stats` (Impact: 21.9)

### 8. `psutil-7.2.2/psutil/arch/openbsd/proc.c` (C) -> Cumulative Risk: **777.57**
- **Archetype:** `file_cluster_13` (Distance: 12.136 IQR)
- **Magnitude:** 243.28 | **LOC:** 206 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `psutil_proc_threads` (Impact: 53.8), `psutil_proc_cmdline` (Impact: 26.2), `psutil_proc_num_fds` (Impact: 21.6)

### 9. `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c` (C) -> Cumulative Risk: **762.3**
- **Archetype:** `file_cluster_13` (Distance: 13.966 IQR)
- **Magnitude:** 1190.16 | **LOC:** 469 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.997%)
- **Heaviest Functions:** `psutil_gather_inet` (Impact: 484.8), `psutil_gather_unix` (Impact: 184.6), `psutil_net_connections` (Impact: 143.2)

### 10. `psutil-7.2.2/psutil/__init__.py` (PYTHON) -> Cumulative Risk: **761.93**
- **Archetype:** `file_cluster_13` (Distance: 12.93 IQR)
- **Magnitude:** 3563.12 | **LOC:** 2485 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (95.2878%)
- **Heaviest Functions:** `_check_conn_kind` (Impact: 2164.5), `net_if_addrs` (Impact: 168.5), `cpu_freq` (Impact: 135.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `psutil-7.2.2/psutil/_pswindows.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.039 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_0: 12.039, file_cluster_13: 12.186, file_cluster_8: 12.589
- **Magnitude:** 10147.76 | **LOC:** 1097 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.2487%), Tech Debt (23.3267%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 259`, `args: 84`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`, `dead_code: 10`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 6`, `api: 76`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 41`, `doc: 80`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.608
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.014388
  * `Imports (Out-Degree: 2):` signal, ._psutil_windows, contextlib, enum, from, threading, functools, ._common...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/_pslinux.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.989 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.883 IQR)
- **Top Global Matches:** file_cluster_0: 11.989, file_cluster_13: 12.004, file_cluster_8: 12.189
- **Magnitude:** 4902.36 | **LOC:** 2270 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 232
- **Risk Profile:** Cognitive Load (17.0407%), Tech Debt (14.6386%)
**Top Internal Functions/Classes:**
  * `calculate_avail_vmem` (Impact: 4644.0 | O(2^N) | DB: 232)
    * *Intent:* # ===================================================================== # --- system memory # ======...
  * `readlink` (Impact: 16.5 | O(2^N) | DB: 3)
  * `_scputimes_ntuple` (Impact: 13.8 | O(N^2) | DB: 3)
  * `is_storage_device` (Impact: 8.5 | O(N^2) | DB: 6)
  * `file_flags_to_mode` (Impact: 5.7 | O(N^2) | DB: 21)
    * *Intent:* """ modes_map = {os.O_RDONLY: 'r', os.O_WRONLY: 'w', os.O_RDWR: 'w+'} mode = modes_map[flags & (os.O...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 362`, `args: 91`, `func_start: 90`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 105`, `dead_code: 5`, `fragile_debt: 7`
* *Architecture:* `io: 83`, `api: 79`, `import: 40`
* *Defense:* `safety: 121`, `doc: 84`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.608
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.014388
  * `Imports (Out-Degree: 1):` collections, errno, struct, time., enum, base64, warnings, functools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.93 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.441 IQR)
- **Top Global Matches:** file_cluster_13: 12.93, file_cluster_0: 13.371, file_cluster_11: 13.448
- **Magnitude:** 3563.12 | **LOC:** 2485 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (34.6506%), Tech Debt (9.6985%)
**Top Internal Functions/Classes:**
  * `_check_conn_kind` (Impact: 2164.5 | O(2^N) | DB: 63)
  * `net_if_addrs` (Impact: 168.5 | O(2^N) | DB: 10)
    * *Intent:* # ===================================================================== # --- CPU related functions ...
  * `cpu_freq` (Impact: 135.1 | O(2^N))
  * `wait_procs` (Impact: 122.8 | O(N^5))
  * `sensors_temperatures` (Impact: 105.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 433`, `args: 105`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 148`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 87`, `concurrency: 11`, `import: 86`
* *Defense:* `safety: 114`, `doc: 166`, `test: 2`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` signal, ._psutil_windows, psutil, time, ._common, pwd, datetime, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.307 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_13: 10.307, file_cluster_8: 10.369, file_cluster_0: 10.927
- **Magnitude:** 2740.15 | **LOC:** 559 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.0035%), Tech Debt (11.5043%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 80`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 70`, `fragile_debt: 1`
* *Architecture:* `io: 31`, `api: 9`, `import: 32`
* *Defense:* `safety: 9`, `doc: 4`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` struct, tempfile, os, glob, setuptools, warnings, distutils.errors, distutils.unixccompiler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_linux.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.523 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.981 IQR)
- **Top Global Matches:** file_cluster_0: 12.523, file_cluster_13: 12.738, file_cluster_8: 12.803
- **Magnitude:** 2474.88 | **LOC:** 2290 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 266
- **Risk Profile:** Cognitive Load (6.6153%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ips` (Impact: 1441.2 | O(N^6) | DB: 266)
  * `test_emulate_multi_cpu` (Impact: 135.8 | O(N^6) | DB: 9)
  * `test_against_lscpu` (Impact: 89.4 | O(2^N) | DB: 12)
  * `test_emulate_data` (Impact: 69.0 | O(N^5) | DB: 9)
    * *Intent:* # Finally, let's make /proc/cpuinfo return meaningless data; # this way we'll fall back on relying o...
  * `test_emulate_no_scaling_cur_freq_file` (Impact: 42.6 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 758`, `args: 155`, `func_start: 154`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 18`, `dead_code: 5`, `fragile_debt: 2`, `duplicate_logic: 9`, `orphaned_logic: 28`
* *Architecture:* `io: 144`, `api: 179`, `import: 45`
* *Defense:* `safety: 341`, `doc: 40`, `test: 590`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` errno, struct, psutil._pslinux, os, psutil, time, psutil._psutil_linux, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.452 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.722 IQR)
- **Top Global Matches:** file_cluster_13: 12.452, file_cluster_0: 12.583, file_cluster_8: 12.656
- **Magnitude:** 2204.4 | **LOC:** 1737 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 152
- **Risk Profile:** Cognitive Load (8.6208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_win_secure_system_proc` (Impact: 844.5 | O(N^6) | DB: 152)
    * *Intent:* # It should show up in pids() and process_iter(). # Call all methods. ns = process_namespace(proc) f...
  * `macos_version` (Impact: 767.9 | O(2^N) | DB: 97)
  * `assert_proc_zombie` (Impact: 75.5 | O(N^5))
  * `assert_proc_gone` (Impact: 37.3 | O(N^6))
  * `safe_rmpath` (Impact: 36.3 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 346`, `args: 94`, `func_start: 93`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 45`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 106`, `api: 94`, `concurrency: 19`, `import: 48`
* *Defense:* `safety: 188`, `doc: 96`, `test: 75`, `sync_locks: 1`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` signal, errno, tempfile, pytest, psutil, ctypes, shlex, textwrap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_process.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.422 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.635 IQR)
- **Top Global Matches:** file_cluster_0: 12.422, file_cluster_13: 12.495, file_cluster_8: 12.543
- **Magnitude:** 1924.56 | **LOC:** 1843 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (6.6007%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cwd_2` (Impact: 225.8 | O(N^6) | DB: 43)
  * `test_memory_maps` (Impact: 117.5 | O(N^6) | DB: 15)
  * `test_nice` (Impact: 106.3 | O(N^6) | DB: 18)
  * `test_pid_0` (Impact: 106.2 | O(N^5))
    * *Intent:* # Process(0) is supposed to work on all platforms except Linux
  * `test_reused_pid` (Impact: 90.3 | O(N^5))
    * *Intent:* # Emulate a case where PID has been reused by another process.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 547`, `args: 101`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 16`, `planned_debt: 2`, `fragile_debt: 14`, `orphaned_logic: 63`
* *Architecture:* `io: 75`, `api: 103`, `import: 74`
* *Defense:* `safety: 325`, `doc: 8`, `test: 497`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` signal, errno, os, psutil, string, time, random, select...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_psbsd.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.057 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.581 IQR)
- **Top Global Matches:** file_cluster_13: 11.057, file_cluster_0: 11.074, file_cluster_8: 11.195
- **Magnitude:** 1448.62 | **LOC:** 905 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (12.0777%), Tech Debt (95.1612%)
**Top Internal Functions/Classes:**
  * `adjust_proc_create_time` (Impact: 956.5 | O(2^N) | DB: 15)
  * `cpu_stats` (Impact: 74.3 | O(2^N) | DB: 3)
    * *Intent:* # XXX # Note about intrs: the C extension returns 0. intrs # can be determined via /proc/stat; it ha...
  * `cpu_freq` (Impact: 63.4 | O(2^N) | DB: 1)
  * `cpu_count_cores` (Impact: 42.9 | O(N^5) | DB: 1)
    * *Intent:* # From the C module we'll get an XML string similar to this: # http://manpages.ubuntu.com/manpages/p...
  * `virtual_memory` (Impact: 38.6 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 212`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 37`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 56`, `import: 24`
* *Defense:* `safety: 37`, `doc: 50`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, collections, errno, shutil, time., functools, xml.etree, ...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.966 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.159 IQR)
- **Top Global Matches:** file_cluster_13: 13.966, file_cluster_11: 14.063, file_cluster_0: 14.208
- **Magnitude:** 1190.16 | **LOC:** 469 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (93.9315%), Tech Debt (20.0468%)
**Top Internal Functions/Classes:**
  * `psutil_gather_inet` (Impact: 484.8 | O(N^5) | DB: 38)
  * `psutil_gather_unix` (Impact: 184.6 | O(N^4) | DB: 23)
  * `psutil_net_connections` (Impact: 143.2 | O(N^4) | DB: 9)
  * `psutil_populate_xfiles` (Impact: 22.0 | O(N^3) | DB: 5)
    * *Intent:* * * Retrieves system-wide open socket connections. This is based off of * sockstat utility source co...
  * `psutil_get_file_from_sock` (Impact: 6.7 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 59`, `args: 8`, `func_start: 6`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 239`, `dead_code: 5`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 96`, `import: 14`
* *Defense:* `safety: 4`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unpcb.h, inet.h, un.h, user.h, in.h, sysctl.h, param.h, tcp_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_process_all.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.079 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.404 IQR)
- **Top Global Matches:** file_cluster_13: 13.079, file_cluster_8: 13.194, file_cluster_4: 13.424
- **Magnitude:** 974.68 | **LOC:** 542 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (16.7893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_time` (Impact: 576.4 | O(N^6) | DB: 24)
    * *Intent:* # on AIX, "<exiting>" processes don't have names
  * `exe` (Impact: 154.9 | O(2^N) | DB: 15)
  * `proc_info` (Impact: 54.3 | O(N^4))
  * `test_all` (Impact: 49.8 | O(N^6) | DB: 1)
  * `name` (Impact: 20.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 250`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4`, `planned_debt: 1`, `fragile_debt: 6`
* *Architecture:* `io: 13`, `api: 50`, `concurrency: 13`, `import: 29`
* *Defense:* `safety: 206`, `doc: 6`, `test: 133`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` traceback, errno, stat, enum, psutil, tests.test_process_all, , multiprocessing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_psutil_aix.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.801 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_8: 12.801, file_cluster_12: 13.083, file_cluster_0: 13.146
- **Magnitude:** 959.44 | **LOC:** 1074 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (89.8469%), Tech Debt (17.1098%)
**Top Internal Functions/Classes:**
  * `PyInit__psutil_aix` (Impact: 53.8 | O(N^2) | DB: 1)
  * `psutil_proc_environ` (Impact: 45.7 | O(N^4) | DB: 16)
  * `psutil_proc_threads` (Impact: 39.1 | O(N^3) | DB: 9)
  * `psutil_per_cpu_times` (Impact: 35.2 | O(N^3) | DB: 10)
  * `psutil_net_io_counters` (Impact: 33.5 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 92`, `args: 2`, `func_start: 20`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 335`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 215`
* *Defense:* `safety: 3`, `immutability_locks: 3`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inet.h, Python.h, thread.h, ifaddrs.h, mntent.h, init.h, sysinfo.h, proc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/sunos/net.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.199 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.13 IQR)
- **Top Global Matches:** file_cluster_8: 13.199, file_cluster_12: 13.333, file_cluster_11: 13.41
- **Magnitude:** 782.22 | **LOC:** 567 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 79
- **Risk Profile:** Cognitive Load (96.7658%), Tech Debt (70.7538%)
**Top Internal Functions/Classes:**
  * `psutil_net_connections` (Impact: 534.9 | O(N^5) | DB: 79)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 16`, `args: 5`, `func_start: 1`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 188`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 54`
* *Defense:* `safety: 1`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stropts.h, kstat.h, if.h, inet.h, in.h, sockio.h, mib2.h, tihdr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_pssunos.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.866 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.486 IQR)
- **Top Global Matches:** file_cluster_0: 10.866, file_cluster_13: 11.013, file_cluster_8: 11.465
- **Magnitude:** 781.46 | **LOC:** 705 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (9.8166%), Tech Debt (90.0886%)
**Top Internal Functions/Classes:**
  * `net_connections` (Impact: 79.3 | O(2^N))
  * `memory_maps` (Impact: 68.9 | O(N^6) | DB: 4)
    * *Intent:* # We may get here if we attempt to query a 64bit process # with a 32bit python. # fail in the same w...
  * `disk_partitions` (Impact: 63.6 | O(2^N) | DB: 1)
  * `_get_unix_sockets` (Impact: 53.7 | O(N^5) | DB: 12)
  * `open_files` (Impact: 43.4 | O(N^6) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 172`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 24`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 27`, `api: 62`, `import: 24`
* *Defense:* `safety: 30`, `doc: 38`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.002
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.007194
  * `Imports (Out-Degree: 1):` collections, errno, functools, socket, ._common, , os, subprocess...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/arch/freebsd/proc_socks.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.252 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.894 IQR)
- **Top Global Matches:** file_cluster_13: 13.252, file_cluster_11: 13.428, file_cluster_8: 13.502
- **Magnitude:** 746.98 | **LOC:** 415 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (83.1131%), Tech Debt (10.8687%)
**Top Internal Functions/Classes:**
  * `psutil_search_tcplist` (Impact: 285.1 | O(2^N) | DB: 10)
    * *Intent:* #if __FreeBSD_version >= 1200026
  * `psutil_proc_net_connections` (Impact: 196.2 | O(N^6) | DB: 42)
  * `psutil_fetch_tcplist` (Impact: 15.3 | O(N^3) | DB: 1)
    * *Intent:* #include <sys/user.h> #include <sys/socketvar.h> // for struct xsocket #include <sys/un.h> #include ...
  * `psutil_sockaddr_matches` (Impact: 9.7 | O(N^3))
  * `psutil_sockaddr_port` (Impact: 8.5 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 61`, `args: 10`, `func_start: 8`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 151`, `dead_code: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 57`, `import: 12`
* *Defense:* `safety: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inet.h, un.h, user.h, in.h, sysctl.h, libutil.h, param.h, tcp_var.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/netbsd/socks.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.861 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.658 IQR)
- **Top Global Matches:** file_cluster_8: 12.861, file_cluster_13: 12.89, file_cluster_11: 13.093
- **Magnitude:** 728.92 | **LOC:** 458 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (90.5864%), Tech Debt (10.9517%)
**Top Internal Functions/Classes:**
  * `psutil_get_info` (Impact: 173.8 | O(N^3))
  * `psutil_net_connections` (Impact: 136.9 | O(N^6) | DB: 23)
  * `psutil_get_sockets` (Impact: 88.3 | O(N^4) | DB: 14)
  * `psutil_get_files` (Impact: 56.3 | O(N^4) | DB: 20)
  * `psutil_kiflist_clear` (Impact: 9.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 78`, `args: 13`, `func_start: 8`, `class_start: 20`
* *Risk/State:* `state_mutation: 167`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 78`, `import: 7`
* *Defense:* `safety: 5`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inet.h, un.h, sysctl.h, queue.h, Python.h, init.h, socket.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_system.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.363 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.874 IQR)
- **Top Global Matches:** file_cluster_0: 13.363, file_cluster_13: 13.481, file_cluster_17: 13.594
- **Magnitude:** 722.62 | **LOC:** 985 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (8.662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_os_constants` (Impact: 54.4 | O(N^5) | DB: 27)
  * `test_wait_procs` (Impact: 46.2 | O(N^4) | DB: 3)
  * `test_users` (Impact: 37.3 | O(N^5))
  * `test_virtual_memory` (Impact: 37.3 | O(N^6))
  * `test_attrs` (Impact: 36.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 390`, `args: 60`, `func_start: 58`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 34`, `dead_code: 8`, `planned_debt: 2`, `orphaned_logic: 32`
* *Architecture:* `io: 41`, `api: 65`, `import: 43`
* *Defense:* `safety: 266`, `doc: 2`, `test: 318`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` signal, shutil, errno, sys, unittest, psutil._common, enum, pprint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/proc_info.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.331 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.632 IQR)
- **Top Global Matches:** file_cluster_8: 12.331, file_cluster_12: 12.674, file_cluster_7: 12.729
- **Magnitude:** 702.18 | **LOC:** 863 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (89.955%), Tech Debt (27.5627%)
**Top Internal Functions/Classes:**
  * `psutil_get_process_data` (Impact: 240.1 | O(N^5) | DB: 34)
  * `psutil_proc_cmdline` (Impact: 75.1 | O(N^4) | DB: 21)
  * `psutil_cmdline_query_proc` (Impact: 44.2 | O(N^3) | DB: 15)
  * `psutil_convert_winerr` (Impact: 5.2 | O(N^2))
  * `psutil_giveup_with_ad` (Impact: 5.2 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 18`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 213`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 101`
* *Defense:* `safety: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` windows.h, Python.h, init.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/sunos/proc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.258 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.948 IQR)
- **Top Global Matches:** file_cluster_8: 12.258, file_cluster_13: 12.448, file_cluster_11: 12.524
- **Magnitude:** 672.34 | **LOC:** 598 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (87.5307%), Tech Debt (34.8365%)
**Top Internal Functions/Classes:**
  * `psutil_proc_memory_maps` (Impact: 143.7 | O(N^6) | DB: 40)
    * *Intent:* /* * Return process memory mappings. */
  * `psutil_proc_name_and_args` (Impact: 59.6 | O(N^4) | DB: 22)
    * *Intent:* /* * Return process name and args as a Python tuple. */
  * `psutil_proc_environ` (Impact: 49.5 | O(N^3) | DB: 14)
    * *Intent:* /* * Return process environ block. */
  * `psutil_proc_cpu_num` (Impact: 24.3 | O(N^2) | DB: 30)
    * *Intent:* /* * Return what CPU the process is running on. */
  * `psutil_file_to_struct` (Impact: 13.2 | O(N^2) | DB: 20)
    * *Intent:* * Copyright (c) 2009, Giampaolo Rodola'. All rights reserved. * Use of this source code is governed ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 52`, `args: 5`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 193`, `orphaned_logic: 9`
* *Architecture:* `io: 22`, `api: 148`, `import: 4`
* *Defense:* `safety: 4`, `immutability_locks: 11`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` libproc.h, fcntl.h, Python.h, init.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_misc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.365 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.526 IQR)
- **Top Global Matches:** file_cluster_8: 12.365, file_cluster_13: 12.39, file_cluster_0: 12.473
- **Magnitude:** 636.46 | **LOC:** 868 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (5.348%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test__all__` (Impact: 62.3 | O(N^6))
  * `test_serialization` (Impact: 55.8 | O(N^5) | DB: 10)
  * `test_supports_ipv6` (Impact: 53.5 | O(N^5) | DB: 39)
  * `run_against` (Impact: 41.4 | O(N^4) | DB: 3)
  * `test_ad_on_process_creation` (Impact: 31.7 | O(N^4))
    * *Intent:* # of zombie processes or access denied. with mock.patch.object( psutil.Process, '_get_ident', side_e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 313`, `args: 60`, `func_start: 60`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 18`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 45`
* *Architecture:* `io: 23`, `api: 67`, `import: 27`
* *Defense:* `safety: 186`, `doc: 12`, `test: 251`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, collections, psutil._common, unittest, os, json, socket, pickle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_common.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.395 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_13: 12.395, file_cluster_8: 12.633, file_cluster_0: 12.649
- **Magnitude:** 614.54 | **LOC:** 862 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (15.2849%), Tech Debt (81.8156%)
**Top Internal Functions/Classes:**
  * `deprecated_method` (Impact: 134.4 | O(N^5) | DB: 17)
  * `conn_to_ntuple` (Impact: 55.0 | O(N^3) | DB: 6)
  * `memoize_when_activated` (Impact: 28.3 | O(N^4))
  * `__str__` (Impact: 26.5 | O(N^4))
  * `parse_environ_block` (Impact: 23.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 157`, `args: 48`, `func_start: 48`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 66`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 37`, `api: 47`, `concurrency: 7`, `import: 18`
* *Defense:* `safety: 57`, `doc: 70`, `test: 3`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 86.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.116547
  * `Imports (Out-Degree: 0):` collections, inspect, enum, stat, warnings, threading, functools, socket...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/arch/freebsd/proc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.906 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.313 IQR)
- **Top Global Matches:** file_cluster_8: 12.906, file_cluster_11: 13.279, file_cluster_0: 13.281
- **Magnitude:** 610.66 | **LOC:** 594 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (86.5426%), Tech Debt (43.9533%)
**Top Internal Functions/Classes:**
  * `psutil_proc_memory_maps` (Impact: 235.3 | O(N^5) | DB: 26)
    * *Intent:* // ============================================================================ // APIS // =========...
  * `psutil_proc_setrlimit` (Impact: 28.1 | O(N^3) | DB: 14)
  * `psutil_proc_cpu_affinity_get` (Impact: 27.1 | O(N^4) | DB: 5)
    * *Intent:* // we need to re-query for thread information, so don't use *kipp
  * `psutil_proc_cpu_affinity_set` (Impact: 22.4 | O(N^3) | DB: 8)
  * `psutil_proc_getrlimit` (Impact: 8.8 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 36`, `args: 1`, `func_start: 6`, `class_start: 8`
* *Risk/State:* `state_mutation: 181`, `orphaned_logic: 6`
* *Architecture:* `api: 95`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cpuset.h, user.h, sysctl.h, libutil.h, Python.h, init.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/proc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.268 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.969 IQR)
- **Top Global Matches:** file_cluster_8: 12.268, file_cluster_13: 12.412, file_cluster_11: 12.578
- **Magnitude:** 590.18 | **LOC:** 1230 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (83.7486%), Tech Debt (35.7648%)
**Top Internal Functions/Classes:**
  * `psutil_proc_threads` (Impact: 132.0 | O(N^4) | DB: 34)
    * *Intent:* #endif
  * `psutil_proc_exe` (Impact: 55.2 | O(N^4) | DB: 19)
  * `psutil_proc_wait` (Impact: 23.4 | O(N^3) | DB: 2)
  * `psutil_proc_memory_uss` (Impact: 15.9 | O(N^3) | DB: 4)
    * *Intent:* // Happens for PID 4.
  * `psutil_proc_kill` (Impact: 15.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 44`, `func_start: 10`
* *Risk/State:* `state_mutation: 183`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 127`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` signal.h, windows.h, Psapi.h, Python.h, tlhelp32.h, init.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_windows.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.089 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.417 IQR)
- **Top Global Matches:** file_cluster_13: 12.089, file_cluster_0: 12.092, file_cluster_8: 12.254
- **Magnitude:** 567.4 | **LOC:** 948 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (6.3087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_boot_time` (Impact: 205.5 | O(N^5) | DB: 15)
  * `test_disks` (Impact: 62.1 | O(N^6))
  * `wmic` (Impact: 48.6 | O(2^N))
  * `test_disk_partitions` (Impact: 21.4 | O(N^3))
  * `test_nic_names` (Impact: 21.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 293`, `args: 75`, `func_start: 75`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 19`
* *Architecture:* `io: 13`, `api: 84`, `import: 36`
* *Defense:* `safety: 134`, `doc: 12`, `test: 226`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` signal, psutil._pswindows, psutil, glob, ctypes, time, datetime, wmi...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_connections.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.841 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.218 IQR)
- **Top Global Matches:** file_cluster_13: 11.841, file_cluster_0: 12.005, file_cluster_8: 12.154
- **Magnitude:** 545.94 | **LOC:** 573 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (5.6268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_count` (Impact: 101.6 | O(N^5))
  * `test_unix` (Impact: 70.5 | O(N^4))
  * `test_it` (Impact: 37.3 | O(N^5))
    * *Intent:* # Skipped on BSD becayse by default the Python process # creates a UNIX socket to '/var/run/log'. if...
  * `compare_procsys_connections` (Impact: 34.4 | O(N^4))
  * `test_filters` (Impact: 32.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 212`, `args: 26`, `func_start: 26`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 12`, `fragile_debt: 3`, `orphaned_logic: 19`
* *Architecture:* `io: 11`, `api: 33`, `import: 36`
* *Defense:* `safety: 90`, `doc: 18`, `test: 111`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, psutil._common, textwrap, socket, psutil, , os, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_psaix.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.143 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.78 IQR)
- **Top Global Matches:** file_cluster_0: 11.143, file_cluster_13: 11.361, file_cluster_11: 11.758
- **Magnitude:** 542.26 | **LOC:** 547 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (12.0058%), Tech Debt (99.999%)
**Top Internal Functions/Classes:**
  * `exe` (Impact: 88.0 | O(2^N) | DB: 45)
    * *Intent:* # if cwd has changed, we're out of luck - this may be wrong!
  * `disk_partitions` (Impact: 44.3 | O(2^N) | DB: 1)
  * `net_connections` (Impact: 42.8 | O(2^N) | DB: 1)
  * `users` (Impact: 28.6 | O(2^N) | DB: 1)
    * *Intent:* # note: the underlying C function includes entries about # to use them in the future. if not user_pr...
  * `net_if_stats` (Impact: 27.8 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 142`, `args: 44`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 26`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 20`
* *Architecture:* `io: 28`, `api: 42`, `import: 20`
* *Defense:* `safety: 12`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` functools, ._common, glob, , os, subprocess, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `psutil-7.2.2/tests/test_posix.py` (PYTHON) | Magnitude: 511.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 289, structural_boundaries: 128, branch: 79, test: 79
- `psutil-7.2.2/psutil/_psosx.py` (PYTHON) | Magnitude: 519.14 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 317, structural_boundaries: 149, encapsulation: 69, args: 46
- `psutil-7.2.2/psutil/_pslinux.py` (PYTHON) | Magnitude: 4902.36 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1390, branch: 384, structural_boundaries: 362, encapsulation: 206
- `psutil-7.2.2/tests/test_osx.py` (PYTHON) | Magnitude: 97.74 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 79, test: 46, safety: 27
- `psutil-7.2.2/tests/test_memleaks.py` (PYTHON) | Magnitude: 351.7 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 153, test: 122, api: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `psutil-7.2.2/tests/test_windows.py` (PYTHON) | Magnitude: 567.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 658, structural_boundaries: 293, test: 226, safety: 134
- `psutil-7.2.2/psutil/_psbsd.py` (PYTHON) | Magnitude: 1448.62 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 550, structural_boundaries: 212, branch: 132, encapsulation: 87
- `psutil-7.2.2/psutil/arch/bsd/disk.c` (C) | Magnitude: 197.46 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, state_mutation: 63, branch: 50, api: 25
- `psutil-7.2.2/tests/test_heap.py` (PYTHON) | Magnitude: 248.74 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 66, test: 28, safety: 27
- `psutil-7.2.2/psutil/arch/linux/proc.c` (C) | Magnitude: 238.6 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, state_mutation: 73, api: 44, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `psutil-7.2.2/psutil/arch/posix/net.c` (C) | Magnitude: 73.8 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 27, api: 13, branch: 8
- `psutil-7.2.2/psutil/arch/posix/pids.c` (C) | Magnitude: 28.1 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, branch: 12, structural_boundaries: 9, import: 4
- `psutil-7.2.2/psutil/arch/sunos/environ.c` (C) | Magnitude: 62.84 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 24, api: 10, branch: 8
- `psutil-7.2.2/tests/test_misc.py` (PYTHON) | Magnitude: 636.46 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 645, structural_boundaries: 313, test: 251, safety: 186
- `psutil-7.2.2/psutil/arch/netbsd/socks.c` (C) | Magnitude: 728.92 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 331, state_mutation: 167, pointers: 125, branch: 118

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `psutil-7.2.2/psutil/_pswindows.py` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 39.7276%)
- `psutil-7.2.2/psutil/_pslinux.py` -> **Severity: 0.004** (Bridge: 0.0001 * Flux: 63.0212%)
- `psutil-7.2.2/psutil/_pssunos.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 43.2507%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `psutil-7.2.2/psutil/_common.py` -> **Severity: 5.545** (Embedded: 0.1165 * Error Risk: 47.5781%)
- `psutil-7.2.2/psutil/arch/windows/wmi.c` -> **Severity: 0.116** (Embedded: 0.0072 * Error Risk: 16.1764%)
- `psutil-7.2.2/psutil/_psutil_windows.c` -> **Severity: 0.107** (Embedded: 0.0162 * Error Risk: 6.6256%)
- `psutil-7.2.2/psutil/_pslinux.py` -> **Severity: 0.069** (Embedded: 0.0144 * Error Risk: 4.7663%)
- `psutil-7.2.2/psutil/arch/all/errors.c` -> **Severity: 0.068** (Embedded: 0.0072 * Error Risk: 9.4685%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `psutil-7.2.2/psutil/_common.py` -> **Severity: 8389.718** (Blast Radius: 86.108 * Doc Risk: 97.4325%)
- `psutil-7.2.2/psutil/arch/windows/ntextapi.h` -> **Severity: 2177.1** (Blast Radius: 21.771 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/arch/aix/ifaddrs.h` -> **Severity: 1655.8** (Blast Radius: 16.558 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/arch/aix/common.h` -> **Severity: 1308.3** (Blast Radius: 13.083 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/_psutil_windows.c` -> **Severity: 1107.357** (Blast Radius: 11.085 * Doc Risk: 99.8969%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
