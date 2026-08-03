# ARCHITECTURAL_BRIEF: curl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/curl` |
| **Timestamp** | `2026-08-03T20:10:02.996276+00:00` |
| **Scan Duration** | `3.42s` |
| **Git Branch** | `master` |
| **Git Commit** | `8f3f470baec57f5e53e11fc2ecaa749201ca9c0c` |
| **Git Remote** | `https://github.com/curl/curl` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 308 malicious artifacts.

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
| Total Artifacts | 4250 |
| Analyzed Artifacts (Scanned) | 430 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3820 |
| Total LOC | 78854 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 10.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4822 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2709 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1058 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 197 | 32784 | 45.8% |
| PERL | 72 | 20671 | 16.7% |
| PYTHON | 46 | 10400 | 10.7% |
| SHELL | 29 | 2155 | 6.7% |
| PLAINTEXT | 26 | 0 | 6.0% |
| M4 | 25 | 11733 | 5.8% |
| MARKDOWN | 19 | 0 | 4.4% |
| MAKEFILE | 8 | 509 | 1.9% |
| YAML | 3 | 124 | 0.7% |
| BATCH | 2 | 339 | 0.5% |
| DOCKERFILE | 1 | 10 | 0.2% |
| JSON | 1 | 111 | 0.2% |
| HTML | 1 | 18 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.392`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 195 | 45.3% |
| file_cluster_13 | 123 | 28.6% |
| file_cluster_0 | 34 | 7.9% |
| file_cluster_17 | 11 | 2.6% |
| file_cluster_9 | 9 | 2.1% |
| file_cluster_12 | 6 | 1.4% |
| file_cluster_11 | 5 | 1.2% |
| file_cluster_4 | 2 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 45 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3820*

**Composition by Extension & Reason:**
- `no_extension`: 1892x Unsupported Format (.undeterminable), 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 89 LOC)
- `.md`: 900x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 564x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 47 LOC), 2x Excluded (Machine-Generated Source Code Signature: 49 LOC)
- `.h`: 181x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 144 LOC)
- `.cmake`: 30x Excluded (Unsupported Extension: '.cmake')
- `.yml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.am`: 12x Excluded (Unsupported Extension: '.am'), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.com`: 18x Excluded (Unsupported Extension: '.com'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 250 LOC), 1x Excluded (Machine-Generated Source Code Signature: 157 LOC)
- `.txt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.prm`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.in`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sln`: 3x Excluded (Unsupported Extension: '.sln')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 32.9 | 26.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 35.2 | 21.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.5 | 5.6 | 5.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.1 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.1 | 0.3 | 0.1 | 0.0 |
| Volatility Exposure | 0.0 | 85.5 | 17.6 | 12.9 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 34.5 | 10.1 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 53.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 13.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 30.0 | 20.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/ech_tests.sh` (Hits: 128)
- `tests/http/testenv/curl.py` (Hits: 57)
- `scripts/wcurl` (Hits: 56)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **tool_setup.h** (`src/tool_setup.h`) — 80 inbound connections
2. **tool_cfgable.h** (`src/tool_cfgable.h`) — 33 inbound connections
3. **tool_msgs.h** (`src/tool_msgs.h`) — 24 inbound connections
4. **tool_operate.h** (`src/tool_operate.h`) — 11 inbound connections
5. **first.h** (`tests/server/first.h`) — 11 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **tool_operate.c** (`src/tool_operate.c`) — 39 outbound dependencies
2. **runtests.pl** (`tests/runtests.pl`) — 37 outbound dependencies
3. **ftpserver.pl** (`tests/ftpserver.pl`) — 29 outbound dependencies
4. **runner.pm** (`tests/runner.pm`) — 28 outbound dependencies
5. **servers.pm** (`tests/servers.pm`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `singletest_count` (@ `tests/runtests.pl`) -> Impact: **7446.7** | LOC: 1987
  * *Intent:* ####################################################################### # Print the test name and count tests
- `render` (@ `scripts/managen`) -> Impact: **7237.9** | LOC: 1069
- `checkcmd` (@ `tests/servers.pm`) -> Impact: **6757.0** | LOC: 2014
  * *Intent:* ####################################################################### # Check for a command in the PATH of the test server. #
- `disc_handshake` (@ `tests/ftpserver.pl`) -> Impact: **6506.2** | LOC: 2333
  * *Intent:* # Perform the disconnect handshake with sockfilt on the secondary connection # (the only connection we actively disconnect). # This involves waiting f...
- `msdosify` (@ `src/tool_doswin.c`) -> Impact: **2420.2** | LOC: 523
  * *Intent:* #endif /* * Test if truncating a path to a file leaves at least a single character * in the filename. Filenames suffixed by an alternate data stream c...
- `runner_init` (@ `tests/runner.pm`) -> Impact: **1629.7** | LOC: 950
  * *Intent:* ####################################################################### # Initialize the runner and prepare it to run tests # The runner ID returned b...
- `rtspd_ProcessRequest` (@ `tests/server/rtspd.c`) -> Impact: **1544.8** | LOC: 377
  * *Intent:* #define REQUEST_KEYWORD_SIZE_TXT "255" #define CMD_AUTH_REQUIRED "auth_required" /* 'idle' means that it will accept the request fine but never respon...
- `do_requests` (@ `tests/http/scorecard.py`) -> Impact: **1512.0** | LOC: 406
- `memanalyze` (@ `tests/memanalyzer.pm`) -> Impact: **1115.2** | LOC: 390
- `single` (@ `scripts/cd2nroff`) -> Impact: **1025.1** | LOC: 255

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `render` (@ `scripts/managen`) -> **O(2^N) [Recursive]**
- `disc_handshake` (@ `tests/ftpserver.pl`) -> **O(2^N) [Recursive]**
  * *Intent:* # Perform the disconnect handshake with sockfilt on the secondary connection # (the only connection we actively disconnect). # This involves waiting f...
- `singletest_count` (@ `tests/runtests.pl`) -> **O(2^N) [Recursive]**
  * *Intent:* ####################################################################### # Print the test name and count tests
- `checkcmd` (@ `tests/servers.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* ####################################################################### # Check for a command in the PATH of the test server. #
- `scan_man_page` (@ `tests/test1222.pl`) -> **O(2^N) [Recursive]**
  * *Intent:* # Scan man page for deprecation in DESCRIPTION and/or AVAILABILITY sections.
- `msdosify` (@ `src/tool_doswin.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif /* * Test if truncating a path to a file leaves at least a single character * in the filename. Filenames suffixed by an alternate data stream c...
- `tool2curlparts` (@ `src/tool_formparse.c`) -> **O(2^N) [Recursive]**
- `parallel_event` (@ `src/tool_operate.c`) -> **O(2^N) [Recursive]**
- `on_uv_timeout` (@ `src/tool_operate.c`) -> **O(2^N) [Recursive]**
  * *Intent:* /* VMS Note: * * Reading binary from files can be a problem... Only FIXED, VAR
- `libcurl_generate_mime_part` (@ `src/tool_setopt.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `checkcmd` (@ `tests/servers.pm`) -> DB Complexity: **676**
  * *Intent:* ####################################################################### # Check for a command in the PATH of the test server. #
- `singletest_count` (@ `tests/runtests.pl`) -> DB Complexity: **476**
  * *Intent:* ####################################################################### # Print the test name and count tests
- `Anonymous_Block_[Truncated]` (@ `tests/ech_tests.sh`) -> DB Complexity: **405**
- `disc_handshake` (@ `tests/ftpserver.pl`) -> DB Complexity: **375**
  * *Intent:* # Perform the disconnect handshake with sockfilt on the secondary connection # (the only connection we actively disconnect). # This involves waiting f...
- `render` (@ `scripts/managen`) -> DB Complexity: **344**
- `runner_init` (@ `tests/runner.pm`) -> DB Complexity: **251**
  * *Intent:* ####################################################################### # Initialize the runner and prepare it to run tests # The runner ID returned b...
- `Anonymous_Block_[Truncated]` (@ `projects/OS400/initscript.sh`) -> DB Complexity: **155**
- `memanalyze` (@ `tests/memanalyzer.pm`) -> DB Complexity: **148**
- `checksystemfeatures` (@ `tests/runtests.pl`) -> DB Complexity: **139**
  * *Intent:* ####################################################################### # Check & display information about curl and the host the test suite runs on. ...
- `rtspd_ProcessRequest` (@ `tests/server/rtspd.c`) -> DB Complexity: **131**
  * *Intent:* #define REQUEST_KEYWORD_SIZE_TXT "255" #define CMD_AUTH_REQUIRED "auth_required" /* 'idle' means that it will accept the request fine but never respon...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests` | 52 | 47236.66 | 37.25% | 0.0% |
| `src` | 91 | 31998.46 | 37.68% | 17.31% |
| `scripts` | 37 | 16719.25 | 73.3% | 41.41% |
| `tests/server` | 14 | 15498.06 | 32.36% | 0.0% |
| `tests/http` | 31 | 10384.14 | 6.02% | 0.0% |
| `tests/unit` | 71 | 9512.5 | 19.91% | 0.0% |
| `tests/http/testenv` | 13 | 8162.38 | 28.65% | 0.0% |
| `projects/OS400` | 12 | 3958.86 | 53.12% | 48.42% |
| `.github/scripts` | 18 | 1077.1 | 46.01% | 38.65% |
| `m4` | 20 | 879.79 | 4.3% | 6.01% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/scripts/cmp-pkg-config.sh` -> **100.0%** Exposure
- `.github/scripts/shellcheck.sh` -> **100.0%** Exposure
- `.github/scripts/typos.sh` -> **100.0%** Exposure
- `.github/scripts/yamlcheck.sh` -> **100.0%** Exposure
- `buildconf` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/scripts/cleancmd.pl` -> **100.0%** Exposure
- `.github/scripts/randcurl.pl` -> **100.0%** Exposure
- `.github/scripts/trimmarkdownheader.pl` -> **100.0%** Exposure
- `.github/scripts/verify-examples.pl` -> **100.0%** Exposure
- `.github/scripts/verify-synopsis.pl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/http/test_02_download.py` -> **38** Orphaned Functions | **0** Duplicates
- `tests/http/test_07_upload.py` -> **38** Orphaned Functions | **0** Duplicates
- `CMake/CurlTests.c` -> **0** Orphaned Functions | **23** Duplicates
- `src/tool_getparam.c` -> **23** Orphaned Functions | **0** Duplicates
- `tests/http/test_01_basic.py` -> **20** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/config2setopts.c`** -> AI Confidence: **99.48%**
2. **`src/curlinfo.c`** -> AI Confidence: **99.48%**
3. **`src/tool_doswin.c`** -> AI Confidence: **99.48%**
4. **`src/tool_main.c`** -> AI Confidence: **99.48%**
5. **`src/tool_parsecfg.c`** -> AI Confidence: **99.48%**
6. **`tests/server/tftpd.c`** -> AI Confidence: **99.48%**
7. **`projects/OS400/ccsidcurl.c`** -> AI Confidence: **99.39%**
8. **`src/tool_cb_hdr.c`** -> AI Confidence: **99.39%**
9. **`src/tool_getparam.c`** -> AI Confidence: **99.39%**
10. **`src/tool_help.c`** -> AI Confidence: **99.39%**
11. **`src/tool_ssls.c`** -> AI Confidence: **99.39%**
12. **`src/var.c`** -> AI Confidence: **99.39%**
13. **`src/tool_cb_dbg.c`** -> AI Confidence: **99.34%**
14. **`src/tool_filetime.c`** -> AI Confidence: **99.34%**
15. **`src/tool_formparse.c`** -> AI Confidence: **99.34%**
16. **`tests/tunit/tool1604.c`** -> AI Confidence: **99.32%**
17. **`tests/unit/unit1612.c`** -> AI Confidence: **99.32%**
18. **`tests/unit/unit1654.c`** -> AI Confidence: **99.32%**
19. **`projects/OS400/os400sys.c`** -> AI Confidence: **99.31%**
20. **`src/tool_cb_rea.c`** -> AI Confidence: **99.31%**
21. **`src/tool_operate.c`** -> AI Confidence: **99.31%**
22. **`src/tool_paramhlp.c`** -> AI Confidence: **99.31%**
23. **`tests/dictserver.py`** -> AI Confidence: **99.31%**
24. **`tests/http/scorecard.py`** -> AI Confidence: **99.31%**
25. **`tests/http/test_02_download.py`** -> AI Confidence: **99.31%**
26. **`tests/http/test_10_proxy.py`** -> AI Confidence: **99.31%**
27. **`appveyor.sh`** -> AI Confidence: **99.29%**
28. **`buildconf`** -> AI Confidence: **99.29%**
29. **`scripts/pythonlint.sh`** -> AI Confidence: **99.29%**
30. **`tests/ech_tests.sh`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tests/unit/unit1307.c` -> **13.0121%** Exposure
- `tests/unit/unit1666.c` -> **0.0003%** Exposure
- `tests/unit/unit1650.c` -> **0.0001%** Exposure
- `tests/unit/unit1658.c` -> **0.0001%** Exposure
### Exploit Generation Surface
- `.github/scripts/cleancmd.pl` -> **100.0%** Exposure
- `.github/scripts/cmp-config.pl` -> **100.0%** Exposure
- `.github/scripts/randcurl.pl` -> **100.0%** Exposure
- `.github/scripts/verify-examples.pl` -> **100.0%** Exposure
- `.github/scripts/verify-synopsis.pl` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `.github/scripts/cleancmd.pl` -> **100.0%** Exposure
- `.github/scripts/cmp-config.pl` -> **100.0%** Exposure
- `.github/scripts/randcurl.pl` -> **100.0%** Exposure
- `.github/scripts/verify-synopsis.pl` -> **100.0%** Exposure
- `scripts/badwords` -> **100.0%** Exposure
### Raw Memory Manipulation
- `src/config2setopts.c` -> **10.0%** Exposure
- `src/tool_cb_hdr.c` -> **10.0%** Exposure
- `src/tool_operate.c` -> **10.0%** Exposure
- `src/tool_getparam.c` -> **9.999%** Exposure
- `tests/server/sws.c` -> **9.999%** Exposure
### Hardcoded Payload Artifacts
- `scripts/mk-ca-bundle.pl` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `.github/scripts/cleancmd.pl` -> **100.0%** Exposure
- `.github/scripts/randcurl.pl` -> **100.0%** Exposure
- `.github/scripts/verify-synopsis.pl` -> **100.0%** Exposure
- `scripts/cd2cd` -> **100.0%** Exposure
- `scripts/cd2nroff` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1464` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/mk-ca-bundle.pl` (PERL) -> Cumulative Risk: **837.64**
- **Archetype:** `file_cluster_0` (Distance: 13.553 IQR)
- **Magnitude:** 691.4 | **LOC:** 677 | **CtrlFlow:** 80.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `warning_message` (Impact: 222.6), `sha256` (Impact: 48.8), `should_output_cert` (Impact: 30.1)

### 2. `src/tool_operhlp.c` (C) -> Cumulative Risk: **812.89**
- **Archetype:** `file_cluster_13` (Distance: 13.624 IQR)
- **Magnitude:** 397.28 | **LOC:** 246 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `add_file_name_to_url` (Impact: 109.5), `get_url_file_name` (Impact: 51.1), `urlerr_cvt` (Impact: 8.6)

### 3. `.github/scripts/verify-synopsis.pl` (PERL) -> Cumulative Risk: **810.04**
- **Archetype:** `file_cluster_13` (Distance: 12.604 IQR)
- **Magnitude:** 145.1 | **LOC:** 88 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `extract` (Impact: 102.2), `testcompile` (Impact: 1.8)

### 4. `.github/scripts/cleancmd.pl` (PERL) -> Cumulative Risk: **805.51**
- **Archetype:** `file_cluster_17` (Distance: 13.732 IQR)
- **Magnitude:** 357.36 | **LOC:** 131 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `process` (Impact: 226.6)

### 5. `projects/OS400/os400sys.c` (C) -> Cumulative Risk: **805.38**
- **Archetype:** `file_cluster_13` (Distance: 13.074 IQR)
- **Magnitude:** 498.46 | **LOC:** 1021 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Curl_getnameinfo_a` (Impact: 101.2), `Curl_getaddrinfo_a` (Impact: 35.6), `get_buffer` (Impact: 17.4)

### 6. `scripts/mdlinkcheck` (PERL) -> Cumulative Risk: **801.08**
- **Archetype:** `file_cluster_0` (Distance: 16.542 IQR)
- **Magnitude:** 207.62 | **LOC:** 255 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9785%)
- **Heaviest Functions:** `checkurl` (Impact: 48.1), `findlinks` (Impact: 41.5), `storelink` (Impact: 6.4)

### 7. `scripts/nroff2cd` (PERL) -> Cumulative Risk: **798.9**
- **Archetype:** `file_cluster_0` (Distance: 15.537 IQR)
- **Magnitude:** 665.28 | **LOC:** 198 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `single` (Impact: 440.7)

### 8. `src/tool_dirhie.c` (C) -> Cumulative Risk: **787.09**
- **Archetype:** `file_cluster_13` (Distance: 11.918 IQR)
- **Magnitude:** 114.24 | **LOC:** 136 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Injection Surface (100.0%), State Flux (99.9937%)
- **Heaviest Functions:** `show_dir_errno` (Impact: 46.8), `create_dir_hierarchy` (Impact: 27.9)

### 9. `src/tool_operate.c` (C) -> Cumulative Risk: **785.9**
- **Archetype:** `file_cluster_13` (Distance: 14.066 IQR)
- **Magnitude:** 1843.52 | **LOC:** 2414 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 53.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `check_finished` (Impact: 724.7), `parallel_event` (Impact: 213.3), `add_parallel_transfers` (Impact: 91.6)

### 10. `scripts/cd2nroff` (PERL) -> Cumulative Risk: **779.21**
- **Archetype:** `file_cluster_0` (Distance: 13.401 IQR)
- **Magnitude:** 1614.72 | **LOC:** 583 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `single` (Impact: 1025.1), `outprotocols` (Impact: 120.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/runtests.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.09 IQR)
- **Top Global Matches:** file_cluster_8: 14.09, file_cluster_0: 14.099, file_cluster_13: 14.198
- **Magnitude:** 10218.62 | **LOC:** 3372 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 476
- **Risk Profile:** Cognitive Load (48.9244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `singletest_count` (Impact: 7446.7 | O(2^N) | DB: 476)
    * *Intent:* ####################################################################### # Print the test name and co...
  * `checksystemfeatures` (Impact: 414.7 | O(N^6) | DB: 139)
    * *Intent:* ####################################################################### # Check & display informatio...
  * `singletest_shouldrun` (Impact: 166.4 | O(N^6) | DB: 28)
    * *Intent:* ####################################################################### # Verify that this test case...
  * `cleardir` (Impact: 73.6 | O(2^N) | DB: 12)
    * *Intent:* ####################################################################### # Remove all files in the sp...
  * `compare` (Impact: 64.7 | O(N^3) | DB: 2)
    * *Intent:* ####################################################################### # compare test results with ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 983`, `structural_boundaries: 491`, `args: 31`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 18`, `state_mutation: 1799`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 48`, `concurrency: 1`, `import: 33`
* *Defense:* `safety: 4`, `sync_locks: 2`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` name, runner, Digest::MD5, POSIX, servers, anything, azure, getpart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/servers.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.132 IQR)
- **Top Global Matches:** file_cluster_8: 14.132, file_cluster_0: 14.138, file_cluster_13: 14.249
- **Magnitude:** 8934.66 | **LOC:** 3220 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 676
- **Risk Profile:** Cognitive Load (41.4128%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkcmd` (Impact: 6757.0 | O(2^N) | DB: 676)
    * *Intent:* ####################################################################### # Check for a command in the...
  * `localhttp` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 879`, `structural_boundaries: 710`, `args: 40`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 2113`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 32`, `api: 3`, `concurrency: 12`, `import: 21`
* *Defense:* `safety: 2`, `sync_locks: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.036
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.004598
  * `Imports (Out-Degree: 6):` by, POSIX, sshhelp, globalconfig, base, gnutls, need, serverhelp...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/managen` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.857 IQR)
- **Top Global Matches:** file_cluster_0: 13.857, file_cluster_8: 14.004, file_cluster_13: 14.129
- **Magnitude:** 8600.12 | **LOC:** 1384 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 344
- **Risk Profile:** Cognitive Load (96.7552%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 7237.9 | O(2^N) | DB: 344)
  * `printdesc` (Impact: 104.7 | O(N^5) | DB: 21)
  * `protocols` (Impact: 59.7 | O(N^3) | DB: 1)
  * `justline` (Impact: 29.9 | O(N^3) | DB: 18)
  * `outputpara` (Impact: 15.2 | O(N^3) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 258`, `args: 30`, `func_start: 27`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 1077`, `dead_code: 3`
* *Architecture:* `io: 20`, `import: 8`
* *Defense:* `safety: 2`, `doc: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` POSIX, strict, several, proper, spaces, in, extra, of...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ftpserver.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.529 IQR)
- **Top Global Matches:** file_cluster_8: 13.529, file_cluster_0: 13.679, file_cluster_13: 13.755
- **Magnitude:** 8581.1 | **LOC:** 3374 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 375
- **Risk Profile:** Cognitive Load (47.1818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `disc_handshake` (Impact: 6506.2 | O(2^N) | DB: 375)
    * *Intent:* # Perform the disconnect handshake with sockfilt on the secondary connection # (the only connection ...
  * `eXsysread` (Impact: 601.6 | O(2^N) | DB: 99)
    * *Intent:* #********************************************************************** # eXsysread is a wrapper aro...
  * `protocolsetup` (Impact: 18.0 | O(N^3) | DB: 1)
    * *Intent:* #********************************************************************** # protocolsetup initializes ...
  * `exit_signal_handler` (Impact: 4.8 | O(N^2) | DB: 3)
    * *Intent:* #********************************************************************** # exit_signal_handler will b...
  * `ftpmsg` (Impact: 2.6 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 738`, `structural_boundaries: 463`, `args: 65`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 1398`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `io: 41`, `import: 25`
* *Defense:* `safety: 4`, `sync_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Digest::MD5, directories, getpart, throttling, globalconfig, NODATACONN, this, RETRWEIRDO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/scorecard.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.544 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.37 IQR)
- **Top Global Matches:** file_cluster_8: 11.544, file_cluster_13: 11.778, file_cluster_0: 11.797
- **Magnitude:** 3729.04 | **LOC:** 1026 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (28.3105%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `do_requests` (Impact: 1512.0 | O(2^N) | DB: 90)
  * `fmt_speed_result` (Impact: 762.9 | O(2^N) | DB: 6)
  * `uploads` (Impact: 225.1 | O(2^N) | DB: 7)
  * `downloads` (Impact: 222.7 | O(2^N) | DB: 8)
  * `__init__` (Impact: 89.2 | O(N^4) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 126`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 219`, `orphaned_logic: 1`
* *Architecture:* `io: 30`, `api: 33`, `import: 10`
* *Defense:* `safety: 11`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, typing, datetime, argparse, logging, json, sys, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_getparam.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.144 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.249 IQR)
- **Top Global Matches:** file_cluster_8: 14.144, file_cluster_13: 14.282, file_cluster_0: 14.423
- **Magnitude:** 3360.38 | **LOC:** 3155 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 65.2%
- **Algorithmic:** O(N^6) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (75.2837%), Tech Debt (29.7083%)
**Top Internal Functions/Classes:**
  * `parse_cert_parameter` (Impact: 235.7 | O(N^6) | DB: 35)
  * `data_urlencode` (Impact: 179.9 | O(N^6) | DB: 30)
  * `set_trace_config` (Impact: 177.3 | O(N^5) | DB: 23)
  * `parse_time_cond` (Impact: 149.6 | O(N^6) | DB: 26)
  * `parse_header` (Impact: 128.3 | O(N^6) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 145`, `args: 30`, `func_start: 32`, `class_start: 13`
* *Risk/State:* `state_mutation: 994`, `orphaned_logic: 23`
* *Architecture:* `io: 13`, `api: 251`, `import: 15`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` tool_libinfo.h, tool_parsecfg.h, tool_paramhlp.h, tool_msgs.h, tool_formparse.h, var.h, tool_filetime.h, tool_stderr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/rtspd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.249 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.545 IQR)
- **Top Global Matches:** file_cluster_0: 14.249, file_cluster_11: 14.255, file_cluster_8: 14.322
- **Magnitude:** 3319.38 | **LOC:** 1362 | **CtrlFlow:** 83.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 131
- **Risk Profile:** Cognitive Load (40.0547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rtspd_ProcessRequest` (Impact: 1544.8 | O(2^N) | DB: 131)
    * *Intent:* #define REQUEST_KEYWORD_SIZE_TXT "255" #define CMD_AUTH_REQUIRED "auth_required" /* 'idle' means tha...
  * `test_rtspd` (Impact: 450.0 | O(N^4) | DB: 112)
  * `rtspd_send_doc` (Impact: 239.1 | O(N^5) | DB: 89)
  * `rtspd_get_request` (Impact: 80.5 | O(N^5) | DB: 50)
    * *Intent:* return 1; /* done */
  * `rtspd_storerequest` (Impact: 46.9 | O(N^2) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 63`, `args: 3`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `state_mutation: 778`, `dead_code: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 41`, `api: 159`, `import: 2`
* *Defense:* `safety: 25`, `doc: 1`, `immutability_locks: 17`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` first.h, tcp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/sws.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.202 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.523 IQR)
- **Top Global Matches:** file_cluster_11: 14.202, file_cluster_8: 14.209, file_cluster_0: 14.221
- **Magnitude:** 3218.5 | **LOC:** 2484 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 84.6%
- **Algorithmic:** O(N^6) | **DB Complexity:** 112
- **Risk Profile:** Cognitive Load (41.4702%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sws_ProcessRequest` (Impact: 957.3 | O(N^6) | DB: 112)
  * `connect_to` (Impact: 255.4 | O(N^6) | DB: 31)
  * `sws_send_doc` (Impact: 235.6 | O(N^5) | DB: 81)
  * `http_connect` (Impact: 227.7 | O(N^6) | DB: 48)
  * `sws_parse_servercmd` (Impact: 215.2 | O(N^5) | DB: 62)
    * *Intent:* *optr = 0; /* in case no sprintf was used */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 104`, `args: 8`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 856`, `dead_code: 6`, `orphaned_logic: 4`
* *Architecture:* `io: 41`, `api: 235`, `import: 2`
* *Defense:* `safety: 28`, `doc: 1`, `immutability_locks: 32`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` first.h, tcp.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/testenv/curl.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.96 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.579 IQR)
- **Top Global Matches:** file_cluster_0: 12.96, file_cluster_11: 13.051, file_cluster_16: 13.068
- **Magnitude:** 3181.74 | **LOC:** 1309 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (46.05%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 829.3 | O(2^N) | DB: 72)
  * `_complete_args` (Impact: 335.4 | O(N^5) | DB: 17)
  * `http_delete` (Impact: 220.2 | O(N^6) | DB: 17)
  * `_run` (Impact: 207.5 | O(N^6) | DB: 12)
  * `__init__` (Impact: 142.4 | O(N^4) | DB: 51)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 236`, `args: 88`, `func_start: 88`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 4`, `state_mutation: 374`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 57`, `api: 86`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 51`, `doc: 2`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .env, os, typing, datetime, threading, shutil, logging, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_doswin.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.023 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.122 IQR)
- **Top Global Matches:** file_cluster_13: 14.023, file_cluster_11: 14.123, file_cluster_0: 14.163
- **Magnitude:** 2912.7 | **LOC:** 919 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 115
- **Risk Profile:** Cognitive Load (85.2361%), Tech Debt (10.2118%)
**Top Internal Functions/Classes:**
  * `msdosify` (Impact: 2420.2 | O(2^N) | DB: 115)
    * *Intent:* #endif /* * Test if truncating a path to a file leaves at least a single character * in the filename...
  * `truncate_dryrun` (Impact: 74.3 | O(N^6) | DB: 4)
    * *Intent:* #ifdef _WIN32 # include <tlhelp32.h> #elif !defined(__DJGPP__) || (__DJGPP__ < 2) /* DJGPP 2.0 has _...
  * `__crt0_glob_function` (Impact: 2.0 | O(N^1))
    * *Intent:* * ***************************************************************************/ #include "tool_setup....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 52`, `args: 9`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `state_mutation: 327`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 80`, `import: 8`
* *Defense:* `safety: 10`, `doc: 1`, `test: 3`, `immutability_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` basename.h, tool_doswin.h, tool_msgs.h, version_win32.h, fcntl.h, tlhelp32.h, tool_cfgable.h, tool_setup.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_formparse.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.347 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.279 IQR)
- **Top Global Matches:** file_cluster_8: 14.347, file_cluster_13: 14.457, file_cluster_11: 14.512
- **Magnitude:** 2882.4 | **LOC:** 898 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (85.2745%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_param_part` (Impact: 712.2 | O(N^6) | DB: 83)
  * `formparse` (Impact: 525.5 | O(N^6) | DB: 58)
    * *Intent:* * * If literal_value is set, any initial '@' or '<' in the value string * loses its special meaning,...
  * `tool2curlparts` (Impact: 213.3 | O(2^N) | DB: 20)
  * `tool_mime_new_filedata` (Impact: 207.4 | O(N^6) | DB: 25)
    * *Intent:* /*
  * `get_param_word` (Impact: 94.8 | O(N^3) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 65`, `args: 11`, `func_start: 15`, `class_start: 16`
* *Risk/State:* `state_mutation: 769`
* *Architecture:* `io: 8`, `api: 144`, `import: 6`
* *Defense:* `safety: 9`, `doc: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` tool_parsecfg.h, tool_paramhlp.h, tool_msgs.h, tool_formparse.h, tool_cfgable.h, tool_setup.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/runner.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.38 IQR)
- **Top Global Matches:** file_cluster_0: 13.38, file_cluster_13: 13.537, file_cluster_8: 13.574
- **Magnitude:** 2676.26 | **LOC:** 1527 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 251
- **Risk Profile:** Cognitive Load (48.561%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `runner_init` (Impact: 1629.7 | O(N^6) | DB: 251)
    * *Intent:* ####################################################################### # Initialize the runner and ...
  * `ipcrecv` (Impact: 71.2 | O(N^3) | DB: 20)
    * *Intent:* ################################################################### # Receive an IPC call in the run...
  * `runnerar` (Impact: 59.6 | O(N^3) | DB: 11)
    * *Intent:* ################################################################### # Receive async response of a pr...
  * `singletest_postcheck` (Impact: 49.2 | O(N^4) | DB: 4)
    * *Intent:* ####################################################################### # Verify that the postcheck ...
  * `runner_test_preprocess` (Impact: 33.9 | O(N^3) | DB: 2)
    * *Intent:* ################################################################### # Get ready to run a single test...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 265`, `args: 21`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 730`, `dead_code: 5`, `planned_debt: 4`
* *Architecture:* `io: 27`, `api: 3`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 3`, `sync_locks: 2`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.783
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002299
  * `Imports (Out-Degree: 6):` name, servers, getpart, windowed, newlines, globalconfig, memanalyzer, valgrind...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/tool_writeout.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.613 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.105 IQR)
- **Top Global Matches:** file_cluster_8: 13.613, file_cluster_13: 13.689, file_cluster_0: 13.707
- **Magnitude:** 2529.64 | **LOC:** 874 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (80.1402%), Tech Debt (9.0549%)
**Top Internal Functions/Classes:**
  * `writeString` (Impact: 445.5 | O(2^N) | DB: 31)
  * `ourWriteOut` (Impact: 441.9 | O(N^6) | DB: 39)
  * `urlpart` (Impact: 326.0 | O(N^6) | DB: 21)
  * `output_header` (Impact: 157.4 | O(N^6) | DB: 20)
  * `writeLong` (Impact: 146.8 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 83`, `args: 7`, `func_start: 11`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 468`, `dead_code: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 156`, `import: 4`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tool_writeout_json.h, tool_setup.h, tool_cfgable.h, tool_writeout.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/sockfilt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.572 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.161 IQR)
- **Top Global Matches:** file_cluster_8: 13.572, file_cluster_11: 13.732, file_cluster_0: 13.734
- **Magnitude:** 2455.14 | **LOC:** 1412 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 91.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 89
- **Risk Profile:** Cognitive Load (39.7809%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `select_ws` (Impact: 880.4 | O(2^N) | DB: 73)
    * *Intent:* #define SOCKFILT_read read_wincon #define SOCKFILT_write write_wincon #else #define SOCKFILT_read re...
  * `select_ws_wait_thread` (Impact: 326.8 | O(2^N) | DB: 15)
    * *Intent:* /*************************************************************************** * _ _ ____ _ * Project ...
  * `test_sockfilt` (Impact: 297.5 | O(N^4) | DB: 89)
  * `juggle` (Impact: 161.6 | O(N^4) | DB: 56)
    * *Intent:* /* retrieve an event from the console buffer */
  * `disc_handshake` (Impact: 36.0 | O(N^2))
    * *Intent:* /* The handle represents a file on disk, this means: * - WaitForMultipleObjectsEx will always be sig...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 62`, `args: 6`, `func_start: 6`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 598`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `api: 133`, `import: 1`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` first.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/config2setopts.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.121 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.806 IQR)
- **Top Global Matches:** file_cluster_8: 13.121, file_cluster_13: 13.216, file_cluster_7: 13.483
- **Magnitude:** 2301.0 | **LOC:** 1067 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (78.4373%), Tech Debt (8.4528%)
**Top Internal Functions/Classes:**
  * `config2setopts` (Impact: 441.7 | O(N^6) | DB: 13)
  * `ssl_setopts` (Impact: 304.8 | O(N^6) | DB: 9)
  * `url_proto_and_rewrite` (Impact: 142.5 | O(N^6) | DB: 16)
  * `tlsversion` (Impact: 142.5 | O(N^5) | DB: 10)
  * `http_setopts` (Impact: 136.1 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 75`, `args: 19`, `func_start: 19`, `class_start: 10`
* *Risk/State:* `state_mutation: 317`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 113`, `import: 18`
* *Defense:* `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` tool_libinfo.h, tool_cb_dbg.h, tool_cb_wrt.h, tool_findfile.h, tool_setopt.h, tool_formparse.h, tool_msgs.h, config2setopts.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `projects/OS400/ccsidcurl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.761 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.111 IQR)
- **Top Global Matches:** file_cluster_13: 13.761, file_cluster_8: 13.854, file_cluster_11: 14.006
- **Magnitude:** 2104.38 | **LOC:** 1473 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (93.4599%), Tech Debt (53.462%)
**Top Internal Functions/Classes:**
  * `curl_formadd_ccsid` (Impact: 502.8 | O(N^6) | DB: 63)
  * `convert` (Impact: 273.3 | O(N^6) | DB: 23)
    * *Intent:* #include "curl.h" #include "mprintf.h" #include "slist.h" #include "urldata.h" #include "url.h" #inc...
  * `curl_easy_setopt_ccsid` (Impact: 209.5 | O(N^2) | DB: 40)
  * `Curl_formadd_convert` (Impact: 72.4 | O(N^6) | DB: 8)
  * `Curl_formget_callback_ccsid` (Impact: 36.5 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 87`, `args: 14`, `func_start: 25`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 513`, `orphaned_logic: 19`
* *Architecture:* `api: 260`, `import: 15`
* *Defense:* `safety: 13`, `doc: 3`, `immutability_locks: 20`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` slist.h, url.h, stdlib.h, setopt.h, mprintf.h, stddef.h, getinfo.h, os400sys.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/smbserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.015 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.03 IQR)
- **Top Global Matches:** file_cluster_8: 10.015, file_cluster_13: 10.156, file_cluster_4: 10.457
- **Magnitude:** 1869.12 | **LOC:** 446 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.8071%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 61`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 16`
* *Architecture:* `io: 21`, `api: 14`, `concurrency: 13`, `import: 13`
* *Defense:* `safety: 9`, `doc: 14`, `test: 1`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, tempfile, argparse, signal, threading, logging, sys, util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_operate.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.066 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.116 IQR)
- **Top Global Matches:** file_cluster_13: 14.066, file_cluster_8: 14.319, file_cluster_11: 14.49
- **Magnitude:** 1843.52 | **LOC:** 2414 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 53.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (92.9908%), Tech Debt (10.8728%)
**Top Internal Functions/Classes:**
  * `check_finished` (Impact: 724.7 | O(N^6) | DB: 76)
  * `parallel_event` (Impact: 213.3 | O(2^N) | DB: 14)
  * `add_parallel_transfers` (Impact: 91.6 | O(N^6) | DB: 22)
    * *Intent:* /* * Check if a given string is a PKCS#11 URI
  * `single_transfer` (Impact: 88.0 | O(N^6) | DB: 12)
    * *Intent:* #include "tool_libinfo.h" #include "tool_main.h" #include "tool_msgs.h" #include "tool_operate.h" #i...
  * `cb_socket` (Impact: 86.0 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 103`, `args: 7`, `func_start: 18`, `class_start: 21`
* *Risk/State:* `state_mutation: 423`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 131`, `import: 39`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` tool_progress.h, tool_paramhlp.h, tool_msgs.h, tool_filetime.h, tool_help.h, tool_cfgable.h, unistd.h, tool_easysrc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/testenv/env.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.331 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.976 IQR)
- **Top Global Matches:** file_cluster_0: 12.331, file_cluster_11: 12.591, file_cluster_16: 12.717
- **Magnitude:** 1721.34 | **LOC:** 856 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 96
- **Risk Profile:** Cognitive Load (49.9013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 472.5 | O(N^6) | DB: 96)
  * `version` (Impact: 109.9 | O(2^N) | DB: 2)
  * `issue_certs` (Impact: 49.1 | O(2^N) | DB: 10)
  * `make_data_file` (Impact: 37.5 | O(N^5) | DB: 6)
  * `httpd_version` (Impact: 37.0 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 266`, `args: 109`, `func_start: 109`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 6`, `state_mutation: 232`, `fragile_debt: 2`, `duplicate_logic: 16`
* *Architecture:* `io: 42`, `api: 152`, `import: 13`
* *Defense:* `safety: 5`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.234
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.02069
  * `Imports (Out-Degree: 1):` gzip, os, typing, tempfile, datetime, shutil, logging, subprocess...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scripts/cd2nroff` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.401 IQR)
- **Top Global Matches:** file_cluster_0: 13.401, file_cluster_8: 13.754, file_cluster_13: 13.802
- **Magnitude:** 1614.72 | **LOC:** 583 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 80
- **Risk Profile:** Cognitive Load (89.2248%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `single` (Impact: 1025.1 | O(N^6) | DB: 80)
  * `outprotocols` (Impact: 120.0 | O(N^4) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 74`, `args: 9`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 12`, `state_mutation: 460`, `dead_code: 2`
* *Architecture:* `io: 7`, `import: 4`
* *Defense:* `safety: 2`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` POSIX, strict, italics, warnings, TLS, header
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/memanalyzer.pm` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.203 IQR)
- **Top Global Matches:** file_cluster_8: 13.203, file_cluster_0: 13.392, file_cluster_13: 13.418
- **Magnitude:** 1519.48 | **LOC:** 447 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 148
- **Risk Profile:** Cognitive Load (42.8856%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `memanalyze` (Impact: 1115.2 | O(N^6) | DB: 148)
  * `newtotal` (Impact: 5.6 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 49`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 390`
* *Architecture:* `io: 6`, `api: 2`, `import: 3`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006897
  * `Imports (Out-Degree: 0):` base, warnings, strict
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/tool_cb_hdr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.292 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.875 IQR)
- **Top Global Matches:** file_cluster_13: 14.292, file_cluster_11: 14.404, file_cluster_0: 14.476
- **Magnitude:** 1379.94 | **LOC:** 549 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 53.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (86.7842%), Tech Debt (10.7422%)
**Top Internal Functions/Classes:**
  * `content_disposition` (Impact: 418.0 | O(N^6) | DB: 28)
  * `tool_header_cb` (Impact: 334.3 | O(N^6) | DB: 37)
  * `write_linked_location` (Impact: 112.5 | O(N^6) | DB: 20)
    * *Intent:* * * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY * KIND, either express...
  * `save_etag` (Impact: 71.5 | O(N^6) | DB: 9)
  * `parse_filename` (Impact: 44.0 | O(N^1) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 45`, `args: 5`, `func_start: 6`, `class_start: 10`
* *Risk/State:* `state_mutation: 285`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 8`, `api: 99`, `import: 9`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` tool_libinfo.h, tool_doswin.h, tool_cb_wrt.h, tool_msgs.h, tool_operate.h, tool_cfgable.h, unistd.h, tool_cb_hdr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/dnsd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.99 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.248 IQR)
- **Top Global Matches:** file_cluster_8: 13.99, file_cluster_0: 14.221, file_cluster_13: 14.225
- **Magnitude:** 1367.56 | **LOC:** 679 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 98
- **Risk Profile:** Cognitive Load (38.4952%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dnsd` (Impact: 493.5 | O(N^6) | DB: 98)
  * `store_incoming` (Impact: 103.0 | O(N^6) | DB: 20)
    * *Intent:* *size -= (p - *pkt); *pkt = p;
  * `read_instructions` (Impact: 84.3 | O(N^4) | DB: 21)
    * *Intent:* */ 0x0, 0x1, /* QDCOUNT a single question */
  * `send_response` (Impact: 82.3 | O(N^6) | DB: 14)
    * *Intent:* bytes[i++] = 0x0c; /* points to the query at this fixed packet index */
  * `qname` (Impact: 13.2 | O(N^1) | DB: 15)
    * *Intent:* * Project ___| | | | _ \| | * / __| | | | |_) | | * | (__| |_| | _ <| |___ * \___|\___/|_| \_\_____|...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 29`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 469`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `api: 90`, `import: 1`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` first.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ech_tests.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.803 IQR)
- **Top Global Matches:** file_cluster_8: 12.803, file_cluster_11: 12.921, file_cluster_0: 12.978
- **Magnitude:** 1365.14 | **LOC:** 1103 | **CtrlFlow:** 93.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 405
- **Risk Profile:** Cognitive Load (44.3592%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 1015.6 | O(N^2) | DB: 405)
  * `__global_context__` (Impact: 38.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 476`, `structural_boundaries: 31`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 164`, `state_mutation: 290`, `dead_code: 5`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 128`, `api: 2`, `import: 2`
* *Defense:* `safety: 26`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/util.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.907 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.865 IQR)
- **Top Global Matches:** file_cluster_8: 12.907, file_cluster_13: 13.181, file_cluster_0: 13.263
- **Magnitude:** 1363.96 | **LOC:** 899 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (35.6477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sockdaemon` (Impact: 263.0 | O(N^6) | DB: 38)
  * `install_signal_handlers` (Impact: 94.3 | O(N^6) | DB: 8)
  * `exit_signal_handler` (Impact: 88.6 | O(2^N) | DB: 27)
    * *Intent:* #if defined(_MSC_VER) && (_MSC_VER <= 1700) /* Workaround for warning C4306: 'type cast' : conversio...
  * `main_window_loop` (Impact: 75.4 | O(N^6) | DB: 9)
    * *Intent:* * * Background information from MSDN: * SIGINT is not supported for any Win32 application. When a CT...
  * `bind_unix_socket` (Impact: 65.9 | O(N^5) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 86`, `args: 22`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `state_mutation: 348`
* *Architecture:* `io: 20`, `api: 126`, `import: 4`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` first.h, share.h, tool_time.h, fcntl.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/testutil.pm` (PERL) | Magnitude: 410.92 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 257, indent_spaces: 129, regex_execution: 68, structural_boundaries: 57
- `tests/server/rtspd.c` (C) | Magnitude: 3319.38 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 980, state_mutation: 778, branch: 321, pointers: 267
- `tests/http/testenv/certs.py` (PYTHON) | Magnitude: 880.3 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 464, structural_boundaries: 136, branch: 99, encapsulation: 89
- `scripts/delta` (PERL) | Magnitude: 196.9 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 180, branch: 53, indent_spaces: 49, structural_boundaries: 43
- `tests/unit/unit1307.c` (C) | Magnitude: 695.32 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 219, branch: 94, sec_reflection_metaprogramming: 48, state_mutation: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/server/sws.c` (C) | Magnitude: 3218.5 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1134, state_mutation: 856, branch: 412, pointers: 363
- `tests/server/tftpd.c` (C) | Magnitude: 1135.06 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 379, state_mutation: 371, branch: 129, pointers: 60
- `tests/server/mqttd.c` (C) | Magnitude: 1208.8 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 621, state_mutation: 501, branch: 153, api: 149
- `tests/server/getpart.c` (C) | Magnitude: 382.96 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 128, indent_spaces: 118, pointers: 60, branch: 45
- `.github/scripts/cmp-pkg-config.sh` (SHELL) | Magnitude: 9.19 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 39, indent_spaces: 25, branch: 22, safety: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/unit/unit1653.c` (C) | Magnitude: 546.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 153, state_mutation: 129, branch: 53, api: 32
- `projects/OS400/initscript.sh` (SHELL) | Magnitude: 351.66 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 116, reflection_metaprogramming: 107, state_mutation: 73, branch: 52
- `appveyor.sh` (SHELL) | Magnitude: 110.14 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 65, branch: 60, reflection_metaprogramming: 39, io: 38
- `projects/OS400/make-include.sh` (SHELL) | Magnitude: 76.44 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: reflection_metaprogramming: 39, state_mutation: 26, safety: 21, branch: 20
- `projects/OS400/make-tests.sh` (SHELL) | Magnitude: 206.08 | Delta: **0.24 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 58, reflection_metaprogramming: 53, state_mutation: 48, branch: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scripts/top-complexity` (PERL) | Magnitude: 390.58 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 51, branch: 35, structural_boundaries: 27
- `tests/unit/unit3212.c` (C) | Magnitude: 104.74 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 73, pointers: 67, state_mutation: 49, branch: 7
- `src/tool_xattr.c` (C) | Magnitude: 149.78 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 58, api: 24, branch: 19
- `tests/unit/unit2601.c` (C) | Magnitude: 288.56 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 172, state_mutation: 112, pointers: 73, branch: 42
- `src/tool_parsecfg.h` (C) | Magnitude: 17.16 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 4, structural_boundaries: 3, api: 3, macros: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/mk-unity.pl` (PERL) | Magnitude: 235.0 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 75, indent_spaces: 57, branch: 23, structural_boundaries: 19
- `scripts/singleuse.pl` (PERL) | Magnitude: 100.04 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 175, state_mutation: 78, branch: 29, structural_boundaries: 18
- `tests/getpart.pm` (PERL) | Magnitude: 821.28 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 266, state_mutation: 234, branch: 99, structural_boundaries: 89
- `.github/scripts/cleancmd.pl` (PERL) | Magnitude: 357.36 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 129, indent_spaces: 62, branch: 37, structural_boundaries: 16
- `src/Makefile.am` (MAKEFILE) | Magnitude: 577.68 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 45, branch: 44, structural_boundaries: 43, indent_tabs: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/wcurl` (SHELL) | Magnitude: 325.4 | Delta: **0.354 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 145, state_mutation: 95, io: 56, branch: 50
- `scripts/perlcheck.sh` (SHELL) | Magnitude: 2.18 | Delta: **0.641 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: io: 8, indent_spaces: 8, branch: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/tool_cb_hdr.h` (C) | Magnitude: 24.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 12, structural_boundaries: 9, api: 9, class_start: 6
- `tests/http/test_17_ssl_use.py` (PYTHON) | Magnitude: 1134.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 484, test: 148, structural_boundaries: 108, branch: 104
- `src/tool_hugehelp.h` (C) | Magnitude: 16.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, macros: 3, pointers: 3, immutability_locks: 3
- `tests/test1544.pl` (PERL) | Magnitude: 231.16 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 111, indent_spaces: 68, branch: 36, structural_boundaries: 21
- `scripts/firefox-db2pem.sh` (SHELL) | Magnitude: 2.99 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 15, io: 14, structural_boundaries: 9, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scripts/dmaketgz` (SHELL) | Magnitude: 17.88 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 6, branch: 5, reflection_metaprogramming: 5
- `scripts/release-tools.sh` (SHELL) | Magnitude: 3.0 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 15, state_mutation: 15, branch: 6, args: 6
- `.github/scripts/shellcheck-ci.sh` (SHELL) | Magnitude: 1.09 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 19, io: 14, indent_spaces: 12, debug_prints: 8
- `src/tool_sdecls.h` (C) | Magnitude: 25.78 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, api: 9, structural_boundaries: 8, class_start: 5
- `tests/tunit/Makefile.inc` (MAKEFILE) | Magnitude: 14.16 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, sec_dead_code: 2, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/tool_operate.c` -> Churn: **82.57%** | Cog Load: 92.9908% | Debt: 10.8728%
- `src/tool_getparam.c` -> Churn: **76.42%** | Cog Load: 75.2837% | Debt: 29.7083%
- `src/tool_doswin.c` -> Churn: **66.91%** | Cog Load: 85.2361% | Debt: 10.2118%
- `src/tool_cb_hdr.c` -> Churn: **66.67%** | Cog Load: 86.7842% | Debt: 10.7422%
- `src/config2setopts.c` -> Churn: **65.11%** | Cog Load: 78.4373% | Debt: 8.4528%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/servers.pm` -> **Viktor Szakats** (83.3% isolated ownership) | Magnitude: 8934.66
- `scripts/managen` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 8600.12
- `tests/http/scorecard.py` -> **Stefan Eissing** (100.0% isolated ownership) | Magnitude: 3729.04
- `tests/server/rtspd.c` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 3319.38
- `tests/server/sws.c` -> **Viktor Szakats** (84.6% isolated ownership) | Magnitude: 3218.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/curl/curl.h` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 82.6545%)
- `src/tool_cfgable.h` -> **Severity: 0.01** (Bridge: 0.0007 * Flux: 13.0216%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/testutil.pm` -> **Severity: 1.541** (Embedded: 0.0155 * Error Risk: 99.7025%)
- `tests/globalconfig.pm` -> **Severity: 1.491** (Embedded: 0.0195 * Error Risk: 76.5777%)
- `tests/pathhelp.pm` -> **Severity: 1.448** (Embedded: 0.0237 * Error Risk: 61.0639%)
- `tests/serverhelp.pm` -> **Severity: 1.447** (Embedded: 0.0209 * Error Risk: 69.2408%)
- `tests/http/testenv/ports.py` -> **Severity: 1.257** (Embedded: 0.0163 * Error Risk: 76.875%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/tool_setup.h` -> **Severity: 3248.659** (Blast Radius: 111.439 * Doc Risk: 29.1519%)
- `src/tool_cfgable.h` -> **Severity: 1499.0** (Blast Radius: 14.99 * Doc Risk: 100.0%)
- `include/curl/curl.h` -> **Severity: 951.7** (Blast Radius: 9.517 * Doc Risk: 100.0%)
- `src/tool_getparam.h` -> **Severity: 662.019** (Blast Radius: 9.869 * Doc Risk: 67.0807%)
- `src/tool_operate.h` -> **Severity: 543.3** (Blast Radius: 5.433 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
