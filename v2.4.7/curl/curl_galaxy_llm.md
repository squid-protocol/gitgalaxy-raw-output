# ARCHITECTURAL_BRIEF: curl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/curl` |
| **Timestamp** | `2026-08-07T04:30:41.677263+00:00` |
| **Scan Duration** | `3.33s` |
| **Git Branch** | `master` |
| **Git Commit** | `8f3f470baec57f5e53e11fc2ecaa749201ca9c0c` |
| **Git Remote** | `https://github.com/curl/curl` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 308 malicious artifacts.

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
| Modularity | 0.4851 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `4.376`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 194 | 45.1% |
| file_cluster_13 | 123 | 28.6% |
| file_cluster_0 | 34 | 7.9% |
| file_cluster_17 | 11 | 2.6% |
| file_cluster_9 | 9 | 2.1% |
| file_cluster_12 | 7 | 1.6% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 32.3 | 26.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 57.3 | 76.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.5 | 5.6 | 5.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.1 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.1 | 0.3 | 0.1 | 0.0 |
| Volatility Exposure | 0.0 | 85.5 | 17.6 | 12.9 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.3 | 8.7 | 0.0 |
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

- `Anonymous_Block_[Truncated]` (@ `tests/ech_tests.sh`) -> Impact: **1481.6** | LOC: 924
- `render` (@ `scripts/managen`) -> Impact: **1079.8** | LOC: 1069
- `checkcmd` (@ `tests/servers.pm`) -> Impact: **1037.7** | LOC: 2014
  * *Intent:* ####################################################################### # Check for a command in the PATH of the test server. #
- `singletest_count` (@ `tests/runtests.pl`) -> Impact: **1031.2** | LOC: 1987
  * *Intent:* ####################################################################### # Print the test name and count tests
- `disc_handshake` (@ `tests/ftpserver.pl`) -> Impact: **1022.5** | LOC: 2333
  * *Intent:* # Perform the disconnect handshake with sockfilt on the secondary connection # (the only connection we actively disconnect). # This involves waiting f...
- `singletest_check` (@ `tests/runtests.pl`) -> Impact: **942.0** | LOC: 1273
  * *Intent:* ####################################################################### # Verify test succeeded
- `runner_init` (@ `tests/runner.pm`) -> Impact: **464.9** | LOC: 950
  * *Intent:* ####################################################################### # Initialize the runner and prepare it to run tests # The runner ID returned b...
- `customize` (@ `tests/ftpserver.pl`) -> Impact: **392.4** | LOC: 567
  * *Intent:* #********************************************************************** # customize configures test server operation for each curl test, reading # con...
- `msdosify` (@ `src/tool_doswin.c`) -> Impact: **368.1** | LOC: 523
  * *Intent:* #endif /* * Test if truncating a path to a file leaves at least a single character * in the filename. Filenames suffixed by an alternate data stream c...
- `memanalyze` (@ `tests/memanalyzer.pm`) -> Impact: **332.5** | LOC: 390

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests` | 52 | 24791.46 | 36.16% | 0.0% |
| `src` | 91 | 19323.06 | 37.33% | 17.41% |
| `tests/server` | 14 | 8834.76 | 32.36% | 0.0% |
| `scripts` | 37 | 7954.41 | 70.89% | 41.41% |
| `tests/unit` | 71 | 6189.2 | 19.91% | 0.0% |
| `tests/http/testenv` | 13 | 3974.48 | 28.12% | 0.0% |
| `tests/http` | 31 | 3869.14 | 5.99% | 0.0% |
| `projects/OS400` | 12 | 2592.56 | 53.08% | 48.42% |
| `m4` | 20 | 876.29 | 4.3% | 6.01% |
| `include/curl` | 12 | 771.34 | 10.9% | 2.67% |

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
29. **`projects/OS400/make-src.sh`** -> AI Confidence: **99.29%**
30. **`scripts/pythonlint.sh`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `scripts/mk-ca-bundle.pl` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1464` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/tool_operhlp.c` (C) -> Cumulative Risk: **705.49**
- **Archetype:** `file_cluster_13` (Distance: 13.624 IQR)
- **Magnitude:** 306.28 | **LOC:** 246 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.1322%)
- **Heaviest Functions:** `get_url_file_name` (Impact: 35.1), `add_file_name_to_url` (Impact: 34.5), `urlerr_cvt` (Impact: 8.6)

### 2. `projects/OS400/os400sys.c` (C) -> Cumulative Risk: **693.36**
- **Archetype:** `file_cluster_13` (Distance: 13.074 IQR)
- **Magnitude:** 385.06 | **LOC:** 1021 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.0321%)
- **Heaviest Functions:** `Curl_getnameinfo_a` (Impact: 30.5), `get_buffer` (Impact: 17.4), `Curl_getaddrinfo_a` (Impact: 13.2)

### 3. `src/tool_getpass.c` (C) -> Cumulative Risk: **677.36**
- **Archetype:** `file_cluster_13` (Distance: 14.258 IQR)
- **Magnitude:** 140.4 | **LOC:** 197 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.8505%)
- **Heaviest Functions:** `getpass_r` (Impact: 19.1), `getpass_r` (Impact: 13.5), `getpass_r` (Impact: 9.4)

### 4. `src/tool_paramhlp.c` (C) -> Cumulative Risk: **675.18**
- **Archetype:** `file_cluster_13` (Distance: 14.211 IQR)
- **Magnitude:** 868.88 | **LOC:** 733 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (93.5731%)
- **Heaviest Functions:** `proto2num` (Impact: 93.8), `file2memory_range` (Impact: 50.1), `checkpasswd` (Impact: 29.4)

### 5. `src/tool_getparam.c` (C) -> Cumulative Risk: **668.6**
- **Archetype:** `file_cluster_8` (Distance: 14.144 IQR)
- **Magnitude:** 2019.18 | **LOC:** 3155 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 65.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.0487%)
- **Heaviest Functions:** `parse_cert_parameter` (Impact: 70.7), `set_trace_config` (Impact: 61.3), `data_urlencode` (Impact: 54.9)

### 6. `src/tool_doswin.c` (C) -> Cumulative Risk: **665.51**
- **Archetype:** `file_cluster_13` (Distance: 14.022 IQR)
- **Magnitude:** 1050.9 | **LOC:** 919 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.566%)
- **Heaviest Functions:** `msdosify` (Impact: 368.1), `rename_if_reserved_dos` (Impact: 81.3), `sanitize_file_name` (Impact: 72.8)

### 7. `src/tool_setopt.c` (C) -> Cumulative Risk: **660.68**
- **Archetype:** `file_cluster_8` (Distance: 13.615 IQR)
- **Magnitude:** 758.06 | **LOC:** 726 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.5197%)
- **Heaviest Functions:** `libcurl_generate_mime_part` (Impact: 49.6), `c_escape` (Impact: 33.8), `tool_setopt_bitmask` (Impact: 20.2)

### 8. `src/tool_cb_hdr.c` (C) -> Cumulative Risk: **659.83**
- **Archetype:** `file_cluster_13` (Distance: 14.292 IQR)
- **Magnitude:** 723.74 | **LOC:** 549 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 53.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (93.6057%)
- **Heaviest Functions:** `content_disposition` (Impact: 124.1), `tool_header_cb` (Impact: 99.5), `parse_filename` (Impact: 44.0)

### 9. `src/tool_easysrc.c` (C) -> Cumulative Risk: **659.21**
- **Archetype:** `file_cluster_13` (Distance: 13.117 IQR)
- **Magnitude:** 247.64 | **LOC:** 235 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.7153%)
- **Heaviest Functions:** `dumpeasysrc` (Impact: 28.6), `easysrc_perform` (Impact: 20.1), `easysrc_addf` (Impact: 6.8)

### 10. `src/var.c` (C) -> Cumulative Risk: **646.76**
- **Archetype:** `file_cluster_13` (Distance: 14.19 IQR)
- **Magnitude:** 761.36 | **LOC:** 494 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.8266%)
- **Heaviest Functions:** `varfunc` (Impact: 126.4), `setvariable` (Impact: 90.0), `varexpand` (Impact: 80.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/runtests.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.057 IQR)
- **Top Global Matches:** file_cluster_8: 14.057, file_cluster_0: 14.067, file_cluster_13: 14.166
- **Magnitude:** 4273.82 | **LOC:** 3372 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (48.3112%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `singletest_count` (Impact: 1031.2)
    * *Intent:* ####################################################################### # Print the test name and co...
  * `singletest_check` (Impact: 942.0)
    * *Intent:* ####################################################################### # Verify test succeeded
  * `checksystemfeatures` (Impact: 130.2)
    * *Intent:* ####################################################################### # Check & display informatio...
  * `singletest` (Impact: 66.9)
    * *Intent:* ####################################################################### # Run a single specified tes...
  * `singletest_shouldrun` (Impact: 51.5)
    * *Intent:* ####################################################################### # Verify that this test case...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 881`, `structural_boundaries: 530`, `args: 31`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 18`, `state_mutation: 1795`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 48`, `concurrency: 1`, `import: 33`
* *Defense:* `safety: 4`, `sync_locks: 2`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` strict, to, server, memanalyzer, a, additional, valgrind, it...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ftpserver.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.505 IQR)
- **Top Global Matches:** file_cluster_8: 13.505, file_cluster_0: 13.651, file_cluster_13: 13.728
- **Magnitude:** 3644.5 | **LOC:** 3374 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (47.3113%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `disc_handshake` (Impact: 1022.5)
    * *Intent:* # Perform the disconnect handshake with sockfilt on the secondary connection # (the only connection ...
  * `customize` (Impact: 392.4)
    * *Intent:* #********************************************************************** # customize configures test ...
  * `eXsysread` (Impact: 120.8)
    * *Intent:* #********************************************************************** # eXsysread is a wrapper aro...
  * `RETR_ftp` (Impact: 77.2)
  * `PASV_ftp` (Impact: 70.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 710`, `structural_boundaries: 544`, `args: 65`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 1388`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `io: 41`, `import: 25`
* *Defense:* `safety: 4`, `sync_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` strict, such, free, use, this, in, warnings, globalconfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/servers.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.098 IQR)
- **Top Global Matches:** file_cluster_8: 14.098, file_cluster_0: 14.104, file_cluster_13: 14.215
- **Magnitude:** 3191.36 | **LOC:** 3220 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (40.8603%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkcmd` (Impact: 1037.7)
    * *Intent:* ####################################################################### # Check for a command in the...
  * `localhttp` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 863`, `structural_boundaries: 757`, `args: 40`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 2089`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 32`, `api: 3`, `concurrency: 12`, `import: 21`
* *Defense:* `safety: 2`, `sync_locks: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.036
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.004598
  * `Imports (Out-Degree: 6):` strict, server, a, need, sshhelp, warnings, globalconfig, POSIX...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/managen` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.843 IQR)
- **Top Global Matches:** file_cluster_0: 13.843, file_cluster_8: 13.992, file_cluster_13: 14.115
- **Magnitude:** 2524.62 | **LOC:** 1384 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.1793%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 1079.8)
  * `getshortlong` (Impact: 218.2)
  * `printdesc` (Impact: 36.7)
  * `protocols` (Impact: 30.3)
  * `justline` (Impact: 16.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 515`, `structural_boundaries: 285`, `args: 30`, `func_start: 27`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 1077`, `dead_code: 3`
* *Architecture:* `io: 20`, `import: 8`
* *Defense:* `safety: 2`, `doc: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` extra, warnings, strict, POSIX, spaces, several, of, proper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_getparam.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.144 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.249 IQR)
- **Top Global Matches:** file_cluster_8: 14.144, file_cluster_13: 14.282, file_cluster_0: 14.423
- **Magnitude:** 2019.18 | **LOC:** 3155 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 65.2%
- **Risk Profile:** Cognitive Load (75.2837%), Tech Debt (29.7083%)
**Top Internal Functions/Classes:**
  * `parse_cert_parameter` (Impact: 70.7)
  * `set_trace_config` (Impact: 61.3)
  * `data_urlencode` (Impact: 54.9)
  * `set_rate` (Impact: 46.9)
  * `parse_time_cond` (Impact: 45.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 145`, `args: 30`, `func_start: 32`, `class_start: 13`
* *Risk/State:* `state_mutation: 994`, `orphaned_logic: 23`
* *Architecture:* `io: 13`, `api: 251`, `import: 15`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` tool_setup.h, tool_filetime.h, tool_cfgable.h, tool_getparam.h, tool_main.h, var.h, tool_parsecfg.h, tool_cb_prg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/smbserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.015 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.03 IQR)
- **Top Global Matches:** file_cluster_8: 10.015, file_cluster_13: 10.156, file_cluster_4: 10.457
- **Magnitude:** 1869.12 | **LOC:** 446 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8071%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 61`, `args: 15`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 16`
* *Architecture:* `io: 21`, `api: 14`, `concurrency: 13`, `import: 13`
* *Defense:* `safety: 9`, `doc: 14`, `test: 1`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` impacket, configparser, util, signal, logging, threading, impacket.nt_errors, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ech_tests.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.921 IQR)
- **Top Global Matches:** file_cluster_8: 12.921, file_cluster_11: 12.988, file_cluster_0: 13.068
- **Magnitude:** 1836.14 | **LOC:** 1103 | **CtrlFlow:** 97.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.5672%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 1481.6)
  * `__global_context__` (Impact: 38.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1034`, `structural_boundaries: 31`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 164`, `state_mutation: 295`, `dead_code: 5`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 128`, `api: 2`, `import: 2`
* *Defense:* `safety: 26`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/sws.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.202 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.523 IQR)
- **Top Global Matches:** file_cluster_11: 14.202, file_cluster_8: 14.209, file_cluster_0: 14.221
- **Magnitude:** 1828.4 | **LOC:** 2484 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 84.6%
- **Risk Profile:** Cognitive Load (41.4702%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sws_ProcessRequest` (Impact: 287.3)
  * `sws_send_doc` (Impact: 87.6)
  * `connect_to` (Impact: 77.9)
  * `sws_parse_servercmd` (Impact: 75.2)
    * *Intent:* *optr = 0; /* in case no sprintf was used */
  * `http_connect` (Impact: 72.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 104`, `args: 8`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 856`, `dead_code: 6`, `orphaned_logic: 4`
* *Architecture:* `io: 41`, `api: 235`, `import: 2`
* *Defense:* `safety: 28`, `doc: 1`, `immutability_locks: 32`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tcp.h, first.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_formparse.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.347 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.279 IQR)
- **Top Global Matches:** file_cluster_8: 14.347, file_cluster_13: 14.457, file_cluster_11: 14.512
- **Magnitude:** 1544.2 | **LOC:** 898 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (85.2745%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_param_part` (Impact: 210.1)
  * `formparse` (Impact: 156.6)
    * *Intent:* * * If literal_value is set, any initial '@' or '<' in the value string * loses its special meaning,...
  * `tool_mime_new_filedata` (Impact: 62.1)
    * *Intent:* /*
  * `get_param_word` (Impact: 48.8)
  * `tool2curlparts` (Impact: 33.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 65`, `args: 11`, `func_start: 15`, `class_start: 16`
* *Risk/State:* `state_mutation: 769`
* *Architecture:* `io: 8`, `api: 144`, `import: 6`
* *Defense:* `safety: 9`, `doc: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` tool_setup.h, tool_cfgable.h, tool_msgs.h, tool_paramhlp.h, tool_formparse.h, tool_parsecfg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/rtspd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.249 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.545 IQR)
- **Top Global Matches:** file_cluster_0: 14.249, file_cluster_11: 14.255, file_cluster_8: 14.322
- **Magnitude:** 1536.88 | **LOC:** 1362 | **CtrlFlow:** 83.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.0547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rtspd_ProcessRequest` (Impact: 236.8)
    * *Intent:* #define REQUEST_KEYWORD_SIZE_TXT "255" #define CMD_AUTH_REQUIRED "auth_required" /* 'idle' means tha...
  * `test_rtspd` (Impact: 190.2)
  * `rtspd_send_doc` (Impact: 89.1)
  * `rtspd_storerequest` (Impact: 32.2)
  * `rtspd_get_request` (Impact: 30.5)
    * *Intent:* return 1; /* done */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 63`, `args: 3`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `state_mutation: 778`, `dead_code: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 41`, `api: 159`, `import: 2`
* *Defense:* `safety: 25`, `doc: 1`, `immutability_locks: 17`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tcp.h, first.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/runner.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.321 IQR)
- **Top Global Matches:** file_cluster_0: 13.321, file_cluster_13: 13.479, file_cluster_8: 13.513
- **Magnitude:** 1367.36 | **LOC:** 1527 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.1143%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `runner_init` (Impact: 464.9)
    * *Intent:* ####################################################################### # Initialize the runner and ...
  * `ipcrecv` (Impact: 37.2)
    * *Intent:* ################################################################### # Receive an IPC call in the run...
  * `runnerar` (Impact: 30.5)
    * *Intent:* ################################################################### # Receive async response of a pr...
  * `singletest_postcheck` (Impact: 20.7)
    * *Intent:* ####################################################################### # Verify that the postcheck ...
  * `runner_test_run` (Impact: 14.5)
    * *Intent:* ################################################################### # Run a single test case with an...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 299`, `args: 21`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 724`, `dead_code: 5`, `planned_debt: 4`
* *Architecture:* `io: 27`, `api: 3`, `concurrency: 6`, `import: 17`
* *Defense:* `safety: 3`, `sync_locks: 2`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.783
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002299
  * `Imports (Out-Degree: 6):` strict, binary, Storable, memanalyzer, something, valgrind, longer, warnings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `projects/OS400/ccsidcurl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.757 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.111 IQR)
- **Top Global Matches:** file_cluster_13: 13.757, file_cluster_8: 13.851, file_cluster_11: 14.003
- **Magnitude:** 1284.88 | **LOC:** 1473 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.4599%), Tech Debt (53.462%)
**Top Internal Functions/Classes:**
  * `curl_formadd_ccsid` (Impact: 152.8)
  * `curl_easy_setopt_ccsid` (Impact: 143.5)
  * `convert` (Impact: 81.5)
    * *Intent:* #include "curl.h" #include "mprintf.h" #include "slist.h" #include "urldata.h" #include "url.h" #inc...
  * `Curl_formadd_convert` (Impact: 22.1)
  * `Curl_formget_callback_ccsid` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 87`, `args: 13`, `func_start: 25`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 513`, `orphaned_logic: 19`
* *Architecture:* `api: 260`, `import: 15`
* *Defense:* `safety: 13`, `doc: 3`, `immutability_locks: 20`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` string.h, stdarg.h, slist.h, ccsidcurl.h, mprintf.h, setopt.h, stddef.h, url.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/testenv/curl.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.956 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.579 IQR)
- **Top Global Matches:** file_cluster_0: 12.956, file_cluster_11: 13.048, file_cluster_16: 13.065
- **Magnitude:** 1275.44 | **LOC:** 1309 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (45.7703%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 133.0)
  * `_complete_args` (Impact: 114.0)
  * `http_delete` (Impact: 68.1)
  * `_run` (Impact: 62.0)
  * `__init__` (Impact: 56.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 236`, `args: 88`, `func_start: 88`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 4`, `state_mutation: 374`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 57`, `api: 86`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 51`, `doc: 2`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` functools, datetime, typing, shutil, statistics, urllib.parse, psutil, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/sockfilt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.557 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.162 IQR)
- **Top Global Matches:** file_cluster_8: 13.557, file_cluster_11: 13.718, file_cluster_0: 13.721
- **Magnitude:** 1201.04 | **LOC:** 1412 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 91.7%
- **Risk Profile:** Cognitive Load (39.7809%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `select_ws` (Impact: 157.8)
    * *Intent:* #define SOCKFILT_read read_wincon #define SOCKFILT_write write_wincon #else #define SOCKFILT_read re...
  * `test_sockfilt` (Impact: 126.0)
  * `juggle` (Impact: 71.5)
    * *Intent:* /* retrieve an event from the console buffer */
  * `select_ws_wait_thread` (Impact: 70.4)
    * *Intent:* /*************************************************************************** * _ _ ____ _ * Project ...
  * `disc_handshake` (Impact: 24.7)
    * *Intent:* /* The handle represents a file on disk, this means: * - WaitForMultipleObjectsEx will always be sig...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 62`, `args: 4`, `func_start: 6`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 598`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `api: 133`, `import: 1`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` first.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_writeout.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.613 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.105 IQR)
- **Top Global Matches:** file_cluster_8: 13.613, file_cluster_13: 13.689, file_cluster_0: 13.707
- **Magnitude:** 1133.64 | **LOC:** 874 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (80.1402%), Tech Debt (9.0549%)
**Top Internal Functions/Classes:**
  * `ourWriteOut` (Impact: 131.8)
  * `urlpart` (Impact: 96.0)
  * `writeString` (Impact: 80.5)
  * `output_header` (Impact: 47.4)
  * `outtime` (Impact: 40.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 83`, `args: 7`, `func_start: 11`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 468`, `dead_code: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 156`, `import: 4`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tool_setup.h, tool_cfgable.h, tool_writeout.h, tool_writeout_json.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_operate.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.069 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.115 IQR)
- **Top Global Matches:** file_cluster_13: 14.069, file_cluster_8: 14.322, file_cluster_11: 14.492
- **Magnitude:** 1096.52 | **LOC:** 2414 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 53.3%
- **Risk Profile:** Cognitive Load (77.0929%), Tech Debt (12.5064%)
**Top Internal Functions/Classes:**
  * `check_finished` (Impact: 219.7)
  * `operate` (Impact: 88.4)
  * `cacertpaths` (Impact: 57.5)
  * `parallel_event` (Impact: 33.4)
  * `add_parallel_transfers` (Impact: 29.1)
    * *Intent:* /* * Check if a given string is a PKCS#11 URI
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 103`, `args: 7`, `func_start: 18`, `class_start: 21`
* *Risk/State:* `state_mutation: 423`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 131`, `import: 39`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` tool_urlglob.h, tool_writeout.h, tool_progress.h, tool_easysrc.h, tool_cb_prg.h, dos.h, tool_operhlp.h, tool_ssls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/config2setopts.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.121 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.806 IQR)
- **Top Global Matches:** file_cluster_8: 13.121, file_cluster_13: 13.216, file_cluster_7: 13.483
- **Magnitude:** 1065.4 | **LOC:** 1067 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (78.4373%), Tech Debt (8.4528%)
**Top Internal Functions/Classes:**
  * `config2setopts` (Impact: 134.3)
  * `ssl_setopts` (Impact: 92.7)
  * `tlsversion` (Impact: 49.0)
  * `url_proto_and_rewrite` (Impact: 42.5)
  * `http_setopts` (Impact: 41.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 75`, `args: 19`, `func_start: 19`, `class_start: 10`
* *Risk/State:* `state_mutation: 317`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 113`, `import: 18`
* *Defense:* `doc: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` tool_setup.h, tool_setopt.h, tool_cfgable.h, tool_cb_rea.h, tool_findfile.h, tool_cb_dbg.h, tool_version.h, tool_msgs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tool_doswin.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.022 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.096 IQR)
- **Top Global Matches:** file_cluster_13: 14.022, file_cluster_11: 14.122, file_cluster_0: 14.159
- **Magnitude:** 1050.9 | **LOC:** 919 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (85.2361%), Tech Debt (17.9206%)
**Top Internal Functions/Classes:**
  * `msdosify` (Impact: 368.1)
    * *Intent:* #endif /* * Test if truncating a path to a file leaves at least a single character * in the filename...
  * `rename_if_reserved_dos` (Impact: 81.3)
  * `sanitize_file_name` (Impact: 72.8)
    * *Intent:* /* dos_name is truncated, check that truncation requirements are met,
  * `win32_stdin_read_thread` (Impact: 56.1)
  * `win_stdin_thread_func` (Impact: 30.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 52`, `args: 8`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `state_mutation: 327`, `dead_code: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 80`, `import: 8`
* *Defense:* `safety: 10`, `doc: 1`, `test: 3`, `immutability_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tool_setup.h, fcntl.h, tool_cfgable.h, tool_msgs.h, basename.h, tool_doswin.h, version_win32.h, tlhelp32.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/scorecard.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.541 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.37 IQR)
- **Top Global Matches:** file_cluster_8: 11.541, file_cluster_13: 11.776, file_cluster_0: 11.795
- **Magnitude:** 952.14 | **LOC:** 1026 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.3105%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `do_requests` (Impact: 233.4)
  * `fmt_speed_result` (Impact: 114.8)
  * `__init__` (Impact: 37.0)
  * `downloads` (Impact: 35.7)
  * `uploads` (Impact: 31.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 126`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 219`, `orphaned_logic: 1`
* *Architecture:* `io: 30`, `api: 33`, `import: 10`
* *Defense:* `safety: 11`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, typing, logging, re, os, argparse, statistics, testenv...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/mqttd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.673 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.164 IQR)
- **Top Global Matches:** file_cluster_11: 14.673, file_cluster_0: 14.686, file_cluster_9: 14.824
- **Magnitude:** 915.5 | **LOC:** 897 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 90.0%
- **Risk Profile:** Cognitive Load (39.9195%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_mqttd` (Impact: 84.5)
  * `mqttit` (Impact: 64.6)
  * `mqttd_getconfig` (Impact: 34.2)
    * *Intent:* * * Read commands from FILE (set with --config). The commands control how to * act and is reset to d...
  * `mqttd_incoming` (Impact: 16.6)
  * `publish` (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 43`, `args: 4`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 501`, `dead_code: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 149`, `import: 1`
* *Defense:* `safety: 40`, `doc: 1`, `immutability_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` first.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/checksrc.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.145 IQR)
- **Top Global Matches:** file_cluster_13: 14.145, file_cluster_17: 14.255, file_cluster_8: 14.269
- **Magnitude:** 901.9 | **LOC:** 1246 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 81.2%
- **Risk Profile:** Cognitive Load (81.7192%), Tech Debt (16.059%)
**Top Internal Functions/Classes:**
  * `checkwarn` (Impact: 47.9)
  * `readlocalfile` (Impact: 14.0)
    * *Intent:* # Reads the .checksrc in $dir for any extended warnings to enable locally. # Currently there is no s...
  * `readskiplist` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 149`, `args: 17`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 814`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 29`, `import: 29`
* *Defense:* `safety: 2`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, strict, to, a, SOCK, support, tool_stderr, ifdef...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/http/testenv/env.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.331 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.976 IQR)
- **Top Global Matches:** file_cluster_0: 12.331, file_cluster_11: 12.591, file_cluster_16: 12.717
- **Magnitude:** 887.44 | **LOC:** 856 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.8726%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 142.7)
  * `version` (Impact: 16.3)
  * `make_data_gzipbomb` (Impact: 14.4)
  * `make_data_file` (Impact: 13.0)
  * `get_incomplete_reason` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 266`, `args: 109`, `func_start: 109`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 6`, `state_mutation: 232`, `fragile_debt: 2`, `duplicate_logic: 16`
* *Architecture:* `io: 42`, `api: 152`, `import: 13`
* *Defense:* `safety: 5`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.234
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.02069
  * `Imports (Out-Degree: 1):` datetime, pytest, configparser, filelock, typing, shutil, gzip, logging...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/tool_paramhlp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.211 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.623 IQR)
- **Top Global Matches:** file_cluster_13: 14.211, file_cluster_11: 14.326, file_cluster_0: 14.349
- **Magnitude:** 868.88 | **LOC:** 733 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (64.5636%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `proto2num` (Impact: 93.8)
  * `file2memory_range` (Impact: 50.1)
  * `checkpasswd` (Impact: 29.4)
  * `get_args` (Impact: 20.4)
  * `file2string` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 83`, `args: 23`, `func_start: 24`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 354`, `dead_code: 3`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `io: 2`, `api: 151`, `import: 9`
* *Defense:* `safety: 22`, `doc: 10`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` tool_setup.h, tool_getparam.h, tool_cfgable.h, tool_libinfo.h, tool_version.h, tool_msgs.h, tool_util.h, tool_paramhlp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sshserver.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.777 IQR)
- **Top Global Matches:** file_cluster_0: 13.777, file_cluster_8: 13.87, file_cluster_13: 13.905
- **Magnitude:** 855.2 | **LOC:** 1207 | **CtrlFlow:** 76.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.4999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sshd_supports_opt` (Impact: 13.4)
    * *Intent:* #*************************************************************************** # Verifies at run time ...
  * `pp` (Impact: 1.2)
    * *Intent:* #*************************************************************************** # Returns a path of the...
  * `logmsg` (Impact: 1.2)
    * *Intent:* #*************************************************************************** # Save the message to t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 79`, `args: 9`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 38`, `state_mutation: 825`, `planned_debt: 1`
* *Architecture:* `io: 14`, `import: 17`
* *Defense:* `safety: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` warnings, and, strict, Digest::SHA, serverhelp, File::Basename, native, MIME::Base64...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server/dnsd.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.99 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.248 IQR)
- **Top Global Matches:** file_cluster_8: 13.99, file_cluster_0: 14.221, file_cluster_13: 14.225
- **Magnitude:** 844.76 | **LOC:** 679 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.4952%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dnsd` (Impact: 151.4)
  * `read_instructions` (Impact: 35.5)
    * *Intent:* */ 0x0, 0x1, /* QDCOUNT a single question */
  * `store_incoming` (Impact: 32.3)
    * *Intent:* *size -= (p - *pkt); *pkt = p;
  * `send_response` (Impact: 26.0)
    * *Intent:* bytes[i++] = 0x0c; /* points to the query at this fixed packet index */
  * `qname` (Impact: 13.2)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/testutil.pm` (PERL) | Magnitude: 351.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 255, indent_spaces: 129, structural_boundaries: 72, regex_execution: 68
- `tests/server/rtspd.c` (C) | Magnitude: 1536.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 980, state_mutation: 778, branch: 321, pointers: 267
- `tests/http/testenv/certs.py` (PYTHON) | Magnitude: 418.4 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 464, structural_boundaries: 136, branch: 99, encapsulation: 89
- `tests/unit/unit1307.c` (C) | Magnitude: 250.32 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 219, branch: 94, sec_reflection_metaprogramming: 48, state_mutation: 33
- `scripts/delta` (PERL) | Magnitude: 179.9 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 170, indent_spaces: 49, branch: 45, structural_boundaries: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/server/sws.c` (C) | Magnitude: 1828.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1134, state_mutation: 856, branch: 412, pointers: 363
- `tests/server/tftpd.c` (C) | Magnitude: 652.06 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 379, state_mutation: 371, branch: 129, pointers: 60
- `tests/server/mqttd.c` (C) | Magnitude: 915.5 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 621, state_mutation: 501, branch: 153, api: 149
- `tests/server/getpart.c` (C) | Magnitude: 244.76 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 128, indent_spaces: 118, pointers: 60, branch: 45
- `.github/scripts/cmp-pkg-config.sh` (SHELL) | Magnitude: 7.85 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 39, indent_spaces: 25, branch: 24, safety: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/unit/unit1653.c` (C) | Magnitude: 281.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 153, state_mutation: 129, branch: 53, api: 32
- `scripts/firefox-db2pem.sh` (SHELL) | Magnitude: 3.19 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, io: 14, branch: 9, structural_boundaries: 9
- `projects/OS400/initscript.sh` (SHELL) | Magnitude: 211.96 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 116, reflection_metaprogramming: 107, branch: 78, state_mutation: 75
- `appveyor.sh` (SHELL) | Magnitude: 134.14 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: branch: 84, indent_spaces: 65, reflection_metaprogramming: 39, io: 38
- `projects/OS400/make-include.sh` (SHELL) | Magnitude: 58.34 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: reflection_metaprogramming: 39, state_mutation: 26, safety: 21, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/unit/unit3212.c` (C) | Magnitude: 80.74 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 73, pointers: 67, state_mutation: 49, branch: 7
- `scripts/top-complexity` (PERL) | Magnitude: 141.18 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 51, branch: 35, structural_boundaries: 28
- `src/tool_xattr.c` (C) | Magnitude: 124.68 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 58, api: 24, branch: 19
- `tests/unit/unit2601.c` (C) | Magnitude: 204.16 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 172, state_mutation: 112, pointers: 73, branch: 42
- `src/tool_parsecfg.h` (C) | Magnitude: 17.16 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 4, structural_boundaries: 3, api: 3, macros: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/mk-unity.pl` (PERL) | Magnitude: 105.1 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 75, indent_spaces: 57, branch: 23, structural_boundaries: 20
- `scripts/singleuse.pl` (PERL) | Magnitude: 89.64 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 175, state_mutation: 78, branch: 29, structural_boundaries: 19
- `tests/getpart.pm` (PERL) | Magnitude: 435.98 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 266, state_mutation: 234, structural_boundaries: 104, branch: 99
- `.github/scripts/cleancmd.pl` (PERL) | Magnitude: 189.66 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 129, indent_spaces: 62, branch: 37, structural_boundaries: 17
- `src/Makefile.am` (MAKEFILE) | Magnitude: 577.68 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 45, branch: 44, structural_boundaries: 43, indent_tabs: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/wcurl` (SHELL) | Magnitude: 254.7 | Delta: **0.354 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 145, state_mutation: 95, branch: 78, io: 56
- `scripts/perlcheck.sh` (SHELL) | Magnitude: 2.46 | Delta: **0.641 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 8, io: 8, indent_spaces: 8, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/tool_cb_hdr.h` (C) | Magnitude: 24.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 12, structural_boundaries: 9, api: 9, class_start: 6
- `tests/test1544.pl` (PERL) | Magnitude: 164.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 111, indent_spaces: 68, branch: 36, structural_boundaries: 23
- `tests/http/test_17_ssl_use.py` (PYTHON) | Magnitude: 394.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 484, test: 148, structural_boundaries: 108, branch: 104
- `src/tool_hugehelp.h` (C) | Magnitude: 16.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, macros: 3, pointers: 3, immutability_locks: 3
- `tests/unit/unit1607.c` (C) | Magnitude: 212.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 95, branch: 39, pointers: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `scripts/dmaketgz` (SHELL) | Magnitude: 19.88 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, branch: 7, state_mutation: 6, reflection_metaprogramming: 5
- `scripts/release-tools.sh` (SHELL) | Magnitude: 3.4 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: io: 15, state_mutation: 15, branch: 10, args: 6
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

- `src/tool_operate.c` -> Churn: **82.57%** | Cog Load: 77.0929% | Debt: 12.5064%
- `src/tool_getparam.c` -> Churn: **76.42%** | Cog Load: 75.2837% | Debt: 29.7083%
- `src/tool_doswin.c` -> Churn: **66.91%** | Cog Load: 85.2361% | Debt: 17.9206%
- `src/tool_cb_hdr.c` -> Churn: **66.67%** | Cog Load: 86.7842% | Debt: 10.7422%
- `src/config2setopts.c` -> Churn: **65.11%** | Cog Load: 78.4373% | Debt: 8.4528%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/servers.pm` -> **Viktor Szakats** (83.3% isolated ownership) | Magnitude: 3191.36
- `scripts/managen` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 2524.62
- `tests/server/sws.c` -> **Viktor Szakats** (84.6% isolated ownership) | Magnitude: 1828.4
- `tests/server/rtspd.c` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 1536.88
- `tests/runner.pm` -> **Viktor Szakats** (100.0% isolated ownership) | Magnitude: 1367.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `include/curl/curl.h` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 82.6545%)
- `src/tool_cfgable.h` -> **Severity: 0.01** (Bridge: 0.0007 * Flux: 13.0216%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/tool_cfgable.h` -> **Severity: 3.886** (Embedded: 0.0754 * Error Risk: 51.513%)
- `src/tool_sdecls.h` -> **Severity: 2.486** (Embedded: 0.0421 * Error Risk: 59.0025%)
- `tests/pathhelp.pm` -> **Severity: 2.19** (Embedded: 0.0237 * Error Risk: 92.3371%)
- `tests/serverhelp.pm` -> **Severity: 1.969** (Embedded: 0.0209 * Error Risk: 94.2311%)
- `src/tool_getparam.h` -> **Severity: 1.879** (Embedded: 0.0365 * Error Risk: 51.4316%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/tool_setup.h` -> **Severity: 2613.167** (Blast Radius: 111.439 * Doc Risk: 23.4493%)
- `src/tool_cfgable.h` -> **Severity: 1499.0** (Blast Radius: 14.99 * Doc Risk: 100.0%)
- `include/curl/curl.h` -> **Severity: 951.7** (Blast Radius: 9.517 * Doc Risk: 100.0%)
- `src/tool_getparam.h` -> **Severity: 626.735** (Blast Radius: 9.869 * Doc Risk: 63.5054%)
- `src/tool_operate.h` -> **Severity: 543.3** (Blast Radius: 5.433 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
