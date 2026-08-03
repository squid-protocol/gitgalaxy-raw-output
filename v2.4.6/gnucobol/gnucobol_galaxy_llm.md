# ARCHITECTURAL_BRIEF: gnucobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/gnucobol` |
| **Timestamp** | `2026-08-03T19:28:56.125821+00:00` |
| **Scan Duration** | `2.51s` |
| **Git Branch** | `main` |
| **Git Commit** | `d139d06201cf0aba9d143e0f675f446c19603b36` |
| **Git Remote** | `https://github.com/paulsmith/gnucobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 152 malicious artifacts.

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
| Total Artifacts | 382 |
| Analyzed Artifacts (Scanned) | 194 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 188 |
| Total LOC | 151502 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3924 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1308 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4165 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| M4 | 73 | 81822 | 37.6% |
| C | 46 | 61461 | 23.7% |
| PLAINTEXT | 36 | 0 | 18.6% |
| MAKEFILE | 11 | 1696 | 5.7% |
| COBOL | 9 | 1461 | 4.6% |
| SHELL | 6 | 533 | 3.1% |
| BATCH | 4 | 812 | 2.1% |
| MARKDOWN | 3 | 0 | 1.5% |
| PERL | 3 | 547 | 1.5% |
| YACC | 2 | 3165 | 1.0% |
| POWERSHELL | 1 | 5 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.356`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 144 | 74.2% |
| file_cluster_13 | 5 | 2.6% |
| file_cluster_9 | 2 | 1.0% |
| file_cluster_0 | 2 | 1.0% |
| file_cluster_11 | 1 | 0.5% |
| file_cluster_6 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 39 | 20.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 188*

**Composition by Extension & Reason:**
- `.vcxproj`: 24x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 24x Excluded (Unsupported Extension: '.filters')
- `.conf`: 19x Excluded (Unsupported Extension: '.conf')
- `no_extension`: 6x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 349 LOC)
- `.user`: 14x Excluded (Unsupported Extension: '.user')
- `.am`: 9x Excluded (Unsupported Extension: '.am'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.words`: 10x Excluded (Unsupported Extension: '.words')
- `.sln`: 8x Excluded (Unsupported Extension: '.sln')
- `.po`: 8x Excluded (Unsupported Extension: '.po')
- `.vcproj`: 6x Excluded (Unsupported Extension: '.vcproj')
- `.m4`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 276 LOC)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpj`: 4x Excluded (Unsupported Extension: '.cpj')
- `.rc`: 4x Excluded (Unsupported Extension: '.rc')
- `.c`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.4 | 25.1 | 6.8 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.1 | 2.3 | 0.0 |
| API Exposure | 0.0 | 17.6 | 3.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 38.9 | 17.1 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 19.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 0.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.5 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/cobcinfo.sh` (Hits: 126)
- `libcob/fileio.c` (Hits: 60)
- `cobc/cobc.c` (Hits: 36)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.h.in** (`build_windows/config.h.in`) — 27 inbound connections
2. **libcob.h** (`libcob.h`) — 15 inbound connections
3. **coblocal.h** (`libcob/coblocal.h`) — 11 inbound connections
4. **cobc.h** (`cobc/cobc.h`) — 10 inbound connections
5. **defaults.h.in** (`build_windows/defaults.h.in`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **common.c** (`libcob/common.c`) — 48 outbound dependencies
2. **cobc.c** (`cobc/cobc.c`) — 34 outbound dependencies
3. **screenio.c** (`libcob/screenio.c`) — 21 outbound dependencies
4. **call.c** (`libcob/call.c`) — 19 outbound dependencies
5. **fileio.h** (`libcob/fileio.h`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `cob_sys_waitpid` (@ `libcob/common.c`) -> Impact: **2585.2** | LOC: 2131
- `get_dupno` (@ `libcob/flmdb.c`) -> Impact: **2177.1** | LOC: 1147
- `process_command_line` (@ `cobc/cobc.c`) -> Impact: **1684.8** | LOC: 2311
  * *Intent:* #endif #ifdef SIGTERM
- `print_program_code` (@ `cobc/cobc.c`) -> Impact: **1617.3** | LOC: 1376
- `field_accept` (@ `libcob/screenio.c`) -> Impact: **1579.5** | LOC: 1245
- `get_suppress_cond` (@ `cobc/tree.c`) -> Impact: **1014.8** | LOC: 1104
- `ix_bdb_open` (@ `libcob/fbdb.c`) -> Impact: **711.1** | LOC: 722
- `cob_gen_optim` (@ `cobc/codeoptim.c`) -> Impact: **686.5** | LOC: 1532
  * *Intent:* #include <config.h> #include <stdio.h> #include <stdlib.h> #include <stddef.h> #include <stdarg.h> #include <string.h> #include <ctype.h> #include "co...
- `cob_set_file_format` (@ `libcob/fileio.c`) -> Impact: **683.6** | LOC: 592
- `EXTFH` (@ `libcob/fextfh.c`) -> Impact: **571.9** | LOC: 352

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `m4_defun` (@ `m4/libtool.m4`) -> **O(2^N) [Recursive]**
  * *Intent:* dnl aclocal-1.4 backwards compatibility: dnl AC_DEFUN([AC_PROG_LIBTOOL], []) dnl AC_DEFUN([AM_PROG_LIBTOOL], []) # _LT_PREPARE_CC_BASENAME # ---------...
- `print_replace_main` (@ `cobc/cobc.c`) -> **O(2^N) [Recursive]**
- `print_program_code` (@ `cobc/cobc.c`) -> **O(2^N) [Recursive]**
- `cb_tree_print` (@ `cobc/debug.c`) -> **O(2^N) [Recursive]**
- `print_program` (@ `cobc/debug.c`) -> **O(2^N) [Recursive]**
- `print_ml_generate_tree` (@ `cobc/debug.c`) -> **O(2^N) [Recursive]**
- `all_children_are_ignored` (@ `cobc/typeck.c`) -> **O(2^N) [Recursive]**
- `all_children_ok_qualified_by_only` (@ `cobc/typeck.c`) -> **O(2^N) [Recursive]**
- `cb_emit_sort_giving` (@ `cobc/typeck.c`) -> **O(2^N) [Recursive]**
- `cb_emit_sort_using` (@ `cobc/typeck.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `process_command_line` (@ `cobc/cobc.c`) -> DB Complexity: **587**
  * *Intent:* #endif #ifdef SIGTERM
- `cob_sys_waitpid` (@ `libcob/common.c`) -> DB Complexity: **522**
- `Anonymous_Block_[Truncated]` (@ `doc/cobcinfo.sh`) -> DB Complexity: **404**
- `print_program_code` (@ `cobc/cobc.c`) -> DB Complexity: **347**
- `get_suppress_cond` (@ `cobc/tree.c`) -> DB Complexity: **332**
- `cob_gen_optim` (@ `cobc/codeoptim.c`) -> DB Complexity: **304**
  * *Intent:* #include <config.h> #include <stdio.h> #include <stdlib.h> #include <stddef.h> #include <stdarg.h> #include <string.h> #include <ctype.h> #include "co...
- `get_dupno` (@ `libcob/flmdb.c`) -> DB Complexity: **250**
- `cob_set_file_format` (@ `libcob/fileio.c`) -> DB Complexity: **218**
- `field_accept` (@ `libcob/screenio.c`) -> DB Complexity: **196**
- `cob_load_xfd` (@ `libcob/fsqlxfd.c`) -> DB Complexity: **181**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `libcob` | 31 | 54746.18 | 58.07% | 11.11% |
| `cobc` | 20 | 30565.2 | 44.09% | 23.5% |
| `m4` | 34 | 3116.27 | 7.7% | 24.76% |
| `tests/testsuite.src` | 36 | 2432.92 | 1.24% | 0.0% |
| `bin` | 4 | 1258.42 | 33.21% | 16.57% |
| `tests/cobol85` | 22 | 1052.14 | 6.55% | 0.0% |
| `extras` | 2 | 297.68 | 33.17% | 10.14% |
| `__monolith__` | 12 | 296.92 | 0.82% | 1.31% |
| `doc` | 2 | 290.2 | 34.71% | 24.67% |
| `build_aux` | 3 | 190.42 | 61.5% | 66.67% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `build_aux/mkinstalldirs` -> **100.0%** Exposure
- `m4/extern-inline.m4` -> **100.0%** Exposure
- `m4/printf-posix.m4` -> **100.0%** Exposure
- `m4/wint_t.m4` -> **100.0%** Exposure
- `build_aux/bootstrap` -> **99.9998%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/gcdiff.c` -> **100.0%** Exposure
- `cobc/cobc.c` -> **100.0%** Exposure
- `cobc/codeoptim.c` -> **100.0%** Exposure
- `cobc/config.c` -> **100.0%** Exposure
- `cobc/field.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `libcob/common.c` -> **82** Orphaned Functions | **0** Duplicates
- `cobc/typeck.c` -> **44** Orphaned Functions | **0** Duplicates
- `libcob/intrinsic.c` -> **36** Orphaned Functions | **0** Duplicates
- `cobc/tree.c` -> **34** Orphaned Functions | **0** Duplicates
- `libcob/move.c` -> **33** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bin/gcdiff.c`** -> AI Confidence: **99.48%**
2. **`cobc/config.c`** -> AI Confidence: **99.48%**
3. **`cobc/field.c`** -> AI Confidence: **99.48%**
4. **`libcob/cobgetopt.c`** -> AI Confidence: **99.48%**
5. **`libcob/move.c`** -> AI Confidence: **99.48%**
6. **`libcob/reportio.c`** -> AI Confidence: **99.48%**
7. **`libcob/screenio.c`** -> AI Confidence: **99.48%**
8. **`libcob/termio.c`** -> AI Confidence: **99.48%**
9. **`cobc/cobc.c`** -> AI Confidence: **99.39%**
10. **`cobc/tree.c`** -> AI Confidence: **99.39%**
11. **`libcob/common.c`** -> AI Confidence: **99.39%**
12. **`libcob/mlio.c`** -> AI Confidence: **99.39%**
13. **`libcob/numeric.c`** -> AI Confidence: **99.39%**
14. **`libcob/strings.c`** -> AI Confidence: **99.39%**
15. **`libcob/fileio.c`** -> AI Confidence: **99.34%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `cobc/cobc.c` -> **20.0%** Exposure
- `cobc/error.c` -> **20.0%** Exposure
- `cobc/tree.c` -> **20.0%** Exposure
- `cobc/typeck.c` -> **20.0%** Exposure
- `libcob/fileio.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `po/Makefile.in.in` -> **100.0%** Exposure
- `doc/cobcinfo.sh` -> **100.0%** Exposure
- `tests/listings-sed.sh` -> **100.0%** Exposure
- `tests/run_prog_manual.sh.in` -> **99.9997%** Exposure
- `libcob/fbdb.c` -> **99.9907%** Exposure
### Raw Memory Manipulation
- `cobc/debug.c` -> **10.0%** Exposure
- `libcob/fileio.c` -> **10.0%** Exposure
- `libcob/fsqlxfd.c` -> **10.0%** Exposure
- `cobc/tree.c` -> **9.9962%** Exposure
- `libcob/call.c` -> **9.9956%** Exposure
### Algorithmic DoS Exposure
- `bin/gcdiff.c` -> **100.0%** Exposure
- `cobc/cobc.c` -> **100.0%** Exposure
- `cobc/config.c` -> **100.0%** Exposure
- `cobc/debug.c` -> **100.0%** Exposure
- `cobc/error.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `31` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `433` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `libcob/fbdb.c` (C) -> Cumulative Risk: **749.7**
- **Archetype:** `file_cluster_8` (Distance: 13.772 IQR)
- **Magnitude:** 1971.36 | **LOC:** 2009 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9907%)
- **Heaviest Functions:** `ix_bdb_open` (Impact: 711.1), `bdb_lock_record` (Impact: 37.8), `bdb_nofile` (Impact: 35.5)

### 2. `cobc/tree.c` (C) -> Cumulative Risk: **739.98**
- **Archetype:** `file_cluster_8` (Distance: 14.529 IQR)
- **Magnitude:** 5224.38 | **LOC:** 6804 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (96.7008%)
- **Heaviest Functions:** `get_suppress_cond` (Impact: 1014.8), `cb_build_intrinsic` (Impact: 377.8), `cb_name_1` (Impact: 340.9)

### 3. `doc/cobcinfo.sh` (SHELL) -> Cumulative Risk: **706.23**
- **Archetype:** `file_cluster_8` (Distance: 11.835 IQR)
- **Magnitude:** 285.56 | **LOC:** 359 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), State Flux (99.9815%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 201.3), `__global_context__` (Impact: 1.5)

### 4. `libcob/common.c` (C) -> Cumulative Risk: **697.24**
- **Archetype:** `file_cluster_8` (Distance: 15.253 IQR)
- **Magnitude:** 10008.0 | **LOC:** 8748 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (94.9573%)
- **Heaviest Functions:** `cob_sys_waitpid` (Impact: 2585.2), `check_current_date` (Impact: 240.4), `cob_correct_numeric` (Impact: 144.5)

### 5. `libcob/fsqlxfd.c` (C) -> Cumulative Risk: **696.96**
- **Archetype:** `file_cluster_8` (Distance: 14.874 IQR)
- **Magnitude:** 5235.3 | **LOC:** 2449 | **CtrlFlow:** 88.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (99.0148%)
- **Heaviest Functions:** `cob_sql_stmt` (Impact: 333.7), `convert_to_date` (Impact: 322.3), `cob_load_xfd` (Impact: 255.6)

### 6. `libcob/fileio.c` (C) -> Cumulative Risk: **694.17**
- **Archetype:** `file_cluster_8` (Distance: 14.68 IQR)
- **Magnitude:** 6037.8 | **LOC:** 7364 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (87.0725%)
- **Heaviest Functions:** `cob_set_file_format` (Impact: 683.6), `cob_file_close` (Impact: 145.4), `cob_file_save_status` (Impact: 140.4)

### 7. `libcob/move.c` (C) -> Cumulative Risk: **688.18**
- **Archetype:** `file_cluster_8` (Distance: 14.53 IQR)
- **Magnitude:** 3653.22 | **LOC:** 2540 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8242%)
- **Heaviest Functions:** `cob_move` (Impact: 222.8), `cob_move_display_to_edited` (Impact: 183.0), `cob_get_s64_pic9` (Impact: 99.6)

### 8. `cobc/cobc.c` (C) -> Cumulative Risk: **682.67**
- **Archetype:** `file_cluster_8` (Distance: 15.022 IQR)
- **Magnitude:** 8418.92 | **LOC:** 8434 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (94.6003%)
- **Heaviest Functions:** `process_command_line` (Impact: 1684.8), `print_program_code` (Impact: 1617.3), `cobc_print_info` (Impact: 107.8)

### 9. `libcob/termio.c` (C) -> Cumulative Risk: **669.02**
- **Archetype:** `file_cluster_8` (Distance: 13.639 IQR)
- **Magnitude:** 987.16 | **LOC:** 751 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (93.4711%)
- **Heaviest Functions:** `cob_display` (Impact: 105.6), `cob_dump_field` (Impact: 102.7), `display_alnum_dump` (Impact: 69.5)

### 10. `libcob/foci.c` (C) -> Cumulative Risk: **666.58**
- **Archetype:** `file_cluster_8` (Distance: 13.79 IQR)
- **Magnitude:** 2176.32 | **LOC:** 1664 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (96.6816%)
- **Heaviest Functions:** `join_environment` (Impact: 169.7), `oci_open` (Impact: 118.8), `chkSts` (Impact: 108.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `libcob/common.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.253 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.999 IQR)
- **Top Global Matches:** file_cluster_8: 15.253, file_cluster_13: 15.361, file_cluster_11: 15.419
- **Magnitude:** 10008.0 | **LOC:** 8748 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 522
- **Risk Profile:** Cognitive Load (94.9573%), Tech Debt (37.2586%)
**Top Internal Functions/Classes:**
  * `cob_sys_waitpid` (Impact: 2585.2 | O(N^2) | DB: 522)
  * `check_current_date` (Impact: 240.4 | O(N^2) | DB: 126)
  * `cob_correct_numeric` (Impact: 144.5 | O(N^1) | DB: 40)
    * *Intent:* /* * Copy the returning 'cob_field' and return address of the copy * This is done to avoid passing b...
  * `cob_sig_handler` (Impact: 80.3 | O(2^N) | DB: 4)
  * `cob_check_numdisp` (Impact: 72.7 | O(N^1) | DB: 8)
    * *Intent:* *p = '4';
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2151`, `structural_boundaries: 750`, `args: 183`, `func_start: 188`, `class_start: 50`
* *Risk/State:* `safety_bypasses: 96`, `high_risk_execution: 2`, `state_mutation: 4423`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 4`, `orphaned_logic: 82`
* *Architecture:* `io: 30`, `api: 735`, `import: 49`
* *Defense:* `safety: 195`, `doc: 2`, `immutability_locks: 205`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` sql.h, curses.h, io.h, xmlversion.h, gettext.h, types.h, lmdb.h, sqlext.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/cobc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.022 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.168 IQR)
- **Top Global Matches:** file_cluster_8: 15.022, file_cluster_13: 15.105, file_cluster_11: 15.144
- **Magnitude:** 8418.92 | **LOC:** 8434 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 587
- **Risk Profile:** Cognitive Load (94.6003%), Tech Debt (14.4974%)
**Top Internal Functions/Classes:**
  * `process_command_line` (Impact: 1684.8 | O(N^2) | DB: 587)
    * *Intent:* #endif #ifdef SIGTERM
  * `print_program_code` (Impact: 1617.3 | O(2^N) | DB: 347)
  * `cobc_print_info` (Impact: 107.8 | O(N^1) | DB: 10)
  * `cobc_def_dump_opts` (Impact: 102.2 | O(N^5) | DB: 11)
  * `print_replace_main` (Impact: 70.9 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1314`, `structural_boundaries: 417`, `args: 115`, `func_start: 116`, `class_start: 64`
* *Risk/State:* `safety_bypasses: 187`, `high_risk_execution: 3`, `state_mutation: 3478`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 7`, `orphaned_logic: 12`
* *Architecture:* `io: 36`, `api: 492`, `import: 33`
* *Defense:* `safety: 150`, `doc: 1`, `immutability_locks: 136`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` sql.h, config.def, io.h, gettext.h, types.h, lmdb.h, sqlext.h, flag.def...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fileio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.68 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.588 IQR)
- **Top Global Matches:** file_cluster_8: 14.68, file_cluster_0: 14.92, file_cluster_11: 14.92
- **Magnitude:** 6037.8 | **LOC:** 7364 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 218
- **Risk Profile:** Cognitive Load (81.9126%), Tech Debt (16.8774%)
**Top Internal Functions/Classes:**
  * `cob_set_file_format` (Impact: 683.6 | O(N^3) | DB: 218)
  * `cob_file_close` (Impact: 145.4 | O(2^N) | DB: 27)
    * *Intent:* cob_file_fcd_sync (f); /* Copy cob_file to app's FCD */
  * `cob_file_save_status` (Impact: 140.4 | O(N^2) | DB: 57)
  * `lock_record` (Impact: 90.3 | O(N^1) | DB: 52)
  * `cob_set_file_defaults` (Impact: 76.0 | O(N^1) | DB: 51)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1484`, `structural_boundaries: 317`, `args: 11`, `func_start: 62`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 110`, `state_mutation: 3061`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 21`
* *Architecture:* `io: 60`, `api: 532`, `import: 5`
* *Defense:* `safety: 75`, `immutability_locks: 83`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fileio.h, signal.h, defaults.h, wait.h, dlfcn.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fsqlxfd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.874 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.422 IQR)
- **Top Global Matches:** file_cluster_8: 14.874, file_cluster_13: 15.137, file_cluster_11: 15.141
- **Magnitude:** 5235.3 | **LOC:** 2449 | **CtrlFlow:** 88.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 181
- **Risk Profile:** Cognitive Load (83.1813%), Tech Debt (12.8783%)
**Top Internal Functions/Classes:**
  * `cob_sql_stmt` (Impact: 333.7 | O(N^1) | DB: 121)
  * `convert_to_date` (Impact: 322.3 | O(N^2) | DB: 69)
  * `cob_load_xfd` (Impact: 255.6 | O(N^2) | DB: 181)
  * `cob_load_ddl` (Impact: 119.8 | O(N^2) | DB: 64)
    * *Intent:* /*
  * `cob_file_to_xfd` (Impact: 118.8 | O(N^2) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 906`, `structural_boundaries: 120`, `args: 48`, `func_start: 37`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 115`, `state_mutation: 2608`, `orphaned_logic: 13`
* *Architecture:* `io: 8`, `api: 297`, `import: 2`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` defaults.h, fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/tree.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.529 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.019 IQR)
- **Top Global Matches:** file_cluster_8: 14.529, file_cluster_13: 14.72, file_cluster_11: 14.721
- **Magnitude:** 5224.38 | **LOC:** 6804 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 332
- **Risk Profile:** Cognitive Load (96.3101%), Tech Debt (46.6691%)
**Top Internal Functions/Classes:**
  * `get_suppress_cond` (Impact: 1014.8 | O(N^3) | DB: 332)
  * `cb_build_intrinsic` (Impact: 377.8 | O(N^2) | DB: 89)
  * `cb_name_1` (Impact: 340.9 | O(2^N) | DB: 39)
  * `get_category_from_arguments` (Impact: 72.3 | O(N^2) | DB: 11)
  * `global_check` (Impact: 56.6 | O(N^2) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1003`, `structural_boundaries: 368`, `args: 80`, `func_start: 81`, `class_start: 78`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 2156`, `planned_debt: 7`, `fragile_debt: 6`, `orphaned_logic: 34`
* *Architecture:* `api: 595`, `import: 10`
* *Defense:* `safety: 72`, `immutability_locks: 139`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, limits.h, tree.h, stdio.h, config.h, stdlib.h, ctype.h, parser.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/field.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.784 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.643 IQR)
- **Top Global Matches:** file_cluster_8: 13.784, file_cluster_13: 14.012, file_cluster_11: 14.089
- **Magnitude:** 3705.72 | **LOC:** 3249 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (84.6786%), Tech Debt (16.5467%)
**Top Internal Functions/Classes:**
  * `validate_pic` (Impact: 238.0 | O(N^1) | DB: 17)
  * `create_implicit_picture` (Impact: 209.9 | O(N^2) | DB: 44)
  * `validate_elementary_item` (Impact: 175.5 | O(N^1) | DB: 77)
  * `cb_build_field_tree` (Impact: 123.0 | O(N^2) | DB: 53)
  * `cb_eval_op` (Impact: 110.8 | O(N^1) | DB: 53)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 814`, `structural_boundaries: 221`, `args: 47`, `func_start: 52`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1161`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 260`, `import: 9`
* *Defense:* `safety: 2`, `immutability_locks: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, limits.h, tree.h, stdio.h, config.h, stdlib.h, ctype.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/move.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.53 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.995 IQR)
- **Top Global Matches:** file_cluster_8: 14.53, file_cluster_13: 14.703, file_cluster_0: 14.759
- **Magnitude:** 3653.22 | **LOC:** 2540 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 140
- **Risk Profile:** Cognitive Load (80.8302%), Tech Debt (26.4078%)
**Top Internal Functions/Classes:**
  * `cob_move` (Impact: 222.8 | O(N^1) | DB: 8)
  * `cob_move_display_to_edited` (Impact: 183.0 | O(N^1) | DB: 140)
  * `cob_get_s64_pic9` (Impact: 99.6 | O(N^1) | DB: 55)
  * `cob_alloc_move` (Impact: 74.9 | O(N^2) | DB: 44)
  * `cob_get_s64_compx` (Impact: 50.0 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 805`, `structural_boundaries: 216`, `args: 80`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1905`, `orphaned_logic: 33`
* *Architecture:* `api: 462`, `import: 11`
* *Defense:* `safety: 56`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` libcob.h, locale.h, math.h, coblocal.h, stdio.h, config.h, stdlib.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/screenio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.835 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.52 IQR)
- **Top Global Matches:** file_cluster_8: 13.835, file_cluster_13: 14.007, file_cluster_11: 14.149
- **Magnitude:** 3637.88 | **LOC:** 3613 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 196
- **Risk Profile:** Cognitive Load (95.3503%), Tech Debt (11.5869%)
**Top Internal Functions/Classes:**
  * `field_accept` (Impact: 1579.5 | O(2^N) | DB: 196)
  * `cob_convert_key` (Impact: 132.7 | O(N^1) | DB: 25)
  * `get_line_and_col_from_field` (Impact: 71.6 | O(N^2) | DB: 17)
  * `cob_screen_init` (Impact: 44.6 | O(N^1) | DB: 20)
    * *Intent:* #endif
  * `cob_prep_input` (Impact: 38.4 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 590`, `structural_boundaries: 132`, `args: 35`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1163`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 268`, `import: 21`
* *Defense:* `safety: 21`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` curses.h, io.h, libcob.h, ncurses.h, coblocal.h, ctype.h, config.h, pdcurses.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/typeck.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.261 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.479 IQR)
- **Top Global Matches:** file_cluster_8: 13.261, file_cluster_13: 13.602, file_cluster_7: 13.654
- **Magnitude:** 3387.46 | **LOC:** 13270 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (75.3266%), Tech Debt (59.6616%)
**Top Internal Functions/Classes:**
  * `cb_build_length` (Impact: 144.3 | O(N^2) | DB: 20)
  * `cb_emit_write` (Impact: 81.3 | O(N^2) | DB: 16)
  * `cb_is_integer_expr` (Impact: 79.2 | O(2^N) | DB: 3)
  * `cb_is_integer_field` (Impact: 76.1 | O(N^1))
  * `cb_emit_report_moves` (Impact: 74.0 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 784`, `structural_boundaries: 395`, `args: 31`, `func_start: 95`, `class_start: 53`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 1315`, `planned_debt: 14`, `fragile_debt: 4`, `orphaned_logic: 44`
* *Architecture:* `api: 359`, `import: 14`
* *Defense:* `safety: 20`, `doc: 1`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cobc.h, limits.h, tree.h, locale.h, stdio.h, config.h, stdlib.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/flmdb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.864 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.814 IQR)
- **Top Global Matches:** file_cluster_8: 13.864, file_cluster_11: 14.026, file_cluster_13: 14.074
- **Magnitude:** 3227.64 | **LOC:** 1563 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 250
- **Risk Profile:** Cognitive Load (96.573%), Tech Debt (13.3418%)
**Top Internal Functions/Classes:**
  * `get_dupno` (Impact: 2177.1 | O(2^N) | DB: 250)
  * `local_file` (Impact: 11.1 | O(N^1) | DB: 14)
  * `db_nofile` (Impact: 7.2 | O(N^1))
  * `db_suppresskey` (Impact: 5.0 | O(N^1) | DB: 5)
  * `lmdb_put` (Impact: 2.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 142`, `args: 35`, `func_start: 41`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 735`, `planned_debt: 15`
* *Architecture:* `io: 6`, `api: 225`, `import: 6`
* *Defense:* `safety: 28`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sysmacros.h, fileio.h, stat.h, lmdb.h, libgen.h, file.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/call.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.034 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.043 IQR)
- **Top Global Matches:** file_cluster_8: 14.034, file_cluster_13: 14.175, file_cluster_0: 14.307
- **Magnitude:** 2778.22 | **LOC:** 2319 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (68.4883%), Tech Debt (15.1678%)
**Top Internal Functions/Classes:**
  * `cob_call` (Impact: 85.8 | O(2^N) | DB: 9)
  * `cob_resolve_internal` (Impact: 83.0 | O(N^1) | DB: 42)
  * `cob_call_cobol` (Impact: 53.4 | O(2^N) | DB: 9)
  * `cob_call_entry` (Impact: 53.4 | O(2^N) | DB: 9)
  * `cob_init_call` (Impact: 52.6 | O(N^1) | DB: 33)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 290`, `args: 60`, `func_start: 59`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 1240`, `orphaned_logic: 15`
* *Architecture:* `io: 7`, `api: 295`, `import: 19`
* *Defense:* `safety: 44`, `doc: 7`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` types.h, ltdl.h, dlfcn.h, libcob.h, coblocal.h, ctype.h, config.h, system.def...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/codeoptim.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.933 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.807 IQR)
- **Top Global Matches:** file_cluster_8: 13.933, file_cluster_13: 14.269, file_cluster_7: 14.32
- **Magnitude:** 2750.42 | **LOC:** 2767 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 304
- **Risk Profile:** Cognitive Load (63.4273%), Tech Debt (8.028%)
**Top Internal Functions/Classes:**
  * `cob_gen_optim` (Impact: 686.5 | O(N^1) | DB: 304)
    * *Intent:* #include <config.h> #include <stdio.h> #include <stdlib.h> #include <stddef.h> #include <stdarg.h> #...
  * `output_storage` (Impact: 4.1 | O(N^1))
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 467`, `args: 141`, `func_start: 2`
* *Risk/State:* `state_mutation: 1870`, `orphaned_logic: 1`
* *Architecture:* `api: 141`, `import: 9`
* *Defense:* `safety: 3`, `immutability_locks: 210`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cobc.h, tree.h, stdio.h, config.h, stdlib.h, ctype.h, string.h, stddef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/numeric.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.909 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.183 IQR)
- **Top Global Matches:** file_cluster_8: 13.909, file_cluster_13: 14.181, file_cluster_0: 14.282
- **Magnitude:** 2574.68 | **LOC:** 2689 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (73.5136%), Tech Debt (38.2871%)
**Top Internal Functions/Classes:**
  * `cob_decimal_get_binary` (Impact: 66.6 | O(N^2) | DB: 12)
  * `cob_decimal_get_field` (Impact: 56.8 | O(N^1) | DB: 7)
  * `cob_get_long_ebcdic_sign` (Impact: 41.4 | O(N^1) | DB: 18)
  * `cob_cmp_numdisp` (Impact: 40.2 | O(N^1) | DB: 16)
    * *Intent:* *val += 1;
  * `cob_add_packed` (Impact: 39.4 | O(N^1) | DB: 36)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 566`, `structural_boundaries: 225`, `args: 20`, `func_start: 75`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1353`, `fragile_debt: 3`, `orphaned_logic: 26`
* *Architecture:* `api: 267`, `import: 14`
* *Defense:* `safety: 43`, `doc: 2`, `immutability_locks: 63`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` libcob.h, coblocal.h, math.h, mpir.h, stdio.h, config.h, stdlib.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fodbc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.861 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.267 IQR)
- **Top Global Matches:** file_cluster_8: 13.861, file_cluster_13: 14.156, file_cluster_7: 14.203
- **Magnitude:** 2511.56 | **LOC:** 1871 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (73.2543%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `join_environment` (Impact: 201.2 | O(N^2) | DB: 72)
  * `chkSts` (Impact: 144.9 | O(N^1) | DB: 35)
  * `odbc_open` (Impact: 122.8 | O(N^1) | DB: 44)
  * `getOdbcMsg` (Impact: 67.3 | O(N^1) | DB: 38)
  * `chkOdbc` (Impact: 56.6 | O(N^1) | DB: 36)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 460`, `structural_boundaries: 189`, `args: 17`, `func_start: 30`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 1255`
* *Architecture:* `api: 215`, `import: 6`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sql.h, fileio.h, sqlca.h, sqlext.h, sqlcli1.h, sqludf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/foci.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.79 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.846 IQR)
- **Top Global Matches:** file_cluster_8: 13.79, file_cluster_13: 14.113, file_cluster_7: 14.136
- **Magnitude:** 2176.32 | **LOC:** 1664 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (72.2174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `join_environment` (Impact: 169.7 | O(N^3) | DB: 49)
  * `oci_open` (Impact: 118.8 | O(N^1) | DB: 44)
  * `chkSts` (Impact: 108.2 | O(N^1) | DB: 36)
  * `oci_setup_stmt` (Impact: 80.8 | O(N^2) | DB: 30)
  * `oci_read_next` (Impact: 50.4 | O(N^1) | DB: 27)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 386`, `structural_boundaries: 167`, `args: 16`, `func_start: 30`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 1093`
* *Architecture:* `api: 182`, `import: 2`
* *Defense:* `safety: 18`, `doc: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` oci.h, fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fisam.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.045 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.783 IQR)
- **Top Global Matches:** file_cluster_8: 14.045, file_cluster_13: 14.311, file_cluster_0: 14.388
- **Magnitude:** 2016.46 | **LOC:** 1670 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 95
- **Risk Profile:** Cognitive Load (79.4069%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isam_open` (Impact: 216.4 | O(N^1) | DB: 95)
  * `isam_read_next` (Impact: 125.2 | O(N^1) | DB: 73)
  * `fisretsts` (Impact: 53.5 | O(N^1))
  * `isam_rewrite` (Impact: 39.1 | O(N^1) | DB: 17)
  * `isam_start` (Impact: 31.7 | O(N^1) | DB: 44)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 470`, `structural_boundaries: 198`, `args: 17`, `func_start: 26`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 1089`
* *Architecture:* `io: 2`, `api: 179`, `import: 5`
* *Defense:* `safety: 14`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.093
  * `Choke Point (Betweenness):` 0.000476 | `Ripple Effect (Closeness):` 0.015385
  * `Imports (Out-Degree: 1):` fileio.h, isam.h, disam.h, vbisam.h, isconfig.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `libcob/fbdb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.772 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.614 IQR)
- **Top Global Matches:** file_cluster_8: 13.772, file_cluster_13: 14.074, file_cluster_0: 14.098
- **Magnitude:** 1971.36 | **LOC:** 2009 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 151
- **Risk Profile:** Cognitive Load (95.5101%), Tech Debt (12.7371%)
**Top Internal Functions/Classes:**
  * `ix_bdb_open` (Impact: 711.1 | O(N^2) | DB: 151)
  * `bdb_lock_record` (Impact: 37.8 | O(N^1) | DB: 30)
  * `bdb_nofile` (Impact: 35.5 | O(N^1) | DB: 7)
  * `bdb_test_record_lock` (Impact: 35.1 | O(N^1) | DB: 23)
  * `bdb_lock_file` (Impact: 27.0 | O(N^1) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 122`, `args: 11`, `func_start: 30`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 835`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 8`, `api: 154`, `import: 2`
* *Defense:* `safety: 31`, `immutability_locks: 24`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h, db.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/fextfh.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.002 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_8: 14.002, file_cluster_13: 14.321, file_cluster_7: 14.332
- **Magnitude:** 1967.42 | **LOC:** 1336 | **CtrlFlow:** 85.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (80.8318%), Tech Debt (15.3912%)
**Top Internal Functions/Classes:**
  * `EXTFH` (Impact: 571.9 | O(2^N) | DB: 61)
  * `copy_fcd_to_file` (Impact: 63.5 | O(N^1) | DB: 53)
  * `copy_file_to_fcd` (Impact: 59.0 | O(N^1) | DB: 62)
  * `update_fcd_to_file` (Impact: 30.1 | O(N^1) | DB: 21)
  * `update_file_to_fcd` (Impact: 27.6 | O(N^1) | DB: 17)
    * *Intent:* /* * Free up allocated memory
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 69`, `args: 15`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 917`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 192`, `import: 1`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fileio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/reportio.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.667 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_8: 13.667, file_cluster_13: 13.986, file_cluster_7: 14.051
- **Magnitude:** 1911.78 | **LOC:** 1836 | **CtrlFlow:** 85.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 69
- **Risk Profile:** Cognitive Load (83.0014%), Tech Debt (14.9926%)
**Top Internal Functions/Classes:**
  * `cob_report_generate` (Impact: 155.0 | O(N^2) | DB: 69)
  * `cob_report_terminate` (Impact: 80.3 | O(N^2) | DB: 20)
  * `dumpFlags` (Impact: 78.7 | O(N^1) | DB: 1)
  * `report_line` (Impact: 73.5 | O(N^1) | DB: 36)
  * `reportDumpOneLine` (Impact: 59.4 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 88`, `args: 1`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 971`, `planned_debt: 3`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 118`, `import: 9`
* *Defense:* `safety: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` libcob.h, coblocal.h, stdio.h, config.h, stdlib.h, ctype.h, errno.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/debug.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.85 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_8: 12.85, file_cluster_13: 13.109, file_cluster_7: 13.236
- **Magnitude:** 1359.94 | **LOC:** 1579 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (85.9757%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cb_tree_print` (Impact: 324.4 | O(2^N) | DB: 60)
  * `cb_tag_str` (Impact: 92.7 | O(N^1))
    * *Intent:* #include "config.h" #include "defaults.h" #include "cobc/cobc.h" #include "libcob/common.h" #include...
  * `print_program` (Impact: 49.3 | O(2^N) | DB: 29)
  * `cb_category_str` (Impact: 37.9 | O(N^1))
  * `print_field` (Impact: 16.9 | O(2^N) | DB: 38)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 159`, `args: 35`, `func_start: 34`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 494`
* *Architecture:* `io: 1`, `api: 144`, `import: 18`
* *Defense:* `safety: 5`, `doc: 4`, `test: 2`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` tree.h, vis.h, string.h, stddef.h, stat.h, ctype.h, common.h, config.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libcob/intrinsic.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.066 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.114 IQR)
- **Top Global Matches:** file_cluster_8: 13.066, file_cluster_13: 13.306, file_cluster_7: 13.477
- **Magnitude:** 1206.46 | **LOC:** 6809 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (88.63%), Tech Debt (73.9771%)
**Top Internal Functions/Classes:**
  * `cob_check_numval_f` (Impact: 77.8 | O(N^1) | DB: 26)
  * `numval` (Impact: 36.3 | O(N^1) | DB: 21)
    * *Intent:* /* NUMVAL */
  * `cob_alloc_field` (Impact: 19.3 | O(N^2) | DB: 8)
  * `locale_time` (Impact: 16.6 | O(N^2) | DB: 7)
  * `get_interval_and_current_year_from_args` (Impact: 12.4 | O(N^1) | DB: 8)
    * *Intent:* /* Get the sum of the squares of the differences from the mean */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 114`, `args: 33`, `func_start: 53`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 610`, `fragile_debt: 1`, `orphaned_logic: 36`
* *Architecture:* `api: 180`, `import: 19`
* *Defense:* `safety: 43`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` timeb.h, libcob.h, langinfo.h, coblocal.h, ctype.h, config.h, time.h, gmp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/config.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.913 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 4.714 IQR)
- **Top Global Matches:** file_cluster_13: 13.913, file_cluster_11: 14.008, file_cluster_8: 14.075
- **Magnitude:** 1137.74 | **LOC:** 818 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (68.909%), Tech Debt (14.696%)
**Top Internal Functions/Classes:**
  * `cb_config_entry` (Impact: 442.9 | O(N^2) | DB: 67)
  * `cb_load_conf_file` (Impact: 51.7 | O(N^1) | DB: 34)
  * `invalid_value` (Impact: 39.0 | O(N^2))
  * `cb_load_conf` (Impact: 27.0 | O(N^1) | DB: 10)
  * `cb_read_conf` (Impact: 25.0 | O(N^2) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 63`, `args: 14`, `func_start: 10`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 6`, `state_mutation: 445`, `dead_code: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 62`, `import: 12`
* *Defense:* `safety: 14`, `immutability_locks: 47`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` cobc.h, limits.h, tree.h, config.def, string.h, stdio.h, config.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/gcdiff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.68 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.964 IQR)
- **Top Global Matches:** file_cluster_8: 13.68, file_cluster_13: 13.706, file_cluster_11: 13.943
- **Magnitude:** 1121.66 | **LOC:** 775 | **CtrlFlow:** 88.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (83.5911%), Tech Debt (13.6916%)
**Top Internal Functions/Classes:**
  * `compare_file` (Impact: 297.8 | O(N^2) | DB: 90)
  * `set_option` (Impact: 83.8 | O(N^1) | DB: 9)
  * `main` (Impact: 50.5 | O(N^1) | DB: 55)
  * `gcd_usage` (Impact: 44.7 | O(N^2) | DB: 11)
  * `print_template` (Impact: 15.2 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 28`, `args: 12`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 527`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 14`, `api: 41`, `import: 16`
* *Defense:* `safety: 5`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` defaults.h, cobgetopt.h, libcob.h, stat.h, tarstamp.h, gettext.h, stdio.h, config.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `m4/ltsugar.m4` (M4 | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.646 IQR)
- **Top Global Matches:** file_cluster_8: 9.646, file_cluster_7: 10.497, file_cluster_17: 10.544
- **Magnitude:** 1031.95 | **LOC:** 125 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.7458%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `args: 69`, `func_start: 14`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobc/scanner.l` (YACC | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.708 IQR)
- **Top Global Matches:** file_cluster_8: 12.708, file_cluster_7: 13.18, file_cluster_13: 13.225
- **Magnitude:** 1030.74 | **LOC:** 2489 | **CtrlFlow:** 87.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (70.1288%), Tech Debt (33.7139%)
**Top Internal Functions/Classes:**
  * `error` (Impact: 55.5 | O(2^N) | DB: 16)
  * `error` (Impact: 20.4 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 43`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 924`, `planned_debt: 4`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.997
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/cobol85/report.pl` (PERL) | Magnitude: 592.14 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 562, indent_tabs: 302, branch: 146, structural_boundaries: 70
- `extras/CBL_OC_DUMP.cob` (COBOL) | Magnitude: 296.68 | Delta: **0.452 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 199, state_mutation: 60, structural_boundaries: 55, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/run_prog_manual.sh.in` (SHELL) | Magnitude: 53.54 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, io: 25, branch: 24, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/cobol85/summary.pl` (PERL) | Magnitude: 180.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 164, indent_tabs: 26, structural_boundaries: 21, encapsulation: 19
- `cobc/config.c` (C) | Magnitude: 1137.74 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 482, state_mutation: 445, branch: 232, pointers: 94
- `libcob/mlio.c` (C) | Magnitude: 513.84 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 277, state_mutation: 243, branch: 110, pointers: 101
- `libcob/cobgetopt.c` (C) | Magnitude: 72.3 | Delta: **0.393 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 46, macros: 14, branch: 13, api: 10
- `bin/cobcrun.c` (C) | Magnitude: 45.02 | Delta: **0.419 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 47, debug_prints: 21, state_mutation: 20, import: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `m4/extern-inline.m4` (M4) | Magnitude: 16.12 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 51, dead_code: 16, fragile_debt: 6, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `bin/gcdiff.c` (C) | Magnitude: 1121.66 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 562, state_mutation: 527, branch: 216, debug_prints: 83
- `copy/xfhfcd.cpy` (COBOL) | Magnitude: 0.53 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1, indent_spaces: 1
- `libcob/strings.c` (C) | Magnitude: 757.3 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 459, indent_tabs: 395, pointers: 166, branch: 115
- `libcob/termio.c` (C) | Magnitude: 987.16 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 521, state_mutation: 484, branch: 215, pointers: 195
- `cobc/cobc.c` (C) | Magnitude: 8418.92 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 3886, state_mutation: 3478, branch: 1314, pointers: 1022

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `m4/intl.m4` (M4) | Magnitude: 21.2 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 128, dead_code: 42, structural_boundaries: 32, dependency_injection: 32
- `build_aux/bootstrap` (SHELL) | Magnitude: 56.06 | Delta: **0.193 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 26, indent_spaces: 23, safety_bypasses: 22, state_mutation: 21

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `libcob/fisam.c` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libcob/fisam.c` -> **Severity: 1.378** (Embedded: 0.0154 * Error Risk: 89.5934%)
- `libcob/coblocal.h` -> **Severity: 0.696** (Embedded: 0.0714 * Error Risk: 9.7557%)
- `libcob/common.h` -> **Severity: 0.558** (Embedded: 0.0756 * Error Risk: 7.3883%)
- `libcob/fileio.h` -> **Severity: 0.262** (Embedded: 0.0492 * Error Risk: 5.3259%)
- `libcob/sysdefines.h` -> **Severity: 0.243** (Embedded: 0.0423 * Error Risk: 5.7324%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libcob/fileio.h` -> **Severity: 3550.7** (Blast Radius: 35.507 * Doc Risk: 100.0%)
- `libcob/common.h` -> **Severity: 2671.996** (Blast Radius: 27.112 * Doc Risk: 98.554%)
- `libcob/coblocal.h` -> **Severity: 2137.0** (Blast Radius: 21.37 * Doc Risk: 100.0%)
- `libcob.h` -> **Severity: 1402.571** (Blast Radius: 26.398 * Doc Risk: 53.1317%)
- `cobc/cobc.h` -> **Severity: 1292.4** (Blast Radius: 12.924 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
