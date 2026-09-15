# ARCHITECTURAL_BRIEF: psutil
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 150 |
| Analyzed Artifacts (Scanned) | 138 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12 |
| Total LOC | 32725 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4558 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5924 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9821 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 102 | 16192 | 73.9% |
| PYTHON | 30 | 16278 | 21.7% |
| MARKDOWN | 3 | 0 | 2.2% |
| PLAINTEXT | 2 | 0 | 1.4% |
| MAKEFILE | 1 | 255 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z +0.41; from the repo's file-archetype mix)
> **File Composition:** Compute Cores Files 20%, Many-Argument Workhorses Files 17%, Defensive Guards Files 16%, Large Core Modules 16%, Declarative / Non-Code 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 133 | 96.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Zero-Density Threshold (LOC: 52, Signals: 0)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.jsonc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 1x Packed Payload Guard (Impossible Density: 3.32 hits/line)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.1 | 47.8 | 50.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.1 | 63.7 | 80.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 40.7 | 35.6 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 26.0 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.5 | 5.3 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 60.3 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 65.4 | 100.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.5 | 1.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 81.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4011 | 129 | 81 | `psutil-7.2.2/psutil/arch/windows/init.h` |
| cleanup | 264 | 52 | 7 | `psutil-7.2.2/psutil/_psutil_aix.c` |
| guards | 3085 | 102 | 53 | `psutil-7.2.2/tests/test_linux.py` |
| danger | 737 | 67 | 15 | `psutil-7.2.2/psutil/_pslinux.py` |
| concurrency | 85 | 18 | 1 | `psutil-7.2.2/tests/__init__.py` |
| connectivity | 2055 | 132 | 46 | `psutil-7.2.2/tests/test_linux.py` |
| io | 769 | 35 | 13 | `psutil-7.2.2/tests/test_linux.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 101 | 25 | 2 | `psutil-7.2.2/tests/__init__.py` |
| time | 71 | 14 | 0 | `psutil-7.2.2/tests/test_process.py` |
| serialization | 7 | 3 | 0 | `psutil-7.2.2/tests/test_misc.py` |
| regex | 51 | 10 | 0 | `psutil-7.2.2/tests/test_linux.py` |
| events | 19 | 2 | 0 | `psutil-7.2.2/tests/test_system.py` |
| tests | 1456 | 21 | 13 | `psutil-7.2.2/tests/test_linux.py` |
| docs | 520 | 31 | 9 | `psutil-7.2.2/psutil/__init__.py` |
| debt | 150 | 46 | 4 | `psutil-7.2.2/tests/test_process.py` |
| mutation | 10519 | 115 | 202 | `psutil-7.2.2/psutil/_pslinux.py` |
| dead_code | 1010 | 116 | 23 | `psutil-7.2.2/tests/test_linux.py` |
| credential | 0 | 0 | 0 | - |
| threat | 757 | 78 | 14 | `psutil-7.2.2/psutil/_psutil_aix.c` |
| ml_ai | 16 | 8 | 0 | `psutil-7.2.2/psutil/arch/freebsd/proc_socks.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0454**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `psutil-7.2.2/tests/test_linux.py` (Hits: 144)
- `psutil-7.2.2/tests/__init__.py` (Hits: 100)
- `psutil-7.2.2/psutil/_pslinux.py` (Hits: 83)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **init.h** (`psutil-7.2.2/psutil/arch/all/init.h`) — 83 inbound connections
2. **_common.py** (`psutil-7.2.2/psutil/_common.py`) — 16 inbound connections
3. **common.h** (`psutil-7.2.2/psutil/arch/aix/common.h`) — 3 inbound connections
4. **ifaddrs.h** (`psutil-7.2.2/psutil/arch/aix/ifaddrs.h`) — 3 inbound connections
5. **ntextapi.h** (`psutil-7.2.2/psutil/arch/windows/ntextapi.h`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`psutil-7.2.2/tests/__init__.py`) — 33 outbound dependencies
2. **_psutil_aix.c** (`psutil-7.2.2/psutil/_psutil_aix.c`) — 25 outbound dependencies
3. **test_process.py** (`psutil-7.2.2/tests/test_process.py`) — 24 outbound dependencies
4. **__init__.py** (`psutil-7.2.2/psutil/__init__.py`) — 21 outbound dependencies
5. **test_windows.py** (`psutil-7.2.2/tests/test_windows.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `psutil_net_connections` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/windows/socks.c`) -> Impact: **139.4** | LOC: 363
  * *Intent:* /* * Return a list of network connections opened by a process */
- `psutil_net_connections` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/sunos/net.c`) -> Impact: **134.8** | LOC: 306
  * *Intent:* /* * Return TCP and UDP connections opened by process. * UNIX sockets are excluded. * * Thanks to: * https://github.com/DavidGriffith/finx/blob/master...
- `psutil_get_process_data` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/windows/proc_info.c`) -> Impact: **126.4** | LOC: 336
  * *Intent:* /* * Get data from the process with the given pid. The data is returned * in the pdata output member as a nul terminated string which must be * freed ...
- `psutil_search_tcplist` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/freebsd/proc_socks.c`) -> Impact: **120.9** | LOC: 305
  * *Intent:* #if __FreeBSD_version >= 1200026
- `psutil_gather_inet` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c`) -> Impact: **117.0** | LOC: 171
  * *Intent:* // Reference: // https://github.com/freebsd/freebsd/blob/master/usr.bin/sockstat/sockstat.c
- `psutil_get_nic_speed` **(Compute Cores)** (@ `psutil-7.2.2/psutil/arch/posix/net.c`) -> Impact: **101.6** | LOC: 137
  * *Intent:* // net_if_stats() macOS/BSD implementation. #ifdef PSUTIL_HAS_NET_IF_DUPLEX_SPEED
- `psutil_proc_environ` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/bsd/proc.c`) -> Impact: **96.2** | LOC: 226
- `psutil_net_if_flags` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/posix/net.c`) -> Impact: **95.8** | LOC: 183
  * *Intent:* /* * Get all of the NIC flags and return them. */
- `psutil_proc_net_connections` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/osx/proc.c`) -> Impact: **84.2** | LOC: 229
  * *Intent:* /* * Return process TCP and UDP connections as a list of tuples. * Raises NSP in case of zombie process. * See lsof source code: * https://github.com/...
- `psutil_disk_partitions` **(Many-Argument Workhorses)** (@ `psutil-7.2.2/psutil/arch/bsd/disk.c`) -> Impact: **80.9** | LOC: 163
  * *Intent:* #include <Python.h> #if PSUTIL_NETBSD // getvfsstat() #include <sys/types.h> #include <sys/statvfs.h> #else // getfsstat() #include <sys/param.h> #inc...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `psutil-7.2.2/tests` | 20 | 8711.52 | 25.61% | 0.0% |
| `psutil-7.2.2/psutil` | 16 | 7811.38 | 35.89% | 32.67% |
| `psutil-7.2.2/psutil/arch/windows` | 19 | 3540.98 | 56.31% | 49.42% |
| `psutil-7.2.2/psutil/arch/freebsd` | 9 | 1590.8 | 60.28% | 45.4% |
| `psutil-7.2.2/psutil/arch/osx` | 11 | 1554.96 | 59.13% | 48.61% |
| `psutil-7.2.2/psutil/arch/sunos` | 8 | 1316.48 | 57.41% | 48.95% |
| `psutil-7.2.2/psutil/arch/posix` | 7 | 856.4 | 45.88% | 45.22% |
| `psutil-7.2.2/psutil/arch/bsd` | 9 | 743.94 | 47.39% | 61.63% |
| `psutil-7.2.2/psutil/arch/netbsd` | 7 | 655.88 | 66.9% | 58.4% |
| `psutil-7.2.2/psutil/arch/openbsd` | 8 | 499.3 | 67.4% | 55.99% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `psutil-7.2.2/Makefile` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/arch/openbsd/cpu.c` -> **99.9989%** Exposure
- `psutil-7.2.2/psutil/_psosx.py` -> **99.997%** Exposure
- `psutil-7.2.2/psutil/arch/netbsd/cpu.c` -> **99.9969%** Exposure
- `psutil-7.2.2/psutil/_psaix.py` -> **99.9924%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `psutil-7.2.2/psutil/__init__.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_common.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_ntuples.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psaix.py` -> **100.0%** Exposure
- `psutil-7.2.2/psutil/_psbsd.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `psutil-7.2.2/tests/test_linux.py` -> **100** Orphaned Functions | **0** Duplicates
- `psutil-7.2.2/tests/test_process.py` -> **92** Orphaned Functions | **0** Duplicates
- `psutil-7.2.2/tests/test_memleaks.py` -> **70** Orphaned Functions | **0** Duplicates
- `psutil-7.2.2/tests/test_windows.py` -> **52** Orphaned Functions | **6** Duplicates
- `psutil-7.2.2/tests/test_system.py` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `790` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `psutil-7.2.2/psutil/arch/netbsd/proc.c` (C) -> Cumulative Risk: **712.43**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.94)
- **Magnitude:** 158.66 | **LOC:** 291 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Tech Debt (98.8651%)
- **Heaviest Functions:** `psutil_proc_threads` (Many-Argument Workhorses, Impact: 26.2), `psutil_proc_cmdline` (Many-Argument Workhorses, Impact: 26.1), `psutil_proc_cwd` (Many-Argument Workhorses, Impact: 13.8)

### 2. `psutil-7.2.2/psutil/arch/bsd/proc.c` (C) -> Cumulative Risk: **691.6**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.84)
- **Magnitude:** 343.8 | **LOC:** 452 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.1642%)
- **Heaviest Functions:** `psutil_proc_environ` (Many-Argument Workhorses, Impact: 96.2), `psutil_proc_oneshot_info` (Many-Argument Workhorses, Impact: 39.9), `psutil_proc_open_files` (Compute Cores, Impact: 38.9)

### 3. `psutil-7.2.2/psutil/arch/windows/services.c` (C) -> Cumulative Risk: **688.92**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.53)
- **Magnitude:** 292.02 | **LOC:** 553 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9705%), Tech Debt (92.7444%)
- **Heaviest Functions:** `psutil_winservice_enumerate` (Many-Argument Workhorses, Impact: 28.6), `psutil_winservice_query_descr` (Many-Argument Workhorses, Impact: 28.2), `psutil_winservice_query_config` (Many-Argument Workhorses, Impact: 25.4)

### 4. `psutil-7.2.2/psutil/arch/openbsd/proc.c` (C) -> Cumulative Risk: **686.67**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `C Struct Operations Files` (z +1.88)
- **Magnitude:** 123.54 | **LOC:** 206 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9884%), Tech Debt (90.696%)
- **Heaviest Functions:** `psutil_proc_threads` (Compute Cores, Impact: 28.0), `psutil_proc_cmdline` (Many-Argument Workhorses, Impact: 16.1), `psutil_proc_num_fds` (C Struct Operations, Impact: 15.5)

### 5. `psutil-7.2.2/psutil/arch/all/str.c` (C) -> Cumulative Risk: **680.69**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.16)
- **Magnitude:** 82.1 | **LOC:** 110 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9912%), Tech Debt (89.7216%)
- **Heaviest Functions:** `str_append` (Defensive Guards, Impact: 23.4), `str_format` (Many-Argument Workhorses, Impact: 14.6), `str_copy` (Defensive Guards, Impact: 10.7)

### 6. `psutil-7.2.2/psutil/arch/sunos/net.c` (C) -> Cumulative Risk: **677.05**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.07)
- **Magnitude:** 500.04 | **LOC:** 567 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.9949%)
- **Heaviest Functions:** `psutil_net_connections` (Many-Argument Workhorses, Impact: 134.8), `psutil_net_if_stats` (Compute Cores, Impact: 50.2), `psutil_net_io_counters` (Many-Argument Workhorses, Impact: 43.7)

### 7. `psutil-7.2.2/psutil/arch/freebsd/proc.c` (C) -> Cumulative Risk: **668.47**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.61)
- **Magnitude:** 485.16 | **LOC:** 594 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.45%)
- **Heaviest Functions:** `psutil_proc_memory_maps` (Many-Argument Workhorses, Impact: 55.1), `psutil_proc_setrlimit` (Compute Cores, Impact: 24.7), `psutil_proc_exe` (Compute Cores, Impact: 21.2)

### 8. `psutil-7.2.2/psutil/_psaix.py` (PYTHON) -> Cumulative Risk: **666.11**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.34)
- **Magnitude:** 378.46 | **LOC:** 547 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9924%), Safety Score (96.5147%)
- **Heaviest Functions:** `exe` (Compute Cores, Impact: 15.5), `net_connections` (Compute Cores, Impact: 11.6), `open_files` (Compute Cores, Impact: 9.7)

### 9. `psutil-7.2.2/psutil/arch/linux/proc.c` (C) -> Cumulative Risk: **665.75**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.96)
- **Magnitude:** 125.1 | **LOC:** 200 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (88.2027%)
- **Heaviest Functions:** `psutil_proc_cpu_affinity_get` (Compute Cores, Impact: 25.7), `psutil_proc_cpu_affinity_set` (Compute Cores, Impact: 19.6), `psutil_proc_ioprio_set` (Compute Cores, Impact: 5.9)

### 10. `psutil-7.2.2/psutil/arch/windows/disk.c` (C) -> Cumulative Risk: **656.23**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.55)
- **Magnitude:** 206.76 | **LOC:** 409 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.943%), Safety Score (81.2054%)
- **Heaviest Functions:** `psutil_disk_partitions` (Many-Argument Workhorses, Impact: 53.5), `psutil_disk_io_counters` (Many-Argument Workhorses, Impact: 32.2), `psutil_get_drive_type` (Compute Cores, Impact: 16.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `psutil-7.2.2/psutil/_pslinux.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1855.76 | **LOC:** 2270 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.0951%), Tech Debt (14.6386%)
**Top Internal Functions/Classes:**
  * `process_inet` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* """Parse /proc/net/tcp* and /proc/net/udp* files."""
  * `process_unix` **(Many-Argument Workhorses)** (Impact: 28.5)
    * *Intent:* """Parse /proc/net/unix files."""
  * `disk_io_counters` **(Compute Cores)** (Impact: 27.8)
    * *Intent:* """Return disk I/O statistics for every disk installed on the system as a dict of raw tuples. """
  * `sensors_battery` **(I/O & Config Routines)** (Impact: 25.4)
    * *Intent:* """Return battery information. Implementation note: it appears /sys/class/power_supply/BAT0/ directo...
  * `disk_partitions` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* """Return mounted disk partitions as a list of namedtuples."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 321 instances
* *State Mutation (weighted view):* 1101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 396`, `args: 91`, `func_start: 90`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 459`, `dead_code: 5`, `fragile_debt: 7`
* *Architecture:* `io: 83`, `api: 79`, `import: 40`
* *Defense:* `safety: 107`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.34
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.014388
  * `Imports (Out-Degree: 1):` , ._common, base64, collections, enum, errno, functools, glob...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1629.52 | **LOC:** 2485 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.3164%), Tech Debt (9.6985%)
**Top Internal Functions/Classes:**
  * `wait_procs` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* """Convenience function which waits for a list of processes to terminate. Return a (gone, alive) tup...
  * `cpu_percent` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* """Return a float representing the current system-wide CPU utilization as a percentage. When *interv...
  * `cpu_times_percent` **(Compute Cores)** (Impact: 27.1)
    * *Intent:* """Same as cpu_percent() but provides utilization percentages for each specific CPU time as is retur...
  * `as_dict` **(Many-Argument Workhorses)** (Impact: 24.3)
    * *Intent:* """Utility method returning process information as a hashable dictionary. If *attrs* is specified it...
  * `children` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* """Return the children of this process as a list of Process instances, pre-emptively checking whethe...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 243 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 438`, `args: 106`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 300`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 93`, `concurrency: 6`, `import: 86`
* *Defense:* `safety: 95`, `doc: 83`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` , ._common, ._pslinux, ._pssunos, ._psutil_windows, ._pswindows, collections, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_linux.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1420.48 | **LOC:** 2290 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.3982%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `open_mock` **(Compute Cores)** (Impact: 31.5)
  * `test_emulate_multi_cpu` **(Defensive Guards)** (Impact: 29.3)
  * `test_flags` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* # first line looks like this: # "eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500" matches_...
  * `open_mock` **(Compute Cores)** (Impact: 18.9)
  * `test_emulate_data` **(Defensive Guards)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 487
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 919`, `args: 158`, `func_start: 154`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 271`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 100`
* *Architecture:* `io: 144`, `api: 179`, `import: 45`
* *Defense:* `safety: 341`, `doc: 20`, `test: 269`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` , collections, contextlib, errno, fcntl, io, os, platform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1267.6 | **LOC:** 1737 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `terminate` **(Defensive Guards)** (Impact: 46.1)
    * *Intent:* """Terminate a process and wait() for it. Process can be a PID or an instance of psutil.Process(), s...
  * `check_connection_ntuple` **(Defensive Guards)** (Impact: 24.9)
    * *Intent:* """Check validity of a connection namedtuple."""
  * `assert_proc_zombie` **(Defensive Guards)** (Impact: 18.3)
  * `copyload_shared_lib` **(Compute Cores)** (Impact: 17.7)
    * *Intent:* """Ctx manager which picks up a random shared DLL lib used by this process, copies it in another loc...
  * `wrapper` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 165 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 14
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 549
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 357`, `args: 95`, `func_start: 93`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 7`, `state_mutation: 219`, `fragile_debt: 3`
* *Architecture:* `io: 100`, `api: 92`, `concurrency: 4`, `import: 46`
* *Defense:* `safety: 171`, `doc: 48`, `test: 15`, `sync_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` atexit, contextlib, ctypes, enum, errno, functools, importlib, ipaddress...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1216.26 | **LOC:** 1843 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.22%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_memory_maps` **(Defensive Guards)** (Impact: 25.0)
  * `test_nice` **(Defensive Guards)** (Impact: 20.2)
  * `test_pid_0` **(Defensive Guards)** (Impact: 19.2)
    * *Intent:* # Process(0) is supposed to work on all platforms except Linux if 0 not in psutil.pids(): with pytes...
  * `test_open_files` **(Defensive Guards)** (Impact: 18.8)
    * *Intent:* # TODO: #595
  * `test_cmdline` **(Defensive Guards)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 146 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 530
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 658`, `args: 104`, `func_start: 100`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 2`, `state_mutation: 238`, `planned_debt: 2`, `fragile_debt: 14`, `unreferenced_by_name: 92`
* *Architecture:* `io: 76`, `api: 103`, `import: 63`
* *Defense:* `safety: 320`, `doc: 4`, `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` , collections, contextlib, enum, errno, getpass, io, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_pswindows.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 737.64 | **LOC:** 1097 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.9398%), Tech Debt (23.3267%)
**Top Internal Functions/Classes:**
  * `wait` **(Defensive Guards)** (Impact: 17.6)
  * `cpu_affinity_set` **(Defensive Guards)** (Impact: 11.6)
  * `send_signal` **(Compute Cores)** (Impact: 9.2)
  * `convert_dos_path` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* # ===================================================================== # --- utils # ==============...
  * `net_connections` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* # ===================================================================== # --- network # ============...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 97 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 262`, `args: 84`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 161`, `dead_code: 10`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `io: 6`, `api: 79`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 40`, `doc: 40`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.34
  * `Choke Point (Betweenness):` 0.000156 | `Ripple Effect (Closeness):` 0.014388
  * `Imports (Out-Degree: 2):` , ._common, ._psutil_windows, contextlib, enum, from, functools, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/tests/test_system.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 672.52 | **LOC:** 985 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.6837%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_net_if_addrs` **(Defensive Guards)** (Impact: 32.0)
  * `test_disk_partitions` **(Defensive Guards)** (Impact: 26.9)
  * `test_os_constants` **(Defensive Guards)** (Impact: 16.5)
  * `test_wait_procs` **(Defensive Guards)** (Impact: 14.2)
  * `test_cpu_freq` **(Defensive Guards)** (Impact: 12.3)
    * *Intent:* # TODO: remove this once 1892 is fixed
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 253
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 416`, `args: 60`, `func_start: 58`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 101`, `dead_code: 8`, `planned_debt: 2`, `unreferenced_by_name: 49`
* *Architecture:* `io: 41`, `api: 65`, `import: 43`
* *Defense:* `safety: 258`, `doc: 1`, `test: 101`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , datetime, enum, errno, os, pprint, psutil, psutil._common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/osx/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 664.3 | **LOC:** 1050 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.1608%), Tech Debt (29.1709%)
**Top Internal Functions/Classes:**
  * `psutil_proc_net_connections` **(Many-Argument Workhorses)** (Impact: 84.2)
    * *Intent:* /* * Return process TCP and UDP connections as a list of tuples. * Raises NSP in case of zombie proc...
  * `psutil_proc_environ` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* // Return process environment as a python string. // On Big Sur this function returns an empty strin...
  * `psutil_proc_memory_uss` **(Compute Cores)** (Impact: 39.6)
    * *Intent:* /* * Returns the USS (unique set size) of the process. Reference: * https://dxr.mozilla.org/mozilla-...
  * `psutil_proc_threads` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* /* * Return process threads */
  * `psutil_proc_open_files` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /* * Return process open files as a Python tuple. * See lsof source code: * https://github.com/apple...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 93 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 87`, `args: 29`, `func_start: 14`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 105`, `dead_code: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 12`, `import: 18`
* *Defense:* `safety: 15`, `immutability_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` init.h, Python.h, inet.h, errno.h, libproc.h, loader.h, mach.h, mach_vm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 662.26 | **LOC:** 1230 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.7003%), Tech Debt (49.1102%)
**Top Internal Functions/Classes:**
  * `psutil_proc_exe` **(Compute Cores)** (Impact: 39.9)
    * *Intent:* /* * Return process executable path. Works for all processes regardless of * privilege. NtQuerySyste...
  * `psutil_proc_threads` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `psutil_proc_username` **(Many-Argument Workhorses)** (Impact: 34.2)
    * *Intent:* /* * Return process username as a "DOMAIN//USERNAME" string. */
  * `psutil_proc_memory_maps` **(Many-Argument Workhorses)** (Impact: 24.6)
    * *Intent:* /* * Return a list of process's memory mappings. */
  * `psutil_GetProcWsetInformation` **(Many-Argument Workhorses)** (Impact: 22.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 74 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 111`, `args: 41`, `func_start: 25`
* *Risk/State:* `state_mutation: 80`, `dead_code: 1`, `unreferenced_by_name: 22`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` init.h, Psapi.h, Python.h, signal.h, tlhelp32.h, windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_common.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 628.14 | **LOC:** 862 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.6116%), Tech Debt (19.3757%)
**Top Internal Functions/Classes:**
  * `conn_to_ntuple` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* """Convert a raw connection tuple to a proper ntuple."""
  * `print_color` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `run` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* """Cache dict and sum numbers which overflow and wrap. Return an updated copy of `input_dict`. """
  * `_infodict` **(Compute Cores)** (Impact: 9.0)
  * `__str__` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* # invoked on `raise Error` info = self._infodict(("pid", "ppid", "name")) if info: details = "({})"....
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 83 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 163`, `args: 48`, `func_start: 48`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 167`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 37`, `api: 44`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 49`, `doc: 35`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.116547
  * `Imports (Out-Degree: 0):` , collections, ctypes, enum, functools, inspect, ipaddress, os...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/_psbsd.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 606.22 | **LOC:** 905 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.2275%), Tech Debt (99.8968%)
**Top Internal Functions/Classes:**
  * `cmdline` **(Defensive Guards)** (Impact: 15.4)
  * `net_connections` **(Compute Cores)** (Impact: 15.0)
  * `exe` **(Compute Cores)** (Impact: 13.9)
  * `cpu_affinity_set` **(Defensive Guards)** (Impact: 11.6)
    * *Intent:* # Pre-emptively check if CPUs are valid because the C # function has a weird behavior in case of inv...
  * `wrapper` **(Defensive Guards)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 215`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 123`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 30`
* *Architecture:* `io: 3`, `api: 56`, `import: 24`
* *Defense:* `safety: 33`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , ._common, collections, contextlib, errno, functools, os, shutil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_windows.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 579.5 | **LOC:** 948 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.5621%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_disks` **(Defensive Guards)** (Impact: 14.2)
  * `wmic` **(Compute Cores)** (Impact: 12.8)
    * *Intent:* """Currently not used, but available just in case. Usage: >>> wmic("Win32_OperatingSystem", "FreePhy...
  * `test_win_service_iter` **(Defensive Guards)** (Impact: 9.5)
  * `test_disk_partitions` **(Defensive Guards)** (Impact: 9.1)
  * `setUp` **(Compute Cores)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 49 instances
* *Api Near Db Sink:* 2 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 322`, `args: 75`, `func_start: 75`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 163`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 52`
* *Architecture:* `io: 13`, `api: 84`, `import: 34`
* *Defense:* `safety: 134`, `doc: 6`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` , ctypes, ctypes.wintypes, datetime, glob, os, platform, psutil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_psutil_aix.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 536.32 | **LOC:** 1074 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.8049%), Tech Debt (15.8052%)
**Top Internal Functions/Classes:**
  * `PyInit__psutil_aix` **(Compute Cores)** (Impact: 26.9)
  * `psutil_proc_environ` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* /* * Return process environment variables as a Python dict */
  * `psutil_proc_threads` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* #ifdef CURR_VERSION_THREAD /* * Retrieves all threads used by process returning a list of tuples * i...
  * `psutil_net_io_counters` **(Many-Argument Workhorses)** (Impact: 20.8)
    * *Intent:* #if defined(CURR_VERSION_NETINTERFACE) && CURR_VERSION_NETINTERFACE >= 3 /* * Return a list of tuple...
  * `psutil_per_cpu_times` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /* * Return a Python list of tuple representing per-cpu times */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 20 instances
* *Amplified Cascading Flux:* 78 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 106`, `args: 43`, `func_start: 22`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 78`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 4`, `import: 25`
* *Defense:* `safety: 5`, `immutability_locks: 4`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Python.h, common.h, ifaddrs.h, net_connections.h, init.h, inet.h, fcntl.h, libperfstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/windows/proc_info.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 520.54 | **LOC:** 863 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.8756%), Tech Debt (26.5554%)
**Top Internal Functions/Classes:**
  * `psutil_get_process_data` **(Many-Argument Workhorses)** (Impact: 126.4)
    * *Intent:* /* * Get data from the process with the given pid. The data is returned * in the pdata output member...
  * `psutil_proc_cmdline` **(Many-Argument Workhorses)** (Impact: 36.3)
    * *Intent:* /* * Return a Python list representing the arguments for the process * with given pid or NULL on err...
  * `psutil_cmdline_query_proc` **(Many-Argument Workhorses)** (Impact: 30.2)
    * *Intent:* /* * Get process cmdline by using NtQueryInformationProcess. This is a * method alternative to PEB w...
  * `psutil_get_proc_info` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /* * Given a process PID and a PSYSTEM_PROCESS_INFORMATION structure * fills the structure with vari...
  * `psutil_proc_info` **(Many-Argument Workhorses)** (Impact: 19.2)
    * *Intent:* /* * Get various process information by using NtQuerySystemInformation. * We use this as a fallback ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 70 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 43`, `args: 30`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 71`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 4`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` init.h, Python.h, windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/_pssunos.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 515.36 | **LOC:** 705 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.2966%), Tech Debt (18.9391%)
**Top Internal Functions/Classes:**
  * `_get_unix_sockets` **(Compute Cores)** (Impact: 19.0)
    * *Intent:* """Get UNIX sockets used by process by parsing 'pfiles' output."""
  * `net_connections` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* """Return socket connections. If pid == -1 return system-wide connections (as opposed to connections...
  * `memory_maps` **(Defensive Guards)** (Impact: 15.0)
  * `threads` **(Defensive Guards)** (Impact: 11.5)
  * `open_files` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 74 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 172`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 118`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 26`, `api: 45`, `import: 24`
* *Defense:* `safety: 29`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.891
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007194
  * `Imports (Out-Degree: 1):` , ._common, collections, errno, functools, os, socket, subprocess...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `psutil-7.2.2/psutil/arch/sunos/net.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 500.04 | **LOC:** 567 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.9397%), Tech Debt (51.7391%)
**Top Internal Functions/Classes:**
  * `psutil_net_connections` **(Many-Argument Workhorses)** (Impact: 134.8)
    * *Intent:* /* * Return TCP and UDP connections opened by process. * UNIX sockets are excluded. * * Thanks to: *...
  * `psutil_net_if_stats` **(Compute Cores)** (Impact: 50.2)
    * *Intent:* // Return stats about a particular network interface. Refs: // * https://github.com/dpaleino/wicd/bl...
  * `psutil_net_io_counters` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* #include <sys/types.h> #include <sys/socket.h> #include <sys/sockio.h> #include <netinet/in.h> #incl...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 33`, `args: 16`, `func_start: 3`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 93`, `fragile_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 3`, `import: 18`
* *Defense:* `safety: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` init.h, Python.h, inet.h, fcntl.h, mib2.h, kstat.h, if.h, in.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/proc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 485.16 | **LOC:** 594 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.2969%), Tech Debt (49.595%)
**Top Internal Functions/Classes:**
  * `psutil_proc_memory_maps` **(Many-Argument Workhorses)** (Impact: 55.1)
  * `psutil_proc_setrlimit` **(Compute Cores)** (Impact: 24.7)
    * *Intent:* /* * An emulation of Linux prlimit() (set). */
  * `psutil_proc_exe` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* /* * Return process pathname executable. * Thanks to Robert N. M. Watson: * http://fxr.googlebit.com...
  * `psutil_proc_cmdline` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* // ============================================================================ // APIS // =========...
  * `psutil_proc_cwd` **(C Struct Operations)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 69`, `args: 17`, `func_start: 12`, `class_start: 14`
* *Risk/State:* `state_mutation: 83`, `unreferenced_by_name: 11`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 4`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` init.h, Python.h, libutil.h, cpuset.h, sysctl.h, user.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_process_all.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 462.38 | **LOC:** 542 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.7609%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_it` **(Defensive Guards)** (Impact: 23.8)
  * `memory_maps` **(Defensive Guards)** (Impact: 23.2)
  * `exe` **(Defensive Guards)** (Impact: 20.9)
  * `open_files` **(Defensive Guards)** (Impact: 15.2)
  * `check` **(Defensive Guards)** (Impact: 14.1)
    * *Intent:* # In case of failure retry up to 3 times in order to avoid # race conditions, especially when runnin...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 253`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 26`, `planned_debt: 1`, `fragile_debt: 6`
* *Architecture:* `io: 13`, `api: 47`, `concurrency: 3`, `import: 29`
* *Defense:* `safety: 200`, `doc: 3`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , enum, errno, multiprocessing, os, psutil, stat, tests.test_process_all...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/posix/net.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 453.54 | **LOC:** 680 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5886%), Tech Debt (40.484%)
**Top Internal Functions/Classes:**
  * `psutil_get_nic_speed` **(Compute Cores)** (Impact: 101.6)
    * *Intent:* // net_if_stats() macOS/BSD implementation. #ifdef PSUTIL_HAS_NET_IF_DUPLEX_SPEED
  * `psutil_net_if_flags` **(Many-Argument Workhorses)** (Impact: 95.8)
    * *Intent:* /* * Get all of the NIC flags and return them. */
  * `psutil_convert_ipaddr` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* #include <sys/sockio.h> #endif #if defined(PSUTIL_AIX) #include <netdb.h> #endif #include "../../arc...
  * `psutil_net_if_addrs` **(Compute Cores)** (Impact: 33.8)
    * *Intent:* /* * Return NICs information a-la ifconfig as a list of tuples. * TODO: on Solaris we won't get any ...
  * `psutil_net_if_duplex_speed` **(C Struct Operations)** (Impact: 17.5)
    * *Intent:* /* * Return stats about a particular network interface. * References: * http://www.i-scream.org/libs...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 64`, `args: 65`, `func_start: 8`, `class_start: 8`
* *Risk/State:* `state_mutation: 41`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 5`, `api: 7`, `import: 23`
* *Defense:* `safety: 2`, `immutability_locks: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` init.h, Python.h, ifaddrs.h, errno.h, ifaddrs.h, if_packet.h, types.h, if.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_bsd.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 450.2 | **LOC:** 588 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ctx_switches` **(Defensive Guards)** (Impact: 9.4)
  * `test_cpu_times` **(Defensive Guards)** (Impact: 9.4)
  * `test_disks` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* # test psutil.disk_usage() and psutil.disk_partitions() # against "df -a" def df(path): out = sh(f'd...
  * `test_sensors_battery` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* # --- sensors_battery
  * `sysctl` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* """Expects a sysctl command with an argument and parse the result returning only the value of intere...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 182`, `args: 58`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 103`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 30`
* *Architecture:* `io: 8`, `api: 63`, `import: 18`
* *Defense:* `safety: 75`, `doc: 4`, `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , datetime, os, psutil, re, shutil, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/sys_socks.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 443.46 | **LOC:** 469 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.7449%), Tech Debt (20.0468%)
**Top Internal Functions/Classes:**
  * `psutil_gather_inet` **(Many-Argument Workhorses)** (Impact: 117.0)
    * *Intent:* // Reference: // https://github.com/freebsd/freebsd/blob/master/usr.bin/sockstat/sockstat.c
  * `psutil_gather_unix` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `psutil_net_connections` **(Compute Cores)** (Impact: 37.5)
  * `psutil_populate_xfiles` **(C Struct Operations)** (Impact: 11.6)
    * *Intent:* #include <sys/file.h> #include <sys/socketvar.h> // for struct xsocket #include <sys/un.h> #include ...
  * `psutil_get_file_from_sock` **(C Struct Operations)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 69 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 74`, `args: 20`, `func_start: 6`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 69`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 4`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` init.h, Python.h, inet.h, in.h, in_pcb.h, ip.h, tcp_var.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_misc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 435.76 | **LOC:** 868 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.6109%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_against` **(Defensive Guards)** (Impact: 17.4)
    * *Intent:* # no args for _ in range(2): ret = obj() assert self.calls == [((), {})] if expected_retval is not N...
  * `test__all__` **(Defensive Guards)** (Impact: 14.4)
  * `test_serialization` **(Defensive Guards)** (Impact: 12.3)
  * `test_cache_clear_public_apis` **(Defensive Guards)** (Impact: 9.4)
  * `test_original` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* # This was the original test before I made it dynamic to test it # against different types. Keeping ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 346`, `args: 60`, `func_start: 60`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 5`, `state_mutation: 120`, `fragile_debt: 1`, `unreferenced_by_name: 45`
* *Architecture:* `io: 23`, `api: 67`, `import: 27`
* *Defense:* `safety: 185`, `doc: 6`, `test: 78`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , collections, contextlib, io, json, os, pickle, psutil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_posix.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 408.78 | **LOC:** 472 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.2788%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ps` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* """Wrapper for calling the ps command with a little bit of cross-platform support for a narrow range...
  * `test_users` **(Defensive Guards)** (Impact: 19.8)
  * `test_users_started` **(Compute Cores)** (Impact: 18.7)
  * `test_pids` **(Compute Cores)** (Impact: 13.5)
    * *Intent:* # Note: this test might fail if the OS is starting/killing # other processes in the meantime pids_ps...
  * `test_disk_usage` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* # AIX can return '-' in df output instead of numbers, e.g. for /proc
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 139`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 102`, `dead_code: 2`, `unreferenced_by_name: 24`
* *Architecture:* `io: 3`, `api: 33`, `import: 28`
* *Defense:* `safety: 39`, `doc: 4`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , datetime, errno, mmap, os, psutil, re, resource...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/tests/test_connections.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 406.44 | **LOC:** 573 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.3509%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_count` **(Defensive Guards)** (Impact: 28.3)
  * `test_unix` **(Defensive Guards)** (Impact: 21.0)
  * `check_conn` **(Many-Argument Workhorses)** (Impact: 16.5)
  * `check_socket` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* """Given a socket, makes sure it matches the one obtained via psutil. It assumes this process create...
  * `compare_procsys_connections` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* """Given a process PID and its list of connections compare those against system-wide connections ret...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 53 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 226`, `args: 26`, `func_start: 26`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 4`, `state_mutation: 77`, `fragile_debt: 3`, `unreferenced_by_name: 19`
* *Architecture:* `io: 11`, `api: 33`, `import: 36`
* *Defense:* `safety: 86`, `doc: 9`, `test: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , contextlib, os, psutil, psutil._common, socket, sys, tests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `psutil-7.2.2/psutil/arch/freebsd/proc_socks.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 397.44 | **LOC:** 415 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.1782%), Tech Debt (14.0712%)
**Top Internal Functions/Classes:**
  * `psutil_search_tcplist` **(Many-Argument Workhorses)** (Impact: 120.9)
    * *Intent:* #if __FreeBSD_version >= 1200026
  * `psutil_proc_net_connections` **(Many-Argument Workhorses)** (Impact: 79.9)
  * `psutil_search_tcplist` **(C Struct Operations)** (Impact: 40.6)
    * *Intent:* #else
  * `psutil_fetch_tcplist` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* #include <sys/user.h> #include <sys/socketvar.h> // for struct xsocket #include <sys/un.h> #include ...
  * `psutil_sockaddr_port` **(C Struct Operations)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 40 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 65`, `args: 13`, `func_start: 8`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 40`, `dead_code: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* `safety: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.408
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` init.h, Python.h, inet.h, libutil.h, in.h, in_pcb.h, tcp_var.h, param.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `psutil-7.2.2/psutil/arch/windows/wmi.c` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 99.9241%)
- `psutil-7.2.2/psutil/_psutil_windows.c` -> **Severity: 0.024** (Bridge: 0.0012 * Flux: 20.1917%)
- `psutil-7.2.2/psutil/_pswindows.py` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)
- `psutil-7.2.2/psutil/_pslinux.py` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `psutil-7.2.2/psutil/_common.py` -> **Severity: 11.209** (Embedded: 0.1165 * Error Risk: 96.1785%)
- `psutil-7.2.2/psutil/_pslinux.py` -> **Severity: 1.412** (Embedded: 0.0144 * Error Risk: 98.1149%)
- `psutil-7.2.2/psutil/_pswindows.py` -> **Severity: 1.319** (Embedded: 0.0144 * Error Risk: 91.6957%)
- `psutil-7.2.2/psutil/_psposix.py` -> **Severity: 1.051** (Embedded: 0.0144 * Error Risk: 73.0199%)
- `psutil-7.2.2/psutil/_psutil_windows.c` -> **Severity: 0.905** (Embedded: 0.0162 * Error Risk: 55.8782%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `psutil-7.2.2/psutil/_common.py` -> **Severity: 1840.498** (Blast Radius: 47.853 * Doc Risk: 38.4615%)
- `psutil-7.2.2/psutil/_psutil_windows.c` -> **Severity: 616.1** (Blast Radius: 6.161 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/_psutil_linux.c` -> **Severity: 485.7** (Blast Radius: 4.857 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/arch/windows/wmi.c` -> **Severity: 485.7** (Blast Radius: 4.857 * Doc Risk: 100.0%)
- `psutil-7.2.2/psutil/arch/all/errors.c` -> **Severity: 437.4** (Blast Radius: 4.374 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
