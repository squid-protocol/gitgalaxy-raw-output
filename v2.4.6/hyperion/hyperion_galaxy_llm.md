# ARCHITECTURAL_BRIEF: hyperion
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/hyperion` |
| **Timestamp** | `2026-08-03T19:29:02.967188+00:00` |
| **Scan Duration** | `4.78s` |
| **Git Branch** | `master` |
| **Git Commit** | `bec74e3a3dc26acb251eb820b3aeafcee0576b88` |
| **Git Remote** | `https://github.com/hercules-390/hyperion.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 368 malicious artifacts.

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
| Total Artifacts | 1039 |
| Analyzed Artifacts (Scanned) | 643 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 396 |
| Total LOC | 192360 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 61.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4264 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2637 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9043 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 321 | 141639 | 49.9% |
| PLAINTEXT | 177 | 0 | 27.5% |
| HTML | 60 | 20558 | 9.3% |
| ASSEMBLY | 32 | 23480 | 5.0% |
| M4 | 29 | 2966 | 4.5% |
| BATCH | 7 | 1675 | 1.1% |
| SHELL | 5 | 334 | 0.8% |
| MARKDOWN | 4 | 0 | 0.6% |
| JCL | 3 | 688 | 0.5% |
| MAKEFILE | 2 | 760 | 0.3% |
| CSS | 1 | 120 | 0.2% |
| PERL | 1 | 139 | 0.2% |
| BINARY_THREAT | 1 | 1 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.848`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 374 | 58.2% |
| file_cluster_13 | 47 | 7.3% |
| file_cluster_7 | 11 | 1.7% |
| file_cluster_2 | 10 | 1.6% |
| file_cluster_9 | 9 | 1.4% |
| file_cluster_12 | 3 | 0.5% |
| file_cluster_11 | 3 | 0.5% |
| file_cluster_0 | 3 | 0.5% |
| file_cluster_6 | 1 | 0.2% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 181 | 28.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 396*

**Composition by Extension & Reason:**
- `.tst`: 62x Excluded (Unsupported Extension: '.tst'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 44x Excluded (Explicitly Denied Extension: '.gif')
- `.core`: 32x Excluded (Unsupported Extension: '.core'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.list`: 31x Excluded (Unsupported Extension: '.list'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.msvc`: 29x Excluded (Unsupported Extension: '.msvc'), 1x Excluded (Unsupported Extension: '.MSVC')
- `.cmake`: 19x Excluded (Unsupported Extension: '.cmake'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rexx`: 7x Unsupported Format (.rexx), 3x Excluded (Unsupported Extension: '.rexx'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.assemble`: 13x Excluded (Unsupported Extension: '.assemble')
- `.listing`: 13x Excluded (Unsupported Extension: '.listing')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 4119 LOC)
- `.am`: 8x Excluded (Unsupported Extension: '.am')
- `.subtst`: 7x Excluded (Unsupported Extension: '.subtst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.m4`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 5958 LOC), 1x Excluded (Machine-Generated Source Code Signature: 436 LOC)
- `.h`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 19650 commas in 1186 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2264 LOC)
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 32.5 | 11.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 24.6 | 5.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 16.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.6 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.7 | 7.6 | 8.7 | 0.0 |
| Concurrency Exposure | 0.0 | 93.4 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 44.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 47.6 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 96.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 50.8 | 47.5 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 1.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `html/hercconf.html` (Hits: 581)
- `html/hercfaq.html` (Hits: 224)
- `html/hercmsdl.html` (Hits: 141)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **hercules.h** (`hercules.h`) — 188 inbound connections
2. **hstdinc.h** (`hstdinc.h`) — 169 inbound connections
3. **opcode.h** (`opcode.h`) — 84 inbound connections
4. **hercules.css** (`html/hercules.css`) — 52 inbound connections
5. **inline.h** (`inline.h`) — 45 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **hstdinc.h** (`hstdinc.h`) — 77 outbound dependencies
2. **hercules.h** (`hercules.h`) — 44 outbound dependencies
3. **ltdl.c** (`ltdl.c`) — 26 outbound dependencies
4. **dyncrypt.c** (`crypto/dyncrypt.c`) — 11 outbound dependencies
5. **hsccmd.c** (`hsccmd.c`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `commadpt_thread` (@ `commadpt.c`) -> Impact: **5107.5** | LOC: 1517
  * *Intent:* /*-------------------------------------------------------------------*/ /* Parsing utilities */ /*----------------------------------------------------...
- `wait_sigq_resp` (@ `hscmisc.c`) -> Impact: **3960.0** | LOC: 1870
- `decNumberFromString` (@ `decNumber/decNumber.c`) -> Impact: **3917.3** | LOC: 2467
- `ckd_read_count` (@ `ckddasd.c`) -> Impact: **3664.3** | LOC: 1606
- `NP_update` (@ `panel.c`) -> Impact: **3332.2** | LOC: 1415
- `cckddasd_start` (@ `cckddasd.c`) -> Impact: **3118.5** | LOC: 1794
  * *Intent:* } /* end function cckddasd_close_device */ /*-------------------------------------------------------------------*/ /* Compressed ckd start/resume chan...
- `w32_init_hostinfo` (@ `w32util.c`) -> Impact: **2297.4** | LOC: 1330
- `testch` (@ `channel.c`) -> Impact: **2121.6** | LOC: 1452
  * *Intent:* /* PROGRAMMING NOTE: The tests below are purposely neither macros * or inlined routines. This is to permit breakpoints during
- `tapedev_execute_ccw` (@ `tapeccws.c`) -> Impact: **1959.5** | LOC: 1088
  * *Intent:* } /* end function TapeCommandIsValid */ /*********************************************************************/ /*************************************...
- `shared_ckd_init` (@ `shared.c`) -> Impact: **1714.1** | LOC: 675

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `ckd_read_count` (@ `ckddasd.c`) -> **O(2^N) [Recursive]**
- `commadpt_thread` (@ `commadpt.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /*-------------------------------------------------------------------*/ /* Parsing utilities */ /*----------------------------------------------------...
- `configure_storage` (@ `config.c`) -> **O(2^N) [Recursive]**
- `cpu_uninit` (@ `cpu.c`) -> **O(2^N) [Recursive]**
- `CTCI_Init` (@ `ctc_ctci.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // ==================================================================== // // ==================================================================== // ...
- `showf1` (@ `dasdseq.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // Open CKD image
- `decFinalize` (@ `decNumber/decCommon.h`) -> **O(2^N) [Recursive]**
- `hthread_initialize_rwlock` (@ `hthreads.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /*-------------------------------------------------------------------*/ /* Initialize a R/W lock */ /*------------------------------------------------...
- `hthreads_internal_init` (@ `hthreads.c`) -> **O(2^N) [Recursive]**
  * *Intent:* static int herc_pri_rvrsd; /* More negative is higher prio */ static int host_low_pri; /* Host policy minimim priority */ static int host_pri_amt; /* ...
- `hthread_initialize_lock` (@ `hthreads.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /*-------------------------------------------------------------------*/ /* Initialize a lock */ /*----------------------------------------------------...

### Highest Data Gravity (Database Complexity)
- `decNumberFromString` (@ `decNumber/decNumber.c`) -> DB Complexity: **463**
- `cckddasd_start` (@ `cckddasd.c`) -> DB Complexity: **369**
  * *Intent:* } /* end function cckddasd_close_device */ /*-------------------------------------------------------------------*/ /* Compressed ckd start/resume chan...
- `NP_update` (@ `panel.c`) -> DB Complexity: **365**
- `commadpt_thread` (@ `commadpt.c`) -> DB Complexity: **314**
  * *Intent:* /*-------------------------------------------------------------------*/ /* Parsing utilities */ /*----------------------------------------------------...
- `wait_sigq_resp` (@ `hscmisc.c`) -> DB Complexity: **299**
- `ckd_read_count` (@ `ckddasd.c`) -> DB Complexity: **270**
- `w32_init_hostinfo` (@ `w32util.c`) -> DB Complexity: **266**
- `testch` (@ `channel.c`) -> DB Complexity: **229**
  * *Intent:* /* PROGRAMMING NOTE: The tests below are purposely neither macros * or inlined routines. This is to permit breakpoints during
- `ecpsvm_dossm` (@ `ecpsvm.c`) -> DB Complexity: **196**
- `UpdateRegisters` (@ `dyngui.c`) -> DB Complexity: **158**
  * *Intent:* // Special GUI commands start with ']'. At the moment, all these special // gui commands tell us is what status information it's interested in...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 297 | 175590.16 | 42.85% | 16.32% |
| `decNumber` | 33 | 11097.64 | 33.35% | 31.96% |
| `m4` | 26 | 2071.02 | 6.76% | 11.18% |
| `tests` | 188 | 1132.94 | 0.52% | 0.0% |
| `util` | 11 | 1030.16 | 20.2% | 9.09% |
| `CMake` | 11 | 162.28 | 14.77% | 70.28% |
| `autoconf` | 3 | 118.92 | 32.22% | 66.67% |
| `crypto` | 8 | 30.68 | 37.42% | 18.18% |
| `scripts` | 1 | 15.54 | 9.46% | 0.0% |
| `man` | 4 | 8.92 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `autoconf/mkinstalldirs` -> **100.0%** Exposure
- `util/dasdlist` -> **100.0%** Exposure
- `CMake/CMakeHercTestAtomic.c` -> **100.0%** Exposure
- `CMake/CMakeHercTestRegparm3.c` -> **100.0%** Exposure
- `CMake/CMakeHercTestSync.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `1Stop` -> **100.0%** Exposure
- `1Stop-CMake` -> **100.0%** Exposure
- `GetGitHash` -> **100.0%** Exposure
- `util/dasdlist` -> **100.0%** Exposure
- `CMake/CMakeHercTestRegparm3.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `loadparm.c` -> **38** Orphaned Functions | **0** Duplicates
- `hsccmd.c` -> **28** Orphaned Functions | **0** Duplicates
- `hthreads.c` -> **23** Orphaned Functions | **0** Duplicates
- `fthreads.c` -> **21** Orphaned Functions | **0** Duplicates
- `decNumber/decContext.c` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bldcfg.c`** -> AI Confidence: **99.48%**
2. **`chsc.c`** -> AI Confidence: **99.48%**
3. **`console.c`** -> AI Confidence: **99.48%**
4. **`crypto/dyncrypt.c`** -> AI Confidence: **99.48%**
5. **`ctc_ptp.c`** -> AI Confidence: **99.48%**
6. **`dfp.c`** -> AI Confidence: **99.48%**
7. **`getopt.c`** -> AI Confidence: **99.48%**
8. **`hsccmd.c`** -> AI Confidence: **99.48%**
9. **`hscmisc.c`** -> AI Confidence: **99.48%**
10. **`panel.c`** -> AI Confidence: **99.48%**
11. **`pfpo.c`** -> AI Confidence: **99.48%**
12. **`qeth.c`** -> AI Confidence: **99.48%**
13. **`hercules.h`** -> AI Confidence: **99.42%**
14. **`hstdinc.h`** -> AI Confidence: **99.42%**
15. **`dyn76.c`** -> AI Confidence: **99.39%**
16. **`impl.c`** -> AI Confidence: **99.39%**
17. **`ltdl.c`** -> AI Confidence: **99.39%**
18. **`archlvl.c`** -> AI Confidence: **99.34%**
19. **`assist.c`** -> AI Confidence: **99.34%**
20. **`cardrdr.c`** -> AI Confidence: **99.34%**
21. **`cgibin.c`** -> AI Confidence: **99.34%**
22. **`channel.c`** -> AI Confidence: **99.34%**
23. **`ckddasd.c`** -> AI Confidence: **99.34%**
24. **`cmpsc.c`** -> AI Confidence: **99.34%**
25. **`cmpsc_2012.c`** -> AI Confidence: **99.34%**
26. **`cmpscmem.c`** -> AI Confidence: **99.34%**
27. **`commadpt.c`** -> AI Confidence: **99.34%**
28. **`con1052c.c`** -> AI Confidence: **99.34%**
29. **`control.c`** -> AI Confidence: **99.34%**
30. **`cpu.c`** -> AI Confidence: **99.34%**
31. **`ctc_ctci.c`** -> AI Confidence: **99.34%**
32. **`ctc_lcs.c`** -> AI Confidence: **99.34%**
33. **`dasdcopy.c`** -> AI Confidence: **99.34%**
34. **`dat.c`** -> AI Confidence: **99.34%**
35. **`decNumber/decNumber.c`** -> AI Confidence: **99.34%**
36. **`decNumber/decimal64.c`** -> AI Confidence: **99.34%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `dyn76.c` -> **100.0%** Exposure
- `hetmap.c` -> **0.0263%** Exposure
- `ltdl.c` -> **0.0004%** Exposure
- `hqadefs.h` -> **0.0002%** Exposure
- `tapedev.c` -> **0.0001%** Exposure
### Exploit Generation Surface
- `util/awswrite.jcl` -> **100.0%** Exposure
- `util/rawstape.jcl` -> **100.0%** Exposure
- `util/tapeconv.jcl` -> **99.9998%** Exposure
- `archlvl.c` -> **20.0%** Exposure
- `awstape.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `ctcadpt.c` -> **100.0%** Exposure
- `hstructs.h` -> **100.0%** Exposure
- `util/awswrite.jcl` -> **100.0%** Exposure
- `util/rawstape.jcl` -> **100.0%** Exposure
- `util/tapeconv.jcl` -> **100.0%** Exposure
### Raw Memory Manipulation
- `cardpch.c` -> **10.0%** Exposure
- `cardrdr.c` -> **10.0%** Exposure
- `cckddasd.c` -> **10.0%** Exposure
- `cgibin.c` -> **10.0%** Exposure
- `channel.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `1Stop` -> **100.0%** Exposure
- `1Stop-CMake` -> **100.0%** Exposure
- `GetGitHash` -> **100.0%** Exposure
- `archlvl.c` -> **100.0%** Exposure
- `awstape.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1168` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `decNumber/decContext.c` (C) -> Cumulative Risk: **763.32**
- **Archetype:** `file_cluster_13` (Distance: 13.227 IQR)
- **Magnitude:** 382.56 | **LOC:** 438 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9934%)
- **Heaviest Functions:** `decContextSetStatusFromString` (Impact: 61.3), `decContextSetStatusFromStringQuiet` (Impact: 61.3), `decContextStatusToString` (Impact: 18.2)

### 2. `tuntap.c` (C) -> Cumulative Risk: **756.96**
- **Archetype:** `file_cluster_13` (Distance: 13.818 IQR)
- **Magnitude:** 145.82 | **LOC:** 1367 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9947%)
- **Heaviest Functions:** `TUNTAP_SetMode` (Impact: 84.2), `tuntap_term` (Impact: 1.8)

### 3. `hscutl.c` (C) -> Cumulative Risk: **751.73**
- **Archetype:** `file_cluster_8` (Distance: 14.225 IQR)
- **Magnitude:** 1141.62 | **LOC:** 1462 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (94.5346%)
- **Heaviest Functions:** `strlcat` (Impact: 627.4), `herc_getopt_long` (Impact: 23.1), `strlcpy` (Impact: 21.2)

### 4. `hthreads.c` (C) -> Cumulative Risk: **746.5**
- **Archetype:** `file_cluster_8` (Distance: 13.08 IQR)
- **Magnitude:** 1835.28 | **LOC:** 1164 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9584%)
- **Heaviest Functions:** `hthread_create_thread` (Impact: 648.9), `hthread_initialize_rwlock` (Impact: 121.5), `hthreads_internal_init` (Impact: 87.1)

### 5. `hscutl2.c` (C) -> Cumulative Risk: **722.27**
- **Archetype:** `file_cluster_13` (Distance: 15.907 IQR)
- **Magnitude:** 139.1 | **LOC:** 113 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8798%)
- **Heaviest Functions:** `setpriority` (Impact: 43.2), `getpriority` (Impact: 42.9)

### 6. `loadparm.c` (C) -> Cumulative Risk: **721.74**
- **Archetype:** `file_cluster_8` (Distance: 12.593 IQR)
- **Magnitude:** 721.2 | **LOC:** 821 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9998%), Documentation (99.6584%)
- **Heaviest Functions:** `set_model` (Impact: 163.6), `get_RealCPCount` (Impact: 49.9), `copy_ebcdic_to_stringz` (Impact: 37.0)

### 7. `decNumber/decimal64.c` (C) -> Cumulative Risk: **717.71**
- **Archetype:** `file_cluster_8` (Distance: 15.076 IQR)
- **Magnitude:** 646.56 | **LOC:** 840 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (99.8776%)
- **Heaviest Functions:** `decDigitsFromDPD` (Impact: 51.3), `decDigitsToDPD` (Impact: 45.6), `decimal64Show` (Impact: 8.5)

### 8. `logmsg.c` (C) -> Cumulative Risk: **710.43**
- **Archetype:** `file_cluster_0` (Distance: 13.787 IQR)
- **Magnitude:** 496.74 | **LOC:** 579 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (92.2168%)
- **Heaviest Functions:** `vfwritemsg` (Impact: 80.3), `log_capture_writer` (Impact: 13.9), `log_route_search` (Impact: 10.8)

### 9. `losc.c` (C) -> Cumulative Risk: **707.73**
- **Archetype:** `file_cluster_8` (Distance: 12.05 IQR)
- **Magnitude:** 98.86 | **LOC:** 72 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7264%)
- **Heaviest Functions:** `losc_check` (Impact: 56.5), `losc_set` (Impact: 2.2)

### 10. `qeth.c` (C) -> Cumulative Risk: **705.94**
- **Archetype:** `file_cluster_8` (Distance: 14.21 IQR)
- **Magnitude:** 5112.68 | **LOC:** 6666 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (92.6193%)
- **Heaviest Functions:** `qeth_do_sync` (Impact: 912.9), `qeth_create_interface` (Impact: 783.1), `qeth_execute_ccw` (Impact: 442.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `commadpt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.07 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.836 IQR)
- **Top Global Matches:** file_cluster_8: 14.07, file_cluster_0: 14.405, file_cluster_7: 14.407
- **Magnitude:** 7074.86 | **LOC:** 3783 | **CtrlFlow:** 91.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 314
- **Risk Profile:** Cognitive Load (95.0196%), Tech Debt (14.9102%)
**Top Internal Functions/Classes:**
  * `commadpt_thread` (Impact: 5107.5 | O(2^N) | DB: 314)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Parsing utilities */ /*--...
  * `commadpt_read_tty` (Impact: 251.2 | O(N^6) | DB: 55)
  * `commadpt_initiate_userdial` (Impact: 117.5 | O(N^6) | DB: 20)
  * `SET_COMM_KEEPALIVE` (Impact: 51.1 | O(N^4) | DB: 4)
  * `connect_message` (Impact: 32.6 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 606`, `structural_boundaries: 54`, `args: 5`, `func_start: 15`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1290`, `dead_code: 9`, `fragile_debt: 3`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 85`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` commadpt.h, parser.h, hstdinc.h, hercules.h, devtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decNumber/decNumber.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.034 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.322 IQR)
- **Top Global Matches:** file_cluster_11: 16.034, file_cluster_0: 16.087, file_cluster_13: 16.144
- **Magnitude:** 6194.14 | **LOC:** 8142 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 463
- **Risk Profile:** Cognitive Load (96.7533%), Tech Debt (11.9291%)
**Top Internal Functions/Classes:**
  * `decNumberFromString` (Impact: 3917.3 | O(N^6) | DB: 463)
  * `decLnOp` (Impact: 160.2 | O(N^5) | DB: 58)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decNumberSubtract -- sub...
  * `decNumberToInt32` (Impact: 18.8 | O(N^1) | DB: 11)
  * `decNumberToUInt32` (Impact: 16.4 | O(N^1) | DB: 10)
  * `decNumberFromInt32` (Impact: 6.6 | O(N^1) | DB: 4)
    * *Intent:* #endif #if DECCHECK // Optional checking routines. Enabling these means that decNumber // and decCon...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 667`, `structural_boundaries: 138`, `args: 5`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1683`, `dead_code: 35`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 350`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 122`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, string.h, stdio.h, decNumber.h, stdlib.h, decNumberLocal.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ckddasd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.992 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.575 IQR)
- **Top Global Matches:** file_cluster_8: 13.992, file_cluster_7: 14.354, file_cluster_13: 14.391
- **Magnitude:** 5537.46 | **LOC:** 6157 | **CtrlFlow:** 95.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 270
- **Risk Profile:** Cognitive Load (96.7073%), Tech Debt (8.3669%)
**Top Internal Functions/Classes:**
  * `ckd_read_count` (Impact: 3664.3 | O(2^N) | DB: 270)
  * `ckddasd_hresume` (Impact: 179.6 | O(N^3) | DB: 24)
  * `ckddasd_read_track` (Impact: 128.7 | O(N^6) | DB: 86)
  * `ckd_build_sense` (Impact: 111.8 | O(N^6) | DB: 34)
  * `mt_advance` (Impact: 31.0 | O(N^3) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 704`, `structural_boundaries: 33`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1222`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 109`, `import: 5`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` hstdinc.h, sr.h, dasdblks.h, hercules.h, devtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `panel.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.881 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.682 IQR)
- **Top Global Matches:** file_cluster_8: 13.881, file_cluster_13: 14.128, file_cluster_7: 14.136
- **Magnitude:** 5513.18 | **LOC:** 3347 | **CtrlFlow:** 93.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 365
- **Risk Profile:** Cognitive Load (87.6819%), Tech Debt (8.5128%)
**Top Internal Functions/Classes:**
  * `NP_update` (Impact: 3332.2 | O(N^6) | DB: 365)
  * `set_console_title` (Impact: 195.0 | O(N^5) | DB: 5)
  * `NP_screen_redraw` (Impact: 140.9 | O(N^5) | DB: 34)
  * `do_panel_command` (Impact: 37.4 | O(N^3) | DB: 7)
    * *Intent:* /* 1 2 3 4 5 6 7 8 */ /* Line ....+....0....+....0....+....0....+....0....+....0....+....0....+....0...
  * `draw_text` (Impact: 33.1 | O(N^3) | DB: 5)
    * *Intent:* /////////////////////////////////////////////////////////////////////// static char *lmsbuf = NULL; ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 731`, `structural_boundaries: 55`, `args: 15`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 1417`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `api: 161`, `import: 7`
* *Defense:* `safety: 27`, `doc: 23`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` opcode.h, hstdinc.h, hercules.h, devtype.h, fillfnam.h, hconsole.h, history.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `qeth.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.21 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.304 IQR)
- **Top Global Matches:** file_cluster_8: 14.21, file_cluster_0: 14.417, file_cluster_11: 14.433
- **Magnitude:** 5112.68 | **LOC:** 6666 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 143
- **Risk Profile:** Cognitive Load (92.3502%), Tech Debt (17.8583%)
**Top Internal Functions/Classes:**
  * `qeth_do_sync` (Impact: 912.9 | O(2^N) | DB: 143)
  * `qeth_create_interface` (Impact: 783.1 | O(N^6) | DB: 130)
  * `qeth_execute_ccw` (Impact: 442.1 | O(N^6) | DB: 134)
    * *Intent:* *sbrem -= *sboff;
  * `copy_packet_to_storage` (Impact: 114.7 | O(N^6) | DB: 19)
    * *Intent:* } else { /* IP address removed from to table */
  * `process_input_queues` (Impact: 79.2 | O(N^6) | DB: 31)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 126`, `args: 7`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 1650`, `dead_code: 11`, `fragile_debt: 8`, `orphaned_logic: 6`
* *Architecture:* `io: 7`, `api: 396`
* *Defense:* `safety: 12`, `immutability_locks: 2`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` dbgtrace.h, hstdinc.h, hercifc.h, mpc.h, chsc.h, hercules.h, devtype.h, qeth.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hscmisc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.333 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.933 IQR)
- **Top Global Matches:** file_cluster_8: 14.333, file_cluster_13: 14.393, file_cluster_0: 14.426
- **Magnitude:** 5101.88 | **LOC:** 3015 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 299
- **Risk Profile:** Cognitive Load (95.9822%), Tech Debt (9.5212%)
**Top Internal Functions/Classes:**
  * `wait_sigq_resp` (Impact: 3960.0 | O(N^6) | DB: 299)
  * `are_any_cpus_started_intlock_held` (Impact: 13.1 | O(N^4) | DB: 2)
    * *Intent:* #include "hercules.h" #include "devtype.h" #include "opcode.h" #include "inline.h" #include "hconsol...
  * `are_all_cpus_stopped_intlock_held` (Impact: 13.1 | O(N^4) | DB: 2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Test if all CPUs are in s...
  * `are_any_cpus_started` (Impact: 2.0 | O(N^2) | DB: 1)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Test if any CPUs are in s...
  * `are_all_cpus_stopped` (Impact: 2.0 | O(N^2) | DB: 1)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Test if all CPUs are in s...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 91`, `args: 3`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 834`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 248`, `import: 10`
* *Defense:* `safety: 94`, `immutability_locks: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` esa390io.h, opcode.h, hstdinc.h, hscmisc.c, inline.h, hercules.h, devtype.h, hexdumpe.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `float.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.198 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.458 IQR)
- **Top Global Matches:** file_cluster_8: 14.198, file_cluster_7: 14.577, file_cluster_13: 14.658
- **Magnitude:** 4889.08 | **LOC:** 7873 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (70.3478%), Tech Debt (7.7303%)
**Top Internal Functions/Classes:**
  * `add_ef` (Impact: 224.1 | O(N^6) | DB: 44)
    * *Intent:* } /* end function add_lf */ /*-------------------------------------------------------------------*/ ...
  * `add_sf` (Impact: 150.9 | O(N^6) | DB: 25)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Static functions */ /*---...
  * `add_lf` (Impact: 150.9 | O(N^6) | DB: 25)
    * *Intent:* } /* end function add_sf */ /*-------------------------------------------------------------------*/ ...
  * `cmp_sf` (Impact: 134.5 | O(N^6) | DB: 16)
    * *Intent:* } /* end function add_ef */ /*-------------------------------------------------------------------*/ ...
  * `cmp_lf` (Impact: 134.5 | O(N^6) | DB: 16)
    * *Intent:* } /* end function cmp_sf */ /*-------------------------------------------------------------------*/ ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1015`, `structural_boundaries: 136`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `state_mutation: 2829`, `planned_debt: 1`
* *Architecture:* `api: 594`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` opcode.h, hstdinc.h, inline.h, hercules.h, float.c
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cckddasd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.967 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_8: 13.967, file_cluster_13: 14.213, file_cluster_11: 14.222
- **Magnitude:** 4778.08 | **LOC:** 6188 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 369
- **Risk Profile:** Cognitive Load (93.6846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cckddasd_start` (Impact: 3118.5 | O(N^6) | DB: 369)
    * *Intent:* } /* end function cckddasd_close_device */ /*-------------------------------------------------------...
  * `cckddasd_init_handler` (Impact: 28.0 | O(N^2) | DB: 34)
    * *Intent:* } /* end function cckddasd_term */ /*---------------------------------------------------------------...
  * `cckddasd_close_device` (Impact: 27.0 | O(N^2) | DB: 30)
    * *Intent:* } /* end function cckddasd_init_handler */ /*-------------------------------------------------------...
  * `cckddasd_init` (Impact: 20.4 | O(N^3) | DB: 27)
    * *Intent:* DLL_EXPORT CCKDBLK cckdblk; /* cckd global area */ /*-----------------------------------------------...
  * `cckddasd_term` (Impact: 8.4 | O(N^2) | DB: 3)
    * *Intent:* } /* end function cckddasd_init */ /*---------------------------------------------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 148`, `args: 25`, `func_start: 33`
* *Risk/State:* `state_mutation: 1224`, `dead_code: 2`
* *Architecture:* `io: 10`, `api: 315`, `import: 4`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` hstdinc.h, opcode.h, hercules.h, devtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ctc_ptp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.462 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.869 IQR)
- **Top Global Matches:** file_cluster_8: 14.462, file_cluster_0: 14.648, file_cluster_13: 14.653
- **Magnitude:** 4733.76 | **LOC:** 9608 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 148
- **Risk Profile:** Cognitive Load (65.3548%), Tech Debt (11.8338%)
**Top Internal Functions/Classes:**
  * `write_rrh_C108` (Impact: 441.1 | O(N^6) | DB: 75)
  * `write_hx0_00` (Impact: 376.2 | O(N^6) | DB: 99)
  * `ptp_unsol_int_thread` (Impact: 176.3 | O(N^6) | DB: 50)
  * `write_rrh_8108` (Impact: 130.3 | O(N^6) | DB: 37)
  * `ptp_init` (Impact: 110.3 | O(N^6) | DB: 48)
    * *Intent:* /* ------------------------------------------------------------------ */ /* Various constants used i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 603`, `structural_boundaries: 122`, `args: 3`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 128`, `state_mutation: 2203`, `dead_code: 23`, `fragile_debt: 2`, `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 513`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 2`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` opcode.h, hstdinc.h, ifaddrs.h, mpc.h, herc_getopt.h, hercules.h, ctc_ptp.h, ctcadpt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hsccmd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.382 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.35 IQR)
- **Top Global Matches:** file_cluster_8: 13.382, file_cluster_13: 13.646, file_cluster_7: 13.743
- **Magnitude:** 3714.38 | **LOC:** 8865 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (76.0275%), Tech Debt (29.9087%)
**Top Internal Functions/Classes:**
  * `mt_cmd` (Impact: 681.5 | O(N^6) | DB: 45)
  * `devinit_cmd` (Impact: 230.6 | O(N^6) | DB: 30)
  * `maxrates_cmd` (Impact: 202.7 | O(N^6) | DB: 30)
    * *Intent:* #endif
  * `savecore_cmd` (Impact: 201.4 | O(N^5) | DB: 45)
    * *Intent:* /* un-stop the unit record device and raise attention interrupt */ /* PRINTER or PUNCH */
  * `defsym_cmd` (Impact: 151.4 | O(N^3) | DB: 5)
    * *Intent:* #endif /* #ifdef OPTION_IODELAY_KLUDGE */ /*--------------------------------------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 111`, `args: 41`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 812`, `dead_code: 1`, `orphaned_logic: 28`
* *Architecture:* `io: 16`, `api: 190`, `import: 11`
* *Defense:* `safety: 5`, `doc: 2`, `immutability_locks: 11`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` opcode.h, ctcadpt.h, hstdinc.h, httpmisc.h, dasdtab.h, hercules.h, devtype.h, qeth.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `w32util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_7` (Drift: 14.984 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.982 IQR)
- **Top Global Matches:** file_cluster_7: 14.984, file_cluster_8: 15.112, file_cluster_13: 15.193
- **Magnitude:** 3536.54 | **LOC:** 4756 | **CtrlFlow:** 88.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 266
- **Risk Profile:** Cognitive Load (47.9416%), Tech Debt (14.0469%)
**Top Internal Functions/Classes:**
  * `w32_init_hostinfo` (Impact: 2297.4 | O(N^6) | DB: 266)
  * `clock_gettime` (Impact: 76.5 | O(N^4) | DB: 36)
  * `get_process_directory` (Impact: 13.6 | O(N^2) | DB: 3)
    * *Intent:* #endif
  * `expand_environ_vars` (Impact: 6.5 | O(N^1) | DB: 1)
    * *Intent:* #endif ////////////////////////////////////////////////////////////////////////////////////////// //...
  * `CountSetBits` (Impact: 5.2 | O(N^2) | DB: 7)
    * *Intent:* #endif ////////////////////////////////////////////////////////////////////////////////////////// //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 60`, `args: 14`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 866`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 241`
* *Defense:* `safety: 11`, `doc: 802`, `immutability_locks: 14`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hstdinc.h, hercules.h, dbgtrace.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `general1.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.448 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.985 IQR)
- **Top Global Matches:** file_cluster_8: 14.448, file_cluster_13: 14.841, file_cluster_7: 14.852
- **Magnitude:** 3165.9 | **LOC:** 6029 | **CtrlFlow:** 96.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (74.7574%), Tech Debt (8.0767%)
**Top Internal Functions/Classes:**
  * `DEF_INST` (Impact: 10.1 | O(N^5) | DB: 1)
    * *Intent:* #define _GENERAL1_C_ #endif #include "hercules.h" #include "opcode.h" #include "inline.h" #include "...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 736`, `structural_boundaries: 29`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 2729`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 368`, `import: 7`
* *Defense:* `safety: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` opcode.h, hstdinc.h, clock.h, inline.h, hercules.h, general1.c
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `console.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.721 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.176 IQR)
- **Top Global Matches:** file_cluster_8: 13.721, file_cluster_13: 13.927, file_cluster_11: 14.011
- **Magnitude:** 3116.64 | **LOC:** 4518 | **CtrlFlow:** 89.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 147
- **Risk Profile:** Cognitive Load (94.0305%), Tech Debt (13.4138%)
**Top Internal Functions/Classes:**
  * `loc3270_init_handler` (Impact: 1486.7 | O(N^6) | DB: 147)
  * `telnet_ev_handler` (Impact: 282.4 | O(N^6) | DB: 16)
    * *Intent:* //-------------------------------------------------------------- // PROGRAMMING NOTE: the TELNET_TEL...
  * `constty_execute_ccw` (Impact: 171.8 | O(N^6) | DB: 58)
  * `dumpbuf` (Impact: 56.8 | O(2^N) | DB: 3)
  * `finish_console_init` (Impact: 18.8 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 48`, `args: 10`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 887`, `dead_code: 2`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 147`, `import: 8`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 14`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` opcode.h, hstdinc.h, sr.h, hexterns.h, hercules.h, cnsllogo.h, devtype.h, hexdumpe.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `control.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.212 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.212 IQR)
- **Top Global Matches:** file_cluster_8: 14.212, file_cluster_7: 14.658, file_cluster_13: 14.698
- **Magnitude:** 2998.38 | **LOC:** 7573 | **CtrlFlow:** 96.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (80.1775%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1227`, `structural_boundaries: 43`, `args: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 42`, `state_mutation: 2529`, `dead_code: 3`
* *Architecture:* `api: 372`, `import: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` opcode.h, hstdinc.h, control.c, inline.h, hercules.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esame.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.068 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.187 IQR)
- **Top Global Matches:** file_cluster_8: 14.068, file_cluster_7: 14.497, file_cluster_13: 14.553
- **Magnitude:** 2981.06 | **LOC:** 8494 | **CtrlFlow:** 99.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (71.1576%), Tech Debt (7.9732%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 15`, `state_mutation: 2136`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 756`, `import: 7`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` opcode.h, hstdinc.h, esame.c, clock.h, inline.h, hercules.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `channel.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.627 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.6 IQR)
- **Top Global Matches:** file_cluster_8: 13.627, file_cluster_13: 13.919, file_cluster_7: 13.988
- **Magnitude:** 2975.56 | **LOC:** 6323 | **CtrlFlow:** 86.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 229
- **Risk Profile:** Cognitive Load (96.8483%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testch` (Impact: 2121.6 | O(N^6) | DB: 229)
    * *Intent:* /* PROGRAMMING NOTE: The tests below are purposely neither macros * or inlined routines. This is to ...
  * `queue_io_interrupt_and_update_status` (Impact: 80.4 | O(N^6) | DB: 6)
  * `IS_CCW_IMMEDIATE` (Impact: 9.4 | O(N^2))
    * *Intent:* #ifndef CHANNEL_INLINES #define CHANNEL_INLINES
  * `clear_subchannel_busy_scsw` (Impact: 3.4 | O(N^5) | DB: 1)
  * `clear_subchannel_busy` (Impact: 1.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 57`, `args: 3`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 635`
* *Architecture:* `api: 97`, `import: 7`
* *Defense:* `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` opcode.h, hstdinc.h, channel.c, chsc.h, hercules.h, devtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hRexx.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.524 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.173 IQR)
- **Top Global Matches:** file_cluster_8: 13.524, file_cluster_13: 13.821, file_cluster_11: 13.835
- **Magnitude:** 2763.36 | **LOC:** 1164 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 91
- **Risk Profile:** Cognitive Load (80.5298%), Tech Debt (8.703%)
**Top Internal Functions/Classes:**
  * `rexx_cmd` (Impact: 1336.7 | O(N^6) | DB: 91)
    * *Intent:* /*-------------------------------------------------------------------*/ /* rexx Command - manage the...
  * `exec_cmd` (Impact: 394.9 | O(N^5) | DB: 67)
    * *Intent:* /*-------------------------------------------------------------------*/ /* exec Command - execute a ...
  * `InitializePaths` (Impact: 47.3 | O(N^3) | DB: 28)
  * `exec_instore_cmd` (Impact: 45.0 | O(N^3) | DB: 9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* exec Command - execute an...
  * `InitializeExtensions` (Impact: 38.2 | O(N^3) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 49`, `args: 14`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 710`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 142`, `import: 3`
* *Defense:* `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hstdinc.h, hercules.h, hRexx.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tapeccws.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.214 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.943 IQR)
- **Top Global Matches:** file_cluster_8: 13.214, file_cluster_7: 13.491, file_cluster_13: 13.497
- **Magnitude:** 2600.58 | **LOC:** 4393 | **CtrlFlow:** 96.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 144
- **Risk Profile:** Cognitive Load (71.1222%), Tech Debt (19.0979%)
**Top Internal Functions/Classes:**
  * `tapedev_execute_ccw` (Impact: 1959.5 | O(N^5) | DB: 144)
    * *Intent:* } /* end function TapeCommandIsValid */ /***********************************************************...
  * `TapeCommandIsValid` (Impact: 12.2 | O(N^2) | DB: 10)
    * *Intent:* /*-------------------------------------------------------------------*/ /* */ /* Determine if a CCW ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 10`, `args: 5`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 470`, `dead_code: 4`, `fragile_debt: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 139`, `import: 3`
* *Defense:* `safety: 1`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hstdinc.h, tapedev.h, hercules.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dfp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.494 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.73 IQR)
- **Top Global Matches:** file_cluster_8: 13.494, file_cluster_7: 13.884, file_cluster_13: 13.95
- **Magnitude:** 2367.76 | **LOC:** 5085 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (66.0295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dfp_number_to_zoned` (Impact: 48.5 | O(N^4) | DB: 22)
  * `dfp_number_from_zoned` (Impact: 39.6 | O(N^4) | DB: 10)
  * `dfp_compare_exponent` (Impact: 38.5 | O(N^4) | DB: 5)
    * *Intent:* /* Set CF and BXCF S-bit */ } /* end function dfp128_set_cf_and_bxcf */ /*--------------------------...
  * `dfp_number_to_fix64` (Impact: 36.5 | O(N^3) | DB: 22)
    * *Intent:* } /* end function dfp_number_from_fix64 */ /*-------------------------------------------------------...
  * `dfp_number_to_fix32` (Impact: 36.5 | O(N^3) | DB: 22)
    * *Intent:* } /* end function dfp_number_from_u64 */ /*---------------------------------------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 48`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1297`
* *Architecture:* `api: 610`, `import: 10`
* *Defense:* `safety: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` decimal64.h, opcode.h, dfp.c, decimal32.h, hstdinc.h, inline.h, hercules.h, decPacked.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ecpsvm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.374 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.754 IQR)
- **Top Global Matches:** file_cluster_8: 13.374, file_cluster_13: 13.626, file_cluster_7: 13.694
- **Magnitude:** 2156.24 | **LOC:** 5113 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 196
- **Risk Profile:** Cognitive Load (83.7177%), Tech Debt (9.0964%)
**Top Internal Functions/Classes:**
  * `ecpsvm_dossm` (Impact: 830.7 | O(N^6) | DB: 196)
  * `ecpsvm_check_pswtrans` (Impact: 35.6 | O(N^4))
  * `ecpsvm_do_fretx` (Impact: 23.9 | O(N^3) | DB: 14)
  * `ecpsvm_do_disp1` (Impact: 19.6 | O(N^3) | DB: 14)
  * `ecpsvm_do_scnvu` (Impact: 12.6 | O(N^4) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 129`, `args: 16`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 986`, `dead_code: 5`, `fragile_debt: 2`
* *Architecture:* `api: 208`, `import: 7`
* *Defense:* `safety: 7`, `doc: 13`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` opcode.h, ecpsvm.c, hstdinc.h, inline.h, ecpsvm.h, hercules.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `codepage.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.069 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.536 IQR)
- **Top Global Matches:** file_cluster_8: 12.069, file_cluster_7: 12.486, file_cluster_13: 12.639
- **Magnitude:** 2142.08 | **LOC:** 1731 | **CtrlFlow:** 90.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 108
- **Risk Profile:** Cognitive Load (88.445%), Tech Debt (15.3283%)
**Top Internal Functions/Classes:**
  * `update_codepage` (Impact: 1218.2 | O(N^6) | DB: 108)
  * `imp_exp_error` (Impact: 95.6 | O(N^6) | DB: 5)
  * `set_codepage` (Impact: 53.7 | O(N^3) | DB: 8)
  * `import_file` (Impact: 25.7 | O(N^3) | DB: 17)
  * `prt_host_to_guest` (Impact: 25.6 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 24`, `args: 11`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 532`, `orphaned_logic: 11`
* *Architecture:* `io: 7`, `api: 102`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` hstdinc.h, hercules.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dasdutil.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.846 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.231 IQR)
- **Top Global Matches:** file_cluster_8: 13.846, file_cluster_13: 13.951, file_cluster_0: 14.009
- **Magnitude:** 2142.08 | **LOC:** 2289 | **CtrlFlow:** 76.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 114
- **Risk Profile:** Cognitive Load (71.4119%), Tech Debt (32.2027%)
**Top Internal Functions/Classes:**
  * `create_ckd` (Impact: 367.2 | O(N^5) | DB: 34)
  * `create_compressed_fba` (Impact: 364.4 | O(N^6) | DB: 114)
  * `valid_dsname` (Impact: 143.6 | O(N^3) | DB: 4)
  * `open_ckd_image` (Impact: 122.3 | O(N^6) | DB: 37)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Subroutine to open a CKD ...
  * `data_dump` (Impact: 118.9 | O(N^6) | DB: 29)
    * *Intent:* } /* end function make_asciiz */ /*-----------------------------------------------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 55`, `args: 11`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 593`, `dead_code: 2`, `orphaned_logic: 13`
* *Architecture:* `io: 33`, `api: 150`, `import: 5`
* *Defense:* `safety: 3`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` opcode.h, hstdinc.h, dasdblks.h, hercules.h, devtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `shared.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.823 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.765 IQR)
- **Top Global Matches:** file_cluster_8: 12.823, file_cluster_13: 13.029, file_cluster_0: 13.128
- **Magnitude:** 2142.0 | **LOC:** 3082 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 118
- **Risk Profile:** Cognitive Load (68.4242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `shared_ckd_init` (Impact: 1714.1 | O(2^N) | DB: 118)
  * `shared_update_notify` (Impact: 25.9 | O(N^6) | DB: 6)
    * *Intent:* /*-------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 41`, `args: 6`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 292`, `dead_code: 1`
* *Architecture:* `io: 7`, `api: 98`, `import: 4`
* *Defense:* `safety: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` hstdinc.h, opcode.h, hercules.h, devtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpserv.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.128 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.487 IQR)
- **Top Global Matches:** file_cluster_8: 13.128, file_cluster_13: 13.424, file_cluster_7: 13.487
- **Magnitude:** 2086.38 | **LOC:** 1263 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (77.3367%), Tech Debt (15.658%)
**Top Internal Functions/Classes:**
  * `http_command` (Impact: 458.1 | O(N^6) | DB: 30)
  * `http_request` (Impact: 274.8 | O(N^6) | DB: 48)
  * `http_server` (Impact: 196.7 | O(N^6) | DB: 26)
  * `http_unescape` (Impact: 89.0 | O(N^3) | DB: 17)
  * `http_root` (Impact: 56.1 | O(N^4) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 45`, `args: 8`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `state_mutation: 560`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 15`, `api: 147`, `import: 4`
* *Defense:* `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` hstdinc.h, hostinfo.h, httpmisc.h, hercules.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fbadasd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.795 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.111 IQR)
- **Top Global Matches:** file_cluster_8: 13.795, file_cluster_13: 14.069, file_cluster_11: 14.133
- **Magnitude:** 2042.08 | **LOC:** 1675 | **CtrlFlow:** 82.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 129
- **Risk Profile:** Cognitive Load (93.4765%), Tech Debt (13.6871%)
**Top Internal Functions/Classes:**
  * `fbadasd_execute_ccw` (Impact: 499.0 | O(N^6) | DB: 116)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Execute a Channel Command...
  * `fbadasd_init_handler` (Impact: 235.9 | O(N^6) | DB: 129)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Initialize the device han...
  * `fbadasd_hresume` (Impact: 106.5 | O(N^4) | DB: 8)
  * `fbadasd_read_blkgrp` (Impact: 65.0 | O(N^6) | DB: 61)
    * *Intent:* } /* end function fba_write */ /*-------------------------------------------------------------------...
  * `fba_write` (Impact: 34.7 | O(N^6) | DB: 23)
    * *Intent:* } /* end function fba_read */ /*-------------------------------------------------------------------*...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 64`, `args: 1`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 814`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 34`, `api: 122`, `import: 4`
* *Defense:* `safety: 3`, `immutability_locks: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` hstdinc.h, sr.h, dasdblks.h, hercules.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `hmalloc.h` (C) | Magnitude: 63.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 154, macros: 82, state_mutation: 37, branch: 33
- `loadmem.c` (C) | Magnitude: 992.92 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 332, state_mutation: 196, branch: 99, sec_reflection_metaprogramming: 82
- `logmsg.c` (C) | Magnitude: 496.74 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 320, indent_spaces: 252, branch: 61, api: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `decNumber/decCommon.h` (C) | Magnitude: 1774.24 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 619, indent_spaces: 484, branch: 199, bitwise_ops: 170
- `decNumber/decNumber.c` (C) | Magnitude: 6194.14 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1683, indent_spaces: 1651, pointers: 823, branch: 667
- `cckdutil.c` (C) | Magnitude: 1799.66 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 570, indent_spaces: 521, branch: 269, pointers: 163

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `util/dasdlist` (SHELL) | Magnitude: 47.32 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 30, safety_bypasses: 28, branch: 9, indent_spaces: 8
- `linklist.h` (C) | Magnitude: 45.58 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 540, indent_spaces: 47, pointers: 25, state_mutation: 20
- `cmpscmem.h` (C) | Magnitude: 58.54 | Delta: **0.16 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 260, macros: 104, indent_spaces: 66, reflection_metaprogramming: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cmpscput.h` (C) | Magnitude: 16.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 52, api: 3, import: 1, ownership: 1
- `tuntap.h` (C) | Magnitude: 63.52 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: macros: 71, indent_spaces: 68, api: 43, args: 18
- `hdl.c` (C) | Magnitude: 609.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 278, state_mutation: 232, pointers: 172, branch: 68
- `decNumber/example1.c` (C) | Magnitude: 12.14 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 18, pointers: 11, api: 4, state_mutation: 3
- `hao.c` (C) | Magnitude: 450.16 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 343, state_mutation: 230, branch: 88, pointers: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `html/hercmsds.html` (HTML) | Magnitude: 0.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 177, indent_spaces: 130, ui_framework: 68, args: 49
- `html/hercmsif.html` (HTML) | Magnitude: 0.02 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 56, indent_spaces: 36, ui_framework: 22, args: 13
- `html/hercmsdl.html` (HTML) | Magnitude: 0.18 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1164, indent_spaces: 897, ui_framework: 469, args: 274
- `html/hercmspr.html` (HTML) | Magnitude: 0.03 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 115, indent_spaces: 81, ui_framework: 49, args: 33
- `html/hercmsdg.html` (HTML) | Magnitude: 0.02 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 83, indent_spaces: 57, ui_framework: 33, io: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `cmpscdbg.h` (C) | Magnitude: 13.08 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 78, macros: 2, structural_boundaries: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `cmpsc_2012.c` (C) | Magnitude: 276.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 284, doc: 234, state_mutation: 188, pointers: 123
- `dyngui.c` (C) | Magnitude: 1114.28 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 780, state_mutation: 457, pointers: 407, doc: 338
- `tt32api.h` (C) | Magnitude: 113.6 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 319, api: 95, macros: 67, indent_spaces: 56
- `bootstrap.c` (C) | Magnitude: 34.82 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 156, indent_spaces: 119, branch: 21, macros: 19
- `w32stape.c` (C) | Magnitude: 338.52 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 280, indent_spaces: 179, state_mutation: 125, branch: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cckdswap.c` (C) | Magnitude: 294.8 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 93, pointers: 56, state_mutation: 47, branch: 42
- `timer.c` (C) | Magnitude: 542.66 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 186, state_mutation: 172, pointers: 63, branch: 59
- `softfloat_types.h` (C) | Magnitude: 18.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, class_start: 4, api: 4, ownership: 3
- `w32stape.h` (C) | Magnitude: 22.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 56, macros: 11, api: 7, args: 6
- `html/hercmscf.html` (HTML) | Magnitude: 0.11 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 687, indent_spaces: 609, ui_framework: 270, args: 190

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `cckdcdsk.c` (C) | Magnitude: 272.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, state_mutation: 45, branch: 33, pointers: 30
- `cckdcomp.c` (C) | Magnitude: 236.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, state_mutation: 41, pointers: 34, branch: 28
- `decNumber/example6.c` (C) | Magnitude: 42.42 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, pointers: 37, state_mutation: 19, api: 15
- `decNumber/example7.c` (C) | Magnitude: 9.88 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, pointers: 11, api: 4, structural_boundaries: 2
- `cmpscget.h` (C) | Magnitude: 26.34 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 78, api: 11, structural_boundaries: 5, indent_spaces: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `feature.h` -> **Severity: 0.288** (Bridge: 0.003 * Flux: 97.317%)
- `inline.h` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 100.0%)
- `hstructs.h` -> **Severity: 0.009** (Bridge: 0.0008 * Flux: 10.1107%)
- `hmacros.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 96.7606%)
- `herc_getopt.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 17.2828%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `chain.h` -> **Severity: 14.062** (Embedded: 0.1484 * Error Risk: 94.7762%)
- `extstring.h` -> **Severity: 13.631** (Embedded: 0.1484 * Error Risk: 91.8717%)
- `cpuint.h` -> **Severity: 10.331** (Embedded: 0.1484 * Error Risk: 69.6311%)
- `w32dl.h` -> **Severity: 10.035** (Embedded: 0.1527 * Error Risk: 65.7143%)
- `hinlines.h` -> **Severity: 8.981** (Embedded: 0.1484 * Error Risk: 60.5262%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `htypes.h` -> **Severity: 1337.0** (Blast Radius: 13.37 * Doc Risk: 100.0%)
- `hstdint.h` -> **Severity: 1233.164** (Blast Radius: 13.042 * Doc Risk: 94.5533%)
- `hercules.h` -> **Severity: 1124.668** (Blast Radius: 94.349 * Doc Risk: 11.9203%)
- `decNumber/decNumber.h` -> **Severity: 1095.8** (Blast Radius: 10.958 * Doc Risk: 100.0%)
- `decNumber/decContext.h` -> **Severity: 1095.153** (Blast Radius: 14.332 * Doc Risk: 76.4131%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
