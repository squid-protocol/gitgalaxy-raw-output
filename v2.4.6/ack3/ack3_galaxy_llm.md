# ARCHITECTURAL_BRIEF: ack3
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/ack3` |
| **Timestamp** | `2026-08-03T19:29:33.332875+00:00` |
| **Scan Duration** | `0.53s` |
| **Git Branch** | `dev` |
| **Git Commit** | `1c9cfd3508dd1109815d85e64c55656b00454289` |
| **Git Remote** | `https://github.com/beyondgrep/ack3.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Total Artifacts | 297 |
| Analyzed Artifacts (Scanned) | 175 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 122 |
| Total LOC | 11211 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 58.9% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0294 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9701 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 99 | 9329 | 56.6% |
| YAML | 27 | 1602 | 15.4% |
| PLAINTEXT | 15 | 0 | 8.6% |
| MARKDOWN | 12 | 0 | 6.9% |
| HTML | 5 | 142 | 2.9% |
| SHELL | 3 | 15 | 1.7% |
| CSHARP | 3 | 8 | 1.7% |
| RUBY | 2 | 64 | 1.1% |
| C | 2 | 17 | 1.1% |
| FORTRAN | 2 | 22 | 1.1% |
| DOCKERFILE | 1 | 5 | 0.6% |
| MAKEFILE | 1 | 1 | 0.6% |
| CSS | 1 | 1 | 0.6% |
| JAVASCRIPT | 1 | 2 | 0.6% |
| PYTHON | 1 | 3 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.843`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 57 | 32.6% |
| file_cluster_13 | 51 | 29.1% |
| file_cluster_0 | 31 | 17.7% |
| file_cluster_17 | 6 | 3.4% |
| file_cluster_4 | 2 | 1.1% |
| file_cluster_9 | 1 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 15.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 122*

**Composition by Extension & Reason:**
- `no_extension`: 27x Unsupported Format (.undeterminable), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 114 LOC)
- `.pm`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.0`: 10x Excluded (Unsupported Extension: '.0')
- `.xxx`: 8x Excluded (Unsupported Extension: '.xxx')
- `.1`: 1x Excluded (Machine-Generated Source Code Signature: 5566 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5800 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5914 LOC)
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2131 LOC)
- `.2`: 1x Excluded (Machine-Generated Source Code Signature: 5616 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5851 LOC), 1x Excluded (Machine-Generated Source Code Signature: 6290 LOC)
- `.py`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3`: 1x Excluded (Machine-Generated Source Code Signature: 5619 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5849 LOC)
- `.min`: 2x Excluded (Unsupported Extension: '.min')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.96`: 1x Excluded (Unsupported Extension: '.96')
- `.22`: 1x Excluded (Unsupported Extension: '.22')
- `.24`: 1x Excluded (Unsupported Extension: '.24')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 44.7 | 41.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 39.0 | 29.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.0 | 0.3 | 0.0 |
| API Exposure | 0.0 | 8.0 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 59.2 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 46.1 | 39.0 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/Util.pm` (Hits: 64)
- `ack` (Hits: 58)
- `dev/linecount-fork` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Util.pm** (`t/Util.pm`) — 66 inbound connections
2. **ack** (`ack`) — 1 inbound connections
3. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
4. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
5. **DESIGN.md** (`DESIGN.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ack** (`ack`) — 47 outbound dependencies
2. **Util.pm** (`t/Util.pm`) — 19 outbound dependencies
3. **Cookbook.pm** (`dev/Cookbook.pm`) — 13 outbound dependencies
4. **timings.pl** (`dev/timings.pl`) — 13 outbound dependencies
5. **00-load.t** (`t/00-load.t`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `lists_match` (@ `t/Util.pm`) -> Impact: **2066.5** | LOC: 743
  * *Intent:* # Use this one if order is important.
- `run_cmd` (@ `t/Util.pm`) -> Impact: **497.0** | LOC: 125
  * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus writes its STDERR to $catcherr_file). # # Sets $a...
- `_where` (@ `dev/generate-rgb-codes.pl`) -> Impact: **277.4** | LOC: 118
- `_test_project_ackrc` (@ `t/forbidden-options.t`) -> Impact: **122.2** | LOC: 103
  * *Intent:* # Test project directory # ackrc in /tmp/x/project/.ackrc
- `_populate_man_options` (@ `xt/man.t`) -> Impact: **94.5** | LOC: 71
- `are_mutually_exclusive` (@ `t/mutex-options.t`) -> Impact: **55.0** | LOC: 39
  * *Intent:* # Do this without system().
- `time_ack` (@ `dev/timings.pl`) -> Impact: **53.0** | LOC: 61
- `check_for_option_in_man_output` (@ `xt/man.t`) -> Impact: **49.0** | LOC: 18
- `build_ack_invocation` (@ `t/Util.pm`) -> Impact: **42.1** | LOC: 43
- `check_with` (@ `t/file-permission.t`) -> Impact: **38.9** | LOC: 28

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `lists_match` (@ `t/Util.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* # Use this one if order is important.
- `_where` (@ `dev/generate-rgb-codes.pl`) -> **O(2^N) [Recursive]**
- `reslash` (@ `t/Util.pm`) -> **O(2^N) [Recursive]**
- `foo` (@ `t/range/rangefile.pm`) -> **O(2^N) [Recursive]**
  * *Intent:* # This function calls print on "foo".
- `bar` (@ `t/range/rangefile.pm`) -> **O(2^N) [Recursive]**
- `run_cmd` (@ `t/Util.pm`) -> **O(N^6)**
  * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus writes its STDERR to $catcherr_file). # # Sets $a...
- `_populate_help_options` (@ `t/ack-help.t`) -> **O(N^6)**
- `_populate_man_options` (@ `xt/man.t`) -> **O(N^6)**
- `_test_project_ackrc` (@ `t/forbidden-options.t`) -> **O(N^5)**
  * *Intent:* # Test project directory # ackrc in /tmp/x/project/.ackrc
- `time_ack` (@ `dev/timings.pl`) -> **O(N^4)**

### Highest Data Gravity (Database Complexity)
- `lists_match` (@ `t/Util.pm`) -> DB Complexity: **249**
  * *Intent:* # Use this one if order is important.
- `run_cmd` (@ `t/Util.pm`) -> DB Complexity: **92**
  * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus writes its STDERR to $catcherr_file). # # Sets $a...
- `run_piped` (@ `t/Util.pm`) -> DB Complexity: **74**
- `invalid_combinations` (@ `dev/crank-mutex`) -> DB Complexity: **36**
- `time_ack` (@ `dev/timings.pl`) -> DB Complexity: **32**
- `_populate_man_options` (@ `xt/man.t`) -> DB Complexity: **28**
- `_test_project_ackrc` (@ `t/forbidden-options.t`) -> DB Complexity: **22**
  * *Intent:* # Test project directory # ackrc in /tmp/x/project/.ackrc
- `_where` (@ `dev/generate-rgb-codes.pl`) -> DB Complexity: **21**
- `MY` (@ `Makefile.PL`) -> DB Complexity: **15**
- `build_ack_invocation` (@ `t/Util.pm`) -> DB Complexity: **13**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 13 | 66492.54 | 9.04% | 22.94% |
| `t` | 98 | 10520.0 | 52.01% | 7.34% |
| `dev` | 15 | 1204.16 | 62.11% | 3.17% |
| `xt` | 4 | 409.94 | 70.19% | 0.0% |
| `t/swamp` | 27 | 274.81 | 4.25% | 14.33% |
| `t/range` | 5 | 68.38 | 12.99% | 0.0% |
| `dev/docker` | 3 | 26.86 | 5.0% | 33.33% |
| `t/text` | 9 | 26.12 | 0.0% | 0.0% |
| `t/swamp/swamp` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/ack-k.yaml` -> **100.0%** Exposure
- `dev/docker/docker-entrypoint.sh` -> **100.0%** Exposure
- `stack` -> **100.0%** Exposure
- `tack` -> **100.0%** Exposure
- `t/swamp/crystallography-weenies.f` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ack` -> **100.0%** Exposure
- `dev/Cookbook.pm` -> **100.0%** Exposure
- `dev/crank-mutex` -> **100.0%** Exposure
- `dev/generate-rgb-codes.pl` -> **100.0%** Exposure
- `dev/issues-scrub.pl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/range.t` -> **0** Orphaned Functions | **4** Duplicates
- `Makefile.PL` -> **0** Orphaned Functions | **2** Duplicates
- `t/swamp/Rakefile` -> **2** Orphaned Functions | **0** Duplicates
- `t/ack-ignore-dir.t` -> **1** Orphaned Functions | **0** Duplicates
- `dev/docker/docker-entrypoint.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`dev/docker/docker-entrypoint.sh`** -> AI Confidence: **99.29%**
2. **`t/swamp/sample.rake`** -> AI Confidence: **99.29%**
3. **`t/swamp/Rakefile`** -> AI Confidence: **98.96%**
4. **`dev/docker/Dockerfile`** -> AI Confidence: **98.84%**
5. **`stack`** -> AI Confidence: **98.84%**
6. **`tack`** -> AI Confidence: **98.84%**
7. **`t/swamp/Makefile`** -> AI Confidence: **98.84%**
8. **`t/swamp/Sample.ascx`** -> AI Confidence: **98.84%**
9. **`t/swamp/Sample.asmx`** -> AI Confidence: **98.84%**
10. **`t/swamp/service.svc`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `ack` -> **100.0%** Exposure
- `dev/generate-rgb-codes.pl` -> **100.0%** Exposure
- `dev/timings.pl` -> **100.0%** Exposure
- `t/Util.pm` -> **100.0%** Exposure
- `t/ack-help.t` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `dev/linecount-fork` -> **100.0%** Exposure
- `dev/timings.pl` -> **100.0%** Exposure
- `t/Util.pm` -> **100.0%** Exposure
- `t/process-substitution.t` -> **100.0%** Exposure
- `dev/Cookbook.pm` -> **55.7238%** Exposure
### Algorithmic DoS Exposure
- `dev/crank-mutex` -> **100.0%** Exposure
- `dev/generate-rgb-codes.pl` -> **100.0%** Exposure
- `dev/timings.pl` -> **100.0%** Exposure
- `t/Util.pm` -> **100.0%** Exposure
- `t/ack-help.t` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `614` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/Util.pm` (PERL) -> Cumulative Risk: **1014.84**
- **Archetype:** `file_cluster_0` (Distance: 13.615 IQR)
- **Magnitude:** 3699.42 | **LOC:** 1380 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Churn (100.0%)
- **Heaviest Functions:** `lists_match` (Impact: 2066.5), `run_cmd` (Impact: 497.0), `build_ack_invocation` (Impact: 42.1)

### 2. `dev/timings.pl` (PERL) -> Cumulative Risk: **895.15**
- **Archetype:** `file_cluster_17` (Distance: 12.532 IQR)
- **Magnitude:** 338.42 | **LOC:** 408 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `time_ack` (Impact: 53.0), `grab_versions` (Impact: 29.3), `color` (Impact: 13.1)

### 3. `xt/man.t` (PERL) -> Cumulative Risk: **767.19**
- **Archetype:** `file_cluster_13` (Distance: 12.972 IQR)
- **Magnitude:** 272.28 | **LOC:** 132 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_populate_man_options` (Impact: 94.5), `check_for_option_in_man_output` (Impact: 49.0), `strip_special_chars` (Impact: 13.6)

### 4. `dev/generate-rgb-codes.pl` (PERL) -> Cumulative Risk: **754.56**
- **Archetype:** `file_cluster_0` (Distance: 20.13 IQR)
- **Magnitude:** 341.58 | **LOC:** 150 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_where` (Impact: 277.4), `_five_to_1` (Impact: 1.6)

### 5. `t/process-substitution.t` (PERL) -> Cumulative Risk: **741.58**
- **Archetype:** `file_cluster_4` (Distance: 12.01 IQR)
- **Magnitude:** 51.84 | **LOC:** 58 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)

### 6. `dev/linecount-fork` (PERL) -> Cumulative Risk: **700.01**
- **Archetype:** `file_cluster_4` (Distance: 13.105 IQR)
- **Magnitude:** 63.74 | **LOC:** 46 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%)

### 7. `t/forbidden-options.t` (PERL) -> Cumulative Risk: **670.05**
- **Archetype:** `file_cluster_0` (Distance: 12.745 IQR)
- **Magnitude:** 210.54 | **LOC:** 145 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_test_project_ackrc` (Impact: 122.2), `_create_ackrc` (Impact: 4.7)

### 8. `t/ack-help.t` (PERL) -> Cumulative Risk: **661.08**
- **Archetype:** `file_cluster_13` (Distance: 12.415 IQR)
- **Magnitude:** 95.42 | **LOC:** 72 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_populate_help_options` (Impact: 22.2), `option_in_usage` (Impact: 22.0), `get_help_options` (Impact: 3.2)

### 9. `t/file-permission.t` (PERL) -> Cumulative Risk: **588.9**
- **Archetype:** `file_cluster_13` (Distance: 12.274 IQR)
- **Magnitude:** 75.66 | **LOC:** 88 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.9891%), Documentation (98.6537%)
- **Heaviest Functions:** `check_with` (Impact: 38.9), `o` (Impact: 8.7)

### 10. `t/mutex-options.t` (PERL) -> Cumulative Risk: **586.91**
- **Archetype:** `file_cluster_8` (Distance: 13.568 IQR)
- **Magnitude:** 357.6 | **LOC:** 225 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Safety Score (99.7437%)
- **Heaviest Functions:** `are_mutually_exclusive` (Impact: 55.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ack` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.365 IQR)
- **Top Global Matches:** file_cluster_0: 14.365, file_cluster_13: 14.588, file_cluster_17: 14.684
- **Magnitude:** 66367.82 | **LOC:** 2545 | **CtrlFlow:** 79.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.8081%), Tech Debt (10.1462%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1146`, `structural_boundaries: 299`, `args: 30`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 12`, `state_mutation: 1568`, `fragile_debt: 3`
* *Architecture:* `io: 58`, `import: 54`
* *Defense:* `safety: 4`, `doc: 161`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.976
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005747
  * `Imports (Out-Degree: 0):` B, F, App::Ack::ConfigLoader, App::Ack, critic, file, C, warnings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.615 IQR)
- **Top Global Matches:** file_cluster_0: 13.615, file_cluster_4: 13.661, file_cluster_13: 13.873
- **Magnitude:** 3699.42 | **LOC:** 1380 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 249
- **Risk Profile:** Cognitive Load (95.6598%), Tech Debt (13.9159%)
**Top Internal Functions/Classes:**
  * `lists_match` (Impact: 2066.5 | O(2^N) | DB: 249)
    * *Intent:* # Use this one if order is important.
  * `run_cmd` (Impact: 497.0 | O(N^6) | DB: 92)
    * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus...
  * `build_ack_invocation` (Impact: 42.1 | O(N^4) | DB: 13)
  * `run_piped` (Impact: 35.0 | O(N^3) | DB: 74)
  * `_do_parent` (Impact: 34.7 | O(N^4) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 380`, `structural_boundaries: 297`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 760`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 64`, `api: 2`, `concurrency: 73`, `import: 21`
* *Defense:* `safety: 3`, `doc: 6`, `test: 19`, `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 246.184
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.37931
  * `Imports (Out-Degree: 0):` File::Temp, Test::More, critic, Carp, warnings, Cwd, Term::ANSIColor, Win32::ShellQuote...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `t/config-loader.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.016 IQR)
- **Top Global Matches:** file_cluster_8: 12.016, file_cluster_0: 12.017, file_cluster_13: 12.079
- **Magnitude:** 796.24 | **LOC:** 298 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (51.806%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 60`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 143`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 8`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` targets, App::Ack::ConfigLoader, Test::More, warnings, Util, lib, argument, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-output-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.279 IQR)
- **Top Global Matches:** file_cluster_0: 13.279, file_cluster_8: 13.509, file_cluster_13: 13.64
- **Magnitude:** 469.5 | **LOC:** 450 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (84.8525%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 115`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 448`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, Term::ANSIColor, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mutex-options.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.568 IQR)
- **Top Global Matches:** file_cluster_8: 13.568, file_cluster_13: 13.654, file_cluster_0: 13.764
- **Magnitude:** 357.6 | **LOC:** 225 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (66.0756%), Tech Debt (27.4438%)
**Top Internal Functions/Classes:**
  * `are_mutually_exclusive` (Impact: 55.0 | O(N^4) | DB: 11)
    * *Intent:* # Do this without system().
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 30`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 299`, `fragile_debt: 1`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/generate-rgb-codes.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 20.13 IQR)
- **Top Global Matches:** file_cluster_0: 20.13, file_cluster_17: 20.272, file_cluster_13: 20.406
- **Magnitude:** 341.58 | **LOC:** 150 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (76.7466%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_where` (Impact: 277.4 | O(2^N) | DB: 21)
  * `_five_to_1` (Impact: 1.6 | O(N^1) | DB: 1)
    * *Intent:* # Helper to scale Term::ANSIColor 0..5 R,G,B to 0.0 .. 1.0 standard
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 43`, `args: 3`, `func_start: 4`
* *Risk/State:* `state_mutation: 61`, `dead_code: 9`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Convert::Color, Convert::Color::HSL, strict, Readonly, Data::Dump, warnings, Term::ANSIColor, Convert::Color::RGB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/timings.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.532 IQR)
- **Top Global Matches:** file_cluster_17: 12.532, file_cluster_13: 12.544, file_cluster_8: 12.546
- **Magnitude:** 338.42 | **LOC:** 408 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (85.8222%), Tech Debt (17.9738%)
**Top Internal Functions/Classes:**
  * `time_ack` (Impact: 53.0 | O(N^4) | DB: 32)
  * `grab_versions` (Impact: 29.3 | O(N^4) | DB: 11)
  * `color` (Impact: 13.1 | O(N^2))
  * `create_format` (Impact: 12.6 | O(N^3) | DB: 2)
  * `counts_valid` (Impact: 9.8 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 90`, `args: 4`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 202`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` autodie, the, JSON, warnings, List::Util, Util, lib, Term::ANSIColor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/man.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.972 IQR)
- **Top Global Matches:** file_cluster_13: 12.972, file_cluster_0: 12.988, file_cluster_8: 13.131
- **Magnitude:** 272.28 | **LOC:** 132 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (91.5587%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_populate_man_options` (Impact: 94.5 | O(N^6) | DB: 28)
  * `check_for_option_in_man_output` (Impact: 49.0 | O(N^3) | DB: 5)
  * `strip_special_chars` (Impact: 13.6 | O(N^1) | DB: 4)
  * `get_man_options` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 31`, `args: 2`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 110`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` critic, Test::More, warnings, Util, lib, strict, Data::Dumper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-pager.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.967 IQR)
- **Top Global Matches:** file_cluster_0: 12.967, file_cluster_8: 13.487, file_cluster_13: 13.542
- **Magnitude:** 255.92 | **LOC:** 248 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.6902%), Tech Debt (16.6986%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 38`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 237`, `planned_debt: 1`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-type.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.653 IQR)
- **Top Global Matches:** file_cluster_0: 13.653, file_cluster_13: 13.709, file_cluster_8: 13.868
- **Magnitude:** 222.22 | **LOC:** 154 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.68%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 205`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lines, Test::More, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/forbidden-options.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.745 IQR)
- **Top Global Matches:** file_cluster_0: 12.745, file_cluster_13: 12.882, file_cluster_8: 13.177
- **Magnitude:** 210.54 | **LOC:** 145 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (90.4123%), Tech Debt (70.1334%)
**Top Internal Functions/Classes:**
  * `_test_project_ackrc` (Impact: 122.2 | O(N^5) | DB: 22)
    * *Intent:* # Test project directory # ackrc in /tmp/x/project/.ackrc
  * `_create_ackrc` (Impact: 4.7 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 31`, `args: 2`, `func_start: 3`
* *Risk/State:* `state_mutation: 82`, `fragile_debt: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Temp, Test::More, warnings, Util, lib, strict, File::Spec
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/Cookbook.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.404 IQR)
- **Top Global Matches:** file_cluster_13: 13.404, file_cluster_0: 13.418, file_cluster_17: 13.467
- **Magnitude:** 198.04 | **LOC:** 589 | **CtrlFlow:** 85.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.6104%), Tech Debt (29.5988%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 37`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 5`, `state_mutation: 176`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `import: 19`
* *Defense:* `safety: 1`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` longer, ack, args, changes, C, guarantee, LWP::Simple, of...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.175 IQR)
- **Top Global Matches:** file_cluster_13: 13.175, file_cluster_0: 13.195, file_cluster_8: 13.197
- **Magnitude:** 195.58 | **LOC:** 185 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.5618%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 54`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 178`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/context.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.947 IQR)
- **Top Global Matches:** file_cluster_13: 12.947, file_cluster_0: 13.025, file_cluster_8: 13.054
- **Magnitude:** 182.66 | **LOC:** 180 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (79.4682%), Tech Debt (39.357%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 45`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 165`, `fragile_debt: 1`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` token, Test::More, separator, black, law, warnings, Util, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-ignore-dir.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.272 IQR)
- **Top Global Matches:** file_cluster_8: 12.272, file_cluster_0: 12.274, file_cluster_13: 12.377
- **Magnitude:** 165.52 | **LOC:** 231 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (80.0954%), Tech Debt (22.1507%)
**Top Internal Functions/Classes:**
  * `set_up_assertion_that_these_options_will` (Impact: 28.9 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 17`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 133`, `orphaned_logic: 1`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, strict, File::Spec
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/highlighting.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.84 IQR)
- **Top Global Matches:** file_cluster_17: 12.84, file_cluster_0: 12.954, file_cluster_13: 13.004
- **Magnitude:** 165.0 | **LOC:** 221 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (98.5936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_it` (Impact: 14.8 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 36`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 147`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, law, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-underline.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.832 IQR)
- **Top Global Matches:** file_cluster_0: 13.832, file_cluster_13: 13.902, file_cluster_8: 14.049
- **Magnitude:** 164.24 | **LOC:** 156 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.7987%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 27`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 147`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, law, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-passthru.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.612 IQR)
- **Top Global Matches:** file_cluster_8: 12.612, file_cluster_0: 12.617, file_cluster_13: 12.627
- **Magnitude:** 150.88 | **LOC:** 188 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (79.4541%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `color_match` (Impact: 9.1 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 42`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 139`
* *Architecture:* `io: 1`, `import: 5`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/range.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.784 IQR)
- **Top Global Matches:** file_cluster_13: 12.784, file_cluster_0: 12.837, file_cluster_17: 12.908
- **Magnitude:** 141.0 | **LOC:** 281 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (78.3959%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `foo` (Impact: 1.1 | O(N^1))
  * `bar` (Impact: 1.1 | O(N^1))
  * `foo` (Impact: 1.1 | O(N^1))
  * `bar` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 54`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 133`, `duplicate_logic: 4`
* *Architecture:* `import: 13`
* *Defense:* `safety: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` start, Test::More, warnings, Util, lib, range, strict, end
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/interactive.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.809 IQR)
- **Top Global Matches:** file_cluster_0: 12.809, file_cluster_13: 12.988, file_cluster_8: 13.072
- **Magnitude:** 136.1 | **LOC:** 138 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (85.2253%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 30`
* *Risk/State:* `state_mutation: 119`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, Term::ANSIColor, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-group.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.054 IQR)
- **Top Global Matches:** file_cluster_0: 13.054, file_cluster_13: 13.219, file_cluster_17: 13.442
- **Magnitude:** 127.72 | **LOC:** 110 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.4674%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 23`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 111`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, heading, warnings, Util, lib, break, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-output.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.05 IQR)
- **Top Global Matches:** file_cluster_0: 13.05, file_cluster_13: 13.353, file_cluster_17: 13.493
- **Magnitude:** 125.68 | **LOC:** 121 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.2456%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 109`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, warnings, Util, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/longopts.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.209 IQR)
- **Top Global Matches:** file_cluster_13: 12.209, file_cluster_8: 12.29, file_cluster_0: 12.775
- **Magnitude:** 119.6 | **LOC:** 162 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (67.1725%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 44`
* *Risk/State:* `state_mutation: 102`
* *Architecture:* `import: 10`
* *Defense:* `safety: 5`, `doc: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, snorgledork, warnings, Util, lib, upper, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/invalid-ackrc.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.768 IQR)
- **Top Global Matches:** file_cluster_17: 13.768, file_cluster_13: 13.807, file_cluster_0: 13.881
- **Magnitude:** 110.2 | **LOC:** 88 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 19`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 94`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` output, File::Temp, Test::More, warnings, Util, lib, strict, List::Util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/config-finder.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.797 IQR)
- **Top Global Matches:** file_cluster_0: 11.797, file_cluster_13: 12.009, file_cluster_8: 12.187
- **Magnitude:** 108.58 | **LOC:** 229 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (63.7337%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expect_ackrcs` (Impact: 22.0 | O(N^2) | DB: 6)
  * `no_home` (Impact: 3.2 | O(N^1) | DB: 2)
  * `with_home` (Impact: 3.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 46`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 77`
* *Architecture:* `import: 12`
* *Defense:* `safety: 3`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App::Ack::ConfigFinder, File::Temp, Test::More, project, Cwd, warnings, Test::Builder, Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/command-line-files.t` (PERL) | Magnitude: 54.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 39, indent_spaces: 23, branch: 22, structural_boundaries: 19
- `dev/linecount` (PERL) | Magnitude: 39.38 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, structural_boundaries: 10, branch: 9, indent_spaces: 8
- `t/Util.pm` (PERL) | Magnitude: 3699.42 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 835, state_mutation: 760, branch: 380, structural_boundaries: 297
- `dev/display-option-coverage.pl` (PERL) | Magnitude: 24.72 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 17, indent_spaces: 10, state_mutation: 9, structural_boundaries: 8
- `t/ack-type.t` (PERL) | Magnitude: 222.22 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 205, indent_spaces: 68, branch: 50, structural_boundaries: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/ack-w.t` (PERL) | Magnitude: 53.7 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 49, branch: 35, structural_boundaries: 23
- `dev/Cookbook.pm` (PERL) | Magnitude: 198.04 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 215, state_mutation: 176, bitwise_ops: 157, indent_spaces: 108
- `xt/man.t` (PERL) | Magnitude: 272.28 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 110, indent_spaces: 81, branch: 49, structural_boundaries: 31
- `t/ack-color.t` (PERL) | Magnitude: 195.58 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 178, indent_spaces: 91, structural_boundaries: 54, encapsulation: 47
- `t/ack-dump.t` (PERL) | Magnitude: 39.44 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 24, branch: 17, structural_boundaries: 11, indent_spaces: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dev/timings.pl` (PERL) | Magnitude: 338.42 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 251, state_mutation: 202, structural_boundaries: 90, branch: 88
- `t/ack-ignore-file.t` (PERL) | Magnitude: 52.34 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 36, branch: 21, structural_boundaries: 11
- `t/invalid-ackrc.t` (PERL) | Magnitude: 110.2 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 94, indent_spaces: 36, branch: 20, structural_boundaries: 19
- `t/ack-print0.t` (PERL) | Magnitude: 99.2 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 83, indent_spaces: 43, structural_boundaries: 26, encapsulation: 21
- `t/highlighting.t` (PERL) | Magnitude: 165.0 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 147, indent_spaces: 61, branch: 40, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/process-substitution.t` (PERL) | Magnitude: 51.84 | Delta: **0.33 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 17, concurrency: 12, structural_boundaries: 11
- `dev/linecount-fork` (PERL) | Magnitude: 63.74 | Delta: **0.407 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 30, indent_spaces: 23, concurrency: 18, branch: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/config-loader.t` (PERL) | Magnitude: 796.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 143, structural_boundaries: 60, branch: 52
- `t/ack-ignore-dir.t` (PERL) | Magnitude: 165.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 133, indent_spaces: 131, branch: 58, structural_boundaries: 17
- `t/ack-passthru.t` (PERL) | Magnitude: 150.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 139, indent_spaces: 56, structural_boundaries: 42, branch: 37
- `t/mutex-options.t` (PERL) | Magnitude: 357.6 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 299, indent_spaces: 96, sec_high_risk_execution: 52, structural_boundaries: 30
- `t/file-iterator.t` (PERL) | Magnitude: 25.0 | Delta: **0.293 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 102, state_mutation: 18, structural_boundaries: 14, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `t/swamp/Makefile` (MAKEFILE) | Magnitude: 10.52 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `t/Util.pm` -> Churn: **100.0%** | Cog Load: 95.6598% | Debt: 13.9159%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/Util.pm` -> **Dmitri Vereshchagin** (100.0% isolated ownership) | Magnitude: 3699.42

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/Util.pm` -> **Severity: 32.933** (Embedded: 0.3793 * Error Risk: 86.8243%)
- `ack` -> **Severity: 0.53** (Embedded: 0.0057 * Error Risk: 92.1991%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/Util.pm` -> **Severity: 8192.339** (Blast Radius: 246.184 * Doc Risk: 33.2773%)
- `t/ack-help.t` -> **Severity: 431.065** (Blast Radius: 4.311 * Doc Risk: 99.9919%)
- `xt/man.t` -> **Severity: 428.034** (Blast Radius: 4.311 * Doc Risk: 99.2888%)
- `t/file-permission.t` -> **Severity: 425.296** (Blast Radius: 4.311 * Doc Risk: 98.6537%)
- `t/needs-line-scan.t` -> **Severity: 424.251** (Blast Radius: 4.311 * Doc Risk: 98.4113%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
