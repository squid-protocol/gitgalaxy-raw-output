# ARCHITECTURAL_BRIEF: psutil
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/psutil` |
| **Timestamp** | `2026-08-07T05:24:59.819907+00:00` |
| **Scan Duration** | `0.65s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 134 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 97.5 | 48.4 | 57.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.8 | 57.8 | 76.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 38.0 | 25.6 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 21.0 | 2.4 | 80.0 |
| API Exposure | 0.0 | 18.2 | 11.2 | 12.2 | 0.0 |
| Concurrency Exposure | 0.0 | 63.6 | 1.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 64.8 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 11.5 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 99.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 72.4 | 98.6 | 0.0 |
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

- `calculate_avail_vmem` (@ `psutil-7.2.2/psutil/_pslinux.py`) -> Impact: **746.9** | LOC: 1947
  * *Intent:* # ===================================================================== # --- system memory # ========================================================...
- `process_unix` (@ `psutil-7.2.2/psutil/_pslinux.py`) -> Impact: **633.1** | LOC: 1347
- `test_ips` (@ `psutil-7.2.2/tests/test_linux.py`) -> Impact: **458.3** | LOC: 1302
- `_check_conn_kind` (@ `psutil-7.2.2/psutil/__init__.py`) -> Impact: **345.9** | LOC: 855
- `is_win_secure_system_proc` (@ `psutil-7.2.2/tests/__init__.py`) -> Impact: **264.3** | LOC: 644
  * *Intent:* # It should show up in pids() and process_iter(). # Call all methods. ns = process_namespace(proc) for fun, name in ns.iter(ns.all, clear_cache=True):...
- `get_procs` (@ `psutil-7.2.2/tests/__init__.py`) -> Impact: **264.1** | LOC: 641
- `create_time` (@ `psutil-7.2.2/tests/test_process_all.py`) -> Impact: **176.3** | LOC: 327
  * *Intent:* # on AIX, "<exiting>" processes don't have names
- `macos_version` (@ `psutil-7.2.2/tests/__init__.py`) -> Impact: **172.1** | LOC: 463
- `psutil_gather_inet` (@ `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c`) -> Impact: **167.3** | LOC: 171
- `adjust_proc_create_time` (@ `psutil-7.2.2/psutil/_psbsd.py`) -> Impact: **156.3** | LOC: 459

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `psutil-7.2.2/psutil` | 16 | 15895.62 | 18.6% | 40.29% |
| `psutil-7.2.2/tests` | 20 | 6172.22 | 5.95% | 0.0% |
| `psutil-7.2.2/psutil/arch/windows` | 19 | 3768.14 | 64.02% | 42.45% |
| `psutil-7.2.2` | 7 | 2864.19 | 2.78% | 6.58% |
| `psutil-7.2.2/psutil/arch/freebsd` | 9 | 1806.18 | 73.98% | 45.89% |
| `psutil-7.2.2/psutil/arch/sunos` | 8 | 1279.28 | 68.34% | 39.87% |
| `psutil-7.2.2/psutil/arch/osx` | 12 | 1244.08 | 65.68% | 37.98% |
| `psutil-7.2.2/psutil/arch/netbsd` | 7 | 915.06 | 74.26% | 58.88% |
| `psutil-7.2.2/psutil/arch/openbsd` | 8 | 729.06 | 74.78% | 57.55% |
| `psutil-7.2.2/psutil/arch/aix` | 7 | 708.82 | 38.1% | 16.16% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `psutil-7.2.2/psutil/_psaix.py` -> **99.999%** Exposure
- `psutil-7.2.2/psutil/arch/netbsd/cpu.c` -> **99.999%** Exposure
- `psutil-7.2.2/psutil/arch/openbsd/cpu.c` -> **99.9989%** Exposure
- `psutil-7.2.2/psutil/_psosx.py` -> **99.997%** Exposure
- `psutil-7.2.2/psutil/arch/bsd/proc.c` -> **99.9955%** Exposure
### Highest State Flux (Mutation/Volatility)
- `psutil-7.2.2/psutil/_psutil_aix.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/aix/common.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/aix/ifaddrs.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/all/init.c` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/all/pids.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `psutil-7.2.2/tests/test_process.py` -> **63** Orphaned Functions | **2** Duplicates
- `psutil-7.2.2/tests/test_memleaks.py` -> **49** Orphaned Functions | **12** Duplicates
- `psutil-7.2.2/tests/test_misc.py` -> **45** Orphaned Functions | **10** Duplicates
- `psutil-7.2.2/tests/test_linux.py` -> **28** Orphaned Functions | **16** Duplicates
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `795` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `psutil-7.2.2/psutil/arch/netbsd/proc.c` (C) -> Cumulative Risk: **727.64**
- **Archetype:** `file_cluster_8` (Distance: 12.901 IQR)
- **Magnitude:** 202.72 | **LOC:** 291 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9812%), Tech Debt (99.2969%)
- **Heaviest Functions:** `psutil_proc_threads` (Impact: 24.6), `psutil_proc_cmdline` (Impact: 22.6), `psutil_proc_num_fds` (Impact: 4.0)

### 2. `psutil-7.2.2/psutil/arch/windows/services.c` (C) -> Cumulative Risk: **718.12**
- **Archetype:** `file_cluster_8` (Distance: 12.266 IQR)
- **Magnitude:** 418.72 | **LOC:** 553 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (99.9709%), Tech Debt (92.7444%)
- **Heaviest Functions:** `psutil_winservice_query_config` (Impact: 23.6), `psutil_winservice_enumerate` (Impact: 23.4), `psutil_winservice_query_descr` (Impact: 21.9)

### 3. `psutil-7.2.2/psutil/arch/openbsd/proc.c` (C) -> Cumulative Risk: **708.47**
- **Archetype:** `file_cluster_13` (Distance: 12.136 IQR)
- **Magnitude:** 183.28 | **LOC:** 206 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9943%), Cognitive Load (89.759%)
- **Heaviest Functions:** `psutil_proc_threads` (Impact: 23.8), `psutil_proc_cmdline` (Impact: 14.2), `psutil_proc_num_fds` (Impact: 9.6)

### 4. `psutil-7.2.2/psutil/arch/sunos/net.c` (C) -> Cumulative Risk: **701.73**
- **Archetype:** `file_cluster_8` (Distance: 13.112 IQR)
- **Magnitude:** 362.62 | **LOC:** 567 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.7658%), Documentation (96.2498%)
- **Heaviest Functions:** `psutil_net_connections` (Impact: 115.3)

### 5. `psutil-7.2.2/psutil/arch/freebsd/proc.c` (C) -> Cumulative Risk: **668.48**
- **Archetype:** `file_cluster_8` (Distance: 12.9 IQR)
- **Magnitude:** 383.56 | **LOC:** 594 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9768%), Safety Score (93.7199%)
- **Heaviest Functions:** `psutil_proc_memory_maps` (Impact: 50.6), `psutil_proc_setrlimit` (Impact: 15.2), `psutil_proc_cpu_affinity_set` (Impact: 12.4)

### 6. `psutil-7.2.2/psutil/arch/windows/proc.c` (C) -> Cumulative Risk: **664.33**
- **Archetype:** `file_cluster_8` (Distance: 12.264 IQR)
- **Magnitude:** 485.98 | **LOC:** 1230 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (99.492%), Safety Score (85.7439%)
- **Heaviest Functions:** `psutil_proc_threads` (Impact: 58.5), `psutil_proc_exe` (Impact: 25.2), `psutil_proc_memory_maps` (Impact: 21.8)

### 7. `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c` (C) -> Cumulative Risk: **662.77**
- **Archetype:** `file_cluster_13` (Distance: 13.932 IQR)
- **Magnitude:** 643.56 | **LOC:** 469 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9655%), Cognitive Load (93.9315%)
- **Heaviest Functions:** `psutil_gather_inet` (Impact: 167.3), `psutil_gather_unix` (Impact: 77.3), `psutil_net_connections` (Impact: 36.6)

### 8. `psutil-7.2.2/psutil/arch/windows/init.c` (C) -> Cumulative Risk: **661.39**
- **Archetype:** `file_cluster_8` (Distance: 12.139 IQR)
- **Magnitude:** 244.02 | **LOC:** 320 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.346%), Safety Score (88.8372%)
- **Heaviest Functions:** `psutil_loadlibs` (Impact: 19.7), `PyErr_SetFromWindowsErrWithFilename` (Impact: 17.3), `psutil_set_winver` (Impact: 17.2)

### 9. `psutil-7.2.2/psutil/arch/aix/ifaddrs.c` (C) -> Cumulative Risk: **655.93**
- **Archetype:** `file_cluster_13` (Distance: 13.505 IQR)
- **Magnitude:** 196.32 | **LOC:** 152 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9159%), Cognitive Load (97.4795%)
- **Heaviest Functions:** `getifaddrs` (Impact: 77.0), `sa_dup` (Impact: 4.5), `freeifaddrs` (Impact: 4.5)

### 10. `psutil-7.2.2/psutil/arch/windows/proc_info.c` (C) -> Cumulative Risk: **653.07**
- **Archetype:** `file_cluster_8` (Distance: 12.337 IQR)
- **Magnitude:** 519.88 | **LOC:** 863 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.2759%), Cognitive Load (89.955%)
- **Heaviest Functions:** `psutil_get_process_data` (Impact: 90.1), `psutil_proc_cmdline` (Impact: 34.6), `psutil_cmdline_query_proc` (Impact: 24.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `psutil-7.2.2/psutil/_pswindows.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.039 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_0: 12.039, file_cluster_13: 12.186, file_cluster_8: 12.589
- **Magnitude:** 10147.76 | **LOC:** 1097 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2487%), Tech Debt (23.3267%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 259`, `args: 84`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`, `dead_code: 10`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 6`, `api: 76`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 41`, `doc: 80`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.608
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.014388
  * `Imports (Out-Degree: 2):` functools, time, ._common, signal, contextlib, threading, , ._psutil_windows...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.307 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_13: 10.307, file_cluster_8: 10.369, file_cluster_0: 10.927
- **Magnitude:** 2740.15 | **LOC:** 559 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4128%), Tech Debt (11.5043%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 80`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 70`, `fragile_debt: 1`
* *Architecture:* `io: 31`, `api: 9`, `import: 32`
* *Defense:* `safety: 9`, `doc: 4`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` distutils.core, io, warnings, setuptools, distutils.errors, contextlib, subprocess, _common.py...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_pslinux.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.996 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.883 IQR)
- **Top Global Matches:** file_cluster_0: 11.996, file_cluster_13: 12.01, file_cluster_8: 12.197
- **Magnitude:** 1626.96 | **LOC:** 2270 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.1352%), Tech Debt (14.6386%)
**Top Internal Functions/Classes:**
  * `calculate_avail_vmem` (Impact: 746.9)
    * *Intent:* # ===================================================================== # --- system memory # ======...
  * `process_unix` (Impact: 633.1)
  * `_scputimes_ntuple` (Impact: 9.5)
  * `readlink` (Impact: 6.1)
  * `is_storage_device` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 362`, `args: 91`, `func_start: 90`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 105`, `dead_code: 5`, `fragile_debt: 7`
* *Architecture:* `io: 83`, `api: 81`, `import: 40`
* *Defense:* `safety: 121`, `doc: 84`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.608
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.014388
  * `Imports (Out-Degree: 1):` time., functools, resource, base64, re, ._common, , warnings...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/tests/test_linux.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.525 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.974 IQR)
- **Top Global Matches:** file_cluster_0: 12.525, file_cluster_13: 12.739, file_cluster_8: 12.808
- **Magnitude:** 1093.28 | **LOC:** 2290 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.5424%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ips` (Impact: 458.3)
  * `test_emulate_multi_cpu` (Impact: 40.6)
  * `open_mock` (Impact: 31.5)
  * `test_emulate_data` (Impact: 24.0)
    * *Intent:* # Finally, let's make /proc/cpuinfo return meaningless data; # this way we'll fall back on relying o...
  * `test_against_lscpu` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 758`, `args: 158`, `func_start: 154`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 18`, `dead_code: 5`, `fragile_debt: 2`, `duplicate_logic: 16`, `orphaned_logic: 28`
* *Architecture:* `io: 144`, `api: 179`, `import: 45`
* *Defense:* `safety: 341`, `doc: 40`, `test: 590`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` io, warnings, errno, collections, fcntl, time, psutil._psutil_linux, platform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.453 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_13: 12.453, file_cluster_0: 12.584, file_cluster_8: 12.657
- **Magnitude:** 1080.9 | **LOC:** 1737 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.6039%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_win_secure_system_proc` (Impact: 264.3)
    * *Intent:* # It should show up in pids() and process_iter(). # Call all methods. ns = process_namespace(proc) f...
  * `get_procs` (Impact: 264.1)
  * `macos_version` (Impact: 172.1)
  * `assert_proc_zombie` (Impact: 27.0)
  * `kernel_version` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 346`, `args: 95`, `func_start: 93`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 45`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 106`, `api: 94`, `concurrency: 19`, `import: 48`
* *Defense:* `safety: 188`, `doc: 96`, `test: 75`, `sync_locks: 1`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` functools, warnings, errno, random, psutil._common, atexit, select, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.9 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.418 IQR)
- **Top Global Matches:** file_cluster_13: 12.9, file_cluster_0: 13.34, file_cluster_11: 13.423
- **Magnitude:** 1046.72 | **LOC:** 2485 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.3061%), Tech Debt (47.985%)
**Top Internal Functions/Classes:**
  * `_check_conn_kind` (Impact: 345.9)
  * `wait_procs` (Impact: 42.9)
  * `net_if_addrs` (Impact: 29.9)
    * *Intent:* # ===================================================================== # --- CPU related functions ...
  * `cpu_percent` (Impact: 28.1)
  * `cpu_times_percent` (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 433`, `args: 106`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 144`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 14`, `api: 87`, `concurrency: 11`, `import: 86`
* *Defense:* `safety: 114`, `doc: 166`, `test: 2`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` time., functools, datetime, collections, psutil._common, time, ._pslinux, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_process.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.423 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.627 IQR)
- **Top Global Matches:** file_cluster_0: 12.423, file_cluster_13: 12.497, file_cluster_8: 12.546
- **Magnitude:** 870.96 | **LOC:** 1843 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6007%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cwd_2` (Impact: 70.0)
  * `test_pid_0` (Impact: 36.9)
    * *Intent:* # Process(0) is supposed to work on all platforms except Linux
  * `test_memory_maps` (Impact: 35.3)
  * `test_nice` (Impact: 32.7)
  * `test_reused_pid` (Impact: 31.4)
    * *Intent:* # Emulate a case where PID has been reused by another process.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 547`, `args: 104`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 16`, `planned_debt: 2`, `fragile_debt: 14`, `duplicate_logic: 2`, `orphaned_logic: 63`
* *Architecture:* `io: 75`, `api: 103`, `import: 74`
* *Defense:* `safety: 325`, `doc: 8`, `test: 497`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` io, itertools, errno, collections, random, psutil._common, select, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_psutil_aix.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.799 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.795 IQR)
- **Top Global Matches:** file_cluster_8: 12.799, file_cluster_12: 13.081, file_cluster_0: 13.144
- **Magnitude:** 795.94 | **LOC:** 1074 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.8469%), Tech Debt (17.1098%)
**Top Internal Functions/Classes:**
  * `PyInit__psutil_aix` (Impact: 36.8)
  * `psutil_proc_threads` (Impact: 21.1)
  * `psutil_proc_environ` (Impact: 20.2)
  * `psutil_per_cpu_times` (Impact: 19.2)
  * `psutil_net_io_counters` (Impact: 18.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 92`, `args: 1`, `func_start: 20`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 335`, `fragile_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 215`
* *Defense:* `safety: 3`, `immutability_locks: 3`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` socket.h, stat.h, ifaddrs.h, stropts.h, mntent.h, init.h, types.h, net_connections.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.932 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.157 IQR)
- **Top Global Matches:** file_cluster_13: 13.932, file_cluster_11: 14.03, file_cluster_0: 14.175
- **Magnitude:** 643.56 | **LOC:** 469 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.9315%), Tech Debt (20.0468%)
**Top Internal Functions/Classes:**
  * `psutil_gather_inet` (Impact: 167.3)
  * `psutil_gather_unix` (Impact: 77.3)
  * `psutil_net_connections` (Impact: 36.6)
  * `psutil_populate_xfiles` (Impact: 11.6)
    * *Intent:* * * Retrieves system-wide open socket connections. This is based off of * sockstat utility source co...
  * `psutil_int_in_seq` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 59`, `args: 4`, `func_start: 6`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 239`, `dead_code: 5`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 96`, `import: 14`
* *Defense:* `safety: 4`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ip.h, socketvar.h, unpcb.h, in.h, tcp_var.h, init.h, user.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/proc_info.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.337 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.632 IQR)
- **Top Global Matches:** file_cluster_8: 12.337, file_cluster_12: 12.678, file_cluster_7: 12.734
- **Magnitude:** 519.88 | **LOC:** 863 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.955%), Tech Debt (34.085%)
**Top Internal Functions/Classes:**
  * `psutil_get_process_data` (Impact: 90.1)
  * `psutil_proc_cmdline` (Impact: 34.6)
  * `psutil_cmdline_query_proc` (Impact: 24.2)
  * `psutil_get_proc_info` (Impact: 21.1)
  * `psutil_proc_info` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 18`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 213`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 101`
* *Defense:* `safety: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` windows.h, init.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/sunos/proc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.258 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.948 IQR)
- **Top Global Matches:** file_cluster_8: 12.258, file_cluster_13: 12.448, file_cluster_11: 12.524
- **Magnitude:** 499.14 | **LOC:** 598 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.0937%), Tech Debt (34.8365%)
**Top Internal Functions/Classes:**
  * `psutil_proc_memory_maps` (Impact: 46.1)
    * *Intent:* /* * Return process memory mappings. */
  * `psutil_proc_name_and_args` (Impact: 26.6)
    * *Intent:* /* * Return process name and args as a Python tuple. */
  * `psutil_proc_environ` (Impact: 26.5)
    * *Intent:* /* * Return process environ block. */
  * `psutil_proc_cpu_num` (Impact: 17.3)
    * *Intent:* /* * Return what CPU the process is running on. */
  * `psutil_file_to_struct` (Impact: 9.2)
    * *Intent:* * Copyright (c) 2009, Giampaolo Rodola'. All rights reserved. * Use of this source code is governed ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 52`, `args: 5`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 193`, `orphaned_logic: 9`
* *Architecture:* `io: 22`, `api: 148`, `import: 4`
* *Defense:* `safety: 4`, `immutability_locks: 11`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fcntl.h, libproc.h, init.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/proc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.264 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.973 IQR)
- **Top Global Matches:** file_cluster_8: 12.264, file_cluster_13: 12.409, file_cluster_11: 12.576
- **Magnitude:** 485.98 | **LOC:** 1230 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.7486%), Tech Debt (46.6268%)
**Top Internal Functions/Classes:**
  * `psutil_proc_threads` (Impact: 58.5)
    * *Intent:* #endif
  * `psutil_proc_exe` (Impact: 25.2)
  * `psutil_proc_memory_maps` (Impact: 21.8)
    * *Intent:* /* * Returns the USS of the process. * Reference: * https://dxr.mozilla.org/mozilla-central/source/x...
  * `psutil_ppid_map` (Impact: 14.2)
  * `psutil_proc_wait` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 44`, `func_start: 10`
* *Risk/State:* `state_mutation: 181`, `dead_code: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 127`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` init.h, tlhelp32.h, signal.h, windows.h, Psapi.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/netbsd/socks.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.816 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.651 IQR)
- **Top Global Matches:** file_cluster_8: 12.816, file_cluster_13: 12.845, file_cluster_11: 13.049
- **Magnitude:** 460.32 | **LOC:** 458 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.5864%), Tech Debt (10.9517%)
**Top Internal Functions/Classes:**
  * `psutil_get_info` (Impact: 89.0)
  * `psutil_net_connections` (Impact: 44.4)
  * `psutil_get_sockets` (Impact: 37.4)
  * `psutil_get_files` (Impact: 24.5)
  * `psutil_kiflist_clear` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 78`, `args: 7`, `func_start: 8`, `class_start: 20`
* *Risk/State:* `state_mutation: 167`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 78`, `import: 7`
* *Defense:* `safety: 5`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` init.h, socket.h, inet.h, queue.h, un.h, sysctl.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_common.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.391 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_13: 12.391, file_cluster_8: 12.63, file_cluster_0: 12.645
- **Magnitude:** 422.74 | **LOC:** 862 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.2849%), Tech Debt (92.2761%)
**Top Internal Functions/Classes:**
  * `deprecated_method` (Impact: 51.3)
  * `outer` (Impact: 45.3)
  * `conn_to_ntuple` (Impact: 28.0)
  * `memoize_when_activated` (Impact: 12.7)
  * `__str__` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 157`, `args: 48`, `func_start: 48`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 66`, `dead_code: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 37`, `api: 47`, `concurrency: 7`, `import: 18`
* *Defense:* `safety: 57`, `doc: 70`, `test: 3`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 86.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.116547
  * `Imports (Out-Degree: 0):` functools, stat, ipaddress, threading, , warnings, inspect, sys...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/arch/windows/services.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.266 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.556 IQR)
- **Top Global Matches:** file_cluster_8: 12.266, file_cluster_13: 12.36, file_cluster_11: 12.436
- **Magnitude:** 418.72 | **LOC:** 553 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.4605%), Tech Debt (92.7444%)
**Top Internal Functions/Classes:**
  * `psutil_winservice_query_config` (Impact: 23.6)
  * `psutil_winservice_enumerate` (Impact: 23.4)
    * *Intent:* // ==================================================================
  * `psutil_winservice_query_descr` (Impact: 21.9)
  * `psutil_winservice_query_status` (Impact: 17.7)
  * `get_state_string` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 38`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 167`, `dead_code: 2`, `fragile_debt: 5`, `orphaned_logic: 6`
* *Architecture:* `api: 114`, `import: 4`
* *Defense:* `immutability_locks: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` windows.h, Winsvc.h, init.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_process_all.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.08 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.404 IQR)
- **Top Global Matches:** file_cluster_13: 13.08, file_cluster_8: 13.195, file_cluster_4: 13.424
- **Magnitude:** 384.58 | **LOC:** 542 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_time` (Impact: 176.3)
    * *Intent:* # on AIX, "<exiting>" processes don't have names
  * `proc_info` (Impact: 23.1)
  * `exe` (Impact: 22.9)
  * `check` (Impact: 20.5)
  * `test_all` (Impact: 15.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 250`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4`, `planned_debt: 1`, `fragile_debt: 6`
* *Architecture:* `io: 13`, `api: 50`, `concurrency: 13`, `import: 29`
* *Defense:* `safety: 206`, `doc: 6`, `test: 133`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` multiprocessing, stat, time, psutil, , errno, tests.test_process_all, enum...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/proc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.9 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.319 IQR)
- **Top Global Matches:** file_cluster_8: 12.9, file_cluster_11: 13.275, file_cluster_0: 13.277
- **Magnitude:** 383.56 | **LOC:** 594 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.5426%), Tech Debt (43.9533%)
**Top Internal Functions/Classes:**
  * `psutil_proc_memory_maps` (Impact: 50.6)
    * *Intent:* // ============================================================================ // APIS // =========...
  * `psutil_proc_setrlimit` (Impact: 15.2)
  * `psutil_proc_cpu_affinity_set` (Impact: 12.4)
  * `psutil_proc_cpu_affinity_get` (Impact: 12.1)
    * *Intent:* // we need to re-query for thread information, so don't use *kipp
  * `psutil_proc_getrlimit` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 36`, `func_start: 6`, `class_start: 8`
* *Risk/State:* `state_mutation: 181`, `orphaned_logic: 6`
* *Architecture:* `api: 95`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` init.h, cpuset.h, user.h, libutil.h, sysctl.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/ntextapi.h` (C | Tier 1.5 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.547 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.182 IQR)
- **Top Global Matches:** file_cluster_8: 7.547, file_cluster_7: 8.508, file_cluster_1: 8.774
- **Magnitude:** 382.58 | **LOC:** 716 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1934%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 71`, `class_start: 36`
* *Risk/State:* None
* *Architecture:* `api: 356`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.771
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021583
  * `Imports (Out-Degree: 0):` winternl.h, iphlpapi.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/_psbsd.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.057 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.581 IQR)
- **Top Global Matches:** file_cluster_13: 11.057, file_cluster_0: 11.074, file_cluster_8: 11.195
- **Magnitude:** 377.42 | **LOC:** 905 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0777%), Tech Debt (95.1612%)
**Top Internal Functions/Classes:**
  * `adjust_proc_create_time` (Impact: 156.3)
  * `cpu_count_cores` (Impact: 15.2)
    * *Intent:* # From the C module we'll get an XML string similar to this: # http://manpages.ubuntu.com/manpages/p...
  * `virtual_memory` (Impact: 14.4)
  * `cpu_stats` (Impact: 13.7)
    * *Intent:* # XXX # Note about intrs: the C extension returns 0. intrs # can be determined via /proc/stat; it ha...
  * `cpu_freq` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 212`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 37`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 56`, `import: 24`
* *Defense:* `safety: 37`, `doc: 50`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` time., functools, ._common, shutil, xml.etree, contextlib, , errno...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_system.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.363 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.874 IQR)
- **Top Global Matches:** file_cluster_0: 13.363, file_cluster_13: 13.481, file_cluster_17: 13.594
- **Magnitude:** 371.42 | **LOC:** 985 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_wait_procs` (Impact: 20.2)
  * `test_os_constants` (Impact: 19.7)
  * `test_attrs` (Impact: 15.2)
  * `test_users` (Impact: 13.0)
  * `test_virtual_memory` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 390`, `args: 60`, `func_start: 58`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 34`, `dead_code: 8`, `planned_debt: 2`, `orphaned_logic: 32`
* *Architecture:* `io: 41`, `api: 65`, `import: 43`
* *Defense:* `safety: 266`, `doc: 2`, `test: 318`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` time, psutil, datetime, shutil, signal, pprint, unittest, ...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_misc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.32 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.501 IQR)
- **Top Global Matches:** file_cluster_8: 12.32, file_cluster_13: 12.348, file_cluster_0: 12.43
- **Magnitude:** 369.16 | **LOC:** 868 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2451%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_serialization` (Impact: 21.2)
  * `test__all__` (Impact: 19.0)
  * `test_supports_ipv6` (Impact: 18.9)
  * `run_against` (Impact: 17.4)
  * `test_ad_on_process_creation` (Impact: 13.5)
    * *Intent:* # of zombie processes or access denied. with mock.patch.object( psutil.Process, '_get_ident', side_e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 313`, `args: 60`, `func_start: 60`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 16`, `fragile_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 45`
* *Architecture:* `io: 23`, `api: 67`, `import: 27`
* *Defense:* `safety: 186`, `doc: 12`, `test: 251`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` psutil, io, , contextlib, unittest, collections, psutil._common, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/sunos/net.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.112 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.138 IQR)
- **Top Global Matches:** file_cluster_8: 13.112, file_cluster_12: 13.25, file_cluster_11: 13.333
- **Magnitude:** 362.62 | **LOC:** 567 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.7658%), Tech Debt (70.7538%)
**Top Internal Functions/Classes:**
  * `psutil_net_connections` (Impact: 115.3)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 16`, `func_start: 1`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 188`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 54`
* *Defense:* `safety: 1`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mib2.h, types.h, kstat.h, in.h, socket.h, init.h, if.h, stropts.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/proc_socks.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.23 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.89 IQR)
- **Top Global Matches:** file_cluster_13: 13.23, file_cluster_11: 13.406, file_cluster_8: 13.48
- **Magnitude:** 361.18 | **LOC:** 415 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.1131%), Tech Debt (10.8687%)
**Top Internal Functions/Classes:**
  * `psutil_proc_net_connections` (Impact: 63.6)
  * `psutil_search_tcplist` (Impact: 51.3)
    * *Intent:* #if __FreeBSD_version >= 1200026
  * `psutil_fetch_tcplist` (Impact: 8.2)
    * *Intent:* #include <sys/user.h> #include <sys/socketvar.h> // for struct xsocket #include <sys/un.h> #include ...
  * `psutil_sockaddr_port` (Impact: 5.9)
  * `psutil_sockaddr_addr` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 61`, `args: 7`, `func_start: 8`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 151`, `dead_code: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 57`, `import: 12`
* *Defense:* `safety: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` socketvar.h, tcp_var.h, in.h, init.h, user.h, inet.h, param.h, in_pcb.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_pssunos.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.867 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.486 IQR)
- **Top Global Matches:** file_cluster_0: 10.867, file_cluster_13: 11.014, file_cluster_8: 11.465
- **Magnitude:** 352.26 | **LOC:** 705 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.931%), Tech Debt (90.0886%)
**Top Internal Functions/Classes:**
  * `memory_maps` (Impact: 21.3)
    * *Intent:* # We may get here if we attempt to query a 64bit process # with a 32bit python. # fail in the same w...
  * `_get_unix_sockets` (Impact: 19.0)
  * `net_connections` (Impact: 16.9)
  * `threads` (Impact: 15.5)
    * *Intent:* # with a 32bit python. # Error originates from read() and also tools like "cat" # fail in the same w...
  * `open_files` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 172`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 24`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 27`, `api: 62`, `import: 24`
* *Defense:* `safety: 30`, `doc: 38`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.002
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.007194
  * `Imports (Out-Degree: 1):` functools, ._common, , errno, collections, subprocess, sys, socket...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/arch/windows/socks.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.574 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.3 IQR)
- **Top Global Matches:** file_cluster_8: 12.574, file_cluster_12: 12.909, file_cluster_7: 12.967
- **Magnitude:** 345.46 | **LOC:** 465 | **CtrlFlow:** 88.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.7989%), Tech Debt (11.704%)
**Top Internal Functions/Classes:**
  * `psutil_net_connections` (Impact: 111.2)
    * *Intent:* /*
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 6`
* *Risk/State:* `state_mutation: 175`, `orphaned_logic: 1`
* *Architecture:* `api: 53`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` windows.h, ws2tcpip.h, init.h, Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `psutil-7.2.2/tests/test_posix.py` (PYTHON) | Magnitude: 244.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 289, structural_boundaries: 128, branch: 79, test: 79
- `psutil-7.2.2/psutil/_pslinux.py` (PYTHON) | Magnitude: 1626.96 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1390, branch: 384, structural_boundaries: 362, encapsulation: 206
- `psutil-7.2.2/tests/test_osx.py` (PYTHON) | Magnitude: 65.54 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 79, test: 46, safety: 27
- `psutil-7.2.2/psutil/_psosx.py` (PYTHON) | Magnitude: 274.74 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 317, structural_boundaries: 149, encapsulation: 69, args: 46
- `psutil-7.2.2/tests/test_memleaks.py` (PYTHON) | Magnitude: 247.5 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 153, test: 122, args: 108

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `psutil-7.2.2/tests/test_windows.py` (PYTHON) | Magnitude: 300.5 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 658, structural_boundaries: 293, test: 226, safety: 134
- `psutil-7.2.2/psutil/_psbsd.py` (PYTHON) | Magnitude: 377.42 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 550, structural_boundaries: 212, branch: 132, encapsulation: 87
- `psutil-7.2.2/psutil/arch/bsd/disk.c` (C) | Magnitude: 148.36 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, state_mutation: 63, branch: 50, api: 25
- `psutil-7.2.2/tests/test_heap.py` (PYTHON) | Magnitude: 90.54 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 66, test: 28, safety: 27
- `psutil-7.2.2/psutil/arch/linux/proc.c` (C) | Magnitude: 163.9 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, state_mutation: 73, api: 44, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `psutil-7.2.2/psutil/arch/posix/pids.c` (C) | Magnitude: 23.6 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, branch: 12, structural_boundaries: 9, import: 4
- `psutil-7.2.2/psutil/arch/sunos/environ.c` (C) | Magnitude: 49.94 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 24, api: 10, branch: 8
- `psutil-7.2.2/psutil/arch/posix/net.c` (C) | Magnitude: 51.6 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 27, api: 13, branch: 8
- `psutil-7.2.2/tests/test_misc.py` (PYTHON) | Magnitude: 369.16 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 645, structural_boundaries: 313, test: 251, safety: 186
- `psutil-7.2.2/psutil/arch/netbsd/socks.c` (C) | Magnitude: 460.32 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
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

- `psutil-7.2.2/psutil/_common.py` -> **Severity: 5.226** (Embedded: 0.1165 * Error Risk: 44.8445%)
- `psutil-7.2.2/psutil/_psutil_windows.c` -> **Severity: 0.916** (Embedded: 0.0162 * Error Risk: 56.6049%)
- `psutil-7.2.2/psutil/_pslinux.py` -> **Severity: 0.642** (Embedded: 0.0144 * Error Risk: 44.6246%)
- `psutil-7.2.2/psutil/_pswindows.py` -> **Severity: 0.569** (Embedded: 0.0144 * Error Risk: 39.5786%)
- `psutil-7.2.2/psutil/arch/windows/wmi.c` -> **Severity: 0.528** (Embedded: 0.0072 * Error Risk: 73.4218%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `psutil-7.2.2/psutil/_common.py` -> **Severity: 3874.55** (Blast Radius: 86.108 * Doc Risk: 44.9964%)
- `psutil-7.2.2/psutil/arch/windows/ntextapi.h` -> **Severity: 2177.1** (Blast Radius: 21.771 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/arch/aix/ifaddrs.h` -> **Severity: 1655.086** (Blast Radius: 16.558 * Doc Risk: 99.9569%)
- `psutil-7.2.2/psutil/arch/aix/common.h` -> **Severity: 1306.909** (Blast Radius: 13.083 * Doc Risk: 99.8937%)
- `psutil-7.2.2/psutil/_psutil_windows.c` -> **Severity: 1105.581** (Blast Radius: 11.085 * Doc Risk: 99.7367%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
