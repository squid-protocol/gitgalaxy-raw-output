# ARCHITECTURAL_BRIEF: hyperion
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/hyperion` |
| **Timestamp** | `2026-08-07T03:51:13.288689+00:00` |
| **Scan Duration** | `4.59s` |
| **Git Branch** | `master` |
| **Git Commit** | `bec74e3a3dc26acb251eb820b3aeafcee0576b88` |
| **Git Remote** | `https://github.com/hercules-390/hyperion.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 368 malicious artifacts.

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
| Modularity | 0.4241 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 32.2 | 11.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 45.6 | 52.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.7 | 7.6 | 8.7 | 0.0 |
| Concurrency Exposure | 0.0 | 93.4 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 44.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 47.6 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 96.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.1 | 28.8 | 11.9 |
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

- `decNumberFromString` (@ `decNumber/decNumber.c`) -> Impact: **1207.3** | LOC: 2467
- `wait_sigq_resp` (@ `hscmisc.c`) -> Impact: **1198.2** | LOC: 1870
- `NP_update` (@ `panel.c`) -> Impact: **1002.6** | LOC: 1415
- `cckddasd_start` (@ `cckddasd.c`) -> Impact: **955.1** | LOC: 1794
  * *Intent:* } /* end function cckddasd_close_device */ /*-------------------------------------------------------------------*/ /* Compressed ckd start/resume chan...
- `panel_display_r` (@ `panel.c`) -> Impact: **805.0** | LOC: 1170
- `commadpt_thread` (@ `commadpt.c`) -> Impact: **794.7** | LOC: 1517
  * *Intent:* /*-------------------------------------------------------------------*/ /* Parsing utilities */ /*----------------------------------------------------...
- `w32_init_hostinfo` (@ `w32util.c`) -> Impact: **703.9** | LOC: 1330
- `tapedev_execute_ccw` (@ `tapeccws.c`) -> Impact: **689.4** | LOC: 1088
  * *Intent:* } /* end function TapeCommandIsValid */ /*********************************************************************/ /*************************************...
- `testch` (@ `channel.c`) -> Impact: **658.0** | LOC: 1452
  * *Intent:* /* PROGRAMMING NOTE: The tests below are purposely neither macros * or inlined routines. This is to permit breakpoints during
- `clear_subchan` (@ `channel.c`) -> Impact: **651.4** | LOC: 1424
  * *Intent:* #endif /* IOBUF_STRUCT */ /*--------------------------------------------------------------------*/ /* CCW prefetch data structure */ /*---------------...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 297 | 127319.96 | 42.66% | 16.95% |
| `decNumber` | 33 | 7801.14 | 32.15% | 33.61% |
| `m4` | 26 | 2070.02 | 6.76% | 11.18% |
| `tests` | 188 | 1132.94 | 0.52% | 0.0% |
| `util` | 11 | 919.32 | 18.36% | 9.09% |
| `CMake` | 11 | 144.18 | 14.77% | 70.28% |
| `autoconf` | 3 | 101.52 | 32.22% | 66.67% |
| `crypto` | 8 | 30.2 | 37.42% | 18.18% |
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
- `decNumber/decNumber.c` -> **36** Orphaned Functions | **0** Duplicates
- `hthreads.c` -> **30** Orphaned Functions | **0** Duplicates
- `hsccmd.c` -> **28** Orphaned Functions | **0** Duplicates
- `fthreads.c` -> **21** Orphaned Functions | **0** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1168` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `decNumber/decContext.c` (C) -> Cumulative Risk: **684.49**
- **Archetype:** `file_cluster_13` (Distance: 13.227 IQR)
- **Magnitude:** 285.56 | **LOC:** 438 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9821%), Tech Debt (98.6712%)
- **Heaviest Functions:** `decContextSetStatusFromString` (Impact: 18.8), `decContextSetStatusFromStringQuiet` (Impact: 18.8), `decContextStatusToString` (Impact: 18.2)

### 2. `hthreads.c` (C) -> Cumulative Risk: **670.51**
- **Archetype:** `file_cluster_8` (Distance: 13.101 IQR)
- **Magnitude:** 1184.38 | **LOC:** 1164 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9582%), Cognitive Load (96.2289%)
- **Heaviest Functions:** `hthread_create_thread` (Impact: 195.8), `locks_cmd` (Impact: 105.5), `herc2host` (Impact: 23.4)

### 3. `history.c` (C) -> Cumulative Risk: **655.91**
- **Archetype:** `file_cluster_13` (Distance: 14.337 IQR)
- **Magnitude:** 237.72 | **LOC:** 233 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.1337%), Safety Score (96.671%)
- **Heaviest Functions:** `history_add` (Impact: 14.5), `history_absolute_line` (Impact: 11.6), `history_relative_line` (Impact: 8.1)

### 4. `loadparm.c` (C) -> Cumulative Risk: **651.91**
- **Archetype:** `file_cluster_8` (Distance: 12.593 IQR)
- **Magnitude:** 527.9 | **LOC:** 821 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.5671%), Documentation (96.9855%)
- **Heaviest Functions:** `set_model` (Impact: 83.1), `get_RealCPCount` (Impact: 21.3), `copy_ebcdic_to_stringz` (Impact: 19.1)

### 5. `hscutl2.c` (C) -> Cumulative Risk: **639.18**
- **Archetype:** `file_cluster_13` (Distance: 15.907 IQR)
- **Magnitude:** 104.3 | **LOC:** 113 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.5666%), Tech Debt (92.4142%)
- **Heaviest Functions:** `setpriority` (Impact: 29.2), `getpriority` (Impact: 22.1)

### 6. `hscutl.c` (C) -> Cumulative Risk: **638.25**
- **Archetype:** `file_cluster_8` (Distance: 14.237 IQR)
- **Magnitude:** 900.42 | **LOC:** 1462 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.3738%), Tech Debt (92.3204%)
- **Heaviest Functions:** `set_socket_keepalive` (Impact: 193.4), `strlcat` (Impact: 192.4), `strlcpy` (Impact: 21.2)

### 7. `telnet.c` (C) -> Cumulative Risk: **621.58**
- **Archetype:** `file_cluster_8` (Distance: 11.746 IQR)
- **Magnitude:** 597.64 | **LOC:** 1807 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9961%), Documentation (99.7789%), Cognitive Load (93.5001%)
- **Heaviest Functions:** `telnet_opt_name` (Impact: 51.7), `telnet_cmd_name` (Impact: 27.6), `telnet_evt_name` (Impact: 21.2)

### 8. `cache.c` (C) -> Cumulative Risk: **602.48**
- **Archetype:** `file_cluster_8` (Distance: 12.403 IQR)
- **Magnitude:** 420.96 | **LOC:** 608 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9857%), Cognitive Load (93.9681%), State Flux (85.0%)
- **Heaviest Functions:** `cache_lookup` (Impact: 121.5), `cache_adjust` (Impact: 39.1), `cache_resize` (Impact: 26.1)

### 9. `decNumber/decimal64.c` (C) -> Cumulative Risk: **596.21**
- **Archetype:** `file_cluster_8` (Distance: 15.076 IQR)
- **Magnitude:** 625.56 | **LOC:** 840 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.931%), Cognitive Load (83.7574%)
- **Heaviest Functions:** `decDigitsFromDPD` (Impact: 51.3), `decDigitsToDPD` (Impact: 32.1), `decimal64Show` (Impact: 6.0)

### 10. `autoconf/mkinstalldirs` (SHELL) -> Cumulative Risk: **596.11**
- **Archetype:** `file_cluster_13` (Distance: 12.259 IQR)
- **Magnitude:** 86.56 | **LOC:** 102 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (96.6749%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 21.9), `Anonymous_Block` (Impact: 10.5), `Anonymous_Block` (Impact: 9.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `float.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.198 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.458 IQR)
- **Top Global Matches:** file_cluster_8: 14.198, file_cluster_7: 14.577, file_cluster_13: 14.658
- **Magnitude:** 4029.38 | **LOC:** 7873 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.3478%), Tech Debt (7.7303%)
**Top Internal Functions/Classes:**
  * `add_ef` (Impact: 71.6)
    * *Intent:* } /* end function add_lf */ /*-------------------------------------------------------------------*/ ...
  * `add_sf` (Impact: 48.5)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Static functions */ /*---...
  * `add_lf` (Impact: 48.5)
    * *Intent:* } /* end function add_sf */ /*-------------------------------------------------------------------*/ ...
  * `cmp_sf` (Impact: 42.0)
    * *Intent:* } /* end function add_ef */ /*-------------------------------------------------------------------*/ ...
  * `cmp_lf` (Impact: 42.0)
    * *Intent:* } /* end function cmp_sf */ /*-------------------------------------------------------------------*/ ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1015`, `structural_boundaries: 136`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `state_mutation: 2829`, `planned_debt: 1`
* *Architecture:* `api: 594`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` inline.h, hercules.h, opcode.h, hstdinc.h, float.c
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `decNumber/decNumber.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.063 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.323 IQR)
- **Top Global Matches:** file_cluster_11: 16.063, file_cluster_0: 16.11, file_cluster_13: 16.174
- **Magnitude:** 3982.54 | **LOC:** 8142 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.6452%), Tech Debt (66.194%)
**Top Internal Functions/Classes:**
  * `decNumberFromString` (Impact: 1207.3)
  * `decAddOp` (Impact: 111.8)
  * `decExpOp` (Impact: 68.5)
    * *Intent:* /* approx := .0819 + 2.59 * f % exponent */ /* end if */ /* */ /* var p:= 3 */ /* const maxp := curr...
  * `decNumberFMA` (Impact: 61.9)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decNumberDivideInteger -...
  * `decLnOp` (Impact: 60.2)
    * *Intent:* /* ------------------------------------------------------------------ */ /* decNumberSubtract -- sub...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 667`, `structural_boundaries: 138`, `args: 5`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1683`, `dead_code: 35`, `fragile_debt: 1`, `orphaned_logic: 36`
* *Architecture:* `api: 350`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 122`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string.h, ctype.h, decNumber.h, stdio.h, decNumberLocal.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `panel.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.882 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.681 IQR)
- **Top Global Matches:** file_cluster_8: 13.882, file_cluster_13: 14.129, file_cluster_7: 14.136
- **Magnitude:** 3698.78 | **LOC:** 3347 | **CtrlFlow:** 93.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.6307%), Tech Debt (8.9116%)
**Top Internal Functions/Classes:**
  * `NP_update` (Impact: 1002.6)
  * `panel_display_r` (Impact: 805.0)
  * `set_console_title` (Impact: 67.6)
  * `NP_screen_redraw` (Impact: 54.9)
  * `do_panel_command` (Impact: 19.5)
    * *Intent:* /* 1 2 3 4 5 6 7 8 */ /* Line ....+....0....+....0....+....0....+....0....+....0....+....0....+....0...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 731`, `structural_boundaries: 55`, `args: 15`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 1417`, `orphaned_logic: 3`
* *Architecture:* `io: 10`, `api: 161`, `import: 7`
* *Defense:* `safety: 27`, `doc: 23`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` history.h, hercules.h, devtype.h, hconsole.h, opcode.h, hstdinc.h, fillfnam.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ctc_ptp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.46 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.87 IQR)
- **Top Global Matches:** file_cluster_8: 14.46, file_cluster_0: 14.646, file_cluster_13: 14.651
- **Magnitude:** 3675.26 | **LOC:** 9608 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.3548%), Tech Debt (12.6797%)
**Top Internal Functions/Classes:**
  * `write_rrh_C108` (Impact: 146.1)
  * `write_hx0_00` (Impact: 133.7)
  * `write_rrh_417E` (Impact: 109.6)
  * `ptp_unsol_int_thread` (Impact: 58.9)
  * `write_rrh_8108` (Impact: 45.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 603`, `structural_boundaries: 122`, `args: 1`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 128`, `state_mutation: 2199`, `dead_code: 23`, `fragile_debt: 2`, `orphaned_logic: 11`
* *Architecture:* `io: 2`, `api: 513`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 2`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` hercules.h, ifaddrs.h, ctc_ptp.h, resolve.h, opcode.h, hstdinc.h, mpc.h, ctcadpt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cckddasd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.956 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.723 IQR)
- **Top Global Matches:** file_cluster_8: 13.956, file_cluster_13: 14.203, file_cluster_11: 14.213
- **Magnitude:** 3557.18 | **LOC:** 6188 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.2288%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cckddasd_start` (Impact: 955.1)
    * *Intent:* } /* end function cckddasd_close_device */ /*-------------------------------------------------------...
  * `cckd_write_trkimg` (Impact: 374.6)
  * `cckd_command` (Impact: 176.4)
    * *Intent:* } /* end function cckd_chk_space */ #endif // DEBUG_FREESPACE
  * `cckd_writer` (Impact: 88.9)
    * *Intent:* /* Return if reading the same track image */
  * `cckd_ra` (Impact: 65.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 148`, `args: 25`, `func_start: 33`
* *Risk/State:* `state_mutation: 1220`, `dead_code: 2`
* *Architecture:* `io: 10`, `api: 315`, `import: 4`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` hercules.h, opcode.h, devtype.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `qeth.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.209 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.302 IQR)
- **Top Global Matches:** file_cluster_8: 14.209, file_cluster_0: 14.415, file_cluster_11: 14.432
- **Magnitude:** 3172.18 | **LOC:** 6666 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.3183%), Tech Debt (22.0505%)
**Top Internal Functions/Classes:**
  * `qeth_create_interface` (Impact: 260.6)
  * `qeth_do_sync` (Impact: 164.7)
  * `qeth_execute_ccw` (Impact: 149.7)
    * *Intent:* *sbrem -= *sboff;
  * `copy_packet_to_storage` (Impact: 37.1)
    * *Intent:* } else { /* IP address removed from to table */
  * `process_l3_icmpv6_packet` (Impact: 34.0)
    * *Intent:* #endif /*defined(ENABLE_IPV6)*/
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 126`, `args: 7`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 1646`, `dead_code: 11`, `fragile_debt: 8`, `orphaned_logic: 11`
* *Architecture:* `io: 7`, `api: 396`
* *Defense:* `safety: 12`, `immutability_locks: 2`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` hercules.h, qeth.h, devtype.h, hercifc.h, chsc.h, resolve.h, hstdinc.h, dbgtrace.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `general1.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.448 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.986 IQR)
- **Top Global Matches:** file_cluster_8: 14.448, file_cluster_13: 14.841, file_cluster_7: 14.852
- **Magnitude:** 3159.8 | **LOC:** 6029 | **CtrlFlow:** 96.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2404%), Tech Debt (8.0767%)
**Top Internal Functions/Classes:**
  * `DEF_INST` (Impact: 4.0)
    * *Intent:* #define _GENERAL1_C_ #endif #include "hercules.h" #include "opcode.h" #include "inline.h" #include "...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 736`, `structural_boundaries: 29`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 2729`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 368`, `import: 7`
* *Defense:* `safety: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` inline.h, hercules.h, clock.h, general1.c, opcode.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `control.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.212 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.212 IQR)
- **Top Global Matches:** file_cluster_8: 14.212, file_cluster_7: 14.658, file_cluster_13: 14.698
- **Magnitude:** 2998.38 | **LOC:** 7573 | **CtrlFlow:** 96.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.7365%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1227`, `structural_boundaries: 43`, `args: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 42`, `state_mutation: 2529`, `dead_code: 3`
* *Architecture:* `api: 372`, `import: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` control.c, inline.h, hercules.h, opcode.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `esame.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.069 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.187 IQR)
- **Top Global Matches:** file_cluster_8: 14.069, file_cluster_7: 14.485, file_cluster_13: 14.541
- **Magnitude:** 2969.06 | **LOC:** 8494 | **CtrlFlow:** 99.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4668%), Tech Debt (7.9732%)
**Top Internal Functions/Classes:**
  * `DEF_INST` (Impact: 3.0)
    * *Intent:* #endif #if !defined(_ESAME_C_) #define _ESAME_C_ #endif #include "hercules.h" #include "opcode.h" #i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 15`, `state_mutation: 2136`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 756`, `import: 7`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` esame.c, inline.h, hercules.h, clock.h, opcode.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hscmisc.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.332 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 4.93 IQR)
- **Top Global Matches:** file_cluster_8: 14.332, file_cluster_13: 14.391, file_cluster_0: 14.423
- **Magnitude:** 2739.18 | **LOC:** 3015 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.093%), Tech Debt (9.5212%)
**Top Internal Functions/Classes:**
  * `wait_sigq_resp` (Impact: 1198.2)
  * `parse_range` (Impact: 88.1)
  * `FormatCRW` (Impact: 28.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* The following 2 routines ...
  * `herc_system` (Impact: 25.2)
  * `FormatND` (Impact: 24.8)
    * *Intent:* U64 opnd1, opnd2; /* Address/length operands */ U64 saddr, eaddr; /* Range start/end addresses */ in...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 91`, `args: 3`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 834`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 258`, `import: 10`
* *Defense:* `safety: 94`, `immutability_locks: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` hexdumpe.h, inline.h, hercules.h, esa390io.h, devtype.h, hconsole.h, hscmisc.c, opcode.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `commadpt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.065 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.836 IQR)
- **Top Global Matches:** file_cluster_8: 14.065, file_cluster_0: 14.401, file_cluster_7: 14.403
- **Magnitude:** 2725.86 | **LOC:** 3783 | **CtrlFlow:** 91.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.8841%), Tech Debt (14.9102%)
**Top Internal Functions/Classes:**
  * `commadpt_thread` (Impact: 794.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Parsing utilities */ /*--...
  * `commadpt_execute_ccw` (Impact: 306.8)
  * `commadpt_read_tty` (Impact: 78.7)
  * `commadpt_initiate_userdial` (Impact: 37.5)
  * `SET_COMM_KEEPALIVE` (Impact: 22.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 606`, `structural_boundaries: 54`, `args: 5`, `func_start: 15`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1290`, `dead_code: 9`, `fragile_debt: 3`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `api: 85`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` parser.h, hercules.h, devtype.h, commadpt.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `w32util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_7` (Drift: 15.018 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.98 IQR)
- **Top Global Matches:** file_cluster_7: 15.018, file_cluster_8: 15.146, file_cluster_13: 15.225
- **Magnitude:** 2277.74 | **LOC:** 4756 | **CtrlFlow:** 88.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.0066%), Tech Debt (42.0814%)
**Top Internal Functions/Classes:**
  * `w32_init_hostinfo` (Impact: 703.9)
  * `socket_init` (Impact: 148.8)
  * `w32_poor_mans_fork` (Impact: 120.0)
  * `clock_gettime` (Impact: 36.0)
  * `w32_read_piped_process_stdxxx_output_thr` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 60`, `args: 14`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 866`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 17`
* *Architecture:* `io: 3`, `api: 241`
* *Defense:* `safety: 11`, `doc: 802`, `immutability_locks: 14`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hercules.h, hstdinc.h, dbgtrace.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `channel.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.633 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.602 IQR)
- **Top Global Matches:** file_cluster_8: 13.633, file_cluster_13: 13.922, file_cluster_7: 13.992
- **Magnitude:** 2193.76 | **LOC:** 6323 | **CtrlFlow:** 86.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.6677%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testch` (Impact: 658.0)
    * *Intent:* /* PROGRAMMING NOTE: The tests below are purposely neither macros * or inlined routines. This is to ...
  * `clear_subchan` (Impact: 651.4)
    * *Intent:* #endif /* IOBUF_STRUCT */ /*--------------------------------------------------------------------*/ /...
  * `queue_io_interrupt_and_update_status` (Impact: 25.4)
  * `call_execute_ccw_chain` (Impact: 19.8)
    * *Intent:* } /* end function test_subchan */ /*----------------------------------------------------------------...
  * `device_reset` (Impact: 15.3)
    * *Intent:* #else #define IODELAY(_dev) #endif /*---------------------------------------------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 57`, `args: 3`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 635`
* *Architecture:* `api: 103`, `import: 7`
* *Defense:* `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` hercules.h, channel.c, devtype.h, chsc.h, opcode.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ckddasd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.992 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.575 IQR)
- **Top Global Matches:** file_cluster_8: 13.992, file_cluster_7: 14.354, file_cluster_13: 14.391
- **Magnitude:** 2178.46 | **LOC:** 6157 | **CtrlFlow:** 95.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.7073%), Tech Debt (8.3669%)
**Top Internal Functions/Classes:**
  * `ckd_read_count` (Impact: 592.3)
  * `ckddasd_hresume` (Impact: 93.6)
  * `ckddasd_read_track` (Impact: 46.2)
  * `ckd_build_sense` (Impact: 36.8)
  * `mt_advance` (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 704`, `structural_boundaries: 33`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1222`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 109`, `import: 5`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` sr.h, hercules.h, devtype.h, hstdinc.h, dasdblks.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dfp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.494 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.73 IQR)
- **Top Global Matches:** file_cluster_8: 13.494, file_cluster_7: 13.884, file_cluster_13: 13.95
- **Magnitude:** 2175.96 | **LOC:** 5085 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.0295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dfp_number_to_zoned` (Impact: 21.6)
  * `dfp_number_to_fix64` (Impact: 20.6)
    * *Intent:* } /* end function dfp_number_from_fix64 */ /*-------------------------------------------------------...
  * `dfp_number_to_fix32` (Impact: 20.6)
    * *Intent:* } /* end function dfp_number_from_u64 */ /*---------------------------------------------------------...
  * `dfp_number_from_zoned` (Impact: 17.1)
  * `dfp_compare_exponent` (Impact: 15.9)
    * *Intent:* /* Set CF and BXCF S-bit */ } /* end function dfp128_set_cf_and_bxcf */ /*--------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 48`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1297`
* *Architecture:* `api: 610`, `import: 10`
* *Defense:* `safety: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` inline.h, hercules.h, dfp.c, opcode.h, decimal128.h, hstdinc.h, decimal64.h, decimal32.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hsccmd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.369 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.348 IQR)
- **Top Global Matches:** file_cluster_8: 13.369, file_cluster_13: 13.633, file_cluster_7: 13.731
- **Magnitude:** 2102.88 | **LOC:** 8865 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.0275%), Tech Debt (29.9087%)
**Top Internal Functions/Classes:**
  * `mt_cmd` (Impact: 206.5)
  * `defsym_cmd` (Impact: 77.5)
    * *Intent:* #endif /* #ifdef OPTION_IODELAY_KLUDGE */ /*--------------------------------------------------------...
  * `savecore_cmd` (Impact: 73.4)
    * *Intent:* /* un-stop the unit record device and raise attention interrupt */ /* PRINTER or PUNCH */
  * `devinit_cmd` (Impact: 70.5)
  * `delsym_cmd` (Impact: 68.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* Add directory to AUTOMOUN...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 111`, `args: 33`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 812`, `dead_code: 1`, `orphaned_logic: 28`
* *Architecture:* `io: 16`, `api: 190`, `import: 11`
* *Defense:* `safety: 5`, `doc: 2`, `immutability_locks: 11`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` history.h, dasdtab.h, hercules.h, qeth.h, devtype.h, httpmisc.h, tapedev.h, ctc_ptp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `console.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.734 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.175 IQR)
- **Top Global Matches:** file_cluster_8: 13.734, file_cluster_13: 13.938, file_cluster_11: 14.021
- **Magnitude:** 2012.14 | **LOC:** 4518 | **CtrlFlow:** 89.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.636%), Tech Debt (14.6916%)
**Top Internal Functions/Classes:**
  * `loc3270_init_handler` (Impact: 457.9)
  * `build_logo` (Impact: 210.2)
  * `telnet_ev_handler` (Impact: 89.8)
    * *Intent:* //-------------------------------------------------------------- // PROGRAMMING NOTE: the TELNET_TEL...
  * `constty_execute_ccw` (Impact: 56.9)
  * `parse_sockspec` (Impact: 38.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 48`, `args: 7`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 887`, `dead_code: 2`, `fragile_debt: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 7`, `api: 147`, `import: 8`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 14`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` sr.h, hexdumpe.h, hercules.h, devtype.h, hexterns.h, opcode.h, hstdinc.h, cnsllogo.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `opcode.h` (C | Tier 0 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.558 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.5 IQR)
- **Top Global Matches:** file_cluster_8: 13.558, file_cluster_12: 13.974, file_cluster_7: 14.056
- **Magnitude:** 1994.52 | **LOC:** 4783 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6499%), Tech Debt (7.9327%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 662`, `structural_boundaries: 95`, `args: 18`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1676`, `fragile_debt: 1`
* *Architecture:* `api: 221`, `import: 2`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.855
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.146077
  * `Imports (Out-Degree: 1):` machdep.h, hercules.h
  * `Imported By (In-Degree: 84):` (Excluded from Brief to save tokens)

### `ecpsvm.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.401 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.756 IQR)
- **Top Global Matches:** file_cluster_8: 13.401, file_cluster_13: 13.648, file_cluster_7: 13.718
- **Magnitude:** 1989.44 | **LOC:** 5113 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.2117%), Tech Debt (9.0964%)
**Top Internal Functions/Classes:**
  * `ecpsvm_dossm` (Impact: 272.1)
  * `ecpsvm_dostosm` (Impact: 250.8)
  * `ecpsvm_dolra` (Impact: 37.6)
    * *Intent:* /* E607 DISP1 Instruction */ /* DISP1 : Early tests part 2 */ /* DISP1 Checks if the user is OK to r...
  * `ecpsvm_enable_disable` (Impact: 32.4)
  * `ecpsvm_enadisaall` (Impact: 21.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 129`, `args: 16`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 986`, `dead_code: 5`, `fragile_debt: 2`
* *Architecture:* `api: 214`, `import: 7`
* *Defense:* `safety: 7`, `doc: 13`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` inline.h, hercules.h, ecpsvm.c, opcode.h, ecpsvm.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `general2.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.125 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.993 IQR)
- **Top Global Matches:** file_cluster_8: 14.125, file_cluster_13: 14.477, file_cluster_0: 14.529
- **Magnitude:** 1989.02 | **LOC:** 2941 | **CtrlFlow:** 91.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.02%), Tech Debt (8.3722%)
**Top Internal Functions/Classes:**
  * `DEF_INST` (Impact: 2.7)
    * *Intent:* #endif #if !defined(_GENERAL2_C_) #define _GENERAL2_C_ #endif #include "hercules.h" #include "opcode...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 45`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 5`, `state_mutation: 1640`, `fragile_debt: 1`
* *Architecture:* `io: 28`, `api: 309`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` inline.h, hercules.h, clock.h, general2.c, opcode.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tapeccws.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.237 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.942 IQR)
- **Top Global Matches:** file_cluster_8: 13.237, file_cluster_7: 13.513, file_cluster_13: 13.519
- **Magnitude:** 1757.98 | **LOC:** 4393 | **CtrlFlow:** 96.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.1222%), Tech Debt (21.5387%)
**Top Internal Functions/Classes:**
  * `tapedev_execute_ccw` (Impact: 689.4)
    * *Intent:* } /* end function TapeCommandIsValid */ /***********************************************************...
  * `build_sense_3410_3420` (Impact: 156.9)
  * `build_sense_3590` (Impact: 143.6)
    * *Intent:* /* Calculate residual byte count... */ // PROGRAMMING NOTE: technically we *should* have up to // 64...
  * `build_sense_Streaming` (Impact: 92.2)
  * `BuildTapeSense` (Impact: 35.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 10`, `args: 5`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 470`, `dead_code: 4`, `fragile_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `api: 139`, `import: 3`
* *Defense:* `safety: 1`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hercules.h, tapedev.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `m4/gettext.m4` (M4 | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.536 IQR)
- **Top Global Matches:** file_cluster_8: 8.536, file_cluster_7: 9.345, file_cluster_0: 9.616
- **Magnitude:** 1711.42 | **LOC:** 550 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9428%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 35`, `args: 30`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `dead_code: 3`
* *Architecture:* `api: 23`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `w32ctca.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_7` (Drift: 14.344 IQR)
- **Local Micro-Species:** `Cluster 1: Algorithmic Bitwise & Encapsulated Core` (Drift: 6.401 IQR)
- **Top Global Matches:** file_cluster_7: 14.344, file_cluster_13: 14.405, file_cluster_8: 14.428
- **Magnitude:** 1670.16 | **LOC:** 459 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.0997%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 29`, `args: 9`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 95`
* *Architecture:* `io: 8`, `api: 47`, `import: 5`
* *Defense:* `doc: 450`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` hercules.h, w32ctca.h, tt32api.h, cygwin.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `makefile.bat` (MAKEFILE | Tier 1 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.341 IQR)
- **Top Global Matches:** file_cluster_8: 8.341, file_cluster_7: 9.343, file_cluster_1: 9.516
- **Magnitude:** 1667.12 | **LOC:** 1004 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.7303%), Tech Debt (10.8082%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `func_start: 44`
* *Risk/State:* `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hRexx.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.516 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.172 IQR)
- **Top Global Matches:** file_cluster_8: 13.516, file_cluster_13: 13.813, file_cluster_11: 13.827
- **Magnitude:** 1497.56 | **LOC:** 1164 | **CtrlFlow:** 86.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.5298%), Tech Debt (8.703%)
**Top Internal Functions/Classes:**
  * `rexx_cmd` (Impact: 401.7)
    * *Intent:* /*-------------------------------------------------------------------*/ /* rexx Command - manage the...
  * `exec_cmd` (Impact: 138.9)
    * *Intent:* /*-------------------------------------------------------------------*/ /* exec Command - execute a ...
  * `InitializePaths` (Impact: 25.3)
  * `exec_instore_cmd` (Impact: 24.2)
    * *Intent:* /*-------------------------------------------------------------------*/ /* exec Command - execute an...
  * `InitializeExtensions` (Impact: 20.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 49`, `args: 11`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 710`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 142`, `import: 3`
* *Defense:* `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.853
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` hercules.h, hRexx.h, hstdinc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `hmalloc.h` (C) | Magnitude: 60.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 154, macros: 82, state_mutation: 37, branch: 33
- `loadmem.c` (C) | Magnitude: 511.92 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 332, state_mutation: 196, branch: 99, sec_reflection_metaprogramming: 82
- `logmsg.c` (C) | Magnitude: 459.34 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 320, indent_spaces: 252, branch: 61, api: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `decNumber/decCommon.h` (C) | Magnitude: 948.64 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 619, indent_spaces: 484, branch: 199, bitwise_ops: 170
- `decNumber/decNumber.c` (C) | Magnitude: 3982.54 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1683, indent_spaces: 1651, pointers: 823, branch: 667
- `cckdutil.c` (C) | Magnitude: 1070.16 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 570, indent_spaces: 521, branch: 269, pointers: 163

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `util/dasdlist` (SHELL) | Magnitude: 57.32 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 30, safety_bypasses: 28, branch: 19, indent_spaces: 8
- `linklist.h` (C) | Magnitude: 45.58 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 540, indent_spaces: 47, pointers: 25, state_mutation: 20
- `cmpscmem.h` (C) | Magnitude: 58.54 | Delta: **0.16 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 260, macros: 104, indent_spaces: 66, reflection_metaprogramming: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cmpscput.h` (C) | Magnitude: 16.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 52, api: 3, import: 1, ownership: 1
- `tuntap.h` (C) | Magnitude: 63.52 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: macros: 71, indent_spaces: 68, api: 43, args: 17
- `hdl.c` (C) | Magnitude: 450.44 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 278, state_mutation: 232, pointers: 172, branch: 68
- `decNumber/example1.c` (C) | Magnitude: 12.14 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 18, pointers: 11, api: 4, state_mutation: 3
- `hao.c` (C) | Magnitude: 430.26 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
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
- `dyngui.c` (C) | Magnitude: 794.28 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 780, state_mutation: 457, pointers: 407, doc: 338
- `tt32api.h` (C) | Magnitude: 113.6 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 319, api: 95, macros: 67, indent_spaces: 56
- `bootstrap.c` (C) | Magnitude: 34.82 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 156, indent_spaces: 119, branch: 21, macros: 19
- `w32stape.c` (C) | Magnitude: 232.42 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 280, indent_spaces: 179, state_mutation: 125, branch: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cckdswap.c` (C) | Magnitude: 145.8 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 93, pointers: 56, state_mutation: 47, branch: 42
- `timer.c` (C) | Magnitude: 331.96 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 186, state_mutation: 172, pointers: 63, branch: 59
- `softfloat_types.h` (C) | Magnitude: 18.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, class_start: 4, api: 4, ownership: 3
- `w32stape.h` (C) | Magnitude: 22.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 56, macros: 11, api: 7, args: 6
- `hscutl.c` (C) | Magnitude: 900.42 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 345, indent_spaces: 257, branch: 113, api: 96

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `cckdcdsk.c` (C) | Magnitude: 125.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, state_mutation: 45, branch: 33, pointers: 30
- `cckdcomp.c` (C) | Magnitude: 111.18 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
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

- `chain.h` -> **Severity: 14.661** (Embedded: 0.1484 * Error Risk: 98.814%)
- `hstdinc.h` -> **Severity: 14.636** (Embedded: 0.2614 * Error Risk: 55.9978%)
- `extstring.h` -> **Severity: 14.587** (Embedded: 0.1484 * Error Risk: 98.3156%)
- `cpuint.h` -> **Severity: 14.043** (Embedded: 0.1484 * Error Risk: 94.6435%)
- `hinlines.h` -> **Severity: 13.68** (Embedded: 0.1484 * Error Risk: 92.1987%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `htypes.h` -> **Severity: 1337.0** (Blast Radius: 13.37 * Doc Risk: 100.0%)
- `hercules.h` -> **Severity: 1124.668** (Blast Radius: 94.349 * Doc Risk: 11.9203%)
- `decNumber/decNumber.h` -> **Severity: 1095.8** (Blast Radius: 10.958 * Doc Risk: 100.0%)
- `decNumber/decContext.h` -> **Severity: 974.044** (Blast Radius: 14.332 * Doc Risk: 67.9629%)
- `hstdint.h` -> **Severity: 870.512** (Blast Radius: 13.042 * Doc Risk: 66.7468%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
